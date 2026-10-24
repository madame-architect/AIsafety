#!/usr/bin/env python3
"""Retrieve and retain exact source bytes; emit a v2 evidence-record draft.

PDF digests cover the exact retrieved entity body, before parsing or rewriting.
HTML digests cover the saved representation (archive response when supplied).
Archive URLs must be capture-specific, not live URLs or archive search pages.
An archive can be captured without contacting the original URL. PDF comparison
with the original is a separate, explicitly requested check.
The researcher still checks edition identity, archive completeness and locators.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import sys
from urllib.request import Request, urlopen

sys.dont_write_bytecode = True
import yaml
from build_commitments import check_url, check_date
from source_provenance import check_payload, validate


def retrieve(url: str) -> tuple[bytes, str]:
    check_url(url, 'retrieval URL')
    request = Request(url, headers={'User-Agent': 'FrontierGovernanceEvals/1.0',
                                    'Accept-Encoding': 'identity'})
    with urlopen(request, timeout=60) as response:
        if response.headers.get('Content-Encoding', 'identity') != 'identity':
            raise ValueError('encoded response refused; request identity entity bytes')
        return response.read(), response.headers.get_content_type()


def capture(original_url: str, archive_url: str | None = None, *,
            compare_original: bool = False) -> tuple[bytes, dict]:
    check_url(original_url, 'original URL')
    if compare_original and not archive_url:
        raise ValueError('--compare-original requires --archive-url')
    checked = None
    if archive_url:
        if archive_url == original_url:
            raise ValueError('an archive must be distinct from the live source URL')
        # The archived representation is independently retrievable even when
        # the original disappears, changes format or denies access.
        data, mime = retrieve(archive_url)
        check_payload(data, mime)
        basis = 'Archive response bytes; original was not retrieved or compared.'
        if compare_original:
            if mime != 'application/pdf':
                raise ValueError('--compare-original only verifies PDF byte identity')
            original, original_mime = retrieve(original_url)
            check_payload(original, original_mime)
            if original_mime != 'application/pdf' or data != original:
                raise ValueError('archive PDF does not match the exact retrieved source bytes')
            basis = 'Archive PDF bytes; retrieved original PDF matched byte for byte.'
        checked = datetime.now(timezone.utc).date().isoformat()
    else:
        data, mime = retrieve(original_url)
        check_payload(data, mime)
        basis = 'Original response bytes; no archive comparison was performed.'
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    return data, dict(original_url=original_url, retrieved_at=now, archive_url=archive_url,
                      archive_checked_on=checked, sha256=hashlib.sha256(data).hexdigest(),
                      byte_length=len(data), mime_type=mime, capture_basis=basis)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--original-url', required=True)
    parser.add_argument('--archive-url')
    parser.add_argument('--compare-original', action='store_true',
                        help='Also retrieve the original and require byte-identical PDFs')
    parser.add_argument('--archive-unavailable-reason')
    parser.add_argument('--id', required=True)
    parser.add_argument('--record-id', required=True)
    parser.add_argument('--published-on')
    parser.add_argument('--version-claim')
    parser.add_argument('--locator-basis', required=True)
    parser.add_argument('--inspection-scope', required=True)
    parser.add_argument('--preservation-note', required=True)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        if not args.archive_url and not args.archive_unavailable_reason:
            raise ValueError('supply --archive-url or explain why archival capture is unavailable')
        data, metadata = capture(args.original_url, args.archive_url,
                                 compare_original=args.compare_original)
        extension = '.pdf' if metadata['mime_type'] == 'application/pdf' else '.html'
        relative = Path('.source-captures') / (metadata['sha256'] + extension)
        item = dict(id=args.id, record_id=args.record_id, source_url=args.original_url,
                    observed_on=metadata['retrieved_at'][:10], inspection_scope=args.inspection_scope,
                    preservation_note=args.preservation_note, **metadata,
                    published_on=args.published_on, version_claim=args.version_claim,
                    locator_basis=args.locator_basis, preservation_status='captured',
                    capture_path=relative.as_posix())
        if args.archive_unavailable_reason:
            item['archive_unavailable_reason'] = args.archive_unavailable_reason
        validate(item, check_date, check_url)
        target = args.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and target.read_bytes() != data:
            raise ValueError('existing capture path has different bytes')
        target.write_bytes(data)
        print(yaml.safe_dump(item, sort_keys=False, allow_unicode=True), end='')
        return 0
    except (OSError, ValueError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
