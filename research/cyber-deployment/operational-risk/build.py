#!/usr/bin/env python3
"""Validate the operational-risk research layer and generate evidence-map.md."""

from __future__ import annotations

import argparse
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
ALLOWED_BIB = {"deferred", "pending", "accepted"}


class ValidationError(ValueError):
    pass


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValidationError(f"{path.name}: root must be a mapping")
    return data


def unique(items: list[dict[str, Any]], key: str, label: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for item in items:
        value = item.get(key)
        if not isinstance(value, str) or not value:
            raise ValidationError(f"{label}: missing non-empty {key}")
        if value in result:
            raise ValidationError(f"{label}: duplicate {key} {value!r}")
        result[value] = item
    return result


def validate() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    assumptions = load_yaml(ASSUMPTIONS_PATH)
    sources = load_yaml(SOURCES_PATH)
    evidence = load_yaml(EVIDENCE_PATH)

    if assumptions.get("round_id") != sources.get("round_id") or assumptions.get("round_id") != evidence.get("round_id"):
        raise ValidationError("round_id must match across all three YAML files")

    assumption_by_id = unique(assumptions.get("assumptions", []), "id", "assumptions")
    source_by_id = unique(sources.get("sources", []), "source_id", "sources")
    observation_by_id = unique(evidence.get("observations", []), "id", "observations")

    for assumption in assumption_by_id.values():
        code = assumption.get("overall_code")
        if code not in ALLOWED_OVERALL:
            raise ValidationError(f"{assumption['id']}: invalid overall_code {code!r}")

    for source in source_by_id.values():
        if source.get("research_admission") not in ALLOWED_ADMISSION:
            raise ValidationError(f"{source['source_id']}: invalid research_admission")
        if source.get("bibliography_admission") not in ALLOWED_BIB:
            raise ValidationError(f"{source['source_id']}: invalid bibliography_admission")
        if source.get("research_admission") == "accepted":
            for field in ("title", "primary_url", "inspection_basis", "limitations"):
                if not source.get(field):
                    raise ValidationError(f"{source['source_id']}: accepted source missing {field}")

    covered_sources: set[str] = set()
    for observation in observation_by_id.values():
        source_id = observation.get("source_id")
        if source_id not in source_by_id:
            raise ValidationError(f"{observation['id']}: unknown source_id {source_id!r}")
        covered_sources.add(source_id)
        links = observation.get("assumption_links")
        if not isinstance(links, list) or not links:
            raise ValidationError(f"{observation['id']}: assumption_links must be non-empty")
        seen: set[str] = set()
        for link in links:
            assumption_id = link.get("assumption_id")
            if assumption_id not in assumption_by_id:
                raise ValidationError(f"{observation['id']}: unknown assumption_id {assumption_id!r}")
            if assumption_id in seen:
                raise ValidationError(f"{observation['id']}: duplicate assumption link {assumption_id!r}")
            seen.add(assumption_id)
            if link.get("role") not in ALLOWED_ROLES:
                raise ValidationError(f"{observation['id']}: invalid role {link.get('role')!r}")

    accepted = {sid for sid, src in source_by_id.items() if src.get("research_admission") == "accepted"}
    missing = accepted - covered_sources
    if missing:
        raise ValidationError(f"accepted sources without evidence observations: {sorted(missing)}")

    return assumptions, sources, evidence


def short(text: str, limit: int = 155) -> str:
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def generate(assumptions: dict[str, Any], sources: dict[str, Any], evidence: dict[str, Any]) -> str:
    source_by_id = {s["source_id"]: s for s in sources["sources"]}
    observations = evidence["observations"]

    lines = [
        "# Operational cyber-risk evidence map",
        "",
        "Generated from [assumptions.yaml](assumptions.yaml), "
        "[source-admission.yaml](source-admission.yaml), and "
        "[risk-evidence.yaml](risk-evidence.yaml).",
        "",
        f"**Round:** `{assumptions['round_id']}`  ",
        f"**Accepted research-layer sources:** {sum(s.get('research_admission') == 'accepted' for s in sources['sources'])}  ",
        "**Canonical bibliography status:** deferred while concurrent preservation and OSF work is in progress.",
        "",
        "## Assumption registry",
        "",
        "| Assumption | Round assessment | Summary |",
        "|---|---|---|",
    ]
    for item in assumptions["assumptions"]:
        lines.append(
            f"| `{item['id']}` — {item['label']} | **{item['overall_code']}** | {short(item['summary'], 230)} |"
        )

    lines += [
        "",
        "## Source evidence",
        "",
        "| Source | Evidence type | Outcome / contribution | Harm status | Assumption roles |",
        "|---|---|---|---|---|",
    ]
    for obs in observations:
        src = source_by_id[obs["source_id"]]
        roles = "; ".join(f"`{x['assumption_id']}`: {x['role']}" for x in obs["assumption_links"])
        lines.append(
            f"| [{src['title']}]({src['primary_url']}) | `{obs['evidence_type']}` | "
            f"{short(obs['observed_outcome'], 215)} | {short(obs['realized_harm'], 145)} | {roles} |"
        )

    lines += [
        "",
        "## Interpretation boundary",
        "",
        "These roles describe how each source bears on an assumption. They are not source-quality scores, "
        "causal effect estimates, or proof that a provider implemented an effective safeguard.",
        "",
        "No admitted source validates the entire chain from benchmark performance to realized harm. "
        "See [bounded-review.md](bounded-review.md) for the synthesis and limitations.",
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
        print(f"wrote {OUTPUT_PATH.relative_to(ROOT.parent.parent.parent)}")
        return 0

    if not OUTPUT_PATH.exists():
        raise SystemExit(f"missing generated file: {OUTPUT_PATH}")
    current = OUTPUT_PATH.read_text(encoding="utf-8")
    if current != generated:
        raise SystemExit("evidence-map.md is stale; run build.py --write")
    print(
        f"validated {len(assumptions['assumptions'])} assumptions, "
        f"{len(sources['sources'])} admitted sources, and "
        f"{len(evidence['observations'])} observations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
