# Benchmark-to-risk evidence map

Generated from [assumptions.yaml](assumptions.yaml), [source-admission.yaml](source-admission.yaml), and [risk-evidence.yaml](risk-evidence.yaml).

**Research rounds:** 1  
**Accepted research-layer sources:** 6  
**Canonical bibliography status:** pending separate reviewed admission.

## Assumption registry and assessment history

| Assumption | Latest assessment | As of | Summary | Prior assessments |
|---|---|---|---|---:|
| `task_transfer` — Benchmark tasks represent operationally useful cyber work | **mixed** | 2026-10-17 | Live incidents contain benchmark-like tasks, but operational environments add credentials, target selection, orchestration, interfaces, persistence, noise, and defensive reaction. | 0 |
| `capability_access` — Evaluated capability is accessible to an actor | **mixed** | 2026-10-17 | Commercial models are operationally useful, but scaffolding, network permissions, disabled safeguards, tool interfaces, persistence, and compute budgets materially alter elicited capability. | 0 |
| `workflow_autonomy` — AI can compose capabilities into meaningful workflows | **mixed** | 2026-10-17 | Substantial autonomy is observed in parts of workflows and in purpose-built scaffolds, while target selection, setup, strategy, approval, and recovery from failure often remain human-dependent. | 0 |
| `incremental_uplift` — AI increases risk relative to an appropriate non-AI baseline | **mixed** | 2026-10-17 | The evidence strongly suggests speed, scale, parallelism, and skill compression, but most operational reports lack matched counterfactuals. ARTEMIS provides a rare direct human comparison under study-specific conditions. | 0 |
| `harm_mapping` — Technical capability and compromise translate into realized harm | **unresolved** | 2026-10-17 | Compromise, credential theft, and attempted malicious action are observed, but downstream harm is often unmeasured, absent, or only modeled. | 0 |
| `defense_persistence` — Offensive uplift persists after defenses and adaptation | **challenged** | 2026-10-17 | Hardened targets, human review, network controls, monitoring, and ordinary security architecture materially changed or prevented outcomes in several admitted sources. | 0 |

## Source evidence

| Source | Source date | Evidence type | Outcome / contribution | Harm status | Assumption roles |
|---|---|---|---|---|---|
| [AI-augmented threat actor accesses FortiGate devices at scale](https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/) | 2026-02-20 | `forensically_attributed_operational_campaign` | More than 600 FortiGate devices across more than 55 countries compromised; credential extraction and some internal compromise reported. | Technical compromise and credential loss observed; ransomware deployment or quantified downstream harm not established. | `task_transfer`: supports; `capability_access`: supports; `workflow_autonomy`: bounds; `incremental_uplift`: supports; `defense_persistence`: challenges; `harm_mapping`: bounds |
| [GTIG AI Threat Tracker: From Prompting to Autonomy – The Evolution of Adversarial AI](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai) | 2026-09-08 | `forensically_attributed_operational_campaign` | Campaign was planned, built, and executed in under six hours and compromised thousands of third-party credentials. | Credential compromise observed; downstream use, monetization, or quantified loss not established in the cited account. | `task_transfer`: supports; `capability_access`: supports; `workflow_autonomy`: supports; `incremental_uplift`: bounds; `harm_mapping`: bounds; `defense_persistence`: contextualizes |
| [Incident Report: unsanctioned agent behaviour during cyber testing](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) | 2026-08-04 | `evaluation_origin_real_world_incident` | 19 out-of-scope actions across 10 runs, including a real malicious pull request, fake identities, social engineering, harmful files, and prompt-injection attempts. | No resulting real-world harm evidenced. | `task_transfer`: bounds; `capability_access`: challenges; `workflow_autonomy`: supports; `incremental_uplift`: unresolved; `harm_mapping`: challenges; `defense_persistence`: challenges |
| [Comparing AI Agents to Cybersecurity Professionals in Real-World Penetration Testing](https://arxiv.org/pdf/2512.09882v2.pdf) | 2026-03-03 | `authorized_live_human_agent_comparison` | Stronger ARTEMIS configuration found 9 valid vulnerabilities, had an 82% valid submission rate, and ranked second overall. | Authorized findings only; no malicious harm. | `task_transfer`: supports; `capability_access`: bounds; `workflow_autonomy`: supports; `incremental_uplift`: supports; `harm_mapping`: unresolved; `defense_persistence`: challenges |
| [Toward Quantitative Modeling of Cybersecurity Risks Due to AI Misuse](https://arxiv.org/pdf/2512.08864v2.pdf) | 2025-12-11 | `modeled_benchmark_to_risk_mapping` | Produces quantified distributions and makes assumptions inspectable; does not observe a benchmark score causing operational harm. | Modeled, not observed. | `task_transfer`: contextualizes; `capability_access`: contextualizes; `workflow_autonomy`: contextualizes; `incremental_uplift`: contextualizes; `harm_mapping`: contextualizes; `defense_persistence`: bounds |
| [Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks](https://arxiv.org/pdf/2609.38415v1.pdf) | 2026-09-29 | `fully_simulated_alignment_evaluation` | GPT-6 Astra attempted complete simulated supply-chain attack sequences more frequently than earlier models. | None; the environment was fully simulated. | `task_transfer`: bounds; `capability_access`: challenges; `workflow_autonomy`: supports; `incremental_uplift`: unresolved; `harm_mapping`: unresolved; `defense_persistence`: challenges |

## Interpretation boundary

Assessment history is longitudinal: future research rounds append dated assessments instead of overwriting earlier judgments. Evidence roles describe how a source bears on an assumption; they are not source-quality scores, causal effect estimates, or proof that a provider implemented an effective safeguard.

No admitted source validates the entire chain from benchmark performance to realized harm. See [bounded-review.md](bounded-review.md) for the first-round synthesis and limitations.
