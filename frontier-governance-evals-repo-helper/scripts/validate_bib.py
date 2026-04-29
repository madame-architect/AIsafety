#!/usr/bin/env python3
"""
Validate a BibLaTeX bibliography against repo conventions.

Usage:
    python scripts/validate_bib.py frontier-governance-evals.bib bibliography.taxonomy.yml
    python scripts/validate_bib.py frontier-governance-evals.bib bibliography.taxonomy.yml --strict

The parser is intentionally lightweight but handles balanced-brace BibLaTeX field values.
PyYAML is optional. When available, the script uses bibliography.taxonomy.yml to check
unknown keyword tags and field conventions.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_REQUIRED_FIELDS = ["author", "title", "keywords", "review_status", "issuer_type", "annotation"]
DEFAULT_REQUIRED_EXACTLY_ONE = ["document_type", "source_status", "evidence_basis"]
DEFAULT_RECOMMENDED_EXACTLY_ONE = ["review_status", "issuer_type"]
DEFAULT_MIRROR_FIELDS = ["review_status", "issuer_type"]


@dataclass
class Entry:
    entry_type: str
    key: str
    fields: dict[str, str]

    @property
    def keywords(self) -> list[str]:
        raw = self.fields.get("keywords", "")
        return [part.strip() for part in raw.split(",") if part.strip()]


def find_entries(text: str) -> list[str]:
    """Return raw @entry blocks by matching balanced top-level braces."""
    blocks: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        at = text.find("@", i)
        if at == -1:
            break
        # Skip comments or accidental @ characters that are not BibTeX entries.
        m = re.match(r"@\s*[A-Za-z]+\s*\{", text[at:])
        if not m:
            i = at + 1
            continue
        start_brace = at + m.end() - 1
        depth = 0
        j = start_brace
        while j < n:
            ch = text[j]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    blocks.append(text[at : j + 1])
                    i = j + 1
                    break
            j += 1
        else:
            raise ValueError(f"Unclosed entry starting near character {at}")
    return blocks


def read_balanced_value(body: str, pos: int) -> tuple[str, int]:
    """Read a BibLaTeX value starting at body[pos]."""
    n = len(body)
    while pos < n and body[pos].isspace():
        pos += 1
    if pos >= n:
        return "", pos

    if body[pos] == "{":
        depth = 0
        start = pos + 1
        pos += 1
        while pos < n:
            if body[pos] == "{":
                depth += 1
            elif body[pos] == "}":
                if depth == 0:
                    return body[start:pos], pos + 1
                depth -= 1
            pos += 1
        raise ValueError("Unclosed braced field value")

    if body[pos] == '"':
        start = pos + 1
        pos += 1
        escaped = False
        while pos < n:
            ch = body[pos]
            if ch == '"' and not escaped:
                return body[start:pos], pos + 1
            escaped = (ch == "\\" and not escaped)
            if ch != "\\":
                escaped = False
            pos += 1
        raise ValueError("Unclosed quoted field value")

    start = pos
    while pos < n and body[pos] not in ",\n\r":
        pos += 1
    return body[start:pos].strip(), pos


def parse_entry(block: str) -> Entry:
    header = re.match(r"@\s*([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", block, re.S)
    if not header:
        raise ValueError(f"Could not parse entry header: {block[:80]!r}")
    entry_type, key = header.group(1).lower(), header.group(2)
    body = block[header.end() : block.rfind("}")]

    fields: dict[str, str] = {}
    pos = 0
    n = len(body)
    while pos < n:
        while pos < n and (body[pos].isspace() or body[pos] == ","):
            pos += 1
        if pos >= n:
            break
        name_match = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\s*=", body[pos:])
        if not name_match:
            # Move forward to avoid an infinite loop. This also tolerates comments.
            pos += 1
            continue
        name = name_match.group(1).lower()
        pos += name_match.end()
        value, pos = read_balanced_value(body, pos)
        fields[name] = " ".join(value.split())
        while pos < n and body[pos] != ",":
            if not body[pos].isspace():
                break
            pos += 1
        if pos < n and body[pos] == ",":
            pos += 1
    return Entry(entry_type=entry_type, key=key, fields=fields)


def parse_bib(path: Path) -> list[Entry]:
    text = path.read_text(encoding="utf-8")
    return [parse_entry(block) for block in find_entries(text)]


def load_taxonomy(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    try:
        import yaml  # type: ignore
    except Exception:
        print("warning: PyYAML is not installed; skipping taxonomy YAML checks", file=sys.stderr)
        return {}
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def taxonomy_settings(taxonomy: dict[str, Any]) -> tuple[list[str], list[str], list[str], set[str]]:
    fields = taxonomy.get("fields", {}) if taxonomy else {}
    keyword_taxonomy = taxonomy.get("keyword_taxonomy", {}) if taxonomy else {}

    required_fields = list(fields.get("required_all_entries", DEFAULT_REQUIRED_FIELDS))
    required_exactly_one = list(keyword_taxonomy.get("required_exactly_one", DEFAULT_REQUIRED_EXACTLY_ONE))
    recommended_exactly_one = list(keyword_taxonomy.get("recommended_exactly_one", DEFAULT_RECOMMENDED_EXACTLY_ONE))

    allowed_tags: set[str] = set()
    namespaces = keyword_taxonomy.get("namespaces", {})
    if isinstance(namespaces, dict):
        for namespace, spec in namespaces.items():
            for value in (spec or {}).get("allowed", []) or []:
                allowed_tags.add(f"{namespace}/{value}")

    return required_fields, required_exactly_one, recommended_exactly_one, allowed_tags


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a BibLaTeX bibliography.")
    parser.add_argument("bibfile", type=Path)
    parser.add_argument("taxonomy", type=Path, nargs="?", help="Optional bibliography.taxonomy.yml")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    entries = parse_bib(args.bibfile)
    taxonomy = load_taxonomy(args.taxonomy)
    required_fields, required_exactly_one, recommended_exactly_one, allowed_tags = taxonomy_settings(taxonomy)

    errors: list[str] = []
    warnings: list[str] = []

    key_counts = Counter(entry.key for entry in entries)
    for key, count in sorted(key_counts.items()):
        if count > 1:
            errors.append(f"duplicate citation key: {key} ({count} occurrences)")

    for entry in entries:
        for field in required_fields:
            if not entry.fields.get(field):
                errors.append(f"{entry.key}: missing required field `{field}`")

        keywords = entry.keywords
        for namespace in required_exactly_one:
            matches = [kw for kw in keywords if kw.startswith(f"{namespace}/")]
            if len(matches) != 1:
                errors.append(f"{entry.key}: expected exactly one `{namespace}/*` keyword, found {len(matches)}")

        for namespace in recommended_exactly_one:
            matches = [kw for kw in keywords if kw.startswith(f"{namespace}/")]
            if len(matches) != 1:
                warnings.append(f"{entry.key}: expected one `{namespace}/*` keyword, found {len(matches)}")

        for field in DEFAULT_MIRROR_FIELDS:
            value = entry.fields.get(field)
            if value and f"{field}/{value}" not in keywords:
                warnings.append(f"{entry.key}: `{field}` field is `{value}` but keyword `{field}/{value}` is missing")

        if allowed_tags:
            for kw in keywords:
                if "/" in kw and kw not in allowed_tags:
                    warnings.append(f"{entry.key}: unknown keyword tag `{kw}`")

    entry_type_counts = Counter(entry.entry_type for entry in entries)
    print(f"Validated {len(entries)} entries in {args.bibfile}")
    print("Entry types: " + ", ".join(f"@{k}={v}" for k, v in sorted(entry_type_counts.items())))

    if errors:
        print("\nErrors:")
        for msg in errors:
            print(f"  - {msg}")

    if warnings:
        print("\nWarnings:")
        for msg in warnings:
            print(f"  - {msg}")

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
