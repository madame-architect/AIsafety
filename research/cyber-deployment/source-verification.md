# Cyber capability evidence and deployment safeguards: source verification

**Checked: 2026-10-16. Baseline: [merged stabilization commit 12287ba](https://github.com/madame-architect/AIsafety/commit/12287bab1a763371a48660330ff9bc90a222e628).**

The five starting sources support a bounded comparative study of **how cyber capability evidence is used to justify deployment safeguards**. Their contributions differ: measured task performance, a proposed safety argument, elicited risk estimates, and two providers' stated policies. Those distinctions determine which claims the next output can make.

This check updates five existing YAML records and their generated exports. It adds no references and changes no synthesis-stream memberships. The other 271 records retain their earlier contents and inspection status. The [audit JSON](source-verification.json) records exact field changes, source URLs, PDF digests, page locators, and bounded version searches. Five dated rows in [intake.csv](../../intake.csv) record these later reviews; legacy discovery dates remain unknown.

## Versions inspected

All page references below are **1-based PDF viewer pages**, including the cover. Version status is as checked on 2026-10-16, not a continuing guarantee.

| Existing record | Inspected document | Version finding |
|---|---|---|
| `phuong_evaluatingfrontier_2024` | [arXiv v2](https://arxiv.org/abs/2403.13793v2), submitted 2024-04-05 | Latest revision listed in [arXiv history](https://arxiv.org/abs/2403.13793); first submitted 2024-03-20. The PDF cover separately prints 2024-04-08. |
| `goemans_safetycasetemplate_2024` | [arXiv v1](https://arxiv.org/abs/2411.08088v1), submitted 2024-11-12 | Only revision listed in [arXiv history](https://arxiv.org/abs/2411.08088). |
| `murray_mappingbenchmarkdata_2025` | [arXiv v2](https://arxiv.org/abs/2503.04299v2), submitted 2025-03-10 | Latest revision listed in [arXiv history](https://arxiv.org/abs/2503.04299); first submitted 2025-03-06. |
| `openai_preparednessv2_2025` | [Preparedness Framework v2](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf), updated 2025-04-15 | Official links still lead to v2; no newer numbered edition was found in the bounded check. Later issuer statements clarify and extend it. The unqualified `current` tag is removed. |
| `deepmind_frontiersafetyv31_2026` | [Frontier Safety Framework v3.1](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf), published 2026-04-17 | The [official history](https://deepmind.google/frontier-safety/) lists it first and the [explicit latest-framework link](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/) resolves to this PDF. `current` is retained with this dated basis. |

The three papers retain their preprint classifications. The bounded checks found no later peer-reviewed publication of the same works; that does not prove none exists. Besides arXiv, the checks used [DeepMind's publication listing](https://deepmind.google/research/publications/78150/), [Farquhar's publication list](https://sebastianfarquhar.com/publications/), [GovAI](https://www.governance.ai/research-paper/safety-case-template-for-frontier-ai-a-cyber-inability-argument), [AISI](https://www.aisi.gov.uk/research/safety-case-template-for-frontier-ai-a-cyber-inability-argument-2), [SaferAI](https://www.safer-ai.org/research/mapping-ai-benchmark-data-to-quantitative-risk-estimates-through-expert-elicitation), and [Papadatos's publication list](https://henrypapadatos.com/publications/). An institutional webpage's posting date is not automatically a new paper version.

## Claims and classification decisions

### Phuong: capability measurements under specified conditions

The [paper](https://arxiv.org/pdf/2403.13793v2) supports claims about its tested Gemini 1.0 setups. For example, Ultra solved 24/81 InterCode-subset challenges, 3/13 in-house challenges, and 0/13 Hack The Box challenges (Tables 6–8, p. 12). These are not estimates of operational harm or contemporary Gemini capability.

The issuer becomes `company/private`; `self_attested/subject_self` describes the developer's own evaluations (pp. 1, 3–4). The `cbrn` tag remains because the taxonomy covers discussed domains, but Appendix B supplies preliminary methods rather than model-specific CBRN results (pp. 37–38). Self-proliferation supports `self_replication` (Section 6). Grégoire Delétang's diacritics are restored from p. 1.

### Goemans: an explicit proposed safety argument

The [paper](https://arxiv.org/pdf/2411.08088v1) supports analysis of what an evaluation-based cyber inability argument needs. Its deployment purpose is explicit (p. 1, footnote 1; p. 2), while novel-attack monitoring and revision support `post_deployment` and `monitoring` (pp. 7–8). The classification therefore includes both lifecycle stages.

This is a proposed `eval_method`: the system is hypothetical (Appendix A, p. 18), and the complete argument is a template (Appendix B, p. 21). It supplies no completed model evaluation or safety certification. GovAI supplies the primary issuer classification, with UK AISI coauthorship retained in the evidence note.

### Murray: elicited estimates using an existing benchmark

The [paper](https://arxiv.org/pdf/2503.04299v2) applies five Cybench tasks to an expert-elicitation pilot (Sections 4.1–4.3, pp. 4–6). Its form becomes `paper`, with `eval_method` replacing both benchmark artifact labels. Risk coverage is coded `cyber/misuse`; the inspected study does not justify the inherited systemic-risk label.

Estimates concern one malware step, conditional on prior steps and capability access, using a supplied 25% baseline. They are not observed attack-success rates. Section 6.1 reports seven complete respondents and removal of data from two; Appendix A's participant/exclusion mapping is not fully explicit (pp. 9, 13–15). We preserve that uncertainty. SaferAI is the lead issuer; the Univ. Rennes/Inria coaffiliation remains in the note.

### OpenAI: stated requirements, with later qualifications

The [v2 PDF](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) defines cyber High/Critical capability thresholds and corresponding safeguards (Table 1, pp. 6–7). These are qualitative policy definitions, not universal benchmark cutoffs. Evaluation, monitoring, security auditing, and post-training coverage are supported by Sections 3–5 and Appendix C.3 (pp. 9–14, 21–22).

The [official launch explanation](https://openai.com/index/updating-our-preparedness-framework/) establishes the terminology **Capabilities Reports** and **Safeguards Reports**, replacing the inherited scorecard wording. It describes SAG recommendations and leadership decisions; it does not independently demonstrate safeguard effectiveness. The record's risk tags distinguish covered domains from empirically tested outcomes, including the nuclear/radiological research category.

Two later texts materially affect interpretation:

- The [GPT-5.3-Codex card, Section 5.2.1.5, final Note](https://deploymentsafety.openai.com/gpt-5-3-codex/preparedness), acknowledges ambiguous v2 wording and explains the intended internal-use trigger as High cyber capability together with long-range autonomy. This is a later issuer clarification, not a change silently attributed to the April 2025 PDF.
- The [August 18, 2026 policy statement](https://openai.com/index/pacing-model-development-cyber-capabilities/) describes practices extending beyond the existing framework and an intended future revision. It establishes why v2 alone is an incomplete current policy account, without establishing a replacement numbered edition.

### DeepMind: cyber CCL and contextual risk acceptance

The [v3.1 PDF](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf) gives cyber a **Critical Capability Level (CCL)** with recommended security level 2+ (Section 2.2.2, p. 12). It specifies no cyber Tracked Capability Level (TCL); TCLs address CBRN and ML R&D/misalignment (Section 1.2, p. 4).

For covered misuse deployments, residual-risk review and CCL safety cases inform external release, with post-market reassessment (Section 2.1.2, p. 10). Risk acceptance and security recommendations carry contextual qualifications (pp. 7–8, 11). They are not interchangeable with OpenAI's High/Critical scale.

Add monitoring/audit, post-training, harmful-manipulation (`persuasion`) and misalignment (`loss_of_control`) coverage. Auditing is a possible ML R&D/misalignment safeguard (p. 13), not universal independent certification. The [issuer update](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/) corroborates the risk-domain changes and relevant safety-case review.

## What is ready for the next output

The synthesis can compare **the evidence used, the inference from capability to risk, the safeguard trigger, who decides, and what prompts reassessment**. That comparison is an analytical use of these sources, not an assertion that they form a validated end-to-end safety system.

These five documents do not establish a common numerical conversion from benchmark performance to harm, demonstrate current model safety, or independently verify provider compliance or safeguard effectiveness. Any later claim about implementation will require evidence of the particular implementation. Murray's probabilities and Phuong's task results must retain their different meanings.

## Inspection and preservation limits

This was AI-assisted full-text inspection and a bounded version/publication check, including the relevant appendices and visual checks of key tables. It was not independent human coding or reproduction of experiments. The inherited confidence labels remain unchanged and do not certify evidence quality. [METHODS.md](../../METHODS.md) explains the explicit issuer-coding and version-date conventions.

PDF versions, URLs, and SHA-256 digests are recorded in the audit JSON. The reviewed PDFs remain intermediate copies and are not redistributed here. No independent archive of the mutable issuer pages was verified, so future comparisons should check for changes rather than assume those pages are immutable.

OSF synchronization remains a separate release task. The [release note](../../releases/stabilization-2026-10-16.md) identifies the already merged stabilization package and the observed maintenance blocker.
