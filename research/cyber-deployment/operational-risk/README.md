# Benchmark-to-risk evidence dataset

This directory is the second of the project's two linked longitudinal cyber datasets. It tracks the assumptions needed to translate cyber evaluation performance into claims about operational risk and accumulates dated empirical, operational, simulated, and modeled evidence bearing on each assumption.

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

Each assumption has a stable `id` and an `assessments` list. A new research round adds a dated assessment rather than overwriting the earlier one. Each evidence observation records its round, admission date, source, context, access and tooling conditions, human role, defensive conditions, outcome, harm status, causal-strength description, and roles against assumptions.

The first round tracks:

- `task_transfer`
- `capability_access`
- `workflow_autonomy`
- `incremental_uplift`
- `harm_mapping`
- `defense_persistence`

## Central finding

The strongest admitted evidence concerns **speed, scale, parallelism, and skill compression**. The weakest links are quantitative uplift against a matched non-AI baseline, translation from compromise to severe harm, and net effect after defenders adapt.

> When benchmark-relevant capabilities are available through an effective scaffold, supplied with suitable tools and permissions, and inserted into an operational workflow, they can reduce expertise, time, and labor requirements and automate meaningful stages of cyber operations. The resulting increase in successful compromise depends materially on target defenses, human orchestration, and downstream bottlenecks.

## Evidence boundaries

- Provider threat-intelligence reports are attributed operational evidence, not controlled causal experiments.
- An authorized live penetration test measures capability in that study environment, not malicious harm under ordinary defense.
- A fully simulated evaluation can establish behavior under a harness without establishing operational access or consequence.
- Quantitative risk models make assumptions inspectable but do not empirically validate those assumptions.
- Technical compromise and realized harm remain distinct outcomes.

The linked AISI technical incident PDF remains pending full-text review and is not counted as an independently admitted source.

## Bibliography and preservation status

The six sources are accepted into this research dataset. Canonical admission to `records.yaml` and exact-byte capture are still pending separate reviewed integration. The preservation and OSF infrastructure has landed; this dataset no longer describes that work as concurrent or unfinished infrastructure.

## Validate and regenerate

From the repository root:

```bash
python3 research/cyber-deployment/operational-risk/build.py --check
python3 research/cyber-deployment/operational-risk/build.py --write
python3 scripts/build_cyber_datasets.py --check
```

The validator checks identifiers, research rounds, chronological assessment history, admission status, cross-file links, evidence roles, source coverage, and generated-output freshness. It does not verify source truth, causal attribution, completeness, preservation, or scholarly consensus.
