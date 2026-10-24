#!/usr/bin/env python3
"""Validate the benchmark-to-risk longitudinal dataset and generate evidence-map.md."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent
ASSUMPTIONS_PATH = ROOT / "assumptions.yaml"
SOURCES_PATH = ROOT / "source-admission.yaml"
EVIDENCE_PATH = ROOT / "risk-evidence.yaml"
OUTPUT_PATH = ROOT / "evidence-map.md"

ALLOWED_OVERALL = {"supported", "mixed", "challenged", "unresolved"}
ALLOWED_ROLES = {"supports", "challenges", "bounds", "contextualizes", "unresolved"}
ALLOWED_ADMISSION = {"accepted", "pending_full_text_review"}
ALLOWED_BIB = {"pending", "accepted", "deferred"}


class ValidationError(ValueError):
    pass


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValidationError(f"{path.name}: root must be a mapping")
    return data


def unique(items: list[dict[str, Any]], key: str, label: str) -> dict[str, dict[str, Any]]:
    if not isinstance(items, list) or not items:
        raise ValidationError(f"{label}: must be a non-empty list")
    result: dict[str, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict):
            raise ValidationError(f"{label}: every item must be a mapping")
        value = item.get(key)
        if not isinstance(value, str) or not value:
            raise ValidationError(f"{label}: missing non-empty {key}")
        if value in result:
            raise ValidationError(f"{label}: duplicate {key} {value!r}")
        result[value] = item
    return result


def valid_date(value: Any, label: str) -> str:
    if not isinstance(value, str):
        raise ValidationError(f"{label}: expected YYYY-MM-DD string")
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError(f"{label}: expected YYYY-MM-DD string") from exc
    return value


def latest_assessment(assumption: dict[str, Any]) -> dict[str, Any]:
    assessments = assumption.get("assessments")
    if not isinstance(assessments, list) or not assessments:
        raise ValidationError(f"{assumption['id']}: assessments must be non-empty")
    ordered = sorted(assessments, key=lambda item: valid_date(item.get("as_of"), f"{assumption['id']}.as_of"))
    return ordered[-1]


def validate() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    assumptions = load_yaml(ASSUMPTIONS_PATH)
    sources = load_yaml(SOURCES_PATH)
    evidence = load_yaml(EVIDENCE_PATH)

    if assumptions.get("schema_version") != "cyber-benchmark-risk-assumptions-v2":
        raise ValidationError("assumptions.yaml: unsupported schema_version")
    if sources.get("schema_version") != "cyber-operational-source-admission-v2":
        raise ValidationError("source-admission.yaml: unsupported schema_version")
    if evidence.get("schema_version") != "cyber-operational-risk-evidence-v2":
        raise ValidationError("risk-evidence.yaml: unsupported schema_version")
    if {assumptions.get("dataset_id"), sources.get("dataset_id"), evidence.get("dataset_id")} != {"benchmark_to_risk_evidence"}:
        raise ValidationError("dataset_id must be benchmark_to_risk_evidence across all three YAML files")

    round_by_id = unique(sources.get("rounds", []), "id", "rounds")
    for round_item in round_by_id.values():
        valid_date(round_item.get("research_completed_on"), f"{round_item['id']}.research_completed_on")
        valid_date(round_item.get("admitted_on"), f"{round_item['id']}.admitted_on")

    assumption_by_id = unique(assumptions.get("assumptions", []), "id", "assumptions")
    assessment_ids: set[str] = set()
    for assumption in assumption_by_id.values():
        if assumption.get("research_priority") not in {"normal", "high", "highest"}:
            raise ValidationError(f"{assumption['id']}: invalid research_priority")
        assessments = assumption.get("assessments")
        if not isinstance(assessments, list) or not assessments:
            raise ValidationError(f"{assumption['id']}: assessments must be non-empty")
        previous_date: str | None = None
        for assessment in assessments:
            if not isinstance(assessment, dict):
                raise ValidationError(f"{assumption['id']}: assessment must be a mapping")
            assessment_id = assessment.get("id")
            if not isinstance(assessment_id, str) or not assessment_id:
                raise ValidationError(f"{assumption['id']}: assessment missing id")
            if assessment_id in assessment_ids:
                raise ValidationError(f"duplicate assessment id {assessment_id!r}")
            assessment_ids.add(assessment_id)
            current_date = valid_date(assessment.get("as_of"), f"{assessment_id}.as_of")
            if previous_date is not None and current_date <= previous_date:
                raise ValidationError(f"{assumption['id']}: assessments must be strictly chronological")
            previous_date = current_date
            if assessment.get("round_id") not in round_by_id:
                raise ValidationError(f"{assessment_id}: unknown round_id {assessment.get('round_id')!r}")
            if assessment.get("code") not in ALLOWED_OVERALL:
                raise ValidationError(f"{assessment_id}: invalid code {assessment.get('code')!r}")
            if not assessment.get("summary"):
                raise ValidationError(f"{assessment_id}: missing summary")

    source_by_id = unique(sources.get("sources", []), "source_id", "sources")
    for source in source_by_id.values():
        if source.get("round_id") not in round_by_id:
            raise ValidationError(f"{source['source_id']}: unknown round_id")
        if source.get("research_admission") not in ALLOWED_ADMISSION:
            raise ValidationError(f"{source['source_id']}: invalid research_admission")
        if source.get("bibliography_admission") not in ALLOWED_BIB:
            raise ValidationError(f"{source['source_id']}: invalid bibliography_admission")
        valid_date(source.get("admitted_on"), f"{source['source_id']}.admitted_on")
        if source.get("research_admission") == "accepted":
            for field in ("title", "primary_url", "inspection_basis", "limitations", "preservation_status"):
                if not source.get(field):
                    raise ValidationError(f"{source['source_id']}: accepted source missing {field}")

    observation_by_id = unique(evidence.get("observations", []), "id", "observations")
    covered_sources: set[str] = set()
    linked_assumptions: set[str] = set()
    for observation in observation_by_id.values():
        source_id = observation.get("source_id")
        if source_id not in source_by_id:
            raise ValidationError(f"{observation['id']}: unknown source_id {source_id!r}")
        if observation.get("round_id") not in round_by_id:
            raise ValidationError(f"{observation['id']}: unknown round_id")
        if observation.get("round_id") != source_by_id[source_id].get("round_id"):
            raise ValidationError(f"{observation['id']}: round_id must match its source")
        valid_date(observation.get("admitted_on"), f"{observation['id']}.admitted_on")
        covered_sources.add(source_id)
        links = observation.get("assumption_links")
        if not isinstance(links, list) or not links:
            raise ValidationError(f"{observation['id']}: assumption_links must be non-empty")
        seen: set[str] = set()
        for link in links:
            if not isinstance(link, dict):
                raise ValidationError(f"{observation['id']}: assumption link must be a mapping")
            assumption_id = link.get("assumption_id")
            if assumption_id not in assumption_by_id:
                raise ValidationError(f"{observation['id']}: unknown assumption_id {assumption_id!r}")
            if assumption_id in seen:
                raise ValidationError(f"{observation['id']}: duplicate assumption link {assumption_id!r}")
            seen.add(assumption_id)
            linked_assumptions.add(assumption_id)
            if link.get("role") not in ALLOWED_ROLES:
                raise ValidationError(f"{observation['id']}: invalid role {link.get('role')!r}")

    accepted = {sid for sid, src in source_by_id.items() if src.get("research_admission") == "accepted"}
    missing = accepted - covered_sources
    if missing:
        raise ValidationError(f"accepted sources without evidence observations: {sorted(missing)}")
    unlinked = set(assumption_by_id) - linked_assumptions
    if unlinked:
        raise ValidationError(f"assumptions without evidence links: {sorted(unlinked)}")

    return assumptions, sources, evidence


def short(text: str, limit: int = 155) -> str:
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def source_date(source: dict[str, Any]) -> str:
    return str(source.get("published_on") or source.get("version_date") or source.get("first_submitted_on") or "Not recorded")


def generate(assumptions: dict[str, Any], sources: dict[str, Any], evidence: dict[str, Any]) -> str:
    source_by_id = {s["source_id"]: s for s in sources["sources"]}
    observations = evidence["observations"]
    rounds = sources["rounds"]

    lines = [
        "# Benchmark-to-risk evidence map",
        "",
        "Generated from [assumptions.yaml](assumptions.yaml), "
        "[source-admission.yaml](source-admission.yaml), and "
        "[risk-evidence.yaml](risk-evidence.yaml).",
        "",
        f"**Research rounds:** {len(rounds)}  ",
        f"**Accepted research-layer sources:** {sum(s.get('research_admission') == 'accepted' for s in sources['sources'])}  ",
        f"**Canonical bibliography:** {sum(s.get('bibliography_admission') == 'accepted' for s in sources['sources'] if s.get('research_admission') == 'accepted')}/{sum(s.get('research_admission') == 'accepted' for s in sources['sources'])} accepted research sources integrated.",
        f"**Source captures:** {sum(s.get('preservation_status') == 'captured' for s in sources['sources'] if s.get('research_admission') == 'accepted')}/{sum(s.get('research_admission') == 'accepted' for s in sources['sources'])} retained; see [capture registry](source-captures.yaml).",
        "",
        "## Assumption registry and assessment history",
        "",
        "| Assumption | Latest assessment | As of | Summary | Prior assessments |",
        "|---|---|---|---|---:|",
    ]
    for item in assumptions["assumptions"]:
        latest = latest_assessment(item)
        lines.append(
            f"| `{item['id']}` — {item['label']} | **{latest['code']}** | {latest['as_of']} | "
            f"{short(latest['summary'], 220)} | {len(item['assessments']) - 1} |"
        )

    lines += [
        "",
        "## Source evidence",
        "",
        "| Source | Source date | Evidence type | Outcome / contribution | Harm status | Assumption roles |",
        "|---|---|---|---|---|---|",
    ]
    for obs in observations:
        src = source_by_id[obs["source_id"]]
        roles = "; ".join(f"`{x['assumption_id']}`: {x['role']}" for x in obs["assumption_links"])
        lines.append(
            f"| [{src['title']}]({src['primary_url']}) | {source_date(src)} | `{obs['evidence_type']}` | "
            f"{short(obs['observed_outcome'], 200)} | {short(obs['realized_harm'], 135)} | {roles} |"
        )

    lines += [
        "",
        "## Interpretation boundary",
        "",
        "Assessment history is longitudinal: future research rounds append dated assessments instead of "
        "overwriting earlier judgments. Evidence roles describe how a source bears on an assumption; they "
        "are not source-quality scores, causal effect estimates, or proof that a provider implemented an "
        "effective safeguard.",
        "",
        "No admitted source validates the entire chain from benchmark performance to realized harm. "
        "See [bounded-review.md](bounded-review.md) for the first-round synthesis and limitations.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="write the generated evidence map")
    mode.add_argument("--check", action="store_true", help="check that the evidence map is current")
    args = parser.parse_args()

    assumptions, sources, evidence = validate()
    generated = generate(assumptions, sources, evidence)

    if args.write:
        OUTPUT_PATH.write_text(generated, encoding="utf-8")
        print(f"wrote {OUTPUT_PATH}")
        return 0

    if not OUTPUT_PATH.exists():
        raise SystemExit(f"missing generated file: {OUTPUT_PATH}")
    current = OUTPUT_PATH.read_text(encoding="utf-8")
    if current != generated:
        raise SystemExit("evidence-map.md is stale; run build.py --write")
    print(
        f"validated {len(assumptions['assumptions'])} assumptions, "
        f"{len(sources['sources'])} admitted sources, "
        f"{len(evidence['observations'])} observations, and "
        f"{len(sources['rounds'])} research round(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
