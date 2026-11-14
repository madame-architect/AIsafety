#!/usr/bin/env python3
"""Check the pending Carbon source package offline; does not admit any source.

Use --require-capture-files with the private .source-captures directory restored.
Without it, missing bytes are reported, never treated as verified payloads.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import re
import sys
import tempfile

sys.dont_write_bytecode = True
import yaml
import build
import build_commitments as history
import source_provenance as provenance

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = Path('research/cyber-deployment/carbon-source-review')


def normalized(value):
    return re.sub(r'[^a-z0-9]', '', value.lower())


class Article(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.skip = 0
        self.words = []

    def handle_starttag(self, tag, attrs):
        if tag == 'article':
            self.active = True
        if self.active and tag in ('script','style'):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag == 'article':
            self.active = False
        if self.active and tag in ('script','style'):
            self.skip -= 1

    def handle_data(self, text):
        if self.active and not self.skip:
            self.words.append(text)


def article_text(path):
    parser = Article()
    parser.feed(path.read_text())
    text = ' '.join(' '.join(parser.words).split())
    if len(text) < 1000:
        raise ValueError('article text is unexpectedly short')
    return text


def check_bytes(root, item, required):
    path = (root / item['capture_path']).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('capture path escapes repository')
    if not path.is_file():
        if required:
            raise ValueError('missing retained bytes: ' + item['capture_path'])
        return False
    data = path.read_bytes()
    if len(data) != item['byte_length'] or hashlib.sha256(data).hexdigest() != item['sha256']:
        raise ValueError('retained SHA-256 or length mismatch: ' + item['capture_path'])
    if item['mime_type'] == 'image/png':
        if not data.startswith(b'\x89PNG\r\n\x1a\n'):
            raise ValueError('invalid PNG signature')
    else:
        provenance.check_payload(data, item['mime_type'])
    return True


def audit(root=ROOT, required=False):
    directory = root / DIRECTORY
    admission = yaml.safe_load((directory/'source-admission.yaml').read_text())
    captures = yaml.safe_load((directory/'source-captures.yaml').read_text())['snapshots']
    drafts = yaml.safe_load((directory/'records.proposed.yaml').read_text())['records']
    canonical = yaml.safe_load((root/'records.yaml').read_text())['records']
    sources = admission['sources']
    by_source = {x['source_id']: x for x in sources}
    by_record = {x['id']: x for x in drafts}
    by_capture = {x['id']: x for x in captures}
    if len(by_source) != 5 or len(by_record) != 5 or len(by_capture) != 6:
        raise ValueError('expected five distinct source drafts and six distinct document captures')
    if sum(x['original_pr21_candidate'] for x in sources) != 3:
        raise ValueError('original three candidates must remain identifiable')
    for source in sources:
        if any(source[f] != 'pending' for f in ('research_admission','bibliography_admission')) or source['admitted_on'] is not None or source['record_id'] is not None:
            raise ValueError('this package must not silently admit sources')
        draft = by_record[source['proposed_record_id']]
        if draft['fields']['title'] != source['title'] or draft['fields']['url'] != source['primary_url']:
            raise ValueError('candidate title/URL disagrees with draft')
        for capture_id in source['capture_ids']:
            capture = by_capture[capture_id]
            if capture['record_id'] != draft['id'] or capture['original_url'] != source['primary_url']:
                raise ValueError('source/capture identity mismatch')
        for item in canonical:
            if item['id'] == draft['id'] or normalized(item['fields']['title']) == normalized(source['title']) or item['fields'].get('url','').rstrip('/') == source['primary_url'].rstrip('/'):
                raise ValueError('possible canonical duplicate requires review: ' + item['id'])

    # Validate draft classifications with the real corpus schema without editing it.
    with tempfile.TemporaryDirectory() as temporary:
        temp = Path(temporary)
        (temp/'records.yaml').write_bytes((directory/'records.proposed.yaml').read_bytes())
        build.load_records(temp, build.lint.load_schema(root/build.SCHEMA_NAME))

    checked = 0
    for item in captures:
        provenance.validate(item, history.check_date, history.check_url)
        checked += check_bytes(root,item,required)
    receipts = json.loads((directory/'retrieval-receipts.json').read_text())
    by_receipt = {x['source_id']:x for x in receipts}
    assets = json.loads((directory/'auxiliary-assets.json').read_text())
    if assets != [by_receipt['exploitgym_chart']]:
        raise ValueError('auxiliary chart receipt disagrees with retained retrieval')
    receipt_checked = sum(check_bytes(root,x,required) for x in receipts)
    for result in json.loads((directory/'comparisons.json').read_text()):
        original = by_receipt[result['source_id']]
        archive = by_receipt[result['source_id']+'_archive']
        for prefix, receipt in [('original',original),('archive',archive)]:
            if result[prefix+'_sha256'] != receipt['sha256'] or result[prefix+'_byte_length'] != receipt['byte_length']:
                raise ValueError('comparison digest/length disagrees with receipt')
        same = original['sha256'] == archive['sha256'] and original['byte_length'] == archive['byte_length']
        if result['byte_identical'] != same:
            raise ValueError('false archive/original byte-identity claim')
        if original['mime_type'] == 'text/html':
            left,right = root/original['capture_path'],root/archive['capture_path']
            if left.is_file() and right.is_file():
                if result['normalized_article_text_identical'] != (article_text(left) == article_text(right)):
                    raise ValueError('false normalized-article comparison')

    baseline = json.loads((directory/'historical-intake-check.json').read_text())
    intake = (root/'intake.csv').read_bytes()
    if hashlib.sha256(intake[:baseline['byte_length']]).hexdigest() != baseline['sha256']:
        raise ValueError('historical intake prefix was changed')
    rows = list(csv.DictReader(io.StringIO(intake.decode())))
    new_rows = rows[-5:]
    if {r['candidate_identifier'] for r in new_rows} != {x['primary_url'] for x in sources} or any(r['decision'] != 'defer' or r['accepted_record_id'] for r in new_rows):
        raise ValueError('new intake rows must remain separate and deferred')
    observation_doc = yaml.safe_load((directory/'observations.proposed.yaml').read_text())
    if observation_doc['status'] != 'pending_admission':
        raise ValueError('observation drafts must stay pending')
    observations = observation_doc['observations']
    if len({x['id'] for x in observations}) != len(observations):
        raise ValueError('duplicate observation ID')
    for observation in observations:
        if observation['source_id'] not in by_source:
            raise ValueError('observation source missing')
        if 'snapshot_id' in observation and observation['snapshot_id'] not in by_capture:
            raise ValueError('observation capture missing')
    return dict(pending_sources=len(sources),proposed_records=len(drafts),document_snapshots=len(captures),
                document_payload_checks=checked,retrieval_payload_checks=receipt_checked,
                unique_payloads=len({x['sha256'] for x in receipts}),
                missing_document_payloads=len(captures)-checked,missing_retrieval_payloads=len(receipts)-receipt_checked,
                canonical_records=len(canonical),
                historical_intake_prefix='unchanged',admission='pending; no corpus integration')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--require-capture-files',action='store_true')
    args = parser.parse_args()
    try:
        print(json.dumps(audit(required=args.require_capture_files),indent=2))
    except (ValueError,KeyError,OSError) as error:
        print('error: '+str(error),file=sys.stderr)
        raise SystemExit(1)
