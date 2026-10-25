#!/usr/bin/env python3
"""Compare recovered originals with freshly saved raw/replay HTML (local files).

Requires beautifulsoup4==4.15.0. No source text is emitted unless a caller
chooses to inspect its own files. Original expected hashes come from results.json.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def article(data: bytes) -> dict:
    soup = BeautifulSoup(data.decode('utf-8'), 'html.parser')
    nodes = soup.select('article')
    if len(nodes) != 1:
        raise ValueError(f'expected exactly one article element, got {len(nodes)}')
    node = nodes[0]
    for hidden in node.select('script,style,noscript,template'):
        hidden.decompose()
    text = ' '.join(node.get_text(' ', strip=True).split())
    texts = lambda selector: [' '.join(n.get_text(' ', strip=True).split())
                              for n in node.select(selector)]
    numeric_tokens = re.findall(r'\d+(?:[.,]\d+)*', text)
    encoded = lambda values: digest(json.dumps(values, ensure_ascii=False,
                                               separators=(',', ':')).encode('utf-8'))
    table_texts = texts('table')
    footnotes = texts('[role=doc-footnote],[id*=footnote],[class*=footnote]')
    return {
        'text_sha256': digest(text.encode('utf-8')),
        'text_characters': len(text),
        'numeric_token_count': len(numeric_tokens),
        'numeric_tokens_sha256': encoded(numeric_tokens),
        'headings_sha256': encoded(texts('h1,h2,h3,h4,h5,h6')),
        'table_count': len(table_texts),
        'table_text_sha256': encoded(table_texts),
        'table_rows': len(node.select('tr')),
        'table_cells': len(node.select('td,th')),
        'footnote_container_count': len(footnotes),
        'nonempty_footnote_container_count': sum(bool(x) for x in footnotes),
        'footnote_text_sha256': encoded(footnotes),
        'superscript_count': len(texts('sup')),
        'superscripts_sha256': encoded(texts('sup')),
        'captions_sha256': encoded(texts('figcaption')),
        'image_count': len(node.select('img')),
        'image_alt_sha256': encoded([n.get('alt') for n in node.select('img')]),
    }


def replay_dynamic_fields(data: bytes) -> tuple[bytes, dict]:
    """Mask only enumerated Wayback-generated fields; retain every other byte.

    Equality after these replacements is an additional byte-level check,
    separate from the normalized article comparison. Do not broaden these
    patterns merely to turn a future disagreement into a passing comparison.
    """
    patterns = {
        'analytics_server': rb"v\.server_name='[^']*';v\.server_ms=\d+",
        'replay_retrieval_date': rb'INTERNET ARCHIVE ON [^\r\n]*\.',
        'playback_timings': rb'<!--\s*playback timings \(ms\):.*?-->',
        'toolbar_capture_count': rb'(<a class="t" href="/web/\d{14}\*/[^\"]+" title="See a list of every capture for this URL">)\d+ captures(</a>)',
    }
    found = {}
    for name, pattern in patterns.items():
        found[name] = [m.group(0).decode('utf-8') for m in re.finditer(pattern, data, re.S)]
        if name == 'toolbar_capture_count':
            data = re.sub(pattern, rb'\1<archive capture count>\2', data, flags=re.S)
        else:
            data = re.sub(pattern, ('<'+name+'>').encode(), data, flags=re.S)
    return data, found


def compare(original: bytes, raw: bytes, replay: bytes) -> dict:
    before, raw_article, replay_article = article(original), article(raw), article(replay)
    original_masked, original_dynamic = replay_dynamic_fields(original)
    replay_masked, replay_dynamic = replay_dynamic_fields(replay)
    return {
        'article_raw_equal': before == raw_article,
        'article_replay_equal': before == replay_article,
        'historical_article': before,
        'all_other_replay_bytes_equal': original_masked == replay_masked,
        'masked_replay_sha256': digest(original_masked),
        'archive_dynamic_fields': {'historical': original_dynamic, 'fresh': replay_dynamic},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--original-dir', type=Path, required=True,
                        help='Directory holding historical HASH.html files')
    parser.add_argument('--fresh-dir', type=Path, required=True,
                        help='Directory holding HISTORICAL_ID.raw.html and .replay.html')
    args = parser.parse_args()
    manifest = json.loads(Path(__file__).with_name('results.json').read_text(encoding='utf-8'))
    for item in manifest['pages']:
        original = (args.original_dir / (item['historical']['sha256']+'.html')).read_bytes()
        if (digest(original) != item['historical']['sha256'] or
                len(original) != item['historical']['byte_length']):
            raise ValueError('historical fingerprint mismatch: '+item['historical_id'])
        raw = (args.fresh_dir / (item['historical_id']+'.raw.html')).read_bytes()
        replay = (args.fresh_dir / (item['historical_id']+'.replay.html')).read_bytes()
        for data, key in [(raw, 'raw'), (replay, 'replay')]:
            if digest(data) != item[key]['sha256'] or len(data) != item[key]['byte_length']:
                raise ValueError('fresh fingerprint mismatch: '+item['historical_id']+' '+key)
        result = compare(original, raw, replay)
        print(json.dumps({'historical_id': item['historical_id'], **result}, ensure_ascii=False))
        if not all(result[k] for k in ['article_raw_equal', 'article_replay_equal',
                                       'all_other_replay_bytes_equal']):
            return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
