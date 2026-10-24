#!/usr/bin/env python3
"""Audit deferred operational-risk bibliography reconciliation without mutating sources.

Run from repository root: python3 scripts/audit_cyber_bibliography.py
Exits nonzero while any accepted source lacks canonical admission.
"""
from __future__ import annotations
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research/cyber-deployment/operational-risk/source-admission.yaml"
RECORDS = ROOT / "records.yaml"

def main() -> int:
    sources = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))["sources"]
    records = yaml.safe_load(RECORDS.read_text(encoding="utf-8"))["records"]
    by_id = {record["id"]: record for record in records}
    failures = []
    for source in sources:
        if source.get("research_admission") != "accepted":
            continue
        source_id = source["source_id"]
        proposed = source.get("record_id") or source.get("proposed_record_id")
        record = by_id.get(proposed)
        if record is None:
            failures.append(f"{source_id}: missing records.yaml entry {proposed}")
            continue
        if source.get("bibliography_admission") != "admitted":
            failures.append(f"{source_id}: bibliography_admission not admitted")
        if source.get("record_id") != proposed:
            failures.append(f"{source_id}: canonical record_id missing")
        if not record.get("fields", {}).get("title"):
            failures.append(f"{source_id}: bibliography title missing")
    if failures:
        print("\n".join(failures))
        return 1
    print(f"OK: {sum(s.get('research_admission') == 'accepted' for s in sources)} accepted sources resolve to admitted bibliography records")
    return 0

if __name__ == "__main__":
    sys.exit(main())
