"""Protect coverage completeness, claim references, depth boundaries and generated views."""
from copy import deepcopy
import csv
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_research as research


class BroadResearchTests(unittest.TestCase):
    def setUp(self):
        with (ROOT / research.DIRECTORY / "coverage.csv").open(encoding="utf-8", newline="") as handle:
            self.rows = list(csv.DictReader(handle))[:2]
        all_records = yaml.safe_load((ROOT / "records.yaml").read_text(encoding="utf-8"))["records"]
        by_key = {record["id"]: record for record in all_records}
        self.records = [by_key[row["citation_key"]] for row in self.rows]
        self.keys = {record["id"] for record in self.records}
        self.claims = {
            "schema_version": "broad-synthesis-v1", "as_of": "2026-11-14",
            "claims": [{
                "id": "C01", "section": "safeguards", "claim": "A scoped finding.",
                "status": "provisional", "limitation": "One model.",
                "counterevidence": "Different contexts remain untested.", "next_check": "Read held-out results.",
                "evidence": [{"citation_key": self.rows[0]["citation_key"], "relation": "supports",
                              "version_url": "https://arxiv.org/html/2504.09604v3", "locator": "Section 4",
                              "finding": "Bounded result.", "review_basis": "supplied_ledger",
                              "checked_scope": "Inherited scoped notes."}],
            }], "families": [],
        }

    def test_coverage_rejects_missing_duplicate_unknown_and_mismatched_keys(self):
        research.validate_coverage(self.records, self.rows)
        for case in (self.rows[:1], self.rows + [self.rows[0]],
                     [dict(self.rows[0], citation_key="unknown"), self.rows[1]],
                     [dict(self.rows[0], repository_stream="contextual"), self.rows[1]]):
            with self.subTest(case=case[0]["citation_key"]):
                with self.assertRaises(research.ValidationError):
                    research.validate_coverage(self.records, case)

    def test_depth_and_prior_check_metadata_cannot_silently_inflate_assurance(self):
        cases = [dict(self.rows[0], inherited_read_depth="Verified"),
                 dict(self.rows[0], prior_ai_check_depth_locator=""),
                 dict(self.rows[0], replication_status="replicated"),
                 dict(self.rows[0], prior_ai_check_status="outside_105_record_register"),
                 dict(self.rows[0], limitations=""),
                 dict(self.rows[0], material_accessed_url="https://chatgpt.com/c/private")]
        for changed in cases:
            with self.subTest(changed=changed):
                with self.assertRaises(research.ValidationError):
                    research.validate_coverage(self.records, [changed, self.rows[1]])

    def test_claims_reject_dangling_keys_relations_and_review_bases(self):
        research.validate_claims(self.claims, self.keys)
        for field, value in (("citation_key", "not_admitted_candidate"), ("relation", "proves"),
                             ("review_basis", "independent_human_review"), ("locator", ""),
                             ("version_url", "https://chatgpt.com/space/private")):
            with self.subTest(field=field):
                changed = deepcopy(self.claims)
                changed["claims"][0]["evidence"][0][field] = value
                with self.assertRaises(research.ValidationError):
                    research.validate_claims(changed, self.keys)

    def test_claim_ids_and_family_keys_are_checked(self):
        changed = deepcopy(self.claims)
        changed["claims"].append(deepcopy(changed["claims"][0]))
        with self.assertRaisesRegex(research.ValidationError, "duplicate claim ID"):
            research.validate_claims(changed, self.keys)
        changed = deepcopy(self.claims)
        changed["families"] = [{"id": "F01", "citation_keys": ["missing"],
                                 "relationship": "Shared data", "basis": "Source notes", "status": "unresolved"}]
        with self.assertRaisesRegex(research.ValidationError, "unknown family citation key"):
            research.validate_claims(changed, self.keys)

    def test_unmapped_records_remain_covered_without_supporting_a_claim(self):
        research.validate_claims(self.claims, self.keys)
        summary = research.generate_summary(self.rows, self.claims)
        self.assertIn("other **1 keys**", summary)
        self.assertIn("An unmapped record is neither excluded nor evidence for a claim", summary)
        self.assertIn("not a complete-document reread", summary)
        self.assertIn("not established errors", summary)
        rendered = research.generate_claims(self.claims)
        self.assertIn("Inherited scoped notes.", rendered)
        self.assertIn("Different contexts remain untested.", rendered)

    def test_stale_or_missing_generated_views_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / research.DIRECTORY
            target.mkdir(parents=True)
            (root / "records.yaml").write_text(yaml.safe_dump({"records": self.records}), encoding="utf-8")
            with (target / "coverage.csv").open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=research.COLUMNS)
                writer.writeheader()
                writer.writerows(self.rows)
            (target / "claims.yaml").write_text(yaml.safe_dump(self.claims), encoding="utf-8")
            with self.assertRaisesRegex(research.ValidationError, "missing or stale"):
                research.build(root, check=True)
            research.build(root)
            research.build(root, check=True)
            changed = deepcopy(self.claims)
            changed["claims"][0]["evidence"][0]["locator"] = "Section 5 instead"
            (target / "claims.yaml").write_text(yaml.safe_dump(changed), encoding="utf-8")
            with self.assertRaisesRegex(research.ValidationError, "missing or stale"):
                research.build(root, check=True)


if __name__ == "__main__":
    unittest.main()
