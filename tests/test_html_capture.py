"""Raw HTML representation, bounded completeness, and immutable retrieval checks."""
from contextlib import redirect_stderr, redirect_stdout
from email.message import Message
import gzip
import hashlib
from io import StringIO
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import capture_source as capture


PAYLOAD = (b'<html><body><article><h1>Policy</h1><p>We require 90% coverage, '
           b'except temporary testing.</p><table><tr><td>2 days</td></tr></table>'
           b'<p>Footnote: internal use only.</p></article></body></html>')
MARKERS = ['Policy', '90% coverage, except temporary testing.', '2 days',
           'Footnote: internal use only.']
REPLAY = 'https://web.archive.org/web/20261024010101/https://example.test/policy'
RAW = 'https://web.archive.org/web/20261024010101id_/https://example.test/policy'


class Response:
    def __init__(self, payload=PAYLOAD, *, length=None, encoding=None, status=200, final_url=RAW):
        self.payload = payload
        self.status = status
        self.final_url = final_url
        self.headers = Message()
        self.headers['Content-Type'] = 'text/html; charset=utf-8'
        self.headers['Content-Length'] = str(len(payload) if length is None else length)
        if encoding:
            self.headers['Content-Encoding'] = encoding

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def getcode(self):
        return self.status

    def geturl(self):
        return self.final_url

    def read(self):
        return self.payload


class HTMLCaptureTests(unittest.TestCase):
    def test_http_receipt_retains_final_url_and_exact_identity_body(self):
        with patch.object(capture, 'urlopen', return_value=Response()) as request:
            response = capture.retrieve(RAW)
        self.assertEqual(tuple(response), (PAYLOAD, 'text/html'))
        self.assertEqual(response.receipt['requested_url'], RAW)
        self.assertEqual(response.receipt['final_url'], RAW)
        self.assertEqual(response.receipt['status'], 200)
        self.assertIn(('Content-Length', str(len(PAYLOAD))), response.receipt['response_headers'])
        self.assertEqual(request.call_args.args[0].get_header('Accept-encoding'), 'identity')

    def test_unsupported_partial_and_truncated_responses_are_rejected(self):
        for response in [Response(encoding='br'), Response(encoding='gzip'),
                         Response(status=206), Response(length=len(PAYLOAD) + 1)]:
            with self.subTest(response=response), patch.object(capture, 'urlopen', return_value=response):
                with self.assertRaises(ValueError):
                    capture.retrieve(RAW)

    def test_gzip_response_is_retained_before_explicit_entity_decode(self):
        compressed = gzip.compress(PAYLOAD, mtime=0)
        with patch.object(capture, 'urlopen', return_value=Response(compressed, encoding='gzip')):
            response = capture.retrieve(RAW)
        self.assertEqual(response[0], PAYLOAD)
        self.assertEqual(response.response_body, compressed)
        self.assertEqual(response.receipt['response_body_sha256'], hashlib.sha256(compressed).hexdigest())
        self.assertEqual(response.receipt['decoded_entity_sha256'], hashlib.sha256(PAYLOAD).hexdigest())
        verify_args = ['--url', RAW, '--sha256', hashlib.sha256(PAYLOAD).hexdigest(),
                       '--byte-length', str(len(PAYLOAD)), '--expect-text', MARKERS[-1]]
        with patch.object(capture, 'urlopen', return_value=Response(compressed, encoding='gzip')), \
                redirect_stdout(StringIO()), patch.object(Path, 'open', side_effect=AssertionError('verification wrote a file')):
            self.assertEqual(capture.verify_main(verify_args), 0)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(capture, 'urlopen', return_value=Response(compressed, encoding='gzip')), \
                    patch.object(sys, 'argv', self.arguments(root, 'gzip_capture')), redirect_stdout(StringIO()):
                self.assertEqual(capture.main(), 0)
            receipt = json.loads((root / '.source-captures/retrievals/gzip_capture.json').read_text())
            body = receipt['retained_responses'][0]
            self.assertEqual((root / body['response_body_path']).read_bytes(), compressed)
            self.assertEqual((root / receipt['capture']['capture_path']).read_bytes(), PAYLOAD)
            self.assertEqual(receipt['capture']['sha256'], hashlib.sha256(PAYLOAD).hexdigest())

    def test_raw_mode_is_explicit_and_requires_capture_specific_wayback_url(self):
        self.assertEqual(capture.raw_archive_url(REPLAY), RAW)
        self.assertEqual(capture.raw_archive_url(RAW), RAW)
        for url in ['https://web.archive.org/web/2026/https://example.test',
                    'https://example.test/web/20261024010101/https://example.test']:
            with self.subTest(url=url), self.assertRaises(ValueError):
                capture.raw_archive_url(url)
        with patch.object(capture, 'retrieve', return_value=(PAYLOAD, 'text/html')) as request:
            capture.capture('https://example.test/policy', REPLAY)
        request.assert_called_once_with(REPLAY)

    def test_redirect_cannot_change_archive_timestamp_or_representation(self):
        capture.require_same_archive_selection(RAW, RAW.replace('/policy', '/canonical-policy'))
        for final in [REPLAY, RAW.replace('20261024010101', '20261025010101'),
                      'https://example.test/policy']:
            with self.subTest(final=final), self.assertRaisesRegex(ValueError, 'redirect changed'):
                capture.require_same_archive_selection(RAW, final)
            args = ['--url', RAW, '--sha256', hashlib.sha256(PAYLOAD).hexdigest(),
                    '--byte-length', str(len(PAYLOAD))]
            with patch.object(capture, 'urlopen', return_value=Response(final_url=final)), \
                    redirect_stderr(StringIO()):
                self.assertEqual(capture.verify_main(args), 1)
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(capture, 'urlopen', return_value=Response(final_url=REPLAY)), \
                    patch.object(sys, 'argv', self.arguments(Path(directory), 'bad_redirect')), \
                    redirect_stderr(StringIO()):
                self.assertEqual(capture.main(), 1)
            self.assertFalse((Path(directory) / '.source-captures').exists())

    def test_completeness_checks_numbers_qualifications_tables_and_footnotes(self):
        self.assertEqual(capture.check_completeness(PAYLOAD, 'text/html', MARKERS)['status'],
                         'selected_markers_present')
        for missing in [b'90%', b'except temporary testing.', b'2 days', b'Footnote: internal use only.']:
            with self.subTest(missing=missing), self.assertRaisesRegex(ValueError, 'text missing'):
                capture.check_completeness(PAYLOAD.replace(missing, b''), 'text/html', MARKERS)
        with self.assertRaisesRegex(ValueError, 'closing tag'):
            capture.check_completeness(PAYLOAD[:-7], 'text/html', MARKERS)
        scripted = b'<html><script>{"claim":"90% coverage"}</script>Incomplete article</html>'
        with self.assertRaisesRegex(ValueError, 'text missing'):
            capture.check_completeness(scripted, 'text/html', ['90% coverage'])
        self.assertEqual(capture.check_completeness(PAYLOAD, 'text/html', [])['status'], 'not_checked')

    def arguments(self, root, capture_id):
        return ['capture_source.py', '--root', str(root), '--original-url', 'https://example.test/policy',
                '--archive-url', REPLAY, '--raw-archive', '--id', capture_id, '--record-id', 'policy',
                '--locator-basis', 'Article headings', '--inspection-scope', 'Selected policy passages',
                '--preservation-note', 'New retrieval; historical fingerprint unchanged',
                '--expect-text', MARKERS[-1]]

    def test_retrievals_get_distinct_receipts_and_existing_bytes_are_not_rewritten(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(capture, 'urlopen', return_value=Response()):
                for capture_id in ['policy_new_1', 'policy_new_2']:
                    with patch.object(sys, 'argv', self.arguments(root, capture_id)), redirect_stdout(StringIO()):
                        self.assertEqual(capture.main(), 0)
                    if capture_id == 'policy_new_1':
                        payload_path = root / '.source-captures' / (hashlib.sha256(PAYLOAD).hexdigest() + '.html')
                        first_mtime = payload_path.stat().st_mtime_ns
                self.assertEqual(payload_path.stat().st_mtime_ns, first_mtime)
                receipt_path = root / '.source-captures/retrievals/policy_new_1.json'
                before = receipt_path.read_bytes()
                receipt = json.loads(before)
                self.assertEqual(receipt['capture']['archive_url'], RAW)
                self.assertEqual(receipt['representation'], 'wayback_identity_body')
                self.assertEqual(receipt['response']['requested_url'], RAW)
                with patch.object(sys, 'argv', self.arguments(root, 'policy_new_1')), \
                        redirect_stderr(StringIO()), patch.object(capture, 'retrieve') as request:
                    self.assertEqual(capture.main(), 1)
                request.assert_not_called()
                self.assertEqual(receipt_path.read_bytes(), before)
            # Canonical historical IDs cannot be reused even without a sidecar.
            history = root / 'research/cyber-deployment/evidence.yaml'
            history.parent.mkdir(parents=True)
            history.write_text('snapshots:\n- id: historical_policy\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'historical'):
                capture.new_receipt_path(root, 'historical_policy')

    def test_verify_has_no_write_path_and_rejects_wrong_fingerprint(self):
        args = ['--url', RAW, '--sha256', hashlib.sha256(PAYLOAD).hexdigest(),
                '--byte-length', str(len(PAYLOAD)), '--expect-text', MARKERS[-1]]
        with patch.object(capture, 'urlopen', return_value=Response()), redirect_stdout(StringIO()) as output:
            self.assertEqual(capture.verify_main(args), 0)
        self.assertEqual(json.loads(output.getvalue())['verification'], 'matched')
        args[3] = '0' * 64
        with patch.object(capture, 'urlopen', return_value=Response()), redirect_stderr(StringIO()):
            self.assertEqual(capture.verify_main(args), 1)


if __name__ == '__main__':
    unittest.main()
