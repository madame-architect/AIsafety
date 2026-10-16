"""Regression checks for data preservation and failures that can corrupt a release."""
from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
from datetime import date
from io import StringIO
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import build
import lint_bibliography as lint


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.schema = {
            "schema_version": build.SCHEMA_VERSION,
            "entry_types": ["misc", "report"],
            "keyword_mirror_policy": {"current_fields": ["synthesis_stream", "risk_domain"], "retained_legacy_fields": []},
            "fields": {
                "synthesis_stream": {"required": True, "multivalue": False, "values": list(build.STREAMS)},
                "stream_note": {"required": True, "multivalue": False},
                "risk_domain": {"required": False, "multivalue": True, "values": ["cyber", "autonomy"]},
            },
        }
        self.data = {
            "schema_version": build.SCHEMA_VERSION,
            "records": [
                {"id": "study_2026", "entry_type": "misc", "fields": {
                    "author": r'{Frontier {AI} Group} and J{\"o}rg Example',
                    "title": 'Tests of {AI}: "quotes", a literal comma, and an unmatched "',
                    "date": "2026-05-01", "urldate": "2026-05-03",
                    "url": "https://example.test/paper?v=1&query=a%2Fb#section",
                    "annotation": '  First line, with = signs.\nSecond line has "quotes", @misc, and {groups}.\n',
                    "evidence_note": r'Escaped \{braces\}, a \% sign, and a double backslash: \\',
                    "risk_domain": ["autonomy", "cyber"],
                    "synthesis_stream": "technical_eval", "stream_note": "A technical evaluation fixture.",
                    "crossref": "policy_2026",
                }},
                {"id": "policy_2026", "entry_type": "report", "fields": {
                    "title": "An official policy", "synthesis_stream": "governance_artifact",
                    "stream_note": "A policy fixture.",
                }},
            ],
        }
        self.write_inputs()

    def write_inputs(self, data=None, schema=None):
        (self.root / build.RECORDS_NAME).write_text(yaml.safe_dump(self.data if data is None else data, sort_keys=False))
        (self.root / build.SCHEMA_NAME).write_text(yaml.safe_dump(self.schema if schema is None else schema, sort_keys=False))

    def snapshot(self):
        return {str(path.relative_to(self.root)): (path.read_bytes(), path.stat().st_mtime_ns)
                for path in self.root.rglob("*") if path.is_file()}

    def test_preserves_every_literal_and_partitions_views(self):
        count, changed = build.build(self.root)
        self.assertEqual(count, 2)
        self.assertEqual(len(changed), 5)
        bibliography = (self.root / build.BIB_NAME).read_text()
        self.assertTrue(bibliography.endswith("\n"))
        self.assertFalse(bibliography.endswith("\n\n"))
        entries = lint.parse_bib(bibliography)
        parsed = {key: (entry_type, fields) for entry_type, key, fields in entries}
        for original in self.data["records"]:
            entry_type, fields = parsed[original["id"]]
            self.assertEqual(entry_type, original["entry_type"])
            for field, value in original["fields"].items():
                expected = ", ".join(value) if isinstance(value, list) else value
                self.assertEqual(lint.strip_outer(fields[field]), expected, field)
        self.assertEqual(lint.split_values(parsed["study_2026"][1]["keywords"]), [
            "synthesis_stream/technical_eval", "risk_domain/autonomy", "risk_domain/cyber"])
        view_ids = []
        for stream, (filename, _) in build.STREAMS.items():
            view = lint.parse_bib((self.root / "views" / filename).read_text())
            for _, key, fields in view:
                self.assertEqual(lint.strip_outer(fields["synthesis_stream"]), stream)
                self.assertEqual(fields, parsed[key][1])
                view_ids.append(key)
        self.assertCountEqual(view_ids, parsed)
        self.assertEqual(build.build(self.root), (2, []))

    def test_check_is_read_only_and_detects_missing_or_stale_exports(self):
        before = self.snapshot()
        count, missing = build.build(self.root, check=True)
        self.assertEqual((count, len(missing)), (2, 5))
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / "views").exists())
        build.build(self.root)
        target = self.root / build.BIB_NAME
        target.write_bytes(target.read_bytes() + b"% manual edit\n")
        before = self.snapshot()
        with redirect_stderr(StringIO()), redirect_stdout(StringIO()):
            code = build.main(["--root", str(self.root), "--check"])
        self.assertEqual(code, 1)
        self.assertEqual(self.snapshot(), before)
        build.build(self.root)
        self.assertEqual(build.build(self.root, check=True), (2, []))

    def test_rejects_shape_type_enum_and_literal_corruption(self):
        cases = [
            ("missing records", lambda d: d.pop("records"), "missing keys"),
            ("empty records", lambda d: d.update(records=[]), "nonempty list"),
            ("unknown root field", lambda d: d.update(extra="hidden"), "unexpected keys"),
            ("version mismatch", lambda d: d.update(schema_version="v2"), "schema_version"),
            ("duplicate id", lambda d: d["records"].append(deepcopy(d["records"][0])), "duplicate record id"),
            ("entry injection", lambda d: d["records"][0].update(entry_type="misc} @misc{evil"), "entry_type"),
            ("id injection", lambda d: d["records"][0].update(id="x, title={evil}"), "citation id"),
            ("unknown record field", lambda d: d["records"][0].update(extra=True), "unexpected keys"),
            ("missing title", lambda d: d["records"][0]["fields"].pop("title"), "required field title"),
            ("numeric scalar", lambda d: d["records"][0]["fields"].update(date=2026), "string"),
            ("timestamp scalar", lambda d: d["records"][0]["fields"].update(date=date(2026, 5, 1)), "string"),
            ("boolean scalar", lambda d: d["records"][0]["fields"].update(stream_note=True), "string"),
            ("scalar as list", lambda d: d["records"][0]["fields"].update(title=["oops"]), "string"),
            ("list as scalar", lambda d: d["records"][0]["fields"].update(risk_domain="cyber"), "list"),
            ("invalid enum", lambda d: d["records"][0]["fields"].update(risk_domain=["unlisted"]), "uncontrolled"),
            ("empty list", lambda d: d["records"][0]["fields"].update(risk_domain=[]), "nonempty list"),
            ("duplicate enum", lambda d: d["records"][0]["fields"].update(risk_domain=["cyber", "cyber"]), "duplicate"),
            ("keywords entered", lambda d: d["records"][0]["fields"].update(keywords="risk_domain/cyber"), "generated"),
            ("field injection", lambda d: d["records"][0]["fields"].update({"evil} @misc{": "x"}), "field name"),
            ("closing brace", lambda d: d["records"][0]["fields"].update(title="} @misc{evil"), "brace"),
            ("unclosed brace", lambda d: d["records"][0]["fields"].update(title="An {unclosed group"), "brace"),
            ("terminal escape", lambda d: d["records"][0]["fields"].update(title="An escape\\"), "backslash"),
            ("control character", lambda d: d["records"][0]["fields"].update(title="x\x00y"), "control"),
            ("missing crossref", lambda d: d["records"][0]["fields"].update(crossref="not_present"), "missing key"),
            ("bad date", lambda d: d["records"][0]["fields"].update(date="2026-02-30"), "invalid date"),
        ]
        for label, mutate, message in cases:
            with self.subTest(label=label):
                broken = deepcopy(self.data)
                mutate(broken)
                self.write_inputs(broken)
                before = self.snapshot()
                with self.assertRaisesRegex(ValueError, message):
                    build.build(self.root)
                self.assertEqual(self.snapshot(), before)

    def test_duplicate_yaml_keys_and_invalid_mirror_policy_fail(self):
        (self.root / build.RECORDS_NAME).write_text("")
        with self.assertRaisesRegex(ValueError, "records root must be a mapping"):
            build.build(self.root)
        for filename, addition in [
            (build.RECORDS_NAME, "\nrecords: []\n"),
            (build.SCHEMA_NAME, "\nentry_types: [misc]\n"),
        ]:
            with self.subTest(filename=filename):
                self.write_inputs()
                path = self.root / filename
                path.write_text(path.read_text() + addition)
                with self.assertRaisesRegex(ValueError, "duplicate YAML key"):
                    build.build(self.root)
        self.write_inputs()
        path = self.root / build.RECORDS_NAME
        path.write_text(path.read_text().replace("    title:", "    title: duplicate\n    title:", 1))
        with self.assertRaisesRegex(ValueError, "duplicate YAML key"):
            build.build(self.root)
        invalid = deepcopy(self.schema)
        invalid["keyword_mirror_policy"]["current_fields"].append("undeclared")
        self.write_inputs(schema=invalid)
        with self.assertRaisesRegex(ValueError, "not declared"):
            build.build(self.root)

    def test_linter_rejects_orphan_keywords_and_duplicate_bibtex_fields(self):
        schema = lint.load_schema(self.root / build.SCHEMA_NAME)
        entries = build.load_records(self.root, schema)
        self.assertFalse(lint.validate_entries(entries, schema))
        entries[0][2]["keywords"] = "{synthesis_stream/governance_artifact, risk_domain/cyber}"
        self.assertTrue(any("no matching field value" in failure for failure in lint.validate_entries(entries, schema)))
        with self.assertRaisesRegex(ValueError, "duplicate field"):
            lint.parse_bib('@misc{x, title={One}, TITLE={Two}}')
        self.assertTrue(lint.validate_entries([], schema))


if __name__ == "__main__":
    unittest.main()
