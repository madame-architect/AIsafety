# Linked longitudinal cyber datasets

Generated from [datasets.yaml](datasets.yaml), [dataset-links.yaml](dataset-links.yaml), the commitment-history YAML, and the benchmark-to-risk evidence YAML.

## Dataset overview

| Dataset | Longitudinal unit | Current contents | Generated view |
|---|---|---:|---|
| Commitment history | Scoped policy provision observed in a document edition | 1 commitment(s), 2 observation(s) | [commitment-history.md](commitment-history.md) |
| Benchmark-to-risk evidence | Dated evidence observation bearing on a stable assumption | 6 assumption(s), 6 evidence observation(s) | [operational-risk/evidence-map.md](operational-risk/evidence-map.md) |

## Explicit linkage

| Commitment | Covered observations | Assumption | Latest assessment | Evidence roles | Why the policy depends on it |
|---|---:|---|---|---|---|
| `deepmind_cyber_ccl_model_weight_security` | 2 | `capability_access` — Evaluated capability is accessible to an actor | **mixed** as of 2026-10-17 | bounds: 1, challenges: 2, contextualizes: 1, supports: 2 | The provision governs model-weight security because the risk pathway depends on an actor obtaining usable access to the capability represented by the protected weights. |
| `deepmind_cyber_ccl_model_weight_security` | 2 | `task_transfer` — Benchmark tasks represent operationally useful cyber work | **mixed** as of 2026-10-17 | bounds: 2, contextualizes: 1, supports: 3 | The cyber capability trigger assumes that evaluated or otherwise assessed model assistance transfers to high-impact operational cyber attacks. |
| `deepmind_cyber_ccl_model_weight_security` | 2 | `incremental_uplift` — AI increases risk relative to an appropriate non-AI baseline | **mixed** as of 2026-10-17 | bounds: 1, contextualizes: 1, supports: 2, unresolved: 2 | The trigger explicitly compares expected harm with a baseline without generative AI and therefore depends on incremental uplift rather than capability in isolation. |
| `deepmind_cyber_ccl_model_weight_security` | 2 | `harm_mapping` — Technical capability and compromise translate into realized harm | **unresolved** as of 2026-10-17 | bounds: 2, challenges: 1, contextualizes: 1, unresolved: 2 | The threshold maps model assistance in attacks to additional expected harm at severe scale; evidence about technical compromise alone does not complete that inference. |
| `deepmind_cyber_ccl_model_weight_security` | 2 | `defense_persistence` — Offensive uplift persists after defenses and adaptation | **challenged** as of 2026-10-17 | bounds: 1, challenges: 4, contextualizes: 1 | The source rationale explicitly weighs automated cyber defense and societal adaptation, making persistence of offensive uplift after defense a material qualification. |

## Interpretation boundary

The commitment dataset records what providers state across document editions. The evidence dataset records what empirical, operational, simulated, or modeled sources imply for stable assumptions. The link says a policy argument relies on an assumption; it does **not** say that the evidence caused the policy change, that the policy was implemented, or that the safeguard was effective.

Future provider observations append to the commitment history. Future research rounds append source observations and dated assumption assessments rather than overwriting earlier judgments.
