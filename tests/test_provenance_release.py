"""Capture integrity and release/deposit mismatch regression tests (no network)."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

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
                capture_source.capture('https://example.test/paper.pdf', 'https://archive.test/paper.pdf')

    def test_html_hashes_archive_representation_not_live_page(self):
        live = b'<html>Current wording</html>'
        historical = b'<html>Archived wording</html>'
        with patch.object(capture_source, 'retrieve', side_effect=[(live, 'text/html'), (historical, 'text/html')]):
            data, metadata = capture_source.capture('https://example.test/policy', 'https://archive.test/20260507/policy')
        self.assertEqual(data, historical)
        self.assertEqual(metadata['sha256'], release.digest(historical)['sha256'])
        self.assertIsNotNone(metadata['archive_checked_on'])

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
