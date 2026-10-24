# Cyber capability evidence and safety commitments

This research area now consists of **two linked longitudinal datasets**:

1. **Commitment history** — how frontier-AI providers change cyber capability thresholds, deployment rules, security requirements, monitoring duties, and qualifications over time.
2. **Benchmark-to-risk evidence** — which assumptions are needed to translate evaluation performance into claims about operational cyber risk, and what evidence supports, challenges, bounds, or contextualizes each assumption.

The datasets remain analytically distinct. Provider statements are not evidence of implementation or effectiveness, and operational incidents do not by themselves explain why a provider revised a policy.

## Dataset map

| File | Role |
|---|---|
| [datasets.yaml](datasets.yaml) | Declares the two datasets, their authoritative files, units of analysis, longitudinal keys, and time fields |
| [dataset-links.yaml](dataset-links.yaml) | Authoritative links from stable commitment IDs to stable benchmark-to-risk assumption IDs |
| [longitudinal-map.md](longitudinal-map.md) | Generated joint view of both datasets and their current links |
| [commitments.yaml](commitments.yaml) | Authoritative policy-provision observations |
| [evidence.yaml](evidence.yaml) | Source-edition observations and preservation metadata for commitment history |
| [commitment-history.md](commitment-history.md) | Generated documentary history |
| [operational-risk/assumptions.yaml](operational-risk/assumptions.yaml) | Stable assumption registry with append-only dated assessment history |
| [operational-risk/source-admission.yaml](operational-risk/source-admission.yaml) | Research rounds and admitted source registry |
| [operational-risk/risk-evidence.yaml](operational-risk/risk-evidence.yaml) | Source observations linked to assumptions |
| [operational-risk/evidence-map.md](operational-risk/evidence-map.md) | Generated benchmark-to-risk evidence map |
| [../../records.yaml](../../records.yaml) | Project-wide bibliographic authority; generates BibTeX through the existing build |

## Longitudinal units

### Commitment history

The unit is **one issuer's scoped policy provision as observed in a particular source edition**. A stable `commitment_id` links observations across editions. Each observation records the trigger, action, scope, modality, qualifications, issuer rationale, source locator, and documentary relationship to an earlier observation.

`observed` means the first observation in this dataset, not necessarily the historical origin of the policy. `revised`, `clarified`, `retained`, and `withdrawn` require a predecessor and evidence. Wording not found in a later document is a review gap, not proof of withdrawal.

### Benchmark-to-risk evidence

The unit is **one source-specific observation bearing on one or more stable assumptions**. Assumption IDs persist across research rounds. Each assumption contains an append-only `assessments` list with an assessment ID, `as_of` date, research round, coded judgment, and rationale.

Future rounds append assessments rather than rewriting previous judgments. Evidence observations distinguish operational, authorized-live, simulated, modeled, and other evidence types. Links use `supports`, `challenges`, `bounds`, `contextualizes`, or `unresolved`; these are not source-quality scores.

## How the datasets link

`dataset-links.yaml` records when a commitment argument **depends on** an assumption. The benchmark-to-risk dataset then records evidence bearing on that assumption. The bridge is the stable `assumption_id`.

For example, the current DeepMind model-weight security provision depends on assumptions about capability access, transfer to operational tasks, incremental uplift over a no-AI baseline, translation to severe harm, and persistence after defenses and adaptation. Evidence can update those assumptions without being treated as the cause of the policy revision.

| Connection | Question | Evidence needed |
|---|---|---|
| Evaluation result → risk threshold | Why should performance under evaluated conditions imply the specified operational capability or risk? | Evaluation design, elicitation, access and tooling assumptions, operational comparisons |
| Risk threshold → safeguard decision | Which action follows, for which systems, with what force, exceptions, and decision authority? | Dated policy provisions and stated rationales |
| Safeguard decision → residual risk | Was the control applied, and what evidence supports its effect? | Attributed implementation evidence and separately assessed effectiveness evidence |

## Preservation and evidence boundaries

New commitment observations follow the [source capture procedure](../../provenance/source-capture.md). The two first observations remain explicit `legacy_uncaptured` exceptions; no historical hash has been invented.

The benchmark-to-risk sources are active in the research dataset, but their canonical bibliography admission and exact-byte capture remain separate reviewed work. `source-admission.yaml` records that state rather than treating the earlier research environment as preservation.

Keep these distinctions explicit:

- Policy statement versus implementation evidence.
- Implementation evidence versus effectiveness evidence.
- Benchmark result versus operational observation.
- Attempt versus technical action, compromise, credential or data loss, persistence, destructive action, and quantified harm.
- Provider-authored telemetry versus independent evidence.

## Validate and regenerate

From the repository root:

```bash
python3 scripts/build.py --check
python3 scripts/build_commitments.py --check
python3 research/cyber-deployment/operational-risk/build.py --check
python3 scripts/build_cyber_datasets.py --check
python3 -m unittest discover -s tests -v
```

To regenerate the views:

```bash
python3 scripts/build_commitments.py --write
python3 research/cyber-deployment/operational-risk/build.py --write
python3 scripts/build_cyber_datasets.py --write
```

Validation checks structure, identifiers, cross-file references, chronological assessment history, and generated-output freshness. It does not establish source truth, causal attribution, completeness, policy compliance, safeguard effectiveness, or scholarly consensus.

## Current scope

The commitment dataset currently contains one DeepMind provision observed across two framework editions. The benchmark-to-risk dataset contains one bounded research round, six stable assumptions, six admitted sources, and six evidence observations.

The next substantive expansion should add provider commitment histories and empirical sources only when their versions, locators, preservation status, and relationship to existing IDs are explicit. Compare within an issuer before normalizing threshold names across organizations.
