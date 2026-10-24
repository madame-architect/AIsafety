#!/usr/bin/env python3
"""Validate the small policy-observation pilot and render its documentary history.

The default command validates only. --write explicitly generates the Markdown;
--check validates and compares it without writing. No network access is used.
Evidence v2 requires capture provenance. Only the two frozen pilot snapshots
retain an explicit legacy exception. Policy statements remain the only evidence
kind. Reports of implementation or measured
effectiveness require a later evidence-format extension, not a policy observation.
"""
from __future__ import annotations

import argparse
from datetime import date
import hashlib
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlsplit

sys.dont_write_bytecode = True

import yaml

import lint_bibliography as lint
import source_provenance as provenance

DIRECTORY = Path("research/cyber-deployment")
OUTPUT = DIRECTORY / "commitment-history.md"
SNAPSHOT_REQUIRED = {"id", "record_id", "source_url", "observed_on", "inspection_scope", "preservation_note"} | provenance.FIELDS
SNAPSHOT_OPTIONAL = {"capture_path", "capture_basis", "archive_unavailable_reason"}
OBSERVATION_REQUIRED = {
    "id", "commitment_id", "snapshot_id", "issuer", "evidence_kind", "modality",
    "scope", "trigger", "action", "qualifications", "locator", "change_type",
}
OBSERVATION_OPTIONAL = {
    "previous_observation_id", "change_note", "claimed_application_on",
    "application_date_note", "source_rationale",
}
MODALITIES = {"requirement", "recommendation", "discretionary", "intention"}
CHANGE_TYPES = {"observed", "revised", "clarified", "withdrawn", "retained"}
ID_RE = re.compile(r"[a-z0-9][a-z0-9_-]*\Z")


def mapping(value: object, required: set[str], optional: set[str], label: str) -> dict:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be a mapping")
    missing = required - value.keys()
    extra = value.keys() - required - optional
    if missing or extra:
        raise ValueError(f"{label}: missing keys {sorted(missing)}; unexpected keys {sorted(map(repr, extra))}")
    return value


def string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty string; quote dates and omit unknown values")
    return value


def check_date(value: str, label: str, *, full: bool = True) -> None:
    pattern = r"\d{4}-\d{2}-\d{2}" if full else r"\d{4}(?:-\d{2}){0,2}"
    try:
        if not re.fullmatch(pattern, value):
            raise ValueError
        parts = [int(part) for part in value.split("-")]
        date(*(parts + [1] * (3 - len(parts))))
    except ValueError:
        expected = "YYYY-MM-DD" if full else "YYYY, YYYY-MM, or YYYY-MM-DD"
        raise ValueError(f"{label} has an invalid date; expected {expected}") from None


def check_url(value: str, label: str) -> None:
    try:
        parsed = urlsplit(value)
        valid = parsed.scheme in {"http", "https"} and bool(parsed.hostname)
    except ValueError:
        valid = False
    if not valid or any(char.isspace() or ord(char) < 32 for char in value):
        raise ValueError(f"{label} must be an absolute HTTP(S) URL without whitespace")


def read_items(root: Path, filename: str, version: str, collection: str,
               required: set[str], optional: set[str]) -> dict[str, dict[str, str]]:
    path = root / DIRECTORY / filename
    data = mapping(lint.read_yaml(path), {"schema_version", collection}, set(), filename)
    if data["schema_version"] != version:
        raise ValueError(f"{filename}: schema_version must be {version}")
    if not isinstance(data[collection], list) or not data[collection]:
        raise ValueError(f"{filename}.{collection} must be a nonempty list")
    items: dict[str, dict[str, str]] = {}
    for number, raw in enumerate(data[collection], 1):
        label = f"{filename}.{collection}[{number}]"
        item = mapping(raw, required, optional, label)
        for field, value in item.items():
            if collection == "snapshots" and (field == "byte_length" or
                                              (field in provenance.NULLABLE and value is None)):
                continue
            string(value, f"{label}.{field}")
        for field in ("id", "commitment_id"):
            if field in item and not ID_RE.fullmatch(item[field]):
                raise ValueError(f"{label}.{field} must use lowercase letters, digits, underscores or hyphens")
        if item["id"] in items:
            raise ValueError(f"{filename}: duplicate id {item['id']}")
        items[item["id"]] = item
    return items


def load_history(root: Path) -> tuple[dict[str, dict[str, str]], list[dict[str, str]]]:
    # Bibliography validation has its own build. Here only resolve identities;
    # later metadata corrections must not rewrite historical observations.
    bibliography = lint.read_yaml(root / "records.yaml")
    records = bibliography.get("records") if isinstance(bibliography, dict) else None
    if not isinstance(records, list) or not records:
        raise ValueError("records.yaml must contain a nonempty records list")
    record_ids: set[str] = set()
    for record in records:
        key = string(record.get("id") if isinstance(record, dict) else None, "bibliography record id")
        if key in record_ids:
            raise ValueError(f"records.yaml: duplicate record id {key}")
        record_ids.add(key)

    snapshots = read_items(root, "evidence.yaml", "cyber-commitment-evidence-v2", "snapshots",
                           SNAPSHOT_REQUIRED, SNAPSHOT_OPTIONAL)
    for key, snapshot in snapshots.items():
        if snapshot["record_id"] not in record_ids:
            raise ValueError(f"{key}: record_id references missing bibliography key {snapshot['record_id']}")
        check_url(snapshot["source_url"], f"{key}.source_url")
        check_date(snapshot["observed_on"], f"{key}.observed_on")
        provenance.validate(snapshot, check_date, check_url)
        if snapshot.get("capture_path"):
            capture = (root / snapshot["capture_path"]).resolve()
            if not capture.is_relative_to(root.resolve()):
                raise ValueError(f"{key}: capture_path must stay inside the repository directory")
            # External source bytes may intentionally be absent from Git. If
            # present locally, always check that they match the declared digest.
            if capture.is_file():
                payload = capture.read_bytes()
                if len(payload) != snapshot["byte_length"]:
                    raise ValueError(f"{key}: capture byte length mismatch")
                if hashlib.sha256(payload).hexdigest() != snapshot["sha256"]:
                    raise ValueError(f"{key}: capture SHA-256 mismatch")
                provenance.check_payload(payload, snapshot["mime_type"])

    observations = read_items(root, "commitments.yaml", "cyber-commitments-v1", "observations",
                              OBSERVATION_REQUIRED, OBSERVATION_OPTIONAL)
    for key, observation in observations.items():
        if observation["snapshot_id"] not in snapshots:
            raise ValueError(f"{key}: snapshot_id references missing snapshot {observation['snapshot_id']}")
        if observation["evidence_kind"] != "policy_statement":
            raise ValueError(f"{key}: evidence_kind must be policy_statement; implementation/effectiveness evidence needs a later format")
        if observation["modality"] not in MODALITIES:
            raise ValueError(f"{key}: unknown modality {observation['modality']}")
        change = observation["change_type"]
        if change not in CHANGE_TYPES:
            raise ValueError(f"{key}: unknown change_type {change}")
        linked_fields = {"previous_observation_id", "change_note"}
        if change == "observed":
            if linked_fields & observation.keys():
                raise ValueError(f"{key}: observed must omit previous_observation_id and change_note")
        elif not linked_fields <= observation.keys():
            raise ValueError(f"{key}: {change} requires previous_observation_id and change_note")
        if "claimed_application_on" in observation:
            if "application_date_note" not in observation:
                raise ValueError(f"{key}: claimed_application_on requires application_date_note")
            check_date(observation["claimed_application_on"], f"{key}.claimed_application_on")
        previous = observation.get("previous_observation_id")
        if previous:
            if previous not in observations:
                raise ValueError(f"{key}: previous_observation_id references missing observation {previous}")
            if previous == key:
                raise ValueError(f"{key}: previous_observation_id references itself")
            before = observations[previous]
            if any(before[field] != observation[field] for field in ("commitment_id", "issuer")):
                raise ValueError(f"{key}: predecessor must have the same commitment_id and issuer")

    # Explicit comparison links determine order, not inferred effective dates.
    ordered: list[dict[str, str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(key: str) -> None:
        if key in visiting:
            raise ValueError(f"cycle in previous_observation_id links at {key}")
        if key in visited:
            return
        visiting.add(key)
        previous = observations[key].get("previous_observation_id")
        if previous:
            visit(previous)
        visiting.remove(key)
        visited.add(key)
        ordered.append(observations[key])

    for key in sorted(observations, key=lambda item: (observations[item]["commitment_id"], item)):
        visit(key)
    return snapshots, ordered


def display(value: object) -> str:
    """Keep data as visible prose rather than Markdown structure or HTML."""
    value = "Not recorded" if value is None else str(value)
    return re.sub(r"([\\`*_\[\]|<>])", r"\\\1", value).replace("\n", " ")


def link(label: str, url: str) -> str:
    destination = quote(url, safe=":/?#[]@!$&'*+,;=%")
    return f"[{display(label)}]({destination})"


def generate_history(root: Path) -> tuple[str, dict[str, int]]:
    snapshots, observations = load_history(root)
    lines = [
        "# Cyber safety commitments: documentary history", "",
        "Generated from [evidence.yaml](evidence.yaml) and [commitments.yaml](commitments.yaml). "
        "Regenerate with `python3 scripts/build_commitments.py --write`.", "",
        "These observations record policy wording. Implementation and effectiveness are **not assessed** "
        "by this pilot. Recommendation changes do not establish adoption, protection achieved, or compliance.", "",
        "Publication dates describe documents; observation dates describe inspection; claimed application "
        "dates are included only when explicitly recorded. Missing values remain **Not recorded**. "
        "Predecessor links determine documentary order. A clarification preserves the earlier statement; "
        "absence of wording is not treated as withdrawal.", "",
    ]
    current_commitment = None
    for observation in observations:
        key = observation["id"]
        snapshot = snapshots[observation["snapshot_id"]]
        if observation["commitment_id"] != current_commitment:
            current_commitment = observation["commitment_id"]
            lines.extend([
                f"## {display(observation['issuer'])}: {display(observation['scope'])}", "",
                f"**Commitment ID:** `{current_commitment}`", "",
            ])
        lines.extend([
            f"### Observation {key}", "",
            "| Field | Recorded observation |", "| --- | --- |",
            f"| Issuer | {display(observation['issuer'])} |",
            f"| Source | {link(snapshot['record_id'], snapshot['source_url'])} |",
            f"| Document version claim | {display(snapshot['version_claim'])} |",
            f"| Document publication date | {display(snapshot.get('published_on', 'Not recorded'))} |",
            f"| Observed on | {snapshot['observed_on']} |",
            f"| Claimed application date | {observation.get('claimed_application_on', 'Not recorded')} |",
            f"| Evidence kind | {display(observation['evidence_kind'])} |",
            f"| Policy modality | {display(observation['modality'])} |",
            f"| Documentary relationship | {display(observation['change_type'])} |", "",
        ])
        for label, field in (("Scope", "scope"), ("Trigger", "trigger"), ("Action", "action"),
                             ("Qualifications", "qualifications"), ("Source rationale", "source_rationale"),
                             ("Source locator", "locator"), ("Application date note", "application_date_note")):
            if field in observation:
                lines.extend([f"**{label}:** {display(observation[field])}", ""])
        if "previous_observation_id" in observation:
            previous = observation["previous_observation_id"]
            lines.extend([
                f"**Compared with:** [{display(previous)}](#observation-{previous}).", "",
                f"**Analyst change note:** {display(observation['change_note'])}", "",
            ])
        lines.extend([f"**Inspection and preservation:** [Snapshot {display(snapshot['id'])}](#snapshot-{snapshot['id']}).", ""])

    lines.extend(["## Source observations and preservation", ""])
    for key, snapshot in sorted(snapshots.items()):
        lines.extend([
            f"### Snapshot {key}", "",
            f"**Bibliography record:** `{snapshot['record_id']}` in [records.yaml](../../records.yaml).", "",
            f"**Inspected source:** {link(snapshot['source_url'], snapshot['source_url'])}", "",
            f"**Observed on:** {snapshot['observed_on']}", "",
            f"**Inspection scope:** {display(snapshot['inspection_scope'])}", "",
            f"**Preservation status:** {display(snapshot['preservation_status'])}", "",
            f"**Retrieved at (UTC):** {display(snapshot['retrieved_at'])}", "",
            f"**SHA-256:** {display(snapshot['sha256'])}", "",
            f"**Byte length:** {display(snapshot['byte_length'])}", "",
            f"**MIME type:** {display(snapshot['mime_type'])}", "",
            f"**Locator basis:** {display(snapshot['locator_basis'])}", "",
            f"**Preservation:** {display(snapshot['preservation_note'])}", "",
        ])
        if snapshot['archive_url'] is not None:
            lines.extend([f"**Checked archive:** {link(snapshot['archive_url'], snapshot['archive_url'])} "
                          f"(checked {snapshot['archive_checked_on']}).", ""])
        else:
            lines.extend(["**Checked archive:** Not recorded.", ""])
        if snapshot.get('capture_basis'):
            lines.extend([f"**Capture basis:** {display(snapshot['capture_basis'])}", ""])
        if snapshot.get('archive_unavailable_reason'):
            lines.extend([f"**Archive limitation:** {display(snapshot['archive_unavailable_reason'])}", ""])
    lines.append("Source URLs and recorded digests do not themselves guarantee future retrieval. "
                 "This view does not fetch sources or verify their contents.")
    counts = {"snapshots": len(snapshots), "observations": len(observations),
              "commitments": len({item['commitment_id'] for item in observations})}
    return "\n".join(lines) + "\n", counts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Validate and write the generated Markdown view")
    mode.add_argument("--check", action="store_true", help="Validate and check generated bytes without writing")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args(argv)
    try:
        content, counts = generate_history(args.root)
        target = args.root / OUTPUT
        encoded = content.encode("utf-8")
        if args.check and (not target.is_file() or target.read_bytes() != encoded):
            print(f"Generated history is missing or stale: {OUTPUT}\nRun: python3 scripts/build_commitments.py --write", file=sys.stderr)
            return 1
        if args.write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(encoded)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"Validated {counts['snapshots']} snapshots and {counts['observations']} policy observations "
          f"for {counts['commitments']} commitment(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

