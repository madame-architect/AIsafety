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

## OpenAI: Cyber Critical capability threshold

**Commitment ID:** `openai_cyber_critical_threshold`

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
| Documentary relationship | observed |

**Scope:** Cyber Critical capability threshold

**Trigger:** Tool-augmented model can autonomously develop functional zero-day exploits across many hardened critical systems, or execute novel end-to-end cyberattack strategies from a high-level goal.

**Action:** Until Critical safeguard and security-control standards are specified, halt further development.

**Qualifications:** Critical denotes qualitatively new severe-harm pathways; this is a documentary requirement, not evidence that a model reached the threshold.

**Source rationale:** OpenAI's stated Preparedness Framework risk-control rationale; not independently verified implementation.

**Source locator:** Table 1, Cybersecurity Critical row, source Table 1 (verify PDF page); section 2.2.

**Inspection and preservation:** [Snapshot openai\_preparedness\_v2\_captured\_2026\_10\_24](#snapshot-openai_preparedness_v2_captured_2026_10_24).

## OpenAI: Cyber High capability threshold

**Commitment ID:** `openai_cyber_high_threshold`

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
| Documentary relationship | observed |

**Scope:** Cyber High capability threshold

**Trigger:** Cyber model removes bottlenecks to scaling cyber operations, including automated end-to-end operations against reasonably hardened targets or discovery and exploitation of operationally relevant vulnerabilities.

**Action:** Classify as High cybersecurity capability and require High security controls and sufficiently effective misuse safeguards before external deployment.

**Qualifications:** Requirement applies to covered models assessed at the High threshold; capability assessment and safeguards sufficiency remain issuer judgments.

**Source rationale:** OpenAI's stated Preparedness Framework risk-control rationale; not independently verified implementation.

**Source locator:** Table 1, Cybersecurity High row, source Table 1 (verify PDF page); sections 2.2 and 4.2.

**Inspection and preservation:** [Snapshot openai\_preparedness\_v2\_captured\_2026\_10\_24](#snapshot-openai_preparedness_v2_captured_2026_10_24).

## OpenAI: Cyber High internal-use safeguards

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

**Scope:** Cyber High internal-use safeguards

**Trigger:** High cybersecurity capability with large-scale internal deployment.

**Action:** Require High-standard safeguards against misalignment for large-scale internal deployment, alongside security controls.

**Qualifications:** Distinct from the external misuse-safeguard condition; scope is large-scale internal deployment.

**Source rationale:** OpenAI's stated Preparedness Framework risk-control rationale; not independently verified implementation.

**Source locator:** Table 1, Cybersecurity High row, PDF viewer p. 6.

**Inspection and preservation:** [Snapshot openai\_preparedness\_v2\_captured\_2026\_10\_24](#snapshot-openai_preparedness_v2_captured_2026_10_24).

## OpenAI: Frontier capability evaluation and reassessment

**Commitment ID:** `openai_frontier_reassessment`

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
| Documentary relationship | observed |

**Scope:** Frontier capability evaluation and reassessment

**Trigger:** Covered frontier model development and deployment, with emerging capability or risk evidence.

**Action:** Evaluate covered models during development and before deployment, maintain scalable testing with deeper reviews, and reassess risk categories and safeguards as evidence changes.

**Qualifications:** Applies within Preparedness Framework tracked categories and covered systems; no external implementation audit is implied.

**Source rationale:** OpenAI's stated Preparedness Framework risk-control rationale; not independently verified implementation.

**Source locator:** Sections 2.1, 3.1-3.3, 4.2 and 5.1, source sections 2.1, 3.1-3.3, 4.2, 5.1 (verify PDF pages).

**Inspection and preservation:** [Snapshot openai\_preparedness\_v2\_captured\_2026\_10\_24](#snapshot-openai_preparedness_v2_captured_2026_10_24).

## OpenAI: Frontier safeguard sufficiency and deployment decision

**Commitment ID:** `openai_frontier_safeguard_review`

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
| Documentary relationship | observed |

**Scope:** Frontier safeguard sufficiency and deployment decision

**Trigger:** Covered frontier model reaches High capability in a Tracked Category, including cybersecurity.

**Action:** Do not deploy until associated severe-harm risks are sufficiently minimized; Safety Advisory Group reviews capability and safeguard evidence and recommends action to leadership.

**Qualifications:** Leadership retains decision authority; source does not independently demonstrate safeguard effectiveness.

**Source rationale:** OpenAI's stated Preparedness Framework risk-control rationale; not independently verified implementation.

**Source locator:** Sections 1, 2.2, 4.2 and 5.1, source sections 1, 2.2, 4.2, 5.1 (verify PDF pages).

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

### Snapshot openai_preparedness_v2_captured_2026_10_24

**Bibliography record:** `openai_preparednessv2_2025` in [records.yaml](../../records.yaml).

**Inspected source:** [https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)

**Observed on:** 2026-10-24

**Inspection scope:** AI-assisted clause inspection of official v2 PDF, sections 2-5 and Table 1; not independent coding.

**Preservation status:** captured

**Retrieved at (UTC):** 2026-10-24T20:28:58Z

**SHA-256:** fae6e4cc6f7212a010bb9348fc0cde1fe711b9cad426c6a99db97740ee52729b

**Byte length:** 170399

**MIME type:** application/pdf

**Locator basis:** One-based PDF viewer pages including cover, and printed section/table headings.

**Preservation:** Exact official PDF response bytes hashed and retained as CI artifact; no independently checked archive. CI artifacts expire and are not a stable historical archive.

**Checked archive:** Not recorded.

**Capture basis:** Original response bytes; no archive comparison was performed.

**Archive limitation:** No independently verified permanent archive was located in this bounded pass; CI artifact is temporary.

Source URLs and recorded digests do not themselves guarantee future retrieval. This view does not fetch sources or verify their contents.
