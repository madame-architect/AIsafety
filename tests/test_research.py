"""Protect coverage completeness, claim references, depth boundaries and generated views."""
from copy import deepcopy
import csv
import hashlib
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

    def review_round(self):
        """A new complete read of the metadata-only fixture, with no forced claim role."""
        payload = b"%PDF-1.7\nRetained reading representation.\n"
        event = {
            "id": "R2_metadata_source", "citation_key": self.rows[1]["citation_key"], "theme": "audit",
            "reading_depth": "Full text", "edition_match": "same_record",
            "edition_match_note": "The identified canonical edition is the inspected object.",
            "coverage_effect": "complete_record_text", "scope": "Complete accessible main text, references and appendix.",
            "locators": ["Main text and Appendix A"], "visual_check": "Figure captions read; pixels not checked.",
            "limitations": "No linked supplements or independent source-truth verification.",
            "replication_status": "not_performed", "numerical_check": "No numerical recomputation.",
            "findings": ["Provides an explicit reporting structure."], "counterevidence": "No outcome effect estimated.",
            "next_check": "Assess implementation separately.", "relevance": "background", "claim_ids": [],
            "relevance_note": "Provides background for institutional design without estimating effects.",
            "capture": {
                "preservation_status": "captured", "original_url": "https://example.test/source.pdf",
                "final_url": "https://example.test/source.pdf", "retrieved_at": "2026-11-14T17:00:01Z",
                "attempted_at": "2026-11-14T17:00:00Z", "archive_url": None, "archive_checked_on": None,
                "archive_unavailable_reason": "No checked remote archive; retained bytes remain local.",
                "sha256": hashlib.sha256(payload).hexdigest(), "byte_length": len(payload), "mime_type": "application/pdf",
                "published_on": "2024", "version_claim": "Edition 1", "locator_basis": "One-based viewer pages.",
                "capture_path": ".source-captures/reading.pdf",
            },
        }
        rounds = {"schema_version": research.ROUND_SCHEMA, "rounds": [{
            "id": "thematic_round", "as_of": "2026-11-14", "base_commit": "a" * 40,
            "question": "What could change the synthesis?", "selection_basis": "A deliberately selected unresolved source.",
            "stopping_rule": "One bounded source review, not corpus completion.",
            "themes": [{"id": "audit", "label": "Audit design", "selection_reason": "Tests an institutional gap.",
                        "citation_keys": [self.rows[1]["citation_key"]]}], "readings": [event],
        }]}
        return rounds, payload

    def write_fixture(self, root, rounds=None):
        target = root / research.DIRECTORY
        target.mkdir(parents=True)
        (root / "records.yaml").write_text(yaml.safe_dump({"records": self.records}), encoding="utf-8")
        with (target / "coverage.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=research.COLUMNS)
            writer.writeheader()
            writer.writerows(self.rows)
        (target / "claims.yaml").write_text(yaml.safe_dump(self.claims), encoding="utf-8")
        if rounds is not None:
            (target / "rounds.yaml").write_text(yaml.safe_dump(rounds), encoding="utf-8")
        return target

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

    def test_round_full_coverage_requires_exact_edition_and_explicit_complete_read(self):
        rounds, _ = self.review_round()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            research.validate_rounds(rounds, self.records, self.claims, root)
            progress = research.round_coverage(self.rows, rounds)
            self.assertEqual(progress["full_additions"], {self.rows[1]["citation_key"]})
            self.assertEqual(list(progress["effective"].values()).count("Full text"), 2)
            for field, value in (("reading_depth", "Selected sections"), ("edition_match", "related_edition"),
                                 ("scope", ""), ("locators", []), ("relevance_note", "")):
                with self.subTest(field=field):
                    changed = deepcopy(rounds)
                    changed["rounds"][0]["readings"][0][field] = value
                    with self.assertRaises(research.ValidationError):
                        research.validate_rounds(changed, self.records, self.claims, root)
            related = deepcopy(rounds)
            event = related["rounds"][0]["readings"][0]
            event.update(edition_match="related_edition", coverage_effect="scoped_review")
            research.validate_rounds(related, self.records, self.claims, root)
            self.assertEqual(research.round_coverage(self.rows, related)["full_additions"], set())
            self.assertEqual(research.round_coverage(self.rows, related)["effective"][event["citation_key"]], "Metadata only")

    def test_round_references_depth_and_replication_categories_are_checked(self):
        rounds, _ = self.review_round()
        for field, value in (("citation_key", "unknown"), ("theme", "unassigned"), ("claim_ids", ["C99"]),
                             ("replication_status", "independent_human_verification"), ("findings", [])):
            with self.subTest(field=field):
                changed = deepcopy(rounds)
                changed["rounds"][0]["readings"][0][field] = value
                with self.assertRaises(research.ValidationError):
                    research.validate_rounds(changed, self.records, self.claims)
        changed = deepcopy(rounds)
        changed["rounds"][0]["readings"].append(deepcopy(changed["rounds"][0]["readings"][0]))
        with self.assertRaisesRegex(research.ValidationError, "duplicate event"):
            research.validate_rounds(changed, self.records, self.claims)
        claims = deepcopy(self.claims)
        claims["claims"][0]["evidence"][0]["review_event_ids"] = ["missing_event"]
        with self.assertRaisesRegex(research.ValidationError, "review_event_ids"):
            research.validate_rounds(rounds, self.records, claims)
        claims["claims"][0]["evidence"][0]["review_event_ids"] = [rounds["rounds"][0]["readings"][0]["id"]]
        with self.assertRaisesRegex(research.ValidationError, "mismatched review_event_ids"):
            research.validate_rounds(rounds, self.records, claims)
        claims["claims"][0]["evidence"][0]["citation_key"] = self.rows[1]["citation_key"]
        research.validate_rounds(rounds, self.records, claims)
        self.assertIn(f"[{rounds['rounds'][0]['readings'][0]['id']}](rounds.md#{rounds['rounds'][0]['readings'][0]['id']})",
                      research.generate_claims(claims))

    def test_round_archives_cannot_be_live_sources_or_unchecked_future_dates(self):
        rounds, _ = self.review_round()
        capture = rounds["rounds"][0]["readings"][0]["capture"]
        capture.update(final_url="https://example.test/redirected.pdf",
                       archive_url="https://archive.test/20261114/source.pdf",
                       archive_checked_on="2026-11-14", archive_unavailable_reason=None)
        research.validate_rounds(rounds, self.records, self.claims)
        for field, value in (("archive_url", capture["original_url"]), ("archive_url", capture["final_url"]),
                             ("archive_checked_on", "2026-11-15"), ("archive_checked_on", "2026-11-13")):
            with self.subTest(field=field, value=value):
                changed = deepcopy(rounds)
                changed["rounds"][0]["readings"][0]["capture"][field] = value
                with self.assertRaises(research.ValidationError):
                    research.validate_rounds(changed, self.records, self.claims)

    def test_failed_access_needs_no_invented_source_finding_or_coverage_upgrade(self):
        rounds, _ = self.review_round()
        event = rounds["rounds"][0]["readings"][0]
        event.update(reading_depth="Inaccessible", coverage_effect="none", relevance="unresolved", findings=[],
                     scope="The publisher response denied access; no source text was inspected.",
                     limitations="HTTP 403 prevented reading the requested representation.",
                     visual_check="No source pages were available for visual inspection.")
        event["capture"].update(preservation_status="unavailable", final_url=None, retrieved_at=None, sha256=None,
                                byte_length=None, mime_type=None, capture_path=None)
        research.validate_rounds(rounds, self.records, self.claims)
        self.assertEqual(research.round_coverage(self.rows, rounds)["full_additions"], set())
        self.assertIn("No source findings; material was inaccessible", research.generate_rounds(rounds, {}))
        successful, _ = self.review_round()
        successful["rounds"][0]["readings"][0].update(reading_depth="Selected sections", coverage_effect="scoped_review", findings=[])
        with self.assertRaisesRegex(research.ValidationError, "findings"):
            research.validate_rounds(successful, self.records, self.claims)

    def test_present_reading_payloads_must_match_declared_text_representation(self):
        valid = [("text/html", b"<!doctype html><html><head><title>A study</title></head><body>Methods</body></html>"),
                 ("application/xhtml+xml", b'<html xmlns="http://www.w3.org/1999/xhtml"><body>Methods</body></html>'),
                 ("text/plain", b"def similarity(a, b):\n    return 1.0\n"),
                 ("application/json", b'{"paper": "study", "items": [1, 2]}')]
        invalid = [("text/html", b"not an HTML document"),
                   ("text/html", b"<html><body>\xff</body></html>"),
                   ("text/html", b"<html><head><title>403 Forbidden</title></head><body>Access denied</body></html>"),
                   ("text/plain", b"\xffbinary"), ("text/plain", b"text\x00binary"),
                   ("text/plain", b"%PDF-1.7\nWrong MIME"), ("text/plain", b"404: Not Found"),
                   ("application/json", b'{"incomplete":'), ("application/json", b'{"binary": "\xff"}')]
        rounds, _ = self.review_round()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / ".source-captures/reading.pdf"
            target.parent.mkdir()
            for accepted, cases in ((True, valid), (False, invalid)):
                for mime_type, payload in cases:
                    with self.subTest(accepted=accepted, mime_type=mime_type, payload=payload):
                        changed = deepcopy(rounds)
                        changed["rounds"][0]["readings"][0]["capture"].update(
                            mime_type=mime_type, sha256=hashlib.sha256(payload).hexdigest(), byte_length=len(payload))
                        target.write_bytes(payload)
                        if accepted:
                            research.validate_rounds(changed, self.records, self.claims, root, require_capture_files=True)
                        else:
                            with self.assertRaises(research.ValidationError):
                                research.validate_rounds(changed, self.records, self.claims, root)

    def test_round_captures_report_missing_bytes_and_reject_corruption_and_traversal(self):
        rounds, payload = self.review_round()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            stats = research.validate_rounds(rounds, self.records, self.claims, root)
            self.assertEqual((stats["captures_checked"], stats["captures_missing"]), (0, 1))
            with self.assertRaisesRegex(research.ValidationError, "required capture file"):
                research.validate_rounds(rounds, self.records, self.claims, root, require_capture_files=True)
            capture = rounds["rounds"][0]["readings"][0]["capture"]
            target = root / capture["capture_path"]
            target.parent.mkdir()
            target.write_bytes(payload)
            stats = research.validate_rounds(rounds, self.records, self.claims, root, require_capture_files=True)
            self.assertEqual((stats["captures_checked"], stats["captures_missing"]), (1, 0))
            target.write_bytes(payload + b"changed")
            with self.assertRaisesRegex(research.ValidationError, "hash/length mismatch"):
                research.validate_rounds(rounds, self.records, self.claims, root)
            for field, value in (("capture_path", ".source-captures/../../outside.pdf"), ("byte_length", True),
                                 ("sha256", "invented"), ("retrieved_at", "2026-11-14")):
                with self.subTest(field=field):
                    changed = deepcopy(rounds)
                    changed["rounds"][0]["readings"][0]["capture"][field] = value
                    with self.assertRaises(research.ValidationError):
                        research.validate_rounds(changed, self.records, self.claims, root)

    def test_round_roles_do_not_force_claim_support_or_inflate_full_reading(self):
        rounds, _ = self.review_round()
        event = rounds["rounds"][0]["readings"][0]
        event.update(reading_depth="Selected sections", coverage_effect="scoped_review")
        progress = research.round_coverage(self.rows, rounds)
        self.assertEqual(progress["full_additions"], set())
        self.assertEqual(progress["effective"][event["citation_key"]], "Selected sections")
        summary = research.generate_summary(self.rows, self.claims, rounds)
        self.assertIn("**1** have an explicit non-claim relevance decision", summary)
        self.assertIn("**0** retain an unresolved role", summary)
        self.assertIn("**0** that lacked an inherited full-text label", summary)
        self.assertIn("background", summary)
        self.assertEqual(summary.count("| Canonical citation key |"), 1)
        rendered = research.generate_rounds(rounds, {})
        self.assertIn("no claim support forced", rendered)
        self.assertIn("No outcome effect estimated", rendered)
        self.assertIn("not_performed", rendered)
        self.assertIn(event["relevance_note"], rendered)

    def test_round_view_is_optional_for_old_payloads_and_detects_stale_findings(self):
        rounds, _ = self.review_round()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = self.write_fixture(root, rounds)
            research.build(root)
            research.build(root, check=True)
            self.assertTrue((target / "rounds.md").is_file())
            changed = deepcopy(rounds)
            changed["rounds"][0]["readings"][0]["findings"].append("A materially different finding.")
            (target / "rounds.yaml").write_text(yaml.safe_dump(changed), encoding="utf-8")
            with self.assertRaisesRegex(research.ValidationError, "rounds.md: missing or stale"):
                research.build(root, check=True)


if __name__ == "__main__":
    unittest.main()
