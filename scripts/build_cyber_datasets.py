#!/usr/bin/env python3
"""Validate the two linked cyber longitudinal datasets and render their joint map."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
DIRECTORY = ROOT / "research" / "cyber-deployment"
MANIFEST_PATH = DIRECTORY / "datasets.yaml"
LINKS_PATH = DIRECTORY / "dataset-links.yaml"
COMMITMENTS_PATH = DIRECTORY / "commitments.yaml"
ASSUMPTIONS_PATH = DIRECTORY / "operational-risk" / "assumptions.yaml"
RISK_EVIDENCE_PATH = DIRECTORY / "operational-risk" / "risk-evidence.yaml"
OUTPUT_PATH = DIRECTORY / "longitudinal-map.md"

ALLOWED_RELATIONSHIPS = {"policy_depends_on"}
ALLOWED_ROLES = {"supports", "challenges", "bounds", "contextualizes", "unresolved"}


class ValidationError(ValueError):
    pass


def load(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValidationError(f"{path.name}: root must be a mapping")
    return data


def keyed(items: Any, key: str, label: str) -> dict[str, dict[str, Any]]:
    if not isinstance(items, list) or not items:
        raise ValidationError(f"{label}: must be a non-empty list")
    result: dict[str, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict):
            raise ValidationError(f"{label}: item must be a mapping")
        value = item.get(key)
        if not isinstance(value, str) or not value:
            raise ValidationError(f"{label}: missing {key}")
        if value in result:
            raise ValidationError(f"{label}: duplicate {key} {value!r}")
        result[value] = item
    return result


def latest_assessment(assumption: dict[str, Any]) -> dict[str, Any]:
    assessments = assumption.get("assessments")
    if not isinstance(assessments, list) or not assessments:
        raise ValidationError(f"{assumption['id']}: missing assessments")
    return sorted(assessments, key=lambda item: item["as_of"])[-1]


def validate() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    manifest = load(MANIFEST_PATH)
    links = load(LINKS_PATH)
    commitments = load(COMMITMENTS_PATH)
    assumptions = load(ASSUMPTIONS_PATH)
    evidence = load(RISK_EVIDENCE_PATH)

    if manifest.get("schema_version") != "cyber-longitudinal-datasets-v1":
        raise ValidationError("datasets.yaml: unsupported schema_version")
    dataset_by_id = keyed(manifest.get("datasets"), "id", "datasets")
    if set(dataset_by_id) != {"commitment_history", "benchmark_to_risk_evidence"}:
        raise ValidationError("datasets.yaml must declare exactly the two longitudinal datasets")
    for dataset in dataset_by_id.values():
        authority_files = dataset.get("authority_files")
        if not isinstance(authority_files, list) or not authority_files:
            raise ValidationError(f"{dataset['id']}: authority_files must be non-empty")
        for relative in authority_files:
            if not isinstance(relative, str) or not (DIRECTORY / relative).is_file():
                raise ValidationError(f"{dataset['id']}: missing authority file {relative!r}")
        generated_view = dataset.get("generated_view")
        if not isinstance(generated_view, str) or not (DIRECTORY / generated_view).is_file():
            raise ValidationError(f"{dataset['id']}: missing generated view {generated_view!r}")
        for field in ("unit_of_analysis", "longitudinal_key", "observation_key", "source_key"):
            if not dataset.get(field):
                raise ValidationError(f"{dataset['id']}: missing {field}")
    linkage = manifest.get("linkage")
    if not isinstance(linkage, dict) or linkage.get("authority_file") != "dataset-links.yaml":
        raise ValidationError("datasets.yaml: linkage authority_file must be dataset-links.yaml")
    if linkage.get("bridge_key") != "assumption_id":
        raise ValidationError("datasets.yaml: bridge_key must be assumption_id")
    if links.get("schema_version") != "cyber-dataset-links-v1":
        raise ValidationError("dataset-links.yaml: unsupported schema_version")

    commitment_by_observation = keyed(commitments.get("observations"), "id", "commitment observations")
    commitment_ids = {item.get("commitment_id") for item in commitment_by_observation.values()}
    if None in commitment_ids:
        raise ValidationError("commitment observation missing commitment_id")

    assumption_by_id = keyed(assumptions.get("assumptions"), "id", "assumptions")
    evidence_by_id = keyed(evidence.get("observations"), "id", "risk evidence")
    evidence_by_assumption: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for obs in evidence_by_id.values():
        for item in obs.get("assumption_links", []):
            assumption_id = item.get("assumption_id")
            if assumption_id not in assumption_by_id:
                raise ValidationError(f"{obs['id']}: unknown assumption_id {assumption_id!r}")
            if item.get("role") not in ALLOWED_ROLES:
                raise ValidationError(f"{obs['id']}: invalid evidence role {item.get('role')!r}")
            evidence_by_assumption[assumption_id].append({"observation_id": obs["id"], "role": item["role"]})

    link_by_id = keyed(links.get("links"), "id", "dataset links")
    seen_pairs: set[tuple[str, str]] = set()
    for link in link_by_id.values():
        commitment_id = link.get("commitment_id")
        assumption_id = link.get("assumption_id")
        if commitment_id not in commitment_ids:
            raise ValidationError(f"{link['id']}: unknown commitment_id {commitment_id!r}")
        if assumption_id not in assumption_by_id:
            raise ValidationError(f"{link['id']}: unknown assumption_id {assumption_id!r}")
        if link.get("relationship") not in ALLOWED_RELATIONSHIPS:
            raise ValidationError(f"{link['id']}: invalid relationship")
        pair = (commitment_id, assumption_id)
        if pair in seen_pairs:
            raise ValidationError(f"duplicate commitment/assumption pair {pair!r}")
        seen_pairs.add(pair)
        observation_ids = link.get("commitment_observation_ids")
        if not isinstance(observation_ids, list) or not observation_ids:
            raise ValidationError(f"{link['id']}: commitment_observation_ids must be non-empty")
        for observation_id in observation_ids:
            observation = commitment_by_observation.get(observation_id)
            if observation is None:
                raise ValidationError(f"{link['id']}: unknown commitment observation {observation_id!r}")
            if observation.get("commitment_id") != commitment_id:
                raise ValidationError(f"{link['id']}: observation does not belong to commitment_id")
        if not link.get("rationale"):
            raise ValidationError(f"{link['id']}: missing rationale")
        if assumption_id not in evidence_by_assumption:
            raise ValidationError(f"{link['id']}: linked assumption has no risk evidence")

    return manifest, links, commitments, assumptions, evidence


def short(value: Any, limit: int = 180) -> str:
    text = " ".join(str(value).split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def generate(manifest: dict[str, Any], links: dict[str, Any], commitments: dict[str, Any],
             assumptions: dict[str, Any], evidence: dict[str, Any]) -> str:
    assumption_by_id = {item["id"]: item for item in assumptions["assumptions"]}
    commitment_observations = commitments["observations"]
    commitment_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for observation in commitment_observations:
        commitment_groups[observation["commitment_id"]].append(observation)

    evidence_roles: dict[str, Counter[str]] = defaultdict(Counter)
    for observation in evidence["observations"]:
        for item in observation["assumption_links"]:
            evidence_roles[item["assumption_id"]][item["role"]] += 1

    lines = [
        "# Linked longitudinal cyber datasets",
        "",
        "Generated from [datasets.yaml](datasets.yaml), [dataset-links.yaml](dataset-links.yaml), "
        "the commitment-history YAML, and the benchmark-to-risk evidence YAML.",
        "",
        "## Dataset overview",
        "",
        "| Dataset | Longitudinal unit | Current contents | Generated view |",
        "|---|---|---:|---|",
        f"| Commitment history | Scoped policy provision observed in a document edition | "
        f"{len(commitment_groups)} commitment(s), {len(commitment_observations)} observation(s) | "
        "[commitment-history.md](commitment-history.md) |",
        f"| Benchmark-to-risk evidence | Dated evidence observation bearing on a stable assumption | "
        f"{len(assumption_by_id)} assumption(s), {len(evidence['observations'])} evidence observation(s) | "
        "[operational-risk/evidence-map.md](operational-risk/evidence-map.md) |",
        "",
        "## Explicit linkage",
        "",
        "| Commitment | Covered observations | Assumption | Latest assessment | Evidence roles | Why the policy depends on it |",
        "|---|---:|---|---|---|---|",
    ]
    for link in links["links"]:
        assumption = assumption_by_id[link["assumption_id"]]
        latest = latest_assessment(assumption)
        roles = evidence_roles[assumption["id"]]
        role_text = ", ".join(f"{key}: {roles[key]}" for key in sorted(roles))
        lines.append(
            f"| `{link['commitment_id']}` | {len(link['commitment_observation_ids'])} | "
            f"`{assumption['id']}` — {assumption['label']} | **{latest['code']}** as of {latest['as_of']} | "
            f"{role_text} | {short(link['rationale'], 210)} |"
        )

    lines += [
        "",
        "## Interpretation boundary",
        "",
        "The commitment dataset records what providers state across document editions. The evidence dataset "
        "records what empirical, operational, simulated, or modeled sources imply for stable assumptions. "
        "The link says a policy argument relies on an assumption; it does **not** say that the evidence caused "
        "the policy change, that the policy was implemented, or that the safeguard was effective.",
        "",
        "Future provider observations append to the commitment history. Future research rounds append source "
        "observations and dated assumption assessments rather than overwriting earlier judgments.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()

    values = validate()
    rendered = generate(*values)
    if args.write:
        OUTPUT_PATH.write_text(rendered, encoding="utf-8")
        print(f"wrote {OUTPUT_PATH.relative_to(ROOT)}")
        return 0
    if not OUTPUT_PATH.exists():
        raise SystemExit(f"missing generated file: {OUTPUT_PATH}")
    if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
        raise SystemExit("longitudinal-map.md is stale; run build_cyber_datasets.py --write")
    print("validated two linked longitudinal datasets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
