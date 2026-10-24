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
| [operational-risk/source-captures.yaml](operational-risk/source-captures.yaml) | Exact-byte provenance for admitted operational sources |
| [expansion-reconciliation-2026-10-24.md](expansion-reconciliation-2026-10-24.md) | Completed within-issuer comparison, bibliography reconciliation, and limitations |
| [../../records.yaml](../../records.yaml) | Project-wide bibliographic authority; generates BibTeX through the existing build |

## Longitudinal units

### Commitment history

The unit is **one issuer's scoped policy provision as observed in a particular source edition**. A stable `commitment_id` links observations across editions. Each observation records the trigger, action, scope, modality, qualifications, issuer rationale, source locator, and documentary relationship to an earlier observation.

`observed` means the first observation in this dataset, not necessarily the historical origin of the policy. `revised`, `clarified`, `retained`, and `withdrawn` require a predecessor and evidence. Wording not found in a later document is a review gap, not proof of withdrawal.

### Benchmark-to-risk evidence

The unit is **one source-specific observation bearing on one or more stable assumptions**. Assumption IDs persist across research rounds. Each assumption contains an append-only `assessments` list with an assessment ID, `as_of` date, research round, coded judgment, and rationale.

Future rounds append assessments rather than rewriting previous judgments. Evidence observations distinguish operational, authorized-live, simulated, modeled, and other evidence types. Links use `supports`, `challenges`, `bounds`, `contextualizes`, or `unresolved`; these are not source-quality scores.

## How the datasets link

`dataset-links.yaml` (schema v2) distinguishes **depends on** (`policy_depends_on`), **seeks to counter** (`policy_counters`), and **assesses** (`policy_assesses`). These describe the policy argument or intended action relative to the stated risk proposition; they do not score policy effectiveness. The bridge remains the stable `assumption_id`, and evidence judgments always concern that assumption as written.

For example, the DeepMind model-weight security rationale relies on access, transfer, uplift and harm premises, but weighs whether offensive uplift persists after defensive adaptation. OpenAI containment aims to counter such persistence, while safeguard review and reassessment examine it. **`defense_persistence` means offensive gains survive defenses, not that defenses remain effective.** Its challenged assessment neither disproves safeguards nor establishes the effectiveness of any particular safeguard. Evidence does not become an effectiveness score by reversing its sign.

| Connection | Question | Evidence needed |
|---|---|---|
| Evaluation result → risk threshold | Why should performance under evaluated conditions imply the specified operational capability or risk? | Evaluation design, elicitation, access and tooling assumptions, operational comparisons |
| Risk threshold → safeguard decision | Which action follows, for which systems, with what force, exceptions, and decision authority? | Dated policy provisions and stated rationales |
| Safeguard decision → residual risk | Was the control applied, and what evidence supports its effect? | Attributed implementation evidence and separately assessed effectiveness evidence |

## Preservation and evidence boundaries

New commitment observations follow the [source capture procedure](../../provenance/source-capture.md). The two first observations remain explicit `legacy_uncaptured` exceptions; no historical hash has been invented.

The six benchmark-to-risk sources have canonical bibliography IDs and capture records. Five OpenAI source representations and these six operational sources are retained in the owner's private source bundle; all eleven payloads have been checked against their SHA-256 and length metadata. The checked archival references and exact capture basis remain explicit. This is not a public deposit or proof of original-publication byte identity. The separate AISI technical incident PDF remains pending full-text review.

Restore the bundle's `.source-captures/` directory and run `python3 scripts/audit_cyber_bibliography.py --require-capture-files` for full local byte verification. Ordinary CI validates metadata and any present bytes, but does not claim to re-download archives or inspect absent private payloads. See the [capture procedure](../../provenance/source-capture.md).

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
python3 scripts/lint_bibliography.py
python3 scripts/audit_cyber_bibliography.py
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

The commitment dataset contains **eight scoped commitments, 17 observations, and seven source observations**. One DeepMind provision has two historical editions; seven OpenAI provision histories span the beta framework, v2, an internal-use clarification, and the August/October 2026 development and containment statements. Publication date, capture date, and effective date are not interchangeable. The system-card clarification has no verified insertion date.

The benchmark-to-risk dataset remains **one bounded research round, six stable assumptions, six admitted sources, and six evidence observations**. Its earlier assessments are unchanged. The datasets have 25 analytical links, not 25 independent findings or causal relationships.

[The integration report](expansion-reconciliation-2026-10-24.md) explains changes and qualifications. Compare within an issuer before normalizing threshold names across organizations. These policy observations do not establish implementation, compliance, or safeguard effectiveness.
