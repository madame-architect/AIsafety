#!/usr/bin/env python3
"""Validate authoritative YAML and deterministically generate BibLaTeX views.

Run from anywhere; paths default to the repository containing this script.
`--check` compares outputs in memory and never writes files or directories.
Only schema-declared controlled multivalue fields use YAML string lists.
All other field contents are literal strings, without BibTeX outer braces.
"""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys
from typing import Sequence

# A fresh --check invocation must not create local import caches either.
sys.dont_write_bytecode = True

import yaml

import lint_bibliography as lint

SCHEMA_VERSION = "frontier-governance-evals-v3"
SCHEMA_NAME = "frontier-governance-evals-schema.yml"
RECORDS_NAME = "records.yaml"
BIB_NAME = "frontier-governance-evals.bib"
STREAMS = {
    "technical_eval": ("technical-evals.bib", "Technical evaluations"),
    "governance_artifact": ("governance-artifacts.bib", "Governance artifacts"),
    "contextual": ("contextual.bib", "Contextual sources"),
}
ID_RE = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.:+/-]*\Z")
FIELD_RE = re.compile(r"[a-z][a-z0-9_]*\Z")
Entry = tuple[str, str, dict[str, str]]


def exact_keys(value: object, expected: set[str], label: str) -> dict:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be a mapping")
    if set(value) != expected:
        missing = sorted(expected - set(value))
        extra = sorted(repr(key) for key in set(value) - expected)
        raise ValueError(f"{label}: missing keys {missing}; unexpected keys {extra}")
    return value


def check_literal(value: object, label: str) -> str:
    """Prevent a field from escaping its generated BibTeX brace wrapper."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty string (quote dates and numbers in YAML)")
    depth = 0
    escaped = False
    for char in value:
        if (ord(char) < 32 and char not in "\n\t") or ord(char) == 127:
            raise ValueError(f"{label} contains an unsupported control character")
        if escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                raise ValueError(f"{label} has an unmatched closing brace")
    if depth:
        raise ValueError(f"{label} has unclosed braces")
    if escaped:
        raise ValueError(f"{label} ends in an unpaired backslash")
    return value


def load_records(root: Path, schema: lint.SchemaConfig) -> list[Entry]:
    data = exact_keys(lint.read_yaml(root / RECORDS_NAME), {"schema_version", "records"}, "records root")
    if schema.schema_version != SCHEMA_VERSION or data["schema_version"] != schema.schema_version:
        raise ValueError(f"records and schema must both declare schema_version: {SCHEMA_VERSION}")
    if not schema.entry_types:
        raise ValueError("schema must declare a nonempty entry_types allowlist")
    if not schema.multivalue_fields <= schema.controlled.keys():
        raise ValueError("schema multivalue fields must declare controlled values")
    if "keywords" in schema.keyword_fields:
        raise ValueError("keywords cannot itself be a keyword mirror field")
    records = data["records"]
    if not isinstance(records, list) or not records:
        raise ValueError("records must be a nonempty list")

    entries: list[Entry] = []
    seen: set[str] = set()
    for number, raw_record in enumerate(records, 1):
        record = exact_keys(raw_record, {"id", "entry_type", "fields"}, f"record {number}")
        key = record["id"]
        if not isinstance(key, str) or not ID_RE.fullmatch(key):
            raise ValueError(f"record {number} has an invalid citation id: {key!r}")
        if key in seen:
            raise ValueError(f"duplicate record id: {key}")
        seen.add(key)
        entry_type = record["entry_type"]
        if not isinstance(entry_type, str) or entry_type not in schema.entry_types:
            raise ValueError(f"{key}: entry_type {entry_type!r} is not allowed by the schema")
        raw_fields = record["fields"]
        if not isinstance(raw_fields, dict) or not raw_fields:
            raise ValueError(f"{key}: fields must be a nonempty mapping")
        for required in ("title", "synthesis_stream", "stream_note"):
            if required not in raw_fields:
                raise ValueError(f"{key}: missing required field {required}")
        if "keywords" in raw_fields:
            raise ValueError(f"{key}: remove fields.keywords; keywords are generated from the schema mirror policy")

        values: dict[str, list[str]] = {}
        unwrapped: dict[str, str] = {}
        for field, raw_value in raw_fields.items():
            if not isinstance(field, str) or not FIELD_RE.fullmatch(field):
                raise ValueError(f"{key}: invalid field name {field!r}")
            label = f"{key}.{field}"
            if field in schema.multivalue_fields:
                if not isinstance(raw_value, list) or not raw_value:
                    raise ValueError(f"{label} must be a nonempty list of strings")
                parts = [check_literal(part, label) for part in raw_value]
                if len(parts) != len(set(parts)):
                    raise ValueError(f"{label} contains duplicate values")
                values[field] = parts
                unwrapped[field] = ", ".join(parts)
            else:
                unwrapped[field] = check_literal(raw_value, label)
                values[field] = [unwrapped[field]]
            if field in schema.controlled:
                for part in values[field]:
                    if part not in schema.controlled[field]:
                        raise ValueError(f"{label} has uncontrolled value {part!r}")
        if unwrapped["synthesis_stream"] not in STREAMS:
            raise ValueError(f"{key}: unsupported synthesis_stream {unwrapped['synthesis_stream']!r}")
        keywords = [f"{field}/{part}" for field in schema.keyword_fields for part in values.get(field, [])]
        if keywords:
            unwrapped["keywords"] = ", ".join(keywords)
        entries.append((entry_type, key, {field: "{" + value + "}" for field, value in sorted(unwrapped.items())}))

    entries.sort(key=lambda entry: entry[1])
    failures = lint.validate_entries(entries, schema)
    if failures:
        raise ValueError(f"{len(failures)} semantic validation failure(s):\n- " + "\n- ".join(failures))
    return entries


def render_bib(entries: Sequence[Entry], stream: str | None = None) -> str:
    lines = [
        "% Generated from records.yaml; do not edit this file directly.",
        "% Regenerate with: python3 scripts/build.py",
        f"% Schema: {SCHEMA_VERSION}",
    ]
    if stream is not None:
        lines.extend([f"% Synthesis stream: {stream}", "% Cross-references may resolve in frontier-governance-evals.bib."])
    lines.append("")
    for entry_type, key, fields in entries:
        lines.append(f"@{entry_type}{{{key},")
        lines.extend(f"    {field} = {value}," for field, value in sorted(fields.items()))
        lines.extend(["}", ""])
    # The final empty list item supplies exactly one terminal newline. Field
    # contents are separate items, so this does not trim literal whitespace.
    text = "\n".join(lines)
    if lint.parse_bib(text) != list(entries):
        raise ValueError("generated BibLaTeX did not round-trip to the same literal field values")
    return text


def generate_outputs(root: Path) -> tuple[dict[Path, str], int]:
    """Return fully validated output text without writing to disk."""
    schema = lint.load_schema(root / SCHEMA_NAME)
    entries = load_records(root, schema)
    outputs = {Path(BIB_NAME): render_bib(entries)}
    counts = Counter(lint.strip_outer(fields["synthesis_stream"]) for _, _, fields in entries)
    index = [
        "# Generated bibliography views", "",
        "Generated from [records.yaml](../records.yaml). Run `python3 scripts/build.py` from the repository root to rebuild.", "",
        "| Synthesis stream | Records | BibLaTeX export |",
        "| --- | ---: | --- |",
    ]
    for stream, (filename, label) in STREAMS.items():
        selected = [entry for entry in entries if lint.strip_outer(entry[2]["synthesis_stream"]) == stream]
        outputs[Path("views") / filename] = render_bib(selected, stream)
        index.append(f"| {label} | {counts[stream]} | [{filename}]({filename}) |")
    index.extend([
        f"| **Total** | **{len(entries)}** | [Complete bibliography](../{BIB_NAME}) |", "",
        "The three streams partition the collection: each citation id occurs in exactly one view. "
        "Views retain every field, including classification notes and any references to records in other streams. "
        "Use the complete bibliography when resolving those references.", "",
        "These are source classifications, not quality ratings or evidence of completed source-level review.", "",
    ])
    outputs[Path("views/index.md")] = "\n".join(index)
    return outputs, len(entries)


def build(root: Path, *, check: bool = False) -> tuple[int, list[str]]:
    outputs, count = generate_outputs(root)
    changed: list[str] = []
    for relative, content in outputs.items():
        target = root / relative
        encoded = content.encode("utf-8")
        if target.is_file() and target.read_bytes() == encoded:
            continue
        changed.append(str(relative))
        if not check:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(encoded)
    return count, changed


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate and check generated files without writing")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="Repository directory (defaults to this script's repository)")
    args = parser.parse_args(argv)
    try:
        count, changed = build(args.root, check=args.check)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if args.check and changed:
        print("Generated outputs are missing or stale:\n- " + "\n- ".join(changed), file=sys.stderr)
        print("Run: python3 scripts/build.py", file=sys.stderr)
        return 1
    print(f"Validated {count} records; " + ("all generated outputs match." if args.check else f"updated {len(changed)} generated file(s)."))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
