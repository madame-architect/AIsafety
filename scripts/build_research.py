#!/usr/bin/env python3
"""Check broad-research references and render coverage and claim views.

This checks annotation consistency, not the truth or completeness of source claims.
The bibliography remains authoritative in records.yaml.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from datetime import date, datetime
import hashlib
from html import unescape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

import yaml
import source_provenance

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = Path("research/synthesis")
DEPTHS = ("Full text", "Selected sections", "Abstract only", "Metadata only", "Inaccessible")
STREAMS = ("technical_eval", "governance_artifact", "contextual")
STATUSES = {"provisional", "scoped_check", "unresolved", "historical"}
RELATIONS = {"supports", "bounds", "challenges", "contextualizes", "unresolved"}
BASES = {"supplied_ledger", "prior_audit", "this_run_primary", "repo_source_review"}
ROUND_SCHEMA = "synthesis-review-rounds-v1"
EDITION_MATCHES = {"same_record", "related_edition", "uncertain"}
COVERAGE_EFFECTS = {"complete_record_text", "scoped_review", "none"}
RELEVANCE = {"claim_evidence", "background", "duplicate_work_family", "out_of_scope_for_round", "unresolved"}
REPLICATION = {"not_performed", "partial_reproduction", "full_reproduction"}
CAPTURE_MIMES = {"application/pdf", "text/html", "application/xhtml+xml", "text/plain", "application/json"}
COLUMNS = (
    "citation_key", "repository_stream", "first_pass_read_depth", "inherited_read_depth",
    "second_pass_read_depth", "pre_targeted_read_depth", "pre_round_five_read_depth",
    "inherited_followup_dates", "material_accessed_url", "recorded_retrieval_routes",
    "material_inspected", "source_supports", "limitations", "review_lead", "current_review_note",
    "prior_ai_check_status", "prior_ai_check_reported_on", "prior_ai_check_url",
    "prior_ai_check_finding", "prior_ai_check_depth_locator", "prior_ai_check_limits",
    "replication_status", "thematic_role",
)


class ValidationError(ValueError):
    pass


def text_field(item: dict, field: str, label: str) -> str:
    value = item.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{label}: missing nonempty {field}")
    return value


def public_url(value: str, label: str) -> None:
    if not isinstance(value, str):
        raise ValidationError(f"{label}: expected HTTP(S) source URL")
    parsed = urlsplit(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValidationError(f"{label}: expected HTTP(S) source URL")
    if parsed.hostname in {"chatgpt.com", "chat.openai.com"}:
        raise ValidationError(f"{label}: private conversation/Page link is not a public source locator")


def validate_coverage(records: list[dict], rows: list[dict]) -> None:
    by_key = {record["id"]: record for record in records}
    if len(by_key) != len(records):
        raise ValidationError("records.yaml: duplicate citation key")
    keys = [row.get("citation_key") for row in rows]
    if len(keys) != len(set(keys)):
        raise ValidationError("coverage.csv: duplicate citation key")
    missing, extra = set(by_key) - set(keys), set(keys) - set(by_key)
    if missing or extra:
        raise ValidationError(f"coverage.csv: missing keys {sorted(missing)}; unknown keys {sorted(extra)}")
    for row in rows:
        key = row["citation_key"]
        if set(row) != set(COLUMNS):
            raise ValidationError(f"{key}: coverage columns differ from the declared schema")
        if row["repository_stream"] != by_key[key]["fields"]["synthesis_stream"]:
            raise ValidationError(f"{key}: coverage stream differs from records.yaml")
        for field in ("first_pass_read_depth", "inherited_read_depth", "second_pass_read_depth",
                      "pre_targeted_read_depth", "pre_round_five_read_depth"):
            if row[field] not in DEPTHS:
                raise ValidationError(f"{key}: invalid {field} {row[field]!r}")
        for field in ("material_inspected", "source_supports", "limitations"):
            text_field(row, field, key)
        if any("chatgpt.com/" in value or "chat.openai.com/" in value for value in row.values()):
            raise ValidationError(f"{key}: private conversation/Page link in public coverage")
        check_fields = ("prior_ai_check_reported_on", "prior_ai_check_url", "prior_ai_check_finding",
                        "prior_ai_check_depth_locator", "prior_ai_check_limits")
        if row["prior_ai_check_status"] == "logged_prior_ai_check":
            for field in check_fields:
                text_field(row, field, key)
            try:
                date.fromisoformat(row["prior_ai_check_reported_on"])
            except ValueError as exc:
                raise ValidationError(f"{key}: invalid prior check report date") from exc
            public_url(row["prior_ai_check_url"], key)
        elif row["prior_ai_check_status"] == "outside_105_record_register":
            if any(row[field] for field in check_fields):
                raise ValidationError(f"{key}: check detail without logged prior AI check")
        else:
            raise ValidationError(f"{key}: invalid prior_ai_check_status")
        if row["replication_status"] != "not_performed_in_this_integration":
            raise ValidationError(f"{key}: this integration does not claim replication")
        if row["thematic_role"] != "claim_links_in_claims_yaml_or_unresolved":
            raise ValidationError(f"{key}: thematic roles must resolve through claims.yaml")


def validate_claims(data: dict, record_ids: set[str]) -> None:
    if not isinstance(data, dict) or data.get("schema_version") != "broad-synthesis-v1":
        raise ValidationError("claims.yaml: unsupported schema_version")
    try:
        date.fromisoformat(data["as_of"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValidationError("claims.yaml: invalid as_of date; quote YAML dates") from exc
    claims = data.get("claims")
    if not isinstance(claims, list) or not claims:
        raise ValidationError("claims.yaml: claims must be a nonempty list")
    seen = set()
    for claim in claims:
        if not isinstance(claim, dict):
            raise ValidationError("claims.yaml: claim must be a mapping")
        identifier = text_field(claim, "id", "claim")
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", identifier) or identifier in seen:
            raise ValidationError(f"claims.yaml: invalid or duplicate claim ID {identifier!r}")
        seen.add(identifier)
        for field in ("section", "claim", "limitation", "counterevidence", "next_check"):
            text_field(claim, field, identifier)
        if claim.get("status") not in STATUSES:
            raise ValidationError(f"{identifier}: invalid claim status")
        evidence = claim.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            raise ValidationError(f"{identifier}: evidence must be a nonempty list")
        for item in evidence:
            if not isinstance(item, dict):
                raise ValidationError(f"{identifier}: evidence must be a mapping")
            if item.get("citation_key") not in record_ids:
                raise ValidationError(f"{identifier}: unknown citation key {item.get('citation_key')!r}")
            if item.get("relation") not in RELATIONS:
                raise ValidationError(f"{identifier}: invalid evidence relation")
            if item.get("review_basis") not in BASES:
                raise ValidationError(f"{identifier}: invalid review basis")
            for field in ("version_url", "locator", "finding", "checked_scope"):
                text_field(item, field, identifier)
            public_url(item["version_url"], identifier)
    families = data.get("families", [])
    if not isinstance(families, list):
        raise ValidationError("claims.yaml: families must be a list")
    seen_families = set()
    for family in families:
        if not isinstance(family, dict):
            raise ValidationError("claims.yaml: family must be a mapping")
        identifier = text_field(family, "id", "family")
        if identifier in seen_families:
            raise ValidationError(f"duplicate family ID {identifier!r}")
        seen_families.add(identifier)
        for field in ("relationship", "basis", "status"):
            text_field(family, field, identifier)
        keys = family.get("citation_keys")
        if not isinstance(keys, list) or not keys or any(not isinstance(key, str) for key in keys):
            raise ValidationError(f"{identifier}: citation_keys must be a nonempty string list")
        if len(keys) != len(set(keys)) or not set(keys) <= record_ids:
            raise ValidationError(f"{identifier}: duplicate or unknown family citation key")


def load_inputs(root: Path = ROOT) -> tuple[list[dict], list[dict], dict]:
    records = yaml.safe_load((root / "records.yaml").read_text(encoding="utf-8"))["records"]
    with (root / DIRECTORY / "coverage.csv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(COLUMNS):
            raise ValidationError("coverage.csv: unexpected header/order")
        rows = list(reader)
    claims = yaml.safe_load((root / DIRECTORY / "claims.yaml").read_text(encoding="utf-8"))
    validate_coverage(records, rows)
    validate_claims(claims, {record["id"] for record in records})
    return records, rows, claims


def cell(value: str) -> str:
    return " ".join(value.split()).replace("|", "\\|")


def claim_links(data: dict) -> dict[str, set[str]]:
    links = defaultdict(set)
    for claim in data["claims"]:
        for evidence in claim["evidence"]:
            links[evidence["citation_key"]].add(claim["id"])
    return links


def string_list(item: dict, field: str, label: str, *, empty: bool = False) -> list[str]:
    values = item.get(field)
    if not isinstance(values, list) or (not empty and not values) or any(
            not isinstance(value, str) or not value.strip() for value in values):
        raise ValidationError(f"{label}: {field} must be a {'possibly empty' if empty else 'nonempty'} string list")
    if len(values) != len(set(values)):
        raise ValidationError(f"{label}: duplicate {field}")
    return values


def iso_date(value: str, label: str) -> date:
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"{label}: expected quoted ISO date") from exc


def utc_time(value: str, label: str) -> datetime:
    if not isinstance(value, str) or not re.fullmatch(
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|\+00:00)", value):
        raise ValidationError(f"{label}: expected full UTC timestamp")
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValidationError(f"{label}: invalid UTC timestamp") from exc


def capture_path(root: Path, value: str, label: str) -> Path:
    if not isinstance(value, str):
        raise ValidationError(f"{label}: missing capture_path")
    relative = Path(value)
    if (relative.is_absolute() or "\\" in value or ".." in relative.parts
            or len(relative.parts) < 2 or relative.parts[0] != ".source-captures"):
        raise ValidationError(f"{label}: capture_path must stay inside .source-captures")
    target = root / relative
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValidationError(f"{label}: capture_path escapes checkout")
    return target


def check_reading_payload(payload: bytes, mime_type: str, label: str) -> None:
    """Check representation type and clear error pages, not scholarly completeness."""
    try:
        source_provenance.check_payload(payload, mime_type)
    except ValueError as exc:
        raise ValidationError(f"{label}: {exc}") from exc
    if mime_type == "application/pdf":
        return
    try:
        text = payload.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValidationError(f"{label}: captured text is not valid UTF-8") from exc
    if any(ord(character) < 32 and character not in "\t\n\r\f" for character in text):
        raise ValidationError(f"{label}: captured text contains binary control bytes")
    if mime_type == "application/json":
        try:
            json.loads(text)
        except json.JSONDecodeError as exc:
            raise ValidationError(f"{label}: captured JSON does not parse") from exc
    # Avoid mistaking a reliably identifiable server/challenge response for a
    # source. A general discussion of access failures within an article is valid.
    titles = re.findall(r"<title\b[^>]*>(.*?)</title\s*>", text[:32768], re.IGNORECASE | re.DOTALL)
    error_titles = {"access denied", "403 forbidden", "404 not found", "429 too many requests",
                    "500 internal server error", "502 bad gateway", "503 service unavailable",
                    "just a moment...", "attention required! | cloudflare"}
    if any(" ".join(unescape(re.sub(r"<[^>]+>", " ", title)).split()).casefold() in error_titles
           for title in titles):
        raise ValidationError(f"{label}: captured response is an error or challenge page")
    if mime_type == "text/plain" and (
            payload.startswith(b"%PDF-") or text.strip().casefold() in error_titles | {"404: not found", "403: forbidden"}):
        raise ValidationError(f"{label}: captured plain text is a document of another type or an error response")


def validate_rounds(data: dict, records: list[dict], claims: dict, root: Path = ROOT,
                    require_capture_files: bool = False) -> dict:
    """Validate declared reading events; this does not certify that reading occurred.

    Stable event IDs and chronological rounds make additions reviewable. Git history,
    rather than this current-state checker, preserves evidence of earlier versions.
    """
    if not isinstance(data, dict) or data.get("schema_version") != ROUND_SCHEMA:
        raise ValidationError("rounds.yaml: unsupported schema_version")
    rounds = data.get("rounds")
    if not isinstance(rounds, list) or not rounds:
        raise ValidationError("rounds.yaml: rounds must be a nonempty list")
    record_ids = {record["id"] for record in records}
    claim_sources = {claim["id"]: {e["citation_key"] for e in claim["evidence"]}
                     for claim in claims["claims"]}
    round_ids, event_ids, events, payloads = set(), set(), {}, {}
    previous_date = None
    for review_round in rounds:
        if not isinstance(review_round, dict):
            raise ValidationError("rounds.yaml: round must be a mapping")
        identifier = text_field(review_round, "id", "round")
        if identifier in round_ids or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", identifier):
            raise ValidationError(f"rounds.yaml: invalid or duplicate round ID {identifier!r}")
        round_ids.add(identifier)
        as_of = iso_date(review_round.get("as_of"), identifier)
        if previous_date is not None and as_of < previous_date:
            raise ValidationError(f"{identifier}: rounds are not chronological")
        previous_date = as_of
        if not isinstance(review_round.get("base_commit"), str) or not re.fullmatch(
                r"[0-9a-f]{40}", review_round["base_commit"]):
            raise ValidationError(f"{identifier}: invalid base_commit")
        for field in ("question", "selection_basis", "stopping_rule"):
            text_field(review_round, field, identifier)
        themes = review_round.get("themes")
        if not isinstance(themes, list) or not themes:
            raise ValidationError(f"{identifier}: themes must be a nonempty list")
        by_theme = {}
        for theme in themes:
            if not isinstance(theme, dict):
                raise ValidationError(f"{identifier}: theme must be a mapping")
            theme_id = text_field(theme, "id", identifier)
            if theme_id in by_theme:
                raise ValidationError(f"{identifier}: duplicate theme ID {theme_id}")
            for field in ("label", "selection_reason"):
                text_field(theme, field, theme_id)
            keys = string_list(theme, "citation_keys", theme_id)
            if not set(keys) <= record_ids:
                raise ValidationError(f"{theme_id}: unknown theme citation key")
            by_theme[theme_id] = set(keys)
        readings = review_round.get("readings")
        if not isinstance(readings, list):
            raise ValidationError(f"{identifier}: readings must be a list")
        for event in readings:
            if not isinstance(event, dict):
                raise ValidationError(f"{identifier}: reading event must be a mapping")
            event_id = text_field(event, "id", identifier)
            if event_id in event_ids or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", event_id):
                raise ValidationError(f"{identifier}: invalid or duplicate event ID {event_id!r}")
            event_ids.add(event_id)
            events[event_id] = event
            key = event.get("citation_key")
            if key not in record_ids:
                raise ValidationError(f"{event_id}: unknown citation key")
            if event.get("theme") not in by_theme or key not in by_theme[event["theme"]]:
                raise ValidationError(f"{event_id}: source does not belong to declared theme")
            for field in ("edition_match_note", "scope", "visual_check", "limitations", "numerical_check",
                          "counterevidence", "next_check", "relevance_note"):
                text_field(event, field, event_id)
            string_list(event, "locators", event_id)
            string_list(event, "findings", event_id, empty=event.get("reading_depth") == "Inaccessible")
            for field, allowed in (("reading_depth", DEPTHS), ("edition_match", EDITION_MATCHES),
                                   ("coverage_effect", COVERAGE_EFFECTS), ("relevance", RELEVANCE),
                                   ("replication_status", REPLICATION)):
                if event.get(field) not in allowed:
                    raise ValidationError(f"{event_id}: invalid {field}")
            linked_claims = string_list(event, "claim_ids", event_id, empty=True)
            if event["relevance"] == "claim_evidence" and not linked_claims:
                raise ValidationError(f"{event_id}: claim_evidence requires claim_ids")
            if any(claim_id not in claim_sources or key not in claim_sources[claim_id]
                   for claim_id in linked_claims):
                raise ValidationError(f"{event_id}: claim_ids do not resolve to source evidence")
            capture = event.get("capture")
            if not isinstance(capture, dict):
                raise ValidationError(f"{event_id}: missing capture mapping")
            required = {"preservation_status", "original_url", "final_url", "retrieved_at", "attempted_at",
                        "archive_url", "archive_checked_on", "archive_unavailable_reason", "sha256",
                        "byte_length", "mime_type", "published_on", "version_claim", "locator_basis", "capture_path"}
            if required != capture.keys():
                raise ValidationError(f"{event_id}: capture fields differ from declared schema")
            public_url(text_field(capture, "original_url", event_id), event_id)
            attempted = utc_time(capture["attempted_at"], event_id)
            if attempted.date() > as_of:
                raise ValidationError(f"{event_id}: attempt date is after round date")
            text_field(capture, "locator_basis", event_id)
            if capture["archive_url"] is None:
                if capture["archive_checked_on"] is not None:
                    raise ValidationError(f"{event_id}: archive date without archive URL")
                text_field(capture, "archive_unavailable_reason", event_id)
            else:
                public_url(capture["archive_url"], event_id)
                if capture["archive_url"] in {capture["original_url"], capture["final_url"]}:
                    raise ValidationError(f"{event_id}: live source URL is not an independent archive")
                if iso_date(capture["archive_checked_on"], event_id) > as_of:
                    raise ValidationError(f"{event_id}: archive check date is after round date")
            for field in ("published_on", "version_claim"):
                if capture[field] is not None:
                    text_field(capture, field, event_id)
            if capture["preservation_status"] == "captured":
                public_url(text_field(capture, "final_url", event_id), event_id)
                retrieved = utc_time(capture["retrieved_at"], event_id)
                if retrieved < attempted or retrieved.date() > as_of:
                    raise ValidationError(f"{event_id}: retrieval time does not fit attempt/round date")
                if (capture["archive_checked_on"] is not None
                        and iso_date(capture["archive_checked_on"], event_id) < retrieved.date()):
                    raise ValidationError(f"{event_id}: archive check predates retained retrieval")
                if (not isinstance(capture["sha256"], str)
                        or not re.fullmatch(r"[0-9a-f]{64}", capture["sha256"])):
                    raise ValidationError(f"{event_id}: invalid source SHA-256")
                if type(capture["byte_length"]) is not int or capture["byte_length"] <= 0:
                    raise ValidationError(f"{event_id}: invalid source byte_length")
                if capture["mime_type"] not in CAPTURE_MIMES:
                    raise ValidationError(f"{event_id}: unsupported source MIME type")
                target = capture_path(root, capture["capture_path"], event_id)
                fingerprint = (capture["sha256"], capture["byte_length"], capture["mime_type"])
                if capture["capture_path"] in payloads and payloads[capture["capture_path"]] != fingerprint:
                    raise ValidationError(f"{event_id}: conflicting metadata for one capture_path")
                payloads[capture["capture_path"]] = fingerprint
                if target.exists():
                    payload = target.read_bytes()
                    if len(payload) != capture["byte_length"] or hashlib.sha256(payload).hexdigest() != capture["sha256"]:
                        raise ValidationError(f"{event_id}: local capture hash/length mismatch")
                    check_reading_payload(payload, capture["mime_type"], event_id)
                elif require_capture_files:
                    raise ValidationError(f"{event_id}: required capture file is missing")
            elif capture["preservation_status"] == "unavailable":
                if any(capture[field] is not None for field in ("retrieved_at", "sha256", "byte_length", "mime_type", "capture_path")):
                    raise ValidationError(f"{event_id}: unavailable capture cannot claim retained bytes")
                if capture["final_url"] is not None:
                    public_url(capture["final_url"], event_id)
                if event["reading_depth"] != "Inaccessible" or event["coverage_effect"] != "none":
                    raise ValidationError(f"{event_id}: unavailable material cannot increase reading coverage")
            else:
                raise ValidationError(f"{event_id}: invalid preservation_status")
            if event["coverage_effect"] == "complete_record_text" and (
                    event["reading_depth"] != "Full text" or event["edition_match"] != "same_record"
                    or capture["preservation_status"] != "captured"):
                raise ValidationError(f"{event_id}: complete_record_text requires full same-record captured reading")
    for claim in claims["claims"]:
        for evidence in claim["evidence"]:
            references = evidence.get("review_event_ids", [])
            if not isinstance(references, list) or any(not isinstance(value, str) for value in references):
                raise ValidationError(f"{claim['id']}: invalid review_event_ids")
            if len(references) != len(set(references)) or any(
                    value not in events or events[value]["citation_key"] != evidence["citation_key"] for value in references):
                raise ValidationError(f"{claim['id']}: unknown or mismatched review_event_ids")
    present = sum((root / path).is_file() for path in payloads)
    return {"events": events, "captures_checked": present, "captures_missing": len(payloads) - present}


def load_rounds(root: Path, records: list[dict], claims: dict, require_capture_files: bool = False) -> tuple[dict | None, dict]:
    path = root / DIRECTORY / "rounds.yaml"
    if not path.exists():
        if (root / DIRECTORY / "rounds.md").exists():
            raise ValidationError("rounds.md exists without its rounds.yaml source")
        if any(evidence.get("review_event_ids") for claim in claims["claims"] for evidence in claim["evidence"]):
            raise ValidationError("claims reference reading events but rounds.yaml is missing")
        return None, {"events": {}, "captures_checked": 0, "captures_missing": 0}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data, validate_rounds(data, records, claims, root, require_capture_files)


def round_coverage(rows: list[dict], rounds: dict) -> dict:
    """Combine inherited labels with eligible new reading, retaining both layers."""
    effective = {row["citation_key"]: row["inherited_read_depth"] for row in rows}
    events = [event for review_round in rounds["rounds"] for event in review_round["readings"]]
    completed = {event["citation_key"] for event in events if event["coverage_effect"] == "complete_record_text"}
    resolved = {event["citation_key"] for event in events if event["relevance"] != "unresolved"}
    for event in events:
        key = event["citation_key"]
        if event["edition_match"] != "same_record" or event["coverage_effect"] == "none":
            continue
        depth = event["reading_depth"]
        if depth == "Full text" and event["coverage_effect"] != "complete_record_text":
            depth = "Selected sections"
        if DEPTHS.index(depth) < DEPTHS.index(effective[key]):
            effective[key] = depth
    inherited_full = {row["citation_key"] for row in rows if row["inherited_read_depth"] == "Full text"}
    additions = completed - inherited_full
    return {"events": events, "effective": effective, "completed": completed, "full_additions": additions,
            "inherited_full_rechecked": completed & inherited_full,
            "inherited_full_without_recheck": inherited_full - completed,
            "resolved": resolved, "fresh_keys": {event["citation_key"] for event in events}}


def generate_summary(rows: list[dict], data: dict, rounds: dict | None = None) -> str:
    counts = Counter(row["inherited_read_depth"] for row in rows)
    first = Counter(row["first_pass_read_depth"] for row in rows)
    checks = sum(row["prior_ai_check_status"] == "logged_prior_ai_check" for row in rows)
    links = claim_links(data)
    progress = round_coverage(rows, rounds) if rounds is not None else None
    readings_by_key = defaultdict(list)
    if progress:
        for event in progress["events"]:
            readings_by_key[event["citation_key"]].append(event)
    role_note = (f"The other **{len(rows)-len(links)} keys** retain source-level notes and an unresolved claim-level role. ")
    if progress:
        unmapped = set(progress["effective"]) - set(links)
        explicit_roles = unmapped & progress["resolved"]
        role_note = (f"The other **{len(unmapped)} keys** are not mapped as claim evidence. "
                     f"Of these, **{len(explicit_roles)}** have an explicit non-claim relevance decision in later rounds "
                     f"and **{len(unmapped-explicit_roles)}** retain an unresolved role. ")
    lines = [
        "# Corpus coverage and checking depth", "",
        "Read [current adjudications and publication holds](reconciliation.md) before using inherited notes. "
        "A populated `current_review_note` takes precedence over contradictory inherited support statements or review leads "
        "for current interpretation; it does not rewrite the earlier inspection history."
        + (" Later dated reading events qualify those earlier notes without changing their provenance." if progress else ""), "",
        "Generated from [coverage.csv](coverage.csv), [claims.yaml](claims.yaml), and canonical "
        "[records.yaml](../../records.yaml) by `python3 scripts/build_research.py --write`.", "",
        "The CSV preserves source-level contributions, inspection descriptions, limitations and proposed checks "
        "for every current bibliography key. These are inherited research notes, not new source verification. "
        "Citation identity, titles, metadata and source classification remain authoritative in `records.yaml`.", "",
        "## Reading labels" + (" inherited before later rounds" if progress else ""), "",
        "| Stream | Full text | Selected sections | Abstract only | Metadata only | Inaccessible | Total |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for stream in STREAMS:
        group = [row for row in rows if row["repository_stream"] == stream]
        by = Counter(row["inherited_read_depth"] for row in group)
        lines.append(f"| `{stream}` | " + " | ".join(str(by[depth]) for depth in DEPTHS) + f" | {len(group)} |")
    lines += ["| **Total** | " + " | ".join(str(counts[depth]) for depth in DEPTHS) + f" | **{len(rows)}** |", "",
        "| Recorded stage | Full text | Selected sections | Abstract only | Metadata only | Inaccessible |",
        "|---|---:|---:|---:|---:|---:|",
        "| First pass in supplied ledger | " + " | ".join(str(first[depth]) for depth in DEPTHS) + " |",
        "| Latest inherited label | " + " | ".join(str(counts[depth]) for depth in DEPTHS) + " |", "",
        "The supplied review's 104 full-text / 9 abstract-only table is superseded by the latest ledger labels above. "
        f"**{len(rows)-counts['Full text']} records remain short of the inherited full-text label.** "
        "Full text refers to the identified object's complete accessible text; linked PDFs, supplements, figures, "
        "data and experiments require separate inspection. Records include pages and policies as well as papers. "
        "These labels are recorded inspection claims, not certification of earlier reading.", "",
        "## Separate later checking", "",
        f"The supplied prior AI-assisted audit logs scoped central-claim checks for **{checks} records**. "
        "Its actual depth, source URL, finding, locator and remaining limits appear in the `prior_ai_check_*` columns. "
        "A selected-section check remains selected-section checking even when the inherited reading label is full text. "
        "`prior_ai_check_reported_on` is the audit reporting date, not a reconstructed source retrieval timestamp. "
        "The register is not a complete-document reread and its title does not establish independent human review "
        "or independence of the underlying sources. The integration checked the register's keys and content; "
        "it did not repeat all its source checks. Later deeper checks outside that register are described where used "
        "in the claim map, rather than silently upgrading its rows. "
        + ("The original integration reported no experimental replication; later events record their own replication status."
           if progress else "No experimental replication was performed in this integration."), "",
        "## Argument coverage", "",
        f"The current map has **{len(data['claims'])} claims** linked to **{len(links)} unique bibliography keys**. "
        + role_note +
        "An unmapped record is neither excluded nor evidence for a claim. A source may bound or challenge a proposition; "
        "inclusion is not corroboration. Shared study families are listed in the [claim map](claims.md).", "",
        f"**{sum(bool(row['review_lead'].strip()) for row in rows)} records** have proposed corrections or checks. "
        "These are review leads, not established errors. Current adjudications and publication-critical holds belong "
        "in the reconciliation note and claim map; inherited notes are retained with that boundary.", "",
        "## Provenance and scope", "",
        "Imported from the supplied revised coverage ledger, original byte SHA-256 "
        "`60b2ea6456ae11262c29eded7e88191b08a0da5012e60e693dcd82f9cc6d3876`. "
        "The review input had SHA-256 `e4a0715b1e7f44720e9a659db784e13ad045fb85ceb43ca15353601d3df0553c`. "
        "The derivative CSV omits private patch-disposition fields and bibliography metadata already held in `records.yaml`. "
        "It preserves first-pass and subsequent inherited depth stages and dates separately from the prior audit. "
        "The full-corpus reading and synthesis objective remains open. This curated collection has no reconstructed "
        "exhaustive search or independent human dual coding; completing reads would not retroactively create either.", "",
        "## Record index", "",
        "Use the CSV for full source notes. Links below identify explicit claim roles; all other roles remain unresolved.", "",
        "| Canonical citation key | Latest inherited reading | Prior scoped AI check | Claim roles | Current review note |",
        "|---|---|---|---|---|",
    ]
    if progress:
        counts_after = Counter(progress["effective"].values())
        fresh = Counter(event["reading_depth"] for event in progress["events"])
        round_lines = [
            "## Subsequent dated review rounds", "",
            "[Reading events and thematic decisions](rounds.md) preserve fresh inspection, exact versions, captures, "
            "contrary evidence and limitations separately from the inherited CSV. Full-text reading is not experimental "
            "replication, and reading a related or uncertain edition does not increase canonical-record coverage.", "",
            f"Later rounds log **{len(progress['events'])} reading events** for **{len(progress['fresh_keys'])} unique keys**. "
            f"**{len(progress['completed'])} keys** have eligible complete-record-text events, including "
            f"**{len(progress['full_additions'])}** that lacked an inherited full-text label. These remain recorded reading "
            "claims, not independent certification of every figure, supplement or source finding.", "",
            f"Of the **{counts['Full text']} records** with inherited full-text labels, "
            f"**{len(progress['inherited_full_rechecked'])}** have a later eligible complete-record-text recheck and "
            f"**{len(progress['inherited_full_without_recheck'])}** have not received such a recheck. "
            "Each key is counted once across rounds. Related-edition, ancillary-object and selected-section events "
            "do not qualify. A fresh complete reading establishes the recorded scope of the identified text; "
            "it does not prove what an earlier reader read or constitute independent human recertification.", "",
            "| Layer | Full text | Selected sections | Abstract only | Metadata only | Inaccessible |",
            "|---|---:|---:|---:|---:|---:|",
            "| Fresh reading events (representations may repeat a key) | " + " | ".join(str(fresh[depth]) for depth in DEPTHS) + " |",
            "| Combined best same-record inspection | " + " | ".join(str(counts_after[depth]) for depth in DEPTHS) + " |", "",
            f"**{len(rows)-counts_after['Full text']} records** remain without a full-text label after eligible new reading. "
            "Combined inspection retains earlier full-text labels without recertifying them; a later selected-section "
            "check neither erases nor independently confirms an earlier complete read. The reading event records replication "
            "and numerical checking separately. Missing local captures are reported by the validator; ordinary CI does not "
            "claim byte verification of absent private files.", "",
        ]
        position = lines.index("## Argument coverage")
        lines[position:position] = round_lines
        lines[-2] = "| Canonical citation key | Latest inherited reading | Prior scoped AI check | Claim roles | Current review note | Later reading events |"
        lines[-1] = "|---|---|---|---|---|---|"
    for row in rows:
        key = row["citation_key"]
        mapped = ", ".join(f"[{identifier}](claims.md#{identifier.lower()})" for identifier in sorted(links.get(key, []))) or "Unresolved"
        checked = "Logged; see CSV scope" if row["prior_ai_check_status"] == "logged_prior_ai_check" else "Outside 105-record register"
        later = readings_by_key.get(key, [])
        if mapped == "Unresolved" and any(event["relevance"] != "unresolved" for event in later):
            mapped = ", ".join(sorted({event["relevance"].replace("_", " ") for event in later if event["relevance"] != "unresolved"}))
        suffix = (" " + ", ".join(f"[{event['id']}](rounds.md#{event['id']})" for event in later) + " |") if progress and later else (" — |" if progress else "")
        lines.append(f"| `{key}` | {row['inherited_read_depth']} | {checked} | {mapped} | {cell(row['current_review_note']) or '—'} |" + suffix)
    return "\n".join(lines) + "\n"


def generate_rounds(data: dict, stats: dict) -> str:
    lines = ["# Dated research rounds and reading events", "",
        "Generated from [rounds.yaml](rounds.yaml). These are research annotations linked to canonical "
        "[records.yaml](../../records.yaml), not a competing bibliography. Selection is purposeful and claim-sensitive; "
        "this is not systematic search or independent human review. Reading depth and replication are separate, "
        "with event-specific status below. Original inherited "
        "reading labels remain in [coverage.csv](coverage.csv).", "",
        "Capture metadata identify retained source representations. The validator hashes locally present files and "
        "reports absent private payloads; generated prose does not claim a fresh network/archive retrieval. "
        "Use `python3 scripts/build_research.py --check --require-capture-files` to require local byte verification. "
        "Hashes do not establish source truth or completeness. Stable IDs and chronological rounds support review; "
        "Git history records changes to earlier annotations.", "",
    ]
    for review_round in data["rounds"]:
        lines += [f"## {review_round['id']}", "", f"**As of:** {review_round['as_of']}. **Base commit:** `{review_round['base_commit']}`.", "",
            "**Question:** " + review_round["question"], "", "**Selection basis:** " + review_round["selection_basis"], "",
            "**Stopping rule:** " + review_round["stopping_rule"], "",
            "| Theme | Why selected | Canonical keys |", "|---|---|---|",
        ]
        for theme in review_round["themes"]:
            lines.append(f"| {cell(theme['label'])} | {cell(theme['selection_reason'])} | " +
                         ", ".join(f"`{key}`" for key in theme["citation_keys"]) + " |")
        lines += ["", "### Event index", "", "| Event | Source | Reading | Edition / coverage effect | Relevance |",
                  "|---|---|---|---|---|"]
        for event in review_round["readings"]:
            lines.append(f"| [{event['id']}](#{event['id']}) | `{event['citation_key']}` | {event['reading_depth']} | "
                         f"{event['edition_match']} / {event['coverage_effect']} | {event['relevance']} |")
        for event in review_round["readings"]:
            capture = event["capture"]
            lines += ["", f"<a id=\"{event['id']}\"></a>", f"### {event['id']}", "",
                f"**Source:** `{event['citation_key']}`. **Theme:** {event['theme']}. "
                f"**Reading:** {event['reading_depth']}. **Coverage effect:** `{event['coverage_effect']}`.", "",
                f"**Edition match:** `{event['edition_match']}`. " + event["edition_match_note"], "",
                "**Inspected scope:** " + event["scope"], "", "**Locators:** " + "; ".join(event["locators"]), "",
                "**Visual check:** " + event["visual_check"], "", "**Findings:**", "",
            ]
            lines.extend("- " + finding for finding in event["findings"])
            if not event["findings"]:
                lines.append("No source findings; material was inaccessible.")
            lines += ["", "**Counterevidence / alternative:** " + event["counterevidence"], "",
                "**Limits:** " + event["limitations"], "",
                f"**Replication:** `{event['replication_status']}`. **Numerical check:** " + event["numerical_check"], "",
                f"**Relevance:** `{event['relevance']}`. **Claim links:** " +
                (", ".join(f"[{identifier}](claims.md#{identifier.lower()})" for identifier in event["claim_ids"]) or "None; no claim support forced."), "",
                "**Relevance rationale:** " + event["relevance_note"], "",
                "**Next check:** " + event["next_check"], "",
                "| Capture field | Value |", "|---|---|",
            ]
            for field, value in capture.items():
                if field in {"original_url", "final_url", "archive_url"} and value:
                    rendered = f"[Source]({value})"
                else:
                    rendered = "Not recorded / unavailable" if value is None else cell(str(value))
                lines.append(f"| `{field}` | {rendered} |")
    return "\n".join(lines) + "\n"


def generate_claims(data: dict) -> str:
    lines = ["# Claim and evidence map", "",
        "Generated from [claims.yaml](claims.yaml). Source identities resolve through [records.yaml](../../records.yaml); "
        "record-level inspection and limitations appear in [coverage.csv](coverage.csv). "
        "This is a provisional map of selected synthesis propositions, not a claim that the entire corpus supports them.", "",
        f"Assessment date: **{data['as_of']}**. `supplied_ledger` means inherited notes; `prior_audit` means a separate "
        "AI-assisted source check reported by the supplied audit; `this_run_primary` means scoped primary inspection "
        "reported by the project integration or a linked review round, not a recheck whenever this view is generated; "
        "`repo_source_review` means an existing dated repository review. None denotes independent human review or replication.", "",
        "Status `provisional` identifies a working synthesis; `scoped_check` identifies a proposition with the stated "
        "source-level checking basis (which may be a prior audit); `unresolved` retains a material discrepancy or hold; "
        "`historical` limits a finding to its dated record. A scoped check does not verify every source claim.", "",
        "## Claim index", "",
        "| Claim | Theme | Status | Proposition |", "|---|---|---|---|",
    ]
    for claim in data["claims"]:
        lines.append(f"| [{claim['id']}](#{claim['id'].lower()}) | {cell(claim['section'])} | {claim['status']} | {cell(claim['claim'])} |")
    for claim in data["claims"]:
        lines += ["", f"<a id=\"{claim['id'].lower()}\"></a>", f"## {claim['id']}", "", claim["claim"], "",
            f"**Status:** {claim['status']}. **Theme:** {claim['section']}.", "",
            "| Source and relation | Version / locator | Scoped finding | Review basis and depth |",
            "|---|---|---|---|",
        ]
        for evidence in claim["evidence"]:
            event_links = "; review events: " + ", ".join(
                f"[{identifier}](rounds.md#{identifier})" for identifier in evidence.get("review_event_ids", [])) if evidence.get("review_event_ids") else ""
            lines.append(f"| `{evidence['citation_key']}` — {evidence['relation']} | "
                         f"[Source]({evidence['version_url']}); {cell(evidence['locator'])} | "
                         f"{cell(evidence['finding'])} | `{evidence['review_basis']}`; {cell(evidence['checked_scope'])}{event_links} |")
        lines += ["", "**Limits:** " + claim["limitation"], "", "**Counterevidence / alternative:** " + claim["counterevidence"],
                  "", "**Next check:** " + claim["next_check"]]
    lines += ["", "## Source families and dependencies", "",
        "These family annotations identify shared work, data or incidents where known. They do not comprehensively "
        "certify independence across the collection. Citation keys are retained pending identity adjudication.", "",
        "| Family | Citation keys | Relationship | Basis | Status |", "|---|---|---|---|---|",
    ]
    for family in data.get("families", []):
        lines.append(f"| `{family['id']}` | " + ", ".join(f"`{key}`" for key in family["citation_keys"]) +
                     f" | {cell(family['relationship'])} | {cell(family['basis'])} | {cell(family['status'])} |")
    return "\n".join(lines) + "\n"


def build(root: Path = ROOT, check: bool = False, require_capture_files: bool = False) -> None:
    records, rows, claims = load_inputs(root)
    rounds, stats = load_rounds(root, records, claims, require_capture_files)
    outputs = {"coverage-summary.md": generate_summary(rows, claims, rounds), "claims.md": generate_claims(claims)}
    if rounds is not None:
        outputs["rounds.md"] = generate_rounds(rounds, stats)
    for name, content in outputs.items():
        path = root / DIRECTORY / name
        if check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                raise ValidationError(f"{path.relative_to(root)}: missing or stale; run scripts/build_research.py --write")
        else:
            path.write_text(content, encoding="utf-8")
    print(f"Broad research: {len(rows)} coverage records; {len(claims['claims'])} claims; generated views "
          + ("checked" if check else "written"))
    if rounds is not None:
        print(f"Review rounds: {len(rounds['rounds'])}; reading events: {len(stats['events'])}; "
              f"local source payloads checked: {stats['captures_checked']}; missing: {stats['captures_missing']}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    parser.add_argument("--require-capture-files", action="store_true",
                        help="require and hash every captured reading payload locally; no network access")
    args = parser.parse_args()
    try:
        build(check=args.check, require_capture_files=args.require_capture_files)
    except (ValidationError, OSError, yaml.YAMLError) as exc:
        parser.exit(1, f"Research validation failed: {exc}\n")


if __name__ == "__main__":
    main()
