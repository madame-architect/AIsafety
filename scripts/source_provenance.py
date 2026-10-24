"""Validation shared by source capture and the documentary-history build."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import re

FIELDS = {
    'original_url', 'retrieved_at', 'archive_url', 'archive_checked_on', 'sha256',
    'byte_length', 'mime_type', 'published_on', 'version_claim', 'locator_basis',
    'preservation_status',
}
NULLABLE = {'retrieved_at', 'archive_url', 'archive_checked_on', 'sha256',
            'byte_length', 'mime_type', 'published_on', 'version_claim'}
# Exact migrated records only. This is not a date-based exemption for new data.
LEGACY = {
    'deepmind_fsf_3_0_observed_2026_10_17': '07d9cb375d1818dbb7d5022a331d92d075eb74ef8444b7fdbb0e7847e4350098',
    'deepmind_fsf_3_1_observed_2026_10_17': '0a4e8c12a2e774a08f5b053260d3e7b842881b8d413f2a0900e7ec17d82e5cc0',
}


def utc_timestamp(value: str) -> datetime:
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|\+00:00)', value):
        raise ValueError('retrieved_at must be a full UTC timestamp, YYYY-MM-DDTHH:MM:SSZ')
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError:
        raise ValueError('retrieved_at is not a valid UTC timestamp') from None


def fingerprint(item: dict) -> str:
    return hashlib.sha256(json.dumps(item, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def validate(item: dict, check_date, check_url) -> None:
    key = item['id']
    check_url(item['original_url'], f'{key}.original_url')
    if item['source_url'] != item['original_url']:
        raise ValueError(f'{key}: source_url must equal original_url (compatibility alias)')
    if item['published_on'] is not None:
        check_date(item['published_on'], f'{key}.published_on', full=False)
    if item['preservation_status'] == 'legacy_uncaptured':
        if LEGACY.get(key) != fingerprint(item):
            raise ValueError(f'{key}: legacy_uncaptured is restricted to the two frozen pilot records')
        return
    if item['preservation_status'] != 'captured':
        raise ValueError(f'{key}: preservation_status must be captured or legacy_uncaptured')
    retrieved = utc_timestamp(item['retrieved_at'])
    if retrieved.date().isoformat() > item['observed_on']:
        raise ValueError(f'{key}: retrieval cannot be later than the recorded inspection date')
    if retrieved > datetime.now(timezone.utc):
        raise ValueError(f'{key}: retrieval cannot be in the future')
    if not isinstance(item['sha256'], str) or not re.fullmatch(r'[0-9a-f]{64}', item['sha256']):
        raise ValueError(f'{key}.sha256 must contain 64 lowercase hexadecimal characters')
    if type(item['byte_length']) is not int or item['byte_length'] <= 0:
        raise ValueError(f'{key}.byte_length must be a positive integer')
    if item['mime_type'] not in {'application/pdf', 'text/html', 'application/xhtml+xml'}:
        raise ValueError(f'{key}: unsupported captured mime_type')
    if (item['archive_url'] is None) != (item['archive_checked_on'] is None):
        raise ValueError(f'{key}: archive_url and archive_checked_on must be paired')
    if item['archive_url'] is None:
        if not item.get('archive_unavailable_reason', '').strip():
            raise ValueError(f'{key}: a missing archive requires archive_unavailable_reason')
    else:
        check_url(item['archive_url'], f'{key}.archive_url')
        if item['archive_url'] == item['original_url']:
            raise ValueError(f'{key}: the current source URL is not an independent archive')
        check_date(item['archive_checked_on'], f'{key}.archive_checked_on')
        if item['archive_checked_on'] < retrieved.date().isoformat():
            raise ValueError(f'{key}: archive check cannot predate the retained retrieval')
        if item['archive_checked_on'] > datetime.now(timezone.utc).date().isoformat():
            raise ValueError(f'{key}: archive check cannot be in the future')
    if item['mime_type'] != 'application/pdf' and item['archive_url'] is None and not item.get('capture_path'):
        raise ValueError(f'{key}: unarchived HTML requires a retained capture_path')


def check_payload(data: bytes, mime_type: str) -> None:
    if not data:
        raise ValueError('source response is empty')
    if mime_type == 'application/pdf' and not data.startswith(b'%PDF-'):
        raise ValueError('expected PDF bytes; the response may be an error or access page')
    if mime_type in {'text/html', 'application/xhtml+xml'} and not re.search(
            br'(?i)<(?:!doctype\s+html|html|head|body)\b', data[:8192]):
        raise ValueError('expected a captured HTML representation')
