#!/usr/bin/env python3
"""Retrieve the five public raw-archive representations and verify fingerprints.

Run from any directory after installing the repository's requirements.txt.
Writes no files, does not change historical observations, and fails on mismatch.
"""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import capture_source


def main() -> int:
    manifest = json.loads(Path(__file__).with_name('results.json').read_text(encoding='utf-8'))
    failures = 0
    for item in manifest['pages']:
        raw = item['raw']
        args = ['--url', raw['response']['requested_url'], '--sha256', raw['sha256'],
                '--byte-length', str(raw['byte_length'])]
        for marker in item['expected_text']:
            args.extend(['--expect-text', marker])
        output = io.StringIO()
        with redirect_stdout(output):
            code = capture_source.verify_main(args)
        failures += bool(code)
        result = {'historical_id': item['historical_id'],
                  'verification': 'failed' if code else 'matched_new_raw_baseline'}
        if not code:
            response = json.loads(output.getvalue())['response']
            result.update(retrieved_at=response['retrieved_at'],
                          sha256=raw['sha256'], byte_length=raw['byte_length'],
                          final_url=response['final_url'])
        print(json.dumps(result))
    return int(bool(failures))


if __name__ == '__main__':
    raise SystemExit(main())
