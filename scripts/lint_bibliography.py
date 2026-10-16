#!/usr/bin/env python3
"""Semantic and advisory linter for frontier-governance-evals.bib.

The schema YAML is the source of truth for controlled vocabularies,
required fields, multivalue fields, keyword mirror fields, and retained
legacy keyword fields.
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date as date_cls
from pathlib import Path
from typing import Mapping, Sequence
from urllib.parse import parse_qsl, urlsplit, urlunsplit

import yaml

DATE_FIELDS = ["date", "origdate", "eventdate", "urldate", "archivedate"]
FULL_DATE_FIELDS = {"urldate", "archivedate"}
UNSTABLE_MAINTENANCE_STATUSES = {"maintained_page", "living_document"}
LIVING_DOCUMENT_STATUSES = {"living_document"}
REMOVED_KEYWORD_PREFIXES = {"document_type", "source_status", "assurance_function"}
URL_FIELDS_FOR_ADVISORY = ("url", "archiveurl")
TRACKING_QUERY_KEYS = {
    "fbclid",
    "gclid",
    "gbraid",
    "wbraid",
    "mc_cid",
    "mc_eid",
    "igshid",
    "msclkid",
    "ref",
    "ref_src",
    "spm",
    "vero_id",
}
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.I)
DOI_PREFIX_RE = re.compile(r"^(?:doi:|https?://(?:dx\.)?doi\.org/)", re.I)
TEX_COMMAND_RE = re.compile(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?")
WORD_RE = re.compile(r"[a-z0-9]+")


class SchemaError(ValueError):
    """Raised when the schema YAML is missing required linter metadata."""


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate keys instead of overwriting data."""


def _unique_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in mapping
        except TypeError as exc:
            raise ValueError(f"YAML mapping key must be scalar at line {key_node.start_mark.line + 1}") from exc
        if duplicate:
            raise ValueError(f"duplicate YAML key {key!r} at line {key_node.start_mark.line + 1}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _unique_mapping)


def read_yaml(path: Path) -> object:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)


@dataclass(frozen=True)
class SchemaConfig:
    path: Path
    schema_version: str
    controlled: dict[str, tuple[str, ...]]
    required_fields: tuple[str, ...]
    multivalue_fields: frozenset[str]
    current_keyword_fields: tuple[str, ...]
    retained_legacy_fields: tuple[str, ...]
    entry_types: tuple[str, ...] = ()

    @property
    def keyword_fields(self) -> tuple[str, ...]:
        return self.current_keyword_fields + self.retained_legacy_fields

    @property
    def allowed_keyword_fields(self) -> frozenset[str]:
        return frozenset(self.keyword_fields)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Lint frontier-governance-evals BibLaTeX entries against the schema YAML."
    )
    parser.add_argument(
        "bib",
        nargs="?",
        type=Path,
        default=Path("frontier-governance-evals.bib"),
        help="BibLaTeX file to lint; default: frontier-governance-evals.bib",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=None,
        help="Schema YAML path; default: frontier-governance-evals-schema.yml next to the .bib or in the repository root",
    )
    parser.add_argument(
        "--no-advisory",
        action="store_true",
        help="Suppress advisory warnings. Semantic failures are still reported.",
    )
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Return a nonzero exit status when advisory warnings are present.",
    )
    parser.add_argument(
        "--stale-urldate-days",
        type=int,
        default=365,
        help="Warn when urldate is older than this many days; set 0 to disable stale-date warnings.",
    )
    parser.add_argument(
        "--fuzzy-title-threshold",
        type=float,
        default=0.94,
        help="Similarity threshold for fuzzy duplicate title warnings, from 0 to 1.",
    )
    parser.add_argument(
        "--max-fuzzy-title-warnings",
        type=int,
        default=50,
        help="Maximum fuzzy duplicate title warnings to print; set 0 to disable fuzzy title warnings.",
    )
    return parser.parse_args(argv[1:])


def find_schema_path(bib_path: Path, explicit_schema: Path | None) -> Path:
    if explicit_schema is not None:
        return explicit_schema

    candidates = [
        bib_path.with_name("frontier-governance-evals-schema.yml"),
        Path(__file__).resolve().parent.parent / "frontier-governance-evals-schema.yml",
        Path.cwd() / "frontier-governance-evals-schema.yml",
    ]
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        if candidate.exists():
            return candidate
    return candidates[0]


def require_mapping(value: object, label: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise SchemaError(f"schema {label} must be a mapping")
    return value


def require_string_list(value: object, label: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise SchemaError(f"schema {label} must be a list")
    result: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise SchemaError(f"schema {label} must contain only strings; got {item!r}")
        result.append(item)
    duplicates = [item for item, count in Counter(result).items() if count > 1]
    if duplicates:
        raise SchemaError(f"schema {label} contains duplicate values: {', '.join(sorted(duplicates))}")
    return tuple(result)


def load_schema(schema_path: Path) -> SchemaConfig:
    if not schema_path.exists():
        raise FileNotFoundError(f"schema YAML not found: {schema_path}")

    data = read_yaml(schema_path)
    root = require_mapping(data, "root")
    fields = require_mapping(root.get("fields"), "fields")
    mirror_policy = require_mapping(root.get("keyword_mirror_policy"), "keyword_mirror_policy")

    current_keyword_fields = require_string_list(
        mirror_policy.get("current_fields"), "keyword_mirror_policy.current_fields"
    )
    retained_legacy_fields = require_string_list(
        mirror_policy.get("retained_legacy_fields"), "keyword_mirror_policy.retained_legacy_fields"
    )
    overlap = set(current_keyword_fields) & set(retained_legacy_fields)
    if overlap:
        raise SchemaError(f"keyword mirror policy repeats fields in both lists: {', '.join(sorted(overlap))}")

    controlled: dict[str, tuple[str, ...]] = {}
    required_fields: list[str] = []
    multivalue_fields: set[str] = set()

    for field_name, raw_spec in fields.items():
        if not isinstance(field_name, str) or not re.fullmatch(r"[a-z][a-z0-9_]*", field_name):
            raise SchemaError(f"schema fields keys must be lowercase field names; got {field_name!r}")
        spec = require_mapping(raw_spec, f"fields.{field_name}")

        for flag in ("required", "multivalue"):
            if flag in spec and not isinstance(spec[flag], bool):
                raise SchemaError(f"schema fields.{field_name}.{flag} must be boolean")
        if spec.get("required", False):
            required_fields.append(field_name)
        if spec.get("multivalue", False):
            multivalue_fields.add(field_name)

        if "values" in spec:
            controlled[field_name] = require_string_list(spec.get("values"), f"fields.{field_name}.values")

    for field in current_keyword_fields + retained_legacy_fields:
        if field not in fields:
            raise SchemaError(f"keyword mirror field {field!r} is not declared under schema fields")
        if field not in controlled:
            raise SchemaError(f"keyword mirror field {field!r} has no controlled values in schema fields")

    schema_version = root.get("schema_version", "")
    if not isinstance(schema_version, str) or not schema_version:
        raise SchemaError("schema schema_version must be a nonempty string")
    entry_types = require_string_list(root.get("entry_types", []), "entry_types")
    if any(not re.fullmatch(r"[a-z]+", value) for value in entry_types):
        raise SchemaError("schema entry_types must be lowercase BibLaTeX type names")
    return SchemaConfig(
        path=schema_path,
        schema_version=schema_version,
        controlled=controlled,
        required_fields=tuple(required_fields),
        multivalue_fields=frozenset(multivalue_fields),
        current_keyword_fields=current_keyword_fields,
        retained_legacy_fields=retained_legacy_fields,
        entry_types=entry_types,
    )


def parse_bib(text: str) -> list[tuple[str, str, dict[str, str]]]:
    """Read literal BibLaTeX records, preserving each value's outer delimiter.

    Quotes inside braced values are literal characters. Quoted values may in
    turn contain braced TeX groups. Macro definitions and concatenation are
    deliberately unsupported: authoritative YAML exports contain literals.
    """
    entries: list[tuple[str, str, dict[str, str]]] = []
    n = len(text)
    i = 0

    def skip_space(pos: int) -> int:
        while pos < n:
            if text[pos].isspace():
                pos += 1
            elif text[pos] == "%":
                end = text.find("\n", pos)
                pos = n if end < 0 else end + 1
            else:
                break
        return pos

    def literal_end(pos: int, key: str) -> int:
        opening = text[pos]
        if opening not in ('{', '"'):
            match = re.match(r"[0-9]+", text[pos:])
            if not match:
                raise ValueError(f"{key}: expected braced, quoted, or numeric literal near offset {pos}")
            return pos + match.end()
        depth = 1 if opening == "{" else 0
        escaped = False
        for end in range(pos + 1, n):
            char = text[end]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth < 0:
                    raise ValueError(f"{key}: unmatched closing brace near offset {end}")
                if opening == "{" and depth == 0:
                    return end + 1
            elif opening == '"' and char == '"' and depth == 0:
                return end + 1
        raise ValueError(f"{key}: unclosed value near offset {pos}")

    while True:
        i = skip_space(i)
        if i >= n:
            break
        match = re.match(r"@([A-Za-z]+)\s*([\{\(])", text[i:])
        if not match:
            raise ValueError(f"Expected BibLaTeX entry near offset {i}")
        entry_type = match.group(1).lower()
        opening = match.group(2)
        closing = "}" if opening == "{" else ")"
        i += match.end()
        if entry_type == "comment":
            depth = 1
            escaped = False
            while i < n and depth:
                char = text[i]
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == opening:
                    depth += 1
                elif char == closing:
                    depth -= 1
                i += 1
            if depth:
                raise ValueError("Unclosed @comment")
            continue
        if entry_type in {"string", "preamble"}:
            raise ValueError(f"@{entry_type} is unsupported; use literal record fields")
        i = skip_space(i)
        key_match = re.match(r"([^,{}()\s]+)\s*,", text[i:])
        if not key_match:
            raise ValueError(f"Missing citation key or comma near offset {i}")
        key = key_match.group(1)
        i += key_match.end()
        fields: dict[str, str] = {}
        while True:
            i = skip_space(i)
            if i >= n:
                raise ValueError(f"Unclosed entry {key}")
            if text[i] == closing:
                i += 1
                break
            field_match = re.match(r"([A-Za-z][A-Za-z0-9_]*)\s*=", text[i:])
            if not field_match:
                raise ValueError(f"{key}: malformed field near offset {i}")
            field = field_match.group(1).lower()
            if field in fields:
                raise ValueError(f"{key}: duplicate field {field}")
            i = skip_space(i + field_match.end())
            if i >= n:
                raise ValueError(f"{key}: missing value for {field}")
            end = literal_end(i, key)
            fields[field] = text[i:end]
            i = skip_space(end)
            if i < n and text[i] == ",":
                i += 1
            elif i >= n or text[i] != closing:
                raise ValueError(f"{key}: expected comma or entry end after {field} near offset {i}")
        entries.append((entry_type, key, fields))
    return entries


def strip_outer(value: str | None) -> str:
    if value is None:
        return ""
    v = value.strip()
    if len(v) >= 2 and ((v[0] == "{" and v[-1] == "}") or (v[0] == '"' and v[-1] == '"')):
        return v[1:-1]
    return v


def split_values(value: str | None) -> list[str]:
    s = strip_outer(value)
    return [p.strip() for p in s.split(",") if p.strip()]


def field_values(fields: Mapping[str, str], field: str) -> list[str]:
    return split_values(fields.get(field, ""))


def has_value(fields: Mapping[str, str], field: str, expected: str) -> bool:
    return expected in field_values(fields, field)


def normalize_url(value: str | None) -> str:
    raw = strip_outer(value).strip().strip("<>")
    if not raw:
        return ""
    parsed = urlsplit(raw)
    if not parsed.scheme or not parsed.netloc:
        return raw.rstrip("/")
    path = parsed.path.rstrip("/") or "/"
    return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.query, parsed.fragment))


def valid_date_part(part: str) -> tuple[bool, str | None]:
    if re.fullmatch(r"\d{4}", part):
        return True, "year"
    month_match = re.fullmatch(r"(\d{4})-(\d{2})", part)
    if month_match:
        month = int(month_match.group(2))
        return 1 <= month <= 12, "month"
    day_match = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", part)
    if day_match:
        year, month, day = map(int, day_match.groups())
        try:
            date_cls(year, month, day)
        except ValueError:
            return False, "day"
        return True, "day"
    return False, None


def valid_bib_date(value: str | None, require_full: bool = False) -> bool:
    s = strip_outer(value).strip()
    if not s:
        return False
    parts = s.split("/")
    if len(parts) > 2 or any(not part for part in parts):
        return False
    granularities = []
    for part in parts:
        ok, granularity = valid_date_part(part)
        if not ok:
            return False
        granularities.append(granularity)
    if len(set(granularities)) > 1:
        return False
    if require_full and granularities[0] != "day":
        return False
    return True


def parse_full_date(value: str | None) -> date_cls | None:
    s = strip_outer(value).strip()
    match = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", s)
    if not match:
        return None
    year, month, day = map(int, match.groups())
    try:
        return date_cls(year, month, day)
    except ValueError:
        return None


def valid_doi(value: str | None) -> bool:
    s = strip_outer(value).strip()
    if not s or DOI_PREFIX_RE.match(s):
        return False
    if any(ch.isspace() for ch in s):
        return False
    return DOI_RE.fullmatch(s) is not None


def validate_entries(entries: Sequence[tuple[str, str, dict[str, str]]], schema: SchemaConfig) -> list[str]:
    failures: list[str] = []
    if not entries:
        failures.append("bibliography contains no records")
    key_counts = Counter(key for _, key, _ in entries)
    keys = set(key_counts)

    for dup_key, count in sorted(key_counts.items()):
        if count > 1:
            failures.append(f"duplicate citation key {dup_key} appears {count} times")

    urls: dict[str, list[str]] = {}
    for _, key, fd in entries:
        url = normalize_url(fd.get("url", ""))
        if url:
            urls.setdefault(url, []).append(key)
    for url, refs in sorted(urls.items()):
        if len(refs) > 1:
            failures.append(f'duplicate url {url}: {", ".join(refs)}')

    for typ, key, fd in entries:
        if not re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_.:+/-]*", key):
            failures.append(f"invalid citation key {key!r}")
        if schema.entry_types and typ not in schema.entry_types:
            failures.append(f"{key}: entry type {typ!r} is not allowed by the schema")
        for field in dict.fromkeys(("title",) + schema.required_fields):
            if not strip_outer(fd.get(field, "")):
                failures.append(f"{key}: missing required field {field}")

        if typ == "online" and not strip_outer(fd.get("urldate", "")):
            failures.append(f"{key}: @online entry missing required urldate")

        for field in DATE_FIELDS:
            if field not in fd:
                continue
            require_full = field in FULL_DATE_FIELDS
            if not valid_bib_date(fd[field], require_full=require_full):
                expected = (
                    "YYYY-MM-DD"
                    if require_full
                    else "YYYY, YYYY-MM, YYYY-MM-DD, or same-granularity range separated by /"
                )
                failures.append(
                    f"{key}: field {field} has invalid date format {strip_outer(fd[field])!r}; expected {expected}"
                )

        if "year" in fd:
            year = strip_outer(fd["year"]).strip()
            if not re.fullmatch(r"\d{4}", year):
                failures.append(f"{key}: field year has invalid date format {year!r}; expected YYYY")
            if "date" in fd:
                failures.append(f"{key}: has both date and year; use date for consistency")

        if "doi" in fd and not valid_doi(fd["doi"]):
            failures.append(f"{key}: field doi has invalid DOI format {strip_outer(fd['doi'])!r}")

        maintenance_status = strip_outer(fd.get("maintenance_status", ""))
        if maintenance_status in UNSTABLE_MAINTENANCE_STATUSES:
            if not strip_outer(fd.get("archiveurl", "")) and not strip_outer(fd.get("evidence_note", "")):
                failures.append(f"{key}: unstable maintained page requires archiveurl or evidence_note")

        for field, allowed_values in sorted(schema.controlled.items()):
            if field not in fd:
                continue
            vals = split_values(fd[field])
            if not vals:
                failures.append(f"{key}: field {field} is empty")
            if len(vals) != len(set(vals)):
                failures.append(f"{key}: field {field} contains duplicate values")
            if field not in schema.multivalue_fields and len(vals) > 1:
                failures.append(f"{key}: field {field} must be single-valued, got {vals}")
            for val in vals:
                if val not in allowed_values:
                    failures.append(f"{key}: field {field} has uncontrolled value {val}")

        tags = split_values(fd.get("keywords", ""))
        tagset = set(tags)
        if len(tags) != len(tagset):
            failures.append(f"{key}: duplicate keywords")
        for tag in tags:
            if "/" not in tag:
                failures.append(f"{key}: keyword {tag} is not namespaced")
                continue
            prefix, value = tag.split("/", 1)
            if prefix in REMOVED_KEYWORD_PREFIXES:
                failures.append(f"{key}: removed legacy keyword prefix still present: {prefix}")
            if prefix not in schema.allowed_keyword_fields:
                failures.append(f"{key}: undocumented keyword prefix: {prefix}")
                continue
            allowed_values = schema.controlled.get(prefix)
            if allowed_values is not None and value not in allowed_values:
                failures.append(f"{key}: keyword {tag} has uncontrolled value {value}")

        expected_tags: set[str] = set()
        for field in schema.keyword_fields:
            if field not in fd:
                continue
            for val in split_values(fd[field]):
                expected = f"{field}/{val}"
                expected_tags.add(expected)
                if expected not in tagset:
                    failures.append(f"{key}: missing keyword mirror {expected}")
        for unexpected in sorted(tagset - expected_tags):
            failures.append(f"{key}: keyword has no matching field value: {unexpected}")

        if strip_outer(fd.get("version_status", "")) == "superseded" and not strip_outer(fd.get("superseded_by", "")):
            if not strip_outer(fd.get("evidence_note", "")):
                failures.append(f"{key}: superseded entry lacks superseded_by or evidence_note")

        for link_field in ("supersedes", "superseded_by", "crossref", "xref", "related", "xdata"):
            refs = split_values(fd.get(link_field, ""))
            if link_field in {"crossref", "xref"} and len(refs) > 1:
                failures.append(f"{key}: {link_field} must reference one key")
            if len(refs) != len(set(refs)):
                failures.append(f"{key}: {link_field} repeats a key")
            for ref in refs:
                if ref and ref not in keys:
                    failures.append(f"{key}: {link_field} references missing key {ref}")
                if ref == key:
                    failures.append(f"{key}: {link_field} references itself")

    return failures


def normalize_title_for_compare(value: str | None) -> str:
    text = strip_outer(value).lower()
    text = TEX_COMMAND_RE.sub(" ", text)
    text = text.replace("{", " ").replace("}", " ")
    return " ".join(WORD_RE.findall(text))


def clip(text: str, limit: int = 110) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def is_tracking_param(name: str) -> bool:
    low = name.lower()
    return low.startswith("utm_") or low in TRACKING_QUERY_KEYS


def advisory_warnings(
    entries: Sequence[tuple[str, str, dict[str, str]]],
    *,
    stale_urldate_days: int,
    fuzzy_title_threshold: float,
    max_fuzzy_title_warnings: int,
) -> list[str]:
    warnings: list[str] = []

    title_records: list[tuple[str, str, str]] = []
    exact_titles: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for _, key, fd in entries:
        raw_title = strip_outer(fd.get("title", "")).strip()
        norm_title = normalize_title_for_compare(raw_title)
        if norm_title:
            title_records.append((key, raw_title, norm_title))
            exact_titles[norm_title].append((key, raw_title))

    exact_duplicate_norms = {norm for norm, records in exact_titles.items() if len(records) > 1}
    for norm_title, records in sorted(exact_titles.items()):
        if len(records) > 1:
            refs = ", ".join(key for key, _ in records)
            example = clip(records[0][1])
            warnings.append(f"duplicate_title_exact: {refs}: {example!r}")

    fuzzy_count = 0
    fuzzy_truncated = False
    if max_fuzzy_title_warnings != 0:
        sorted_titles = sorted(title_records, key=lambda item: item[2])
        for i, (key_a, raw_a, norm_a) in enumerate(sorted_titles):
            if max_fuzzy_title_warnings > 0 and fuzzy_count >= max_fuzzy_title_warnings:
                fuzzy_truncated = True
                break
            if norm_a in exact_duplicate_norms or len(norm_a) < 24:
                continue
            tokens_a = set(norm_a.split())
            for key_b, raw_b, norm_b in sorted_titles[i + 1 :]:
                if max_fuzzy_title_warnings > 0 and fuzzy_count >= max_fuzzy_title_warnings:
                    fuzzy_truncated = True
                    break
                if norm_b in exact_duplicate_norms or len(norm_b) < 24:
                    continue
                tokens_b = set(norm_b.split())
                if not tokens_a or not tokens_b:
                    continue
                # Cheap prefilter: fuzzy title pairs should have meaningful token overlap.
                token_overlap = len(tokens_a & tokens_b) / min(len(tokens_a), len(tokens_b))
                if token_overlap < 0.55:
                    continue
                ratio = difflib.SequenceMatcher(None, norm_a, norm_b).ratio()
                if ratio >= fuzzy_title_threshold:
                    warnings.append(
                        f"duplicate_title_fuzzy: ({ratio:.2f}) {key_a} {clip(raw_a)!r} ~= {key_b} {clip(raw_b)!r}"
                    )
                    fuzzy_count += 1
        if fuzzy_truncated:
            warnings.append(
                f"duplicate_title_fuzzy_truncated: scan truncated at {max_fuzzy_title_warnings} warnings; "
                "raise --max-fuzzy-title-warnings to inspect more"
            )

    today = date_cls.today()
    for _, key, fd in entries:
        if has_value(fd, "scope_relevance", "core") and has_value(fd, "governance_function", "evaluation"):
            if not field_values(fd, "risk_domain"):
                warnings.append(f"missing_risk_domain: {key}: core evaluation entry lacks risk_domain")

        if has_value(fd, "scope_relevance", "core") and not field_values(fd, "lifecycle_stage"):
            warnings.append(f"missing_lifecycle_stage: {key}: core entry lacks lifecycle_stage")

        is_living_document = (
            strip_outer(fd.get("maintenance_status", "")) in LIVING_DOCUMENT_STATUSES
            or strip_outer(fd.get("version_status", "")) in LIVING_DOCUMENT_STATUSES
        )
        if is_living_document and not strip_outer(fd.get("archiveurl", "")):
            warnings.append(f"living_document_missing_archiveurl: {key}: living document lacks archiveurl")

        for url_field in URL_FIELDS_FOR_ADVISORY:
            raw_url = strip_outer(fd.get(url_field, "")).strip().strip("<>")
            if not raw_url:
                continue
            parsed = urlsplit(raw_url)
            if not parsed.query:
                continue
            params = [name for name, _ in parse_qsl(parsed.query, keep_blank_values=True)]
            if not params:
                warnings.append(f"url_query_parameters: {key}: {url_field} contains a raw query string; review for canonical citation URL")
                continue
            tracking = [name for name in params if is_tracking_param(name)]
            if tracking:
                warnings.append(
                    f"url_query_parameters: {key}: {url_field} contains tracking/query parameters {sorted(set(params))}; "
                    f"tracking-like parameters: {sorted(set(tracking))}"
                )
            else:
                warnings.append(f"url_query_parameters: {key}: {url_field} contains query parameters {sorted(set(params))}; review canonical URL")

        urldate = parse_full_date(fd.get("urldate", ""))
        if urldate is not None:
            if urldate > today:
                warnings.append(f"future_urldate: {key}: urldate {urldate.isoformat()} is in the future relative to {today.isoformat()}")
            elif stale_urldate_days > 0 and (today - urldate).days > stale_urldate_days:
                warnings.append(
                    f"stale_urldate: {key}: urldate {urldate.isoformat()} is older than {stale_urldate_days} days; review freshness"
                )

    return warnings


def print_report(entries_count: int, failures: Sequence[str], warnings: Sequence[str], schema: SchemaConfig) -> None:
    print(f"schema={schema.path}")
    if schema.schema_version:
        print(f"schema_version={schema.schema_version}")
    print(f"schema_required_fields={len(schema.required_fields)}")
    print(f"schema_multivalue_fields={len(schema.multivalue_fields)}")
    print(f"schema_controlled_fields={len(schema.controlled)}")
    print(f"schema_keyword_mirror_fields={len(schema.current_keyword_fields)}")
    print(f"schema_retained_legacy_fields={len(schema.retained_legacy_fields)}")
    print(f"entries={entries_count}")
    print(f"failures={len(failures)}")
    print(f"warnings={len(warnings)}")
    if failures:
        print("\nFAILURES")
        for failure in failures:
            print(f"- {failure}")
    if warnings:
        categories = Counter(warning.split(":", 1)[0] for warning in warnings)
        print("\nWARNING SUMMARY")
        for category, count in sorted(categories.items()):
            print(f"- {category}: {count}")
        print("\nWARNINGS")
        for warning in warnings:
            print(f"- {warning}")


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    schema_path = find_schema_path(args.bib, args.schema)
    schema = load_schema(schema_path)
    entries = parse_bib(args.bib.read_text(encoding="utf-8"))
    failures = validate_entries(entries, schema)
    warnings = [] if args.no_advisory else advisory_warnings(
        entries,
        stale_urldate_days=args.stale_urldate_days,
        fuzzy_title_threshold=args.fuzzy_title_threshold,
        max_fuzzy_title_warnings=args.max_fuzzy_title_warnings,
    )
    print_report(len(entries), failures, warnings, schema)
    if failures or (warnings and args.warnings_as_errors):
        return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
