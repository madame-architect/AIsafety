# TAG_VOCAB

## Scope and intent

This file defines the **canonical tag vocabulary** for the controlled tag dimensions used in the annotated bibliography:

- Risk domain
- Lifecycle stage
- Assurance function
- Threat model
- Method area

For schema details (required/optional fields, formatting rules, and allowed placeholders like `unknown`), see `SCHEMA.md`.

---

## Global tagging rules

### Tag encoding

- Tags are **multi-select** unless stated otherwise.
- Use **semicolon + space** as delimiter: `tag1; tag2`.
- Use canonical spelling and casing exactly as listed below.
- Prefer ordering tags in the order shown within each dimension.

### Handling uncertainty

- Use `unknown` when the tag dimension should apply but you cannot confidently assign a value.
- Use `not_applicable` only when the dimension is structurally irrelevant for the artifact (rare; see SCHEMA).

---

## Risk domain

Which risk domain(s) are directly analyzed, evaluated, or governed.

| Tag | Definition | Include when… | Exclude when… |
| --- | --- | --- | --- |
| `cyber` | Cybersecurity misuse or compromise (offense/defense), including tool-use intrusion and vuln exploitation. | The artifact evaluates/mitigates cyber capabilities, cyber tool-use, intrusion workflows, prompt injection for cyber tools, etc. | “Security” in the generic sense without cyber-specific content. |
| `bio` | Biological misuse risk (non-CBRN), including expert uplift for biological harm. | The artifact concerns bio misuse evaluation, bio security controls, or bio red teaming protocols. | The artifact only mentions bio as an example without methodological detail. |
| `CBRN` | Chemical, biological, radiological, nuclear (CBRN) risks, especially high-severity misuse scenarios. | The artifact targets CBRN evaluation or governance of CBRN misuse. | General “catastrophic risk” without CBRN content. |
| `persuasion` | Manipulation, misinformation, influence operations, or psychological persuasion risks. | The artifact evaluates persuasive ability, disinformation, influence, or social engineering at scale. | General “societal impact” discussion without mechanisms. |
| `autonomy` | Agentic autonomy: long-horizon planning/execution, goal pursuit, or autonomous task completion. | The artifact evaluates agents, autonomous execution, or long-horizon tool-use risks. | Single-turn chat safety without agentic framing. |
| `open-weights` | Risks and governance tied to releasing model weights (diffusion, fine-tuning, re-deployment). | The artifact studies open-weight releases, misuse adaptation via fine-tuning, or release governance. | API-only deployment with no weight-release dimension. |
| `privacy` | Data leakage, memorization, extraction, or unlearning/forgetting claims. | The artifact evaluates privacy leakage, membership inference, extraction, or unlearning verification. | Purely security or alignment topics without privacy leakage. |

**Notes**
- If a governance document is cross-cutting across many domains and does not meaningfully specialize, prefer `unknown` rather than tagging every domain.

---

## Lifecycle stage

Which part(s) of the system lifecycle the artifact primarily affects.

| Tag | Definition | Include when… |
| --- | --- | --- |
| `pretraining` | Concerns model development before initial training completes (data sourcing, compute, training pipeline). | Data governance for training, compute thresholds, training-time interventions. |
| `post-training` | Concerns alignment or modification after base training (SFT/RLHF/RLAIF, fine-tuning, safety training). | Reward modeling, alignment tuning, adversarial fine-tuning defenses. |
| `deployment` | Concerns pre-release gating and deployment-time assurance (evaluation, red teaming, release decisions). | Capability evals, safety cases, deployment controls, access policies. |
| `post-deployment` | Concerns operations after release (monitoring, incident response, continuous evaluation). | Telemetry/monitoring, incident reporting, drift detection, rollback processes. |

**Notes**
- Many artifacts span `deployment; post-deployment`. Tag both when warranted.

---

## Assurance function

What assurance role(s) the artifact supports in a safety case / audit regime.

| Tag | Definition | Typical evidence outputs |
| --- | --- | --- |
| `eval` | Produces measurements/tests of model behavior or capability. | Benchmarks, red-team results, capability thresholds, TEVV-style test protocols. |
| `mitigation` | Proposes or validates interventions that reduce risk. | Guardrails, training-time mitigations, access controls, hardening methods. |
| `monitoring` | Ongoing detection/telemetry/alerting for deployed systems. | Logs, KPIs, drift signals, anomaly detection, monitor designs. |
| `auditing` | Independent or structured verification of claims/processes (often third-party). | Audit protocols, evidence checklists, evaluation access methods, compliance verification. |
| `reporting` | Disclosure, documentation, incident reporting, or transparency mechanisms. | Model/system cards, incident reports, reporting regimes, documentation standards. |

**Notes**
- `auditing` is about **verification of claims/process**, not just “running an eval.”
- `monitoring` is **continuous/operational**, not a one-time evaluation.

---

## Threat model

Which attacker/abuse model is assumed.

| Tag | Definition | Include when… |
| --- | --- | --- |
| `non-expert uplift` | Improves capability of non-experts to cause harm. | The work targets consumer misuse or low-skill attackers. |
| `expert uplift` | Improves capability of trained experts to cause harm (harder to measure). | The work explicitly discusses expert-level assistance or domain experts. |
| `insider` | Trusted user/operator with privileged access. | Internal deployment risk, privileged misuse, employee threat. |
| `supply chain` | Compromise via data/model pipeline, dependencies, distribution, or artifacts. | Poisoning, backdoors, build integrity, signing, provenance. |
| `adaptive attacker` | Strategic attacker adapting to evaluations/controls (gaming, evasion). | Sandbagging, eval-awareness, jailbreak adaptation, monitor evasion. |

**Notes**
- If the artifact concerns evaluation gaming, jailbreaks, or evasion, `adaptive attacker` is usually appropriate.

---

## Method area

A lightweight topical index to help routing and retrieval.

| Tag | Definition | Include when… |
| --- | --- | --- |
| `governance` | Policy/regulatory frameworks, standards, organizational processes, safety cases. | RSPs, preparedness frameworks, regulatory regimes, reporting requirements. |
| `evaluation/benchmarks` | Benchmarking, evaluation suites, TEVV methods, red teaming protocols. | New evaluations, benchmark infrastructure, external eval access. |
| `monitoring` | Monitorability, telemetry, continuous assurance, incident detection. | CoT monitoring, post-deploy telemetry frameworks, drift monitoring. |
| `security` | Security-to-safety work: jailbreaks, prompt injection, backdoors/poisoning, robustness to attacks. | Offensive/defensive security methods affecting safety assurance. |
| `interpretability` | Mechanistic interpretability, internal signal analysis, causal probing for safety. | Feature attribution, representation analysis, interpretability-based controls. |
| `post-training/alignment` | Post-training methods for alignment, reward modeling, refusal training. | RLHF/RLAIF, reward models, safety tuning and persistence. |
| `compute governance` | Compute measurement, reporting, and enforcement-related methods. | Compute thresholds, accounting, hardware telemetry and reporting regimes. |

---

## Deprecated and free-text exceptions

This tag vocabulary is intentionally small. If you encounter a concept not captured:

1) First try to represent it using **multiple tags** (e.g., `security; evaluation/benchmarks`).
2) If it still does not fit, use `Method area: governance` and capture the nuance in free-text fields (`Annotation`, `Limitations / open questions`), rather than creating a one-off tag.
3) Propose a new tag only if it would plausibly recur.

---

## Common confusions

### Deployment vs post-deployment

- Use **`deployment`** for *gating decisions* and *pre-release evaluation* (even if the method could be automated).
- Use **`post-deployment`** for *operational monitoring*, *incident handling*, and *continuous assurance after release*.

### Monitoring vs auditing

- **Monitoring** = continuous signals/telemetry used during operations.
- **Auditing** = structured verification that an org’s claims/processes are true (often third-party), which may *use* monitoring outputs as evidence.

### Eval vs auditing

- **Eval** = measurement protocol or benchmark result.
- **Auditing** = assurance activity that checks whether evals were done correctly, whether results are trustworthy, and whether governance commitments were met.

### Security vs risk domain

- `security` is a **method area** (how you study/control problems).
- `cyber` is a **risk domain** (what harms you are worried about).  
  A paper can be `Method area: security` without being `Risk domain: cyber` (e.g., backdoors in general models).

### Open-weights vs supply chain

- `open-weights` (risk domain) is about *release and downstream adaptation*.
- `supply chain` (threat model) is about *compromise in the pipeline*, which can apply to both closed and open weights.

---

## Tagging decision tree (text flowchart)

```
START
 |
 |-- 1) What is the primary subject of the artifact?
 |     |
 |     |-- A) Governance / policy / standards / organizational process?
 |     |      -> Method area: governance
 |     |      -> Assurance function: reporting (often) and/or auditing (if verification is central)
 |     |      -> Lifecycle stage: deployment (default) + post-deployment if operations/incident response is central
 |     |
 |     |-- B) Benchmark / evaluation / testing protocol / red teaming method?
 |     |      -> Method area: evaluation/benchmarks
 |     |      -> Assurance function: eval (add auditing if third-party/verification focus)
 |     |      -> Lifecycle stage: deployment (default); add post-deployment if continuous evaluation is described
 |     |
 |     |-- C) Mitigation / alignment / training-time or post-training intervention?
 |     |      -> Method area: post-training/alignment (or security if mitigation is security-hardening)
 |     |      -> Assurance function: mitigation (add eval if it includes measurement)
 |     |      -> Lifecycle stage: pretraining and/or post-training (and deployment if it is a deploy-time guardrail)
 |     |
 |     |-- D) Runtime monitoring / telemetry / incident detection?
 |     |      -> Method area: monitoring
 |     |      -> Assurance function: monitoring (add reporting if disclosure regime is central)
 |     |      -> Lifecycle stage: post-deployment (add deployment if it is also used as a gate)
 |     |
 |     |-- E) Security-to-safety attack/defense analysis (jailbreaks, poisoning, backdoors)?
 |            -> Method area: security
 |            -> Assurance function: eval (attack measurement) and/or mitigation (defense)
 |            -> Threat model: adaptive attacker (for gaming/jailbreaks) and/or supply chain (for poisoning/backdoors)
 |
 |-- 2) Assign Risk domain:
 |     - Does the artifact directly concern cyber, bio, CBRN, persuasion, autonomy, open-weights, or privacy?
 |     - If cross-cutting and not specialized -> Risk domain: unknown
 |
 |-- 3) Assign Threat model:
 |     - If evaluation gaming/evasion/jailbreak adaptation -> adaptive attacker
 |     - If poisoning/backdoors/build integrity -> supply chain
 |     - If internal privileged misuse -> insider
 |     - If misuse uplift framed explicitly -> non-expert uplift and/or expert uplift
 |
END
```

---

## Done when

- [ ] Each controlled tag dimension has a canonical list with concise, non-overlapping definitions.
- [ ] “Common confusions” addresses at least: deployment vs post-deployment, monitoring vs auditing, and eval vs auditing.
- [ ] A tagging decision tree is provided that guides users to consistent tags without adding new tag values.
- [ ] Any one-off or idiosyncratic tagging needs are directed to free-text fields rather than new controlled tags.
