# Gemini 4 Carbon’s restricted cyber rollout

Google announced the rollout on 2026-10-28. Public sources were reviewed on 2026-11-03. This is a case note and source intake for the cyber research. The date identifies the announcement. The exact date on which the first partner received access is unresolved.

## What the public record establishes

| Evidence | Observation and scope |
|---|---|
| Announced access | Google said it would start with a subset of cyber defenders that week and gradually extend access to additional trusted Fairwind partners. It described collecting feedback and refining guardrails before wider product access. It also reported participating in the U.S. government’s voluntary pre-release testing process. The announcement gives no test result or review outcome. [Carbon announcement][carbon] |
| Cyber benchmark performance | Google reported 88.2% on SEC-bench Pro, 54.8% on ExploitGym and 71.0% on CWE-bench. On ExploitGym, Carbon scored 53.5% at the default six-hour cap and 54.8% at the extended ten-hour cap. Google used one attempt per task, the Antigravity harness, no internet access, and mitigations switched off. Success required capturing the target flag and an LLM judge confirming that the exploit used the intended vulnerability. This measures exploitation in the evaluated setup. [Carbon announcement][carbon], [Google’s ExploitGym chart][exploitgym-chart], [methodology, printed p. 3][method] |
| Carbon safety claims | Google says Carbon builds on Argon’s training, real-time misuse defenses, prompt-injection resilience and chain-of-thought monitoring. It reports zero successful evaluated attacks on Gray Swan’s indirect prompt-injection benchmark. That benchmark tests attempts to hijack the agent through content it encounters. The question here is how effectively the deployed controls prevent an authorized user or someone using their account from misusing Carbon’s cyber capability. [Carbon announcement, “Advancing frontier model safety & security”][carbon] |
| Argon and Fairwind context | Google could not rule out that unmitigated Argon reached Cyber Uplift Level 1, its cyber Critical Capability Level (CCL), and assessed Argon’s safeguarded risk as below that level. The linked report’s cyber assessment names Argon, and the official Argon model card corroborates the determination. A search of the third-party report transcription yielded no Carbon matches. Fairwind publicly describes vetting, managed access and phishing-resistant MFA, with model-specific team restrictions stated for Argon. The Carbon configuration remains unverified. [Argon model card, “Frontier Safety Assessment”][argon-card], [linked report, §3.2.2, printed p. 33][argon-report], [searchable report transcription][argon-text], [Fairwind, “Governance and trust”][fairwind] |

## What would make the decision independently scrutinizable?

DeepMind’s Frontier Safety Framework v3.1 treats deployment scope and safeguard robustness as inputs to residual-risk assessment. For models reaching a misuse capability threshold, §2.1.2 describes pre-deployment review for external deployments. When a CCL is reached, it calls for a supplemental safety case. The cyber CCL in §2.2.2 concerns uplift on high-impact attacks sufficient to create additional expected harm at severe scale. ExploitGym measures a component of that risk pathway. [Frontier Safety Framework v3.1, §§2.1.2 and 2.2.2][fsf]

1. **Threshold assessment.** What was Google’s cyber CCL determination for unmitigated Carbon, and what evidence connected its evaluation results to high-impact attack scenarios?
2. **Residual risk for the initial cohort.** Which access conditions and misuse controls were applied to Carbon, how were they tested with the partner configuration in place, and what supported the conclusion that remaining risk was acceptable for that cohort?
3. **Expansion criteria.** What observed control failures, attempted misuse, or changes in users and tool permissions would pause or trigger a reassessment before the next phase?

The Carbon announcement, evaluation methodology, public model-card index and Fairwind page yielded no Carbon-specific cyber CCL determination, residual-risk rationale for the initial cohort, or criteria for approving expansion. This is a bounded finding about the public materials reviewed. This AI-assisted review inspected the title page and cybersecurity determination in the publisher’s Argon PDF and used a third-party transcription for the document-wide term search. The announcement and methodology were inspected through public web retrieval. Exact source bytes and a capture-specific archive were not verified for this note. [Model-card index][cards]

## Research treatment

Record the model-specific rollout by its announcement date. Use the ExploitGym result as a candidate benchmark observation for `capability_access`, where the unresolved issue is whether the evaluated capability is accessible with the tools, permissions, safeguards and attempt budget of the deployment. A safeguards-off score supplies no test of whether offensive uplift persists with the deployed defenses in place. The sources are logged as deferred candidates in [the intake register][intake].

[carbon]: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
[method]: https://storage.googleapis.com/deepmind-media/gemini/gemini_4_carbon_model_evaluation.pdf#page=4
[exploitgym-chart]: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini_4_carbon_exploitgym.original.png
[argon-card]: https://deepmind.google/models/model-cards/gemini-4-argon/
[argon-report]: https://storage.googleapis.com/deepmind-media/gemini/gemini_4_safety_report.pdf#page=34
[argon-text]: https://malob.github.io/ai-system-cards/google-deepmind/gemini-4-argon/
[fairwind]: https://deepmind.google/fairwind-program/
[fsf]: https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf
[cards]: https://deepmind.google/models/model-cards/
[intake]: ../../intake.csv
