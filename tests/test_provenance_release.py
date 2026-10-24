"""Capture integrity and release/deposit mismatch regression tests (no network)."""
from copy import deepcopy
from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build
import build_commitments
import capture_source
import release
import source_provenance


class CaptureTests(unittest.TestCase):
    def test_pdf_digest_covers_exact_bytes_and_archive_must_match(self):
        payload = b'%PDF-1.7\r\n\x00\xffexact original bytes\r\n'
        with patch.object(capture_source, 'retrieve', return_value=(payload, 'application/pdf')):
            data, metadata = capture_source.capture('https://example.test/paper.pdf')
        self.assertEqual(data, payload)
        self.assertEqual(release.digest(payload), {key: metadata[key] for key in ('sha256', 'byte_length')})
        with patch.object(capture_source, 'retrieve', side_effect=[(payload, 'application/pdf'),
                                                                  (payload.replace(b'\r\n', b'\n'), 'application/pdf')]):
            with self.assertRaisesRegex(ValueError, 'does not match'):
                capture_source.capture('https://example.test/paper.pdf', 'https://archive.test/paper.pdf',
                                       compare_original=True)

    def test_html_hashes_archive_representation_not_live_page(self):
        historical = b'<html>Archived wording</html>'
        with patch.object(capture_source, 'retrieve', return_value=(historical, 'text/html')) as retrieve:
            data, metadata = capture_source.capture('https://example.test/policy', 'https://archive.test/20260507/policy')
        retrieve.assert_called_once_with('https://archive.test/20260507/policy')
        self.assertEqual(data, historical)
        self.assertEqual(metadata['sha256'], release.digest(historical)['sha256'])
        self.assertIsNotNone(metadata['archive_checked_on'])
        self.assertIn('original was not retrieved or compared', metadata['capture_basis'])

    def test_archive_recovery_does_not_contact_missing_original(self):
        original = 'https://example.test/disappeared'
        archive = 'https://archive.test/capture/disappeared'
        failures = [HTTPError(original, 404, 'Not Found', None, None),
                    HTTPError(original, 403, 'Forbidden', None, None),
                    URLError('host no longer resolves')]
        for payload, mime in [(b'%PDF-1.7\r\n\x00\xffarchived bytes', 'application/pdf'),
                              (b'<html>Archived policy</html>', 'text/html')]:
            for failure in failures:
                with self.subTest(mime=mime, failure=failure):
                    def retrieve(url):
                        if url == original:
                            raise failure
                        self.assertEqual(url, archive)
                        return payload, mime
                    with patch.object(capture_source, 'retrieve', side_effect=retrieve) as request:
                        data, metadata = capture_source.capture(original, archive)
                    request.assert_called_once_with(archive)
                    self.assertEqual(data, payload)
                    self.assertEqual(metadata['original_url'], original)
                    self.assertEqual(metadata['archive_url'], archive)
                    self.assertEqual(metadata['sha256'], release.digest(payload)['sha256'])
                    self.assertEqual(metadata['byte_length'], len(payload))

    def test_original_comparison_is_explicit_and_requires_matching_pdfs(self):
        payload = b'%PDF-1.7\nArchived document'
        with patch.object(capture_source, 'retrieve', return_value=(payload, 'application/pdf')) as request:
            _, metadata = capture_source.capture('https://example.test/paper.pdf',
                                                  'https://archive.test/paper.pdf', compare_original=True)
        self.assertEqual([args.args[0] for args in request.call_args_list],
                         ['https://archive.test/paper.pdf', 'https://example.test/paper.pdf'])
        self.assertIn('matched byte for byte', metadata['capture_basis'])
        with patch.object(capture_source, 'retrieve') as request:
            with self.assertRaisesRegex(ValueError, 'requires --archive-url'):
                capture_source.capture('https://example.test/paper.pdf', compare_original=True)
            with self.assertRaisesRegex(ValueError, 'distinct'):
                capture_source.capture('https://example.test/paper.pdf', 'https://example.test/paper.pdf')
            request.assert_not_called()
        with patch.object(capture_source, 'retrieve', return_value=(b'<html>Policy</html>', 'text/html')):
            with self.assertRaisesRegex(ValueError, 'only verifies PDF'):
                capture_source.capture('https://example.test/policy', 'https://archive.test/policy',
                                       compare_original=True)

    def test_cli_retains_archive_bytes_and_emits_valid_evidence_draft(self):
        for payload, mime, extension in [(b'%PDF-1.7\r\n\x00\xffretained PDF', 'application/pdf', '.pdf'),
                                          (b'<html>Retained policy</html>', 'text/html', '.html')]:
            with self.subTest(mime=mime), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                arguments = ['capture_source.py', '--root', directory,
                             '--original-url', 'https://example.test/disappeared',
                             '--archive-url', 'https://archive.test/capture/disappeared',
                             '--id', 'recovered_policy', '--record-id', 'policy_fixture',
                             '--locator-basis', 'Locations in the retained archive representation',
                             '--inspection-scope', 'Archived policy provision',
                             '--preservation-note', 'Original unavailable; archive inspected']
                output = StringIO()
                with patch.object(sys, 'argv', arguments), redirect_stdout(output), \
                        patch.object(capture_source, 'retrieve', return_value=(payload, mime)) as request:
                    self.assertEqual(capture_source.main(), 0)
                request.assert_called_once_with('https://archive.test/capture/disappeared')
                item = yaml.safe_load(output.getvalue())
                self.assertEqual((root / item['capture_path']).read_bytes(), payload)
                self.assertTrue(item['capture_path'].endswith(extension))
                self.assertEqual(item['sha256'], release.digest(payload)['sha256'])
                self.assertIn('original was not retrieved or compared', item['capture_basis'])
                research = root / build_commitments.DIRECTORY
                research.mkdir(parents=True)
                (research / 'evidence.yaml').write_text(yaml.safe_dump({
                    'schema_version': 'cyber-commitment-evidence-v2', 'snapshots': [item]}), encoding='utf-8')
                snapshots = build_commitments.read_items(root, 'evidence.yaml',
                    'cyber-commitment-evidence-v2', 'snapshots',
                    build_commitments.SNAPSHOT_REQUIRED, build_commitments.SNAPSHOT_OPTIONAL)
                self.assertEqual(snapshots['recovered_policy'], item)

    def test_error_page_is_not_pdf_and_legacy_exception_is_frozen(self):
        with self.assertRaisesRegex(ValueError, 'expected PDF'):
            source_provenance.check_payload(b'<html>Access denied</html>', 'application/pdf')
        snapshots, _ = build_commitments.load_history(ROOT)
        item = deepcopy(next(iter(snapshots.values())))
        item['preservation_note'] += ' Unreviewed change.'
        with self.assertRaisesRegex(ValueError, 'frozen'):
            source_provenance.validate(item, build_commitments.check_date, build_commitments.check_url)


class ReleaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temporary.name) / 'repo'
        shutil.copytree(ROOT, cls.root, ignore=shutil.ignore_patterns('.git', 'dist', '__pycache__', '.source-captures'))
        build.build(cls.root)
        history, _ = build_commitments.generate_history(cls.root)
        (cls.root / build_commitments.OUTPUT).write_bytes(history.encode())
        cls.run_git('init')
        cls.run_git('add', '.')
        cls.run_git('-c', 'user.name=Release Test', '-c', 'user.email=fixture@example.test', 'commit', '-m', 'fixture')
        cls.run_git('tag', 'test-v1')
        cls.target = release.prepare(cls.root, 'test-v1', Path(cls.temporary.name) / 'release')
        cls.manifest = json.loads(cls.target.read_text())
        cls.payload = (cls.target.parent / cls.manifest['payload']['path']).read_bytes()

    @classmethod
    def tearDownClass(cls):
        # Git object files are read-only on Windows; shutil needs a permission reset.
        def writable(function, path, error):
            import os
            os.chmod(path, 0o700)
            function(path)
        shutil.rmtree(Path(cls.temporary.name), onerror=writable)
        cls.temporary.cleanup()

    @classmethod
    def run_git(cls, *args):
        return subprocess.check_output(['git', '-C', str(cls.root), *args], stderr=subprocess.PIPE)

    def test_package_is_deterministic_and_binds_commit_authorities_outputs(self):
        release.verify(self.manifest, self.payload, self.root)
        files = release.inventory(self.root, self.manifest['github_commit'])
        self.assertEqual(release.package(files), self.payload)
        self.assertEqual(self.manifest['osf']['status'], 'synchronization_unconfirmed')
        self.assertFalse(self.manifest['preservation']['longitudinal_ready'])
        for path in release.AUTHORITIES:
            self.assertEqual(next(item for item in self.manifest['files'] if item['path'] == path)['role'], 'authoritative_yaml')

    def test_tampered_zip_hash_inventory_and_repointed_tag_fail(self):
        with self.assertRaisesRegex(ValueError, 'hash'):
            release.verify(self.manifest, self.payload + b'changed')
        modified = deepcopy(self.manifest)
        modified['files'][0]['sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'file mismatch'):
            release.verify(modified, self.payload)
        modified = deepcopy(self.manifest)
        modified['files'].pop()
        with self.assertRaisesRegex(ValueError, 'inventory|lacks required'):
            release.verify(modified, self.payload)
        modified = deepcopy(self.manifest)
        modified['github_commit'] = '0' * 40
        with self.assertRaisesRegex(ValueError, 'tag'):
            release.verify(modified, self.payload, self.root)

    def test_stale_output_fails_before_packaging(self):
        files = release.inventory(self.root, self.manifest['github_commit'])
        files['views/index.md'] += b'Manual edit.\n'
        with self.assertRaisesRegex(ValueError, 'stale'):
            release.validate_payload(files)

    def test_osf_receipt_requires_version_object_project_and_identical_bytes(self):
        url = 'https://files.osf.io/v1/resources/9ks5m/providers/osfstorage/object123?version=2'
        verified = release.record_osf(self.manifest, 'object123', '2', url, self.payload)
        self.assertEqual(verified['osf']['version_id'], '2')
        self.assertEqual(verified['osf']['sha256'], self.manifest['payload']['sha256'])
        self.assertEqual(self.manifest['osf']['status'], 'synchronization_unconfirmed')
        for bad in [url.replace('?version=2', ''), url.replace('9ks5m', 'wrong'), url.replace('object123', 'other'), url.replace('version=2', 'version=3')]:
            with self.subTest(url=bad), self.assertRaises(ValueError):
                release.record_osf(self.manifest, 'object123', '2', bad, self.payload)
        with self.assertRaisesRegex(ValueError, 'hash'):
            release.record_osf(self.manifest, 'object123', '2', url, self.payload + b'wrong')

    def test_osf_metadata_must_confirm_project_and_version(self):
        version = {'data': {'id': '2', 'type': 'file_versions', 'attributes': {'size': len(self.payload)}}}
        file = {'data': {'id': 'object123', 'relationships': {'node': {'links': {'related': {'href': 'https://api.osf.io/v2/nodes/9ks5m/'}}}}}}
        with patch.object(release, 'fetch_json', side_effect=[version, file]):
            receipt = release.verify_osf_metadata('object123', '2', len(self.payload))
        self.assertIn('/versions/2/', receipt['version_api_url'])
        version['data']['id'] = '3'
        with patch.object(release, 'fetch_json', side_effect=[version, file]):
            with self.assertRaisesRegex(ValueError, 'metadata'):
                release.verify_osf_metadata('object123', '2', len(self.payload))

    def test_github_requires_matching_published_tag_and_downloaded_asset(self):
        ref = {'object': {'type': 'commit', 'sha': self.manifest['github_commit']}}
        published = {'id': 123, 'draft': False, 'assets': [{'id': 456,
                     'name': self.manifest['payload']['path'], 'browser_download_url': 'https://github.com/fixture/download'}]}
        from io import BytesIO
        with patch.object(release, 'fetch_json', side_effect=[ref, published]), \
                patch.object(release, 'urlopen', return_value=BytesIO(self.payload)):
            receipt = release.verify_github(self.manifest)
        self.assertEqual(receipt['github_asset_id'], '456')
        ref['object']['sha'] = '0' * 40
        with patch.object(release, 'fetch_json', side_effect=[ref, published]):
            with self.assertRaisesRegex(ValueError, 'does not match'):
                release.verify_github(self.manifest)


if __name__ == '__main__':
    unittest.main()
