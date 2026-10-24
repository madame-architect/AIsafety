#!/usr/bin/env python3
"""Validate canonical cyber-source identities, preservation metadata and retained bytes.

No network requests. Missing optional cache files are reported, not invented.
Use --require-capture-files after restoring the retained capture bundle to check
all captured policy/evidence payloads. Legacy DeepMind gaps stay explicit.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import yaml
import build_commitments as history
import source_provenance as provenance

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = Path('research/cyber-deployment/operational-risk')


def keyed(items: object, field: str, label: str) -> dict[str, dict]:
    if not isinstance(items, list):
        raise ValueError(f'{label}: expected list')
    result = {}
    for item in items:
        if not isinstance(item, dict):
            raise ValueError(f'{label}: expected mapping')
        key = history.string(item.get(field), f'{label}.{field}')
        if key in result:
            raise ValueError(f'{label}: duplicate {field} {key}')
        result[key] = item
    return result


def check_bytes(item: dict, root: Path, required: bool) -> bool:
    relative = item.get('capture_path')
    if not relative:
        if required:
            raise ValueError(f"{item['id']}: missing capture_path")
        return False
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"{item['id']}: capture_path escapes repository")
    if not path.is_file():
        if required:
            raise ValueError(f"{item['id']}: retained capture file missing: {relative}")
        return False
    payload = path.read_bytes()
    if len(payload) != item['byte_length'] or hashlib.sha256(payload).hexdigest() != item['sha256']:
        raise ValueError(f"{item['id']}: capture SHA-256 or byte length mismatch")
    provenance.check_payload(payload, item['mime_type'])
    return True


def validate_documents(records: dict, admission: dict, capture_doc: dict, root: Path,
                       *, require_capture_files: bool = False) -> dict[str, int]:
    by_record = keyed(records.get('records'), 'id', 'records.yaml')
    sources = keyed(admission.get('sources'), 'source_id', 'source-admission.yaml')
    if capture_doc.get('schema_version') != 'cyber-operational-source-captures-v1':
        raise ValueError('source-captures.yaml: unsupported schema_version')
    captures = keyed(capture_doc.get('snapshots'), 'id', 'source-captures.yaml')
    used = set()
    counts = dict(accepted_sources=0, canonical_sources=0, operational_captures=0, payloads_checked=0)
    for source_id, source in sources.items():
        if source.get('research_admission') != 'accepted':
            continue
        counts['accepted_sources'] += 1
        if source.get('bibliography_admission') != 'accepted':
            if not source.get('bibliography_exception', '').strip():
                raise ValueError(f'{source_id}: unadmitted bibliography requires bibliography_exception')
            continue
        record_id = source.get('record_id')
        if record_id not in by_record:
            raise ValueError(f'{source_id}: missing canonical record_id {record_id!r}')
        fields = by_record[record_id]['fields']
        if fields.get('title') != source.get('title') or fields.get('url') != source.get('primary_url'):
            raise ValueError(f'{source_id}: canonical title/URL mismatch')
        if source.get('arxiv_id') and (fields.get('eprint') != source['arxiv_id'] or
                                      fields.get('version') != source.get('inspected_version')):
            raise ValueError(f'{source_id}: canonical arXiv identity/version mismatch')
        counts['canonical_sources'] += 1
        if source.get('preservation_status') != 'captured':
            if not source.get('preservation_note', '').strip():
                raise ValueError(f'{source_id}: uncaptured source requires preservation_note')
            continue
        capture_id = source.get('capture_id')
        if capture_id not in captures or capture_id in used:
            raise ValueError(f'{source_id}: missing or reused capture_id')
        used.add(capture_id)
        item = captures[capture_id]
        history.mapping(item, history.SNAPSHOT_REQUIRED | {'source_id'},
                        history.SNAPSHOT_OPTIONAL, capture_id)
        for field, value in item.items():
            if field == 'byte_length' or (field in provenance.NULLABLE and value is None):
                continue
            history.string(value, f'{capture_id}.{field}')
        if item['source_id'] != source_id or item['record_id'] != record_id:
            raise ValueError(f'{capture_id}: source/record identity mismatch')
        if item['original_url'] != source['primary_url']:
            raise ValueError(f'{capture_id}: original URL mismatch')
        if item['preservation_status'] != 'captured':
            raise ValueError(f'{capture_id}: new evidence capture cannot use a legacy exception')
        history.check_date(item['observed_on'], f'{capture_id}.observed_on')
        provenance.validate(item, history.check_date, history.check_url)
        if source.get('inspected_version') and item['version_claim'] != source['inspected_version']:
            raise ValueError(f'{capture_id}: captured version mismatch')
        counts['operational_captures'] += 1
        counts['payloads_checked'] += check_bytes(item, root, require_capture_files)
    if used != set(captures):
        raise ValueError(f'unreferenced source captures: {sorted(set(captures) - used)}')
    return counts


def audit(root: Path, *, require_capture_files: bool = False) -> dict[str, int]:
    def read(path: Path) -> dict:
        value = yaml.safe_load(path.read_text(encoding='utf-8'))
        if not isinstance(value, dict):
            raise ValueError(f'{path}: expected mapping')
        return value
    counts = validate_documents(read(root / 'records.yaml'),
                                read(root / DIRECTORY / 'source-admission.yaml'),
                                read(root / DIRECTORY / 'source-captures.yaml'), root,
                                require_capture_files=require_capture_files)
    snapshots, _ = history.load_history(root)
    counts['policy_captures'] = 0
    counts['legacy_uncaptured'] = 0
    for item in snapshots.values():
        if item['preservation_status'] == 'legacy_uncaptured':
            counts['legacy_uncaptured'] += 1
            continue
        counts['policy_captures'] += 1
        counts['payloads_checked'] += check_bytes(item, root, require_capture_files)
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--require-capture-files', action='store_true')
    args = parser.parse_args()
    try:
        c = audit(args.root, require_capture_files=args.require_capture_files)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1
    print(f"Validated {c['canonical_sources']}/{c['accepted_sources']} canonical sources, "
          f"{c['operational_captures']} operational captures, {c['policy_captures']} policy captures; "
          f"checked {c['payloads_checked']} local payloads; "
          f"{c['legacy_uncaptured']} explicit legacy capture gaps.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
