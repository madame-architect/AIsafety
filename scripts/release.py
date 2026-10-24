#!/usr/bin/env python3
"""Prepare an exact-tag release, verify its inventory, and record OSF byte verification.

The release manifest is outside the immutable ZIP to avoid self-reference.
Publication/upload are explicit maintainer actions; preparation never means synced.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit, parse_qs
from urllib.request import Request, urlopen
import zipfile

sys.dont_write_bytecode = True
import build
import build_commitments

AUTHORITIES = {'records.yaml', 'research/cyber-deployment/evidence.yaml',
               'research/cyber-deployment/commitments.yaml',
               'research/cyber-deployment/datasets.yaml',
               'research/cyber-deployment/dataset-links.yaml',
               'research/cyber-deployment/operational-risk/assumptions.yaml',
               'research/cyber-deployment/operational-risk/source-admission.yaml',
               'research/cyber-deployment/operational-risk/source-captures.yaml',
               'research/cyber-deployment/operational-risk/risk-evidence.yaml'}
GENERATED = {'frontier-governance-evals.bib', 'views/contextual.bib',
             'views/governance-artifacts.bib', 'views/technical-evals.bib',
             'views/index.md', 'research/cyber-deployment/commitment-history.md',
             'research/cyber-deployment/longitudinal-map.md',
             'research/cyber-deployment/operational-risk/evidence-map.md'}


def digest(data: bytes) -> dict:
    return {'sha256': hashlib.sha256(data).hexdigest(), 'byte_length': len(data)}


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(['git', '-C', str(root), *args], stderr=subprocess.PIPE)


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def tag_commit(root: Path, tag: str) -> str:
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', tag):
        raise ValueError('use a simple release tag containing letters, digits, dots, hyphens or underscores')
    return git(root, 'rev-parse', '--verify', f'refs/tags/{tag}^{{commit}}').decode().strip()


def inventory(root: Path, commit: str) -> dict[str, bytes]:
    result = {}
    for entry in git(root, 'ls-tree', '-r', '-z', commit).split(b'\0'):
        if not entry:
            continue
        info, raw_path = entry.split(b'\t', 1)
        mode, kind, sha = info.decode().split()
        path = raw_path.decode('utf-8')
        if kind != 'blob' or mode not in {'100644', '100755'}:
            raise ValueError(f'unsupported release entry: {path}')
        if Path(path).is_absolute() or '..' in Path(path).parts or '\\' in path:
            raise ValueError(f'unsafe release path: {path}')
        result[path] = git(root, 'cat-file', 'blob', sha)
    if not AUTHORITIES | GENERATED <= result.keys():
        raise ValueError('release is missing authoritative YAML or generated outputs')
    return result


def validate_payload(files: dict[str, bytes]) -> dict:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        for path, payload in files.items():
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
        outputs, _ = build.generate_outputs(root)
        history, _ = build_commitments.generate_history(root)
        outputs[build_commitments.OUTPUT] = history
        for path, expected in outputs.items():
            if files.get(path.as_posix()) != expected.encode():
                raise ValueError(f'generated output is missing or stale at release commit: {path}')
        for script in ('research/cyber-deployment/operational-risk/build.py',
                       'scripts/build_cyber_datasets.py', 'scripts/audit_cyber_bibliography.py'):
            flags = [] if script.endswith('audit_cyber_bibliography.py') else ['--check']
            result = subprocess.run([sys.executable, '-B', str(root / script), *flags],
                                    cwd=root, capture_output=True, text=True)
            if result.returncode:
                raise ValueError(f'linked dataset validation failed: {script}: {result.stdout}{result.stderr}')
        snapshots, _ = build_commitments.load_history(root)
    legacy = sorted(key for key, item in snapshots.items() if item['preservation_status'] == 'legacy_uncaptured')
    unarchived = sorted(key for key, item in snapshots.items()
                        if item['preservation_status'] == 'captured' and item['archive_url'] is None)
    return {'legacy_uncaptured_snapshot_ids': legacy, 'unarchived_snapshot_ids': unarchived,
            'longitudinal_ready': not (legacy or unarchived)}


def package(files: dict[str, bytes]) -> bytes:
    stream = BytesIO()
    # Fixed ZIP metadata and no compression make packaging reproducible across zlib versions.
    with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_STORED) as archive:
        for path, data in sorted(files.items()):
            info = zipfile.ZipInfo(path, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return stream.getvalue()


def write_json(path: Path, data: dict) -> None:
    path.write_bytes((json.dumps(data, indent=2, ensure_ascii=False) + '\n').encode())


def prepare(root: Path, tag: str, output: Path) -> Path:
    commit = tag_commit(root, tag)
    files = inventory(root, commit)
    # Use the release commit's actual code, not a different checkout's builders.
    for path in ['scripts/build.py', 'scripts/build_commitments.py',
                 'scripts/lint_bibliography.py', 'scripts/source_provenance.py', 'scripts/release.py']:
        if (root / path).read_bytes() != files.get(path):
            raise ValueError(f'checkout must use the release commit tooling: {path}')
    preservation = validate_payload(files)
    payload = package(files)
    manifest = dict(schema_version='frontier-release-v1', project='Frontier AI Governance Evals',
                    prepared_at=now(), github_commit=commit, github_tag=tag,
                    github_release_url=f'https://github.com/madame-architect/AIsafety/releases/tag/{tag}',
                    github_status='publication_unconfirmed',
                    payload=dict(path=f'{tag}.zip', **digest(payload)),
                    files=[dict(path=path, role='authoritative_yaml' if path in AUTHORITIES else
                                'generated_output' if path in GENERATED else 'supporting', **digest(data))
                           for path, data in sorted(files.items())],
                    preservation=preservation,
                    osf=dict(project_url='https://osf.io/9ks5m/', status='synchronization_unconfirmed',
                             object_id=None, version_id=None, download_url=None,
                             verified_at=None, sha256=None, byte_length=None))
    output.mkdir(parents=True, exist_ok=True)
    target = output / f'{tag}-manifest.json'
    if target.exists() or (output / manifest['payload']['path']).exists():
        raise ValueError('release files already exist; verify them rather than overwriting evidence')
    (output / manifest['payload']['path']).write_bytes(payload)
    write_json(target, manifest)
    return target


def verify(manifest: dict, data: bytes, root: Path | None = None) -> None:
    if manifest.get('schema_version') != 'frontier-release-v1':
        raise ValueError('unsupported release manifest schema')
    if any(manifest['payload'][key] != value for key, value in digest(data).items()):
        raise ValueError('release ZIP hash or byte length mismatch')
    expected = {item['path']: item for item in manifest['files']}
    if len(expected) != len(manifest['files']) or not AUTHORITIES | GENERATED <= expected.keys():
        raise ValueError('manifest has duplicate paths or lacks required release files')
    with zipfile.ZipFile(BytesIO(data)) as archive:
        if len(archive.namelist()) != len(expected) or set(archive.namelist()) != expected.keys():
            raise ValueError('ZIP inventory differs from manifest')
        files = {path: archive.read(path) for path in expected}
    for path, payload in files.items():
        if any(expected[path][key] != value for key, value in digest(payload).items()):
            raise ValueError(f'manifest file mismatch: {path}')
        role = 'authoritative_yaml' if path in AUTHORITIES else 'generated_output' if path in GENERATED else 'supporting'
        if expected[path].get('role') != role:
            raise ValueError(f'manifest role mismatch: {path}')
    if root is not None:
        if tag_commit(root, manifest['github_tag']) != manifest['github_commit']:
            raise ValueError('Git tag no longer resolves to the manifest commit')
        if inventory(root, manifest['github_commit']) != files:
            raise ValueError('release files differ from the specified Git commit')


def record_osf(manifest: dict, object_id: str, version_id: str,
               download_url: str, downloaded: bytes) -> dict:
    # Require an OSF version-pinned download, not a mutable latest URL.
    parsed = urlsplit(download_url)
    query = parse_qs(parsed.query)
    expected_path = f'/v1/resources/9ks5m/providers/osfstorage/{object_id}'
    if (parsed.scheme != 'https' or parsed.hostname != 'files.osf.io' or
            parsed.path.rstrip('/') != expected_path or parsed.fragment or parsed.username or parsed.port or
            query.get('version') != [version_id]):
        raise ValueError('use the OSF Storage download URL for project 9ks5m and the object, pinned with ?version=<version_id>')
    if not re.fullmatch(r'[A-Za-z0-9_-]+', object_id) or not re.fullmatch(r'[1-9][0-9]*', version_id):
        raise ValueError('supply the actual OSF object identifier and positive version number')
    verify(manifest, downloaded)
    result = json.loads(json.dumps(manifest))
    result['osf'] = dict(project_url='https://osf.io/9ks5m/', status='deposit_bytes_verified',
                         object_id=object_id, version_id=version_id, download_url=download_url,
                         verified_at=now(), **digest(downloaded))
    return result


def fetch_json(url: str) -> dict:
    request = Request(url, headers={'Accept': 'application/json', 'User-Agent': 'FrontierGovernanceEvals/1.0'})
    with urlopen(request, timeout=60) as response:
        return json.load(response)


def verify_osf_metadata(object_id: str, version_id: str, byte_length: int) -> dict:
    url = f'https://api.osf.io/v2/files/{object_id}/versions/{version_id}/'
    version = fetch_json(url)['data']
    file = fetch_json(f'https://api.osf.io/v2/files/{object_id}/')['data']
    node = file['relationships']['node']['links']['related']['href'].rstrip('/')
    if (version['id'] != version_id or version['type'] != 'file_versions' or
            version['attributes']['size'] != byte_length or file['id'] != object_id or
            node != 'https://api.osf.io/v2/nodes/9ks5m'):
        raise ValueError('OSF metadata does not identify the expected project, object, version and length')
    return {'object_api_url': f'https://api.osf.io/v2/files/{object_id}/', 'version_api_url': url}


def verify_github(manifest: dict) -> dict:
    base = 'https://api.github.com/repos/madame-architect/AIsafety'
    tag = manifest['github_tag']
    ref = fetch_json(f'{base}/git/ref/tags/{tag}')['object']
    # Follow annotated tags; reject unexpected object kinds and cycles.
    visited = set()
    while ref['type'] == 'tag':
        if ref['sha'] in visited:
            raise ValueError('cyclic Git tag object')
        visited.add(ref['sha'])
        ref = fetch_json(f"{base}/git/tags/{ref['sha']}")['object']
    release = fetch_json(f'{base}/releases/tags/{tag}')
    if ref['type'] != 'commit' or ref['sha'] != manifest['github_commit'] or release['draft']:
        raise ValueError('published GitHub release/tag does not match the manifest commit')
    asset = next((asset for asset in release['assets'] if asset['name'] == manifest['payload']['path']), None)
    if not asset:
        raise ValueError('published GitHub release is missing the release ZIP asset')
    with urlopen(asset['browser_download_url'], timeout=60) as response:
        verify(manifest, response.read())
    return {'github_status': 'release_bytes_verified', 'github_release_id': str(release['id']),
            'github_asset_id': str(asset['id']), 'github_verified_at': now()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest='command', required=True)
    create = commands.add_parser('prepare')
    create.add_argument('--tag', required=True)
    create.add_argument('--output-dir', type=Path, default=Path('dist'))
    check = commands.add_parser('verify')
    check.add_argument('manifest', type=Path)
    github = commands.add_parser('record-github')
    github.add_argument('manifest', type=Path)
    record = commands.add_parser('record-osf')
    record.add_argument('manifest', type=Path)
    record.add_argument('--object-id', required=True)
    record.add_argument('--version-id', required=True)
    record.add_argument('--download-url', required=True)
    args = parser.parse_args()
    try:
        if args.command == 'prepare':
            print(prepare(args.root, args.tag, args.output_dir))
        else:
            manifest = json.loads(args.manifest.read_text(encoding='utf-8'))
            payload = args.manifest.parent / manifest['payload']['path']
            if payload.name != manifest['payload']['path']:
                raise ValueError('payload path must be a basename next to the manifest')
            verify(manifest, payload.read_bytes(), args.root)
            if args.command == 'record-osf':
                # URL validation precedes the network request. Verification is repeated after download.
                record_osf(manifest, args.object_id, args.version_id, args.download_url, payload.read_bytes())
                identifiers = verify_osf_metadata(args.object_id, args.version_id, manifest['payload']['byte_length'])
                request = Request(args.download_url, headers={'Accept-Encoding': 'identity'})
                with urlopen(request, timeout=60) as response:
                    deposited = response.read()
                manifest = record_osf(manifest, args.object_id, args.version_id, args.download_url, deposited)
                manifest['osf'].update(identifiers)
                write_json(args.manifest, manifest)
                print('OSF deposited bytes verified; publish this updated manifest to both release locations.')
            elif args.command == 'record-github':
                manifest.update(verify_github(manifest))
                write_json(args.manifest, manifest)
                print('Published GitHub tag, release and ZIP asset verified; retain the updated manifest.')
            else:
                print('Release ZIP, authoritative YAML, outputs and Git tag match the manifest.')
        return 0
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError, zipfile.BadZipFile) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
