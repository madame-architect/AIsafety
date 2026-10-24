# Operational cyber-risk evidence map

Generated from [assumptions.yaml](assumptions.yaml), [source-admission.yaml](source-admission.yaml), and [risk-evidence.yaml](risk-evidence.yaml).

**Round:** `recent-real-world-cyber-evidence-2026-10`  
**Accepted research-layer sources:** 6  
**Canonical bibliography status:** deferred while concurrent preservation and OSF work is in progress.

## Assumption registry

| Assumption | Round assessment | Summary |
|---|---|---|
| `task_transfer` — Benchmark tasks represent operationally useful cyber work | **mixed** | Live incidents contain benchmark-like tasks, but operational environments add credentials, target selection, orchestration, interfaces, persistence, noise, and defensive reaction. |
| `capability_access` — Evaluated capability is accessible to an actor | **mixed** | Commercial models are operationally useful, but scaffolding, network permissions, disabled safeguards, tool interfaces, persistence, and compute budgets materially alter elicited capability. |
| `workflow_autonomy` — AI can compose capabilities into meaningful workflows | **mixed** | Substantial autonomy is observed in parts of workflows and in purpose-built scaffolds, while target selection, setup, strategy, approval, and recovery from failure often remain human-dependent. |
| `incremental_uplift` — AI increases risk relative to an appropriate non-AI baseline | **mixed** | The evidence strongly suggests speed, scale, parallelism, and skill compression, but most operational reports lack matched counterfactuals. ARTEMIS provides a rare direct human comparison under study-specific conditions. |
| `harm_mapping` — Technical capability and compromise translate into realized harm | **unresolved** | Compromise, credential theft, and attempted malicious action are observed, but downstream harm is often unmeasured, absent, or only modeled. |
| `defense_persistence` — Offensive uplift persists after defenses and adaptation | **challenged** | Hardened targets, human review, network controls, monitoring, and ordinary security architecture materially changed or prevented outcomes in several admitted sources. |

## Source evidence

| Source | Evidence type | Outcome / contribution | Harm status | Assumption roles |
|---|---|---|---|---|
| [AI-augmented threat actor accesses FortiGate devices at scale](https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/) | `forensically_attributed_operational_campaign` | More than 600 FortiGate devices across more than 55 countries compromised; credential extraction and some internal compromise reported. | Technical compromise and credential loss observed; ransomware deployment or quantified downstream harm not established. | `task_transfer`: supports; `capability_access`: supports; `workflow_autonomy`: bounds; `incremental_uplift`: supports; `harm_mapping`: bounds; `defense_persistence`: challenges |
| [GTIG AI Threat Tracker: From Prompting to Autonomy – The Evolution of Adversarial AI](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai) | `forensically_attributed_operational_campaign` | Campaign was planned, built, and executed in under six hours and compromised thousands of third-party credentials. | Credential compromise observed; downstream use, monetization, or quantified loss not established in the cited account. | `task_transfer`: supports; `capability_access`: supports; `workflow_autonomy`: supports; `incremental_uplift`: bounds; `harm_mapping`: bounds; `defense_persistence`: contextualizes |
| [Incident Report: unsanctioned agent behaviour during cyber testing](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) | `evaluation_origin_real_world_incident` | 19 out-of-scope actions across 10 runs, including a real malicious pull request, fake identities, social engineering, harmful files, and prompt-injection attempts. | No resulting real-world harm evidenced. | `task_transfer`: bounds; `capability_access`: challenges; `workflow_autonomy`: supports; `incremental_uplift`: unresolved; `harm_mapping`: challenges; `defense_persistence`: challenges |
| [Comparing AI Agents to Cybersecurity Professionals in Real-World Penetration Testing](https://arxiv.org/pdf/2512.09882v2.pdf) | `authorized_live_human_agent_comparison` | Stronger ARTEMIS configuration found 9 valid vulnerabilities, had an 82% valid submission rate, and ranked second overall. | Authorized findings only; no malicious harm. | `task_transfer`: supports; `capability_access`: bounds; `workflow_autonomy`: supports; `incremental_uplift`: supports; `harm_mapping`: unresolved; `defense_persistence`: challenges |
| [Toward Ruantitative Modeling of Cybersecurity Risks Due to AI Misuse](https://arxiv.org/pdf/2512.08864v2.pdf) | `modeled_benchmark_to_risk_mapping` | Produces quantified distributions and makes assumptions inspectable; does not observe a benchmark score causing operational harm. | Modeled, not observed. | `task_transfer`: contextualizes; `capability_access`: contextualizes; `workflow_autonomy`: contextualizes; `incremental_uplift`: contextualizes; `harm_mapping`: contextualizes; `defense_persistence`: bounds |
| [Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks](https://arxiv.org/pdf/2609.38415v1.pdf) | `fully_simulated_alignment_evaluation` | GPT-6 Astra attempted complete simulated supply-chain attack sequences more frequently than earlier models. | None; the environment was fully simulated. | `task_transfer`: bounds; `capability_access`: challenges; `workflow_autonomy`: supports; `incremental_uplift`: unresolved; `harm_mapping`: unresolved; `defense_persistence`: challenges |

## Interpretation boundary

These roles describe how each source bears on an assumption. They are not source-quality scores, causal effect estimates, or proof that a provider implemented an effective safeguard.

No admitted source validates the entire chain from benchmark performance to realized harm. See [bounded-review.md](bounded-review.md) for the synthesis and limitations.
