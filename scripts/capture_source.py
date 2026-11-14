#!/usr/bin/env python3
"""Retrieve and retain exact source bytes; emit a v2 evidence-record draft.

Digests cover response entity bytes after explicit HTTP content decoding and
before parsing or rewriting. Encoded response bodies are retained separately.
Archive URLs must be capture-specific, not live URLs or archive search pages.
An archive can be captured without contacting the original URL. PDF comparison
with the original is a separate, explicitly requested check.
The researcher still checks edition identity, archive completeness and locators.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import gzip
import hashlib
from html.parser import HTMLParser
from http.client import HTTPException
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen
import zlib

sys.dont_write_bytecode = True
import yaml
from build_commitments import check_url, check_date
from source_provenance import check_payload, validate


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


class Retrieved(tuple):
    """Preserve the historical two-value API while exposing HTTP provenance."""

    def __new__(cls, data: bytes, mime: str, receipt: dict, response_body: bytes):
        result = super().__new__(cls, (data, mime))
        result.receipt = receipt
        result.response_body = response_body
        return result


def retrieve(url: str) -> tuple[bytes, str]:
    check_url(url, 'retrieval URL')
    request = Request(url, headers={'User-Agent': 'FrontierGovernanceEvals/1.0',
                                    'Accept-Encoding': 'identity'})
    with urlopen(request, timeout=60) as response:
        encoding = response.headers.get('Content-Encoding', 'identity').strip().lower()
        if encoding not in {'identity', 'gzip', 'deflate'}:
            raise ValueError(f'unsupported Content-Encoding: {encoding}')
        status = response.getcode()
        if status != 200:
            raise ValueError(f'expected HTTP 200; received {status}')
        try:
            body = response.read()
        except HTTPException as exc:
            raise ValueError(f'incomplete HTTP response: {exc}') from exc
        length = response.headers.get('Content-Length')
        if length is not None and (not length.isdecimal() or int(length) != len(body)):
            raise ValueError('response Content-Length does not match retained bytes')
        try:
            data = (gzip.decompress(body) if encoding == 'gzip' else
                    zlib.decompress(body) if encoding == 'deflate' else body)
        except (OSError, EOFError, zlib.error) as exc:
            raise ValueError(f'invalid or truncated {encoding} response body: {exc}') from exc
        return Retrieved(data, response.headers.get_content_type(), {
            'requested_url': url, 'final_url': response.geturl(), 'status': status,
            'redirected': response.geturl() != url,
            'response_headers': list(response.headers.items()),
            'request_headers': dict(request.header_items()), 'retrieved_at': utc_now(),
            'content_encoding': encoding,
            'response_body_sha256': hashlib.sha256(body).hexdigest(),
            'response_body_byte_length': len(body),
            'decoded_entity_sha256': hashlib.sha256(data).hexdigest(),
            'decoded_entity_byte_length': len(data),
            'byte_basis': 'HTTP response body before content decoding; transfer framing is not retained. '
                          'Capture sha256 and byte_length identify the decoded entity, before HTML parsing.',
        }, body)


def raw_archive_url(url: str) -> str:
    """Select Wayback's identity replay explicitly; never rewrite by default."""
    parsed = urlsplit(url)
    match = re.fullmatch(r'/web/(\d{14})(?:[a-z]+_)?/(https?://.+)', parsed.path)
    if parsed.hostname != 'web.archive.org' or not match:
        raise ValueError('--raw-archive requires a timestamped web.archive.org capture URL')
    return urlunsplit((parsed.scheme, parsed.netloc,
                       f'/web/{match[1]}id_/{match[2]}', parsed.query, parsed.fragment))


def representation(url: str) -> str:
    parsed = urlsplit(url)
    if parsed.hostname == 'web.archive.org':
        return ('wayback_identity_body' if re.match(r'/web/\d{14}id_/', parsed.path)
                else 'wayback_replay_body')
    return 'http_identity_body'


def require_same_archive_selection(requested: str, final: str) -> None:
    """A redirect must not quietly select a different Wayback snapshot or mode."""
    before, after = urlsplit(requested), urlsplit(final)
    selection = re.match(r'/web/(\d{14})([a-z]+_)?/', before.path)
    if before.hostname != 'web.archive.org' or not selection:
        return
    received = re.match(r'/web/(\d{14})([a-z]+_)?/', after.path)
    if (after.hostname != 'web.archive.org' or not received or
            selection.groups() != received.groups()):
        raise ValueError('archive redirect changed the specified capture timestamp or representation')


class VisibleText(HTMLParser):
    """Text markers must occur in HTML content, not scripts or embedded JSON."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style', 'noscript', 'template'}:
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in {'script', 'style', 'noscript', 'template'} and self.hidden:
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def check_completeness(data: bytes, mime: str, expected_text: list[str]) -> dict:
    """Check selected passages; a passing marker check is not a full-text audit."""
    if mime not in {'text/html', 'application/xhtml+xml'}:
        if expected_text:
            raise ValueError('--expect-text applies to HTML; inspect PDF text separately')
        return {'status': 'not_applicable', 'expected_text': []}
    if not re.search(br'</html\s*>', data, re.I):
        raise ValueError('HTML closing tag missing; inspect possible truncated response')
    limitation = ('Markers and a closing tag do not establish article completeness. '
                  'Review the opening, ending, numbers, qualifications, tables and footnotes; '
                  'linked assets and script-rendered content are not checked.')
    if not expected_text:
        return {'status': 'not_checked', 'expected_text': [], 'limitation': limitation}
    # UTF-8 is required for marker checks; do not silently replace unreadable bytes.
    text = data.decode('utf-8-sig')
    parser = VisibleText()
    parser.feed(text)
    visible = ' '.join(' '.join(parser.parts).split())
    markers = [' '.join(marker.split()) for marker in expected_text]
    if any(not marker for marker in markers):
        raise ValueError('expected HTML text markers must be nonempty')
    missing = [marker for marker in markers if marker not in visible]
    if missing:
        raise ValueError(f'expected HTML text missing: {missing!r}')
    return {'status': 'selected_markers_present', 'expected_text': markers,
            'limitation': limitation}


def verify_bytes(data: bytes, sha256: str, byte_length: int) -> None:
    if not re.fullmatch(r'[0-9a-f]{64}', sha256) or byte_length <= 0:
        raise ValueError('expected digest must be lowercase SHA-256 and length must be positive')
    if len(data) != byte_length or hashlib.sha256(data).hexdigest() != sha256:
        raise ValueError('retrieved bytes do not match the expected SHA-256 and byte length')


def capture(original_url: str, archive_url: str | None = None, *,
            compare_original: bool = False, response_details: dict | None = None,
            response_bodies: list | None = None) -> tuple[bytes, dict]:
    check_url(original_url, 'original URL')
    if compare_original and not archive_url:
        raise ValueError('--compare-original requires --archive-url')
    checked = None
    if archive_url:
        if archive_url == original_url:
            raise ValueError('an archive must be distinct from the live source URL')
        # The archived representation is independently retrievable even when
        # the original disappears, changes format or denies access.
        response = retrieve(archive_url)
        data, mime = response
        check_payload(data, mime)
        basis = 'Archive response bytes; original was not retrieved or compared.'
        if compare_original:
            if mime != 'application/pdf':
                raise ValueError('--compare-original only verifies PDF byte identity')
            original_response = retrieve(original_url)
            original, original_mime = original_response
            if response_bodies is not None and hasattr(original_response, 'receipt'):
                response_bodies.append((original_response.response_body, original_response.receipt))
            check_payload(original, original_mime)
            if original_mime != 'application/pdf' or data != original:
                raise ValueError('archive PDF does not match the exact retrieved source bytes')
            basis = 'Archive PDF bytes; retrieved original PDF matched byte for byte.'
        checked = datetime.now(timezone.utc).date().isoformat()
    else:
        response = retrieve(original_url)
        data, mime = response
        check_payload(data, mime)
        basis = 'Original response bytes; no archive comparison was performed.'
    if response_details is not None:
        response_details.update(getattr(response, 'receipt', {}))
    if response_bodies is not None and hasattr(response, 'receipt'):
        response_bodies.insert(0, (response.response_body, response.receipt))
    encoding = getattr(response, 'receipt', {}).get('content_encoding', 'identity')
    if encoding != 'identity':
        basis += f' HTTP Content-Encoding {encoding} was explicitly decoded before hashing the entity.'
    now = getattr(response, 'receipt', {}).get('retrieved_at', utc_now())
    return data, dict(original_url=original_url, retrieved_at=now, archive_url=archive_url,
                      archive_checked_on=checked, sha256=hashlib.sha256(data).hexdigest(),
                      byte_length=len(data), mime_type=mime, capture_basis=basis)


def new_receipt_path(root: Path, capture_id: str) -> Path:
    if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', capture_id):
        raise ValueError('capture ID must contain lowercase letters, digits, underscores or hyphens')
    receipt = root / '.source-captures' / 'retrievals' / (capture_id + '.json')
    if receipt.exists():
        raise ValueError('capture ID already has a retrieval receipt; use a new ID')
    for relative, collection in [('research/cyber-deployment/evidence.yaml', 'snapshots'),
                                 ('research/cyber-deployment/operational-risk/source-captures.yaml', 'snapshots')]:
        source = root / relative
        if source.is_file():
            document = yaml.safe_load(source.read_text(encoding='utf-8'))
            if any(item.get('id') == capture_id for item in document.get(collection, [])):
                raise ValueError('capture ID is a historical observation; use a new ID')
    return receipt


def verify_main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description='Retrieve the specified representation and verify its exact bytes; write no files.')
    parser.add_argument('--url', required=True)
    parser.add_argument('--sha256', required=True)
    parser.add_argument('--byte-length', type=int, required=True)
    parser.add_argument('--expect-text', action='append', default=[])
    args = parser.parse_args(argv)
    try:
        response = retrieve(args.url)
        data, mime = response
        final_url = getattr(response, 'receipt', {}).get('final_url', args.url)
        require_same_archive_selection(args.url, final_url)
        if mime not in {'application/pdf', 'text/html', 'application/xhtml+xml'}:
            raise ValueError('unsupported source MIME type')
        check_payload(data, mime)
        verify_bytes(data, args.sha256, args.byte_length)
        checks = check_completeness(data, mime, args.expect_text)
        print(json.dumps({'verification': 'matched', 'sha256': args.sha256,
                          'byte_length': len(data), 'representation': representation(final_url),
                          'response': getattr(response, 'receipt', {}),
                          'completeness': checks}, indent=2, ensure_ascii=False))
        return 0
    except (OSError, ValueError, UnicodeError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == 'verify':
        return verify_main(sys.argv[2:])
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--original-url', required=True)
    parser.add_argument('--archive-url')
    parser.add_argument('--raw-archive', action='store_true',
                        help='Explicitly select Wayback id_ response body; supplied URLs otherwise remain unchanged')
    parser.add_argument('--expect-text', action='append', default=[],
                        help='Required visible HTML passage; repeat for title, ending and consequential claims')
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
        receipt_path = new_receipt_path(args.root, args.id)
        if not args.archive_url and not args.archive_unavailable_reason:
            raise ValueError('supply --archive-url or explain why archival capture is unavailable')
        if args.raw_archive:
            if not args.archive_url:
                raise ValueError('--raw-archive requires --archive-url')
            args.archive_url = raw_archive_url(args.archive_url)
        details, bodies = {}, []
        data, metadata = capture(args.original_url, args.archive_url,
                                 compare_original=args.compare_original, response_details=details,
                                 response_bodies=bodies)
        requested_url = args.archive_url or args.original_url
        final_url = details.get('final_url', requested_url)
        require_same_archive_selection(requested_url, final_url)
        if args.raw_archive and metadata['mime_type'] != 'application/pdf' and not args.expect_text:
            raise ValueError('raw HTML capture requires --expect-text article markers')
        checks = check_completeness(data, metadata['mime_type'], args.expect_text)
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
        if not target.exists():
            with target.open('xb') as stream:
                stream.write(data)
        retained_responses = []
        for body, response_receipt in bodies:
            encoding = response_receipt['content_encoding']
            suffix = {'gzip': '.response.gz', 'deflate': '.response.deflate',
                      'identity': '.response'}[encoding]
            body_relative = Path('.source-captures') / (response_receipt['response_body_sha256'] + suffix)
            body_path = args.root / body_relative
            if body_path.exists() and body_path.read_bytes() != body:
                raise ValueError('existing raw response path has different bytes')
            if not body_path.exists():
                with body_path.open('xb') as stream:
                    stream.write(body)
            retained_responses.append({**response_receipt, 'response_body_path': body_relative.as_posix()})
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt = {'schema_version': 'source-retrieval-v1', 'capture': item,
                   'representation': representation(final_url),
                   'response': details, 'retained_responses': retained_responses,
                   'completeness': checks}
        with receipt_path.open('x', encoding='utf-8', newline='\n') as stream:
            json.dump(receipt, stream, indent=2, ensure_ascii=False)
            stream.write('\n')
        print(yaml.safe_dump(item, sort_keys=False, allow_unicode=True), end='')
        return 0
    except (OSError, ValueError, UnicodeError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
