"""Checks for faithful policy observations and an explicitly opt-in export."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import build_commitments


class CommitmentTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.research = self.root / "research" / "cyber-deployment"
        self.research.mkdir(parents=True)
        self.target = self.research / "commitment-history.md"
        self.records = {
            "schema_version": "frontier-governance-evals-v3",
            "records": [{
                "id": "policy_fixture", "entry_type": "report",
                "fields": {
                    "title": "A mutable policy record",
                    "url": "https://example.test/current-policy",
                    "date": "2001-01-02", "version": "current-v99",
                },
            }],
        }
        snapshots = []
        for number, published in enumerate(("2025", "2026-02", None), start=1):
            snapshot = {
                "id": f"snapshot_{number}", "record_id": "policy_fixture",
                "source_url": f"https://example.test/inspected-policy/{number}",
                "version_claim": f"inspected-v{number}",
                "observed_on": f"2026-05-{number + 6:02d}",
                "inspection_scope": "Only the cyber deployment section was inspected.",
                "preservation_note": "Live page inspected; no archival copy was captured.",
                "original_url": f"https://example.test/inspected-policy/{number}",
                "retrieved_at": f"2026-05-{number + 6:02d}T12:00:00Z",
                "archive_url": None, "archive_checked_on": None,
                "archive_unavailable_reason": "Archive service unavailable; local bytes retained outside Git.",
                "sha256": "a" * 64, "byte_length": 128, "mime_type": "application/pdf",
                "published_on": None, "locator_basis": "One-based PDF viewer pages including cover.",
                "preservation_status": "captured",
            }
            if published is not None:
                snapshot["published_on"] = published
            snapshots.append(snapshot)
        self.evidence = {
            "schema_version": "cyber-commitment-evidence-v2", "snapshots": snapshots,
        }
        initial = {
            "id": "observation_1", "commitment_id": "cyber_release",
            "snapshot_id": "snapshot_1", "issuer": "Fixture Institute",
            "evidence_kind": "policy_statement", "modality": "requirement",
            "scope": "Hosted cyber-capable models only.",
            "trigger": "Before releasing a model above the stated capability threshold.",
            "action": "Review the deployment safeguards.",
            "qualifications": "Subject to further testing; exceptions remain possible.\nAn unmatched { is ordinary policy text.",
            "locator": "Cyber section, paragraph 2.", "change_type": "observed",
        }
        revision = dict(
            initial, id="observation_2", snapshot_id="snapshot_2", change_type="revised",
            previous_observation_id="observation_1",
            trigger="Before release and after a material change in capability.",
            change_note="Analyst comparison: a post-deployment review trigger was added.",
            source_rationale="Source explanation: the policy cites improved detection.",
            claimed_application_on="2026-04-01",
            application_date_note="Source-stated applicability; retrospective coverage is unverified.",
        )
        independent = dict(
            initial, id="observation_3", commitment_id="weight_release",
            snapshot_id="snapshot_3", modality="discretionary",
            action="May withhold model weights.",
        )
        self.commitments = {
            "schema_version": "cyber-commitments-v1",
            "observations": [initial, revision, independent],
        }
        self.write_inputs()

    def write_inputs(self, evidence=None, commitments=None, records=None):
        documents = {
            self.root / "records.yaml": self.records if records is None else records,
            self.research / "evidence.yaml": self.evidence if evidence is None else evidence,
            self.research / "commitments.yaml": self.commitments if commitments is None else commitments,
        }
        for path, value in documents.items():
            path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")

    def files(self):
        return {
            path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mtime_ns)
            for path in self.root.rglob("*") if path.is_file()
        }

    def cli(self, *flags):
        return subprocess.run(
            [sys.executable, "-B", str(SCRIPTS / "build_commitments.py"),
             "--root", str(self.root), *flags],
            capture_output=True, text=True, check=False,
        )

    def test_pilot_preserves_caveats_and_distinguishes_dates(self):
        before = self.files()
        markdown, counts = build_commitments.generate_history(self.root)
        self.assertEqual(self.files(), before)
        self.assertEqual(build_commitments.generate_history(self.root), (markdown, counts))
        self.assertIsInstance(counts, dict)
        for text in (
            "Hosted cyber-capable models only.",
            "Subject to further testing; exceptions remain possible.",
            "An unmatched { is ordinary policy text.",
            "Only the cyber deployment section was inspected.",
            "Live page inspected; no archival copy was captured.",
            "May withhold model weights.",
            "Source-stated applicability; retrospective coverage is unverified.",
            "2025", "2026-02", "2026-05-07", "2026-05-08", "2026-05-09", "2026-04-01",
        ):
            self.assertIn(text, markdown)
        self.assertNotIn("2025-01-01", markdown)
        self.assertNotIn("2026-02-01", markdown)
        self.assertRegex(markdown, r"(?i)(?:published|publication)[^\n]*Not recorded")
        self.assertRegex(markdown, r"(?i)application[^\n]*Not recorded")
        self.assertRegex(markdown, r"(?i)observed[^\n]*2026-05-07")
        self.assertRegex(markdown, r"(?i)application[^\n]*2026-04-01")
        note = self.commitments["observations"][1]["change_note"]
        rationale = self.commitments["observations"][1]["source_rationale"]
        self.assertIn(note, markdown)
        self.assertIn(rationale, markdown)
        self.assertNotEqual(
            next(line for line in markdown.splitlines() if note in line),
            next(line for line in markdown.splitlines() if rationale in line),
        )
        self.assertIn("policy wording", markdown.lower())
        self.assertRegex(markdown, r"(?is)implementation.{0,100}effectiveness.{0,100}not assessed")

    def test_rejects_corrupt_inputs_without_writing(self):
        cases = [
            ("duplicate snapshot id", lambda e, c, r: e["snapshots"].append(deepcopy(e["snapshots"][0]))),
            ("duplicate observation id", lambda e, c, r: c["observations"].append(deepcopy(c["observations"][0]))),
            ("unknown record", lambda e, c, r: e["snapshots"][0].update(record_id="missing")),
            ("unknown snapshot", lambda e, c, r: c["observations"][0].update(snapshot_id="missing")),
            ("unknown predecessor", lambda e, c, r: c["observations"][1].update(previous_observation_id="missing")),
            ("invalid publication date", lambda e, c, r: e["snapshots"][0].update(published_on="2025-02-30")),
            ("partial observation date", lambda e, c, r: e["snapshots"][0].update(observed_on="2026-05")),
            ("invalid application date", lambda e, c, r: c["observations"][1].update(claimed_application_on="2026-02-30")),
            ("application date without explanation", lambda e, c, r: c["observations"][1].pop("application_date_note")),
            ("invalid hash", lambda e, c, r: e["snapshots"][0].update(sha256="A" * 64)),
            ("invalid modality", lambda e, c, r: c["observations"][0].update(modality="must")),
            ("invalid evidence kind", lambda e, c, r: c["observations"][0].update(evidence_kind="implementation")),
            ("invalid change type", lambda e, c, r: c["observations"][0].update(change_type="updated")),
            ("other commitment predecessor", lambda e, c, r: c["observations"][1].update(previous_observation_id="observation_3")),
            ("other issuer predecessor", lambda e, c, r: c["observations"][1].update(issuer="Other Institute")),
            ("self predecessor", lambda e, c, r: c["observations"][1].update(previous_observation_id="observation_2")),
            ("cycle", lambda e, c, r: c["observations"][0].update(
                change_type="revised", previous_observation_id="observation_2", change_note="Creates a cycle.")),
            ("revision without predecessor", lambda e, c, r: c["observations"][1].pop("previous_observation_id")),
            ("revision without explanation", lambda e, c, r: c["observations"][1].pop("change_note")),
            ("observed with change note", lambda e, c, r: c["observations"][0].update(change_note="Not a transition.")),
            ("unpaired archive", lambda e, c, r: e["snapshots"][0].update(archive_url="https://example.test/archive")),
            ("null mandatory digest", lambda e, c, r: e["snapshots"][0].update(sha256=None)),
            ("numeric optional value", lambda e, c, r: e["snapshots"][0].update(version_claim=1)),
            ("missing provenance key", lambda e, c, r: e["snapshots"][0].pop("retrieved_at")),
            ("timezone absent", lambda e, c, r: e["snapshots"][0].update(retrieved_at="2026-05-07T12:00:00")),
            ("retrieval after inspection", lambda e, c, r: e["snapshots"][0].update(retrieved_at="2026-05-08T12:00:00Z")),
            ("boolean length", lambda e, c, r: e["snapshots"][0].update(byte_length=True)),
            ("zero length", lambda e, c, r: e["snapshots"][0].update(byte_length=0)),
            ("invented legacy exception", lambda e, c, r: e["snapshots"][0].update(preservation_status="legacy_uncaptured")),
            ("live URL as archive", lambda e, c, r: e["snapshots"][0].update(archive_url=e["snapshots"][0]["original_url"], archive_checked_on="2026-05-07")),
            ("unexplained missing archive", lambda e, c, r: e["snapshots"][0].pop("archive_unavailable_reason")),
            ("HTML without retained representation", lambda e, c, r: e["snapshots"][0].update(mime_type="text/html")),
            ("empty required value", lambda e, c, r: c["observations"][0].update(qualifications="")),
        ]
        for label, mutate in cases:
            with self.subTest(label=label):
                evidence, commitments, records = deepcopy((self.evidence, self.commitments, self.records))
                mutate(evidence, commitments, records)
                self.write_inputs(evidence, commitments, records)
                before = self.files()
                with self.assertRaises((ValueError, yaml.YAMLError)):
                    build_commitments.generate_history(self.root)
                self.assertEqual(self.files(), before)
        for relative, key in (
            ("records.yaml", "records"),
            ("research/cyber-deployment/evidence.yaml", "snapshots"),
            ("research/cyber-deployment/commitments.yaml", "observations"),
        ):
            with self.subTest(duplicate_yaml_key=relative):
                self.write_inputs()
                path = self.root / relative
                path.write_text(path.read_text(encoding="utf-8") + f"\n{key}: []\n", encoding="utf-8")
                before = self.files()
                with self.assertRaises((ValueError, yaml.YAMLError)):
                    build_commitments.generate_history(self.root)
                self.assertEqual(self.files(), before)

    def test_cli_requires_write_and_check_never_writes(self):
        before = self.files()
        result = self.cli()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.files(), before)
        result = self.cli("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.files(), before)
        result = self.cli("--write")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        after = self.files()
        self.assertEqual(set(after) - set(before), {"research/cyber-deployment/commitment-history.md"})
        self.assertEqual({name: after[name] for name in before}, before)
        markdown, _ = build_commitments.generate_history(self.root)
        self.assertEqual(self.target.read_bytes(), markdown.encode("utf-8"))
        result = self.cli("--check")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.files(), after)
        self.target.write_bytes(self.target.read_bytes() + b"\nManual edit.\n")
        stale = self.files()
        result = self.cli("--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.files(), stale)


if __name__ == "__main__":
    unittest.main()

