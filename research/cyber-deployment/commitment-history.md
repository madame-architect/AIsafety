# Cyber safety commitments: documentary history

Generated from [evidence.yaml](evidence.yaml) and [commitments.yaml](commitments.yaml). Regenerate with `python3 scripts/build_commitments.py --write`.

These observations record policy wording. Implementation and effectiveness are **not assessed** by this pilot. Recommendation changes do not establish adoption, protection achieved, or compliance.

Publication dates describe documents; observation dates describe inspection; claimed application dates are included only when explicitly recorded. Missing values remain **Not recorded**. Predecessor links determine documentary order. A clarification preserves the earlier statement; absence of wording is not treated as withdrawal.

## Google DeepMind: Model-weight security for models reaching the cyber critical capability level.

**Commitment ID:** `deepmind_cyber_ccl_model_weight_security`

### Observation deepmind_cyber_weights_fsf_3_0

| Field | Recorded observation |
| --- | --- |
| Issuer | Google DeepMind |
| Source | [deepmind\_frontiersafetyv3\_2025](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf) |
| Document version claim | 3.0 |
| Document publication date | 2025-09-22 |
| Observed on | 2026-10-17 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | recommendation |
| Documentary relationship | observed |

**Scope:** Model-weight security for models reaching the cyber critical capability level.

**Trigger:** Cyber uplift level 1: model assistance supplies sufficient uplift in high-impact cyber attacks to produce additional expected harm at severe scale, relative to a baseline without generative AI.

**Action:** Recommends Security Level 2 (SL2).

**Qualifications:** The issuer may judge other security adequate. Recommendations can change with comparable models' capabilities and security, or the assessed benefits of releasing weights. These are conditional security goals.

**Source rationale:** The issuer expects possible automated cyber defense and societal adaptation following exfiltration to weigh against higher security levels and their innovation costs, despite potential interest from well-resourced state actors. This is the issuer's risk judgment.

**Source locator:** Section 2.2.2, Table 2.2.2.a, PDF p. 10; sections 1.6 (p. 7), 2.1.1 (p. 8), 2.2 (p. 9); baseline footnote 10 (p. 10).

**Inspection and preservation:** [Snapshot deepmind\_fsf\_3\_0\_observed\_2026\_10\_17](#snapshot-deepmind_fsf_3_0_observed_2026_10_17).

### Observation deepmind_cyber_weights_fsf_3_1

| Field | Recorded observation |
| --- | --- |
| Issuer | Google DeepMind |
| Source | [deepmind\_frontiersafetyv31\_2026](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf) |
| Document version claim | 3.1 |
| Document publication date | 2026-04-17 |
| Observed on | 2026-10-17 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | recommendation |
| Documentary relationship | revised |

**Scope:** Model-weight security for models reaching the cyber critical capability level.

**Trigger:** Cyber uplift level 1: model assistance supplies sufficient uplift in high-impact cyber attacks to produce additional expected harm at severe scale, relative to a baseline without generative AI.

**Action:** Recommends Security Level 2+ (SL2+).

**Qualifications:** The issuer may judge other security adequate. Comparable models and benefits of releasing weights remain considerations. Additional SL2+ controls are illustrative, not a mandatory checklist.

**Source rationale:** The issuer expects possible automated cyber defense and societal adaptation following exfiltration to weigh against higher security levels and their innovation costs, despite potential interest from well-resourced state actors. This is the issuer's risk judgment.

**Source locator:** Section 2.2.2, Table 2.2.2.a, PDF p. 12; sections 1.3.5 (p. 7), 2.1.1 (p. 9), 2.2 (p. 11), 5.3 (p. 17); baseline footnote 8 (p. 11).

**Compared with:** [deepmind\_cyber\_weights\_fsf\_3\_0](#observation-deepmind_cyber_weights_fsf_3_0).

**Analyst change note:** The recommended level changes from SL2 to SL2+. The cyber CCL and rationale retain their wording in the compared tables; other framework provisions also changed. This records a documentary revision, not a measured improvement in security or proof of model-specific implementation.

**Inspection and preservation:** [Snapshot deepmind\_fsf\_3\_1\_observed\_2026\_10\_17](#snapshot-deepmind_fsf_3_1_observed_2026_10_17).

## OpenAI: Conditions for continuing development under Critical cyber risk

**Commitment ID:** `openai_cyber_critical_development_gate`

### Observation openai_cyber_critical_development_gate_beta

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_preparednessbeta\_2023](https://cdn.openai.com/openai-preparedness-framework-beta.pdf) |
| Document version claim | Beta |
| Document publication date | 2023-12-18 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | observed |

**Scope:** Conditions for continuing development under Critical cyber risk

**Trigger:** Critical pre-mitigation risk is reached or forecast in a tracked category, including cyber.

**Action:** Continue capability-enhancing development only when mitigations reduce post-mitigation risk to High or lower and there is dependable alignment evidence against initiating Critical tasks without instruction.

**Qualifications:** Safety-enhancing development is not precluded; the text requires reasonable assurance rather than proof of zero risk.

**Source locator:** Restricting development, PDF viewer p. 21; Operations, pp. 22-24.

**Inspection and preservation:** [Snapshot openai\_preparedness\_beta\_observed\_2026\_10\_24](#snapshot-openai_preparedness_beta_observed_2026_10_24).

### Observation openai_cyber_critical_development_gate_v2

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_preparednessv2\_2025](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) |
| Document version claim | 2 |
| Document publication date | 2025-04-15 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | revised |

**Scope:** Conditions for continuing development under Critical cyber risk

**Trigger:** Two related triggers: (1) attained Critical cyber capability for the Table 1 conditional halt; (2) attained or forecast Critical capability in a Tracked Category, including cyber, for the additional development safeguards in section 4.4.

**Action:** For attained Critical cyber capability, halt further development until safeguard and security-control standards meeting a Critical standard are specified (Table 1). For attained or forecast Critical capability, require additional safety and security controls during development, regardless of whether or when external deployment is planned (section 4.4).

**Qualifications:** The Table 1 halt is conditional on specifying standards, not an unconditional permanent moratorium. Section 4.4 retains prospective safeguard coverage; a forecast alone is not coded as triggering the Table 1 halt. The Critical approach must address malicious internal/external actors and model misalignment. Read with the general risk-minimization process and section 4.3 qualifications. Neither rule demonstrates implementation or safeguard effectiveness.

**Source locator:** Table 1, Critical cybersecurity safeguards, PDF viewer p. 7 (printed p. 6); section 4.4, PDF viewer p. 13 (printed p. 12); context: section 2.2, p. 5 and sections 4.2-4.3, pp. 11-13.

**Compared with:** [openai\_cyber\_critical\_development\_gate\_beta](#observation-openai_cyber_critical_development_gate_beta).

**Analyst change note:** Retains prospective coverage for attained or forecast Critical capability while changing the beta post-mitigation ceiling and alignment-evidence gate into additional development safeguards plus a separate conditional halt for attained Critical cyber capability pending specified standards. Prospective safeguards did not disappear; the two triggers and their actions are not interchangeable.

**Inspection and preservation:** [Snapshot openai\_preparedness\_v2\_captured\_2026\_10\_24](#snapshot-openai_preparedness_v2_captured_2026_10_24).

### Observation openai_cyber_critical_development_gate_pacing_2026

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_pacingcyberdevelopment\_2026](https://openai.com/index/pacing-model-development-cyber-capabilities/) |
| Document version claim | Not recorded |
| Document publication date | 2026-08-18 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | revised |

**Scope:** Conditions for continuing development under Critical cyber risk

**Trigger:** Frontier research workloads involving Astra/cyber models and a planned frontier RL run under possible Critical cyber capability.

**Action:** Require stronger evidence of aligned behavior throughout training and the strictest security safeguards for Astra/cyber workloads; workloads remain paused until they meet the new security bar.

**Qualifications:** This announcement says its broader approach extends beyond the current framework. It does not label these requirements a new numbered edition or explicitly certify fulfillment of every v2 Critical standard. Reported pauses and resumes are implementation claims, not coded outcomes.

**Source locator:** Opening paragraphs 2-4; Securing our research environments, final two paragraphs; What’s next, first paragraph.

**Compared with:** [openai\_cyber\_critical\_development\_gate\_v2](#observation-openai_cyber_critical_development_gate_v2).

**Analyst change note:** Specifies and broadens development-safeguard conditions in a separate announcement. This does not establish formal replacement of v2 or certify fulfillment of its Critical-standard condition.

**Inspection and preservation:** [Snapshot openai\_pacing\_cyber\_observed\_2026\_10\_24](#snapshot-openai_pacing_cyber_observed_2026_10_24).

## OpenAI: Cyber Critical capability definition

**Commitment ID:** `openai_cyber_critical_threshold`

### Observation openai_cyber_critical_threshold_beta

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_preparednessbeta\_2023](https://cdn.openai.com/openai-preparedness-framework-beta.pdf) |
| Document version claim | Beta |
| Document publication date | 2023-12-18 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | observed |

**Scope:** Cyber Critical capability definition

**Trigger:** A tool-enabled model autonomously develops functional zero-day exploits at every severity across all software projects OR devises and executes novel end-to-end attacks on hardened targets from a high-level goal.

**Action:** Use the Critical classification in the beta risk scorecard and development safeguard decision.

**Qualifications:** The all-software quantifier belongs to the first branch; the second branch is an alternative. Classification is not a claim a model has attained it.

**Source locator:** Cybersecurity table, Critical row, PDF viewer p. 8; Restricting development, p. 21.

**Inspection and preservation:** [Snapshot openai\_preparedness\_beta\_observed\_2026\_10\_24](#snapshot-openai_preparedness_beta_observed_2026_10_24).

### Observation openai_cyber_critical_threshold_v2

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_preparednessv2\_2025](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) |
| Document version claim | 2 |
| Document publication date | 2025-04-15 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | revised |

**Scope:** Cyber Critical capability definition

**Trigger:** A tool-enabled model autonomously develops functional zero-day exploits at every severity in many hardened real-world critical systems OR devises and executes novel end-to-end attacks on hardened targets from a high-level goal.

**Action:** Use the Critical capability threshold to invoke development safeguards; the development gate is coded separately.

**Qualifications:** Both branches are retained, and no capability attainment is inferred.

**Source locator:** Table 1, Cybersecurity Critical row, PDF viewer p. 7; section 2.2, p. 5.

**Compared with:** [openai\_cyber\_critical\_threshold\_beta](#observation-openai_cyber_critical_threshold_beta).

**Analyst change note:** The first branch changes its scope from all software projects to many hardened real-world critical systems; the high-level-goal alternative remains. This documentary change alone does not quantify a shift in risk.

**Inspection and preservation:** [Snapshot openai\_preparedness\_v2\_captured\_2026\_10\_24](#snapshot-openai_preparedness_v2_captured_2026_10_24).

## OpenAI: Cyber High threshold and associated safeguard trigger

**Commitment ID:** `openai_cyber_high_threshold`

### Observation openai_cyber_high_threshold_beta

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_preparednessbeta\_2023](https://cdn.openai.com/openai-preparedness-framework-beta.pdf) |
| Document version claim | Beta |
| Document publication date | 2023-12-18 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | observed |

**Scope:** Cyber High threshold and associated safeguard trigger

**Trigger:** A tool-enabled model autonomously produces proofs of concept for high-value exploits on hardened targets, or executes cyber operations end to end without human intervention when supplied a detailed strategy.

**Action:** Treat this as High risk in the beta scorecard; use the pre-/post-mitigation ratings to trigger security and deployment controls.

**Qualifications:** Beta has four risk levels. High is not a benchmark score or directly equivalent to the later capability label.

**Source rationale:** The issuer links scarce high-value exploitation and end-to-end execution to broader access and increased attack throughput.

**Source locator:** Cybersecurity table, High row, PDF viewer p. 8; Scorecard p. 13; Safety baselines pp. 20-21.

**Inspection and preservation:** [Snapshot openai\_preparedness\_beta\_observed\_2026\_10\_24](#snapshot-openai_preparedness_beta_observed_2026_10_24).

### Observation openai_cyber_high_threshold_v2

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_preparednessv2\_2025](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) |
| Document version claim | 2 |
| Document publication date | 2025-04-15 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | revised |

**Scope:** Cyber High threshold and associated safeguard trigger

**Trigger:** A model removes scaling bottlenecks by automating end-to-end cyber operations against reasonably hardened targets OR automating discovery and exploitation of operationally relevant vulnerabilities.

**Action:** Apply High-standard security controls and external-misuse safeguards; the separately coded internal-use provision concerns misalignment safeguards.

**Qualifications:** Threshold determination uses holistic evidence and evaluation uncertainty, not a mechanical benchmark conversion. Internal-use ambiguity is retained separately.

**Source rationale:** The issuer argues that scalable automation could upset the offense/defense balance.

**Source locator:** Section 2.2 and Table 1, PDF viewer pp. 5-6; sections 3.1-3.3, pp. 9-11.

**Compared with:** [openai\_cyber\_high\_threshold\_beta](#observation-openai_cyber_high_threshold_beta).

**Analyst change note:** Reframes High from autonomous high-value exploit proofs of concept/detailed-strategy execution to removal of scaling bottlenecks. Beta risk labels and v2 capability thresholds are not treated as calibrated equivalents.

**Inspection and preservation:** [Snapshot openai\_preparedness\_v2\_captured\_2026\_10\_24](#snapshot-openai_preparedness_v2_captured_2026_10_24).

## OpenAI: Misalignment safeguards for internal use of cyber-capable models

**Commitment ID:** `openai_cyber_internal_use`

### Observation openai_cyber_internal_use_v2

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_preparednessv2\_2025](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) |
| Document version claim | 2 |
| Document publication date | 2025-04-15 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | observed |

**Scope:** Misalignment safeguards for internal use of cyber-capable models

**Trigger:** Table 1 associates High cyber capability with large-scale internal deployment; its separate risk-rationale column discusses cyber capability in conjunction with long-range autonomy.

**Action:** Require High-standard misalignment safeguards for large-scale internal deployment.

**Qualifications:** The safeguard bullet itself does not repeat the autonomy condition. Preserve this ambiguity rather than retroactively inserting the later clarification into v2. This differs from external misuse safeguards.

**Source locator:** Table 1, High cyber row and separate risk/safeguard columns, PDF viewer p. 6; Table 2, Long-range Autonomy, p. 8; Appendix C.2, pp. 19-20.

**Inspection and preservation:** [Snapshot openai\_preparedness\_v2\_captured\_2026\_10\_24](#snapshot-openai_preparedness_v2_captured_2026_10_24).

### Observation openai_cyber_internal_use_codex_clarification

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_gpt53codexsystemcard\_2026](https://deploymentsafety.openai.com/gpt-5-3-codex/gpt-5-3-codex.pdf) |
| Document version claim | Not recorded |
| Document publication date | 2026-02-05 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | clarified |

**Scope:** Misalignment safeguards for internal use of cyber-capable models

**Trigger:** The issuer states that the intended trigger combines High cyber capability with long-range autonomy.

**Action:** Interpret the internal-deployment safeguard requirement as contingent on that combination; the issuer says future framework revisions will make this explicit.

**Qualifications:** The system card is dated 2026-02-05, but the insertion/effective date of the final Note is not verified. No claimed\_application\_on is assigned. This is the issuer's interpretation, not independent proof of compliance.

**Source rationale:** The issuer says cyber capability can remove a bottleneck to internal misuse risks when combined with long-range autonomy.

**Source locator:** Section 5.2.1.5, PDF viewer pp. 29-30; final Note on p. 30 (printed p. 29).

**Compared with:** [openai\_cyber\_internal\_use\_v2](#observation-openai_cyber_internal_use_v2).

**Analyst change note:** Adds an explicit conjunctive trigger to the interpretation of the internal-use rule. Preserve the earlier table and classify as an issuer clarification, not an observed safety outcome or silently backdated wording.

**Inspection and preservation:** [Snapshot openai\_gpt53\_codex\_observed\_2026\_10\_24](#snapshot-openai_gpt53_codex_observed_2026_10_24).

## OpenAI: Evaluation updates and reassessment of frontier cyber risk

**Commitment ID:** `openai_frontier_reassessment`

### Observation openai_frontier_reassessment_beta

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_preparednessbeta\_2023](https://cdn.openai.com/openai-preparedness-framework-beta.pdf) |
| Document version claim | Beta |
| Document publication date | 2023-12-18 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | observed |

**Scope:** Evaluation updates and reassessment of frontier cyber risk

**Trigger:** Non-trivial capability changes, observed misuse, new research, or changing risk assessments.

**Action:** Maintain a frequently updated scorecard; evaluate before, during, and after training as needed and use misuse monitoring/research to revise evaluations and risk levels.

**Qualifications:** The beta gives a greater-than-twofold effective-compute increase or major algorithmic breakthrough as example evaluation triggers, and includes periodic reporting and urgent escalation.

**Source locator:** Scorecard and evaluation approach, PDF viewer pp. 13-14; Operations, pp. 23-24.

**Inspection and preservation:** [Snapshot openai\_preparedness\_beta\_observed\_2026\_10\_24](#snapshot-openai_preparedness_beta_observed_2026_10_24).

### Observation openai_frontier_reassessment_v2

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_preparednessv2\_2025](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) |
| Document version claim | 2 |
| Document publication date | 2025-04-15 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | revised |

**Scope:** Evaluation updates and reassessment of frontier cyber risk

**Trigger:** New information about risk, elicitation, capabilities or significant deployment conditions makes an existing assessment insufficient.

**Action:** Periodically review categories; reassess evaluations as elicitation improves; use scalable evaluations and deep dives, with significant model/deployment changes covered when existing reports no longer reasonably apply. Review the framework for continued sufficiency at least annually and reassess safeguards when reasonable contrary evidence emerges.

**Qualifications:** Not every incremental/distilled model is automatically re-evaluated. Section 3.2 and footnote 6 bound coverage; SAG decides ambiguous cases.

**Source locator:** Section 2.1, PDF viewer p. 5; sections 3.1-3.3, pp. 9-11; section 4.2, pp. 12-13; Appendix B, p. 16.

**Compared with:** [openai\_frontier\_reassessment\_beta](#observation-openai_frontier_reassessment_beta).

**Analyst change note:** Retains evidence-responsive reassessment while replacing the scorecard-centered mechanism with scalable evaluations, deep dives, and report-applicability tests. No fixed re-testing frequency is inferred.

**Inspection and preservation:** [Snapshot openai\_preparedness\_v2\_captured\_2026\_10\_24](#snapshot-openai_preparedness_v2_captured_2026_10_24).

## OpenAI: Isolation and assurance requirements for frontier training and evaluation

**Commitment ID:** `openai_frontier_research_containment`

### Observation openai_frontier_research_containment_pacing_2026

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_pacingcyberdevelopment\_2026](https://openai.com/index/pacing-model-development-cyber-capabilities/) |
| Document version claim | Not recorded |
| Document publication date | 2026-08-18 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | observed |

**Scope:** Isolation and assurance requirements for frontier training and evaluation

**Trigger:** Research workloads execute model-generated/untrusted code, process model output, or otherwise qualify as higher-risk cyber work.

**Action:** Require stronger workload isolation and the strictest security safeguards for Astra/cyber workloads; isolate high-risk workloads from the internet with defense in depth.

**Qualifications:** The article mixes requirements with implementation reports and testing plans. Only stated policy is coded; named security testing work is not proof of containment.

**Source locator:** Securing our research environments: Workload isolation, Network isolation, Continuous security testing, and concluding paragraphs.

**Inspection and preservation:** [Snapshot openai\_pacing\_cyber\_observed\_2026\_10\_24](#snapshot-openai_pacing_cyber_observed_2026_10_24).

### Observation openai_frontier_research_containment_containment_2026

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_frontiertrainingenvironment\_2026](https://openai.com/index/securing-our-frontier-model-training-environment/) |
| Document version claim | Not recorded |
| Document publication date | 2026-10-23 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | revised |

**Scope:** Isolation and assurance requirements for frontier training and evaluation

**Trigger:** Frontier-model training and most evaluation; safety cases for future frontier RL training/evaluation.

**Action:** Conduct frontier training without live internet access until advances in safeguards justify broader access; maintain boundaries around authorized resources and include high-compute red-teaming in safety cases for future runs.

**Qualifications:** Training/most evaluation are not the same as customer deployments or an absolute ban for every evaluation. Offline cached content is distinct from live access. No effective date is inferred from publication, and the reported October 1 resumption is not evidence of policy effectiveness.

**Source locator:** Opening policy paragraph beginning Based on the current state; Our new approach to model containment; Building an offline world; Resuming frontier training with stronger defenses, Making red-teaming part of our safety cases.

**Compared with:** [openai\_frontier\_research\_containment\_pacing\_2026](#observation-openai_frontier_research_containment_pacing_2026).

**Analyst change note:** Makes no-live-internet frontier training and red-teaming in safety cases explicit, relative to the earlier risk-tiered isolation statement. Does not establish all systems complied or that residual risk vanished.

**Inspection and preservation:** [Snapshot openai\_frontier\_training\_observed\_2026\_10\_24](#snapshot-openai_frontier_training_observed_2026_10_24).

## OpenAI: Deployment gate and safeguard sufficiency review, including cyber risk

**Commitment ID:** `openai_frontier_safeguard_review`

### Observation openai_frontier_safeguard_review_beta

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_preparednessbeta\_2023](https://cdn.openai.com/openai-preparedness-framework-beta.pdf) |
| Document version claim | Beta |
| Document publication date | 2023-12-18 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | observed |

**Scope:** Deployment gate and safeguard sufficiency review, including cyber risk

**Trigger:** A model reaches or is forecast to reach High pre-mitigation risk in a tracked category.

**Action:** Do not deploy unless post-mitigation risk is Medium or lower; SAG advises, leadership decides, and the board can reverse decisions.

**Qualifications:** Trusted-party deployment may be a mitigation. The beta restriction is expressed as post-mitigation risk ratings, not the later High capability/safeguard-report process.

**Source locator:** Restricting deployment, PDF viewer p. 21; Operations, pp. 22-24.

**Inspection and preservation:** [Snapshot openai\_preparedness\_beta\_observed\_2026\_10\_24](#snapshot-openai_preparedness_beta_observed_2026_10_24).

### Observation openai_frontier_safeguard_review_v2

| Field | Recorded observation |
| --- | --- |
| Issuer | OpenAI |
| Source | [openai\_preparednessv2\_2025](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) |
| Document version claim | 2 |
| Document publication date | 2025-04-15 |
| Observed on | 2026-10-24 |
| Claimed application date | Not recorded |
| Evidence kind | policy\_statement |
| Policy modality | requirement |
| Documentary relationship | revised |

**Scope:** Deployment gate and safeguard sufficiency review, including cyber risk

**Trigger:** A covered system reaches a High or Critical capability threshold in a Tracked Category, including cybersecurity.

**Action:** Require safeguards judged sufficient to minimize severe-harm risk for deployment; SAG reviews Capabilities and Safeguards Reports and recommends action to leadership.

**Qualifications:** Leadership retains decision authority and SSC/board oversight is described in Appendix B. Section 4.3 permits adjustments only after confirming a changed external risk landscape, assessing no meaningful overall risk increase, publicly acknowledging the adjustment, and retaining more protective safeguards than the comparator. Sufficiency is an issuer judgment, not measured effectiveness.

**Source locator:** Section 2.2, PDF viewer p. 5; section 4.2, pp. 11-13; section 4.3, p. 13; Appendix B, p. 16.

**Compared with:** [openai\_frontier\_safeguard\_review\_beta](#observation-openai_frontier_safeguard_review_beta).

**Analyst change note:** Replaces a post-mitigation score ceiling with capability-triggered safeguard sufficiency review and distinct reports. The qualification and decision authority remain explicit; no single strengthened/weakened rating is assigned.

**Inspection and preservation:** [Snapshot openai\_preparedness\_v2\_captured\_2026\_10\_24](#snapshot-openai_preparedness_v2_captured_2026_10_24).

## Source observations and preservation

### Snapshot deepmind_fsf_3_0_observed_2026_10_17

**Bibliography record:** `deepmind_frontiersafetyv3_2025` in [records.yaml](../../records.yaml).

**Inspected source:** [https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework\_3.pdf](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf)

**Observed on:** 2026-10-17

**Inspection scope:** AI-assisted inspection of the primary PDF cover, sections 1.4, 1.6, 2.1.1, 2.2 and 2.2.2, including the cyber table and its qualifications. Page locators use one-based PDF viewer pages, cover included. Observation dates in this file use UTC. This is a scoped clause review, not a new full-source classification review or independent human coding.

**Preservation status:** legacy\_uncaptured

**Retrieved at (UTC):** Not recorded

**SHA-256:** Not recorded

**Byte length:** Not recorded

**MIME type:** Not recorded

**Locator basis:** One-based PDF viewer pages, cover included; section and table labels as printed.

**Preservation:** Version-specific issuer PDF URL inspected through primary-document retrieval. No new PDF byte capture or verified independent archive is retained for this observation; no checksum is recorded. The historical publication date is not a historical capture date. A URL alone does not guarantee that the original bytes will remain retrievable.

**Checked archive:** Not recorded.

### Snapshot deepmind_fsf_3_1_observed_2026_10_17

**Bibliography record:** `deepmind_frontiersafetyv31_2026` in [records.yaml](../../records.yaml).

**Inspected source:** [https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework\_3-1.pdf](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf)

**Observed on:** 2026-10-17

**Inspection scope:** AI-assisted inspection of the primary PDF cover, sections 1.3.3, 1.3.5, 2.1.1, 2.2, 2.2.2 and 5.3, including the cyber table, security-level definition, qualifications and version history. Page locators use one-based PDF viewer pages, cover included. Observation dates in this file use UTC. This scoped comparison extends the earlier source review; it is not independent human coding.

**Preservation status:** legacy\_uncaptured

**Retrieved at (UTC):** Not recorded

**SHA-256:** Not recorded

**Byte length:** Not recorded

**MIME type:** Not recorded

**Locator basis:** One-based PDF viewer pages, cover included; section and table labels as printed.

**Preservation:** Version-specific issuer PDF URL inspected through primary-document retrieval. No new PDF byte capture or verified independent archive is retained for this observation; no checksum is recorded. The earlier cached PDF and its hash in source-verification.md belong to that earlier inspection and are not presented as a fresh capture. The historical publication date is not a historical capture date.

**Checked archive:** Not recorded.

### Snapshot openai_frontier_training_observed_2026_10_24

**Bibliography record:** `openai_frontiertrainingenvironment_2026` in [records.yaml](../../records.yaml).

**Inspected source:** [https://openai.com/index/securing-our-frontier-model-training-environment/](https://openai.com/index/securing-our-frontier-model-training-environment/)

**Observed on:** 2026-10-24

**Inspection scope:** AI-assisted inspection of the complete archived article body, including opening policy statements, Our new approach to model containment, Building an offline world, and Resuming frontier training with stronger defenses. The archived substantive body was compared with a separate live retrieval; normalized policy text matched. Only scoped policy provisions are coded, not incident, vulnerability or effectiveness findings. Retained bytes rechecked locally during PR #19 completion on 2026-10-24; no new network retrieval time is asserted.

**Preservation status:** captured

**Retrieved at (UTC):** 2026-10-24T17:35:11Z

**SHA-256:** 046cbd4cad9fdc26e827d7091a7131758e84badec93bbcd3ccdd9e014a33aeb3

**Byte length:** 482384

**MIME type:** text/html

**Locator basis:** Named headings and numbered article-body paragraphs or bullet labels in the retained HTML; navigation, duplicated table of contents, related-content cards and archive toolbar excluded.

**Preservation:** Complete article body retained as a capture-specific archived HTML representation. SHA-256 and length describe that archived response, not the live page or extracted text. The archive timestamp is an archive assertion and is not the publication date or our retrieval date. Exact-byte public reproduction of this historical file is not asserted. Follow-up recovery, comparison and fresh-retrieval results are recorded separately in provenance/html-reproducibility/README.md.

**Checked archive:** [https://web.archive.org/web/20261024161822/https://openai.com/index/securing-our-frontier-model-training-environment/](https://web.archive.org/web/20261024161822/https://openai.com/index/securing-our-frontier-model-training-environment/) (checked 2026-10-24).

**Capture basis:** Archived HTML response bytes, including archive rewriting. A separate live retrieval had identical normalized substantive article text; HTML byte identity is neither expected nor claimed.

### Snapshot openai_gpt53_codex_observed_2026_10_24

**Bibliography record:** `openai_gpt53codexsystemcard_2026` in [records.yaml](../../records.yaml).

**Inspected source:** [https://deploymentsafety.openai.com/gpt-5-3-codex/gpt-5-3-codex.pdf](https://deploymentsafety.openai.com/gpt-5-3-codex/gpt-5-3-codex.pdf)

**Observed on:** 2026-10-24

**Inspection scope:** AI-assisted inspection of cover and sections 5.1.2 and 5.2.1, with focused coding of section 5.2.1.5 and its final Note (PDF pp. 29-30). The clarification page was visually checked. The cover date does not establish when the final Note was first added; no dated revision history for that Note was verified. Model performance, implementation and effectiveness claims are not admitted as commitment observations. Retained bytes rechecked locally during PR #19 completion on 2026-10-24; no new network retrieval time is asserted.

**Preservation status:** captured

**Retrieved at (UTC):** 2026-10-24T17:32:46Z

**SHA-256:** 320635949a1e8b127af026167c4e991bb73a7e1f2ab824ee07fd764a92708107

**Byte length:** 952381

**MIME type:** application/pdf

**Locator basis:** One-based PDF viewer pages, cover included; printed page numbers may differ by one.

**Preservation:** Exact archived PDF bytes retained and hashed before extraction. Archive retrieval and current issuer-byte equality do not prove which bytes were published on the document date or inspected in any earlier review.

**Checked archive:** [https://web.archive.org/web/20260814152722id\_/https://deploymentsafety.openai.com/gpt-5-3-codex/gpt-5-3-codex.pdf](https://web.archive.org/web/20260814152722id_/https://deploymentsafety.openai.com/gpt-5-3-codex/gpt-5-3-codex.pdf) (checked 2026-10-24).

**Capture basis:** Archive PDF bytes; separately retrieved issuer PDF matched byte for byte.

### Snapshot openai_pacing_cyber_observed_2026_10_24

**Bibliography record:** `openai_pacingcyberdevelopment_2026` in [records.yaml](../../records.yaml).

**Inspected source:** [https://openai.com/index/pacing-model-development-cyber-capabilities/](https://openai.com/index/pacing-model-development-cyber-capabilities/)

**Observed on:** 2026-10-24

**Inspection scope:** AI-assisted inspection of the complete archived article body, especially Securing our research environments, Expanding chain-of-thought monitoring and What’s next. The archived substantive body was compared with a separate live retrieval on the same day; normalized policy text matched, while related-content cards differed. Only stated requirements are coded here. Retained bytes rechecked locally during PR #19 completion on 2026-10-24; no new network retrieval time is asserted.

**Preservation status:** captured

**Retrieved at (UTC):** 2026-10-24T17:33:32Z

**SHA-256:** 5e9e4065cd4ded6b1bd62bd96e8266770e4d4e93c9c326416a96879e1d72ee67

**Byte length:** 474542

**MIME type:** text/html

**Locator basis:** Named headings and numbered article-body paragraphs or bullet labels in the retained HTML; navigation, duplicated table of contents, related-content cards and archive toolbar excluded.

**Preservation:** Complete article body retained as a capture-specific archived HTML representation. SHA-256 and length describe that archived response, not the live page or extracted text. The archive timestamp is an archive assertion and is not the publication date or our retrieval date. Exact-byte public reproduction of this historical file is not asserted. Follow-up recovery, comparison and fresh-retrieval results are recorded separately in provenance/html-reproducibility/README.md.

**Checked archive:** [https://web.archive.org/web/20261016033459/https://openai.com/index/pacing-model-development-cyber-capabilities/](https://web.archive.org/web/20261016033459/https://openai.com/index/pacing-model-development-cyber-capabilities/) (checked 2026-10-24).

**Capture basis:** Archived HTML response bytes, including archive rewriting. A separate live retrieval had identical normalized substantive article text; HTML byte identity is neither expected nor claimed.

### Snapshot openai_preparedness_beta_observed_2026_10_24

**Bibliography record:** `openai_preparednessbeta_2023` in [records.yaml](../../records.yaml).

**Inspected source:** [https://cdn.openai.com/openai-preparedness-framework-beta.pdf](https://cdn.openai.com/openai-preparedness-framework-beta.pdf)

**Observed on:** 2026-10-24

**Inspection scope:** AI-assisted scoped review of the cover, cyber risk table (p. 8), scorecard and evaluation methods (pp. 13-14), and governance and safety baselines (pp. 20-26). Key cyber table visually checked. This is documentary coding, not independent human coding or experimental verification. Retained bytes rechecked locally during PR #19 completion on 2026-10-24; no new network retrieval time is asserted.

**Preservation status:** captured

**Retrieved at (UTC):** 2026-10-24T17:32:47Z

**SHA-256:** c84e3a59c7dab251e45434e0b0d3e8abadcea7293f995cf92d32269e7d290398

**Byte length:** 27448530

**MIME type:** application/pdf

**Locator basis:** One-based PDF viewer pages, cover included; printed page numbers may differ by one.

**Preservation:** Exact archived PDF bytes retained and hashed before extraction. Archive retrieval and current issuer-byte equality do not prove which bytes were published on the document date or inspected in any earlier review.

**Checked archive:** [https://web.archive.org/web/20261012222200id\_/https://cdn.openai.com/openai-preparedness-framework-beta.pdf](https://web.archive.org/web/20261012222200id_/https://cdn.openai.com/openai-preparedness-framework-beta.pdf) (checked 2026-10-24).

**Capture basis:** Archive PDF bytes; separately retrieved issuer PDF matched byte for byte.

### Snapshot openai_preparedness_v2_captured_2026_10_24

**Bibliography record:** `openai_preparednessv2_2025` in [records.yaml](../../records.yaml).

**Inspected source:** [https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)

**Observed on:** 2026-10-24

**Inspection scope:** AI-assisted reinspection of the retained v2 PDF, sections 2-4, Appendices A-B, and relevant Appendix C provisions; Table 1 visually checked. Capability thresholds, risk rationale, and safeguard columns distinguished. Not independent human coding.

**Preservation status:** captured

**Retrieved at (UTC):** 2026-10-24T20:28:58Z

**SHA-256:** fae6e4cc6f7212a010bb9348fc0cde1fe711b9cad426c6a99db97740ee52729b

**Byte length:** 170399

**MIME type:** application/pdf

**Locator basis:** One-based PDF viewer pages including cover, and printed section/table headings.

**Preservation:** The issuer retrieval timestamp and digest are retained. The recovered private capture bundle contains an earlier archived PDF with the identical SHA-256 and byte length; archive provenance comes from that retained receipt. Local byte identity was checked on 2026-10-24. The source is no longer retained only in an expiring CI artifact. Neither capture proves the bytes published in April 2025.

**Checked archive:** [https://web.archive.org/web/20261016205815if\_/https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf](https://web.archive.org/web/20261016205815if_/https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) (checked 2026-10-24).

**Capture basis:** Original response bytes; no archive comparison was performed.

Source URLs and recorded digests do not themselves guarantee future retrieval. This view does not fetch sources or verify their contents.
