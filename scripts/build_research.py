#!/usr/bin/env python3
"""Check broad-research references and render coverage and claim views.

This checks annotation consistency, not the truth or completeness of source claims.
The bibliography remains authoritative in records.yaml.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from datetime import date
from pathlib import Path
import re
from urllib.parse import urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = Path("research/synthesis")
DEPTHS = ("Full text", "Selected sections", "Abstract only", "Metadata only", "Inaccessible")
STREAMS = ("technical_eval", "governance_artifact", "contextual")
STATUSES = {"provisional", "scoped_check", "unresolved", "historical"}
RELATIONS = {"supports", "bounds", "challenges", "contextualizes", "unresolved"}
BASES = {"supplied_ledger", "prior_audit", "this_run_primary", "repo_source_review"}
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


def generate_summary(rows: list[dict], data: dict) -> str:
    counts = Counter(row["inherited_read_depth"] for row in rows)
    first = Counter(row["first_pass_read_depth"] for row in rows)
    checks = sum(row["prior_ai_check_status"] == "logged_prior_ai_check" for row in rows)
    links = claim_links(data)
    lines = [
        "# Corpus coverage and checking depth", "",
        "Read [current adjudications and publication holds](reconciliation.md) before using inherited notes. "
        "A populated `current_review_note` takes precedence over contradictory inherited support statements or review leads "
        "for current interpretation; it does not rewrite the earlier inspection history.", "",
        "Generated from [coverage.csv](coverage.csv), [claims.yaml](claims.yaml), and canonical "
        "[records.yaml](../../records.yaml) by `python3 scripts/build_research.py --write`.", "",
        "The CSV preserves source-level contributions, inspection descriptions, limitations and proposed checks "
        "for every current bibliography key. These are inherited research notes, not new source verification. "
        "Citation identity, titles, metadata and source classification remain authoritative in `records.yaml`.", "",
        "## Reading labels", "",
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
        "in the claim map, rather than silently upgrading its rows. No experimental replication was performed in this integration.", "",
        "## Argument coverage", "",
        f"The current map has **{len(data['claims'])} claims** linked to **{len(links)} unique bibliography keys**. "
        f"The other **{len(rows)-len(links)} keys** retain source-level notes and an unresolved claim-level role. "
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
    for row in rows:
        key = row["citation_key"]
        mapped = ", ".join(f"[{identifier}](claims.md#{identifier.lower()})" for identifier in sorted(links.get(key, []))) or "Unresolved"
        checked = "Logged; see CSV scope" if row["prior_ai_check_status"] == "logged_prior_ai_check" else "Outside 105-record register"
        lines.append(f"| `{key}` | {row['inherited_read_depth']} | {checked} | {mapped} | {cell(row['current_review_note']) or '—'} |")
    return "\n".join(lines) + "\n"


def generate_claims(data: dict) -> str:
    lines = ["# Claim and evidence map", "",
        "Generated from [claims.yaml](claims.yaml). Source identities resolve through [records.yaml](../../records.yaml); "
        "record-level inspection and limitations appear in [coverage.csv](coverage.csv). "
        "This is a provisional map of selected synthesis propositions, not a claim that the entire corpus supports them.", "",
        f"Assessment date: **{data['as_of']}**. `supplied_ledger` means inherited notes; `prior_audit` means a separate "
        "AI-assisted source check reported by the supplied audit; `this_run_primary` means scoped primary inspection in this run; "
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
            lines.append(f"| `{evidence['citation_key']}` — {evidence['relation']} | "
                         f"[Source]({evidence['version_url']}); {cell(evidence['locator'])} | "
                         f"{cell(evidence['finding'])} | `{evidence['review_basis']}`; {cell(evidence['checked_scope'])} |")
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


def build(root: Path = ROOT, check: bool = False) -> None:
    _, rows, claims = load_inputs(root)
    outputs = {"coverage-summary.md": generate_summary(rows, claims), "claims.md": generate_claims(claims)}
    for name, content in outputs.items():
        path = root / DIRECTORY / name
        if check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                raise ValidationError(f"{path.relative_to(root)}: missing or stale; run scripts/build_research.py --write")
        else:
            path.write_text(content, encoding="utf-8")
    print(f"Broad research: {len(rows)} coverage records; {len(claims['claims'])} claims; generated views "
          + ("checked" if check else "written"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        build(check=args.check)
    except (ValidationError, OSError, yaml.YAMLError) as exc:
        parser.exit(1, f"Research validation failed: {exc}\n")


if __name__ == "__main__":
    main()
