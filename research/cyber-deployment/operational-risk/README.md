# Benchmark-to-risk evidence dataset

This directory is the second of the project's two linked longitudinal cyber datasets. It tracks the assumptions needed to translate cyber evaluation performance into claims about operational risk and accumulates dated empirical, operational, simulated, and modeled evidence bearing on each assumption.

It is a case study within the [broader research project](../../README.md), whose synthesis and corpus coverage extend beyond cyber evidence.

The companion [commitment history](../README.md) records provider policy changes. The datasets are linked through stable assumption IDs in [dataset-links.yaml](../dataset-links.yaml).

## Files

| File | Role |
|---|---|
| [assumptions.yaml](assumptions.yaml) | Stable assumption registry with append-only dated assessments |
| [source-admission.yaml](source-admission.yaml) | Research-round metadata and source registry |
| [risk-evidence.yaml](risk-evidence.yaml) | Source-level observations linked to assumptions |
| [evidence-map.md](evidence-map.md) | Generated longitudinal evidence map |
| [bounded-review.md](bounded-review.md) | Curated synthesis from the first bounded round |
| [build.py](build.py) | Validator and deterministic evidence-map generator |

## Longitudinal model

Each assumption has a stable `id` and an `assessments` list. New evidence or a later review of the existing evidence can add a dated assessment. Earlier assessments remain in the record. Each evidence observation records its round, admission date, source, context, access and tooling conditions, human role, defensive conditions, outcome, harm status, causal-strength description, and roles against assumptions.

The first round tracks:

- `task_transfer`
- `capability_access`
- `workflow_autonomy`
- `incremental_uplift`
- `harm_mapping`
- `defense_persistence`

## Central finding

The strongest admitted evidence concerns **AI assistance in multi-step workflows**, including some observed parallelism and short completion times. Incremental uplift against a matched non-AI baseline, the translation from compromise to severe harm, and the net effect after defenders adapt remain poorly measured.

> Purpose-built scaffolds and operational tooling can automate meaningful stages of cyber work under some conditions. The admitted studies and incident reports identify examples. The size and direction of the change in successful compromise depend on the baseline, access, target defenses, human orchestration, and downstream bottlenecks.

## Evidence boundaries

- Provider threat-intelligence reports are attributed operational evidence, not controlled causal experiments.
- An authorized live penetration test measures capability in that study environment, not malicious harm under ordinary defense.
- A fully simulated evaluation can establish behavior under a harness without establishing operational access or consequence.
- Quantitative risk models make assumptions inspectable but do not empirically validate those assumptions.
- Technical compromise and realized harm remain distinct outcomes.

The linked AISI technical incident PDF remains pending full-text review and is not counted as an independently admitted source.

## Bibliography and preservation status

The November 7 correction package was integrated on November 14, preserving original assessments and adding dated interpretation reviews. The six sources are admitted to this research dataset and to the authoritative bibliography following the [October 24 integration](../expansion-reconciliation-2026-10-24.md). Their capture metadata are recorded in [source-captures.yaml](source-captures.yaml); retained payloads remain in the owner's private bundle. Ordinary checks validate metadata and any available local bytes, without claiming to retrieve absent payloads or establish public byte reproduction. The [parent research guide](../README.md#preservation-and-evidence-boundaries) gives the strict local audit command and preservation limits. The [release guide](../../../releases/README.md) distinguishes the October 24 deposit receipt from later un-deposited changes.

## Validate and regenerate

From the repository root:

```bash
python3 research/cyber-deployment/operational-risk/build.py --check
python3 research/cyber-deployment/operational-risk/build.py --write
python3 scripts/build_cyber_datasets.py --check
```

The validator checks identifiers, research rounds, chronological assessment history, admission status, cross-file links, evidence roles, source coverage, and generated-output freshness. It does not verify source truth, causal attribution, completeness, preservation, or scholarly consensus.
