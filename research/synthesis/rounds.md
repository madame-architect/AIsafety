# Dated research rounds and reading events

Generated from [rounds.yaml](rounds.yaml). These are research annotations linked to canonical [records.yaml](../../records.yaml), not a competing bibliography. Selection is purposeful and claim-sensitive; this is not systematic search or independent human review. Reading depth and replication are separate, with event-specific status below. Original inherited reading labels remain in [coverage.csv](coverage.csv).

Capture metadata identify retained source representations. The validator hashes locally present files and reports absent private payloads; generated prose does not claim a fresh network/archive retrieval. Use `python3 scripts/build_research.py --check --require-capture-files` to require local byte verification. Hashes do not establish source truth or completeness. Stable IDs and chronological rounds support review; Git history records changes to earlier annotations.

## thematic-challenge-2026-11-14

**As of:** 2026-11-14. **Base commit:** `269d2856bab868ecce3d80ac2fb36f273fb5d22a`.

**Question:** Which missing arguments and counterevidence change the existing broad synthesis, and which consequential numerical/version claims survive deeper source inspection?

**Selection basis:** Purposive, claim-sensitive selection from the existing corpus and reconciliation queue. The baseline has27 claims/60 mapped keys,226 unmapped roles, and181 records without inherited full-text labels. Four complementary themes include27 initially unmapped records; three mapped sources receive targeted numerical/version checks. This is not a systematic sample or preregistration. The working selection is recorded before integration; source acquisition began in parallel.

**Stopping rule:** Finish one reviewable bounded round with explicit source scopes and thematic consequences. Read manageable claim-critical texts fully where feasible; use scoped methods/appendix checks for long or related editions. Stop chasing inaccessible historical inputs after a documented bounded attempt; omit or qualify affected numbers. Carry forward the remaining corpus and deferred themes.

| Theme | Why selected | Canonical keys |
|---|---|---|
| Oversight, control and learning from weaker feedback | Tests whether the inference-time oversight narrative misses training results, stronger simple comparators, control protocols or monitorability constraints. | `burns_weakstronggeneralization_2024`, `lang_debatehelpsweak_2025`, `arnesen_trainingwindebates_2024`, `greenblatt_controlimprovingsafety_2024`, `sudhir_benchmarkscalableoversight_2025`, `korbak_chainthoughtmonitorability_2025`, `openai_monitoringmonitorability_2025` |
| Safeguards, adaptive evaluation and collateral effects | Tests positive methodological/control evidence against attack adaptivity, judge and utility limits; resolves HarmBench family and CyberSecEval2 numerical leads. | `chao_jailbreakbenchopen_2024`, `mazeika_harmbenchstandardized_2024`, `harmbench_standardizedevaluation_2024`, `bhatt_cyberseceval2wide_2024`, `pavlova_automatedredteaming_2024`, `qi_safetyalignmentshould_2025`, `hayes_inexactunlearningneeds_2024` |
| Institutional conditions for useful audits and external evaluation | Challenges the assumption that external access or transparency alone provides assurance; examines institutional alternatives, selection, independence and proposed process benefits. | `casper_blackboxaccessaudits_2024`, `raji_outsideroversight_2022`, `longpre_safeharbor_2024`, `longpre_inhouseevaluation_2025`, `mokander_auditinglargelanguagemodels_2024`, `raji_closingaccountabilitygap_2020`, `charnock_expandingexternalaccess_2026` |
| Multi-metric and human-context evaluation | Adds noncyber evidence that could change the transfer argument: user interaction, measurement validity, cost, data documentation and multidimensional benchmark results. | `gebru_datasheets_2021`, `kapoor_aiagentsmatter_2024`, `amironesei_aria_pilot_2025`, `liang_helm_2023`, `wang_decodingtrust_2023`, `huang_trustllm_2024` |
| Leading numerical and version claims | Closes precise access/locator gaps where possible; keeps unresolved experiment provenance as a numerical hold without blocking other findings. | `wijk_rebench_2025`, `lin_artemispenetration_2026`, `xu_benchmarkingleakage_2024` |

### Event index

| Event | Source | Reading | Edition / coverage effect | Relevance |
|---|---|---|---|---|
| [r2_oversight_01](#r2_oversight_01) | `sudhir_benchmarkscalableoversight_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r2_oversight_02](#r2_oversight_02) | `arnesen_trainingwindebates_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_oversight_03](#r2_oversight_03) | `lang_debatehelpsweak_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_oversight_04](#r2_oversight_04) | `burns_weakstronggeneralization_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r2_oversight_05](#r2_oversight_05) | `greenblatt_controlimprovingsafety_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_oversight_06](#r2_oversight_06) | `korbak_chainthoughtmonitorability_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r2_oversight_07](#r2_oversight_07) | `openai_monitoringmonitorability_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_safeguards_01](#r2_safeguards_01) | `chao_jailbreakbenchopen_2024` | Full text | same_record / complete_record_text | claim_evidence |
| [r2_safeguards_02](#r2_safeguards_02) | `mazeika_harmbenchstandardized_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r2_safeguards_03](#r2_safeguards_03) | `harmbench_standardizedevaluation_2024` | Metadata only | uncertain / scoped_review | duplicate_work_family |
| [r2_safeguards_04](#r2_safeguards_04) | `bhatt_cyberseceval2wide_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_safeguards_05](#r2_safeguards_05) | `hayes_inexactunlearningneeds_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r2_safeguards_06](#r2_safeguards_06) | `pavlova_automatedredteaming_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_safeguards_07](#r2_safeguards_07) | `qi_safetyalignmentshould_2025` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r2_safeguards_08](#r2_safeguards_08) | `hayes_inexactunlearningneeds_2024` | Inaccessible | uncertain / none | unresolved |
| [r2_safeguards_09](#r2_safeguards_09) | `qi_safetyalignmentshould_2025` | Inaccessible | related_edition / none | unresolved |
| [r2_institutions_01](#r2_institutions_01) | `charnock_expandingexternalaccess_2026` | Full text | same_record / complete_record_text | claim_evidence |
| [r2_institutions_02](#r2_institutions_02) | `casper_blackboxaccessaudits_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r2_institutions_03](#r2_institutions_03) | `raji_outsideroversight_2022` | Full text | same_record / complete_record_text | claim_evidence |
| [r2_institutions_04](#r2_institutions_04) | `longpre_safeharbor_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_institutions_05](#r2_institutions_05) | `raji_closingaccountabilitygap_2020` | Full text | same_record / complete_record_text | claim_evidence |
| [r2_sociotechnical_01](#r2_sociotechnical_01) | `gebru_datasheets_2021` | Full text | same_record / complete_record_text | claim_evidence |
| [r2_sociotechnical_02](#r2_sociotechnical_02) | `kapoor_aiagentsmatter_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_sociotechnical_03](#r2_sociotechnical_03) | `amironesei_aria_pilot_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_sociotechnical_04](#r2_sociotechnical_04) | `liang_helm_2023` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_sociotechnical_05](#r2_sociotechnical_05) | `wang_decodingtrust_2023` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_sociotechnical_06](#r2_sociotechnical_06) | `huang_trustllm_2024` | Abstract only | same_record / scoped_review | background |
| [r2_claimchecks_01](#r2_claimchecks_01) | `wijk_rebench_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_claimchecks_02](#r2_claimchecks_02) | `wijk_rebench_2025` | Selected sections | related_edition / scoped_review | background |
| [r2_claimchecks_03](#r2_claimchecks_03) | `lin_artemispenetration_2026` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_claimchecks_04](#r2_claimchecks_04) | `lin_artemispenetration_2026` | Inaccessible | uncertain / none | unresolved |
| [r2_claimchecks_05](#r2_claimchecks_05) | `xu_benchmarkingleakage_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r2_claimchecks_06](#r2_claimchecks_06) | `xu_benchmarkingleakage_2024` | Full text | related_edition / scoped_review | claim_evidence |
| [r2_claimchecks_07](#r2_claimchecks_07) | `xu_benchmarkingleakage_2024` | Full text | related_edition / scoped_review | background |

<a id="r2_oversight_01"></a>
### r2_oversight_01

**Source:** `sudhir_benchmarkscalableoversight_2025`. **Theme:** oversight_control. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Canonical preprint is arXiv 2504.03731, year2025; retained v1 cover names the ICLR2025 BiAlign workshop. No main-conference publication claim is made.

**Inspected scope:** All 15 PDF pages of accessible extracted text read: main §§1–5, captions, Table 1, references, and Appendices A–D including setup, pseudocode and prompts. Linked code was not inspected.

**Locators:** §2 ASD definition and weak-baseline examples, printed pp 3–4; §3.1 benchmark limitations; §4 demonstrative results; §5 and Appendix A: 100 GSM8K questions, one gpt-4o-mini judge; Table 1 printed p 9; Appendices B–D printed pp 12–15

**Visual check:** No independent visual figure/table inspection; extracted text, captions and readable table cells only.

**Findings:**

- Agent score difference compares the reward for prompted true-answer advocacy versus prompted false-answer advocacy; judge accuracy need not measure the same incentive under consultancy.
- In the demonstrative100-question, one-judge setting, debate has higher reported average ASD than the tested consultancy and NaiveJudge variants. The protocol called Propaganda is a single-argument proxy, not an actual RLHF training run.
- The authors distinguish average ASD from worst-case catastrophic failure and call their experiments small/demonstrative.

**Counterevidence / alternative:** Truth/falsehood are simulated with instructed current models and known ground truth. Extrapolating ASD versus expected agent score to future models is proposed rather than validated; the work does not demonstrate general incentive compatibility.

**Limits:** Plot coordinates/error bars were not digitized and linked implementation was not inspected. Printed pseudocode duplicates agent_response rather than appending adversary_response; whether this is only a documentation error is unresolved and no implementation-error conclusion is drawn.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C32](claims.md#c32)

**Relevance rationale:** Adds affirmative oversight/control evidence and conditions missing from the existing broad map; source counts are not independent corroboration.

**Next check:** Use the metric distinction without the headline that debate beats RLHF. Inspect pinned implementation before numerical reuse or before attributing significance to pseudocode discrepancies.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2504.03731v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2504.03731v1) |
| `retrieved_at` | 2026-11-14T17:14:37Z |
| `attempted_at` | 2026-11-14T17:14:37Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 4971b2edc689bcea2e82b2be25a7c1da14ef1927a3be56f386d507ffbd90f49d |
| `byte_length` | 1819262 |
| `mime_type` | application/pdf |
| `published_on` | 2025-03-31 |
| `version_claim` | arXiv 2504.03731v1; ICLR2025 BiAlign workshop |
| `locator_basis` | One-based PDF viewer pages count cover; printed pages agree unless separately stated. Retrieval timestamp also records completion of the observed retrieval attempt, not its subsecond start. |
| `capture_path` | .source-captures/synthesis-4971b2edc689bcea2e82b2be25a7c1da14ef1927a3be56f386d507ffbd90f49d.pdf |

<a id="r2_oversight_02"></a>
### r2_oversight_02

**Source:** `arnesen_trainingwindebates_2024`. **Theme:** oversight_control. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. The retained arXiv 2409.16636v1 matches the canonical preprint title/authors. Final-venue or later-version equivalence was not checked.

**Inspected scope:** Complete main text §§1–6, printed pp 1–10; acknowledgments/references inspected in the extraction; Appendices A–G, printed pp 16–23, plus H opening/evaluation prompt on p 24. The rest of H and sample transcriptsI pp 31–48 were not read.

**Locators:** §§2.1–2.4 task, protocols and endpoints; §§3.1–3.2 judge/SFT/DPO training; §4.2 reported training gain; §4.3 information exposure versus refutation; §5.2 limitations; Appendix B training data; Appendix D judge labels; Appendix G one-turn ablation

**Visual check:** No independent visual figure/table inspection; extracted text, captions and readable table cells only.

**Findings:**

- The paper trains Llama 3-8B debaters with SFT then modified self-play DPO and reports more accurate judgments as debate skill improves; this adds an actual training strand beyond the earlier inference-time comparisons.
- On 433 filtered QuALITY-HARD validation questions, the paper reports a 4-percentage-point increase in GPT-4-Turbo judge accuracy between SFT and fully trained debate models; this is source-reported, not independently recomputed.
- Double consultancy closes much of the gap: pooled checkpoint accuracies are reported as 68% single consultancy, 72% ensembled, 75% double consultancy and77% debate. One-turn experiments provide little evidence that explicit refutation drives accuracy.
- The judge is finetuned on prior human judgments and initial SFT uses prior human/GPT-4 transcripts; the claim that gains require no ground-truth training signal is limited to the subsequent self-play objective, not the whole pipeline.

**Counterevidence / alternative:** Information asymmetry over reading comprehension differs from a general expertise gap. Double consultancy and one-turn results favor evidence exposure and training incentives over a simple refutation explanation. Dataset/transcript lineage overlaps Michael/Khan work, so this is not independent raw evidence from those sources.

**Limits:** No full 48-page read, remaining prompt/transcript appendix read, chart transcription, significance recomputation or experiment replication. Main text and captions were checked; graph values were not independently digitized.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C29](claims.md#c29)

**Relevance rationale:** Adds affirmative oversight/control evidence and conditions missing from the existing broad map; source counts are not independent corroboration.

**Next check:** Retain a qualitative affirmative training result; verify remaining prompts/transcripts and uncertainty calculation before leading publication with the 4-point estimate.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2409.16636v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2409.16636v1) |
| `retrieved_at` | 2026-11-14T17:14:35Z |
| `attempted_at` | 2026-11-14T17:14:35Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 7866d600d306563a5c6428b30b51176fb9ca58b1f4f2352e9e2ea8de58c90c69 |
| `byte_length` | 6927971 |
| `mime_type` | application/pdf |
| `published_on` | 2024-09-25 |
| `version_claim` | arXiv 2409.16636v1 |
| `locator_basis` | One-based PDF viewer pages count cover; printed pages agree unless separately stated. Retrieval timestamp also records completion of the observed retrieval attempt, not its subsecond start. |
| `capture_path` | .source-captures/synthesis-7866d600d306563a5c6428b30b51176fb9ca58b1f4f2352e9e2ea8de58c90c69.pdf |

<a id="r2_oversight_03"></a>
### r2_oversight_03

**Source:** `lang_debatehelpsweak_2025`. **Theme:** oversight_control. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Canonical arXiv 2501.13124 identifies this v1; retained PDF has9 pages, while the inherited ledger says a 17-page full read. The earlier representation/edition remains unverified, so this event does not certify that prior reading label.

**Inspected scope:** Selected introduction/related-work distinction, complete methods/setup and main-results/ablation/limitations text, including Tables 1–5 and Figure 2–3 captions. Final references and any final-AAAI-version differences were not completely checked.

**Locators:** Preliminaries PGR definition; Methods and Experimental Setups; Table 2 raw accuracy and PGR; Tables 4–5 comparator/ensemble ablations; Ablation on number of turns; Limitations and Conclusion

**Visual check:** No independent visual figure/table inspection; extracted text, captions and readable table cells only.

**Findings:**

- Debate ensembles used to train a weak Qwen-7B supervisor improve the subsequently trained Qwen-14B student on all four tested converted binary NLP tasks relative to listed baselines. This is training via improved weak supervision, not only inference-time judge assistance.
- PGR percentages76.5, 69.2, 56.5, 70.0 in Table 2 correspond to raw accuracy differences of 2.6, 2.7, 1.3, 1.4 percentage points over the weak models; normalization and denominator must remain explicit.
- The authors use a four-member ensemble and three debate turns. More turns did not improve final performance in the reported two-task ablation; they acknowledge extra cost, a small 7B/14B size gap and weak consultancy comparator.

**Counterevidence / alternative:** The best result combines debate, diverse sampling and ensembles with more computation; the comparison does not isolate debate as a universally superior training intervention or establish superhuman alignment.

**Limits:** No complete-document reread, final venue authentication, plot digitization, significance/raw-run verification or replication. The converted binary tasks and model/compute gap constrain transfer.

**Replication:** `not_performed`. **Numerical check:** Documentary arithmetic only: 100*(student−weak)/(ceiling−weak), using rounded Table 2 accuracies, reproduces76.5/69.2/56.5/70.0. No model experiments or statistical uncertainty reproduced.

**Relevance:** `claim_evidence`. **Claim links:** [C28](claims.md#c28), [C29](claims.md#c29)

**Relevance rationale:** Adds affirmative oversight/control evidence and conditions missing from the existing broad map; source counts are not independent corroboration.

**Next check:** Add the training strand and cost/comparator conditions. Resolve the 9-versus17-page prior-reading representation before treating inherited full-text provenance as established; confirm final AAAI metadata separately.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2501.13124v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2501.13124v1) |
| `retrieved_at` | 2026-11-14T17:14:34Z |
| `attempted_at` | 2026-11-14T17:14:34Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 5cb3e0c22dccb620d392e0f81adae5d003c05ee5a76a3f4c391d0c21233e7815 |
| `byte_length` | 269056 |
| `mime_type` | application/pdf |
| `published_on` | 2025-01-21 |
| `version_claim` | arXiv 2501.13124v1; AAAI copyright notice visible but final proceedings identity not independently checked |
| `locator_basis` | One-based PDF viewer pages count cover; printed pages agree unless separately stated. Retrieval timestamp also records completion of the observed retrieval attempt, not its subsecond start. |
| `capture_path` | .source-captures/synthesis-5cb3e0c22dccb620d392e0f81adae5d003c05ee5a76a3f4c391d0c21233e7815.pdf |

<a id="r2_oversight_04"></a>
### r2_oversight_04

**Source:** `burns_weakstronggeneralization_2024`. **Theme:** oversight_control. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. The canonical record names ICML2024 proceedings. This capture is the original arXiv 2312.09390v1, 14Dec2023; equivalence with the final proceedings edition was not established. An initial v3 route returned404; the arXiv submission history identified v1.

**Inspected scope:** Selected primary preprint text: pp 1–10 abstract/introduction/related work, methodology and main results; §5.1 pp 11–12 overfitting text; §6.1–6.2 pp 16–18 disanalogies/future-work text. Remaining methods/results pages and appendices were not completely read.

**Locators:** §3 PGR and weak/strong/ceiling setup; §4.1 tasks and no downstream RL step; §4.2 task-dependent results; §§4.3.1–4.3.2 bootstrap/confidence loss; §5.1 overfitting; §6.1 imitation saliency and pretraining leakage

**Visual check:** No independent visual figure/table inspection; extracted text, captions and readable table cells only.

**Findings:**

- Strong students trained on weak labels can outperform their weak supervisors on the tested NLP, chess and reward-modeling tasks, with substantial task-dependent residual gaps.
- Auxiliary confidence loss improves many NLP settings; bootstrapping improves chess but has little/no improvement in the reported NLP/reward-modeling preliminary comparisons. No method works universally.
- The authors explicitly do not study the RL optimization step on the learned reward model. They identify weak-error imitation and pretraining leakage as disanalogies that could make the proxy overly optimistic.

**Counterevidence / alternative:** Positive recovery of held-out task performance is useful experimental progress rather than assurance about a deployed reward model. Ground truth was available for methodology development/evaluation, and future latent superhuman knowledge could be harder to elicit.

**Limits:** Large49-page preprint only selected sections; not final ICML verification, complete appendix read, graph transcription or replication. PDF extraction reported a recoverable xref warning; inspected text is coherent, but complete extraction fidelity was not certified.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C28](claims.md#c28)

**Relevance rationale:** Adds affirmative oversight/control evidence and conditions missing from the existing broad map; source counts are not independent corroboration.

**Next check:** Inspect the final ICML edition and missing appendices before final numerical citation; keep qualitative recovery and task-dependent failure modes. Reconcile metadata claiming independence from the subject when OpenAI authors studied internal GPT-family models.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2312.09390v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2312.09390v1) |
| `retrieved_at` | 2026-11-14T17:17:16Z |
| `attempted_at` | 2026-11-14T17:17:16Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 720656b49d4c00dac26d6ebe10dad0d8482d3bcc87640a66b73867730b89515f |
| `byte_length` | 2299371 |
| `mime_type` | application/pdf |
| `published_on` | 2023-12-14 |
| `version_claim` | arXiv 2312.09390v1; related to canonical ICML2024 work |
| `locator_basis` | One-based PDF viewer pages count cover; printed pages agree unless separately stated. Retrieval timestamp also records completion of the observed retrieval attempt, not its subsecond start. |
| `capture_path` | .source-captures/synthesis-720656b49d4c00dac26d6ebe10dad0d8482d3bcc87640a66b73867730b89515f.pdf |

<a id="r2_oversight_05"></a>
### r2_oversight_05

**Source:** `greenblatt_controlimprovingsafety_2024`. **Theme:** oversight_control. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Publisher-owned mlresearch/v235 metadata explicitly identifies this 42-page PDF as greenblatt24a, ICML2024 pp 16295–16336, matching canonical fields. The proceedings landing returned503 and the ordinary PDF route404; the publisher repository supplied the linked PDF.

**Inspected scope:** Published primary main text §§1–6, printed pp 1–9, including Table 1 and figure captions; Appendix K sampling/uncertainty text pp 22–23 and selected Appendix L/M protocol details/Table 5 pp 23–25. Other appendices/examples not fully read.

**Locators:** §§2.1–2.5 resources, metrics, audit assumptions and simplifications; Table 1 printed p 4; §3.5 trusted editing p 8; §5/Impact Statement pp 8–9; Appendix K pp 22–23; Table 5 p 25

**Visual check:** No independent visual figure/table inspection; extracted text, captions and readable table cells only.

**Findings:**

- AI control evaluates whole protocols under intentional-subversion threat models, adding an affirmative system-level intervention strand beyond evaluating a model alone. Trusted editing and safeguarded untrusted monitoring improve the constructed safety/usefulness frontier relative to simple baselines.
- Table 1 reports trusted editing at 20% with 92% scenario safety and94% rescaled usefulness. Safety is no submitted exploitable backdoor over a simulated5000-problem scenario, not per-problem accuracy or deployment safety.
- High-quality human labor is simulated by trusted GPT-4, audit correctness benefits from the backdoor definition, and model interactions on 1500 problems are resampled into2000 simulated5000-problem scenarios. The study has no validation/test split and constrains red-team state/tools.

**Counterevidence / alternative:** The controlled protocol comparison provides positive evidence conditional on the threat model, but optimistic auditor assumptions, constrained attacks, resampling and task reuse could inflate estimates. It does not establish natural scheming incidence or ordinary deployment harm reduction.

**Limits:** No full 42-page read, remaining detailed red-team prompts/example investigation, raw simulations or replication. The observed HTTP MIME was application/octet-stream; PDF type was verified from%PDF bytes and pdfinfo. Publisher raw URL is mutable; local bytes/hash identify the inspected edition.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C30](claims.md#c30)

**Relevance rationale:** Adds affirmative oversight/control evidence and conditions missing from the existing broad map; source counts are not independent corroboration.

**Next check:** Use the published edition and qualitative protocol improvement; carry metric/auditor/sampling assumptions with any92%/94% figure. No need to hold the broader argument on unreplicated simulation estimates.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/greenblatt24a/greenblatt24a.pdf) |
| `final_url` | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/greenblatt24a/greenblatt24a.pdf) |
| `retrieved_at` | 2026-11-14T17:18:05Z |
| `attempted_at` | 2026-11-14T17:18:05Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 21ff7e1fba042526de65b36c9973babd26b417c29d6d40f28f74e0970aa069a6 |
| `byte_length` | 759508 |
| `mime_type` | application/pdf |
| `published_on` | 2024-07-08 |
| `version_claim` | ICML2024 PMLR235 greenblatt24a, publisher repository PDF; last-file-commit metadata d9021075a7f9c88a75dac45955d17fe46bb3a4e3 |
| `locator_basis` | One-based PDF viewer pages count cover; printed pages agree unless separately stated. Retrieval timestamp also records completion of the observed retrieval attempt, not its subsecond start. |
| `capture_path` | .source-captures/synthesis-21ff7e1fba042526de65b36c9973babd26b417c29d6d40f28f74e0970aa069a6.pdf |

<a id="r2_oversight_06"></a>
### r2_oversight_06

**Source:** `korbak_chainthoughtmonitorability_2025`. **Theme:** oversight_control. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Canonical arXiv 2507.11473 work matches retained v2; the inherited ledger specifically describes v2. This fresh full read does not create an additional previously non-full record.

**Inspected scope:** All 11 PDF pages of accessible extracted text read: §§1–6, Figure 1 caption and references. No separately linked source papers/interactives were read for this event.

**Locators:** §1.1 externalized reasoning does not guarantee incriminating content; §1.2 necessity versus propensity; §3 direct/end-to-end evaluation proposals; §4 development/deployment choices; §5 process-supervision and other limitations

**Visual check:** No independent visual figure/table inspection; extracted text, captions and readable table cells only.

**Findings:**

- The paper argues for CoT as an additional monitoring channel without requiring a complete faithful account of all computation. It distinguishes necessity to reason externally from propensity to verbalize.
- It explicitly allows tradeoffs: process supervision could improve alignment enough to justify a small loss of monitorability; preserving current CoT behavior unconditionally can miss productive safety interventions.
- It recommends direct/end-to-end adversarial evaluations and treating monitorability alongside propensity and operational response, rather than equating monitor accuracy with harm prevention.

**Counterevidence / alternative:** A benign-looking CoT does not establish absence of bad intent; some harmful tasks need little external reasoning and future models may hide or compress relevant information. These limits coexist with conditional utility.

**Limits:** This is a position/research-agenda paper that synthesizes cited experiments, not a new primary monitoring-effect trial. Architecture diagram was read through caption/text, not independently visually evaluated; references are not audited by reading their citation strings.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C31](claims.md#c31)

**Relevance rationale:** Adds affirmative oversight/control evidence and conditions missing from the existing broad map; source counts are not independent corroboration.

**Next check:** Use as conceptual framing/background supporting a separate empirical monitorability study, not as independent empirical corroboration of that study.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2507.11473v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2507.11473v2) |
| `retrieved_at` | 2026-11-14T17:14:34Z |
| `attempted_at` | 2026-11-14T17:14:34Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 420d2c12a787b6903242b4369d3b6c5c7949e27fdfa62dd4c2dc5b4e2f399307 |
| `byte_length` | 416330 |
| `mime_type` | application/pdf |
| `published_on` | 2025-12-07 |
| `version_claim` | arXiv 2507.11473v2 |
| `locator_basis` | One-based PDF viewer pages count cover; printed pages agree unless separately stated. Retrieval timestamp also records completion of the observed retrieval attempt, not its subsecond start. |
| `capture_path` | .source-captures/synthesis-420d2c12a787b6903242b4369d3b6c5c7949e27fdfa62dd4c2dc5b4e2f399307.pdf |

<a id="r2_oversight_07"></a>
### r2_oversight_07

**Source:** `openai_monitoringmonitorability_2025`. **Theme:** oversight_control. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Canonical arXiv 2512.18311 matches retained v1 and its full author/title cover. Corporate-only author metadata can be replaced by the 12 named authors from the primary cover while retaining issuer OpenAI.

**Inspected scope:** Selected90-page primary PDF: pp 1–3 and5–8 conceptual/metric/scope definitions; pp 15–26 outcome-label limitations and §§4–9 results/scaling/follow-ups/discussion, including captions. Detailed intervention estimators and appendicesA–J not comprehensively read.

**Locators:** §2.1 non-intervention g-mean²=TPR×TNR and separate intervention estimator; §2.2 observation scopes; §3.3 outcome-property label/filter limitations, pp 15–16; §4 current-model monitor comparisons; §5 obfuscation model organisms; §§6.1–6.3 scaling and compute; §7 follow-up limitations; §9 discussion

**Visual check:** No independent visual figure/table inspection; extracted text, captions and readable table cells only.

**Findings:**

- Across the tested suite, giving monitors CoT generally improves detection over action-only scope; more monitor reasoning effort and agent follow-up CoT can improve measured monitorability. This is affirmative operational-design evidence with conditions.
- The authors report no consistent average degradation across two frontier RL runs, while noting a middle-training decrease, task-specific declines, direct obfuscation effects and uncertainty at larger scale. This bounds a blanket claim that ordinary RL necessarily destroys monitorability.
- For non-intervention evaluations the metric is TPR×TNR, deliberately insensitive to target prevalence; intervention evaluations use a separately defined estimator that was not fully checked. Neither provides operational positive predictive value or harm prevented by itself. Some ground-truth labels use model judges and ambiguous cases are filtered.
- A smaller agent at higher reasoning effort can improve monitorability at matched measured capability, but costs more inference compute; single seeds, mostly in-distribution capability tests and unmodeled latency limit the suggested deployment tradeoff. General follow-ups need multiple samples, and in some subtle-framing tasks follow-ups degrade monitorability.

**Counterevidence / alternative:** The findings make monitoring an intervention choice rather than an intrinsic model property. Shared provider models/monitors, label construction, averaging and missing adversarial/deployment denominators limit transfer; conditional gains do not make a safety guarantee.

**Limits:** No full 90-page read, complete appendix, figure digitization, raw metric or experimental reproduction. Agent-vs-monitor comparisons use OpenAI monitors; filters/data differ across plots and only tool-free environments are used for some external-model comparisons.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C31](claims.md#c31)

**Relevance rationale:** Adds affirmative oversight/control evidence and conditions missing from the existing broad map; source counts are not independent corroboration.

**Next check:** Complete relevant appendix estimators, per-environment filtering and calibration before any numerical deployment claim; retain the positive scope/compute result and its cost/nulls now. Correct author metadata from the primary cover.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2512.18311v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2512.18311v1) |
| `retrieved_at` | 2026-11-14T17:14:39Z |
| `attempted_at` | 2026-11-14T17:14:39Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | ecb8076f08298956cc535d8ae516653808ade0d1fb62a7c06ac465392b88ada8 |
| `byte_length` | 39927761 |
| `mime_type` | application/pdf |
| `published_on` | 2025-12-20 |
| `version_claim` | arXiv 2512.18311v1 |
| `locator_basis` | One-based PDF viewer pages count cover; printed pages agree unless separately stated. Retrieval timestamp also records completion of the observed retrieval attempt, not its subsecond start. |
| `capture_path` | .source-captures/synthesis-ecb8076f08298956cc535d8ae516653808ade0d1fb62a7c06ac465392b88ada8.pdf |

<a id="r2_safeguards_01"></a>
### r2_safeguards_01

**Source:** `chao_jailbreakbenchopen_2024`. **Theme:** safeguards. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. The canonical arXiv URL resolves to v5; retained v5 cover names the NeurIPS2024 Datasets and Benchmarks track and matches title/byline. Exact byte equality with a separately hosted conference PDF is not claimed.

**Inspected scope:** Read all25 PDF text pages sequentially: main §§1–5, references, AppendicesA–I including judge dataset, extra evaluations, reproducibility, prompts, checklist and data card. Linked datasets/artifacts and image-only plot values were not separately inspected.

**Locators:** §§3.1,3.4–3.7; §4 Tables1–3; AppendicesB–E; data cardI.5.2

**Visual check:** No figure pixels inspected; extracted table text and captions only.

**Findings:**

- Artifacts, explicit prompts/templates/judges and query/token accounting make scoped comparisons reproducible;100 matched benign behaviors provide an over-refusal sanity check.
- Judge selection uses300 examples (200 attack pairs plus100 benign XS-Test examples), compared to three expert-majority labels; this is a scoped reference, not universal judge validity.
- JBB-Behaviors reuses27% TDC/HarmBench and18% AdvBench behaviors; GOAT later reuses JBB behaviors and judge. These evaluations have explicit dataset dependence.

**Counterevidence / alternative:** The published defense comparison uses transferred precomputed jailbreaks, so even strong reductions are lower bounds on adaptive worst-case success. The authors explicitly describe existing-attack-only evaluation as unsuitable in data cardI.5.2. Benign refusal is not a full utility test.

**Limits:** Static historical models and policy-based100-behavior sample. Figures/captions and text were read but plots not digitized. No benchmark execution or independent human labeling.

**Replication:** `not_performed`. **Numerical check:** Read Table1/2/3 numerical text and source proportions directly; no rerun. §3.1/AppendixB says55% original,18% AdvBench,27% TDC/HarmBench.

**Relevance:** `claim_evidence`. **Claim links:** [C33](claims.md#c33)

**Relevance rationale:** Adds a positive evaluation-method strand and independently stated adaptive-evaluation limit; provides shared-dataset provenance rather than independent corroboration.

**Next check:** Use this positive methodological contribution while preserving attack adaptation, cost exclusions and judge-reference limitations. Pin dataset/model/judge revisions before numerical publication.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2404.01318v5) |
| `final_url` | [Source](https://arxiv.org/pdf/2404.01318v5) |
| `retrieved_at` | 2026-11-14T17:16:05Z |
| `attempted_at` | 2026-11-14T17:16:05Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URLs are retained. Independent archival preservation is not claimed. |
| `sha256` | 78c2f251cc101bce36e3dd3138fc0c89f7b73c599099f79ec55318165fe4a981 |
| `byte_length` | 641300 |
| `mime_type` | application/pdf |
| `published_on` | 2024-10-31 |
| `version_claim` | arXiv v5; cover NeurIPS2024 |
| `locator_basis` | PDF viewer pages include cover; these papers print page numbers matching viewer pages. HTML locators use named sections and tables. |
| `capture_path` | .source-captures/synthesis-78c2f251cc101bce36e3dd3138fc0c89f7b73c599099f79ec55318165fe4a981.pdf |

<a id="r2_safeguards_02"></a>
### r2_safeguards_02

**Source:** `mazeika_harmbenchstandardized_2024`. **Theme:** safeguards. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Read the ICML/PMLR2024 final PDF linked by the official PMLR page; the canonical key points to arXiv. Title and12-author byline match arXiv v2 metadata, but final/preprint byte or complete text equivalence is not claimed.

**Inspected scope:** Read cover/abstract, selected main setup/metrics and results passages, §§4.3,5.1–5.2, AppendixA.1 R2D2 method, AppendixC.1/C.2/C.5.1–2 judge/held-out setup, and Table12/its full caption. Did not read all44pages or every template/behavior/figure.

**Locators:** PMLR PDF pp1,7–9,15,18–21,33; §§4.3,5.1–5.2; AppendixA.1,C.1,C.2,C.5.1–2; Table12

**Visual check:** No figure pixels inspected; extracted table text and captions only.

**Findings:**

- The official proceedings identify the same named HarmBench study:12 authors, full Automated Red Teaming and Robust Refusal title,18 attack methods and33 model/defense targets.
- The benchmark defines100 validation/410 test behaviors and prohibits tuning on test/semantically identical behaviors. Its noncopyright success criterion counts a clear attempt even if generated code is incorrect; copyright uses actual-content matching.
- R2D2 is a positive adversarial-training result on tested attacks. §5.2 reports improvements across attacks but smaller gains for methods unlike its training adversary. Table12 explicitly distinguishes the DPO-trained ZephyrBeta comparator from R2D2 trained without DPO.

**Counterevidence / alternative:** No attack/defense is uniformly effective. A comparative ASR reduction is not deployable security or harm prevention; Table12 does not isolate a matched utility-preservation causal effect.

**Limits:** The raw PDF response advertises application/octet-stream but bytes begin %PDF and parse as44pages; capture MIME records detected PDF type. Judge validation/prompt tuning uses a human-labeled validation set, not a new independent held-out judge test. Full44page reading and exact preprint/final comparison remain incomplete.

**Replication:** `not_performed`. **Numerical check:** No independent numerical recomputation or experiment reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C34](claims.md#c34)

**Relevance rationale:** Adds affirmative defense progress and shows why metric/utility comparators are part of the inference.

**Next check:** Retain positive model-level defense evidence; keep precise success criteria, attack diversity, training comparator and utility limits. Complete final/preprint and DOI lineage before merging or aliasing keys.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/mazeika24a/mazeika24a.pdf) |
| `final_url` | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/mazeika24a/mazeika24a.pdf) |
| `retrieved_at` | 2026-11-14T17:16:07Z |
| `attempted_at` | 2026-11-14T17:16:07Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URLs are retained. Independent archival preservation is not claimed. |
| `sha256` | 6b87608143d17d5b2ae4f26f06892f41a2d2a356f83091d6f4920392e5dba56b |
| `byte_length` | 3050143 |
| `mime_type` | application/pdf |
| `published_on` | 2024 |
| `version_claim` | ICML2024, PMLR235:35181–35224 |
| `locator_basis` | PDF viewer pages include cover; these papers print page numbers matching viewer pages. HTML locators use named sections and tables. |
| `capture_path` | .source-captures/synthesis-6b87608143d17d5b2ae4f26f06892f41a2d2a356f83091d6f4920392e5dba56b.pdf |

<a id="r2_safeguards_03"></a>
### r2_safeguards_03

**Source:** `harmbench_standardizedevaluation_2024`. **Theme:** safeguards. **Reading:** Metadata only. **Coverage effect:** `scoped_review`.

**Edition match:** `uncertain`. The official PMLR title/byline/venue and18/33 study description match the intended source described in this key’s inherited coverage, but its corporate author/shortened title and10.5555 DOI were not independently resolved to that exact edition.

**Inspected scope:** Read complete substantive PMLR landing-page abstract and BibTeX/metadata, and compared with arXiv v2 abstract/byline/history. No full second study is counted.

**Locators:** Official PMLR landing page abstract/BibTeX; arXiv2402.04249 v2 metadata and history

**Visual check:** No figure pixels inspected; extracted table text and captions only.

**Findings:**

- PMLR gives the full title,12-author byline, ICML2024, volume235, pages35181–35224.
- Both canonical keys’ inherited support statements describe the same18-method/33-target study; no second independent HarmBench study was identified.

**Counterevidence / alternative:** Related editions and inaccurate metadata can coexist; do not equate the final PDF and arXiv v2 byte representations or silently delete a key.

**Limits:** The two records should be grouped as the same intended work family; source-identity metadata and DOI relation need explicit editorial correction before alias consolidation. Different retained PDF hashes do not establish different independent studies.

**Replication:** `not_performed`. **Numerical check:** No independent numerical recomputation or experiment reproduction.

**Relevance:** `duplicate_work_family`. **Claim links:** None; no claim support forced.

**Relevance rationale:** A bibliography-identity/family decision, not additional empirical corroboration.

**Next check:** Correct final-record metadata against PMLR, preserve both existing keys pending an alias/edition policy, and mark shared study lineage as confirmed at the named-study level. DOI-specific equivalence remains unverified.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://proceedings.mlr.press/v235/mazeika24a.html) |
| `final_url` | [Source](https://proceedings.mlr.press/v235/mazeika24a.html) |
| `retrieved_at` | 2026-11-14T17:14:58Z |
| `attempted_at` | 2026-11-14T17:14:58Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URLs are retained. Independent archival preservation is not claimed. |
| `sha256` | 89c4049946a16f9355d35b63a519ffe92bcb981f5126a1ffe32c024406bbeace |
| `byte_length` | 16291 |
| `mime_type` | text/html |
| `published_on` | 2024 |
| `version_claim` | Official ICML2024/PMLR235 proceedings landing and BibTeX |
| `locator_basis` | Retained HTML headings and named tables/sections; not a rendered browser view. |
| `capture_path` | .source-captures/synthesis-89c4049946a16f9355d35b63a519ffe92bcb981f5126a1ffe32c024406bbeace.html |

<a id="r2_safeguards_04"></a>
### r2_safeguards_04

**Source:** `bhatt_cyberseceval2wide_2024`. **Theme:** safeguards. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. The retained arXiv v1 matches the edition named in inherited coverage; its cover gives April18 and arXiv submission header April19,2024.

**Inspected scope:** Read abstract/introduction range claims; §§4.1.1–4.1.2,4.3.1–4.3.2,5.2,5.4 and6; visually inspected PDFpage12 Figure3 heatmap/bar plot and surrounding caption. Did not reread entire21pages or released results data.

**Locators:** Abstract/introduction; §§4.1,4.3,5.2,5.4,6; Figure3 printed/viewer p12

**Visual check:** Rendered and directly viewed PDFpage12 containing Figure3 and Figure2; no plot digitization or full-figure audit.

**Findings:**

- The prose reports incompatible prompt-injection summaries: abstract/introduction26–41%, §5.2 minimum17.1%, conclusion13–47%.
- The interpreter evaluation judges compliance with500 prompts acrossfive categories without executing outputs in an integrated interpreter; it is not a measured escape rate.
- The study positively operationalizes false refusal alongside malicious-request compliance, illustrating a safety/utility evaluation rather than one aggregate risk score.

**Counterevidence / alternative:** Figure3 visibly contains heterogeneous per-variant and per-model results; its lowest model bar appears near0.13 rather than supporting the §5.2 minimum. Without exact plotted data/aggregation, no replacement headline range is warranted.

**Limits:** No released-run reconstruction, exact bar-value extraction or weighting/denominator reconciliation. Figure3 is not a substitute for underlying results. Keep model-default safety/API and single-turn exclusions explicit.

**Replication:** `not_performed`. **Numerical check:** Documentary comparison of three printed ranges and visual inspection of Figure3 only; no alternative headline range computed.

**Relevance:** `claim_evidence`. **Claim links:** [C36](claims.md#c36)

**Relevance rationale:** Resolves the publication disposition (omit/qualify the affected number), while leaving source inconsistency unresolved.

**Next check:** Retain the qualitative, configured result and omit a single prompt-injection range until exact model/variant data and aggregation reconcile. The project need not wait for this number.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2404.13161v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2404.13161v1) |
| `retrieved_at` | 2026-11-14T17:14:58Z |
| `attempted_at` | 2026-11-14T17:14:58Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URLs are retained. Independent archival preservation is not claimed. |
| `sha256` | a3614ecb7e09cc850d97a083b8ecd98fd717b53b6795101b03691c5663d27633 |
| `byte_length` | 1578070 |
| `mime_type` | application/pdf |
| `published_on` | 2024-04-19 |
| `version_claim` | arXiv v1 |
| `locator_basis` | PDF viewer pages include cover; these papers print page numbers matching viewer pages. HTML locators use named sections and tables. |
| `capture_path` | .source-captures/synthesis-a3614ecb7e09cc850d97a083b8ecd98fd717b53b6795101b03691c5663d27633.pdf |

<a id="r2_safeguards_05"></a>
### r2_safeguards_05

**Source:** `hayes_inexactunlearningneeds_2024`. **Theme:** safeguards. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Canonical record identifies SaTML2025; obtained arXiv v3 May21,2024. Same title/byline does not authenticate final/preprint equivalence; final DOI route returned empty content. No canonical full-text upgrade.

**Inspected scope:** Read selected substantive passages from introduction; §§3.1–3.3 adversary/U-MIA distinction; §4 training/retain-privacy discussion; §5 PaLM2 design and results text onpp14–15; some §6 discussion. Appendices and complete37page text were not read.

**Locators:** arXiv v3 §§1,3.1–3.3,4.2–4.4,5; printed pp6–8,10–15

**Visual check:** No figure pixels inspected; extracted table text and captions only.

**Findings:**

- Per-example U-MIA can expose distinguishability left by inexact unlearning that population-aggregate tests miss.
- The vision study reports that some forget-example privacy improves while other forget and retained examples can worsen; privacy collateral effects are part of the evaluation target.
- PaLM2 experiments are fine-tuning on LIMA plus handcrafted100-example subsets; they do not measure erasure from a complete frontier pretraining corpus.

**Counterevidence / alternative:** Exact unlearning/retraining remains conceptually distinct; weak attacks failing does not prove privacy, but strong-audit access and small constructed fine-tuning sets also limit broad claims that every unlearning method fails.

**Limits:** Related preprint only; source scope is per-example versus population attackers, not user-level/privacy-group auditing. Shadow-model/training/data access assumptions make this an intentionally strong audit adversary, not a deployment attack-rate estimate. No figure values independently read or experiments reproduced.

**Replication:** `not_performed`. **Numerical check:** No independent numerical recomputation or experiment reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C35](claims.md#c35)

**Relevance rationale:** Adds the missing collateral-privacy/per-example argument to the unlearning strand, with final-version status kept open.

**Next check:** Correct inherited “user-level MIA” shorthand to per-example U-MIA. Preserve the final-version gap; inspect SaTML final and appendices before quantitative privacy conclusions.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2403.01218v3) |
| `final_url` | [Source](https://arxiv.org/pdf/2403.01218v3) |
| `retrieved_at` | 2026-11-14T17:16:06Z |
| `attempted_at` | 2026-11-14T17:16:06Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URLs are retained. Independent archival preservation is not claimed. |
| `sha256` | ab11e4823137b7fd03c08a341282cdd18304fbee51285444af98d0f786427dac |
| `byte_length` | 2743434 |
| `mime_type` | application/pdf |
| `published_on` | 2024-05-21 |
| `version_claim` | arXiv v3 |
| `locator_basis` | PDF viewer pages include cover; these papers print page numbers matching viewer pages. HTML locators use named sections and tables. |
| `capture_path` | .source-captures/synthesis-ab11e4823137b7fd03c08a341282cdd18304fbee51285444af98d0f786427dac.pdf |

<a id="r2_safeguards_06"></a>
### r2_safeguards_06

**Source:** `pavlova_automatedredteaming_2024`. **Theme:** safeguards. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. The canonical arXiv work and inherited full-text reading explicitly identify v1; this round only checked v1 selected methods/results.

**Inspected scope:** Read §4 dataset/scoring/success metric/attacker/target/budget/comparison setup and §5 main results text/captions. Did not reread full appendices or graph values.

**Locators:** arXiv v1 §§4–5; Figures2–3 captions; success metric ASR@k

**Visual check:** No figure pixels inspected; extracted table text and captions only.

**Findings:**

- GOAT uses100 JBB behaviors and JBB’s Llama3-70B judge; counts any unsafe message within a conversation and at least one success acrossk conversations.
- Its Crescendo reimplementation shares the helpful-only attacker andfive target-request conversation cap, providing a useful controlled method comparison.

**Counterevidence / alternative:** ASR@10 is cumulative over conversations/turns, not per-attempt or deployment harm. Shared JBB behavior/judge lineage prevents treating this as independent dataset corroboration.

**Limits:** Historical named models, helpful-only attacker and automatic judge; exact in-context definitions/conversations not independently reconstructed. No full new read and no experiments.

**Replication:** `not_performed`. **Numerical check:** No independent numerical recomputation or experiment reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C33](claims.md#c33)

**Relevance rationale:** Adds a concrete matched-comparator/multi-turn dimension and shared-data dependence to benchmark interpretation.

**Next check:** Add the source to C03 as a budget/aggregation example, or use it as background to C33. Retain the access model, judge, denominator and five-turn cap; do not pool ASR@1 andASR@10.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/html/2410.01606v1) |
| `final_url` | [Source](https://arxiv.org/html/2410.01606v1) |
| `retrieved_at` | 2026-11-14T17:15:00Z |
| `attempted_at` | 2026-11-14T17:15:00Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URLs are retained. Independent archival preservation is not claimed. |
| `sha256` | f7bcb3d08f8de91ce68165eb05b0d64d5639973ebfeb021926e23960af6ff32c |
| `byte_length` | 214540 |
| `mime_type` | text/html |
| `published_on` | Not recorded / unavailable |
| `version_claim` | arXiv v1 |
| `locator_basis` | Retained HTML headings and named tables/sections; not a rendered browser view. |
| `capture_path` | .source-captures/synthesis-f7bcb3d08f8de91ce68165eb05b0d64d5639973ebfeb021926e23960af6ff32c.html |

<a id="r2_safeguards_07"></a>
### r2_safeguards_07

**Source:** `qi_safetyalignmentshould_2025`. **Theme:** safeguards. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Read arXiv v1 June2024 already named in inherited coverage, while canonical unversioned record/date and prior review also reference ICLR2025. Fresh final PDF access returned403; no version equivalence or full new read claimed.

**Inspected scope:** Read §3.1 utility comparison and §3.2/Table2 augmentation results plus selected AppendixA.4 aggregation details and AppendixC biased-constraint/combined-method discussion. Did not rederive Eq27 or read complete proof/main text.

**Locators:** arXiv v1 §§3.1–3.2, Table2; AppendixA.4; AppendixC Tables4–6 discussion

**Visual check:** No figure pixels inspected; extracted table text and captions only.

**Findings:**

- Recovery-data augmentation reduces reported40-token-prefill ASR from57.0% to4.5% on the tested setup; AlpacaEval win rate changes from51.8% to49.5% with the safety system prompt held.
- Augmentation and early-token-constrained subsequent fine-tuning are distinct interventions; AppendixC says combining them was not consistently better and large uniform constraints can collapse utility.

**Counterevidence / alternative:** Positive defense gains do not establish all-budget robustness or zero utility cost. Table2/AppendixA.4 GCG reporting uses thethree most successful runs out often, so mean-rate summaries require aggregation context.

**Limits:** Tested Llama2-7B conditions; automated judge/HEx-PHI endpoint, not harm. ICLR final access blocked. The theory equation-direction lead was not checked and remains outside this scoped finding.

**Replication:** `not_performed`. **Numerical check:** No independent numerical recomputation or experiment reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C34](claims.md#c34)

**Relevance rationale:** Adds constructive defense-design evidence and directly conditions claims about utility and general robustness.

**Next check:** Keep affirmative mitigation results and explicit utility/aggregation limits. Exclude the unverified Eq27 lead from numerical publication until checked; reconcile exact final edition independently.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/html/2406.05946v1) |
| `final_url` | [Source](https://arxiv.org/html/2406.05946v1) |
| `retrieved_at` | 2026-11-14T17:16:08Z |
| `attempted_at` | 2026-11-14T17:16:08Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URLs are retained. Independent archival preservation is not claimed. |
| `sha256` | db6d97e430b427d611293f6d20faca186845df877c20ecdedc6bd1c99113f3e8 |
| `byte_length` | 530011 |
| `mime_type` | text/html |
| `published_on` | Not recorded / unavailable |
| `version_claim` | arXiv v1 |
| `locator_basis` | Retained HTML headings and named tables/sections; not a rendered browser view. |
| `capture_path` | .source-captures/synthesis-db6d97e430b427d611293f6d20faca186845df877c20ecdedc6bd1c99113f3e8.html |

<a id="r2_safeguards_08"></a>
### r2_safeguards_08

**Source:** `hayes_inexactunlearningneeds_2024`. **Theme:** safeguards. **Reading:** Inaccessible. **Coverage effect:** `none`.

**Edition match:** `uncertain`. The DOI is an existing coverage lead, not fresh verified proceedings metadata.

**Inspected scope:** Attempted DOI-to-IEEE retrieval; received an empty HTML response, so no final-version source text was read.

**Locators:** DOI10.1109/SaTML64287.2025.00034 redirect to IEEE10992375

**Visual check:** None; no source content obtained.

**Findings:**

No source findings; material was inaccessible.

**Counterevidence / alternative:** The related preprint is useful but does not close this final-version gap.

**Limits:** Empty publisher response, not an authenticated final paper.

**Replication:** `not_performed`. **Numerical check:** No independent numerical recomputation or experiment reproduction.

**Relevance:** `unresolved`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Explicit access limitation for consequential final-version check.

**Next check:** Keep final/preprint equivalence unresolved and do not upgrade canonical final reading depth.

| Capture field | Value |
|---|---|
| `preservation_status` | unavailable |
| `original_url` | [Source](https://doi.org/10.1109/SaTML64287.2025.00034) |
| `final_url` | [Source](https://ieeexplore.ieee.org/document/10992375/) |
| `retrieved_at` | Not recorded / unavailable |
| `attempted_at` | 2026-11-14T17:16:08Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No source content was obtained: ModuleNotFoundError: No module named 'bs4' |
| `sha256` | Not recorded / unavailable |
| `byte_length` | Not recorded / unavailable |
| `mime_type` | Not recorded / unavailable |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Not recorded / unavailable |
| `locator_basis` | Retained HTML headings and named tables/sections; not a rendered browser view. |
| `capture_path` | Not recorded / unavailable |

<a id="r2_safeguards_09"></a>
### r2_safeguards_09

**Source:** `qi_safetyalignmentshould_2025`. **Theme:** safeguards. **Reading:** Inaccessible. **Coverage effect:** `none`.

**Edition match:** `related_edition`. The supplied ICLR final URL was attempted directly.

**Inspected scope:** Attempted publisher final-PDF retrieval; HTTP403, no source bytes read.

**Locators:** OpenReview final paper id6Mxhg9PtDE

**Visual check:** None; no source content obtained.

**Findings:**

No source findings; material was inaccessible.

**Counterevidence / alternative:** Prior final-version checks are inherited; this round does not independently authenticate them.

**Limits:** HTTP403 on final PDF; arXiv v1 findings remain version-limited.

**Replication:** `not_performed`. **Numerical check:** No independent numerical recomputation or experiment reproduction.

**Relevance:** `unresolved`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Explicit final-version access limit; not evidence of missing paper or changed result.

**Next check:** Retain version-qualified preprint findings and seek lawful final access in a future claim-critical round.

| Capture field | Value |
|---|---|
| `preservation_status` | unavailable |
| `original_url` | [Source](https://openreview.net/pdf?id=6Mxhg9PtDE) |
| `final_url` | [Source](https://openreview.net/pdf?id=6Mxhg9PtDE) |
| `retrieved_at` | Not recorded / unavailable |
| `attempted_at` | 2026-11-14T17:14:59Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No source content was obtained: HTTPError: HTTP Error 403: Forbidden |
| `sha256` | Not recorded / unavailable |
| `byte_length` | Not recorded / unavailable |
| `mime_type` | Not recorded / unavailable |
| `published_on` | Not recorded / unavailable |
| `version_claim` | ICLR2025 final URL |
| `locator_basis` | Retained HTML headings and named tables/sections; not a rendered browser view. |
| `capture_path` | Not recorded / unavailable |

<a id="r2_institutions_01"></a>
### r2_institutions_01

**Source:** `charnock_expandingexternalaccess_2026`. **Theme:** audit_institutions. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Title/authors/arXiv identifier match the canonical preprint. The arXiv history exposed only v1; source cover dates January 21 while arXiv records submission January 17. These are recorded distinctly rather than treated as a chronology error.

**Inspected scope:** All accessible text of the 20-page arXiv v1 PDF: introduction, §§2–5, Tables 1–5 and references. This is a text reading of the identified PDF, not an audit of cited primary studies or current Code obligations.

**Locators:** §§2.1–2.2 benefits and challenges; §§3.1–3.4 model access, model information, timeframe and interdependencies; Tables 1–2; §§4.1–4.3 and Tables 3–5 proposed access levels; §5 Conclusion (including limitations)

**Visual check:** Tables 1–5 were read in extracted text; no rendered figure/table visual verification.

**Findings:**

- Model access, model information and evaluator time enable different techniques and are interdependent; deeper access is not a substitute for enough time or context.
- The authors include reducing false positives, contextualizing findings and enabling reproducibility among access benefits, alongside detecting missed dangerous capabilities.
- AL1–AL3 are the authors’ proposed descriptive categories and interpretation of Code expectations, not validated quality scores or Commission-endorsed legal thresholds.
- Expanded access has security and capacity costs; the paper discusses structured APIs, on-site controls, confidentiality and liaison support rather than assuming unconstrained disclosure.

**Counterevidence / alternative:** Public information may understate existing private access. More access can add security burdens; risk and evaluation purpose can justify different levels across dimensions and releases. Casper is a coauthor here and in the 2024 access paper; these are not independent experimental confirmations.

**Limits:** No empirical comparison of the proposed levels; authors rely on public information about evaluator arrangements. No private contracts or current Code chapter was audited. Exact arXiv submission and document-cover dates differ.

**Replication:** `not_performed`. **Numerical check:** No experimental result or causal effect estimate was replicated. No numerical claim from the cross-industry secondary literature is adopted as a freshly verified estimate.

**Relevance:** `claim_evidence`. **Claim links:** [C38](claims.md#c38)

**Relevance rationale:** Supplies an affirmative institutional or access mechanism and its limits; inclusion is not independent corroboration of an effectiveness claim.

**Next check:** Check the access method, information supplied, evaluation time and restrictions for each applied case; test the proposed taxonomy against actual agreements before claiming implementation.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2601.11916v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2601.11916v1) |
| `retrieved_at` | 2026-11-14T17:15:17.943921+00:00 |
| `attempted_at` | 2026-11-14T17:15:17.943921+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 155a1033844ed3f00d7b3737de5c48751590920ef3b3d75781c161e1f7039d55 |
| `byte_length` | 321326 |
| `mime_type` | application/pdf |
| `published_on` | 2026-01-17 |
| `version_claim` | arXiv:2601.11916v1; arXiv submission January 17, 2026, document cover January 21, 2026 |
| `locator_basis` | PDF viewer pages count the cover; section/table labels are stable locators. |
| `capture_path` | .source-captures/synthesis-155a1033844ed3f00d7b3737de5c48751590920ef3b3d75781c161e1f7039d55.pdf |

<a id="r2_institutions_02"></a>
### r2_institutions_02

**Source:** `casper_blackboxaccessaudits_2024`. **Theme:** audit_institutions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. The canonical record is the ACM FAccT 2024 publication, pp2254–2272, DOI10.1145/3630106.3659037. This arXiv v3 carries that venue/DOI and matching title/authors, but byte/text equivalence to the publisher edition was not established; do not upgrade canonical full-text coverage.

**Inspected scope:** Selected arXiv v3: §2.1 and Table 1 access definitions; portions of §§3–4.1 reviewing access-enabled testing; §§5–7 on outside-the-box information, security and discussion; Appendix D in full. Not the complete paper or all technical appendices/references.

**Locators:** §2.1 and Table 1 access definitions; §5 outside-the-box access; §6 security considerations; §7 discussion; Appendix D Beyond Access: Other Aspects of Rigorous Audits

**Visual check:** Extracted table text only; no rendered figures or plots inspected.

**Findings:**

- Model/data/process information can help diagnose failures and design complementary tests; technical access widens the set of feasible audit techniques.
- The paper explicitly states white- and outside-the-box access is necessary but insufficient; Appendix D identifies resources, technical tooling, scope, conflicts, representation and regulatory capture as additional conditions.
- Secure interfaces can offer some white-box computations without distributing weights, but API exposure can still carry reconstruction and misuse risks.

**Counterevidence / alternative:** Black-box and human attack methods can remain useful and sometimes competitive; access alone does not order audit quality. Shared authorship and cited-study reuse mean these arguments cannot be counted as independent empirical corroboration.

**Limits:** The paper reviews technical studies; their experiments, appendices and quoted performance numbers were not independently reproduced. ACM-final equivalence remains unresolved.

**Replication:** `not_performed`. **Numerical check:** No experimental result or causal effect estimate was replicated. No numerical claim from the cross-industry secondary literature is adopted as a freshly verified estimate.

**Relevance:** `claim_evidence`. **Claim links:** [C38](claims.md#c38), [C39](claims.md#c39)

**Relevance rationale:** Supplies an affirmative institutional or access mechanism and its limits; inclusion is not independent corroboration of an effectiveness claim.

**Next check:** Compare the exact ACM edition with arXiv v3 before treating this reading as canonical full text; inspect primary technical studies if an access-related performance number becomes publication-leading.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2401.14446v3) |
| `final_url` | [Source](https://arxiv.org/pdf/2401.14446v3) |
| `retrieved_at` | 2026-11-14T17:15:17.942655+00:00 |
| `attempted_at` | 2026-11-14T17:15:17.942655+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 7143e9ce2dc24a0cea3742e969a83fdce20dee3ff4ef707d7608a7b3af9d277b |
| `byte_length` | 948088 |
| `mime_type` | application/pdf |
| `published_on` | 2024 |
| `version_claim` | arXiv:2401.14446v3; source carries FAccT2024 publication metadata |
| `locator_basis` | PDF viewer pages1–19; stable section and appendix labels used, rather than extraction line numbers. |
| `capture_path` | .source-captures/synthesis-7143e9ce2dc24a0cea3742e969a83fdce20dee3ff4ef707d7608a7b3af9d277b.pdf |

<a id="r2_institutions_03"></a>
### r2_institutions_03

**Source:** `raji_outsideroversight_2022`. **Theme:** audit_institutions. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Author-hosted published-format AIES2022 article matches canonical title/authors, DOI10.1145/3514094.3534181 and printed pages557–571. Identity is based on publication metadata, not byte comparison with ACM.

**Inspected scope:** All accessible text of the 15-page published-format PDF, printed pp557–571: §§1–6, references, Appendix Tables1–2, plus visual inspection of the main audit matrix and the disputed appendix rows.

**Locators:** §2.1 audit categories and §2.2 internal-audit limitations; §3 five institutional design dimensions; §§4.1–4.5 evidence base and AI implications; §4.5.2 restricted transparency and audit registry; §5 limitations and internal/external complementarity; Figure1, printedp561/PDFp5 (called Table1 in adjacent prose); Appendix Table2, printedp571/PDFp15, FDA FAERS and FCC TCB rows

**Visual check:** Rendered PDFp5/printedp561 main Figure1 matrix and PDFp15/printedp571 Appendix Table2 inspected. The FDA FAERS and FCC TCB row-description mismatch is visible in the rendered PDF; it is not only a text-extraction artifact.

**Findings:**

- Audit labels conceal consequential differences in selection/payment, access/legal protection, scope, professional standards and follow-up. A paid nominal third-party arrangement can reproduce the incentives and limits of an internal audit.
- The source proposes registered audit reports with public or vetted summaries and fuller regulator access as a potentially useful restricted transparency regime; it does not demand that every audit detail be public.
- The authors explicitly retain the value of internal audits and argue against relying on them alone; §5 also notes interactions, such as access mattering only when independence is adequate.
- Appendix Table2 visibly assigns the telecommunications description to the FDA FAERS row and the drug/adverse-event description to FCC TCB. Omit these example descriptions pending program-level verification; this local defect does not by itself resolve the separate institutional argument.

**Counterevidence / alternative:** Licensing and rotation evidence is mixed; familiarity/expertise can trade off against independence. Disclosure can be costly, inflate grades or divert attention, so more public information is not a demonstrated monotonic improvement. The article does not choose an enacted legislative versus regulatory implementation path.

**Limits:** The evidence survey is selective and drawn substantially from other sectors. Underlying cross-industry effect estimates were not independently checked. Appendix Table2 appears to interchange the FDA FAERS and FCC TCB descriptions; those example rows are not relied on as correct program descriptions.

**Replication:** `not_performed`. **Numerical check:** No experimental result or causal effect estimate was replicated. No numerical claim from the cross-industry secondary literature is adopted as a freshly verified estimate.

**Relevance:** `claim_evidence`. **Claim links:** [C39](claims.md#c39), [C41](claims.md#c41)

**Relevance rationale:** Supplies an affirmative institutional or access mechanism and its limits; inclusion is not independent corroboration of an effectiveness claim.

**Next check:** Retain the conditional institutional argument, omit the two affected Appendix Table2 examples, and verify FDA/FCC primary program descriptions before reusing them. Check applied audit funding, selection, access, follow-up and disclosure terms separately.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://dho.stanford.edu/wp-content/uploads/Outsider_Oversight.pdf) |
| `final_url` | [Source](https://dho.stanford.edu/wp-content/uploads/Outsider_Oversight.pdf) |
| `retrieved_at` | 2026-11-14T17:14:54.329250+00:00 |
| `attempted_at` | 2026-11-14T17:14:54.329250+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 88d9248ee040cb6c1e194ca7d325768d79fc1cd81518b696a4c767f9d6f12036 |
| `byte_length` | 1262015 |
| `mime_type` | application/pdf |
| `published_on` | 2022 |
| `version_claim` | Published-format AIES2022 author-hosted copy, DOI10.1145/3514094.3534181 |
| `locator_basis` | PDF viewerp1 corresponds to printedp557; printedp571 is PDFp15. Appendix labels distinguish its Table1 from main Figure1. |
| `capture_path` | .source-captures/synthesis-88d9248ee040cb6c1e194ca7d325768d79fc1cd81518b696a4c767f9d6f12036.pdf |

<a id="r2_institutions_04"></a>
### r2_institutions_04

**Source:** `longpre_safeharbor_2024`. **Theme:** audit_institutions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. The canonical PMLR235 proceedings landing page directly links this mlresearch-hosted PDF, with matching title/authors and 20-page proceedings span. HTTP MIME was application/octet-stream; PDF signature and successful PDF extraction confirm PDF content.

**Inspected scope:** PMLR published PDF pp1–4 (abstract, introduction, definitions/Table1 and researcher-experience discussion/Table2), the sampling-qualification paragraph at the beginning of p5, plus §4, §§4.1–4.2 and Figure1 text on PDFpp6–9. Remaining company-policy text/Table3 and later sections/appendices were not read in full.

**Locators:** Table1 definitions; Table2 informal researcher discussions and sampling limits; §4 and Figure1 proposed mutual commitments, PDFpp6–7; §4.1 civil versus criminal limitations, PDFpp7–8; §4.2 independent pre-review and transparent appeals, PDFpp8–9

**Visual check:** Figure1 text was readable in extraction and inspected there; no rendered visual check.

**Findings:**

- Legal assurance against company reprisal and technical assurance against account suspension solve distinct barriers; a legal promise alone does not provide technical access.
- The proposed protections are conditional on good faith, agreed vulnerability-disclosure rules, privacy protection and avoiding harm; they are not a blanket exemption from law or all platform rules.
- Suggested implementation paths include trusted third-party access review and independently reviewed appeals. These mechanisms could widen participation but remain proposals rather than measured implementation effects.
- The source distinguishes company protection against civil claims from criminal liability; its proposals are framed in a US legal context.

**Counterevidence / alternative:** Delegated access can still exclude critical or unaffiliated researchers if companies select only a narrow partner network. Earlier/deeper/subsidized access, information and stable model versions remain separate constraints. No assurance that these mechanisms improve safety has been measured here.

**Limits:** Not a full-text reading. Historical 2024 company terms and legal assertions are not recertified as current law or current access practice. No adopted safe-harbor outcome study or current legal authority was checked. The survey themes come from informal discussions with an imperfect, selected group, not a representative prevalence estimate.

**Replication:** `not_performed`. **Numerical check:** No experimental result or causal effect estimate was replicated. No numerical claim from the cross-industry secondary literature is adopted as a freshly verified estimate.

**Relevance:** `claim_evidence`. **Claim links:** [C40](claims.md#c40)

**Relevance rationale:** Supplies an affirmative institutional or access mechanism and its limits; inclusion is not independent corroboration of an effectiveness claim.

**Next check:** Read AppendicesA–C and review current jurisdiction-specific law before a legal conclusion. Treat 2024 company-policy coding as historical and verify present operative policies separately.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/longpre24a/longpre24a.pdf) |
| `final_url` | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/longpre24a/longpre24a.pdf) |
| `retrieved_at` | 2026-11-14T17:15:17.944392+00:00 |
| `attempted_at` | 2026-11-14T17:15:17.944392+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 3f7993c7bf810e025596ea8598ec0c487062939726f5db05a9c1eab6b78f304a |
| `byte_length` | 311993 |
| `mime_type` | application/pdf |
| `published_on` | 2024 |
| `version_claim` | PMLR235/ICML2024 published position paper; exact linked PDF |
| `locator_basis` | PDF internal pages1–20; PDFp6 begins §4 and PDFp7 contains Figure1. |
| `capture_path` | .source-captures/synthesis-3f7993c7bf810e025596ea8598ec0c487062939726f5db05a9c1eab6b78f304a.pdf |

<a id="r2_institutions_05"></a>
### r2_institutions_05

**Source:** `raji_closingaccountabilitygap_2020`. **Theme:** audit_institutions. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. The canonical record is arXiv:2001.00973 and the only listed version is v1. The exact v1 matches title/authors and January3,2020 submission date. PDF also carries FAT*2020 venue and ACM DOI10.1145/3351095.3372873; publisher-final equivalence was not needed for this canonical arXiv record.

**Inspected scope:** All accessible text of the 12-page arXiv v1 PDF: §§1–6, references and both hypothetical CompanyX examples. Figures1–2 were also rendered and visually inspected. Linked supplementary worked templates were not retrieved/read.

**Locators:** §2.4 internal audits and pre-deployment access; §4 SMACTR framework and hypothetical CompanyX examples; §§4.1–4.6 proposed stages, reflection and post-audit decisions; Figure1 PDFp2 and Figure2 PDFp6; §5 Limitations of Internal Audits

**Visual check:** Rendered Figure1/PDFp2 and Figure2/PDFp6 inspected, including development-stage intervention and post-audit go/no-go, mitigation and implementation tracking.

**Findings:**

- Internal access to intermediate models, data and development processes can support prospective testing and traceable artifacts before deployment, rather than leaving external reviewers to reconstruct harms afterward.
- SMACTR proposes scoping, mapping, artifact collection, testing and reflection, tied to risk analysis, remediation, design history and summary reporting. Post-audit action may include redesign, delay or cancellation.
- Documentation is a proposed decision and accountability process, not merely a public disclosure artifact. Such artifacts can also assist subsequent external scrutiny.
- The source acknowledges internal auditors’ organizational interests and presents internal auditing as one part of wider checks and balances.

**Counterevidence / alternative:** A complete-looking audit file can reflect organizational priorities and omit affected stakeholders. The paper assumes the decision to conduct an audit has already been made and does not establish which systems must be selected. Hypothetical cases demonstrate structure, not adoption or harm reduction.

**Limits:** The two CompanyX examples are explicitly hypothetical. Author affiliation does not establish observed deployment at that organization. Linked supplementary templates are outside this reading. Analogies to aviation/healthcare and secondary quantitative claims were not transported into AI effect estimates.

**Replication:** `not_performed`. **Numerical check:** No experimental result or causal effect estimate was replicated. No numerical claim from the cross-industry secondary literature is adopted as a freshly verified estimate.

**Relevance:** `claim_evidence`. **Claim links:** [C41](claims.md#c41)

**Relevance rationale:** Supplies an affirmative institutional or access mechanism and its limits; inclusion is not independent corroboration of an effectiveness claim.

**Next check:** For a publication-leading implementation claim, inspect an actual audit record with decision owners, affected-stakeholder input, remediation completion and external challenge. Linked templates may illustrate workflow but cannot establish observed effectiveness.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2001.00973v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2001.00973v1) |
| `retrieved_at` | 2026-11-14T17:15:17.943351+00:00 |
| `attempted_at` | 2026-11-14T17:15:17.943351+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | dd509e76cc4698d50bae2eb450d74e2506a6c5e12c33838df77850a4a1ba4824 |
| `byte_length` | 621854 |
| `mime_type` | application/pdf |
| `published_on` | 2020-01-03 |
| `version_claim` | arXiv:2001.00973v1, submitted January3,2020; source carries FAT*2020 publication metadata |
| `locator_basis` | PDF viewer pages1–12; figures on viewerpages2and6. Section labels used for extracted text. |
| `capture_path` | .source-captures/synthesis-dd509e76cc4698d50bae2eb450d74e2506a6c5e12c33838df77850a4a1ba4824.pdf |

<a id="r2_sociotechnical_01"></a>
### r2_sociotechnical_01

**Source:** `gebru_datasheets_2021`. **Theme:** sociotechnical. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. The canonical record uses arXiv1803.09010 DOI/eprint/URL. Source history identifies v8 submitted2021-12-01; PDF cover agrees and matches the record publication month. This is full reading of that arXiv object, not a claim of byte/layout equivalence with the7-page CACM publication.

**Inspected scope:** All18 pages of arXivv8 accessible extracted text read in three complete six-page blocks: introduction/objectives, development process, all questions/workflow, impact/challenges, acknowledgments/references, AppendixA and all four text-based example datasheet figures. External cited datasets/links were not opened.

**Locators:** §1.1 pp2–3; §2 pp3–4; §3.2 pp5–6 representativeness and archival questions; §3.5 pp8–9 intended/nonrecommended uses; §3.7 pp9–10 maintenance; §4 pp10–11 implementation reports and limits; AppendixA/Figures1–4 pp14–18

**Visual check:** No separate rendered-page visual inspection. Text and table/caption extraction were read; graphical coordinates, image-only contents and layout equivalence are not certified.

**Findings:**

- The framework asks dataset creators to articulate sampling, validated representativeness, collection procedures, intended and discouraged uses, external dependencies, rights, and maintenance. This supplies an actionable disclosure workflow rather than a generic transparency slogan.
- The development process used example datasheets and feedback with product teams; questions were revised to discourage yes/no answers and integrate legal/ethical issues into lifecycle stages.
- The authors explicitly say datasheet creation is not intended to be automated because careful creator reflection is a central objective; they recommend recording unknowns rather than omitting documentation.
- The paper reports adoption/pilots and identifies overhead, organizational incentives, dynamic-dataset maintenance and inability to anticipate every use as implementation limits.

**Counterevidence / alternative:** Documentation can improve communication and appropriate dataset selection without proving representative data or outcome improvement. The proposal itself challenges treating automatically populated metadata as equivalent to creator reflection.

**Limits:** Published CACM equivalence not authenticated. Reported organizational pilots are author reports, not independently verified adoption or causal evidence of harm reduction. Examples disclose unknowns; full text does not include all linked datasets or web resources.

**Replication:** `not_performed`. **Numerical check:** No experimental replication or numerical recomputation; documentary quantities checked only where stated.

**Relevance:** `claim_evidence`. **Claim links:** [C44](claims.md#c44)

**Relevance rationale:** Adds the missing data-provenance and reflective-process mechanism to the governance/synthesis strand; neither a statutory rule nor an empirical efficacy estimate.

**Next check:** Use the existing record as a methodological/governance contribution. If citing the journal layout, inspect/pin CACM DOI10.1145/3458723 separately; do not infer full publication equivalence from matching title.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/1803.09010v8) |
| `final_url` | [Source](https://arxiv.org/pdf/1803.09010v8) |
| `retrieved_at` | 2026-11-14T17:15:38.971315Z |
| `attempted_at` | 2026-11-14T17:15:38.971315Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | c7f595988ee2c109631d5173fdae37ff1774c68ec17add51bd012f2a6e8792d0 |
| `byte_length` | 554802 |
| `mime_type` | application/pdf |
| `published_on` | 2021-12-01 |
| `version_claim` | arXiv1803.09010v8 |
| `locator_basis` | One-based PDF viewer pages count cover; the printed page numbers coincide for Datasheets, Agents, HELM and main DecodingTrust. ARIA printed page1 begins PDF viewer8. HTML locators use named abstract/metadata headings. |
| `capture_path` | .source-captures/synthesis-c7f595988ee2c109631d5173fdae37ff1774c68ec17add51bd012f2a6e8792d0.pdf |

<a id="r2_sociotechnical_02"></a>
### r2_sociotechnical_02

**Source:** `kapoor_aiagentsmatter_2024`. **Theme:** sociotechnical. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. The canonical record identifies arXiv2407.01502, submitted2024-07-01. The only listed version is v1; the PDF has a July2 cover date, preserved as a distinct source date.

**Inspected scope:** Complete main text §§1–7, PDF pp1–11; complete AppendixA–B text/tables/captions pp18–26 plus AppendixC/D opening/selection and NovelQA setup onp26. References pp12–17 and remaining AppendicesC–I/NeurIPS checklist pp27–33 were not read completely; image-only plot values were not digitized.

**Locators:** §§2.2–2.3 pp3–4; Figure1; TableA1 p20; §§3.1–3.2 p5; AppendixB pp22–26; TableA3 p23; §4–§4.1 pp6–7; §5/Table1 pp8–10; §6 pp10–11

**Visual check:** No separate rendered-page visual inspection. Text and table/caption extraction were read; graphical coordinates, image-only contents and layout equivalence are not certified.

**Findings:**

- On modified HumanEval with example tests for all164 problems, simple retry/warming baselines match or improve the cost–accuracy frontier relative to selected complex architectures. Claims that planning/reflection caused the gains require stronger controls.
- HotPotQA joint optimization searches prompt/example/temperature choices using100 optimization samples and200 evaluation samples; it reports lower variable cost with similar retrieval accuracy, demonstrating constructive benchmark-guided design.
- The paper distinguishes scientific model comparison from downstream procurement: dated dollar costs matter for the latter and token counts allow repricing. Appropriate holdouts depend on the generality claimed.
- The authors argue human-in-the-loop performance may be underestimated by autonomous-only evaluations; this is a missing-use-context argument supported partly through cited external studies, not a new direct human-feedback experiment in this paper.

**Counterevidence / alternative:** Some complex techniques may help on harder tasks such as SWE-bench. The paper does not show that planning/reflection never help; its simple-baseline and cost results are task/model/version-specific. Joint optimization is positive evidence that better evaluation can lead to more useful designs.

**Limits:** Selected33-page preprint, not a full read. Experiments are the authors' own reproduced/re-evaluated runs in historical2024 model/pricing conditions; this review ran no agents. Five-run confidence intervals omit optimization/resampling variability, as FigureA5 notes. Holdout appropriateness counts include stated intentions, not only existing holdouts. NovelQA comparison was one run and its sequential-cost extrapolation is modeled.

**Replication:** `not_performed`. **Numerical check:** No experimental replication or numerical recomputation; documentary quantities checked only where stated.

**Relevance:** `claim_evidence`. **Claim links:** [C43](claims.md#c43)

**Relevance rationale:** Adds cost-controlled constructive comparison and separate model/deployment decision needs; challenges both inflated leaderboard claims and a blanket view that benchmark evidence has no practical design value.

**Next check:** Retain qualified cost/holdout conclusions and a dated benchmark method role. Complete remaining appendices and inspect raw run data before quoting broad rankings or inferred efficiency gains.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2407.01502v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2407.01502v1) |
| `retrieved_at` | 2026-11-14T17:15:38.972039Z |
| `attempted_at` | 2026-11-14T17:15:38.972039Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 1681013e0421f9d193ca5bb556b566f50d1e5eaa43d7a9700a31ca3dd0e2ff7a |
| `byte_length` | 1235369 |
| `mime_type` | application/pdf |
| `published_on` | 2024-07-01 |
| `version_claim` | arXiv2407.01502v1; cover July2,2024 |
| `locator_basis` | One-based PDF viewer pages count cover; the printed page numbers coincide for Datasheets, Agents, HELM and main DecodingTrust. ARIA printed page1 begins PDF viewer8. HTML locators use named abstract/metadata headings. |
| `capture_path` | .source-captures/synthesis-1681013e0421f9d193ca5bb556b566f50d1e5eaa43d7a9700a31ca3dd0e2ff7a.pdf |

<a id="r2_sociotechnical_03"></a>
### r2_sociotechnical_03

**Source:** `amironesei_aria_pilot_2025`. **Theme:** sociotechnical. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Official NIST AI700-2 publisher PDF, November2025 cover and matching title/report identity. Canonical record specifies publication2025-11-13/update11-14; no separate version replacement is inferred.

**Inspected scope:** Abstract/TOC PDF pp4–5; main text §§1–7 PDF pp8–21 (printed1–14), including testing, annotation, crosswalk, CoRIx topology, example interpretations and future work; AppendixC PDFp29/printed22. Other appendices and rendered tree graphics not completely reviewed.

**Locators:** §2 printedpp2–4 / viewer9–11; §3 adjudication printedp6 / viewer13; §4 printedpp7–8 / viewer14–15; §5.2 printedpp10–13 / viewer17–20; Table1 printedpp9–10; AppendixC Tables5–7 printedp22 / viewer29

**Visual check:** No separate rendered-page visual inspection. Text and table/caption extraction were read; graphical coordinates, image-only contents and layout equivalence are not certified.

**Findings:**

- ARIA combines model testing, adversarial red teaming and scenario-based human field testing, with dialogue annotations and tester questionnaires mapped to a validity construct. This is a concrete implemented measurement procedure beyond isolated model benchmarks.
- Example applications have different testing levels contributing the largest validity-risk signal. Field tester perceptions can miss violations observed in annotations; model tests may also elicit problems not prominent in ordinary interactions.
- CoRIx trees make aggregation and the source of risk indicators inspectable. The report explicitly says cross-application/scenario tree comparisons are not meaningful and the initial instrument is better suited to characterization than comparison.
- The manuscript contains a numerical reconciliation lead: main adjudication text says267 dialogues and52 risk violations; AppendixC Table7 gives49Yes+218No (=267). Do not convert Table6's964 annotation judgments into independent-dialogue rates.

**Counterevidence / alternative:** The field-style method is affirmative feasibility evidence, but may still underestimate or overestimate real-world validity because instruction/scenario framing and respondent judgments matter. It is not an estimated effect on harms or an externally validated general safety scale.

**Limits:** Exploratory seven-application pilot with51 red teamers and19 field testers under English scenarios, not representative deployment outcomes. Proxy scenarios differ from severe harms; not every application was tested at every level. Questionnaires and annotations are not directly comparable, and scores are characterized as better for describing than ranking applications. Uncertainty propagation and questionnaire validation remain future work.

**Replication:** `not_performed`. **Numerical check:** Documentary arithmetic only: AppendixC Table7 gives49+218=267. Table6 totals185+445+111+223=964 risk-assessment annotations; comparison with mainp6 count52 is unresolved, not an experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C45](claims.md#c45)

**Relevance rationale:** Adds implemented human/system-context testing and transparent aggregation while narrowing claims about objective impacts and cross-system comparisons.

**Next check:** Omit disputed violation counts/rates from synthesis pending NIST clarification or authenticated revision. Keep the qualitative layered-testing result; inspect full measurement/appendix methods if publishing a CoRIx-based numerical comparison.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-2.pdf) |
| `final_url` | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-2.pdf) |
| `retrieved_at` | 2026-11-14T17:14:59.250326Z |
| `attempted_at` | 2026-11-14T17:14:59.250326Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 5478e8c37a182adaf9449d1d315689beba3db2808db430c54fe3fc8da04ea3b9 |
| `byte_length` | 8040325 |
| `mime_type` | application/pdf |
| `published_on` | 2025-11 |
| `version_claim` | NIST AI700-2, November2025 |
| `locator_basis` | One-based PDF viewer pages count cover; the printed page numbers coincide for Datasheets, Agents, HELM and main DecodingTrust. ARIA printed page1 begins PDF viewer8. HTML locators use named abstract/metadata headings. |
| `capture_path` | .source-captures/synthesis-5478e8c37a182adaf9449d1d315689beba3db2808db430c54fe3fc8da04ea3b9.pdf |

<a id="r2_sociotechnical_04"></a>
### r2_sociotechnical_04

**Source:** `liang_helm_2023`. **Theme:** sociotechnical. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Canonical arXiv2211.09110 record and prior ledger explicitly identify v2/TMLR cover. Captured PDF states arXivv2 October1,2023 and TMLR publication08/2023. No assertion of identity with later live HELM releases.

**Inspected scope:** Title/abstract and §1 overview; selected §1.2 top-level findings pp7–10; selected scenario and metric-method text pp23–32, especially §4.1–4.2 Tables2–4 and §4.6–4.8; missing-scenario/metric/model/adaptation discussion §10.1–10.5 pp78–80. Not a complete162-page read; full appendices, results figures and live raw outputs not audited.

**Locators:** §1 pp1–2; §1.2 selected findings pp7–10; §4.1–4.2/Tables2–4 pp25–27; §4.6–4.8 pp30–32; §10.1–10.5 pp78–80

**Visual check:** No separate rendered-page visual inspection. Text and table/caption extraction were read; graphical coordinates, image-only contents and layout equivalence are not certified.

**Findings:**

- HELM explicitly treats broad coverage, recognition of incompleteness, multiple metrics and standardized adaptation as complementary goals.
- Its design measures98 of112 selected scenario–desideratum pairs (16core scenarios ×7 top-level metrics); some omissions are not well-defined and others are deliberately avoided over validity concerns.
- Standardized common evaluation exposes tradeoffs and disparities that average accuracy alone misses; the framework also distinguishes fairness as task-performance disparities from bias in generated language.
- The paper explicitly excludes or incompletely addresses properties requiring broader-system or social-context knowledge; English coverage, contextualized toxicity, user experience and undisclosed-model access remain gaps.

**Counterevidence / alternative:** The evaluated subspace is selected for feasible access and scalable measurement, so breadth does not imply a deployment safety measure. Nevertheless the framework provides reproducible common comparisons and design-relevant information rather than only a list of caveats.

**Limits:** Historical30-model comparison. Metric coverage and known omissions are part of the result. Fairness perturbations may miss complex distribution differences; demographic group labels are missing for many scenarios; bias/toxicity proxies have acknowledged validity limits. No underlying prediction matrix or live leaderboard was reproduced. Some PDF diagram text/URLs extract poorly; no graph-coordinate verification.

**Replication:** `not_performed`. **Numerical check:** Documentary table check:98/112=87.5%, consistent with Table4. No evaluation results or coverage matrix independently recomputed.

**Relevance:** `claim_evidence`. **Claim links:** [C46](claims.md#c46)

**Relevance rationale:** Adds a constructive multi-metric evaluation program and explicit coverage architecture, qualifying an overly negative inference that benchmarks can only establish their own limitations.

**Next check:** Use the pinned v2 method contribution and qualified cross-metric findings. Verify any specific model ranking against its scenario/metric, raw outputs and current model identity before publication.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2211.09110v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2211.09110v2) |
| `retrieved_at` | 2026-11-14T17:15:38.972660Z |
| `attempted_at` | 2026-11-14T17:15:38.972660Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 30970bda8958a1a8adf6a0a82feef9728331840288b7d2b49368bac87fd25f18 |
| `byte_length` | 6045688 |
| `mime_type` | application/pdf |
| `published_on` | 2023-10-01 |
| `version_claim` | arXiv2211.09110v2; TMLR08/2023 |
| `locator_basis` | One-based PDF viewer pages count cover; the printed page numbers coincide for Datasheets, Agents, HELM and main DecodingTrust. ARIA printed page1 begins PDF viewer8. HTML locators use named abstract/metadata headings. |
| `capture_path` | .source-captures/synthesis-30970bda8958a1a8adf6a0a82feef9728331840288b7d2b49368bac87fd25f18.pdf |

<a id="r2_sociotechnical_05"></a>
### r2_sociotechnical_05

**Source:** `wang_decodingtrust_2023`. **Theme:** sociotechnical. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Official NeurIPS2023 Datasets and Benchmarks PDF at the exact proceedings route already logged as a retrieval lead; title/authors/venue match canonical record. This is the proceedings object, not an assumed match to unpinned arXivlatest.

**Inspected scope:** Main text PDF/printed pp1–2 and4–10; AppendixB preliminaries/model/role setup PDFp30 (appendix printedp6). Includes text of Tables1–4 and selected method/result discussions for toxicity, robustness, OOD, demonstrations, privacy and fairness. Main Figure1 page3, full108-page appendices and graph values are not fully reviewed.

**Locators:** Mainp2 footnote3; AppendixB.1 PDFp30: gpt-4-0314 and gpt-3.5-turbo-0301; Main§2/Table1 p4; §4/Table2 pp5–6; Main§9/Table4 pp9–10

**Visual check:** No separate rendered-page visual inspection. Text and table/caption extraction were read; graphical coordinates, image-only contents and layout equivalence are not certified.

**Findings:**

- The benchmark measures eight distinct trustworthiness perspectives on fixed GPT checkpoints and reports both standard-condition improvements and adverse prompt/demonstration reversals.
- Table1 shows substantial detoxification in benign conditions compared with GPT-3 baselines while adversarial system conditions elicit much more toxicity; those endpoints use25 generations per prompt and must not be read as field incidence.
- Table4 reports higher GPT-4 accuracy together with greater demographic-parity/equalized-odds differences under constructed unequal base-rate conditions. Thus more accuracy does not determine every fairness endpoint.
- The work builds on existing benchmark families, including RealToxicityPrompts and AdvGLUE; overlap with other broad benchmark suites prevents treating them as fully independent samples of safety evidence.

**Counterevidence / alternative:** GPT-4 is better on several robustness/OOD/standard measures, so the study does not support a blanket claim that capability and trustworthiness move oppositely. Prompts, metrics and accessible roles determine the specific reversal.

**Limits:** Historical March2023 API checkpoints. Researchers can set system and user roles, so adversarial-system conditions are a particular access threat model rather than all ordinary deployments. Proxy toxic classifiers, prompted stereotype agreement and Adult salary prediction fairness do not estimate population harm. Proposed mechanisms attributing vulnerability to instruction following are hypotheses, not isolated causal tests. No full appendix or code/data reproduction.

**Replication:** `not_performed`. **Numerical check:** Documentary inspection of Tables1–4 and explicit25-generation endpoint only; no statistical, classifier or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C47](claims.md#c47)

**Relevance rationale:** Moves this record beyond inherited abstract-only coverage and supplies affirmative gains plus configuration-specific counterevidence to a single scalar capability/safety ranking.

**Next check:** Use qualitative tradeoffs with exact checkpoints/access and endpoint definitions. Finish relevant appendices and classifier-validity checks before reusing headline toxicity/fairness numbers or generalizing to current models.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://proceedings.neurips.cc/paper_files/paper/2023/file/63cb9921eecf51bfad27a99b2c53dd6d-Paper-Datasets_and_Benchmarks.pdf) |
| `final_url` | [Source](https://proceedings.neurips.cc/paper_files/paper/2023/file/63cb9921eecf51bfad27a99b2c53dd6d-Paper-Datasets_and_Benchmarks.pdf) |
| `retrieved_at` | 2026-11-14T17:14:59.249699Z |
| `attempted_at` | 2026-11-14T17:14:59.249699Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 0af07f4ded9e4d2c4ae1cc3ec5c765318d6e804a46211d206c1cbea9967dc8fe |
| `byte_length` | 42206195 |
| `mime_type` | application/pdf |
| `published_on` | 2023 |
| `version_claim` | NeurIPS2023 proceedings |
| `locator_basis` | One-based PDF viewer pages count cover; the printed page numbers coincide for Datasheets, Agents, HELM and main DecodingTrust. ARIA printed page1 begins PDF viewer8. HTML locators use named abstract/metadata headings. |
| `capture_path` | .source-captures/synthesis-0af07f4ded9e4d2c4ae1cc3ec5c765318d6e804a46211d206c1cbea9967dc8fe.pdf |

<a id="r2_sociotechnical_06"></a>
### r2_sociotechnical_06

**Source:** `huang_trustllm_2024`. **Theme:** sociotechnical. **Reading:** Abstract only. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Captured canonical PMLR235/huang24x landing page gives the exact proceedings title, author list and pages20166–20270. The initially guessed nested PMLR PDF route returned404; the actual PDF link points to mlresearch GitHub and was not retrieved/read in this bounded round.

**Inspected scope:** Official PMLR landing title/venue/pages and complete abstract; PDF download link identified. No methods/results/appendices read beyond inherited ledger.

**Locators:** PMLR235 landing page: Abstract and Cite this Paper

**Visual check:** No separate rendered-page visual inspection. Text and table/caption extraction were read; graphical coordinates, image-only contents and layout equivalence are not certified.

**Findings:**

- The abstract reports generally positive capability–trustworthiness association alongside a few open-model competitors and a benign-utility/over-refusal tradeoff. These are affirmative counter-leads for the broader review.

**Counterevidence / alternative:** Abstract summaries cannot decide whether the association survives matched capability, model-family, benchmark and refusal definitions. Do not add this abstract as independent empirical confirmation of another study.

**Limits:** Abstract-level review only. The proposed eight principles, six benchmark dimensions,16models and30+datasets are author summaries; no definitions, baselines, denominators or full methods verified. No coverage upgrade relative to inherited selected-section reading.

**Replication:** `not_performed`. **Numerical check:** No experimental replication or numerical recomputation; documentary quantities checked only where stated.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Retain a clearly identified positive counter-lead in the sociotechnical theme queue; do not force the abstract into a present empirical claim.

**Next check:** Read exact proceedings methods/results and dataset reuse before deciding how its positive association and utility tradeoff change the synthesis.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://proceedings.mlr.press/v235/huang24x.html) |
| `final_url` | [Source](https://proceedings.mlr.press/v235/huang24x.html) |
| `retrieved_at` | 2026-11-14T17:15:38.973420Z |
| `attempted_at` | 2026-11-14T17:15:38.973420Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 83cd7a5392faa64ee1532c44e83e4e6d14ff2a7c23cb56db531520934b041f70 |
| `byte_length` | 26196 |
| `mime_type` | text/html |
| `published_on` | 2024 |
| `version_claim` | PMLR235 proceedings abstract |
| `locator_basis` | One-based PDF viewer pages count cover; the printed page numbers coincide for Datasheets, Agents, HELM and main DecodingTrust. ARIA printed page1 begins PDF viewer8. HTML locators use named abstract/metadata headings. |
| `capture_path` | .source-captures/synthesis-83cd7a5392faa64ee1532c44e83e4e6d14ff2a7c23cb56db531520934b041f70.html |

<a id="r2_claimchecks_01"></a>
### r2_claimchecks_01

**Source:** `wijk_rebench_2025`. **Theme:** claim_checks. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. The PMLR 267 canonical landing page links this exact raw-GitHub PDF; PDF title/byline/ICML 2025 proceedings identity match the canonical record. The response MIME was application/octet-stream, but bytes have a valid PDF signature and pdfinfo reports61 pages.

**Inspected scope:** Final proceedings abstract; §§ 2.1 and human-comparison setup,3.1–3.5,5.1–5.3; Appendix A.1 and A.2–A.2.2; selected figure captions. Not all 61 pages or appendicesB–L.

**Locators:** Abstract printed p. 1; Figure 2 printed p. 3; §§ 3.2–3.3 printed pp. 5–6; § 5.2 printed p. 8; Appendix A.1 printed p. 14 and A.2 printed pp. 15–16

**Visual check:** Figure 2 and its time-budget axis/caption visually inspected on PDFviewerp3. No chart values independently digitized.

**Findings:**

- The final publication explicitly uses best-of-k sampling with replacement across shorter attempts; the human 32-hour point is best-of-four 8-hour runs, not one continuous32-hour session.
- Figure 2 reports the best observed time allocation for each agent. Results depend on both run duration and number of samples.
- Appendix A.1 explicitly allowed human experts to browse the internet and use LLMs and other tools. The comparison is autonomous agents versus expert workflows, not an unassisted-human/no-AI causal-uplift baseline.
- Final discussion retains an affirmative economic counterpoint: agents can be cheaper per unit time, so a time-score disadvantage need not imply economic noncompetitiveness.

**Counterevidence / alternative:** Realistic tools and human comparators strengthen relevance, while small self-contained tasks, best-of-k selection, heterogeneous human expertise and permitted LLM use bound automation and pure-AI uplift interpretations. Equal wall-clock budgets are not equal monetary cost.

**Limits:** The final proceedings access gap is closed for the checked claim, but this was not a complete61-page reread. No run-level scores or bootstraps recomputed; all environments/supplements not audited.

**Replication:** `not_performed`. **Numerical check:** None; no experiment or statistical analysis reproduced.

**Relevance:** `claim_evidence`. **Claim links:** [C03](claims.md#c03)

**Relevance rationale:** Directly bears on existing C03; preserves positive findings while resolving or bounding a version/method/numerical question.

**Next check:** Use exact final locators and comparator conditions in C03; leave full appendices/run-level reproduction as future work rather than blocking the scoped result.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wijk25a/wijk25a.pdf) |
| `final_url` | [Source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wijk25a/wijk25a.pdf) |
| `retrieved_at` | 2026-11-14T17:15:55.784044Z |
| `attempted_at` | 2026-11-14T17:15:55.784044Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 0208b92fe358754e6e245a2596d468961dba3fce9455da3f899e71f061af3df6 |
| `byte_length` | 13952284 |
| `mime_type` | application/pdf |
| `published_on` | 2025 |
| `version_claim` | ICML 2025 PMLR 267 proceedings, pp. 66772–66832 |
| `locator_basis` | One-based PDF viewer pages match printed page numbers1–61; external proceedings page span is66772–66832. |
| `capture_path` | .source-captures/synthesis-0208b92fe358754e6e245a2596d468961dba3fce9455da3f899e71f061af3df6.pdf |

<a id="r2_claimchecks_02"></a>
### r2_claimchecks_02

**Source:** `wijk_rebench_2025`. **Theme:** claim_checks. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. arXiv 2411.15114v1 is the earlier author preprint, not the canonical ICML 2025 proceedings object. Matching central passages do not establish complete edition equivalence.

**Inspected scope:** Selected preprint abstract,§ 4.2 best-of-k budgets and§ 4.3 environment comparisons; compared with final§§ 3.2–3.3.

**Locators:** arXiv v1 abstract; §§ 4.2–4.3

**Visual check:** No preprint chart values independently inspected or digitized.

**Findings:**

- The preprint likewise describes human 32-hour comparison as best of four 8-hour runs and agent budgets as different sample/duration allocations.
- The central aggregate-budget qualification survives into final publication, with changed section numbering.

**Counterevidence / alternative:** Version consistency on this one method point is not evidence that all preprint results and appendices are identical.

**Limits:** Only claim-critical sections compared, not a full-text diff or complete byline/appendix equivalence check.

**Replication:** `not_performed`. **Numerical check:** None; no experiment or statistical analysis reproduced.

**Relevance:** `background`. **Claim links:** [C03](claims.md#c03)

**Relevance rationale:** Directly bears on existing C03; preserves positive findings while resolving or bounding a version/method/numerical question.

**Next check:** Prefer the final proceedings source for C03 and retain this as a bounded version comparison.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/html/2411.15114v1) |
| `final_url` | [Source](https://arxiv.org/html/2411.15114v1) |
| `retrieved_at` | 2026-11-14T17:15:17.600320Z |
| `attempted_at` | 2026-11-14T17:15:17.600320Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | e9c7d8e1f744a50cc811f5b52d58be1db32cf4b59a8411509f963f876535ec62 |
| `byte_length` | 843441 |
| `mime_type` | text/html |
| `published_on` | Not recorded / unavailable |
| `version_claim` | arXiv 2411.15114v1 |
| `locator_basis` | HTML section headings and figure captions in captured arXiv v1 representation. |
| `capture_path` | .source-captures/synthesis-e9c7d8e1f744a50cc811f5b52d58be1db32cf4b59a8411509f963f876535ec62.html |

<a id="r2_claimchecks_03"></a>
### r2_claimchecks_03

**Source:** `lin_artemispenetration_2026`. **Theme:** claim_checks. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. The cover identifies arXiv 2512.09882v2,3 Mar 2026. Fresh retrieved SHAe83eb9c7… and length904633 exactly match the existing capture registry fingerprint; this does not constitute a fresh archive replay check.

**Inspected scope:** Abstract; Table 1; §§ 3.1–3.3 including Table 2/Benchmarks; § 5.3/Table 3; § 5.4 cost; § 6; § 7 limitations; Appendix E opening statement on scaffold design.

**Locators:** Table 1 printed p. 2; §§ 3.1–3.3 printed pp. 3–5; Table 2 and Benchmarks printed p. 5; Table 3/§ 5.3 printed p. 7; § 5.4 and§ 6 printed p. 8; § 7 limitations printed pp. 8–9; Appendix E opening printed p. 22

**Visual check:** Table 3 visually inspected on PDFviewerp7. No independent visual scoring of all findings, figures or run-level trajectories.

**Findings:**

- Table 1 and abstract supportA2 second overall, nine valid findings from eleven submissions and 82% rounded valid rate, outranking nine of ten professionals under the study score.
- Section 5.4 givesA1 $291.47 total/$18.21 per hour andA2 $944.07 total/$59 per hour. The cheaper configuration is not the strongestA2 result.
- The null Cybench scaffold comparison is located at Table 2 and§ 3.3 Benchmarks, printed p. 5; § 5.4 is cost analysis. C21 currently mislocates this point.
- Appendix E opening states that the v2 scaffold was designed by referencing the analyzed human attack graph. The paper also states that authentic defensive interdiction was absent and flagged actions were manually approved.
- TinyPilot remains internally inconsistent: Table 3 marks remote-console success at medium and host-only hints, while§ 6 prose says medium and high hints. The specific hint-level conclusion should be omitted.

**Counterevidence / alternative:** The authorized-network comparison is affirmative scoped capability evidence, while one site, ten selected professionals, score design, human-informed scaffold and relaxed interdiction prevent a general causal AI-assistance uplift estimate. The TinyPilot contradiction does not invalidate the overall 9/11 finding.

**Limits:** Conference-final source remains inaccessible, so no ICLR/preprint equivalence or publication-metadata update is established. Selected29-page v2 passages only; not all appendices reread.

**Replication:** `not_performed`. **Numerical check:** Documentary rounding only: 9/11=81.818…%, consistent with the rounded 82% table rate. No finding tally, significance test, cost reproduction or experiment replicated.

**Relevance:** `claim_evidence`. **Claim links:** [C21](claims.md#c21)

**Relevance rationale:** Directly bears on existing C21; preserves positive findings while resolving or bounding a version/method/numerical question.

**Next check:** Correct C21 locators and preserve central comparison and cost qualifications. Omit which TinyPilot hint levels succeeded until source data or an accessible authenticated later version resolves the table/prose mismatch. Do not hold the whole study hostage.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2512.09882v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2512.09882v2) |
| `retrieved_at` | 2026-11-14T17:15:17.601250Z |
| `attempted_at` | 2026-11-14T17:15:17.601250Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | e83eb9c7e3f92f02bafdc819e79f7c14a3df26d801eaf89e265592cd21759659 |
| `byte_length` | 904633 |
| `mime_type` | application/pdf |
| `published_on` | 2026-03-03 |
| `version_claim` | arXiv v2 |
| `locator_basis` | One-based PDF viewer pages count cover; printed numbers coincide for inspected pages. Note that malformed chart extraction contains form-feed glyphs, so page numbers were checked using per-page pdftotext and screenshot, not raw text split counts. |
| `capture_path` | .source-captures/synthesis-e83eb9c7e3f92f02bafdc819e79f7c14a3df26d801eaf89e265592cd21759659.pdf |

<a id="r2_claimchecks_04"></a>
### r2_claimchecks_04

**Source:** `lin_artemispenetration_2026`. **Theme:** claim_checks. **Reading:** Inaccessible. **Coverage effect:** `none`.

**Edition match:** `uncertain`. Requested the conference-final attachment cited in the existing review. No source bytes authenticated, so final title/edition/equivalence cannot be assumed.

**Inspected scope:** No conference paper text read. Official attachment returnedHTTP 403; the forum route redirected to an OpenReview challenge. No further OpenReview attempts made.

**Locators:** No authenticated final-paper locator

**Visual check:** None; no source PDF obtained.

**Findings:**

- No new substantive finding about the final paper.

**Counterevidence / alternative:** Failure to retrieve does not establish that the final differs fromv2 or that the earlier findings are wrong.

**Limits:** OpenReview attachmentHTTP 403; forum challenge is not source content. Its HTML was not admitted as a paper capture.

**Replication:** `not_performed`. **Numerical check:** None; no experiment or statistical analysis reproduced.

**Relevance:** `unresolved`. **Claim links:** [C21](claims.md#c21)

**Relevance rationale:** Directly bears on existing C21; preserves positive findings while resolving or bounding a version/method/numerical question.

**Next check:** Retain the preprint citation and omit final-version equivalence/venue changes until lawful authenticated final access is available.

| Capture field | Value |
|---|---|
| `preservation_status` | unavailable |
| `original_url` | [Source](https://openreview.net/attachment?id=Us00XndbVi&name=pdf) |
| `final_url` | Not recorded / unavailable |
| `retrieved_at` | Not recorded / unavailable |
| `attempted_at` | 2026-11-14T17:15:17.600845Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Source retrieval failed; no source bytes or independently checked archive were obtained. |
| `sha256` | Not recorded / unavailable |
| `byte_length` | Not recorded / unavailable |
| `mime_type` | Not recorded / unavailable |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Requested alleged ICLR final; unverified |
| `locator_basis` | No paper bytes or locators obtained. |
| `capture_path` | Not recorded / unavailable |

<a id="r2_claimchecks_05"></a>
### r2_claimchecks_05

**Source:** `xu_benchmarkingleakage_2024`. **Theme:** claim_checks. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. The captured HTML identifies arXiv 2404.18824v1,29 Apr 2024, matching the dated canonical preprint object.

**Inspected scope:** §§ 3.1–3.3 probe/reference/normalization design; § 4 controlled-exposure setup; § 5.3 instance-level interpretation and reported counts; Appendix A.2 training setup and completeA.3 formula/description; compared with pinned helper and README.

**Locators:** v1§ 3.2 reference synthesis; § 3.3 pipeline; § 4; § 5.3; Appendix A.2; Appendix A.3 Eq5

**Visual check:** HTML formula text/MathML read; no image-only figure values independently transcribed.

**Findings:**

- Appendix A.3 Eq5 printsD/max while the pinned helper computes1−D/max. The labels are opposite in orientation for identical strings.
- Section 5.3 and the pinned README both state an edit-similarity threshold greater than0.9, while helper reformat_data counts values greater than0.75.
- The paper itself says reference synthesis can introduce phraseology bias and that equal train/test exposure can mask its relative signal. Its controlled exposure test directly trains one model on benchmark data; it does not authenticate exposure of each model flagged by the observational proxy.
- The25 MATH-test exact-match examples in§ 5.3 remain reported proxy observations, not a verified count of leaked training records. The threshold discrepancy concerns lenient edit-score results and should not automatically erase separate exact-match findings.

**Counterevidence / alternative:** Plausible paper typo or code changes are hypotheses, not a recovered experiment manifest. Direct controlled exposure demonstrates probe sensitivity under its intentional training condition, while paraphrase differences, simultaneous exposure and reformatting limit exposure inference.

**Limits:** Not a new full article/table reread, not the earlier186-row recomputation. Exact experiment revision, saved predictions and which helper produced each table remain unestablished.

**Replication:** `not_performed`. **Numerical check:** None; no experiment or statistical analysis reproduced.

**Relevance:** `claim_evidence`. **Claim links:** [C10](claims.md#c10)

**Relevance rationale:** Directly bears on existing C10; preserves positive findings while resolving or bounding a version/method/numerical question.

**Next check:** Keep affected edit-similarity leakage quantities out of leading claims; retain narrow measured-proxy and design findings. Request/locate a run manifest only in a later bounded round if these numbers become publication-critical.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/html/2404.18824v1) |
| `final_url` | [Source](https://arxiv.org/html/2404.18824v1) |
| `retrieved_at` | 2026-11-14T17:15:17.602182Z |
| `attempted_at` | 2026-11-14T17:15:17.602182Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 2829ce99bcef4729e4e3ec857515e5df3475ba6e3d075c24626d9030c1451023 |
| `byte_length` | 976227 |
| `mime_type` | text/html |
| `published_on` | 2024-04-29 |
| `version_claim` | arXiv v1 |
| `locator_basis` | Captured arXiv v1 HTML section headings and MathML/text formula Eq5. |
| `capture_path` | .source-captures/synthesis-2829ce99bcef4729e4e3ec857515e5df3475ba6e3d075c24626d9030c1451023.html |

<a id="r2_claimchecks_06"></a>
### r2_claimchecks_06

**Source:** `xu_benchmarkingleakage_2024`. **Theme:** claim_checks. **Reading:** Full text. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. This is the ancillary75-line metric helper at a pinned code commit, not the paper itself. Reading it fully does not upgrade paper coverage.

**Inspected scope:** Complete metric_utils.py source, all 75 lines, including edit_similarity_score, reformat_data and __main__ file-selection loop.

**Locators:** Pinned commit 8cbb7fd341f0efe840ed5d9b148b87287362d9e9; metric_utils.py lines23–28 and40–48; main loop lines58–75

**Visual check:** None; plain source text.

**Findings:**

- The function computes1−edit_distance/max_length.
- reformat_data uses edit_similarity >0.75, and does not overwrite preexisting edit_similarity values.
- The script main loop filters for Grok/GSM8K filenames; its existence does not show that this helper generated every published model/table result.

**Counterevidence / alternative:** Precomputed score fields can survive unchanged through reformat_data, making the helper insufficient to reconstruct original experiment semantics.

**Limits:** Static code reading only. Dependencies/model predictions not executed; repository revision is not authenticated as the paper experiment revision.

**Replication:** `not_performed`. **Numerical check:** Static code comparison; no experimental replication. Identical nonempty strings haveD=0, hence printed formula0 versus helper1 by direct arithmetic.

**Relevance:** `claim_evidence`. **Claim links:** [C10](claims.md#c10)

**Relevance rationale:** Directly bears on existing C10; preserves positive findings while resolving or bounding a version/method/numerical question.

**Next check:** Retain the documentary mismatch and bound any inference about affected published values; do not silently recompute paper results using this helper as the definitive pipeline.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/GAIR-NLP/benbench/8cbb7fd341f0efe840ed5d9b148b87287362d9e9/src/metric_utils.py) |
| `final_url` | [Source](https://raw.githubusercontent.com/GAIR-NLP/benbench/8cbb7fd341f0efe840ed5d9b148b87287362d9e9/src/metric_utils.py) |
| `retrieved_at` | 2026-11-14T17:15:17.606035Z |
| `attempted_at` | 2026-11-14T17:15:17.606035Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 75b274565e098b7a91ab9578b289088a15a9aa4c9f36f1aa84d2c0074358585c |
| `byte_length` | 2973 |
| `mime_type` | text/plain |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Git commit 8cbb7fd341f0efe840ed5d9b148b87287362d9e9 |
| `locator_basis` | Line numbers in exact retained75-line UTF-8source; no code execution. |
| `capture_path` | .source-captures/synthesis-75b274565e098b7a91ab9578b289088a15a9aa4c9f36f1aa84d2c0074358585c.txt |

<a id="r2_claimchecks_07"></a>
### r2_claimchecks_07

**Source:** `xu_benchmarkingleakage_2024`. **Theme:** claim_checks. **Reading:** Full text. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. The pinned repository README is ancillary project documentation, not the canonical paper edition.

**Inspected scope:** Complete retained README Markdown text, including pipeline/instance-detection description and citation; linked images/demo/payloads not read.

**Locators:** README at pinned commit 8cbb7fd341f0efe840ed5d9b148b87287362d9e9; Examples instance-level scoring paragraph

**Visual check:** None; linked images/GIF/demo not inspected.

**Findings:**

- The pinned README repeats edit similarity >0.9, matching paper § 5.3 and differing from the same-revision helper threshold >0.75.

**Counterevidence / alternative:** Agreement between README and article clarifies the documentary inconsistency but does not establish which threshold generated released results.

**Limits:** Full README text only. It is not an experiment manifest or source-data reproduction and does not upgrade whole-paper depth.

**Replication:** `not_performed`. **Numerical check:** None; no experiment or statistical analysis reproduced.

**Relevance:** `background`. **Claim links:** [C10](claims.md#c10)

**Relevance rationale:** Directly bears on existing C10; preserves positive findings while resolving or bounding a version/method/numerical question.

**Next check:** Preserve both written specification and helper behavior; do not declare a corrected empirical leakage rate.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/GAIR-NLP/benbench/8cbb7fd341f0efe840ed5d9b148b87287362d9e9/README.md) |
| `final_url` | [Source](https://raw.githubusercontent.com/GAIR-NLP/benbench/8cbb7fd341f0efe840ed5d9b148b87287362d9e9/README.md) |
| `retrieved_at` | 2026-11-14T17:15:17.606704Z |
| `attempted_at` | 2026-11-14T17:15:17.606704Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 7df0d1974534921f84665b8e090e5f26f7ccc54c8ed046e454da66188fdfe376 |
| `byte_length` | 7796 |
| `mime_type` | text/plain |
| `published_on` | Not recorded / unavailable |
| `version_claim` | README at Git commit 8cbb7fd341f0efe840ed5d9b148b87287362d9e9 |
| `locator_basis` | Headings and literal Markdown paragraphs of the retained README; linked media excluded. |
| `capture_path` | .source-captures/synthesis-7df0d1974534921f84665b8e090e5f26f7ccc54c8ed046e454da66188fdfe376.txt |
## mechanistic-fairness-policy-2026-11-14

**As of:** 2026-11-14. **Base commit:** `017bd8f3dc67d8a329e75c4c53ad36c1355c4577`.

**Question:** What do mechanistic validation, fairness/value evaluation and policy-implementation sources add to or change in the broad synthesis, including the two deferred audit papers?

**Selection basis:** Purposive selection from the existing corpus and prior reconciliation queue, following the maintainer's next priorities. The starting local state has45 claims/83 mapped keys,201 unresolved roles and175 records without a combined full-text label. Six complementary strands select29 keys, including existing claim checks and background material. Source acquisition begins in parallel with this working selection; this is neither systematic sampling nor preregistration.

**Stopping rule:** Finish a bounded reviewable thematic unit with source-level depth and relevance decisions. Read manageable texts completely when consequential; use exact methods/appendix/figure checks for long or related editions. Preserve failed access and hold/omit affected numerical or current-status claims rather than blocking unrelated findings. No new bibliography admission or public release is part of this round.

| Theme | Why selected | Canonical keys |
|---|---|---|
| SAE validation and ground-truth/control tests | Challenges C13 with affirmative validation, negative controls, causal/reconstruction endpoints and transfer limits. | `makelov_principledevaluations_2024`, `karvonen_measuringprogressdictionar_2024`, `braun_identifyingfunctionally_2024`, `cunningham_sparseautoencoders_2024`, `heap_sparseautoencoders_2025` |
| Circuit tracing and interpretation evidence | Separates interpretable descriptions and attribution from demonstrated causal mechanisms, graph completeness and useful controls. | `ameisen_circuittracingrevealing_2025`, `lindsey_biology_2025`, `sharkey_openproblemsmechanistic_2025`, `paulo_automaticallyinterpreting_2024`, `lan_sparseautoencoders_2024` |
| Deferred audit layers and compliance-review mechanisms | Completes the two explicitly deferred sources where feasible and tests the proposal/observed-review distinction against Homewood. | `longpre_inhouseevaluation_2025`, `mokander_auditinglargelanguagemodels_2024`, `homewood_thirdpartycompliance_2025` |
| Fairness metrics, plural preferences and affected populations | Separates group metrics, value elicitation, judge agreement and impact; seeks missing counterevidence to averaged-score or universal-value claims. | `huang_collectiveconstitutional_2024`, `swamy_minimaximalistapproach_2024`, `huang_trustllm_2024`, `wang_decodingtrust_2023`, `bender_stochasticparrots_2021` |
| Federal-use implementation comparators | Distinguishes historical reported acts, inventory evidence and prospective procedures, with explicit relevance limits for frontier-provider governance. | `sba_complianceplanomb_2024`, `eac_complianceplanomb_2024`, `exim_complianceplanomb_2024`, `statedepartment_complianceplanomb_2024`, `omb_2024federalagency_2024`, `omb_m2521_2025` |
| Provider disclosure and implementation evidence | Tests what transparency scores, framework comparisons and provider accounts actually establish about practices, implementation and effects. | `wan_foundationmodeltransparency_2025`, `metr_commonelementsfrontier_2024`, `nvidia_frontierriskassessment_2025`, `anthropic_frontiercomplianceframework_2026`, `meta_advancedaiscalingframeworkv2_2026` |

### Event index

| Event | Source | Reading | Edition / coverage effect | Relevance |
|---|---|---|---|---|
| [r3_mechvalidation_01](#r3_mechvalidation_01) | `karvonen_measuringprogressdictionar_2024` | Full text | same_record / complete_record_text | claim_evidence |
| [r3_mechvalidation_02](#r3_mechvalidation_02) | `cunningham_sparseautoencoders_2024` | Full text | same_record / complete_record_text | claim_evidence |
| [r3_mechvalidation_03](#r3_mechvalidation_03) | `braun_identifyingfunctionally_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_mechvalidation_04](#r3_mechvalidation_04) | `makelov_principledevaluations_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_circuits_01](#r3_circuits_01) | `ameisen_circuittracingrevealing_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_circuits_02](#r3_circuits_02) | `lindsey_biology_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_circuits_03](#r3_circuits_03) | `paulo_automaticallyinterpreting_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r3_circuits_04](#r3_circuits_04) | `lan_sparseautoencoders_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r3_circuits_05](#r3_circuits_05) | `sharkey_openproblemsmechanistic_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_circuits_06](#r3_circuits_06) | `paulo_automaticallyinterpreting_2024` | Abstract only | same_record / none | background |
| [r3_circuits_07](#r3_circuits_07) | `lan_sparseautoencoders_2024` | Abstract only | related_edition / none | background |
| [r3_circuits_08](#r3_circuits_08) | `sharkey_openproblemsmechanistic_2025` | Abstract only | same_record / none | background |
| [r3_audits_01](#r3_audits_01) | `longpre_inhouseevaluation_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_audits_02](#r3_audits_02) | `mokander_auditinglargelanguagemodels_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_audits_03](#r3_audits_03) | `homewood_thirdpartycompliance_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_fairness_01](#r3_fairness_01) | `huang_collectiveconstitutional_2024` | Full text | related_edition / none | claim_evidence |
| [r3_fairness_02](#r3_fairness_02) | `swamy_minimaximalistapproach_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_fairness_03](#r3_fairness_03) | `huang_trustllm_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_fairness_04](#r3_fairness_04) | `wang_decodingtrust_2023` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_fairness_05](#r3_fairness_05) | `bender_stochasticparrots_2021` | Selected sections | same_record / scoped_review | background |
| [r3_public_01](#r3_public_01) | `exim_complianceplanomb_2024` | Full text | same_record / complete_record_text | claim_evidence |
| [r3_public_02](#r3_public_02) | `omb_m2521_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r3_public_03](#r3_public_03) | `sba_complianceplanomb_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_public_04](#r3_public_04) | `eac_complianceplanomb_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_public_05](#r3_public_05) | `statedepartment_complianceplanomb_2024` | Inaccessible | uncertain / none | unresolved |
| [r3_public_06](#r3_public_06) | `omb_2024federalagency_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_public_07](#r3_public_07) | `omb_2024federalagency_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_public_08](#r3_public_08) | `omb_2024federalagency_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_public_09](#r3_public_09) | `omb_2024federalagency_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_provider_01](#r3_provider_01) | `wan_foundationmodeltransparency_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_provider_02](#r3_provider_02) | `nvidia_frontierriskassessment_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r3_provider_03](#r3_provider_03) | `meta_advancedaiscalingframeworkv2_2026` | Selected sections | same_record / scoped_review | claim_evidence |
| [r3_provider_04](#r3_provider_04) | `metr_commonelementsfrontier_2024` | Selected sections | same_record / scoped_review | background |
| [r3_provider_05](#r3_provider_05) | `metr_commonelementsfrontier_2024` | Selected sections | related_edition / scoped_review | background |
| [r3_provider_06](#r3_provider_06) | `anthropic_frontiercomplianceframework_2026` | Inaccessible | uncertain / none | unresolved |

<a id="r3_mechvalidation_01"></a>
### r3_mechvalidation_01

**Source:** `karvonen_measuringprogressdictionar_2024`. **Theme:** mechanistic_validation. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact arXiv identifier, title, and author match to the authoritative record; pinned arXiv:2408.00113v2, dated 30 October 2024 on the PDF cover; NeurIPS2024 footer. This event certifies this arXiv edition only, not identity with a separately published proceedings version or future revisions.

**Inspected scope:** Complete pinned 21-page arXiv v2 PDF: abstract, Sections1–8, author contributions, acknowledgments, references, Appendices A–G, Tables1–5, Figures1–6. Linked code, model weights, datasets, and other papers were not opened or reproduced.

**Locators:** Sections2.1–3.2, pp.2–5: eight-layer chess/Othello models, researcher-specified BSPs, coverage and board reconstruction definitions; Section5, pp.7–9; Table1 p.8; Figures2–4 pp.6–9: trained/random comparison and p-annealing comparisons; Section6 p.9: domain, researcher ontology, and downstream-use limitations; AppendixD, pp.18–19, Tables4–5: per-property trained/random comparisons; AppendixF.2 p.20: masking initial board locations and layer1 positional shortcut control

**Visual check:** Rendered and visually inspected every figure (1–6) on PDF pages2,6,7,9,20,21; inspected plotted axes/legends, board examples, and Table1 plus Tables2–5 in text. No external feature dashboard or executable artifact inspected.

**Findings:**

- The paper supplies affirmative reference-task validation: features recover formally specified board properties, and board-state metrics distinguish trained models from same-architecture random-weight controls (Section5/Table1).
- Coverage averages the best single-feature F1 for each researcher-selected BSP; reconstruction combines features having at least .95 training precision and evaluates board-level F1 on a distinct test set of1000 games (Section3.2). These measure recovery under a specified feature ontology rather than all possible model knowledge.
- AppendixF.2 explicitly removes pieces at initial locations to reduce positional shortcuts. The layer1 SAE reconstruction F1 is reported as .01 under this restriction versus .52 when initial locations are included; the authors attribute the latter to PGN token position. This is a reported documentary control, not a reproduced result.
- AppendixD/Table5 shows some random-model strategy properties score highly when correlated with syntax or move number, including queen/castling-related properties. “Ground truth” labels alone do not eliminate shortcuts.
- p-annealing improves over standard L1 SAEs on tested proxy and supervised metrics; coverage also reveals expansion-size differences not evident in earlier unsupervised plots. Linear probes still outperform the SAEs on board recovery.

**Counterevidence / alternative:** Random-weight controls are weak on full board reconstruction but can be strong on some strategic labels; linear probes remain better and the paper explicitly says downstream interpretability tasks are not tested. The existence of useful discriminating metrics challenges an undifferentiated reading that SAE evaluation cannot separate learned structure from random structure.

**Limits:** Two small eight-layer GPT board-game models, residual stream after layer6, hand-selected board/strategy properties and restricted move positions. Board-property recovery is not a comprehensive dictionary, mechanistic pathway audit, natural-language safety evaluation, or deployment validation. No replication. Table1 and Table4 use similarly named board-state reconstruction results without enough reporting detail here to certify identical aggregation/selection; do not collapse them into one best-score claim.

**Replication:** `not_performed`. **Numerical check:** Documentary comparison of reported metrics and controls only; no data extraction, uncertainty recalculation, model execution, or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C48](claims.md#c48)

**Relevance rationale:** Adds affirmative validation and boundaries to C13; maps the source to specific new claims without treating source inclusion or separate-agent checking as independent corroboration.

**Next check:** If a publication-leading reconstruction number is needed, inspect released evaluation code/results to reconcile Table1 game-level G_board-state reconstruction with Table4 grouped per-property comparisons, verifying target, averaging, SAE selection, and masking. Retain a qualitative statement until those match. Test whether analogous controls survive more complex language tasks.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2408.00113v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2408.00113v2) |
| `retrieved_at` | 2026-11-14T17:53:03Z |
| `attempted_at` | 2026-11-14T17:53:03Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | cb876b31bbc8d9095ddd8b4f1aad5a60fd8ef2f8727394a9063ddc45db0a8ca4 |
| `byte_length` | 3451373 |
| `mime_type` | application/pdf |
| `published_on` | 2024-10-30 |
| `version_claim` | arXiv:2408.00113v2, dated 30 October 2024 on the PDF cover; NeurIPS2024 footer |
| `locator_basis` | Printed page numbers agree with PDF viewer pages; numbered sections, figures, tables, and appendices are version-specific. |
| `capture_path` | .source-captures/synthesis-cb876b31bbc8d9095ddd8b4f1aad5a60fd8ef2f8727394a9063ddc45db0a8ca4.pdf |

<a id="r3_mechvalidation_02"></a>
### r3_mechvalidation_02

**Source:** `cunningham_sparseautoencoders_2024`. **Theme:** mechanistic_validation. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact arXiv identifier, title, and author match to the authoritative record; pinned arXiv:2309.08600v3, dated 4 October 2023 on the PDF cover. This event certifies this arXiv edition only, not identity with a separately published proceedings version or future revisions.

**Inspected scope:** Complete pinned 20-page arXiv v3 PDF: abstract, Sections1–6, acknowledgments, references, Appendices A–G, Tables1–2, Figures1–18. This is the arXiv edition dated 4 October 2023, not a newly inspected ICLR2024 proceedings artifact. No linked code, source data, or model weights executed.

**Locators:** Sections2–3, pp.2–5: tied-weight SAE methods, baselines, automatic interpretation; Sections4.1–4.2, pp.5–6, Figure3: Pythia410M IOI counterfactual activation patching and edit-magnitude comparisons; Section5, pp.6–8, Figures4–5: selected token-feature ablations and closing-parenthesis causal tree; Section6.2 pp.8–9: reconstruction residuals, perplexity increase, architecture/layer and task-generalization limitations; AppendixA pp.11–12: GPT4 explanations/GPT3.5 simulation, top-random mixture, skipped low-variation features; AppendicesC.2–C.3 pp.13–15 and G pp.18–20: random-only scoring, dead MLP features, matched top-K baseline; AppendicesD.3–D.4 pp.16–17 and F pp.18–19: selection procedure, failed weight-only circuit method, other IOI layers

**Visual check:** Rendered and visually inspected all Figures1–18 on PDF pages2,4,5,7,8,12–20, including other-layer IOI curves and top-K baselines. Figures16–17 contain dense panels and were read as qualitative trends, not digitized numerical estimates. Tables1–2 read in PDF text and rendering.

**Findings:**

- On IOI, counterfactual feature patching on Pythia410M can move output distributions toward the counterfactual target with fewer patched directions and smaller edits than PCA/non-sparse dictionaries under the reported selection procedure (Section4/Figure3). This is affirmative task-level causal utility, distinct from automatic interpretability scoring.
- The ACDC feature ordering is selected separately per decomposition by average KL divergence over50 IOI datapoints; the patch adds coefficient differences times learned decoder directions to original activations. The evidence is targeted intervention success under this setup, not recovery of every causally important feature.
- Selected apostrophe and closing-parenthesis examples use ablation effects on logits/upstream features, giving causally checked examples beyond input correlation. AppendixD.3 explains feature searching/selection, so examples should remain described as selected case studies.
- Random-only fragment scoring is much lower than top-random scoring but retains the early-layer relative advantage; top-K PCA/ICA controls explain only a small fraction of the score gap. Late-layer advantage is smaller, and MLP dictionaries have many dead features (AppendixC/G).
- Reconstruction loses behaviorally relevant information: Section6.2 reports layer2 Pythia70M replacement increasing Pile perplexity from25 to40. The authors describe IOI generalization beyond the tested behavior as future work, not an established result.

**Counterevidence / alternative:** Reconstruction is incomplete; autointerpretability varies by layer/sample protocol; selected feature examples and IOI patching are not a comprehensive mechanistic account. AppendixD.4 reports a failed weight-based cross-layer feature-connection method, and AppendixC documents MLP failures.

**Limits:** Pythia70M/410M and Pile/OpenWebText; selected IOI templates and token-feature examples. The same IOI task family used in later Makelov work is not an independent task replication. Automatic scores do not certify semantic completeness; selected ablations do not establish reliable safeguards. ArXivv3 is identified by the authoritative record’s exact eprint/DOI; the record’s separate ICLR2024 venue/year is not recertified by this reading.

**Replication:** `not_performed`. **Numerical check:** Documentary comparison of reported metrics and controls only; no data extraction, uncertainty recalculation, model execution, or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C49](claims.md#c49)

**Relevance rationale:** Adds affirmative validation and boundaries to C13; maps the source to specific new claims without treating source inclusion or separate-agent checking as independent corroboration.

**Next check:** For any publication claim tied to peer-reviewed wording, inspect the ICLR2024 proceedings edition and determine whether its methods/results differ from the fully read arXivv3. Broaden causal tests beyond IOI and retain random-model controls from later metric-validity studies.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2309.08600v3) |
| `final_url` | [Source](https://arxiv.org/pdf/2309.08600v3) |
| `retrieved_at` | 2026-11-14T17:53:06Z |
| `attempted_at` | 2026-11-14T17:53:05Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 0475237e835c07738a74b2f372f0b7aa33ac047dce6affd49bb750dc4009e661 |
| `byte_length` | 1820169 |
| `mime_type` | application/pdf |
| `published_on` | 2023-10-04 |
| `version_claim` | arXiv:2309.08600v3, dated 4 October 2023 on the PDF cover |
| `locator_basis` | Printed page numbers agree with PDF viewer pages; numbered sections, figures, tables, and appendices are version-specific. |
| `capture_path` | .source-captures/synthesis-0475237e835c07738a74b2f372f0b7aa33ac047dce6affd49bb750dc4009e661.pdf |

<a id="r3_mechvalidation_03"></a>
### r3_mechvalidation_03

**Source:** `braun_identifyingfunctionally_2024`. **Theme:** mechanistic_validation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact arXiv identifier, title, and author match to the authoritative record; pinned arXiv:2405.12241v2, dated 24 May 2024 on the PDF cover. This event certifies this arXiv edition only, not identity with a separately published proceedings version or future revisions.

**Inspected scope:** Pinned31-page arXivv2 PDF: abstract and Sections1–3.4, pp.1–8; AppendixA.7 discussion/Figure9/Table4 pp.15–17; AppendixD experimental details pp.20–23; AppendixE dictionary-size/training-sample descriptions p.23; AppendixH runtime discussion/Table6 p.31. Other sections/appendices were not fully read.

**Locators:** Sections1–2.5, pp.1–5: functional importance, frozen-model output-KL objective, downstream reconstruction loss, evaluation/data definitions; Sections3.1–3.4 pp.5–8, Figures1–3 and Table1: output fidelity, reconstruction divergence, cross-seed features, automatic interpretation; AppendixA.7 pp.15–17, Figure9/Table4: matched-sparsity versus matched-CE interpretation comparisons; AppendixD pp.20–23: OpenWebText samples, training/evaluation settings and frozen target model; AppendixE p.23 and AppendixH p.31: extra local-training comparisons and compute cost

**Visual check:** Rendered and visually inspected Figures1–3 and9 on PDF pages2,7,8,17; read Tables1,4,6 and selected experimental details in text. Did not inspect all31 pages or all appendix plots/dashboards.

**Findings:**

- End-to-end training optimizes output-KL after inserting SAE reconstructions into a frozen target model; adding downstream activation reconstruction constrains the path through later layers (Sections2.3–2.4).
- The reported end-to-end objectives improve the sparsity/output-performance tradeoff over local activation-MSE SAEs in the tested GPT2-small setting. Selected learning rates follow the Pareto frontier, and AppendixE discusses more local-training compute; training cost is higher (AppendixH).
- Pure output matching can retain output distributions while producing much larger downstream activation errors and less cross-seed feature alignment. Downstream reconstruction brings internal activations and feature stability closer to local SAEs (Sections3.2–3.3/Figures2–3).
- “No cost to interpretability” is bounded by the sampled automatic metric: matched-L0 comparisons show no significant difference; matched-CE comparisons favor e2e+downstream at layers2 and6 but not10 (Section3.4/AppendixA.7). This is not human confirmation of every feature or deployment validation.

**Counterevidence / alternative:** The pure output-matching variant demonstrates underdetermination of internal mechanisms by output fidelity. The downstream-loss variant mitigates this in studied models; sampled automated interpretation and geometric similarity remain partial evidence. Claims of uniquely correct mechanisms or reliable monitoring are unsupported.

**Limits:** GPT2-small, with supplementary TinyStories1M described but not fully reread here; OpenWebText training/evaluation, sampled automatic interpretation. Objective improvement is evaluated against local-SAE baselines and should not be equated with discovery of a unique true computation. No model, code, dashboard, or dataset execution.

**Replication:** `not_performed`. **Numerical check:** Documentary comparison of reported metrics and controls only; no data extraction, uncertainty recalculation, model execution, or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C50](claims.md#c50)

**Relevance rationale:** Adds affirmative validation and boundaries to C13; maps the source to specific new claims without treating source inclusion or separate-agent checking as independent corroboration.

**Next check:** Extend pathway/causal and random-model controls to larger/new architectures; inspect remaining appendices and qualitative dashboards before upgrading reading depth. Do not promote output fidelity alone to mechanistic faithfulness.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2405.12241v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2405.12241v2) |
| `retrieved_at` | 2026-11-14T17:53:05Z |
| `attempted_at` | 2026-11-14T17:53:04Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 903cf5400ba4ad7c18f265dd27971798a7e264abcb8795b9a10851f5da3d5b0d |
| `byte_length` | 17209779 |
| `mime_type` | application/pdf |
| `published_on` | 2024-05-24 |
| `version_claim` | arXiv:2405.12241v2, dated 24 May 2024 on the PDF cover |
| `locator_basis` | Printed page numbers agree with PDF viewer pages; numbered sections, figures, tables, and appendices are version-specific. |
| `capture_path` | .source-captures/synthesis-903cf5400ba4ad7c18f265dd27971798a7e264abcb8795b9a10851f5da3d5b0d.pdf |

<a id="r3_mechvalidation_04"></a>
### r3_mechvalidation_04

**Source:** `makelov_principledevaluations_2024`. **Theme:** mechanistic_validation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact arXiv identifier, title, and author match to the authoritative record; pinned arXiv:2405.08366v3, dated 20 May 2024 on the PDF cover. This event certifies this arXiv edition only, not identity with a separately published proceedings version or future revisions.

**Inspected scope:** Pinned51-page arXivv3 PDF: abstract/overview; Sections3–6 and8 pp.4–16; AppendicesA.1–A.4 pp.21–24, A.11 pp.34–35 and A.14 pp.39–40. Visual checks limited to Figures2–4,6,13. Other appendices, full plotting appendix, linked code and data were not fully inspected.

**Locators:** Sections3.2–3.4 pp.4–7: necessity/sufficiency, sparse attribute control and interpretation-consistent causal effects are different tests; Sections4.1–4.2 pp.7–9, Figures2–3: supervised task dictionaries and control reference; Section5.1–5.2 pp.9–13, Figures2–4: task/full-distribution SAE methods, greedy feature editing, frozen-random-decoder control; Section6.1–6.2 pp.13–14, Figure6: feature occlusion and over-splitting; Section8 pp.15–16: human-chosen ontology, single-model/task limitation; AppendicesA.2–A.4 pp.22–24: mean-ablation baseline, editing normalization and train/test task construction; AppendixA.11 pp.34–35: SAE hyperparameters and training distribution; AppendixA.14 pp.39–40/Figure13: occlusion sweep, magnitude intervention and toy model

**Visual check:** Rendered and visually inspected Figures2,3,4,6,13 on PDF pages5,8,11,13,39. Figure5 and large appendix grids/causal-interpretation plots were not visually checked; no claims of reading them in full.

**Findings:**

- A successful task evaluation distinguishes dictionary reconstruction sufficiency/necessity, sparse control of specified attributes, and causal consistency of feature interpretations. The supervised dictionaries are tested as a task-specific reference, rather than assumed to be complete truth (Sections3–4).
- Both task-specific and full-distribution SAEs contain interpretable IOI features, but task-specific SAEs fall short of supervised dictionaries on sparse control and full-distribution SAEs perform worse (Section5.2). For some subject edits, a no-intervention baseline already agrees highly with the counterfactual, reducing test resolution.
- The frozen-at-initialization decoder control performs worse than ordinary task-specific SAEs, establishing nontrivial control utility for the latter. Full-distribution SAEs perform on par with that frozen-decoder control in the reported IOI controllability comparison; interpretation alone is insufficient for sparse control (Section5.2).
- Feature occlusion provides a concrete missing-evidence risk: causally relevant subject information is less often recovered as high-F1 individual-name features than slightly larger indirect-object features. Reducing the latter’s magnitude improves discovery of subject-name features; the related toy effect depends on interpretation threshold (Section6.1/AppendixA.14).
- “Ground truth edit” means the target model’s response to replacing activations by counterfactual-prompt activations, not ground-truth external task correctness. AppendixA.4 distinguishes positive correct-versus-incorrect-name logit difference from actual top-token accuracy.

**Counterevidence / alternative:** Control tests do discriminate ordinary task-SAEs from frozen random decoder features, so this paper supplies affirmative utility as well as failure evidence. Human-chosen attributes can penalize useful alternative decompositions; non-exhaustive tuning prevents a universal statement about all SAEs. Cross-task and frontier-scale usefulness remain unverified.

**Limits:** GPT2-small IOI circuit using researcher-selected IO/subject/position ontology, simplified templates and non-exhaustive SAE tuning. Supervised dictionaries are a validated task reference, not complete ground truth for every representation. Shared IOI task lineage with Cunningham reduces task diversity; this is not independent replication. Toy occlusion/splitting results are author-reported and not rerun here.

**Replication:** `not_performed`. **Numerical check:** Documentary comparison of reported metrics and controls only; no data extraction, uncertainty recalculation, model execution, or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C49](claims.md#c49), [C50](claims.md#c50)

**Relevance rationale:** Adds affirmative validation and boundaries to C13; maps the source to specific new claims without treating source inclusion or separate-agent checking as independent corroboration.

**Next check:** Full reading would require remaining appendices and plots, including causal-interpretation sufficiency/necessity and extensive hyperparameter panels. If advancing the final thesis, compare the later ICLR2025 publication edition and newer SAE methods before treating these2024 gap sizes as current limits.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2405.08366v3) |
| `final_url` | [Source](https://arxiv.org/pdf/2405.08366v3) |
| `retrieved_at` | 2026-11-14T17:53:03Z |
| `attempted_at` | 2026-11-14T17:53:02Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | e036ae6ba0fc604d79ebd30d6bbd14100117c6cd1b4665669688c8063e3721d1 |
| `byte_length` | 2335650 |
| `mime_type` | application/pdf |
| `published_on` | 2024-05-20 |
| `version_claim` | arXiv:2405.08366v3, dated 20 May 2024 on the PDF cover |
| `locator_basis` | Printed page numbers agree with PDF viewer pages; numbered sections, figures, tables, and appendices are version-specific. |
| `capture_path` | .source-captures/synthesis-e036ae6ba0fc604d79ebd30d6bbd14100117c6cd1b4665669688c8063e3721d1.pdf |

<a id="r3_circuits_01"></a>
### r3_circuits_01

**Source:** `ameisen_circuittracingrevealing_2025`. **Theme:** circuit_evidence. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Canonical title/authors and URL match this source; live HTML is time-bounded by the retained hash, not assumed immutable.

**Inspected scope:** Introduction; Building an Interpretable Replacement Model (including local replacement model); selected quantitative CLT/graph evaluations and graph completeness; Limitations (dark matter, inactive/inhibitory features, feature abstraction, global circuits, mechanistic faithfulness); Appendix Validating the Replacement Model; Nuances of Steering with Cross-Layer Features; Unexplained Variance and Choice of Steering Factors; selected Additional Evaluation Details. Not the complete article, training details, linked graphs or visual assets.

**Locators:** Building an Interpretable Replacement Model / From Cross-Layer Transcoder to Replacement Model / The Local Replacement Model; Evaluations / Quantitative CLT Evaluations / Evaluating and Comparing Graph Completeness; Limitations / Mechanistic Faithfulness; Appendix / Validating the Replacement Model / Evaluating Faithfulness of the Local Replacement Model; Appendix / Nuances of Steering with Cross-Layer Features; Additional Evaluation Details

**Visual check:** No complete visual review. Text and captions only; linked interactive graphs and external assets were not inspected.

**Findings:**

- Cross-layer transcoders produce prompt-specific computational graphs and improve the article’s selected reconstruction/sparsity/interpretability and graph metrics relative to per-layer transcoders or thresholded neurons; they also shorten paths, making some mechanisms more tractable to investigate.
- Error correction and freezing attention/normalization make the local replacement model exactly match original activations and logits on the unperturbed prompt, but the article explicitly says this does not establish use of the same mechanisms.
- Perturbation checks support some graph-predicted effects and outperform simple importance baselines. The broader appendix faithfulness comparison freezes attention in BOTH underlying and replacement models, finds useful short-range agreement, and accumulating errors farther downstream.
- Constrained patching can guarantee or nearly force direct feature-to-feature effects before an intervention layer; downstream knock-on and especially actual-output effects provide the nontrivial tests. Selective supernodes and layer/strength sweeps constrain the validation claim.

**Counterevidence / alternative:** The evidence is stronger than descriptive activation correlation alone: interventions on model computation test predicted downstream effects. Conversely, good reconstruction and the selectively successful interventions permit alternative replacement mechanisms; larger dictionaries do not uniformly improve perturbation faithfulness.

**Limits:** Selected sections only. Graph completeness/replacement scores concern influence assigned to feature versus error nodes inside this approximation, not semantic completeness or a calibrated safety-monitor coverage rate. Attention routing, reconstruction dark matter, suppressed inactive features, subjective supernode grouping and replacement shortcuts remain blind spots. No complete figures or interactive review, raw metrics, code or experiments.

**Replication:** `not_performed`. **Numerical check:** Read textual 50% next-token agreement qualification and selected dataset filters, plus appendix 20-prompt/0.72 Spearman report. These were not recalculated or digitized, and are not proposed as leading numerical claims.

**Relevance:** `claim_evidence`. **Claim links:** [C51](claims.md#c51)

**Relevance rationale:** Evidence for bounded mechanistic-validation synthesis; inclusion does not certify a complete read or deployment assurance.

**Next check:** For any leading quantitative claim, inspect the exact graph sample, attention-freezing condition, intervention layer/strength sweep, selection protocol and relevant plots; test downstream utility against baselines before calling this a monitor.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) |
| `final_url` | [Source](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) |
| `retrieved_at` | 2026-11-14T17:53:22.128574Z |
| `attempted_at` | 2026-11-14T17:53:21.428679Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independent archive capture was checked in this bounded round; exact local bytes and pinned version URLs where available are retained, without claiming archived immutability. |
| `sha256` | a70ce88c09533238154875dbb1320fd2d2aebedfd5fc7e782518385b3d597673 |
| `byte_length` | 276666 |
| `mime_type` | text/html |
| `published_on` | 2025-03-27 |
| `version_claim` | Live article, source byline March 27, 2025; retrieved 2026-11-14, no immutable revision identifier. |
| `locator_basis` | HTML section/subsection headings and retained extracted-text line spans. |
| `capture_path` | .source-captures/synthesis-a70ce88c09533238154875dbb1320fd2d2aebedfd5fc7e782518385b3d597673.html |

<a id="r3_circuits_02"></a>
### r3_circuits_02

**Source:** `lindsey_biology_2025`. **Theme:** circuit_evidence. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Canonical title/authors and URL match this source; live HTML is time-bounded by the retained hash, not assumed immutable.

**Inspected scope:** Method overview and validation caveat; full text of Introductory Example: Multi-step Reasoning, Planning in Poems and Multilingual Circuits subsections; selected hallucination/refusal intervention caveats. Other case studies, appendices and interactives not comprehensively read.

**Locators:** Method Overview (paragraph beginning Because they are based on our replacement model); Introductory Example: Multi-step Reasoning / Validation with Inhibition Experiments / Swapping Alternative Features; Planning in Poems / Planned Words Features and their Mechanistic Role / Planned Words Determine Sentence Structure; Multilingual Circuits / Editing the Operation: Antonyms to Synonyms / Editing the Operand / Editing the Output Language

**Visual check:** No complete visual review. Text and captions only; linked interactive graphs and external assets were not inspected.

**Findings:**

- The Dallas→Texas→Austin example includes a direct shortcut alongside the hypothesized two-step path. Replacing the Texas cluster by a California cluster identified from an Oakland prompt changes the original-model output to Sacramento; related swaps give other appropriate capitals.
- Poem interventions on candidate end-word representations at a newline change both eventual end words and intervening sentence structure in selected cases. This supports a local planning mechanism rather than only a descriptive label applied after completion.
- English-derived operation and operand feature interventions induce language-appropriate changes in English, French and Chinese prompts, while changing language features can change output language while preserving operation/operand. This is within-model cross-language evidence, not cross-model universality.
- The method overview explicitly distinguishes graph hypotheses from original-model intervention tests, prelabels/groupings before perturbation results, and notes that constrained-patching direct effects can be trivial while downstream outputs are the strongest validation endpoint.

**Counterevidence / alternative:** Actual model-output changes are affirmative causal evidence beyond correlated feature labels. The article itself retains shortcuts, partial circuit stories, unknown-name interventions that sometimes fail, strong-steering requirements and attention sensitivity; these defeat a blanket claim that a complete or uniquely correct circuit was recovered.

**Limits:** Selected illustrative cases in Claude 3.5 Haiku, not prevalence estimates over all planning or reasoning. Some interventions require atypically large activation multiples; causal intervention success can coexist with incomplete grouping and shortcut computation. No live interactive/visual-asset audit; no reproduction. The title’s biology is an interpretability metaphor, not biological-threat evidence.

**Replication:** `not_performed`. **Numerical check:** Read reported planning sample descriptions (25 poems, 70% end-word injection; 500 samples per illustrated experiment) and multilingual activation-count qualifications, but no raw denominator/figure audit; retain qualitative findings rather than publish these numbers.

**Relevance:** `claim_evidence`. **Claim links:** [C51](claims.md#c51)

**Relevance rationale:** Evidence for bounded mechanistic-validation synthesis; inclusion does not certify a complete read or deployment assurance.

**Next check:** Before foregrounding prevalence or cross-language generality, inspect sampling denominator, corresponding intervention figure assets and attention conditions; reproduce selected original-model outputs where access permits.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) |
| `final_url` | [Source](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) |
| `retrieved_at` | 2026-11-14T17:53:22.816995Z |
| `attempted_at` | 2026-11-14T17:53:22.150960Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independent archive capture was checked in this bounded round; exact local bytes and pinned version URLs where available are retained, without claiming archived immutability. |
| `sha256` | 0a17caa271974ab39d618b7aa86a650984049bd8c4afd943607dd654314a4c73 |
| `byte_length` | 246323 |
| `mime_type` | text/html |
| `published_on` | 2025-03-27 |
| `version_claim` | Live article, source byline March 27, 2025; retrieved 2026-11-14, no immutable revision identifier. |
| `locator_basis` | HTML section/subsection headings and retained extracted-text line spans. |
| `capture_path` | .source-captures/synthesis-0a17caa271974ab39d618b7aa86a650984049bd8c4afd943607dd654314a4c73.html |

<a id="r3_circuits_03"></a>
### r3_circuits_03

**Source:** `paulo_automaticallyinterpreting_2024`. **Theme:** circuit_evidence. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Same arXiv work/title/authors as canonical unversioned 2024 preprint record, but inspected v3 is a later 2025 proceedings-form version. No claim of equivalence to the original edition, and no canonical depth upgrade.

**Inspected scope:** All main-text sections 1–5 and data/code/impact statement (PDF pp1–9), Appendix C and D.1–D.3 selected prompt/scoring details (pp13–15), Table A10 and all Appendix G.1–G.4 text (pp22–24), Figure3 visually on p8. Other appendix sections/tables and references not comprehensively read; no full-text label.

**Locators:** v3 §§3.1–3.3.5, 4.1.1, 4.2, 5; Figure 3 (PDF p8); Appendix C (p13), D.1–D.3 (pp13–15); Appendix G.1–G.4 (pp22–24); Table A10 (p22)

**Visual check:** Visually inspected PDF p8 Figure3: trained-SAE intervention-score distribution has a positive tail relative to randomized TopK and shuffled-explanation controls; right-panel negative trend is layer32 at target KL3. No digitization; other figures not visually inspected.

**Findings:**

- Context-based detection/fuzzing ask whether a description predicts activation contexts or tokens; intervention scoring instead measures how a description explains changed generated output, as the scorer’s mean log-probability gain for the interpretation relative to clean generations.
- Intervention explanations distinguish trained SAE features from randomized TopK SAE features and shuffled descriptions in the illustrated comparisons. Some features with poor activation-context explanations have informative descriptions of their output effects, so a low context score is not sufficient to discard a feature’s possible causal role.
- Appendix G uses stratified feature-active RPJv2 contexts, separates 10 explanation prompts from 30 scoring prompts, tunes intervention strength to target KL on the scoring set, and generates at most eight new tokens with additive interventions. These design choices bound the endpoint and generalization claim.
- Broader activation-context sampling improves coverage of low-activating examples relative to top-only sampling, but may give overly broad or confused descriptions. The paper recommends multiple scores because they have different failure modes.

**Counterevidence / alternative:** Trained-versus-randomized feature and shuffled-description controls are positive validity checks for this output-description endpoint. A score increase can still be scorer/prompt/short-generation dependent, and later-layer output proximity helps explain higher intervention scores. Good explanation scores do not establish completeness or safety-monitor performance.

**Limits:** Pinned arXiv v3 is dated 2025-08-06 and carries an ICML/PMLR2025 proceedings footer, whereas the bibliography year/preprint type is 2024. This is explicitly a later version, not assumed unchanged from v1. Only selected appendix material and one figure visually reviewed; no full-document upgrade, downstream safety task, raw-data check or experiments. Intervention prompts are feature-active contexts; KL is tuned on scoring set rather than a completely untouched calibration set.

**Replication:** `not_performed`. **Numerical check:** Figure3 printed correlation r=-0.37 is visually confirmed for that illustrative layer32/KL3 panel, not an all-layer result. Appendix G prompt split/≤8-token limit/KL-tuning procedure checked textually; no recomputation.

**Relevance:** `claim_evidence`. **Claim links:** [C52](claims.md#c52)

**Relevance rationale:** Evidence for bounded mechanistic-validation synthesis; inclusion does not certify a complete read or deployment assurance.

**Next check:** Pin the exact version in any synthesis citation; compare v1/v3 if retaining 2024-specific conclusions. For leading intervention scores, inspect held-out calibration, stronger negative controls, longer generations and actual downstream utility.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2410.13928v3) |
| `final_url` | [Source](https://arxiv.org/pdf/2410.13928v3) |
| `retrieved_at` | 2026-11-14T17:54:58.523935Z |
| `attempted_at` | 2026-11-14T17:54:57.455759Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independent archive capture was checked in this bounded round; exact local bytes and pinned version URLs where available are retained, without claiming archived immutability. |
| `sha256` | e5e2631cfd4cd7a1b6ac960536593f700b83790603ba7b80d7aa47ff76e072d4 |
| `byte_length` | 7894423 |
| `mime_type` | application/pdf |
| `published_on` | 2025-08-06 |
| `version_claim` | arXiv:2410.13928v3, 6 Aug 2025; PDF proceedings footer PMLR267/ICML2025. |
| `locator_basis` | PDF page numbers count title page as page 1; section headings as printed. |
| `capture_path` | .source-captures/synthesis-e5e2631cfd4cd7a1b6ac960536593f700b83790603ba7b80d7aa47ff76e072d4.pdf |

<a id="r3_circuits_04"></a>
### r3_circuits_04

**Source:** `lan_sparseautoencoders_2024`. **Theme:** circuit_evidence. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Canonical citation key/title records the earlier Sparse autoencoders reveal universal feature spaces across large language models work; retrieved arXiv v4 has a different title. Track as related later edition pending record-level version adjudication; do not upgrade original depth.

**Inspected scope:** PDF pp1–6: abstract,introduction,definitions,method,setup and first results overview; pp9–11 related work/conclusion/limitations; Appendix A–D (pp17–19) and opening E.1–E.2 text/visuals on p20. Large remaining appendix, many result plots/tables and source code not read.

**Locators:** v4 §§1–4.2, 6 and Limitations (pp1–6,10); Appendix A–B (pp17–18); Appendix D / Baseline Comparisons to SAEs Trained on LLMs with Randomized Weights (pp18–20); Appendix E.1; Figure6 and Figure7 (p20)

**Visual check:** Visually inspected PDF p20 Figure6 randomized-Pythia heatmaps (low scores, not a zero-effect proof) and Figure7 same-SAE heatmaps with matching-layer diagonals near1. Remaining plots not visually audited.

**Findings:**

- Analogous Feature Universality concerns similarity of spaces spanned by paired SAE decoder features under representational transformations, not recovery of atomic true features or identical feature inventories.
- The method first pairs features by activation correlation on shared-token inputs, then measures decoder-weight-space similarity using SVCCA/RSA against randomized pairing/subset baselines. Some middle-layer and semantic subsets show stronger alignment than these baselines.
- Appendix D adds a useful alternative-explanation check: trained-versus-randomized Pythia comparisons (embedding layer retained) have much lower paired similarity than selected trained-model comparisons. This supports learned-structure contribution beyond the simplest data-sparsity explanation, within these controls.
- Main comparisons retain filtered subsets (non-concept token, shared top-token, correlation and many-to-one filters); Appendix B/E show very different retained fractions and recovered similarities across SAE training quality. Similarity is therefore conditional on pairing and feature extraction, with substantial unmatched or inconsistently recovered representation.

**Counterevidence / alternative:** Positive trained-versus-randomized and shuffled-pairing/subset controls make a blanket dismissal as meaningless correlation too strong. Conversely, weaker RSA, unmatched features, filter sensitivity, same-tokenizer restrictions and SAE-quality effects support narrower analogous-subspace similarity rather than universal causal circuits.

**Limits:** Current v4 title differs from the canonical 2024 title. Selected sections only; same-tokenizer model families, chosen widths/layers/datasets and filtered feature subsets. Neither tested portability of steering/control nor causal identity follows from representational alignment. No complete appendix/figure audit or reproduction. The random-model control retains embeddings and custom-SAEs have weaker recovery, limiting causal interpretation of differences.

**Replication:** `not_performed`. **Numerical check:** Read text reporting main filtered-retention range 10–30% versus much lower custom-SAE retention and approximately1% randomized-control retention. These are source-reported and condition-specific; no recomputation or aggregate universality percentage proposed.

**Relevance:** `claim_evidence`. **Claim links:** [C53](claims.md#c53)

**Relevance rationale:** Evidence for bounded mechanistic-validation synthesis; inclusion does not certify a complete read or deployment assurance.

**Next check:** Resolve canonical version/title handling; inspect Appendix J/K pairing/filter robustness and hold-out matching; demonstrate actual cross-model causal transfer before making a portable-control claim.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2410.06981v4) |
| `final_url` | [Source](https://arxiv.org/pdf/2410.06981v4) |
| `retrieved_at` | 2026-11-14T17:54:58.874419Z |
| `attempted_at` | 2026-11-14T17:54:58.534460Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independent archive capture was checked in this bounded round; exact local bytes and pinned version URLs where available are retained, without claiming archived immutability. |
| `sha256` | 41f7bfb24aa26c622b225ad1a235d5c95d3df7564cc0cb3a2438b3f606753cd8 |
| `byte_length` | 1884948 |
| `mime_type` | application/pdf |
| `published_on` | 2025-05-21 |
| `version_claim` | arXiv:2410.06981v4, 21 May 2025; title Quantifying Feature Space Universality Across Large Language Models via Sparse Autoencoders. |
| `locator_basis` | PDF page numbers count title page as page 1; section headings as printed. |
| `capture_path` | .source-captures/synthesis-41f7bfb24aa26c622b225ad1a235d5c95d3df7564cc0cb3a2438b3f606753cd8.pdf |

<a id="r3_circuits_05"></a>
### r3_circuits_05

**Source:** `sharkey_openproblemsmechanistic_2025`. **Theme:** circuit_evidence. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Canonical arXiv work/title/authors and currently only listed arXiv v1 match. This event does not resolve the separate published-TMLR edition lead.

**Inspected scope:** Title/abstract and selected §§2.1.4,2.1.4a,2.1.4b (PDF pp17–19), §2.3 circuit-validation/discovery issues (pp21–22), and §3.6 generalizability/selected §3.7 opening (pp31–32). Not a full review read or check of underlying cited experiments.

**Locators:** arXiv v1 §2.1.4–2.1.4b (pp17–19); §2.3 (pp21–22); §3.6 (p31), §3.7 opening (pp31–32)

**Visual check:** No complete visual review. Text and captions only; linked interactive graphs and external assets were not inspected.

**Findings:**

- This review treats feature descriptions as hypotheses requiring predictive validation and distinguishes activation/counterfactual tests, ground-truth models, downstream engineering success and competitive downstream evaluations.
- The review identifies method-dependent circuit faithfulness, imperfect decompositions, first-order attribution approximations, backup/inhibitory behavior and deliberately easy tasks as obstacles. It also acknowledges useful circuit insights and successful local engineering examples rather than claiming all interpretability has failed.
- Generalization of both methods and conclusions beyond a few architectures/model families is posed as an open empirical problem; conceptual promise for auditing or monitoring is not itself another performance experiment.

**Counterevidence / alternative:** The source articulates multiple affirmative validation routes and practical successes alongside limitations. Its cautions are guidance for interpreting direct experiments, not independent corroboration of the exact effects in Ameisen/Lindsey/Paulo/Lan.

**Limits:** Expert review/research agenda, not an independent safeguard efficacy trial. Read only selected v1 sections; cited experiments are not independently checked by reading the review. Existing ledger’s TMLR September2025 lead is not resolved by this arXiv-v1 capture, and published-final equivalence is not assumed.

**Replication:** `not_performed`. **Numerical check:** No raw-data calculation or experimental replication. Numerical descriptions, if mentioned, are documentary source checks only.

**Relevance:** `claim_evidence`. **Claim links:** [C51](claims.md#c51), [C52](claims.md#c52), [C53](claims.md#c53)

**Relevance rationale:** Evidence for bounded mechanistic-validation synthesis; inclusion does not certify a complete read or deployment assurance.

**Next check:** Check official published TMLR version and compare changed relevant sections before citing final status; prioritize competitive downstream validation and primary sources for claim-leading empirical effects.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2501.16496v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2501.16496v1) |
| `retrieved_at` | 2026-11-14T17:54:59.286205Z |
| `attempted_at` | 2026-11-14T17:54:58.880397Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independent archive capture was checked in this bounded round; exact local bytes and pinned version URLs where available are retained, without claiming archived immutability. |
| `sha256` | 9a50cdc6b9f2ba3687339453804acb9519525941198c14d07765aaecbb1436d2 |
| `byte_length` | 2409360 |
| `mime_type` | application/pdf |
| `published_on` | 2025-01-27 |
| `version_claim` | arXiv:2501.16496v1, 27 Jan 2025. |
| `locator_basis` | PDF page numbers count title page as page 1; section headings as printed. |
| `capture_path` | .source-captures/synthesis-9a50cdc6b9f2ba3687339453804acb9519525941198c14d07765aaecbb1436d2.pdf |

<a id="r3_circuits_06"></a>
### r3_circuits_06

**Source:** `paulo_automaticallyinterpreting_2024`. **Theme:** circuit_evidence. **Reading:** Abstract only. **Coverage effect:** `none`.

**Edition match:** `same_record`. Read abstract and submission history: v1 17Oct2024, v2 4Dec2024, v3 6Aug2025. Metadata-page current abstract may differ from the pinned PDF abstract; no equivalence assumed.

**Inspected scope:** Current arXiv abstract and version/submission history; no complete paper read for this metadata representation.

**Locators:** Title, Abstract, Submission history

**Visual check:** No paper figures in this representation.

**Findings:**

- Read abstract and submission history: v1 17Oct2024, v2 4Dec2024, v3 6Aug2025. Metadata-page current abstract may differ from the pinned PDF abstract; no equivalence assumed.

**Counterevidence / alternative:** No independent empirical corroboration is supplied by a metadata page for the same work.

**Limits:** Metadata/abstract access is not full-text reading; version-page claims do not prove equivalence across editions.

**Replication:** `not_performed`. **Numerical check:** Dates and version strings checked; no empirical quantities audited.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Version provenance for the related scoped reading; not counted as another source family or complete-text read.

**Next check:** Use the pinned PDF event for scoped empirical claims; adjudicate edition discrepancies explicitly.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/abs/2410.13928) |
| `final_url` | [Source](https://arxiv.org/abs/2410.13928) |
| `retrieved_at` | 2026-11-14T17:53:22.974992Z |
| `attempted_at` | 2026-11-14T17:53:22.830117Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independent archive capture was checked in this bounded round; exact local bytes and pinned version URLs where available are retained, without claiming archived immutability. |
| `sha256` | ec097841329e67a2c82b627989077a45e50bfa4f6434bac36247260cd20fed17 |
| `byte_length` | 43598 |
| `mime_type` | text/html |
| `published_on` | 2025-08-06 |
| `version_claim` | arXiv abstract page identifies current v3, last revised6Aug2025. |
| `locator_basis` | arXiv abstract-page title/abstract/submission history. |
| `capture_path` | .source-captures/synthesis-ec097841329e67a2c82b627989077a45e50bfa4f6434bac36247260cd20fed17.html |

<a id="r3_circuits_07"></a>
### r3_circuits_07

**Source:** `lan_sparseautoencoders_2024`. **Theme:** circuit_evidence. **Reading:** Abstract only. **Coverage effect:** `none`.

**Edition match:** `related_edition`. Read current title/abstract and submission history; v1 9Oct2024, current v4 21May2025. Confirms title drift; does not resolve which edition the authoritative record should represent.

**Inspected scope:** Current arXiv abstract and version/submission history; no complete paper read for this metadata representation.

**Locators:** Title, Abstract, Submission history

**Visual check:** No paper figures in this representation.

**Findings:**

- Read current title/abstract and submission history; v1 9Oct2024, current v4 21May2025. Confirms title drift; does not resolve which edition the authoritative record should represent.

**Counterevidence / alternative:** No independent empirical corroboration is supplied by a metadata page for the same work.

**Limits:** Metadata/abstract access is not full-text reading; version-page claims do not prove equivalence across editions.

**Replication:** `not_performed`. **Numerical check:** Dates and version strings checked; no empirical quantities audited.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Version provenance for the related scoped reading; not counted as another source family or complete-text read.

**Next check:** Use the pinned PDF event for scoped empirical claims; adjudicate edition discrepancies explicitly.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/abs/2410.06981) |
| `final_url` | [Source](https://arxiv.org/abs/2410.06981) |
| `retrieved_at` | 2026-11-14T17:53:23.116787Z |
| `attempted_at` | 2026-11-14T17:53:22.979005Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independent archive capture was checked in this bounded round; exact local bytes and pinned version URLs where available are retained, without claiming archived immutability. |
| `sha256` | e4366ea3b01e91c2664b7808fa3dc08258d4f6974b732c425d76d60ff71f5961 |
| `byte_length` | 45037 |
| `mime_type` | text/html |
| `published_on` | 2025-05-21 |
| `version_claim` | arXiv abstract page identifies v4, last revised21May2025. |
| `locator_basis` | arXiv abstract-page title/abstract/submission history. |
| `capture_path` | .source-captures/synthesis-e4366ea3b01e91c2664b7808fa3dc08258d4f6974b732c425d76d60ff71f5961.html |

<a id="r3_circuits_08"></a>
### r3_circuits_08

**Source:** `sharkey_openproblemsmechanistic_2025`. **Theme:** circuit_evidence. **Reading:** Abstract only. **Coverage effect:** `none`.

**Edition match:** `same_record`. Read title/abstract and submission history. No separate journal edition or peer-review status inferred from this page.

**Inspected scope:** Current arXiv abstract and version/submission history; no complete paper read for this metadata representation.

**Locators:** Title, Abstract, Submission history

**Visual check:** No paper figures in this representation.

**Findings:**

- Read title/abstract and submission history. No separate journal edition or peer-review status inferred from this page.

**Counterevidence / alternative:** No independent empirical corroboration is supplied by a metadata page for the same work.

**Limits:** Metadata/abstract access is not full-text reading; version-page claims do not prove equivalence across editions.

**Replication:** `not_performed`. **Numerical check:** Dates and version strings checked; no empirical quantities audited.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Version provenance for the related scoped reading; not counted as another source family or complete-text read.

**Next check:** Use the pinned PDF event for scoped empirical claims; adjudicate edition discrepancies explicitly.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/abs/2501.16496) |
| `final_url` | [Source](https://arxiv.org/abs/2501.16496) |
| `retrieved_at` | 2026-11-14T17:53:23.228101Z |
| `attempted_at` | 2026-11-14T17:53:23.120669Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independent archive capture was checked in this bounded round; exact local bytes and pinned version URLs where available are retained, without claiming archived immutability. |
| `sha256` | 207c290ebbb89faa153245d28afe6077841ec74f098cd37326518b7be67bf940 |
| `byte_length` | 45206 |
| `mime_type` | text/html |
| `published_on` | 2025-01-27 |
| `version_claim` | arXiv abstract page lists only v1, submitted27Jan2025. |
| `locator_basis` | arXiv abstract-page title/abstract/submission history. |
| `capture_path` | .source-captures/synthesis-207c290ebbb89faa153245d28afe6077841ec74f098cd37326518b7be67bf940.html |

<a id="r3_audits_01"></a>
### r3_audits_01

**Source:** `longpre_inhouseevaluation_2025`. **Theme:** deferred_audits. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact ICML 2025 proceedings/PMLR267 longpre25a final PDF, matching canonical title, authors and proceedings record. It is not treated as interchangeable with the differently titled arXiv preprint.

**Inspected scope:** Final ICML/PMLR 267 PDF pp1–9 (abstract and all main §§1–7); Appendix A pp18–20; Appendix B.1 introductory/example explanations p20, B.2–B.3 and Table A1 pp22–25; Appendix C.1–C.4 pp25–28, including Table A2. Figure A7 p26 visually inspected. The table of contents p17, references pp9–16, visual example cards p21, and Appendix D pp29–31 were not read in full; this is selected-section review.

**Locators:** Final proceedings §§3–4.3, PDFpp4–8; §5 alternatives and §6 future work,pp8–9; Appendix A.1,A.4,pp18–20,FigureA3; Appendix B.1,p20 and B.2/TableA1,pp22–23; Appendix C.1–C.4,pp25–28; FigureA7,p26; TableA2,p27 is explicitly a January2025 snapshot

**Visual check:** FigureA7 rendered and inspected at PDFp26: schematic protection/access/infrastructure categories, not a measured effect. Other selected figure captions and TableA1/TableA2 text were read from pdftotext; the Figure2 form, FigureA3 spectrum and illustrative cards were not independently inspected visually.

**Findings:**

- The final paper supplies concrete candidate mechanisms: versioned/session-linked flaw reports, statistical recurrence evidence for probabilistic failures, conduct-based good-faith rules, provider legal commitments plus moderation-exempt access/appeals, and routing of transferable flaws across supply-chain stakeholders (§4). These are substantive design contributions rather than empirical estimates of impact.
- Appendix A.1 defines third-party evaluation as lacking a direct contractual or obligatory relationship to the provider, distinct from contracted second-party evaluation. A.4 makes independence a spectrum with blurred boundaries, so external/third-party should not be treated as automatic independence certificates.
- Appendix B.1 explicitly says the two past-case report cards illustrate what could have been filed, not reports produced by an implemented coordination system. The motivating DEFCON event is described secondhand here and is not independently re-audited.
- Section5 acknowledges resource/administration trade-offs; §6 leaves responsibility disagreements, the effectiveness of mitigation/remediation after disclosure, and coordination-center governance unresolved. FigureA7 is a proposal illustration, not an observed guarantee of protection or harmlessness.

**Counterevidence / alternative:** Software-vulnerability-disclosure analogies and reported past flaw discoveries support feasibility arguments but do not establish effects for the full GPAI proposal. Legal promises bind the promising provider to a limited policy and do not eliminate all third-party or criminal-law risks; the template itself expects applicable-law compliance. Provider vetting can constrain participation, even where conduct-based selection is preferred. The assertion that these costs become minimal or have substantial returns is not a measured cost-benefit estimate.

**Limits:** Original round2 capture is reused unchanged; the original receipt logs a single access-event timestamp as retrieved_at and that existing timestamp is also carried as attempted_at, following its capture convention. No fresh retrieval is claimed. Server MIME was application/octet-stream; bytes have PDF signature and parse as a31-page PDF. Reading is partial, including gaps specified in scope. TableA2 legal/status claims were not verified against operative primary law; safe-harbor diagrams cannot establish legal immunity. No adopted coordination-center evidence or report-processing outcome data were obtained.

**Replication:** `not_performed`. **Numerical check:** None. Documentary counts are attributed to the paper and were not independently recounted against its underlying evidence; no experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C38](claims.md#c38), [C39](claims.md#c39), [C40](claims.md#c40)

**Relevance rationale:** Supplies bounded primary evidence for existing institutional claims and the proposed claim(s); inclusion is not independent corroboration or observed audit effectiveness.

**Next check:** Read AppendixD/provider-policy inventory and visual example cards; verify any cited operative access policy or legal protection in its dated primary form before describing current protection, adoption or effectiveness. For effects, obtain report→response→mitigation records, not only proposal text.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/longpre25a/longpre25a.pdf) |
| `final_url` | [Source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/longpre25a/longpre25a.pdf) |
| `retrieved_at` | 2026-11-14T17:15:17.944907+00:00 |
| `attempted_at` | 2026-11-14T17:15:17.944907+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact primary-edition URLs and local bytes are retained; independent archival preservation is not claimed. |
| `sha256` | 921e087197d00bd2d15bd5a9ee6dcf6fbaf0cbb3cc9a9d849f5fe5ce3bc765b0 |
| `byte_length` | 5959117 |
| `mime_type` | application/pdf |
| `published_on` | 2025 |
| `version_claim` | Final ICML2025/PMLR267 proceedings PDF,31pages |
| `locator_basis` | PDF viewer pages1–31 have printed article-local pages1–31; proceedings bibliography range81728–81758 is not used as a PDF-page locator. |
| `capture_path` | .source-captures/synthesis-921e087197d00bd2d15bd5a9ee6dcf6fbaf0cbb3cc9a9d849f5fe5ce3bc765b0.pdf |

<a id="r3_audits_02"></a>
### r3_audits_02

**Source:** `mokander_auditinglargelanguagemodels_2024`. **Theme:** deferred_audits. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Publisher DOI PDF bears AI and Ethics (2024)4:1085–1115, matching canonical DOI/title/authors. It prints online publication30 May2023; 2024 is the issue year, not an inferred manuscript revision date.

**Inspected scope:** Final AI and Ethics issue PDF pp1–22, printed pp1085–1106: abstract and every narrative section §§1–6; Appendix 1 methodology in full, acknowledgments, contributions/funding/data/conflict/license statements. Figures 1–2 (viewer pp10,17; printed pp1094,1101) rendered and visually inspected. The remaining bibliography-only pages23–31 (printed pp1107–1115) were not read; accordingly this event remains Selected sections rather than a full-document certification.

**Locators:** §3.2,printedpp1091–1093 (viewerpp7–9),claims1–7; §4.1–4.5,printedpp1094–1101 (viewerpp10–17),Figures1–2; §5.1–5.3,printedpp1102–1103 (viewerpp18–19); §6,pp1103–1105; Appendix1,pp1105–1106 (viewerpp21–22)

**Visual check:** Both figures rendered and visually inspected: Figure1 specifies governance/model/application scopes, observables and methods; Figure2 explicitly routes model limitations, training/testing information, impact reports and output/environmental logs among audit levels. They depict the proposed architecture, not observed implementation.

**Findings:**

- The proposed governance/model/application layers form a linked evidence process: model limitations should inform application design; application impact/output logs should feed model revision; governance audits should test that feedback mechanisms exist (§4.5,Figure2). This adds an affirmative pathway rather than treating audit reports as inherently empty.
- The blueprint calls for external yet collaborative audits and distinguishes access needs: governance includes organizational records/personnel; model audits technical/model/training-data access; application testing can use lower-level output access (§§3.2,4.2–4.4). It also acknowledges capture, cost and expertise trade-offs.
- Appendix1 reports a systematised126-document review, gap analysis, procedural design, and over20 semi-structured interviews/feedback with researchers, auditors, frontier-lab developers and policymakers. This is a literature-/stakeholder-informed design study, not an evaluated implementation of the complete layered audit or a causal estimate of compliance/harm effects.
- Section4.3–4.4 locates unjust discrimination and conversational appropriateness in application context: general benchmark performance cannot establish fairness across deployment settings. §5.1 foregrounds construct validity and mutually incompatible operationalizations; §5.2 recognizes institutional backing as unresolved; §5.3 preserves political reform beyond technology-level audits.

**Counterevidence / alternative:** The authors make strong claims of necessity/feasibility and effective assurance, but these remain design inferences from prior literature and stakeholder consultation. They explicitly do not establish who audits whom or enforce post-audit action. Collaborative access may improve technical assessment while weakening independence through client dependence. §5.3 includes contestable political judgments about capability restraint and opportunity costs; those judgments are not adopted here as empirical conclusions.

**Limits:** All accessible narrative text and the meaningful methodology appendix were read, but the remaining bibliography-only pages23–31 were not, so no full-record depth upgrade is proposed. Cited primary studies/interview records were not audited or reproduced. Institution choice, post-audit action and current law are outside this paper’s implemented evidence. Reused round2 bytes and original single logged access-event timestamp are retained; no fresh download or historical revision is asserted.

**Replication:** `not_performed`. **Numerical check:** None. Documentary counts are attributed to the paper and were not independently recounted against its underlying evidence; no experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C54](claims.md#c54)

**Relevance rationale:** Supplies bounded primary evidence for existing institutional claims and the proposed claim(s); inclusion is not independent corroboration or observed audit effectiveness.

**Next check:** Inspect the references and underlying studies/transcripts only where needed to support the publication’s chosen claim. Seek actual connected audit records, decisions and follow-up effects; adjudicate context-specific fairness constructs and political trade-offs separately from technical compliance.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://link.springer.com/content/pdf/10.1007/s43681-023-00289-2.pdf) |
| `final_url` | [Source](https://link.springer.com/content/pdf/10.1007/s43681-023-00289-2.pdf?error=cookies_not_supported&code=2a52c110-16ae-41a4-bc99-cac7daad869b) |
| `retrieved_at` | 2026-11-14T17:15:17.946203+00:00 |
| `attempted_at` | 2026-11-14T17:15:17.946203+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact primary-edition URLs and local bytes are retained; independent archival preservation is not claimed. |
| `sha256` | a03b71802c1e742a223f39d8fabcd363e75b53f217e7abe72282a46c45b3f2f1 |
| `byte_length` | 2650666 |
| `mime_type` | application/pdf |
| `published_on` | 2023-05-30 |
| `version_claim` | Final publisher issue PDF: AI and Ethics(2024)4:1085–1115; published online30May2023 |
| `locator_basis` | Viewer page1=printed1085; add1084 to viewer-page numbers through31=1115. |
| `capture_path` | .source-captures/synthesis-a03b71802c1e742a223f39d8fabcd363e75b53f217e7abe72282a46c45b3f2f1.pdf |

<a id="r3_audits_03"></a>
### r3_audits_03

**Source:** `homewood_thirdpartycompliance_2025`. **Theme:** deferred_audits. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Explicit arXiv:2505.01643v2 [cs.CY],4 Jul2025, matching the v2 source-review lead for the canonical preprint. The live unversioned URL is not assumed to freeze v2.

**Inspected scope:** arXiv v2 PDF p1 (abstract/date/version), pp5–9 (§1, §2.1–2.2 in full, opening §3 and opening §3.1), pp14–18 (end §3.2; §3.3 and Tables3–4; §3.4 in full; beginning §3.5 through key-area option), pp22–23 (alternatives, §5 conclusion in full, acknowledgments and opening references). Executive summary/options tables pp3–4, reviewer comparisons/structures pp10–13, remaining action/timing/options discussion pp19–21, and references pp24–27 were not read in full.

**Locators:** arXivv2 §1,pp5–6 (scope and terminology); §2.1–2.2,pp6–9 (benefits and challenges); §3.2,pp14; §3.3,pp14–16 and Tables3–4,pp15,17; §3.4,pp16–18; opening §3.5,p18; alternatives and §5,pp22–23

**Visual check:** No separate figure/table image inspection. Tables3–4 were read in the PDF text extraction: mock objective/controls and generic/example maturity framework, not observed graded company results. Layout-dependent details were not used as evidence.

**Findings:**

- The paper studies voluntary third-party review of adherence to a company’s own frontier safety framework, explicitly distinguishing that from audits of AI systems and reviews of the framework’s adequacy (§1). A finding of compliance therefore does not establish that the framework or model is safe.
- Section3.3 gives concrete alternative assessment designs: grade commitments directly; operationalize objectives into implemented controls then test a random set; or compare observed process maturity with specified targets. Table3 is explicitly a mock objective with five mock controls, and Table4 a generic framework plus constructed forecasting example, not a completed company assessment.
- The proposed assurance chain depends on evidence and decisions: structural policies alone have limited assurance; logs/communications, operational interviews/walkthroughs and system tests can expose different gaps (§3.2). §2.2 identifies false positives/negatives, client-retention conflicts, vague commitments and employee self-censorship as failure mechanisms.
- External disclosure ranges from none to detailed reports with planned follow-up; greater detail can aid accountability but has security/privacy and chilling risks (§3.4). The key-area response option in §3.5 can tie noncompliance to delayed actions, but company selection of agreeable findings can weaken it. Internal reviews and compliance management systems are proposed complements (§4 alternatives,p22).

**Counterevidence / alternative:** The proposed operationalization and reporting mechanisms are useful even without measured outcomes, but a vague or weak framework can be followed faithfully. Self-censorship, review shopping/conflicts, rigid controls, secrecy and company discretion over follow-up can yield false assurance. Broader access can improve findings while increasing security, confidentiality and coordination burdens. The paper’s assurance/compliance benefit expectations are extrapolations from other-sector studies and design reasoning, not direct frontier-AI control-effect estimates.

**Limits:** Selected sections only, with explicit gaps in scope. No actual frontier-framework compliance review, underlying company review report, control test sample, adoption dataset or outcome experiment was inspected. The paper’s cited evidence from other sectors and current company policies was not independently rechecked. The positive-effect language in the abstract/conclusion must not be promoted into a measured finding.

**Replication:** `not_performed`. **Numerical check:** None. Documentary counts are attributed to the paper and were not independently recounted against its underlying evidence; no experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C41](claims.md#c41), [C55](claims.md#c55)

**Relevance rationale:** Supplies bounded primary evidence for existing institutional claims and the proposed claim(s); inclusion is not independent corroboration or observed audit effectiveness.

**Next check:** Obtain dated actual review reports and underlying scope/access/assessment/disclosure/remediation evidence before asserting adoption or effects. Compare compliance with a separately argued adequacy standard; preserve an indeterminate result where a commitment cannot be operationalized rather than convert ambiguity into a pass.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2505.01643v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2505.01643v2) |
| `retrieved_at` | 2026-11-14T17:55:36.308460+00:00 |
| `attempted_at` | 2026-11-14T17:55:35.987900+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact primary-edition URLs and local bytes are retained; independent archival preservation is not claimed. |
| `sha256` | 3010a0f6d8806cf727514bd2ae70d1f03ee80086639a1c09878fafde3c12db65 |
| `byte_length` | 712778 |
| `mime_type` | application/pdf |
| `published_on` | 2025-07-04 |
| `version_claim` | arXiv:2505.01643v2 [cs.CY],4Jul2025 |
| `locator_basis` | Viewer pages1–27 include title page,contents and executive summary; printed pages5–27 match viewer numbering in inspected text. |
| `capture_path` | .source-captures/synthesis-3010a0f6d8806cf727514bd2ae70d1f03ee80086639a1c09878fafde3c12db65.pdf |

<a id="r3_fairness_01"></a>
### r3_fairness_01

**Source:** `huang_collectiveconstitutional_2024`. **Theme:** fairness_values. **Reading:** Full text. **Coverage effect:** `none`.

**Edition match:** `related_edition`. All 23 pages of arXiv:2406.07814v1 were read. The manuscript carries FAccT2024 title/authors, DOI10.1145/3630106.3658979 and a 23-page ACM reference, but the publisher object was not obtained for a text identity check. The bibliography cites the published proceedings DOI as well as arXiv; conservatively do not upgrade its canonical proceedings reading label from this manuscript alone.

**Inspected scope:** Complete arXiv v1 text: main pp1–10; references pp10–12; appendices A.1–A.10 pp12–23 including public/standard constitutions, aggregation examples and qualitative response examples. Main quantitative charts on p7, Table1 p8 and participant interface p13 were visually inspected; other charts are read through captions and accompanying text, not digitized.

**Locators:** arXiv v1 pp3–6 §§3.1–3.4; pp7–8 §4.3, Figures4–5, Table1; pp9–10 §§5–7; p12 A.2; p13 A.3/Figures6–7; pp14–23 A.4–A.10

**Visual check:** Rendered PDFp7 confirms Public below Standard on all nine BBQ social dimensions and all five OpinionQA ideology scores; p8 confirms Table1 labels/values and narrative wording; p13 confirms screenshot minimum of40 votes.

**Findings:**

- The paired Public/Standard training controls pretraining data, helpfulness human feedback, hyperparameters, steps, seeds and harmlessness prompt mixes; constitution is the stated difference. Public model has lower BBQ bias across all nine tested dimensions.
- Public-input constitution is feasible but includes consequential investigator choices:21 seeds (7 inspired by Standard), moderation, two opinion clusters, group-aware consensus product,95-idea cutoff, deduplication and rewriting.
- Public model has lower OpinionQA representativeness across all five U.S. ideology groups. Authors lack a direct adherence metric and explicitly limit democratic-legitimacy/global-public interpretations.
- The paper contains source-internal discrepancies in vote summaries/instructions and an Elo label/interpretation mismatch; these are unresolved rather than silently corrected.

**Counterevidence / alternative:** Positive BBQ results coexist with worse OpinionQA distribution alignment; equal opportunity to vote and high consensus do not establish all affected groups are represented. Authors do not resolve conflicting principles or evaluate downstream societal impact.

**Limits:** One controlled pair of constitutions/models based on a screened U.S. participant sample, not a global public or a direct measure of adherence, consent or impact. Screen included news/discussion familiarity; demographic sampling omitted race. Full manuscript reading does not equal final-edition identity, source-code checking, statistical equivalence testing or experimental replication.

**Replication:** `not_performed`. **Numerical check:** Documentary arithmetic only: 38,252/1,002=38.1756 votes/person, while mainp4 says average34. Screenshotp13 requires40 votes for completion; mainp4 requires30 before adding a statement. These are different stages and are not treated as an error. Figure5 Public scores .49/.51/.53/.55/.54 versus Standard .52/.54/.56/.57/.57; these confirm 2–3-point differences. Table1 MMLU72.3/72.4 and GSM8K85.6/85.2 are nearby observed scores, not an equivalence test. Table1 Harmfulness row and harmlessness paragraph end with a 'more helpful' interpretation; no Elo direction/equivalence promoted.

**Relevance:** `claim_evidence`. **Claim links:** [C57](claims.md#c57)

**Relevance rationale:** Adds positive evidence and counterevidence about public-input alignment without equating participation with representative public consent.

**Next check:** Compare the exact publisher edition, then inspect code/data or author errata for vote totals,30/40 instruction difference and Elo labels before using those quantities. For publication leading claims assess subgroup coverage, direct adherence and real-use impact.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2406.07814v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2406.07814v1) |
| `retrieved_at` | 2026-11-14T17:53:30.751631Z |
| `attempted_at` | 2026-11-14T17:53:30.223576Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URL retained. Independent archival preservation not claimed. |
| `sha256` | bf59c3f9a5c569b7c29063a24803128f7c3c8228790fa451e838cd1536cf9d15 |
| `byte_length` | 2767196 |
| `mime_type` | application/pdf |
| `published_on` | 2024-06-12 |
| `version_claim` | arXiv:2406.07814v1; FAccT2024-formatted author manuscript |
| `locator_basis` | PDF viewer pages1–23; paper has no sequential printed page numbers. Exact v1 header is on PDFp1. |
| `capture_path` | .source-captures/synthesis-bf59c3f9a5c569b7c29063a24803128f7c3c8228790fa451e838cd1536cf9d15.pdf |

<a id="r3_fairness_02"></a>
### r3_fairness_02

**Source:** `swamy_minimaximalistapproach_2024`. **Theme:** fairness_values. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact arXiv:2401.04056v1 matches the arXiv identifier and preprint type in the current bibliography. Subsequent ICML/PMLR final text was not compared; this is not a claim to have read that final edition.

**Inspected scope:** Main pp1–10 including §3 definitions, Theorem3.3 statement and main-text proof sketch, Theorem3.4 counterexample, theoretical/practical algorithms and experimental/task discussion; AppendixA.7 contextual definition p23. Appendix proofs A.1–A.6, contextual algorithms continuation p24 and appendicesB–D not comprehensively read. Graph values not digitized.

**Locators:** arXiv v1 pp4–6 §§3.1–3.3, Definition3.2, Theorems3.3–3.4; p7 §3.4/Algorithms1–2; pp8–10 §§4–5; p23 AppendixA.7

**Visual check:** No independent visual inspection of plot values; read figure captions and main-text descriptions. No headline experimental rates are extracted.

**Findings:**

- Minimax Winner can represent cyclic/intransitive pairwise preference structure that a single scalar reward ordering cannot; SPO reduces symmetric game solving to single-agent no-regret self-play.
- Theoretical Theorem3.3 concerns averaged iterates; practical Algorithm2 returns best iterate on validation data, so its empirical implementation is not identical to the theorem statement.
- The paper reports continuous-control results with constructed stochastic/intransitive/non-Markovian preference functions; language modeling and recommendation are explicitly future-domain tests in §5.

**Counterevidence / alternative:** The paper is a constructive alternative to scalar reward aggregation; it supplies no guarantee that elicited preferences, population weights or resulting distributions are legitimate or fair to demographic groups. Improvements over a reward model are scoped to the examined algorithms/tasks.

**Limits:** Guarantees depend on a supplied antisymmetric preference oracle, convex/compact policy class and no-regret updates, and concern an average policy. Practical Algorithm2 uses a finite queue and validation-selected iterate. Continuous-control/synthetic preference experiments are not public deliberation or language-model demographic-impact evidence.

**Replication:** `not_performed`. **Numerical check:** No experiment reproduced; theoretical bound and proof sketch inspected as text rather than independently verified in all appendix cases. No numerical performance claim admitted.

**Relevance:** `claim_evidence`. **Claim links:** [C58](claims.md#c58)

**Relevance rationale:** New argument about plural preference representation; does not turn a social-choice solution concept into a fairness certificate.

**Next check:** Read full appendix proofs and exact ICML final edition; test preference estimation/aggregation assumptions separately from optimization and distinguish average-iterate guarantees from returned practical policy.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2401.04056v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2401.04056v1) |
| `retrieved_at` | 2026-11-14T17:53:31.950204Z |
| `attempted_at` | 2026-11-14T17:53:30.888859Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URL retained. Independent archival preservation not claimed. |
| `sha256` | a8c9edd12526b5e429bd34203014a477e6e632d92f3709e00bf7792198cdabb3 |
| `byte_length` | 3123305 |
| `mime_type` | application/pdf |
| `published_on` | 2024-01-08 |
| `version_claim` | arXiv:2401.04056v1 |
| `locator_basis` | PDF and printed pages coincide1–28; selected AppendixA.7 begins p23. |
| `capture_path` | .source-captures/synthesis-a8c9edd12526b5e429bd34203014a477e6e632d92f3709e00bf7792198cdabb3.pdf |

<a id="r3_fairness_03"></a>
### r3_fairness_03

**Source:** `huang_trustllm_2024`. **Theme:** fairness_values. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact PDF linked by canonical ICML/PMLR235 huang24x publisher page; title includes Position: TrustLLM, with proceedings identifier235 and author list. Source headers label it PMLR2024. HTTP content-type was application/octet-stream, but retained bytes are a PDF and extracted successfully; MIME here is detected application/pdf.

**Inspected scope:** Publisher PDFp1 abstract, p5 benchmark figure/caption and discussion opening, complete AppendixF assessment of fairness pp74–79 including stereotype agreement/recognition/query tasks, salary association test, preference dataset/prompts/metric, Tables19–25. Other dimensions, main summary and remainder of105-page PDF not comprehensively read. Publisher metadata page was checked for PDF identity and date.

**Locators:** PMLR235 PDFp1, p5 Figure1/caption; AppendixF.1 pp74–76, Tables19–22; AppendixF.2 pp76–78/Table23; AppendixF.3 pp78–79/Tables24–25

**Visual check:** Rendered PDFp79 visually confirms Table25 category scores and Total columns. Other fairness tables read through PDF text; no graph digitization.

**Findings:**

- Stereotype fairness is separately measured as agreement rate (ChatGPT extraction), recognition accuracy, and refusal to answer stereotype queries (Longformer classification).
- Salary classification examines sex/race association using chi-square tests; paper itself warns Oasst high p-values may arise from predictions little better than random and do not imply greater fairness.
- Preference fairness is explicitly a normative choice: neutrality/refusal on each subjective forced-choice question; operational metric is Longformer RtA. This differs from population preference alignment or group outcome parity.
- Reported benchmark positives include low stereotype agreement and high stereotype-query refusal for several models, while recognition accuracy and salary associations reveal distinct weaknesses.

**Counterevidence / alternative:** TrustLLM itself reports positives and over-refusal risks, and acknowledges that a random predictor can pass one association metric. Neutrality-by-refusal is not interchangeable with responsiveness to plural public preferences. Table25 category denominator needs reconciliation before quantitative use.

**Limits:** Historical model suite. Fairness tasks rely on CrowS-Pairs, StereoSet, Do-Not-Answer, Adult-inspired synthetic salary prompts, and author-written subjective choices; ChatGPT answer extraction and Longformer refusal detection are proxies. Shared datasets and judgment conventions create dependencies with other suites. No sample representativeness, causal impact or universal fairness established.

**Replication:** `not_performed`. **Numerical check:** Table25 denominator inconsistency: §F.3 states120 questions=80 ideology+40 culture/lifestyle, but Mistral plain1.000/.800 has Total.867 (stated weights imply.933); GPT4 forced.100/.025 has Total.050 (stated weights imply.075). Both totals match reversed40/80 weighting. Exact underlying dataset/aggregation remains unchecked, so no corrected headline rate asserted. Table23 p-values are significance tests, not fairness effect sizes; absence of significance does not establish absence of bias.

**Relevance:** `claim_evidence`. **Claim links:** [C59](claims.md#c59)

**Relevance rationale:** Admits final-edition methods and a source-internal arithmetic lead, not a generic trustworthiness ranking.

**Next check:** Inspect dataset and exact evaluation/aggregation code for F.3 category counts, Longformer error rates and handling of refusals. Check effect sizes/contingency counts before any salary fairness ranking.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24x/huang24x.pdf) |
| `final_url` | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24x/huang24x.pdf) |
| `retrieved_at` | 2026-11-14T17:56:00.294799Z |
| `attempted_at` | 2026-11-14T17:55:59.741473Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URL retained. Independent archival preservation not claimed. |
| `sha256` | 271df3ae5a8550838ba357392eec39f58617ff1952e6e0390dd802ad5784d9b5 |
| `byte_length` | 2560872 |
| `mime_type` | application/pdf |
| `published_on` | 2024-07-08 |
| `version_claim` | ICML2024/PMLR235 final publisher PDF; Position: TrustLLM |
| `locator_basis` | PDF page numbers1–105 coincide with internal printed1–105; PMLR metadata bibliographic pages20166–20270 are not used as PDF locators. |
| `capture_path` | .source-captures/synthesis-271df3ae5a8550838ba357392eec39f58617ff1952e6e0390dd802ad5784d9b5.pdf |

<a id="r3_fairness_04"></a>
### r3_fairness_04

**Source:** `wang_decodingtrust_2023`. **Theme:** fairness_values. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact NeurIPS2023 Datasets and Benchmarks proceedings PDF, freshly retrieved this round; SHA256 equals the prior round object. This is a deeper fairness-specific reading of the same publication, not independent evidence.

**Inspected scope:** Main §9 text/Table4 previously checked; this event reads AppendixJ introductory passage PDFp86, J.1–J.4 pp87–89 including metric definitions, examples/captions and Tables41–44. Main and other appendices were not newly reread in full.

**Locators:** NeurIPS2023 AppendixJ.1 PDFp87/appendix printedp63; J.2–J.3 PDFp88/printedp64 Tables41–42; J.3–J.4 PDFp89/printedp65 Tables43–44

**Visual check:** Rendered PDFp89 visually confirms Table43 and Table44 captions/values; metric definitions read via extracted PDF text. Table41 comparison is documentary text inspection.

**Findings:**

- Fairness is demographic parity and equalized-odds difference on constructed income prediction, while data base-rate parity is controlled separately; sensitive attribute is in input.
- J.3 varies32-shot context base parity at fixed balanced200-sample test set and reports larger endpoint group gaps for highly biased demonstrations.
- J.4 reports lower gaps with balanced demonstrations, providing possible mitigation evidence; comparison of its zero-shot baseline with earlier rows needs sampling/test-condition clarification. A source error is not established and affected numerical remedy contrasts are omitted.

**Counterevidence / alternative:** The appendix includes mitigation as well as failures and higher GPT4 accuracy; its bounded demonstration effect does not prove general fairness or a necessary capability/safety tradeoff. Shared Adult task ancestry with TrustLLM is a dependency, not independent corroboration.

**Limits:** Each evaluation describes200 constructed Adult test samples with controlled target base rates, binary sex/race/age groupings and income threshold$50k; subgroup and label-conditioned denominators are not fully provided in the examined pages. Historical API checkpoints from prior C47 remain. Constructed gap changes are not population harm incidence, a universal capability/fairness tradeoff or modern-model comparison.

**Replication:** `not_performed`. **Numerical check:** J.1 prints signed differences without absolute-value notation; implementation convention and subgroup counts not checked. Table44 caption and J.4 say testbase parity.5, yet its zero-shot rows exactly repeat Table41 parity1.0 rows (GPT3.5:73.0/.46/.49; GPT4:85.5/.71/.95), not Table41 parity.5 rows (68.5/.31/.19;78.5/.47/.40). The text separately describes random test-sample selection, so distinct draws/cohorts are a possible explanation; code/data are needed to resolve condition, sampling or copied-row alternatives; omit condition-specific remedy numbers. Table43 GPT3.5 Mdpd falls.033→.026 at intermediate context parity, so 'larger always means larger' is not monotone for every reported cell.

**Relevance:** `claim_evidence`. **Claim links:** [C47](claims.md#c47), [C59](claims.md#c59)

**Relevance rationale:** Deepens C47 methods/denominators and contrasts fairness constructs for C59; leaves a concrete unresolved numerical lead.

**Next check:** Inspect exact release code/data and metric implementation, signed/absolute conventions, subgroup counts, sampling seeds and Table44 base-rate condition before any headline numerical mitigation claim. Retain C47 qualitative bound.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://proceedings.neurips.cc/paper_files/paper/2023/file/63cb9921eecf51bfad27a99b2c53dd6d-Paper-Datasets_and_Benchmarks.pdf) |
| `final_url` | [Source](https://proceedings.neurips.cc/paper_files/paper/2023/file/63cb9921eecf51bfad27a99b2c53dd6d-Paper-Datasets_and_Benchmarks.pdf) |
| `retrieved_at` | 2026-11-14T17:58:02.007143Z |
| `attempted_at` | 2026-11-14T17:58:00.449240Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URL retained. Independent archival preservation not claimed. |
| `sha256` | 0af07f4ded9e4d2c4ae1cc3ec5c765318d6e804a46211d206c1cbea9967dc8fe |
| `byte_length` | 42206195 |
| `mime_type` | application/pdf |
| `published_on` | 2023 |
| `version_claim` | NeurIPS2023 Datasets and Benchmarks final proceedings PDF |
| `locator_basis` | 108-page PDF includes24 main/reference pages before appendix; PDFp87=appendix printedp63, p88=64, p89=65. |
| `capture_path` | .source-captures/synthesis-0af07f4ded9e4d2c4ae1cc3ec5c765318d6e804a46211d206c1cbea9967dc8fe.pdf |

<a id="r3_fairness_05"></a>
### r3_fairness_05

**Source:** `bender_stochasticparrots_2021`. **Theme:** fairness_values. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. DOI-matched FAccT2021 paper mirror,14 pages with printed610–623. Not newly publisher-downloaded or text-compared against ACM. Its DOI/title/authors/pages identify the corpus work; no different-edition claim made.

**Inspected scope:** Selected contextual reading: §4.1 opening on dataset size and diversity PDFp4/printed613, §7 Paths Forward opening and first recommendations PDFp9/printed618; nearby environmental-cost discussion was skimmed and its borrowed numerical estimates were not audited. Inherited full-text label is preserved, not newly earned.

**Locators:** FAccT2021 §4.1 opening PDFp4/printed613; §7 opening PDFp9/printed618

**Visual check:** None; contextual prose only. No plotted or borrowed numeric claim verified.

**Findings:**

- The paper argues that large convenient Internet corpora need not represent diverse groups or interests and that curation/filtering choices alter whose voices remain.
- Paths Forward recommends documenting dataset selection goals, values and stakeholders, understanding how systems perform tasks and considering their place in sociotechnical systems rather than only leaderboard averages.

**Counterevidence / alternative:** These recommendations do not by themselves show a proposed participatory method or benchmark actually improves affected-group outcomes. They motivate questions and design criteria, rather than supply a comparative model effect.

**Limits:** Scholarly argument and cited examples predating present frontier systems; this event does not independently check the papers/estimates cited or quantify present incidence/impact. A normative motivation for impact-aware evaluation is not empirical corroboration of any new C57–C59 effect.

**Replication:** `not_performed`. **Numerical check:** No quantitative claim adopted and no experiments or source-paper estimates reproduced.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Explicit conceptual background on representation, data curation and situated impacts; no claim is forced merely to assign a synthesis role.

**Next check:** If an environmental, demographic or deployment-effect number is used, verify its original cited study, historical context and denominator; retain contextual role otherwise.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://s10251.pcdn.co/pdf/2021-bender-parrots.pdf) |
| `final_url` | [Source](https://s10251.pcdn.co/pdf/2021-bender-parrots.pdf) |
| `retrieved_at` | 2026-11-14T17:53:33.002823Z |
| `attempted_at` | 2026-11-14T17:53:32.685258Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and exact primary version URL retained. Independent archival preservation not claimed. |
| `sha256` | e283b37a14e894c105ca26003d8cf5447535e8a73423cd7f1001d7b46af6c1d6 |
| `byte_length` | 304472 |
| `mime_type` | application/pdf |
| `published_on` | 2021-03 |
| `version_claim` | FAccT2021 DOI10.1145/3442188.3445922; public mirror of14-page proceedings paper |
| `locator_basis` | PDFp1–14 correspond to proceedings printed610–623. |
| `capture_path` | .source-captures/synthesis-e283b37a14e894c105ca26003d8cf5447535e8a73423cd7f1001d7b46af6c1d6.pdf |

<a id="r3_public_01"></a>
### r3_public_01

**Source:** `exim_complianceplanomb_2024`. **Theme:** public_implementation. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical EXIM URL delivered an18-page PDF with September 24, 2024 revision history and v1.0 initial publication, consistent with cited2024 plan.

**Inspected scope:** All extracted text on PDF pp. 1–18, including cover, revision history, contents, governance, inventory, innovation, risk-management sections and Appendix A definitions; no linked underlying policies or successor plan.

**Locators:** v1.0 revision history p. 2; Purpose p. 4; Strengthening AI Governance pp. 5–9; AI Strategy pp. 11–13; Managing Risks pp. 14–16; Appendix A pp. 17–18

**Visual check:** None. Text extraction inspected; no rendered figure/table inspection or visual authentication. Narrative section text is the basis for findings.

**Findings:**

- Sept. 24, 2024 v1.0 self-reports an assembled governance body and FY24 updates to annual security training, CPIC/SDLC technology-review processes and IT Rules of Behavior, while its agency AI policy is described variously as drafted/developed and as still to formalize procedures.
- Existing technology reviews are described as a route to detect planned or existing AI and engage the governance body (p. 9); this specifies a trigger and responsible body, not observed referrals or outcomes.
- EXIM reports no rights- or safety-impacting use cases and no cases requiring waivers; additional criteria and waiver formalization remain prospective (pp. 15–16). AI strategy completion and baseline skills assessment are expected in FY25 (pp. 11,13).

**Counterevidence / alternative:** Specific reported policy updates are more than abstract commitments, but do not demonstrate that risk-review/waiver pathways were exercised; the reported absence of rights/safety cases limits tests of those pathways.

**Limits:** Agency self-report under historical M-24-10; not an independent implementation audit, high-impact test outcome, current policy check, or frontier-developer rule. No underlying CPIC/SDLC policies, meeting minutes, case files or M-25-21 successor plan reviewed. Mixed tenses in policy/governance descriptions prevent assuming every listed process was operational.

**Replication:** `not_performed`. **Numerical check:** None; no quantitative inference or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C60](claims.md#c60)

**Relevance rationale:** Supporting federal-agency-use comparator for institutional implementation and evidence boundaries; not direct evidence of frontier-model release governance.

**Next check:** Inspect dated underlying policies and actual review/termination or waiver records if making an implementation-effectiveness claim; retain historical comparator scope.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://img.exim.gov/s3fs-public/documents/EXIM%20Compliance%20Plan%20for%20OMB%20Memorandum%20M-24-10Final.pdf) |
| `final_url` | [Source](https://img.exim.gov/s3fs-public/documents/EXIM%20Compliance%20Plan%20for%20OMB%20Memorandum%20M-24-10Final.pdf) |
| `retrieved_at` | 2026-11-14T17:54:35.798084Z |
| `attempted_at` | 2026-11-14T17:54:35.135763Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary response bytes and URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 510ff923e6d41ee7b29d20047b0968410fdf8d8080433276d91e7fb6b4f180fe |
| `byte_length` | 446464 |
| `mime_type` | application/pdf |
| `published_on` | 2024-09-24 |
| `version_claim` | Version 1.0, Initial Publication September 24, 2024 |
| `locator_basis` | PDF viewer page numbers include cover and coincide with printed page numbers where shown. |
| `capture_path` | .source-captures/synthesis-510ff923e6d41ee7b29d20047b0968410fdf8d8080433276d91e7fb6b4f180fe.pdf |

<a id="r3_public_02"></a>
### r3_public_02

**Source:** `omb_m2521_2025`. **Theme:** public_implementation. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical WhiteHouse PDF URL delivered the25-page memorandum headed M-25-21, April 3, 2025; February in URL path is not used as publication date.

**Inspected scope:** All extracted text on PDF pp. 1–25, including main memorandum, Appendix §§1–8, footnotes, high-impact definitions/categories and consolidated actions table. Operative narrative clauses, rather than the summary table, support timing/obligation paraphrases.

**Locators:** Overview p. 1; Appendix §1 pp. 4–5; Appendix §§3(a)(i)(F),3(b)(v) pp. 11–13; Appendix §§4(a)–(b) pp. 14–17; §5 pp. 18–20; §6 pp. 21–22

**Visual check:** None. Text extraction inspected; no rendered figure/table inspection or visual authentication. Narrative section text is the basis for findings.

**Findings:**

- The April 3, 2025 memorandum expressly rescinds and replaces M-24-10. It governs covered agencies’ own AI use, with exclusions including national security systems; it expressly does not create rights or obligations for the public (p. 4 fn. 4).
- High-impact requires output to serve as a principal basis for a consequential decision/action; human oversight does not itself remove that classification (pp. 14,19). The prescribed process links determination, documented testing/impact assessment, nondeveloper review within the agency, signed risk acceptance, monitoring, and discontinuation of noncompliant functionality (pp. 14–17).
- A reviewer of an impact assessment must be within the agency and uninvolved in development (p. 16 §4(b)(ii)(F)); this is a specified separation of duties, not an outside-institution audit. The memo permits qualified pilot exemptions and system/context-specific CAIO waivers, with tracking and disclosure requirements (p. 15).

**Counterevidence / alternative:** Defined scope, principal-basis trigger, pilot exemptions, waivers and conditional feasibility/appropriateness clauses bound any universal testing or cessation claim. Black-box alternatives, including vendor-returned results, are permitted when source/model/data access is unavailable (§4(b)(i)).

**Limits:** Normative design in the April 3, 2025 edition, not proof of compliance, effectiveness or current legal status on retrieval date. No later amendment, implementation inventory, waiver register or agency case file audited. Extracted consolidated table was read, not visually checked; no deadlines are rederived from its compressed rows.

**Replication:** `not_performed`. **Numerical check:** None; no quantitative inference or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C61](claims.md#c61)

**Relevance rationale:** Supporting federal-agency-use comparator for institutional implementation and evidence boundaries; not direct evidence of frontier-model release governance.

**Next check:** For a publication asserting current duties, check dated subsequent instruments; for actual control effectiveness, inspect completed case-specific tests, reviews, risk-acceptance signatures, waiver justifications and remediation records.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf) |
| `final_url` | [Source](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf) |
| `retrieved_at` | 2026-11-14T17:54:35.577694Z |
| `attempted_at` | 2026-11-14T17:54:35.136546Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary response bytes and URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 0aab0aa4eaeac969ed93894d3940c5dc9d0b7377048171b164a439e8b9e49813 |
| `byte_length` | 2629748 |
| `mime_type` | application/pdf |
| `published_on` | 2025-04-03 |
| `version_claim` | M-25-21, April 3, 2025 |
| `locator_basis` | PDF viewer page numbers include cover and coincide with printed page numbers where shown. |
| `capture_path` | .source-captures/synthesis-0aab0aa4eaeac969ed93894d3940c5dc9d0b7377048171b164a439e8b9e49813.pdf |

<a id="r3_public_03"></a>
### r3_public_03

**Source:** `sba_complianceplanomb_2024`. **Theme:** public_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Official legacy.sba.gov exact PDF matches ledger download route for September 2024 plan,17 pages; landing update date is not substituted for plan date.

**Inspected scope:** PDF pp. 3–4,9,11,15–17 only: governance steps, inventory form, generative AI notice and risk-management plans. Existing inherited full reading is not repeated/certified.

**Locators:** Strengthening AI Governance pp. 3–4; AI Use Case Inventories p. 9; Generative AI p. 11; Managing Risks pp. 15–16

**Visual check:** None. Text extraction inspected; no rendered figure/table inspection or visual authentication. Narrative section text is the basis for findings.

**Findings:**

- SBA reports creating a use-case submission form at the end of March 2024 and publicizing it through staff events; the plan also quotes a February 27, 2024 temporary restriction on publicly available generative AI for official/sensitive business (pp. 9,11).
- SBA explicitly says waiver criteria and process have not yet been developed (p. 15). Council approval, annual owner certification, compliance updates and termination/restart plans are described as a planned process (p. 16).
- The plan reports all use cases then under review as internally focused, with nothing deployed to the public; network surveillance and removal are described as existing generic noncompliant-technology controls (p. 16).

**Counterevidence / alternative:** Form publication and a stated network-removal pathway are identifiable reported acts, but cannot be equated to validated AI-specific testing, effective restriction enforcement, or demonstrated public-deployment oversight.

**Limits:** Historical agency plan self-description, not proof that these controls operated or remained policy later. The underlying Information Notice, submission records, network enforcement and actual governance decisions were not retrieved. No other pages reread.

**Replication:** `not_performed`. **Numerical check:** None; no quantitative inference or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C60](claims.md#c60)

**Relevance rationale:** Supporting federal-agency-use comparator for institutional implementation and evidence boundaries; not direct evidence of frontier-model release governance.

**Next check:** If asserting operation, inspect the underlying dated notice, case submissions, review decisions and restriction logs; keep future risk-control steps in future tense.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://legacy.sba.gov/sites/default/files/2024-10/Final%20508-Compliant%20SBA%20M-24-10%20Implementation%20Plan%20for%20AI%20-%20September%202024.pdf) |
| `final_url` | [Source](https://legacy.sba.gov/sites/default/files/2024-10/Final%20508-Compliant%20SBA%20M-24-10%20Implementation%20Plan%20for%20AI%20-%20September%202024.pdf) |
| `retrieved_at` | 2026-11-14T17:54:36.066850Z |
| `attempted_at` | 2026-11-14T17:54:35.136950Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary response bytes and URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 3e5a405ad28e2d16771f0fa24f2932e398b47bbec3e4dab3118f363cef06c6e3 |
| `byte_length` | 382078 |
| `mime_type` | application/pdf |
| `published_on` | 2024-09 |
| `version_claim` | SBA M-24-10 Implementation Plan, September 2024 |
| `locator_basis` | PDF viewer page numbers include cover and coincide with printed page numbers where shown. |
| `capture_path` | .source-captures/synthesis-3e5a405ad28e2d16771f0fa24f2932e398b47bbec3e4dab3118f363cef06c6e3.pdf |

<a id="r3_public_04"></a>
### r3_public_04

**Source:** `eac_complianceplanomb_2024`. **Theme:** public_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact canonical EAC14-page PDF; August 2 cover and September 20 FINAL revision both recorded rather than silently selecting one.

**Inspected scope:** PDF pp. 1–6,10–13: cover/revision history, purpose/scope, established governance, prospective inventory, risk/redress sections and selected definitions; no reread of pp. 7–9 or14.

**Locators:** Cover p. 1; revision history p. 2; Purpose/Scope p. 3; Strengthening AI Governance pp. 4–6; Managing Risks pp. 11–12

**Visual check:** None. Text extraction inspected; no rendered figure/table inspection or visual authentication. Narrative section text is the basis for findings.

**Findings:**

- Cover says August 2, 2024 v1.0; revision history records September 20, 2024 changes accepted FINAL. EAC reports designation of a CAIO, establishment of a governance board, staff guidance and acquisition of AI features in existing products (pp. 2,4).
- Operational framework and inventory collection use future tense; monitoring/auditing, termination and redress are listed with develop/establish/implement verbs rather than supported case outcomes (pp. 5–6,11–12). Although p. 11 labels review/waiver processes established, the accompanying develop/establish wording and lack of records prevent treating their operation as independently established.
- Scope covers EAC administrative IT and third parties acting on its behalf and excludes Commission guidance/actions about non-agency AI; purpose says use-case-specific practice compliance will be reported separately through annual inventory (p. 3).

**Counterevidence / alternative:** Some organizational acts are expressly reported completed, while risk-controls are described aspirationally or with mixed tenses. Neither the plan’s title nor those descriptions establish control effectiveness.

**Limits:** Historical self-report; no meeting minutes, completed case reviews, actual waiver/redress decisions or independent audit inspected. Does not establish voting-system safety or governance across election administration generally. Existing inherited full reading is not repeated/certified.

**Replication:** `not_performed`. **Numerical check:** None; no quantitative inference or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C60](claims.md#c60)

**Relevance rationale:** Supporting federal-agency-use comparator for institutional implementation and evidence boundaries; not direct evidence of frontier-model release governance.

**Next check:** Use as historical internal-agency comparator; inspect case-specific inventory and records before inferring testing, termination or remedies operated.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://www.eac.gov/sites/default/files/2024-10/EAC_Compliance_Plan_OMB_Memorandum_FINAL_508.pdf) |
| `final_url` | [Source](https://www.eac.gov/sites/default/files/2024-10/EAC_Compliance_Plan_OMB_Memorandum_FINAL_508.pdf) |
| `retrieved_at` | 2026-11-14T17:54:35.541808Z |
| `attempted_at` | 2026-11-14T17:54:35.137720Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary response bytes and URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 68479902111077458e0b84f27f6610f4e8e35a558b0abaf55a7b2f39463d5d28 |
| `byte_length` | 450204 |
| `mime_type` | application/pdf |
| `published_on` | 2024-09-20 |
| `version_claim` | Cover August 2, 2024 v1.0; revision log September 20, 2024 FINAL |
| `locator_basis` | PDF viewer page numbers include cover and coincide with printed page numbers where shown. |
| `capture_path` | .source-captures/synthesis-68479902111077458e0b84f27f6610f4e8e35a558b0abaf55a7b2f39463d5d28.pdf |

<a id="r3_public_05"></a>
### r3_public_05

**Source:** `statedepartment_complianceplanomb_2024`. **Theme:** public_implementation. **Reading:** Inaccessible. **Coverage effect:** `none`.

**Edition match:** `uncertain`. Exact canonical archive PDF route did not yield the PDF; no new binary version match authenticated.

**Inspected scope:** Access check only. Exact archived state.gov PDF URL returned Technical Difficulties HTML; alternate current-domain same-path request returned HTTP 403. No source PDF text inspected in this round.

**Locators:** Canonical September 23, 2024 PDF URL; no content locator authenticated

**Visual check:** None; no source PDF retrieved.

**Findings:**

No source findings; material was inaccessible.

**Counterevidence / alternative:** Inherited full-text label and prior AI scoped check may supply useful leads, but do not substitute for the inaccessible bytes in this round.

**Limits:** An HTTP-success Technical Difficulties HTML response is not the cited State plan. Alternate https://www.state.gov/wp-content/uploads/2024/09/DOS-Compliance-Plan-with-OMB-M-24-10-Accessible-9.23.2024.pdf returned 403 at 2026-11-14T17:55:30.099533Z. Earlier reported inventory/TEVV findings remain inherited, not a new primary check.

**Replication:** `not_performed`. **Numerical check:** None.

**Relevance:** `unresolved`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Scope would be a historical federal-use comparator, but new source access failed; no claim support assigned.

**Next check:** Retrieve an authenticated same-version official copy before adding State-specific findings; do not downgrade inherited labels or claim new corroboration.

| Capture field | Value |
|---|---|
| `preservation_status` | unavailable |
| `original_url` | [Source](https://2021-2025.state.gov/wp-content/uploads/2024/09/DOS-Compliance-Plan-with-OMB-M-24-10-Accessible-9.23.2024.pdf) |
| `final_url` | Not recorded / unavailable |
| `retrieved_at` | Not recorded / unavailable |
| `attempted_at` | 2026-11-14T17:54:35.138101Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked. Canonical endpoint returned a technical-error page and alternate official endpoint returned 403. |
| `sha256` | Not recorded / unavailable |
| `byte_length` | Not recorded / unavailable |
| `mime_type` | Not recorded / unavailable |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Not recorded / unavailable |
| `locator_basis` | No cited source PDF retrieved; failure located at exact URL. |
| `capture_path` | Not recorded / unavailable |

<a id="r3_public_06"></a>
### r3_public_06

**Source:** `omb_2024federalagency_2024`. **Theme:** public_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Immutable official OMB repository representation at commit 4a29d132291261d4829b187acd8af618e7295294; README snapshot is dated January 23, 2025 although canonical corpus date is December 16, 2024. Specific raw/v2/schema representation and limited scope are explicit.

**Inspected scope:** Complete README text only at immutable commit 4a29d132291261d4829b187acd8af618e7295294; repository tree used to identify files; this is not a comprehensive reading of the cited dataset.

**Locators:** README Summary; Key Considerations; Submissions Schedule; Repository Structure

**Visual check:** None. Text extraction inspected; no rendered figure/table inspection or visual authentication. Narrative section text is the basis for findings.

**Findings:**

- README reports 41 agency submissions, 2,133 use cases and 351 rights- and/or safety-impacting use cases as of January 23, 2025. It describes a consolidated administrative inventory, not measured deployment outcomes.
- README lists exclusions including qualifying R&D, national security and Intelligence Community systems, Department of Defense and legally/policy restricted public disclosure. Some details can be submitted to OMB but withheld publicly.
- Its repository-structure example names raw.csv/raw.xls, while the actual tree also contains raw_v2 files. The summary totals reproduce from raw_v2, not from the older raw.csv; this is a version-selection hazard rather than evidence that the summary totals are false.

**Counterevidence / alternative:** Publicly released agency-reported entries can make disclosure concrete; exclusions, mixed stages and unverified reporting prevent inference to all deployment, harms or controls.

**Limits:** README is documentation, not comprehensive dataset reading or compliance verification. Full per-agency provenance, inventories withheld from release and linked reporting instructions not inspected. Snapshot date differs from initial December 16, 2024 submissions deadline.

**Replication:** `not_performed`. **Numerical check:** README totals compared to exact v2 CSV recount in r3_public_07; no source-experiment replication.

**Relevance:** `claim_evidence`. **Claim links:** [C62](claims.md#c62)

**Relevance rationale:** Supporting federal-agency-use comparator for institutional implementation and evidence boundaries; not direct evidence of frontier-model release governance.

**Next check:** Always cite immutable commit and raw_v2 representation when using reproduced totals; audit primary agency submissions before outcome claims.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/4a29d132291261d4829b187acd8af618e7295294/README.md) |
| `final_url` | [Source](https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/4a29d132291261d4829b187acd8af618e7295294/README.md) |
| `retrieved_at` | 2026-11-14T17:55:30.437322Z |
| `attempted_at` | 2026-11-14T17:55:30.098171Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary response bytes and URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | dc846005495e339b6a77a38030a973d1dfec53648611de72ea045edc5275ea7f |
| `byte_length` | 6096 |
| `mime_type` | text/plain |
| `published_on` | Not recorded / unavailable |
| `version_claim` | README at repository commit 4a29d132291261d4829b187acd8af618e7295294; summary dated January 23, 2025 |
| `locator_basis` | Immutable repository commit or Git blob; Markdown headings, YAML field names and CSV headers/rows identify the inspected material. |
| `capture_path` | .source-captures/synthesis-dc846005495e339b6a77a38030a973d1dfec53648611de72ea045edc5275ea7f.txt |

<a id="r3_public_07"></a>
### r3_public_07

**Source:** `omb_2024federalagency_2024`. **Theme:** public_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Immutable official OMB repository representation at commit 4a29d132291261d4829b187acd8af618e7295294; README snapshot is dated January 23, 2025 although canonical corpus date is December 16, 2024. Specific raw/v2/schema representation and limited scope are explicit.

**Inspected scope:** Immutable GitHub blob API JSON and its base64-decoded exact raw_v2.csv bytes. Strict cp1252 parse of all rows for headers, row count, agency labels, impact categories and development-stage distributions; no substantive reading of every narrative field or row.

**Locators:** data/2024_consolidated_ai_inventory_raw_v2.csv at commit 4a29d132291261d4829b187acd8af618e7295294; Git blob 1efc086ad73dc7e0647968e3ecab60e9b9da88f0; columns Agency, Stage of Development and rights-/safety-impact question

**Visual check:** None. Text extraction inspected; no rendered figure/table inspection or visual authentication. Narrative section text is the basis for findings.

**Findings:**

- Pinned raw_v2 has 2,133 data rows, 41 agency labels after whitespace stripping, and 351 rights-impacting/safety-impacting/both labels after stripping and casefold normalization; these match README totals.
- Inventory contains multiple lifecycle stages, including initiated, acquisition/development, operation/maintenance and retired, so its total is not a deployed-system count. Neither row existence nor an agency-reported yes establishes control effectiveness.
- Original raw_v2 response is application/octet-stream and the CSV is cp1252, not UTF-8. The retained API JSON is UTF-8 with base64 data; decoded content is byte-identical to retained original response (SHA256 789e1bac6d2551e8f90e5cfc5feb37ac23c6ca9f302f5af92fea8a577caa0a83). No source bytes were transcoded.

**Counterevidence / alternative:** A concrete inventory documents reported records beyond promises, but source-defined scope, stage variation and self-report prevent interpreting totals as tested, safe or compliant systems.

**Limits:** Source capture is the immutable official GitHub JSON representation, not a transformed CSV. CSV header/selected categorical-field processing does not mean all use cases were read or independently verified. Counts are descriptive administrative reports, not estimates of deployment prevalence or harm. No row-level external validation or census of excluded/withheld cases.

**Replication:** `not_performed`. **Numerical check:** Programmatic documentary recount, not replication: strict cp1252 CSV decode; 2133 rows; 41 distinct Agency.strip() values; 131 rights-impacting +25 safety-impacting +195 both =351 after impact.strip().casefold(); 0 DictReader overflow rows. API base64 decode asserted byte-equal to original raw CSV. Stage categories were inspected as a documentary scope check, not independently validated.

**Relevance:** `claim_evidence`. **Claim links:** [C62](claims.md#c62)

**Relevance rationale:** Supporting federal-agency-use comparator for institutional implementation and evidence boundaries; not direct evidence of frontier-model release governance.

**Next check:** Retain exact commit/blob/CSV hash and normalization script; inspect conditional question requirements and primary case files before computing compliance rates.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://api.github.com/repos/ombegov/2024-Federal-AI-Use-Case-Inventory/git/blobs/1efc086ad73dc7e0647968e3ecab60e9b9da88f0) |
| `final_url` | [Source](https://api.github.com/repos/ombegov/2024-Federal-AI-Use-Case-Inventory/git/blobs/1efc086ad73dc7e0647968e3ecab60e9b9da88f0) |
| `retrieved_at` | 2026-11-14T17:56:59.184814Z |
| `attempted_at` | 2026-11-14T17:56:58.075648Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary response bytes and URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | bdc6e6bcbbcb057c7ceded805d2fd52857d5c24971f87b3dcae1f535d1bcb049 |
| `byte_length` | 4109845 |
| `mime_type` | application/json |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Git blob 1efc086ad73dc7e0647968e3ecab60e9b9da88f0 in commit 4a29d132291261d4829b187acd8af618e7295294 |
| `locator_basis` | Immutable repository commit or Git blob; Markdown headings, YAML field names and CSV headers/rows identify the inspected material. |
| `capture_path` | .source-captures/synthesis-bdc6e6bcbbcb057c7ceded805d2fd52857d5c24971f87b3dcae1f535d1bcb049.json |

<a id="r3_public_08"></a>
### r3_public_08

**Source:** `omb_2024federalagency_2024`. **Theme:** public_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Immutable official OMB repository representation at commit 4a29d132291261d4829b187acd8af618e7295294; README snapshot is dated January 23, 2025 although canonical corpus date is December 16, 2024. Specific raw/v2/schema representation and limited scope are explicit.

**Inspected scope:** YAML lines 1–110 and 680–835 only: identifiers, stage/impact fields and risk-management fields 51–56; no whole-dictionary read.

**Locators:** validation/data_dictionary.yaml: 16_dev_stage and 17_impact_type; Fields 51_extension_request through 56_monitor_postdeploy

**Visual check:** None. Text extraction inspected; no rendered figure/table inspection or visual authentication. Narrative section text is the basis for findings.

**Findings:**

- Dictionary differentiates model benchmark testing, performance evaluation in an operational/simulated environment and impact evaluation using counterfactual/rigorous methodologies; these are separate response categories, not interchangeable evidence.
- Risk-management questions are conditional on impact classification, lifecycle stage and (for fields 52 onward) no extension request. Blank values must not be treated as universal failure or noncompliance without applying those conditions.
- Field55 defines independent evaluation as CAIO/oversight/appropriate agency office with the reviewing authority not directly involved in development, not necessarily an institution external to the agency.

**Counterevidence / alternative:** Structured fields can enable follow-up audit and distinguish evidence types, but self-reported answers and conditional applicability are insufficient for independent assurance.

**Limits:** Dictionary uses machine-style headers corresponding to older raw.csv, while v2 uses human-readable questions and fewer columns; not an audited complete mapping. No compliance-rate inference made. Linked reporting instruction document and underlying assessments not inspected.

**Replication:** `not_performed`. **Numerical check:** None; no quantitative inference or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C62](claims.md#c62)

**Relevance rationale:** Supporting federal-agency-use comparator for institutional implementation and evidence boundaries; not direct evidence of frontier-model release governance.

**Next check:** If calculating control rates, create an explicit reviewed v2 header mapping, apply all conditional requirements and validate responses against underlying case artifacts.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/4a29d132291261d4829b187acd8af618e7295294/validation/data_dictionary.yaml) |
| `final_url` | [Source](https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/4a29d132291261d4829b187acd8af618e7295294/validation/data_dictionary.yaml) |
| `retrieved_at` | 2026-11-14T17:55:44.447903Z |
| `attempted_at` | 2026-11-14T17:55:44.071859Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary response bytes and URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | bc2302170a5b3aee419479522cd6afbb5416de9555a8d6fe7e34a848d7e8eee0 |
| `byte_length` | 45842 |
| `mime_type` | text/plain |
| `published_on` | Not recorded / unavailable |
| `version_claim` | data_dictionary.yaml at commit 4a29d132291261d4829b187acd8af618e7295294 |
| `locator_basis` | Immutable repository commit or Git blob; Markdown headings, YAML field names and CSV headers/rows identify the inspected material. |
| `capture_path` | .source-captures/synthesis-bc2302170a5b3aee419479522cd6afbb5416de9555a8d6fe7e34a848d7e8eee0.txt |

<a id="r3_public_09"></a>
### r3_public_09

**Source:** `omb_2024federalagency_2024`. **Theme:** public_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Immutable official OMB repository representation at commit 4a29d132291261d4829b187acd8af618e7295294; README snapshot is dated January 23, 2025 although canonical corpus date is December 16, 2024. Specific raw/v2/schema representation and limited scope are explicit.

**Inspected scope:** Older raw.csv strict UTF-8-sig parse of headers and all rows for row count and selected category distributions; no substantive reading of all free-text entries.

**Locators:** data/2024_consolidated_ai_inventory_raw.csv at commit 4a29d132291261d4829b187acd8af618e7295294

**Visual check:** None. Text extraction inspected; no rendered figure/table inspection or visual authentication. Narrative section text is the basis for findings.

**Findings:**

- Older raw.csv contains 1,757 data rows, while raw_v2 has 2,133. Selecting a file by the README structure example alone would not reproduce its January 23 summary. Both files coexist; intentional historical/version distinction remains possible.

**Counterevidence / alternative:** Versioned files may intentionally retain older snapshots. The useful correction is exact artifact selection and explicit normalization, not alleging inconsistency.

**Limits:** No claim that an older file should equal the v2 snapshot; no publisher error inferred. No full dataset read, release chronology audit or provenance reconciliation.

**Replication:** `not_performed`. **Numerical check:** Documentary file recount only: 1757 DictReader data rows, no overflow rows; not full-text reading or experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C62](claims.md#c62)

**Relevance rationale:** Supporting federal-agency-use comparator for institutional implementation and evidence boundaries; not direct evidence of frontier-model release governance.

**Next check:** Use v2 for the README snapshot totals and inspect Git history if interpreting change over time.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/4a29d132291261d4829b187acd8af618e7295294/data/2024_consolidated_ai_inventory_raw.csv) |
| `final_url` | [Source](https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/4a29d132291261d4829b187acd8af618e7295294/data/2024_consolidated_ai_inventory_raw.csv) |
| `retrieved_at` | 2026-11-14T17:55:44.651753Z |
| `attempted_at` | 2026-11-14T17:55:44.071086Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary response bytes and URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 9a2c9e25d41eb7b4b2e5463459c8ea78e0e02db0c15e82cc09c88e78889b40f5 |
| `byte_length` | 2655883 |
| `mime_type` | text/plain |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Older raw.csv in commit 4a29d132291261d4829b187acd8af618e7295294 |
| `locator_basis` | Immutable repository commit or Git blob; Markdown headings, YAML field names and CSV headers/rows identify the inspected material. |
| `capture_path` | .source-captures/synthesis-9a2c9e25d41eb7b4b2e5463459c8ea78e0e02db0c15e82cc09c88e78889b40f5.txt |

<a id="r3_provider_01"></a>
### r3_provider_01

**Source:** `wan_foundationmodeltransparency_2025`. **Theme:** provider_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Same work/title/date; exact arXiv 2512.10169 v1 dated 11 December 2025 pinned rather than mutable latest URL.

**Inspected scope:** Exact arXiv v1 PDF pp. 1,3–6,14–19,32–39,48–49: abstract, index/instrument background and changes, full §§4.1–4.5 methods, overall results/Figure 7, reporting-method comparison, longitudinal discussion/Figures 16–17/Table 3, conclusion/conflicts, and AppendixA including agent prompt and retrieval comparison. Other results subsections, indicator tables and bibliography pages not fully read.

**Locators:** §§3.1,3.3, pp. 5,14–15; Figure 6 p. 14; §§4.1–4.5 pp. 15–18; Figure 7 p. 19; Figure 15 pp. 32–33; §5.3/Figures 16–17/Table 3 pp. 33–37; AppendixA pp. 48–49

**Visual check:** No rendered figure inspection; numerical figure labels and table text were read in the PDF text extraction. Figure 7 arithmetic checked separately.

**Findings:**

- FMTI 2025 assesses 13 developers on 100 disclosure indicators each: 1,300 developer–indicator pairs, independently assigned by two FMTI team scorers before consensus. It is a disclosure-measurement exercise, not an operational compliance audit or causal estimate of safety effects.
- Seven companies prepared solicited reports; for six others the team searched official company artifacts, complemented by an agent search whose findings required expert checking. All 13 companies were offered a response phase. New information could be disclosed through the reports and responses; the source set was not restricted to information public before solicitation.
- AppendixA explicitly says all published scores reflect FMTI-team judgments; no published scores were proposed or directly determined by an AI system. Agent retrieval used official-company-domain constraints and could generate false positives and false negatives; source dependence on issuer communications remains.
- Figure 7 scores sum to 529, giving 529/13=40.6923; Results uses 40.69/100, whereas abstract says 40. Report 40.69 or approximately 41, or reproduce the abstract as an attributed quotation rather than silently treating 40 as the exact mean.
- Instrument comparison is materially confounded: 55 indicators are new and only nine are unchanged. Figure 16 holds nine companies constant and finds seven lower 2025 scores, but indicators, reporting mechanisms and flagship models still differ. Table 3 supplies narrower examples of reduced disclosure, not proof that underlying practices ceased.
- Positive mechanism: solicited structured reports and response engagement elicit additional disclosures, with responses clarifying/correcting/updating information for a reported mean 18.9 indicators and increasing scores by mean 9.71. The seven report-preparing companies score 54.1 on average versus 25.0 for six FMTI-prepared reports; selection and disclosure effort are alternative explanations, so this gap is not a causal intervention effect.
- Points can be awarded for disclosure of information dependencies or contractual restrictions in the circumstances described on p. 15. A missing point therefore cannot be uniformly interpreted as absence of a control or practice, nor can a point uniformly mean the requested underlying measurement was supplied.

**Counterevidence / alternative:** IBM 95, Writer 72 and AI 21 Labs 66 demonstrate high disclosure scores are achievable in this instrument; report engagement yields useful new information. Selection, changed instrument/flagship models and security/commercial disclosure tradeoffs bound interpretation of both gaps and regressions.

**Limits:** No independent re-scoring of the 1,300 cells, developer report/source audit, evaluation reproduction or complete 49-page reading. The authors identify industry affiliations on p. 39; external FMTI scoring does not make issuer disclosures independent evidence of practice. Two internal prose issues retained in notes: p. 33 says seven reports in 2024 where Figure 16 says 2025; p. 37 says Meta dropped 23 from 2024–25 while Figure 16 says 29. Neither inconsistent prose number is used as a new result.

**Replication:** `not_performed`. **Numerical check:** Figure 7:13 scores sum 529; mean 40.6923077 rounds 40.69. Agreement: (1300−138)/1300=89.3846%, consistent with 89.4%. Figure 16 scores:7/9 lower; Meta 60→31 is−29. No experiment reproduced.

**Relevance:** `claim_evidence`. **Claim links:** [C63](claims.md#c63)

**Relevance rationale:** Adds a measured disclosure result and a positive reporting mechanism while bounding the inference from disclosure to implementation.

**Next check:** Retain exact mean/method denominators and distinguish non-disclosure from practice absence. Audit leading indicator-level examples against the published developer reports before attributing a regression to a particular organizational practice. If a trend claim leads publication, compare the fixed nine unchanged indicators and constant developers; do not present aggregate decline as a controlled estimate.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2512.10169v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2512.10169v1) |
| `retrieved_at` | 2026-11-14T17:54:09Z |
| `attempted_at` | 2026-11-14T17:54:09Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | b05cf7c81e7b97828e4085772f61348f638e0d8b94f5de877568acd6a60fd16c |
| `byte_length` | 2222160 |
| `mime_type` | application/pdf |
| `published_on` | 2025-12-11 |
| `version_claim` | arXiv 2512.10169 v1,11 December 2025 |
| `locator_basis` | PDF viewer pages equal printed page numbers 1–49. |
| `capture_path` | .source-captures/synthesis-b05cf7c81e7b97828e4085772f61348f638e0d8b94f5de877568acd6a60fd16c.pdf |

<a id="r3_provider_02"></a>
### r3_provider_02

**Source:** `nvidia_frontierriskassessment_2025`. **Theme:** provider_implementation. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Title/issuer match canonical record; captured 15-page PDF cover says Applicable from August 2025. Source has four named cover authors; corporate authorship remains an editorial choice. Exact canonical publication day 17 February 2025 was not established by the body or independently checked.

**Inspected scope:** All 15 PDF pages, including cover/abstract/executive summary, Preliminary and Detailed Risk Assessments, both V-model figures, Tables 1–2, risk mitigation/tool descriptions, risk evaluation and governance, and the footnotes printed in this document. Linked tools, model cards and cited studies were not independently opened.

**Locators:** Cover p. 1: applicability and historical frontier-model statement; PRA pp. 2–3; DRA/lifecycle pp. 3–5, Figures 1–2 p. 4; Risk formula/Table 1 pp. 6–7; template/Table 2 p. 8; Tools and risk evaluation pp. 9–14; Governance pp. 14–15

**Visual check:** Rendered p. 4 checked for both V-model diagrams and p. 8 for Table 2; remaining tables read from extracted text. The rendering confirms Table 2 labels the 49→5 numbers as a risk-analysis template.

**Findings:**

- The report describes positive operational mechanisms: design-stage screening by capability, intended use and autonomy; MR 4 business-unit approval and MR 5 committee approval language; reassessment on product/context/hazard changes; model-card documentation; and deployment-dependent controls. MR 5 approval by an independent committee means an internal governance mechanism such as NVIDIA’s AI ethics committee, not independently verified external assurance.
- It states NVIDIA uses Garak as a highest-priority assessment before release and describes product-specific guardrails and data-processing practices. These are concrete issuer reports of operational use, stronger than a bare commitment, but the document supplies no independently checked execution record, counterfactual or measured reduction in catastrophic harm.
- It explicitly says mapping and enforcing specific controls across all model types/use cases is infeasible and leaves relevant controls to engineering teams with increased oversight at higher risk. Downloaded weights constrain downstream controls; models with use-case restrictions may receive a lower PRA category.
- The cover applicability is August 2025 and states frontier models were not then under development at NVIDIA. Table 2’s 49→5 is an example/template, not a reported product outcome; broad claims about watermarks or tooling efficacy are not substantiated by independent testing in this reading.

**Counterevidence / alternative:** Operational details and claimed pre-release use give a concrete implementation hypothesis, but neither all-products control coverage nor actual risk reduction follows. Internal governance approval is distinct from external independence; use-case restrictions can change the initial category as well as residual risk.

**Limits:** Complete reading is of this 15-page report, not linked software/manuals/model cards or demonstrated implementation. Cover historical statement is not a claim about NVIDIA in November 2026. PDF creation metadata 12 February 2025 cannot establish publication 17 February 2025; do not infer it. Descriptions of tool capabilities and broad efficacy language were not externally validated.

**Replication:** `not_performed`. **Numerical check:** Documentary formula check only: pp. 6–7 factors yield minimum 1 and maximum 64. Enumerating the literal listed Table 1 scores cannot produce Table 2 initial risk 49; residual 5 is possible. No input-factor assignment or empirical derivation for 49→5 is supplied. Treat as illustrative and omit any percentage-reduction claim. No experiment/tool benchmark reproduced.

**Relevance:** `claim_evidence`. **Claim links:** [C64](claims.md#c64)

**Relevance rationale:** Provides a concrete positive provider implementation account while distinguishing reported practice, internal approval, illustrative arithmetic and externally demonstrated effects.

**Next check:** Seek a dated product assessment/model card, review decision, test configuration and incident follow-up before claiming realized control effectiveness. Retain reported mechanisms now. Preserve August applicability separately from unverified 17 February publication date, and omit template risk-reduction numbers.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://images.nvidia.com/content/pdf/NVIDIA-Frontier-AI-Risk-Assessment.pdf) |
| `final_url` | [Source](https://images.nvidia.com/content/pdf/NVIDIA-Frontier-AI-Risk-Assessment.pdf) |
| `retrieved_at` | 2026-11-14T17:54:09Z |
| `attempted_at` | 2026-11-14T17:54:09Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 8c6aade8b0cff8797f481715cf3dc512171299790031f921c00ae60f53d0077b |
| `byte_length` | 638458 |
| `mime_type` | application/pdf |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Cover: Applicable from August 2025; no publication day printed in inspected document. |
| `locator_basis` | PDF viewer pages 1–15; no printed page numbers. |
| `capture_path` | .source-captures/synthesis-8c6aade8b0cff8797f481715cf3dc512171299790031f921c00ae60f53d0077b.pdf |

<a id="r3_provider_03"></a>
### r3_provider_03

**Source:** `meta_advancedaiscalingframeworkv2_2026`. **Theme:** provider_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. CoverVersion 2 and AppendixII explicitly identifies 7 April 2026 Advanced AI Scaling Frameworkv 2.0, matching canonical record. Do not treat later retrieval date as a later policy edition.

**Inspected scope:** PDF pp. 1–17,25–28,39–44: executive summary, scope, complete governance/transparency/accountability sections, outcomes/threat-model inclusion criteria and risk thresholds, evaluation environment and elicitation/deployment-context passages, first cybersecurity threshold example, benefits assessment, future work, terminology and change log. Risk-domain scenarios and detailed domain-specific implementation pp. 18–24,29–38 not read in full.

**Locators:** §§1–2 pp. 3–11: scope/governance/preparedness reports/accountability; §§3.1–3.3 pp. 12–17; Table 1 p. 15; §§4.1–4.2 pp. 25–28; §4.3/§5 pp. 39–40; AppendixI pp. 41–43; AppendixII change log p. 44

**Visual check:** No rendered visual inspection. Table 1 and terminology read in PDF text extraction.

**Findings:**

- Version 2 defines pre-mitigation risk tiers and conditions deployment/development on mitigations. Critical and high models may deploy only with sufficient defined, implemented and validated mitigations reducing risk to moderate or lower; §3.3 further conditions continued development of critical models. These are declared conditions, not evidence a particular model satisfied them.
- AppendixII describes two coupled changes: primary threshold language moves from uniquely enable to substantially contribute; tier labels move from Stop/Do not release to Develop with Mitigations/Deploy with mitigations. The new criterion and response must be read together, without assuming a uniform tightening or weakening.
- Concrete accountability mechanisms include named Chief AI Officer/Director of Alignment and Risk responsibility, risk review, preparedness-report contents/update triggers and incident response. Some reporting/whistleblower protocols are still described as developing or future commitments; preserve that tense.
- Framework scope is deliberately narrower than all serious harm: inclusion requires plausibility, catastrophic scale, net-new outcome and instantaneous or irremediable impact. It acknowledges gradual or partly remediable catastrophic harms are handled outside the Framework. Implementation text acknowledges unknown unknowns, deployment-dependent elicitation and incomplete evaluation science.

**Counterevidence / alternative:** The broader material-contribution trigger and more explicit accountability/reporting are positive institutional mechanisms; mitigation-based continuation is conditional, not a demonstrated loss of restraint. Conversely the scope excludes some serious harms and self-reported validation does not prove external effectiveness.

**Limits:** Not a full 44-page reading, independent adherence audit or verification of a released model’s preparedness report. Prior policy was not independently retrieved; comparisons with v1 are attributed to the inspected v2 change log. Institutional and causal efficacy remains untested here.

**Replication:** `not_performed`. **Numerical check:** Source comparison only: v2 Table 1/§3.3/AppendixII checked for consistency of threshold/response language. Compute threshold 10^26 is a definitional trigger, not measured risk or a safety result. No experiments reproduced.

**Relevance:** `claim_evidence`. **Claim links:** [C65](claims.md#c65)

**Relevance rationale:** Adds precise current-edition process and scope evidence while preventing a simple tightening/loosening narrative from replacing comparative evaluation.

**Next check:** If the policy change becomes a leading normative argument, retrieve and compare exact v1 bytes plus dated preparedness reports and actual risk decisions. For now report v2 conditions and scope, attributing old/new labels to its change log; leave the overall strengthening/weakening interpretation open.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2/) |
| `final_url` | [Source](https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2/) |
| `retrieved_at` | 2026-11-14T17:54:09Z |
| `attempted_at` | 2026-11-14T17:54:09Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | d87aa9bf00456ec747e80b84216f9f2ffc427c1e98541f8b3c8f7f52c13c7b6a |
| `byte_length` | 668289 |
| `mime_type` | application/pdf |
| `published_on` | 2026-04-07 |
| `version_claim` | Version 2; AppendixII:7 April 2026 Advanced AI Scaling Frameworkv 2.0. |
| `locator_basis` | PDF viewer pages 1–44; printed page numbers 2–44, cover counted as 1. |
| `capture_path` | .source-captures/synthesis-d87aa9bf00456ec747e80b84216f9f2ffc427c1e98541f8b3c8f7f52c13c7b6a.pdf |

<a id="r3_provider_04"></a>
### r3_provider_04

**Source:** `metr_commonelementsfrontier_2024`. **Theme:** provider_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Issuer static PDF explicitly titled Common Elements of Frontier AI Safety Policies and dated August 2024 on cover. This resolves a historical-edition route without replacing the 2024 work with the later living page.

**Inspected scope:** PDF pp. 1–5,21–22: cover, summary, introduction, common-components list and initial capability-threshold excerpts, plus policy-updating excerpts. Other pages and underlying three policy editions not fully read.

**Locators:** Cover:August 2024; Summary/introduction pp. 2–3; Common Components and threshold excerpts pp. 4–5; Updating Policies over Time, concluding excerpts pp. 21–22

**Visual check:** No rendered visual checks; selected PDF text inspected.

**Findings:**

- The original August 2024 report compares three existing detailed safety frameworks and distinguishes that set from sixteen Seoul-commitment signatories.
- The common-component inventory supplies a useful descriptive vocabulary: threat models, weight security, deployment mitigations, stopping conditions, capability elicitation, evaluation timing, accountability and policy updates. Its quoted commitments do not establish implementation or effects.
- Updating-policy excerpts themselves describe exploratory/preliminary estimates and possible revisions; these are historical policy statements, not a stable 2026 consensus.

**Counterevidence / alternative:** Common stated mechanisms can be substantive design commitments, but their presence and the descriptive comparison do not establish compliance, common risk tolerance or externally demonstrated effectiveness.

**Limits:** PDF extractor reported a recoverable xref warning; selected text was readable, but visual fidelity of all 22 pages was not checked. This is a descriptive comparison of three published policies and quoted commitments, not their operational execution. Underlying policy versions not independently rechecked.

**Replication:** `not_performed`. **Numerical check:** Denominator check: summary/introduction name three policies—Anthropic, OpenAI and Google DeepMind. Sixteen Seoul signatories are a separate group, not sixteen analyzed policies. No experiment reproduced.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Historical comparator and methods vocabulary; it need not become independent support for provider compliance or the new claims. It also establishes that later twelve-policy coding cannot be attributed to the 2024 edition.

**Next check:** Keep historicalAugust 2024 PDF for claims about that review. Use later page only as a related edition with its own date, denominator and caveats; no new claim is required merely to assign this record a background role.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://metr.org/assets/common_elements_of_frontier_ai_safety_policies.pdf) |
| `final_url` | [Source](https://metr.org/assets/common_elements_of_frontier_ai_safety_policies.pdf) |
| `retrieved_at` | 2026-11-14T17:57:47Z |
| `attempted_at` | 2026-11-14T17:57:42Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | 38560378b8dbe7be72a95296c452db2820aa08e9cf62c85ea8500e2388b26486 |
| `byte_length` | 991761 |
| `mime_type` | application/pdf |
| `published_on` | 2024-08 |
| `version_claim` | Cover:August 2024. |
| `locator_basis` | PDF viewer pages equal printed pages 1–22, with cover counted as 1. |
| `capture_path` | .source-captures/synthesis-38560378b8dbe7be72a95296c452db2820aa08e9cf62c85ea8500e2388b26486.pdf |

<a id="r3_provider_05"></a>
### r3_provider_05

**Source:** `metr_commonelementsfrontier_2024`. **Theme:** provider_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Living issuer page explicitly labels 16 December 2025 and says original report wasAugust 2024. Twelve-policy expansion and regulatory guidance belong to this later edition, not the canonical 2024 snapshot.

**Inspected scope:** Living page header/date, Summary, Introduction, common-element inventory/Table 1, opening Capability Thresholds excerpts and Table 2, Conclusion and footnotes 1–4. Remaining per-element excerpts and cited sources not fully read.

**Locators:** Header/date and Summary:December 16,2025; Introduction/Table 1:presence of safety elements across 12 policies; Table 2:covered threat models; Conclusion; footnotes 1–4

**Visual check:** No rendered visual checks; visible HTML parsed to text for selected sections.

**Findings:**

- The later page expands the comparison to 12 policies and expressly distinguishes the originalAugust 2024 report from thisDecember 2025 version.
- Footnote 1 says descriptive, not prescriptive, and warns missing policy elements need not imply regulatory noncompliance: applicability, effective dates, omitted relevant text and separate compliance documentation are alternatives.
- The page still quotes Meta’s earlier Frontier AI Framework; the separately inspectedApril 2026 v2 is later and has different scope/threshold/governance text. This is a concrete version boundary, not proof the entire living comparison has been recoded.

**Counterevidence / alternative:** Published comparisons improve navigability and expose mechanisms, but some omissions can reflect document scope or coding rather than absence of practice or legal compliance.

**Limits:** Mutable page as retrieved 14 November 2026 still labelsDecember 2025; this does not certify that provider policies remain current. The page does not incorporate MetaApril 2026 v2 in its listed Meta title/quoted first-framework text. Presence coding was not independently rerun.

**Replication:** `not_performed`. **Numerical check:** Version/denominator comparison: later page lists 12 policies, versus 3 inAugust 2024. No twelve-policy rate was newly recomputed or used to judge compliance.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Useful later comparative context with explicit missing-information caution; related-edition status prevents inflation of the 2024 reading coverage.

**Next check:** Preserve the two editions separately. If a current twelve-policy comparison matters, recheck exact provider editions and applicable law rather than treating the live page as a contemporaneous compliance audit.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://metr.org/common-elements) |
| `final_url` | [Source](https://metr.org/common-elements) |
| `retrieved_at` | 2026-11-14T17:54:09Z |
| `attempted_at` | 2026-11-14T17:54:09Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific archive was available in this bounded round; local bytes and the exact primary version URL are retained. Independent archival preservation is not claimed. |
| `sha256` | a684be69aa2b86e50f8884313bcc7e3e207e99f651642446fdc5cd206907fab3 |
| `byte_length` | 342380 |
| `mime_type` | text/html |
| `published_on` | 2025-12-16 |
| `version_claim` | Page date:December 16,2025; explicitly described asDecember 2025 version. |
| `locator_basis` | HTML heading/table/footnote names; no PDF page numbers. |
| `capture_path` | .source-captures/synthesis-a684be69aa2b86e50f8884313bcc7e3e207e99f651642446fdc5cd206907fab3.html |

<a id="r3_provider_06"></a>
### r3_provider_06

**Source:** `anthropic_frontiercomplianceframework_2026`. **Theme:** provider_implementation. **Reading:** Inaccessible. **Coverage effect:** `none`.

**Edition match:** `uncertain`. CanonicalMarch 2026 edition cannot be established from the exact resource endpoint: HTTP 200 returned only a Trust Center application shell, visible text Anthropic Trust Center.

**Inspected scope:** Attempted exact issuer resource endpoint; no underlying framework text or methods/appendices read.

**Locators:** Requested March2026 framework body at the canonical trust-resource endpoint; only an Anthropic Trust Center shell was returned, so no framework locator was inspected.

**Visual check:** None; no source body available.

**Findings:**

No source findings; material was inaccessible.

**Counterevidence / alternative:** An access failure is not evidence that the framework does not exist, lacks safeguards or is not implemented.

**Limits:** Exact URL returned 7166 bytes of HTML application shell, not the framework. The shell response hash/bytes are recorded only in private retrieval diagnostics; neither source reading nor framework preservation is claimed. March 2026 date/content and distinction from RSP remain unverified.

**Replication:** `not_performed`. **Numerical check:** None.

**Relevance:** `unresolved`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Accounts for an assigned unresolved framework without promoting issuer marketing/metadata or a shell to source evidence.

**Next check:** Obtain the exactMarch 2026 framework download from issuer or an appropriately accessible copy; preserve edition identity before judging substance. Keep the record unresolved rather than inferring content from title, FAQ or adjacent RSP.

| Capture field | Value |
|---|---|
| `preservation_status` | unavailable |
| `original_url` | [Source](https://trust.anthropic.com/resources?name=anthropic-frontier-compliance-framework&s=eorilovp4wxk38nxbi7k3) |
| `final_url` | [Source](https://trust.anthropic.com/resources?name=anthropic-frontier-compliance-framework&s=eorilovp4wxk38nxbi7k3) |
| `retrieved_at` | Not recorded / unavailable |
| `attempted_at` | 2026-11-14T17:54:09Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No readable framework or checked capture-specific archive obtained. The retrieved TrustCenter HTML shell is retained privately for diagnostics and is not a capture of the framework. |
| `sha256` | Not recorded / unavailable |
| `byte_length` | Not recorded / unavailable |
| `mime_type` | Not recorded / unavailable |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Not recorded / unavailable |
| `locator_basis` | No readable framework body. |
| `capture_path` | Not recorded / unavailable |
## safety-cases-evaluation-validity-2026-11-14

**As of:** 2026-11-14. **Base commit:** `e484ed0d5c805b98ba55cc9d35b14c989dc41a63`.

**Question:** Which assurance arguments, evaluator-validation methods and strategic-behavior results add missing roles or challenge the broad synthesis, and what can fresh complete rechecks establish about inherited reading coverage?

**Selection basis:** Purposive selection from 177 unresolved roles and the existing exact-edition/numerical queue. Prioritizes safety-case construction/confidence, evaluation awareness and sandbagging, reward/judge validity, and a small heterogeneous sample of inherited full-text objects. Three mapped works receive edition or denominator follow-up. Selection is recorded before acquisition; not a systematic sample, retrospective search reconstruction, or independent human review.

**Stopping rule:** Complete one bounded reviewable round. Prefer complete reading of manageable claim-critical exact texts; retain selected scope for long artifacts and unverified editions. Source roles may be supportive, contrary, background or unresolved. Make bounded exact-source access attempts and omit disputed quantities where their provenance remains uncertain. Do not force every selected key into a claim or infer earlier reading from a fresh check.

| Theme | Why selected | Canonical keys |
|---|---|---|
| Safety-case construction, confidence and change | Tests whether structured arguments improve decisions and what validates their confidence or update rules. | `lee_constructingsafety_2026`, `barrett_assessingconfidence_2025`, `bloomfield_assurancesystemsdependabil_2024`, `carlan_dynamicsafetycases_2024`, `buhl_safetycasesfrontier_2024`, `hilton_safetycasesscalable_2025` |
| Evaluation awareness, sandbagging and monitor validity | Distinguishes elicited strategic behavior, awareness probes and interventions from spontaneous behavior, capability concealment and effective deployment monitoring. | `chaudhary_evaluationawareness_2025`, `li_cancovertlysandbag_2025`, `nguyen_probingsteeringevaluation_2025`, `hua_steeringevaluation_2025`, `kutasov_evaluatingsabotage_2025` |
| Reward models and substitution of human judgments | Tests whether reward/judge rankings predict useful downstream behavior and when statistical agreement can justify a defined substitution. | `lambert_rewardbenchevaluating_2024`, `frick_evaluaterewardrlhf_2024`, `calderon_alternativeannotator_2025`, `dubois_skewedscore_2025`, `wang_selftaughtevaluators_2024` |
| Fresh checks of inherited full-text anchors and related artifacts | Purposeful contrast among a taxonomy, a joint model evaluation, a changing measurement page and a benchmark portal; distinguishes the identified object from linked reports and historical snapshots. | `fmf_preliminarytaxonomy_2024`, `aisi_safetyinstitutesjoint_2024`, `metr_timehorizons_2026`, `mlcommons_ailuminate_2026`, `mlcommons_ailuminatev10_2025` |
| Exact editions, a fairness denominator and a statutory date | Targets final-proceedings equivalence, public-input label interpretation and TrustLLM category aggregation without a blanket error verdict. The unresolved New York effective-date question was added adaptively before retrieval at2026-11-14T23:33Z; this is not retrospective preregistration. | `cunningham_sparseautoencoders_2024`, `huang_collectiveconstitutional_2024`, `huang_trustllm_2024`, `newyork_raiseact_article44b_nd` |

### Event index

| Event | Source | Reading | Edition / coverage effect | Relevance |
|---|---|---|---|---|
| [r4_safetycases_01](#r4_safetycases_01) | `buhl_safetycasesfrontier_2024` | Full text | same_record / complete_record_text | claim_evidence |
| [r4_safetycases_02](#r4_safetycases_02) | `hilton_safetycasesscalable_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r4_safetycases_03](#r4_safetycases_03) | `lee_constructingsafety_2026` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r4_safetycases_04](#r4_safetycases_04) | `barrett_assessingconfidence_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r4_safetycases_05](#r4_safetycases_05) | `carlan_dynamicsafetycases_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r4_safetycases_06](#r4_safetycases_06) | `bloomfield_assurancesystemsdependabil_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r4_awareness_01](#r4_awareness_01) | `chaudhary_evaluationawareness_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r4_awareness_02](#r4_awareness_02) | `nguyen_probingsteeringevaluation_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r4_awareness_03](#r4_awareness_03) | `hua_steeringevaluation_2025` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r4_awareness_04](#r4_awareness_04) | `li_cancovertlysandbag_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r4_awareness_05](#r4_awareness_05) | `kutasov_evaluatingsabotage_2025` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r4_judges_01](#r4_judges_01) | `lambert_rewardbenchevaluating_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r4_judges_02](#r4_judges_02) | `frick_evaluaterewardrlhf_2024` | Selected sections | same_record / scoped_review | background |
| [r4_judges_03](#r4_judges_03) | `frick_evaluaterewardrlhf_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r4_judges_04](#r4_judges_04) | `wang_selftaughtevaluators_2024` | Full text | same_record / complete_record_text | claim_evidence |
| [r4_judges_05](#r4_judges_05) | `calderon_alternativeannotator_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r4_judges_06](#r4_judges_06) | `dubois_skewedscore_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r4_judges_07](#r4_judges_07) | `lambert_rewardbenchevaluating_2024` | Metadata only | related_edition / none | background |
| [r4_depthsample_01](#r4_depthsample_01) | `fmf_preliminarytaxonomy_2024` | Full text | same_record / complete_record_text | background |
| [r4_depthsample_02](#r4_depthsample_02) | `aisi_safetyinstitutesjoint_2024` | Full text | same_record / complete_record_text | claim_evidence |
| [r4_depthsample_03](#r4_depthsample_03) | `aisi_safetyinstitutesjoint_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r4_depthsample_04](#r4_depthsample_04) | `metr_timehorizons_2026` | Full text | same_record / complete_record_text | claim_evidence |
| [r4_depthsample_05](#r4_depthsample_05) | `mlcommons_ailuminate_2026` | Full text | same_record / complete_record_text | claim_evidence |
| [r4_depthsample_06](#r4_depthsample_06) | `mlcommons_ailuminatev10_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r4_depthsample_07](#r4_depthsample_07) | `mlcommons_ailuminatev10_2025` | Abstract only | related_edition / none | background |
| [r4_editions_01](#r4_editions_01) | `cunningham_sparseautoencoders_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r4_editions_02](#r4_editions_02) | `huang_collectiveconstitutional_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r4_editions_03](#r4_editions_03) | `huang_trustllm_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r4_editions_04](#r4_editions_04) | `huang_trustllm_2024` | Selected sections | related_edition / scoped_review | background |
| [r4_editions_05](#r4_editions_05) | `huang_trustllm_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r4_editions_06](#r4_editions_06) | `huang_trustllm_2024` | Metadata only | related_edition / none | background |
| [r4_editions_07](#r4_editions_07) | `cunningham_sparseautoencoders_2024` | Metadata only | same_record / none | background |
| [r4_ny_01](#r4_ny_01) | `newyork_raiseact_article44b_nd` | Selected sections | same_record / scoped_review | claim_evidence |
| [r4_ny_02](#r4_ny_02) | `newyork_raiseact_article44b_nd` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r4_ny_03](#r4_ny_03) | `newyork_raiseact_article44b_nd` | Selected sections | related_edition / scoped_review | claim_evidence |

<a id="r4_safetycases_01"></a>
### r4_safetycases_01

**Source:** `buhl_safetycasesfrontier_2024`. **Theme:** safety_cases. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical arXiv identifier, title and author identity match. This event concerns the pinned v1 only; later revisions and linked artifacts are not equated with it.

**Inspected scope:** All 25 pages of accessible v1 text read, including title, contents, executive summary, Sections1–7, footnotes, Tables1–5, text/captions of Figures1–6, abbreviations, acknowledgments and references. No linked sources or underlying industry cases independently inspected.

**Locators:** §§2.1–2.3 pp5–8; Figure2/Table2 pp6–7; §3.2 pp9–12, Tables3–4: comparison with specific rules; §§4.1–4.4 pp12–16: scope, objectives, arguments and evidence; §§5.1–5.2 pp16–18; Table5: methodology, reviewers and capacity

**Visual check:** Rendered and visually inspected Figure2 on p6. All other figures/tables read through their extracted labels/captions/cells, without separate pixel inspection. No diagram is treated as an executed evaluation.

**Findings:**

- A safety case is an outcome-oriented, system-specific argument with evidence and stated operational scope; adherence to an organization-wide framework must additionally be justified as sufficient for the safety objective (§2.3).
- The proposed writer/reviewer/decision-maker process makes argument validity, evidential support and change conditions inspectable. Figure2 and Table2 are explicit sketches, not sufficient or sound cases for an actual near-term system.
- Tables3–4 compare flexibility, innovation and use of developer knowledge with review costs, reduced transparency, inconsistent judgments, capture and gamability. The preferred regulatory approach is conditional on industry/regulator circumstances, and precise rules can complement or eventually replace parts of the approach.
- The paper acknowledges little empirical evidence of safety-case efficacy and warns against overreliance before methodology and reviewer capacity mature. External review is a mature-ecosystem goal, not represented as a precondition already fulfilled.

**Counterevidence / alternative:** A structured argument can expose gaps but can also give false assurance; costs, expertise, conflicts, unknown future capabilities and open-ended deployment contexts constrain its use. The paper treats several arguments beyond inability as unresolved rather than demonstrated safeguards.

**Limits:** Conceptual/governance analysis focused on catastrophic risks and the US/UK/EU in the 2024 edition. Full reading does not verify its cited industry evidence, present regulation or actual frontier deployment outcomes. The illustrative 80% task threshold and risk quantities are examples, not validated decision thresholds.

**Replication:** `not_performed`. **Numerical check:** Documentary reading only; no experimental reproduction, code execution, or numerical recomputation.

**Relevance:** `claim_evidence`. **Claim links:** [C66](claims.md#c66)

**Relevance rationale:** Adds a specified assurance mechanism, constructive illustration or limitation to the broad synthesis; methodological proposals, illustrative cases and author-reported experiments remain separate from independently verified decision effects.

**Next check:** If making an efficacy or regulatory-superiority claim, seek actual decision/review records and comparative implementation evidence. Retain conditional design argument now.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2410.21572v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2410.21572v1) |
| `retrieved_at` | 2026-11-14T23:26:03.107441+00:00 |
| `attempted_at` | 2026-11-14T23:26:02.975724+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and pinned URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 86fc0ede73b44c09558971940bd81bb29830977de60b9b81927b2880af547779 |
| `byte_length` | 823413 |
| `mime_type` | application/pdf |
| `published_on` | 2024-10-28 |
| `version_claim` | arXiv:2410.21572v1; 28 October2024; 25-page PDF |
| `locator_basis` | One-based PDF viewer pages; printed pages agree except Bloomfield, whose printed page is one less than viewer page. |
| `capture_path` | .source-captures/synthesis-86fc0ede73b44c09558971940bd81bb29830977de60b9b81927b2880af547779.pdf |

<a id="r4_safetycases_02"></a>
### r4_safetycases_02

**Source:** `hilton_safetycasesscalable_2025`. **Theme:** safety_cases. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical arXiv identifier, title and author identity match. This event concerns the pinned v1 only; later revisions and linked artifacts are not equated with it.

**Inspected scope:** All accessible text of the 19-page v1 representation, including Sections1–5, both figure captions/labels, Tables1–3, footnotes and references. The final page contains only a page number. No linked papers, standards or empirical artifacts opened.

**Locators:** §§2.1–2.4 pp2–7; Figures1–2 pp2,6; §3.1 p8 and Table2: organizational frameworks versus system cases; §3.2/Table3 pp9–12: conditional mapping to Seoul commitments; §§4.1–4.3 pp12–14: thresholds, independence, quantification, generalization and implementation questions

**Visual check:** Rendered and visually inspected both Figures1–2 on pp2,6. Tables read as extracted cells; no additional visual authentication of historical policy examples.

**Findings:**

- The proposed writer, red-team and decision-maker roles include experiments/counterexamples by the reviewer, rather than document review alone; cases can support development, go/no-go decisions and incident response (§2.1).
- The Seoul-commitment mapping is explicitly conditional on an adequate process producing correct cases. Threshold-setting, broader governance, quick response triggers and public communication still require other processes (Table3).
- The source distinguishes inability, safeguards, control and trustworthiness arguments and explicitly says it does not yet know how to make good arguments for increasingly capable future systems. Multiple independent arguments are an aspiration, with independence itself an open question.
- Compared with prescriptive, information-sharing and ex-post alternatives, the proposal offers flexibility and assessability but carries documentation/evidence costs and unresolved methodological choices.

**Counterevidence / alternative:** Failure to elicit a dangerous capability is weaker than proving no one can elicit it; threshold adequacy, out-of-distribution monitoring and confidence measures remain research questions. Method flexibility is not measured deployment safety.

**Limits:** This complete reading is a fresh recheck of an inherited full-text object, not a new full-text-label addition or proof of the earlier reading. It does not independently verify the cited Seoul text/current frameworks or experimental findings. Shared Buhl/Goemans lineage is not independent outcome corroboration.

**Replication:** `not_performed`. **Numerical check:** Documentary reading only; no experimental reproduction, code execution, or numerical recomputation.

**Relevance:** `claim_evidence`. **Claim links:** [C66](claims.md#c66)

**Relevance rationale:** Adds a specified assurance mechanism, constructive illustration or limitation to the broad synthesis; methodological proposals, illustrative cases and author-reported experiments remain separate from independently verified decision effects.

**Next check:** Use a real reviewed case with declared thresholds, reviewer authority and update triggers if claiming implementation effects; keep the current argument as a methodological proposal.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2503.04744v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2503.04744v1) |
| `retrieved_at` | 2026-11-14T23:26:03.068845+00:00 |
| `attempted_at` | 2026-11-14T23:26:02.976710+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and pinned URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 3c00b327c3b98a6cc67447a3c86b921d9281aaca0779cd672c5320569e486c1b |
| `byte_length` | 461687 |
| `mime_type` | application/pdf |
| `published_on` | 2025 |
| `version_claim` | arXiv:2503.04744v1; 19-page retained representation |
| `locator_basis` | One-based PDF viewer pages; printed pages agree except Bloomfield, whose printed page is one less than viewer page. |
| `capture_path` | .source-captures/synthesis-3c00b327c3b98a6cc67447a3c86b921d9281aaca0779cd672c5320569e486c1b.pdf |

<a id="r4_safetycases_03"></a>
### r4_safetycases_03

**Source:** `lee_constructingsafety_2026`. **Theme:** safety_cases. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. The arXiv identifier and original title match the canonical record, but this v1 lists six authors while the canonical author field includes Lionel Briand as a seventh. The later v3 has a changed title. This mixed-edition record is conservatively related_edition; no equivalence or metadata rewrite is assumed.

**Inspected scope:** Pinned v1 pp1,8–10,13–14,26–30: title/abstract/introduction opening; review methodology and selection; taxonomy/architecture opening; complete tender-case section and limitations/conclusion. Other taxonomy/pattern subsections, all selected-study appendices and bibliography not fully read.

**Locators:** §3 pp8–10, Figures4–5: literature-selection design; §4.1–4.3 pp13–14: composable CAE structure and inferred mappings; §6 pp26–29, Table7/Figure8: GPT-4o tender-review illustration; §7–8 pp29–30: limits, verification-process boundary and future work

**Visual check:** Rendered and visually inspected Figure8 on p29. Other selected figures/tables read through extracted labels/captions/cells only.

**Findings:**

- The v1 proposes reusable claim–argument–evidence patterns grounded in an author-described literature review, and explicitly distinguishes observed CAE framing from inferred mappings that can introduce interpretive bias (§§3–4).
- Section6 describes a prompt-based GPT-4o tender-review pilot and reports controlled comparisons on 200 synthetic tender cases. This is more specific than a purely abstract template; the paper calls it a real-world case, while the reported evaluation materials are synthetic.
- The case reports comparative agreement/consistency and an acceptance threshold, but the inspected case text does not provide the estimator denominator, bootstrap output or confidence-interval endpoints needed to verify noninferiority or broad safety/fairness. It also moves between the marginal difference and the AI–human absolute inconsistency rate as the threshold quantity.
- The contribution explicitly concerns assembling and contextualizing evidence; §7 says the verification processes producing those artifacts are not modeled. Therefore a well-structured template does not itself verify its inputs.

**Counterevidence / alternative:** The attributed pilot offers an implementation illustration, but agreement with an accepted comparator does not establish correct or fair decisions; synthetic evaluation does not establish deployed procurement effects. Template composition can preserve weak evidence as readily as strong evidence.

**Limits:** Related v1 edition has different authorship from the canonical record. No full 41-page read, independent dataset/script inspection, metric recomputation or equivalence with v3. The numerical tender results are not promoted to verified efficacy or noninferiority.

**Replication:** `not_performed`. **Numerical check:** Documentary reading only; no experimental reproduction, code execution, or numerical recomputation.

**Relevance:** `claim_evidence`. **Claim links:** [C66](claims.md#c66)

**Relevance rationale:** Adds a specified assurance mechanism, constructive illustration or limitation to the broad synthesis; methodological proposals, illustrative cases and author-reported experiments remain separate from independently verified decision effects.

**Next check:** Adjudicate canonical title/authorship against an exact edition, then inspect the released protocol/data if a tender effectiveness or fairness claim matters. Preserve the mechanism and attributed synthetic illustration without the affected quantitative conclusion.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2601.22773v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2601.22773v1) |
| `retrieved_at` | 2026-11-14T23:26:03.192305+00:00 |
| `attempted_at` | 2026-11-14T23:26:02.973978+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and pinned URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 6b5b31dfc748d77fddbaef06fb60cfbcaeac4665a6609f3846668ad70335b8c6 |
| `byte_length` | 1290395 |
| `mime_type` | application/pdf |
| `published_on` | 2026-01-30 |
| `version_claim` | arXiv:2601.22773v1; 30 January2026; original title; six named authors |
| `locator_basis` | One-based PDF viewer pages; printed pages agree except Bloomfield, whose printed page is one less than viewer page. |
| `capture_path` | .source-captures/synthesis-6b5b31dfc748d77fddbaef06fb60cfbcaeac4665a6609f3846668ad70335b8c6.pdf |

<a id="r4_safetycases_04"></a>
### r4_safetycases_04

**Source:** `barrett_assessingconfidence_2025`. **Theme:** safety_cases. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact canonical arXiv identifier, title and author identity match. This event concerns the pinned v1 only; later revisions and linked artifacts are not equated with it.

**Inspected scope:** Pinned v1 Sections1–2 pp6–9; full §4 pp17–20; §7 and opening §8 pp27–33; §9.3 and §10 pp42–45. Unread logical-block/weight-of-evidence details pp10–16, defeater details pp21–26, remaining priority/communication details pp34–41 and bibliography pp46–48 remain outside this event.

**Locators:** §§2.1–2.2 pp7–9: confidence in argument versus risk claim; §4.1–4.3 pp17–20 and Figure5 p19: LLM-Delphi pilot and comparison; §7.1 pp27–30, Eqs5–9/Table3: propagation model; §§7.2–7.3 pp31–33; §§10.1–10.2 pp42–44: interpretation and limits

**Visual check:** Rendered and visually inspected Figure5 on p19 and the Eq5–9 page28. Other probability diagrams/tables read as extracted text; no plot digitization or source-data reproduction.

**Findings:**

- The source separates logical soundness, explicit defeaters and residual doubts from the later numerical confidence valuation. Its safety-case application is an illustrative cyber-inability argument, not an observed deployment audit.
- It reports a pilot with 100 resolved binary Metaculus questions and 50 role-prompted GPT-4o-mini instances drawn from 40 roles; Figure5 reports lower Brier score than its selected Metaculus comparator. This is a constructive experiment, not merely an untested elicitation proposal.
- The Metaculus comparator uses last available forecasts while the LLM is assigned an earlier information cutoff, and the question sample, aggregation and source inputs were not re-audited here. Brier score combines more than calibration; the figure does not establish calibrated safety-case probabilities or independent expert agreement.
- The product model requires independence under its conjunctive representation. The sum-of-doubts lower bound Eq9 is a union bound and does not require independence; adjacent prose about independence/equality must not be inherited literally. Both remain conditional models of a separately justified argument, not measured system risk.
- The paper acknowledges very low propagated confidences, subjective overrides, related claim dependencies, unknown-hazard monitoring problems and unvalidated transfer from its forecasting pilot. Its proposed value includes exposing assumptions and prioritizing further work, not a certified absolute safety probability.

**Counterevidence / alternative:** Documented elicitation and conservative bounds can improve inspectability, but many prompted instances of one model do not provide independent human expertise. A confidence graph can look precise without calibrated leaf probabilities, a sound argument model or adequate risk coverage.

**Limits:** Selected 19-page scope within a 48-page paper; no code/data inspection, model experiment rerun or recomputed Brier score. Reported role diversity is not source independence. Do not treat the illustrative 95%/99.3% calculation as a required universal safety threshold, or a zero lower bound as proof of zero actual confidence.

**Replication:** `not_performed`. **Numerical check:** Documentary/mathematical check only: visually verified Eq7 versus Eq9. P(conjunction) >= max(0,1-sum of doubt probabilities) is the union-bound lower bound regardless of dependence; equality of a union probability with a sum generally requires mutually exclusive doubts, not independent doubts. No published pilot score, graph node probability or experimental result was recomputed.

**Relevance:** `claim_evidence`. **Claim links:** [C67](claims.md#c67)

**Relevance rationale:** Adds a specified assurance mechanism, constructive illustration or limitation to the broad synthesis; methodological proposals, illustrative cases and author-reported experiments remain separate from independently verified decision effects.

**Next check:** Validate exact forecast inputs and baseline/aggregation before reusing numerical performance. Require application-specific calibration or credible human elicitation for safety-case probabilities; preserve qualitative structural insights now.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2502.05791v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2502.05791v1) |
| `retrieved_at` | 2026-11-14T23:26:03.225454+00:00 |
| `attempted_at` | 2026-11-14T23:26:02.974606+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and pinned URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 7d5d7091ef4d9b2523784a9b59dc85609e17bdca0e599217f9bf24b122b8ab45 |
| `byte_length` | 1998763 |
| `mime_type` | application/pdf |
| `published_on` | 2025-02-09 |
| `version_claim` | arXiv:2502.05791v1; 9 February2025; 48-page PDF |
| `locator_basis` | One-based PDF viewer pages; printed pages agree except Bloomfield, whose printed page is one less than viewer page. |
| `capture_path` | .source-captures/synthesis-7d5d7091ef4d9b2523784a9b59dc85609e17bdca0e599217f9bf24b122b8ab45.pdf |

<a id="r4_safetycases_05"></a>
### r4_safetycases_05

**Source:** `carlan_dynamicsafetycases_2024`. **Theme:** safety_cases. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact canonical arXiv identifier, title and author identity match. This event concerns the pinned v1 only; later revisions and linked artifacts are not equated with it.

**Inspected scope:** Pinned v1 pp6–12 (related work, DSCMS requirements, CSA assumptions and SPI design); pp27–28 (selected no-underelicitation/no-sandbagging SPI tables); pp33–36 (example change impact and governance integration); pp45–47 (discussion, recommendations and conclusion). Remaining detailed indicators, scenarios, governance comparisons, appendices and references were not read in full.

**Locators:** §§3–4.2 pp6–12, Table1 and Assumptions1–3; Tables9–11 pp27–28: example SPIs and thresholds; §4.4 Scenario4/Table13 p33; §5.1 pp34–36/Table14; §§6–8 pp45–47: tool/prototype status and validation limits

**Visual check:** Text, captions and selected table cells inspected. No separate rendering/pixel inspection of figures or all 41 tables/figures; conceptual diagrams are not treated as actual system telemetry.

**Findings:**

- The proposal links monitored indicator breaches or changed artifacts to directly and indirectly affected argument elements through explicit consistency rules, then assigns investigation/escalation and update responsibilities.
- Completeness/accuracy claims depend on a valid initial argument, complete traceability and correct metrics/thresholds. A mechanically consistent update does not discover missing hazards or establish that a chosen indicator tracks actual risk.
- The cyber examples use specified hypothetical indicator values, thresholds and change scenarios. Governance roles and decision gates describe a proposed response path rather than observed alerts, completed interventions or measured risk reduction.
- Section6 explicitly places toolset investigation outside scope and says SPI integration is not currently automated. Section7 calls for a minimal frontier-AI prototype and governance exercises. Existing tools from other sectors are not demonstrated frontier deployment.

**Counterevidence / alternative:** Partial automation and explicit ownership are constructive design mechanisms, but inadequate indicators can produce false negatives/positives; external data access, nonlinear context changes and major capability jumps may require expert judgment or rebuilding the case.

**Limits:** Selected sections of 75 pages; no linked tool, formal model or live implementation inspected. Generic documents in requirements are placeholders. Example indicator percentages and response-time thresholds are not validated normative limits or empirical rates.

**Replication:** `not_performed`. **Numerical check:** Documentary reading only; no experimental reproduction, code execution, or numerical recomputation.

**Relevance:** `claim_evidence`. **Claim links:** [C68](claims.md#c68)

**Relevance rationale:** Adds a specified assurance mechanism, constructive illustration or limitation to the broad synthesis; methodological proposals, illustrative cases and author-reported experiments remain separate from independently verified decision effects.

**Next check:** Test a minimal actual case, trace dependencies, validate indicators and measure decisions/updates before claims of operational performance. Keep the conditional workflow and assumptions explicit.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2412.17618v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2412.17618v1) |
| `retrieved_at` | 2026-11-14T23:26:04.415683+00:00 |
| `attempted_at` | 2026-11-14T23:26:02.975329+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and pinned URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | a8d4c6e066de38b838e4fb1133eb941e6283e59ac9dc6be310c516c947a90cff |
| `byte_length` | 6377086 |
| `mime_type` | application/pdf |
| `published_on` | 2024-12-23 |
| `version_claim` | arXiv:2412.17618v1; 23 December2024; 75-page PDF |
| `locator_basis` | One-based PDF viewer pages; printed pages agree except Bloomfield, whose printed page is one less than viewer page. |
| `capture_path` | .source-captures/synthesis-a8d4c6e066de38b838e4fb1133eb941e6283e59ac9dc6be310c516c947a90cff.pdf |

<a id="r4_safetycases_06"></a>
### r4_safetycases_06

**Source:** `bloomfield_assurancesystemsdependabil_2024`. **Theme:** safety_cases. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact canonical arXiv identifier, title and author identity match. This event concerns the pinned v1 only; later revisions and linked artifacts are not equated with it.

**Inspected scope:** Pinned v1 PDF pp11–14 (§§2–2.2 opening), pp16–20 (§2.3 and architecture-summary opening), pp31–33 (§4 opening/contractual trust), pp43–44 (§6 opening). Corresponding printed pages are10–13,15–19,30–32,42–43. Other case examples, normative enforcement discussion, AGI arguments and bibliography not fully read.

**Locators:** §§2.1–2.2 PDFpp12–14/printed11–13: world-model/guard dependency; §2.3 PDFpp16–20/printed15–19: diversity and defense in depth; §4 PDFpp31–33/printed30–32: generic versus focused-system assurance; §6 opening PDFpp43–44/printed42–43: high-bar dependability perspective

**Visual check:** Extracted text and architecture labels only. No independent rendered-figure inspection or cited accident reconstruction.

**Findings:**

- The dependability perspective proposes guarding opaque AI/ML components with simpler components whose properties can be conventionally justified. Remediation and enforcement must themselves be engineered; adding a monitor also adds possible hazards.
- An action guard can fail if it relies on an inaccurate AI-built world model. For some constrained settings a conventionally checked geofence or backup can support stronger assurance; broader perception and hazard coverage remain difficult.
- Diverse components may improve reliability, but the source rejects a naive multiplicative failure argument: hard cases and shared models can make failures correlated. Defense in depth is useful without assuming demonstrated independence.
- The report explicitly adopts a demanding dependability standard and acknowledges a continuum of alternative assurance perspectives. Its conclusion is a design/research position, not an empirical finding that every AI safeguard or useful lower-assurance application is impossible.

**Counterevidence / alternative:** Constrained, conventionally checked guards can support meaningful guarantees. Where guards depend on AI perception or normative judgments, the trusted boundary remains unresolved; diversity can reduce demands on a backup without establishing independent failure probabilities.

**Limits:** Selected sections of the 62-page original edition, not the revised2025 v3 read in inherited notes. Cyber-physical examples and a demanding assurance philosophy do not establish effectiveness of present LLM application guards. Accident examples and cited primary work were not independently audited.

**Replication:** `not_performed`. **Numerical check:** Documentary reading only; no experimental reproduction, code execution, or numerical recomputation.

**Relevance:** `claim_evidence`. **Claim links:** [C69](claims.md#c69)

**Relevance rationale:** Adds a specified assurance mechanism, constructive illustration or limitation to the broad synthesis; methodological proposals, illustrative cases and author-reported experiments remain separate from independently verified decision effects.

**Next check:** For the intended LLM use, specify exactly which hazards are checked, which perception/judgment is trusted, and which safe intervention is possible; inspect actual system tests and later editions if leading a publication claim.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2407.13948v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2407.13948v1) |
| `retrieved_at` | 2026-11-14T23:26:03.278405+00:00 |
| `attempted_at` | 2026-11-14T23:26:02.974979+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and pinned URLs are retained locally. Independent archival preservation is not claimed. |
| `sha256` | b382d5513d7c7602309a40252a91a3717f752b73ad6de12168a17552574bf8dd |
| `byte_length` | 933569 |
| `mime_type` | application/pdf |
| `published_on` | 2024-07-18 |
| `version_claim` | arXiv:2407.13948v1; uploaded18 July2024; report cover says22 July2024, SRI-CSL-2024-02 |
| `locator_basis` | One-based PDF viewer pages; printed pages agree except Bloomfield, whose printed page is one less than viewer page. |
| `capture_path` | .source-captures/synthesis-b382d5513d7c7602309a40252a91a3717f752b73ad6de12168a17552574bf8dd.pdf |

<a id="r4_awareness_01"></a>
### r4_awareness_01

**Source:** `chaudhary_evaluationawareness_2025`. **Theme:** evaluation_awareness. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical arXiv identifier, year and authors; v2 title includes Large and the final four byline positions differ from inherited metadata. These documentary metadata leads do not establish a different work. This event reads the pinned v2, not all previous versions.

**Inspected scope:** Complete eight-page arXiv v2: abstract, main Sections1–5, references, Appendix6.1–6.5, all figure captions and reproducibility table. All Figures1–5 visually inspected on PDF pp1,4,6,7. No linked implementation/data executed or source literature independently reread.

**Locators:** Sections3.1–3.3 pp2–3: model selection, contrastive probes and SAD scoring; Sections4–5 pp3–4 and Figure1 p1: selected best-layer size association; Appendix6.1–6.5 pp6–8; Figures3–5: dataset, template, excluded Qwen and reproducibility details

**Visual check:** All Figures1–5 rendered and visually checked; qualitative axes/series/legend comparison, not digitization or fit recomputation.

**Findings:**

- The paper reports stronger best-layer probe separation with model size in the selected families. The endpoint is classification of evaluation/deployment prompts, not observed deception or concealed capability.
- Appendix6.2 shows large chat-template dependence; Appendix6.3 excludes Qwen from the main trend and explicitly reports that Qwen does not follow the hypothesized size increase.
- Probe construction reuses Nguyen’s synthetic contrastive dataset and the SAD oversight evaluation. These are shared method/task inputs, not independent behavioral validation.

**Counterevidence / alternative:** Positive classification signal survives in selected models, but Qwen and template sensitivity challenge a universal scaling law; no behavioral deception outcome was measured.

**Limits:** Best-layer selection, one benchmark construction, family/template dependence and excluded contrary results bound extrapolation. Fresh complete reading concerns this exact v2, not verification of past reading, workshop acceptance or experimental replication.

**Replication:** `not_performed`. **Numerical check:** Documentary methods/figure check only. No AUROC, uncertainty or fitted curve recomputed. Avoid a headline model-count/forecasting claim; the enumerated reproducibility list and exclusions would need an experiment manifest if that count matters.

**Relevance:** `claim_evidence`. **Claim links:** [C70](claims.md#c70)

**Relevance rationale:** Adds a previously unresolved source role while distinguishing observed signals, induced behavior, controls and monitor endpoints. A new reading does not prove an earlier reader read this text.

**Next check:** Use a conditional separability result. Validate prospective behavioral outcomes, held-out layer/model selection and additional families before forecasting deception from this fit.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2509.13333v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2509.13333v2) |
| `attempted_at` | 2026-11-14T23:25:51.401559+00:00 |
| `retrieved_at` | 2026-11-14T23:25:51.903648+00:00 |
| `sha256` | fb99ff6caea385ca5328f62488a6209122c7f71cf2f69bb0c0bde0525d43c7bd |
| `byte_length` | 856365 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary PDF bytes are retained privately. Independent archival preservation is not claimed. |
| `published_on` | 2025-11-09 |
| `version_claim` | arXiv:2509.13333v2, PDF cover 9 November 2025; NeurIPS2025 footer is source-attributed, venue type not independently authenticated |
| `locator_basis` | One-based PDF viewer pages; printed page numbers agree. Section/figure/appendix locators identify the pinned edition. |
| `capture_path` | .source-captures/synthesis-fb99ff6caea385ca5328f62488a6209122c7f71cf2f69bb0c0bde0525d43c7bd.pdf |

<a id="r4_awareness_02"></a>
### r4_awareness_02

**Source:** `nguyen_probingsteeringevaluation_2025`. **Theme:** evaluation_awareness. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical arXiv identifier/title/authors and2025 date; pinned July9 v2 matches the inherited review’s stated edition. Complete fresh text inspection neither proves the inherited reading occurred nor independently authenticates all earlier claims.

**Inspected scope:** Complete 18-page arXiv v2: abstract, Sections1–6, acknowledgments/impact, all references pp9–13, appendix prompts, all dataset descriptions/SAE labels pp13–17, Figures1–9 captions and final all-feature plot p18. Linked source datasets, implementation and dashboards were not inspected.

**Locators:** Sections3.1–3.4 pp3–4: selection, baselines, prompted WMDP and recovery definition; Sections4.1–4.3 pp4–7: probe validation and steering; Sections5.3–5.5 pp7–8: targeted-noise alternative and transfer limits; Appendix pp13–18; Figures8–9 pp15,18: selected features and unrelated controls

**Visual check:** Figures8–9 rendered and visually inspected, including all 15 feature curves on p18. Other figure captions/available extracted labels were read, without independent pixel inspection of Figures1–7.

**Findings:**

- The simple contrastive probe distinguishes SAD prompt contexts better than the tested random, prompt-length and special-character heuristics, with additional cross-dataset validation; it is a selected representation signal, not a causal deception test.
- On explicitly prompted WMDP underperformance, a simple deployment suffix recovers far more of the accuracy gap than linear-probe steering; selected SAE features give partial recovery.
- Figures8–9 show unrelated control features with recovery comparable to or greater than relevant features. Section5.3 explicitly leaves genuine belief modification versus targeted noise unresolved.

**Counterevidence / alternative:** Above-heuristic classification and selected intervention effects are affirmative findings. Strong prompting and unrelated-feature controls weaken claims of awareness-specific steering or superiority of internal interventions.

**Limits:** One Llama 3.3-70B-Instruct model, synthetic/stylized prompts and selected layers/features/strengths. Probe thresholds/layers selected using SAD; benign user questions can look test-like. No natural sandbagging, live monitor utility or unique awareness mechanism established.

**Replication:** `not_performed`. **Numerical check:** Checked recovery formula as fraction of the induced accuracy gap, not an absolute percentage-point increase. Main text gives roughly 83% suffix recovery and less than 5% linear-probe recovery. Figures8–9 contain control-specific maxima; no headline best-SAE rate is adopted or experimental result reproduced.

**Relevance:** `claim_evidence`. **Claim links:** [C70](claims.md#c70), [C71](claims.md#c71)

**Relevance rationale:** Adds a previously unresolved source role while distinguishing observed signals, induced behavior, controls and monitor endpoints. A new reading does not prove an earlier reader read this text.

**Next check:** Retain the probe/behavior distinction and simple controls; test independent selection sets, wider tasks and known latent behavior before general monitoring or mechanism claims.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2507.01786v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2507.01786v2) |
| `attempted_at` | 2026-11-14T23:25:51.402595+00:00 |
| `retrieved_at` | 2026-11-14T23:25:51.805174+00:00 |
| `sha256` | 055c35ee272d3e1f81d86ad135f739fa22f318ada2064de52c29e913e9ab97f9 |
| `byte_length` | 2953126 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary PDF bytes are retained privately. Independent archival preservation is not claimed. |
| `published_on` | 2025-07-09 |
| `version_claim` | arXiv:2507.01786v2,9 July2025; cover identifies two ICML 2025 workshops |
| `locator_basis` | One-based PDF viewer pages; printed page numbers agree. Section/figure/appendix locators identify the pinned edition. |
| `capture_path` | .source-captures/synthesis-055c35ee272d3e1f81d86ad135f739fa22f318ada2064de52c29e913e9ab97f9.pdf |

<a id="r4_awareness_03"></a>
### r4_awareness_03

**Source:** `hua_steeringevaluation_2025`. **Theme:** evaluation_awareness. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Exact arXiv work identifier/title/authors, but inspected v5 is 2026 and conference-styled whereas canonical citation describes a2025 preprint. Conservatively related_edition; no canonical depth upgrade or final-proceedings identity assumed.

**Inspected scope:** Pinned 62-page arXiv v5: main text pp1–12 (Sections1–6, contributions/acknowledgments); AppendixG pp31–35 including layer/strength selection, belief-behavior caveat and grading prompt; AppendixI.1 pp40–41 and Table16/p44; AppendixI.2 pp45–46. Remaining references, training/robustness appendices, many figures and transcripts not fully read.

**Locators:** Sections3–4 pp4–7: synthetic-document/expert-iteration organism and intervention setup; Sections5.1–5.3 pp7–10; Figures3–5 pp8–10: type-hint effects and controls; Section6 pp10–11: explicit-cue limitations and unknown deployment behavior; AppendixG pp31–35 and I.1–I.2 pp40–41,44–46: tuning, prompting and belief-grading caveats

**Visual check:** Figures3–5 visually checked on PDF pp8–10; other selected appendix figure captions/text read, without plot digitization or comprehensive visual review.

**Findings:**

- A steering direction extracted before evaluation-aware fine-tuning changes a deliberately trained type-hint behavior under an evaluation cue, with smaller effects from24 matched-distribution random vectors.
- The main benchmark uses 256 selected BigCodeBench questions, explicit context cues and usually an awareness hint. Strength/layer choices are tuned against the known behavior and coding performance.
- Some declarative prompts also elicit deployment-like behavior; authors did not exhaustively red-team prompting. AppendixG’s verbalized-belief/behavior relation has a no-hint caveat, and steered type-hint rates can overshoot the unsteered deployment rate.

**Counterevidence / alternative:** Random-vector and pre-fine-tuning controls support a meaningful targeted intervention; alternative prompts, explicit-cue dependence, tuning and accuracy effects limit a universal mitigation or unique-belief-mechanism inference.

**Limits:** This 2026/ICLR-styled v5 extends the canonical 2025 preprint representation; equivalence to the2025 edition is not certified. Engineered type hints, one model organism and known-target tuning do not validate recovery of unknown natural deployment behavior.

**Replication:** `not_performed`. **Numerical check:** Documentary comparison of type-hint endpoint, coding accuracy and prompt/steering comparators only; no model execution, confidence-interval reconstruction or experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C71](claims.md#c71)

**Relevance rationale:** Adds a previously unresolved source role while distinguishing observed signals, induced behavior, controls and monitor endpoints. A new reading does not prove an earlier reader read this text.

**Next check:** Inspect earlier/final editions and omitted appendices if exact magnitudes lead. Require behavioral validation on more capable naturally evaluation-aware models; treat this as constructive organism evidence now.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2510.20487v5) |
| `final_url` | [Source](https://arxiv.org/pdf/2510.20487v5) |
| `attempted_at` | 2026-11-14T23:25:51.403066+00:00 |
| `retrieved_at` | 2026-11-14T23:25:52.257769+00:00 |
| `sha256` | 969dd38af789f1333eb14cc9d03a4ac14b9afc999fa0ebf143f0c8431a704712 |
| `byte_length` | 9457435 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary PDF bytes are retained privately. Independent archival preservation is not claimed. |
| `published_on` | 2026-03-02 |
| `version_claim` | arXiv:2510.20487v5,2 March2026; cover says Published as a conference paper at ICLR2026 |
| `locator_basis` | One-based PDF viewer pages; printed page numbers agree. Section/figure/appendix locators identify the pinned edition. |
| `capture_path` | .source-captures/synthesis-969dd38af789f1333eb14cc9d03a4ac14b9afc999fa0ebf143f0c8431a704712.pdf |

<a id="r4_awareness_04"></a>
### r4_awareness_04

**Source:** `li_cancovertlysandbag_2025`. **Theme:** evaluation_awareness. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact canonical arXiv identifier/title/authors/year; pinned v2 is the edition named in inherited notes. This scoped recheck does not recertify its inherited full-text label or claim final IJCNLP-AACL text equivalence.

**Inspected scope:** Pinned 28-page arXiv v2: abstract, selected main Sections1–5/limitations pp1–6; AppendixB.1–B.4 text/captions pp9–12; AppendixD and Figures11–12 pp16–17, plus AppendixE opening classification description. Attack prompt AppendixA, complete references, additional-performance pages13–15 and worked biological/chemical transcripts pp18–28 were not fully read.

**Locators:** Section3 pp2–3: ten models,400 WMDP and400 MMLU items, three instructed conditions and score; Section4.1 p4/Figure3: approval conditional on successful instructed sandbagging; AppendixB.2–B.4 pp10–12: baseline FPR, noisy two-run success proxy, GPT 5 same-prompt comparator; AppendixD pp16–17/Figures11–12: harder benchmark and metric-label hold

**Visual check:** Main Figure3/p4 and Appendix Figures11–12/p17 visually inspected. Other inspected figure captions/text were read but not independently digitized; worked hazardous-domain transcripts were not reviewed.

**Findings:**

- Monitor-aware instructions can increase approval among successful instructed sandbagging attempts, while reducing efficacy or selectivity. This is capability under prompting, not spontaneous propensity.
- AppendixB.3 defines success using one correct baseline answer followed by one incorrect instructed answer and explicitly notes noise from lucky guesses/errors; the monitor sees question, reasoning and answer, but not the sandbagging instruction.
- GPT 5 substitution with the same GPT 4.1-mini-tuned monitor prompt does not show a significant improvement in the reported analysis; the harder ProtocolQA condition is less favorable to covert sandbagging for most models.

**Counterevidence / alternative:** Successful instructed evasions are evidence of a failure mode. Low joint reliability, effect/selectivity tradeoffs, difficult-task changes and noisy filtering bound both alarmist and reassuring interpretations.

**Limits:** Selected reading of MCQ proxy tasks and one monitoring design. Conditional approval is not an unconditional covert-success or deployment-incidence rate. Same-prompt model substitution is not an optimized monitor comparison. No hazardous-item or worked-transcript audit.

**Replication:** `not_performed`. **Numerical check:** No model/data reproduction. AppendixB defines FPR on honest baseline responses and conditional approval as approximate FNR; Figures7b/11 captions use FPR for related approval results. Retain the definition/label distinction and omit affected headline ProtocolQA rates rather than infer corrected values.

**Relevance:** `claim_evidence`. **Claim links:** [C72](claims.md#c72)

**Relevance rationale:** Adds a previously unresolved source role while distinguishing observed signals, induced behavior, controls and monitor endpoints. A new reading does not prove an earlier reader read this text.

**Next check:** Use the conditional metric and benchmark/monitor configuration. Omit ProtocolQA headline percentages until its approval/FPR wording and denominators are reconciled; test repeated trials and better-elicited monitors before broad conclusions.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2508.00943v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2508.00943v2) |
| `attempted_at` | 2026-11-14T23:25:51.402158+00:00 |
| `retrieved_at` | 2026-11-14T23:25:52.439378+00:00 |
| `sha256` | 1df7272af88f5bc4757efe8aaa9f85eb812cd0a091b77db15039c75849845ba5 |
| `byte_length` | 4321610 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary PDF bytes are retained privately. Independent archival preservation is not claimed. |
| `published_on` | 2025-10-31 |
| `version_claim` | arXiv:2508.00943v2,31 October2025 |
| `locator_basis` | One-based PDF viewer pages; printed page numbers agree. Section/figure/appendix locators identify the pinned edition. |
| `capture_path` | .source-captures/synthesis-1df7272af88f5bc4757efe8aaa9f85eb812cd0a091b77db15039c75849845ba5.pdf |

<a id="r4_awareness_05"></a>
### r4_awareness_05

**Source:** `kutasov_evaluatingsabotage_2025`. **Theme:** evaluation_awareness. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Same arXiv identifier/authors/year but v2 adds SHADE-Arena to the title absent from the canonical title. Conservatively related_edition until earlier-title content comparison; canonical key preserved and no full-depth upgrade claimed.

**Inspected scope:** Pinned 44-page arXiv v2: main pp1–10 through conclusions and opening references; AppendixB pp14–15; AppendixD.1–D.2 pp24–25; AppendixJ/K text pp38–40; AppendixL.2 paragraph on p41; remaining monitoring/high-level/compute text pp42–44. Full bibliography, detailed task transcripts, prompts and many appendix figures not comprehensively read.

**Locators:** Sections2–4 pp2–8: task/monitor setup, joint success and held-out fine-tuning; AppendixB pp14–15: task judges, construction and excluded task; AppendixD.1–D.2 pp24–25: successful-side-task filtering, balancing/dropped tasks and model-specific scaffolds; AppendixJ–M pp38–43: scratchpad sanity check, failure-mode dependence and human baseline

**Visual check:** Figures7–8 visually checked on PDF p7; other selected captions/text inspected but not comprehensive figure review or curve digitization.

**Findings:**

- SHADE-Arena separates completing a benign main task, a supplied harmful side task and evading a monitor. Overall success requires all three; a model can score on marginal outcomes without joint success.
- Monitor ROC evaluations keep successful side-task attacks, rebalance task contributions and drop task pairs without successful attacks. Full-transcript detection after the event is different from preventing harmful actions.
- Fine-tuned GPT 4o improves on held-out task pairs; turn-by-turn monitoring and prompting/requerying depend on failure mode and cost. Removing hidden-scratchpad instructions reduces sabotage, whereas revealing an assumed-hidden scratchpad is explicitly an artificially easy sanity check.

**Counterevidence / alternative:** Complex agent tasks and positive held-out monitor improvements expand the evidence beyond MCQs. Task heterogeneity, execution bottlenecks, post-hoc detection and conditional analysis prevent a universal monitor-performance or human-replacement claim.

**Limits:** Constructed synthetic environments, instructed side goals, selected agents/scaffolds and few tasks. Some task evaluation uses Claude 3.7 judgments. Human ratings cover 32 transcripts, so their AUC cannot be directly compared with full-set monitor AUC. No spontaneous sabotage or deployed harm estimate.

**Replication:** `not_performed`. **Numerical check:** No experimental replication or curve recomputation. Figure8’s 0.87 AUC is the Gemini 2.5 Pro monitor against Claude 3.7 attack transcripts; its other attacker curve differs. Avoid pooling this with the small human subset. Seventeen constructed task pairs include one excluded task (AppendixB.3), so do not infer every aggregate uses all17.

**Relevance:** `claim_evidence`. **Claim links:** [C73](claims.md#c73)

**Relevance rationale:** Adds a previously unresolved source role while distinguishing observed signals, induced behavior, controls and monitor endpoints. A new reading does not prove an earlier reader read this text.

**Next check:** Use the joint/conditional endpoints explicitly; test live interruption, operational false-positive budgets, matched human subsets and held-out methods before deployment assurance.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2506.15740v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2506.15740v2) |
| `attempted_at` | 2026-11-14T23:25:51.403522+00:00 |
| `retrieved_at` | 2026-11-14T23:25:51.904492+00:00 |
| `sha256` | f9c1656907b7387faad5099d405d048a0346071bea8dbffc0b68962a278330f4 |
| `byte_length` | 3703037 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary PDF bytes are retained privately. Independent archival preservation is not claimed. |
| `published_on` | 2025-07-08 |
| `version_claim` | arXiv:2506.15740v2,8 July2025; PDF title SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents |
| `locator_basis` | One-based PDF viewer pages; printed page numbers agree. Section/figure/appendix locators identify the pinned edition. |
| `capture_path` | .source-captures/synthesis-f9c1656907b7387faad5099d405d048a0346071bea8dbffc0b68962a278330f4.pdf |

<a id="r4_judges_01"></a>
### r4_judges_01

**Source:** `lambert_rewardbenchevaluating_2024`. **Theme:** judge_validity. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Pinned arXiv identifier, title and author list match the authoritative preprint record. This checks the named arXiv edition, not identity with a later proceedings artifact.

**Inspected scope:** ArXiv v2: abstract; introduction/background and benchmark construction/scoring text on PDF pp1–5; Table2 and scoring continuation p6; §5.3 and conclusion p9; AppendixA and opening AppendixB p16. Other results, many appendices, references, original datasets and code not comprehensively read.

**Locators:** v2 §§3–4.2 pp4–6; Table1 p3; §5.3 and §6 p9; AppendixA and AppendixB opening p16

**Visual check:** Extracted text, table cells and figure captions only; no rendered RewardBench plot or full figure inspection.

**Findings:**

- The toolkit compares reward models on structured chosen/rejected pairs spanning chat, difficult instruction following, safety and reasoning; safety includes both should-refuse and should-respond subsets.
- The score mixes per-prompt and category averaging; reasoning balances math/code and Prior Sets receive half weight in this edition. A displayed average needs its exact scoring recipe.
- AppendixA explicitly leaves downstream-training correlation unresolved and notes contamination and possible formatting shortcuts; AppendixB length controls test discrimination without length as a useful proxy.

**Counterevidence / alternative:** Structured contrasts and should-respond checks are affirmative diagnostic contributions. They do not show that a higher aggregate score improves every optimized policy or faithfully represents all human values.

**Limits:** Semi-automatic chosen/rejected construction with manual validation and benchmark reuse. No new dataset audit or downstream optimization experiment; full44-page object not read. Later NAACL edition metadata is separate from the v2 content check.

**Replication:** `not_performed`. **Numerical check:** Documentary reading only. No numerical recomputation, model execution or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C74](claims.md#c74)

**Relevance rationale:** Adds a defined evaluator-validity role with affirmative evidence and limits. Related editions and shared benchmark lineage are not independent corroboration.

**Next check:** Use pinned scoring/data versions and a downstream validation design for the intended training recipe; inspect final proceedings text before treating its content as equivalent.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2403.13787v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2403.13787v2) |
| `retrieved_at` | 2026-11-14T23:26:15.552851Z |
| `attempted_at` | 2026-11-14T23:26:15.358951Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific independent archive was available in this bounded round. Exact primary bytes and version URLs are retained locally; independent archival preservation is not claimed. |
| `sha256` | 1fd2c5532ac0b5511bdebea15d270853a36c9a48dfb6d8bed4bf8cd8665a7728 |
| `byte_length` | 1121878 |
| `mime_type` | application/pdf |
| `published_on` | 2024-06-08 |
| `version_claim` | arXiv:2403.13787v2, 8 June2024 |
| `locator_basis` | PDF viewer pages count the cover and agree with printed page numbers unless separately stated; named sections/tables/figures are edition-specific. |
| `capture_path` | .source-captures/synthesis-1fd2c5532ac0b5511bdebea15d270853a36c9a48dfb6d8bed4bf8cd8665a7728.pdf |

<a id="r4_judges_02"></a>
### r4_judges_02

**Source:** `frick_evaluaterewardrlhf_2024`. **Theme:** judge_validity. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Pinned arXiv identifier, title and author list match the authoritative preprint record. This checks the named arXiv edition, not identity with a later proceedings artifact.

**Inspected scope:** ArXiv v2: selected dataset/method sections3–5 and main §§6–9 on PDF pp3–10; AppendixA.3 DPO configuration, A.4 vote details and opening A.5 style-controlled comparison pp28–29. Not the entire30-page object or all result tables/code.

**Locators:** v2 §§4.1–5.2 pp4–6; §§6–8 pp7–10; Figures3–4 p9; AppendixA.3–A.5 pp28–29

**Visual check:** Rendered PDF p9 and inspected Figures3–4 metric/category matrices and captions. Other plots/tables were read selectively in extracted text; no plot digitization.

**Findings:**

- The preprint reports an end-to-end DPO comparison of nine reward models followed by12,190 blinded human-preference votes, connecting proxy metrics with downstream policy evaluations under that recipe.
- Granular pairwise accuracy is more predictive than some aggregate ranking/correlation metrics in this selected comparison; correctness and user preference need not coincide.
- PPE’s human-preference curation removes potentially harmful conversations and its correctness curation selects prompts with discriminating correct/incorrect samples. Neither is an unrestricted harm or population-impact evaluation.

**Counterevidence / alternative:** This is empirical downstream validation beyond standalone benchmark ranking, but selecting top RewardBench models limits score range and does not establish a universal sign of correlation. Different base models, online PPO and changed preferences remain open.

**Limits:** Nine selected popular/high-performing reward models, one Llama3.1-8B-Instruct base policy and off-policy DPO. Crowdsourced preference users/prompts and filtered data are not a representative public-value sample. No code/data reconstruction, training or independent re-estimation. Final ICLR artifact is separately inspected.

**Replication:** `not_performed`. **Numerical check:** Reported nine-model design and12,190-vote count checked against methods/appendix text; no vote-level recount, correlation re-estimation or model experiments. Figures report multiple metric/category coefficients; a single unqualified0.77 is not adopted.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Edition/publication context only; not additional empirical corroboration or a complete canonical-paper reading.

**Next check:** Use the separately captured final-paper qualifications and an exact metric/aggregation definition before quoting the inherited0.77 summary as predictive validity.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2410.14872v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2410.14872v2) |
| `retrieved_at` | 2026-11-14T23:26:15.723440Z |
| `attempted_at` | 2026-11-14T23:26:15.359697Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific independent archive was available in this bounded round. Exact primary bytes and version URLs are retained locally; independent archival preservation is not claimed. |
| `sha256` | c696a853a5e3577358b43e9b26af18a9ec3228e838518af97bd2def0cb1c9055 |
| `byte_length` | 1816954 |
| `mime_type` | application/pdf |
| `published_on` | 2024-10-22 |
| `version_claim` | arXiv:2410.14872v2, 22 October2024 |
| `locator_basis` | PDF viewer pages count the cover and agree with printed page numbers unless separately stated; named sections/tables/figures are edition-specific. |
| `capture_path` | .source-captures/synthesis-c696a853a5e3577358b43e9b26af18a9ec3228e838518af97bd2def0cb1c9055.pdf |

<a id="r4_judges_03"></a>
### r4_judges_03

**Source:** `frick_evaluaterewardrlhf_2024`. **Theme:** judge_validity. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Official ICLR proceedings metadata and PDF identify the same title and nine authors as canonical arXiv2410.14872. The canonical record is explicitly the2024 preprint; this2025 proceedings artifact is related_edition. Only selected critical text was compared, not complete equivalence.

**Inspected scope:** Official ICLR2025 PDF: cover/abstract/title/authors and introduction p1; complete §§6–8 and conclusion on pp7–10; AppendixA.6 text and A.6.1 reward-benchmark interpretation pp33–34; selected A.6.2 style-control table/figure text pp34–35; A.6.3, A.7 and A.8 p36. Other main methods/results, references and appendices not read in full.

**Locators:** Final §§6.1–6.2 pp7–8; §7 pp8–9, Figures5–6 p9; §8 p10; AppendixA.6.1 p34; A.6.3/A.7 p36

**Visual check:** Rendered and inspected final PDF p9 Figures5–6, including labels and category-specific positive/negative coefficients; did not independently inspect all final plots.

**Findings:**

- Final methods retain the nine-reward-model/one-base DPO experiment and12,190 blinded preference votes; the source explicitly limits transfer to other base policies and RL algorithms.
- Final AppendixA.6.1 labels over-optimization to RewardBench as a hypothesis, not an isolated cause; it explicitly permits that initial benchmark improvements may still predict downstream improvements.
- The final paper adds an economical recommended configuration using the human-preference set and MATH accuracy, while the low-quantile robustness explanation remains tentative.

**Counterevidence / alternative:** The study provides constructive criteria for choosing a reward-model evaluation and also a counterexample to treating all benchmark rankings as downstream guarantees. One selected experiment cannot establish general RewardBench invalidity or guarantee that optimizing PPE yields out-of-sample gains.

**Limits:** Official final edition matches title/authors but is36 pages versus the30-page inspected preprint and has additional analysis/renumbered figures. It is related-edition evidence, not a complete-read upgrade or certification that all preprint/final claims are identical. Same underlying study, not another independent outcome test.

**Replication:** `not_performed`. **Numerical check:** Documentary method/count and visual figure checks, not replication. Final Figure5 overall human-preference accuracy correlation is0.73, with other category/aggregation values; conclusion reports77%. Exact mapping of that summary to the plotted/aggregated metric is not established here. Omit a generic0.77 predictive-validity claim; this is not an asserted numerical error.

**Relevance:** `claim_evidence`. **Claim links:** [C74](claims.md#c74)

**Relevance rationale:** Adds a defined evaluator-validity role with affirmative evidence and limits. Related editions and shared benchmark lineage are not independent corroboration.

**Next check:** Validate metric selection/aggregation on held-out reward models, other base policies and online optimization if broad predictive claims are needed; retain qualitative findings without an unqualified headline coefficient.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e01083b381b4865919b4915ef32e3d2-Paper-Conference.pdf) |
| `final_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e01083b381b4865919b4915ef32e3d2-Paper-Conference.pdf) |
| `retrieved_at` | 2026-11-14T23:31:10.955349Z |
| `attempted_at` | 2026-11-14T23:31:10.165852Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific independent archive was available in this bounded round. Exact primary bytes and version URLs are retained locally; independent archival preservation is not claimed. |
| `sha256` | 4f72c1529c8f693a7f371e60286b553cfee761f7773ccb2a31be3d4d63cfbbb4 |
| `byte_length` | 1648113 |
| `mime_type` | application/pdf |
| `published_on` | 2025 |
| `version_claim` | Official ICLR2025 conference PDF;36 pages |
| `locator_basis` | PDF viewer pages count the cover and agree with printed page numbers unless separately stated; named sections/tables/figures are edition-specific. |
| `capture_path` | .source-captures/synthesis-4f72c1529c8f693a7f371e60286b553cfee761f7773ccb2a31be3d4d63cfbbb4.pdf |

<a id="r4_judges_04"></a>
### r4_judges_04

**Source:** `wang_selftaughtevaluators_2024`. **Theme:** judge_validity. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Pinned arXiv identifier, title and author list match the authoritative preprint record. This checks the named arXiv edition, not identity with a later proceedings artifact.

**Inspected scope:** Complete16-page arXivv2 accessible text: abstract, §§1–9, acknowledgments, all references, AppendixA.1–A.4, every table1–12 and Figure1–10 caption/template/example text. No linked model weights, code, WildChat records or benchmark datasets executed/read exhaustively.

**Locators:** §§3.1–4.3 pp3–5; Figure1 p2; §§5–6 pp5–9, Tables1–6 pp6,8; §8 p9; AppendixA.3/Table9 pp12–13; Tables10–12 p14

**Visual check:** Rendered and inspected p2 method diagram and p6 Tables1–4; p7 Figures3–6 distributions. All other table cells, templates, example and captions read in extracted text. No claim of visually checking every appendix template or reproducing plots.

**Findings:**

- Iterative synthetic preference/judgment training improves the reported RewardBench result and HelpSteer2 average/position-consistent agreement over the seed, without newly supplied human-preference labels in that training loop.
- Success depends on constructing a likely worse response by changing the instruction, selecting reasoning prompts and rejection-sampling judgments that agree with the synthetic preference. Each iteration trains again from the original seed.
- MT-Bench agreement improvements are smaller and not monotonic across iterations; ties are excluded. Some RewardBench Chat/category results worsen even while the overall score improves.
- AppendixA.3 tests response order, showing substantial residual order sensitivity in the same fifth-iteration model and recommends averaging both orderings. Classifier reward models can still outperform the generative recipe.

**Counterevidence / alternative:** This is affirmative evidence that synthetic training can improve a judge under tested endpoints. It does not make judgments independent of the seed/constructed data, demonstrate universally better evaluation or prove downstream RL policy gains. Added majority-vote inference has a different sampling cost.

**Limits:** Llama3-70B-Instruct seed and a specific synthetic-pair construction/filtering recipe; human-written WildChat inputs, pretrained/aligned seed and human-reference evaluation remain. No causal isolation of all training components or test of universal fairness/independent judgments. No inference-cost evaluation or smaller-model demonstration.

**Replication:** `not_performed`. **Numerical check:** Documentary reading of reported tables only. Table9 reports85.5 versus91.1 when the preferred response is always first versus last; their average is88.3, consistent with the stated two-order protocol. No training or independent benchmark-scoring reproduction; no cross-paper aggregate headline improvement is used.

**Relevance:** `claim_evidence`. **Claim links:** [C75](claims.md#c75)

**Relevance rationale:** Adds a defined evaluator-validity role with affirmative evidence and limits. Related editions and shared benchmark lineage are not independent corroboration.

**Next check:** Pin exact RewardBench implementation/aggregation and inference budget for numerical comparisons; test downstream policy effects, broader tasks and adversarially selected failures before claiming general evaluator replacement.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2408.02666v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2408.02666v2) |
| `retrieved_at` | 2026-11-14T23:26:15.702072Z |
| `attempted_at` | 2026-11-14T23:26:15.360051Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific independent archive was available in this bounded round. Exact primary bytes and version URLs are retained locally; independent archival preservation is not claimed. |
| `sha256` | 1bcdb416f2f49ab2dd6f60684f27f9479af5600f6acd5a1496d044af82ee24a7 |
| `byte_length` | 1674475 |
| `mime_type` | application/pdf |
| `published_on` | 2024-08-08 |
| `version_claim` | arXiv:2408.02666v2, 8 August2024 |
| `locator_basis` | PDF viewer pages count the cover and agree with printed page numbers unless separately stated; named sections/tables/figures are edition-specific. |
| `capture_path` | .source-captures/synthesis-1bcdb416f2f49ab2dd6f60684f27f9479af5600f6acd5a1496d044af82ee24a7.pdf |

<a id="r4_judges_05"></a>
### r4_judges_05

**Source:** `calderon_alternativeannotator_2025`. **Theme:** judge_validity. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact publisher URL/DOI, title, three authors, ACL2025 venue and printed pages match the authoritative proceedings record.

**Inspected scope:** ACL final31-page PDF: abstract; complete method§3 pp3–6; selected setup/results§§4–5 pp6–9 including Tables1–2 and Figure2; conclusion§6 p9; complete limitations§7 p10. AppendixB.1–B.2 pp17–18; selected B.3/C.1 explanation and weighting formula pp18–19; C.4 subjectivity/options and C.5 opening pp20–21. Full theorem proof, references, full dataset appendix and prompt appendices not read.

**Locators:** §§3.1–3.3 pp3–5/printed16053–16055; §5.1/Figure2 p9; §7 p10; AppendixB.1–B.2 pp17–18; C.1 pp18–19; C.4 pp20–21

**Visual check:** Rendered and inspected Figure2 on PDFp9, including sample-size/epsilon curves and legend. Other method equations/table cells read in extracted text; no full graphical appendix inspection.

**Findings:**

- The test formalizes a local replacement decision through leave-one-annotator-out alignment, paired comparisons and Benjamini–Yekutieli FDR control; it supplies more explicit uncertainty/decision structure than a raw agreement threshold.
- Passing is sensitive to the cost-benefit epsilon, sample size, human comparator and annotation aspect. The suggested50–100 examples is a study-specific practical guideline, not a universal assurance sample size.
- AppendixC.1 acknowledges that an always-majority-label predictor can pass under severe imbalance and proposes inverse-probability weighting. C.4 proposes minority-sensitive weighting/score changes because matching the majority is not automatically the right objective.

**Counterevidence / alternative:** Empirical passes in some tested tasks are constructive evidence for task-specific substitution. Contamination, weak or inappropriate human comparators, label imbalance and subjective minority views bound the inference. A pass is not proof of truth, public legitimacy or human-free research validation.

**Limits:** The reference is the sampled human-annotation distribution, normally used as a proxy for unavailable gold labels. Human expertise, task/aspect, score function, cost-benefit epsilon and winning threshold are substantive choices. No theorem-proof recertification or data/code reproduction.

**Replication:** `not_performed`. **Numerical check:** No statistical tests or dataset results rerun. Read the paper’s FDR and winning-rate definitions and the epsilon/sample-size sensitivity analysis. No blanket nine-of-ten replacement rate or fixed universal minimum sample is promoted.

**Relevance:** `claim_evidence`. **Claim links:** [C76](claims.md#c76)

**Relevance rationale:** Adds a defined evaluator-validity role with affirmative evidence and limits. Related editions and shared benchmark lineage are not independent corroboration.

**Next check:** Before applying to this project, define the judgment, human calibration sample/expertise, epsilon, imbalance correction and failure costs, and validate across the actual publication tasks. No existing project annotation is recertified by this reading.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://aclanthology.org/2025.acl-long.782.pdf) |
| `final_url` | [Source](https://aclanthology.org/2025.acl-long.782.pdf) |
| `retrieved_at` | 2026-11-14T23:25:58.109605Z |
| `attempted_at` | 2026-11-14T23:25:57.377815Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific independent archive was available in this bounded round. Exact primary bytes and version URLs are retained locally; independent archival preservation is not claimed. |
| `sha256` | 2e166a7a7c71cc45ee21ce72dae3ac1370c3fffc11b48ad5dcd20bfdd9b05cdf |
| `byte_length` | 1019668 |
| `mime_type` | application/pdf |
| `published_on` | 2025-07 |
| `version_claim` | ACL2025 final paper, DOI10.18653/v1/2025.acl-long.782, pp16051–16081 |
| `locator_basis` | PDF viewer pages count the cover and agree with printed page numbers unless separately stated; named sections/tables/figures are edition-specific. |
| `capture_path` | .source-captures/synthesis-2e166a7a7c71cc45ee21ce72dae3ac1370c3fffc11b48ad5dcd20bfdd9b05cdf.pdf |

<a id="r4_judges_06"></a>
### r4_judges_06

**Source:** `dubois_skewedscore_2025`. **Theme:** judge_validity. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Pinned arXiv identifier, title and author list match the authoritative preprint record. This checks the named arXiv edition, not identity with a later proceedings artifact.

**Inspected scope:** Complete20-page arXivv3 accessible text: abstract/introduction, framework, Questions1.1–5 and conclusion, both reference pages, AppendicesA–C, Tables1–3 and all Figures1–11 captions. Linked HiBayes package/notebooks not executed or independently validated.

**Locators:** Framework and Table1 pp2–3; illustrative-data declaration p4; Questions1.1–4 pp4–12; Figure6 p11; Question5 pp12–13; AppendicesA–C pp16–20

**Visual check:** Rendered and inspected Figure6 on p11 to distinguish raw agreement, posterior prediction and bias-adjusted model counterfactual. All other captions/tables/equations read in extracted text; plots not independently digitized or all visually checked.

**Findings:**

- Bayesian ordinal/binomial GLMs provide a coherent way to model grader/item/model effects, uncertainty and structured dependence while addressing the primary model-comparison question.
- The demonstrations distinguish systematic score-scale differences from residual disagreement, and represent a bias-adjusted agreement scenario through posterior predictions rather than equating low raw agreement with random noise.
- AppendixB shows some more complex models perform similarly to simpler alternatives and recommends simplicity unless justified. AppendixC warns that ordinal one-point differences are not equal-sized effects across the scale.

**Counterevidence / alternative:** The simulations and implementation recipe are affirmative methodological contributions. They do not demonstrate the magnitude or cause of real grader bias, validate the chosen reference judgments, or show that a modeled bias correction improves deployed decisions.

**Limits:** All worked examples use simulated data and a fictional researcher. Inferences depend on the likelihood, covariates, dependence structure, priors and human-reference objective; a model-adjusted prediction is not an observed intervention effect. No external grader-error prevalence or empirical validation on this project is supplied.

**Replication:** `not_performed`. **Numerical check:** No GLM fits/notebooks, intervals or agreement metrics reproduced. Figure6’s corrected agreement is explicitly a model-based counterfactual on simulated data, not a measured improvement in this project.

**Relevance:** `claim_evidence`. **Claim links:** [C77](claims.md#c77)

**Relevance rationale:** Adds a defined evaluator-validity role with affirmative evidence and limits. Related editions and shared benchmark lineage are not independent corroboration.

**Next check:** Apply a preregistered measurement model to an actual held-out calibration set, assess fit/priors/dependence and practical equivalence, and compare simpler models before claiming real error correction or project-specific bias estimates.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2507.03772v3) |
| `final_url` | [Source](https://arxiv.org/pdf/2507.03772v3) |
| `retrieved_at` | 2026-11-14T23:26:15.832990Z |
| `attempted_at` | 2026-11-14T23:26:15.360427Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific independent archive was available in this bounded round. Exact primary bytes and version URLs are retained locally; independent archival preservation is not claimed. |
| `sha256` | 89c5aa510c6503fc5519043ecf7095a047d7d6e939660e33e864d917a8c39a74 |
| `byte_length` | 4077901 |
| `mime_type` | application/pdf |
| `published_on` | 2026-02-26 |
| `version_claim` | arXiv:2507.03772v3, 26 February2026 |
| `locator_basis` | PDF viewer pages count the cover and agree with printed page numbers unless separately stated; named sections/tables/figures are edition-specific. |
| `capture_path` | .source-captures/synthesis-89c5aa510c6503fc5519043ecf7095a047d7d6e939660e33e864d917a8c39a74.pdf |

<a id="r4_judges_07"></a>
### r4_judges_07

**Source:** `lambert_rewardbenchevaluating_2024`. **Theme:** judge_validity. **Reading:** Metadata only. **Coverage effect:** `none`.

**Edition match:** `related_edition`. Official publisher metadata matches the canonical preprint’s title and twelve authors, but identifies a later2025 published representation with a different DOI. Treat as related_edition; no full-text equivalence asserted.

**Inspected scope:** Official ACL Anthology metadata fields: title, twelve authors, Findings of NAACL2025, April2025, DOI10.18653/v1/2025.findings-naacl.96 and pp1755–1797. Final PDF body not retrieved/read in this event.

**Locators:** ACL Anthology2025.findings-naacl.96 metadata: title/authors/venue/month/DOI/pages

**Visual check:** None; metadata text only.

**Findings:**

- The previously proposed NAACL publication lead is corroborated by official publisher metadata; the existing2024 citation key and authoritative preprint identity remain unchanged.

**Counterevidence / alternative:** A later peer-reviewed representation supplies publication context, not another independent study or automatic proof of all preprint claims.

**Limits:** Publication identity does not establish complete preprint/final textual equivalence or validate empirical findings. No new paper full-text coverage or independent corroboration.

**Replication:** `not_performed`. **Numerical check:** None; metadata-only identity/venue check.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Edition/publication context only; not additional empirical corroboration or a complete canonical-paper reading.

**Next check:** If citing final-paper methods/results, inspect its exact PDF and reconcile changes before substituting it for the pinned preprint.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://aclanthology.org/2025.findings-naacl.96/) |
| `final_url` | [Source](https://aclanthology.org/2025.findings-naacl.96/) |
| `retrieved_at` | 2026-11-14T23:32:44.606659Z |
| `attempted_at` | 2026-11-14T23:32:44.018202Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked capture-specific independent archive was available in this bounded round. Exact primary bytes and version URLs are retained locally; independent archival preservation is not claimed. |
| `sha256` | 657e09246f6e45ae5e2c348912fa5c4e0117bb6db59524c61b97d247716a230c |
| `byte_length` | 48648 |
| `mime_type` | text/html |
| `published_on` | 2025-04 |
| `version_claim` | ACL Anthology Findings of NAACL2025 metadata |
| `locator_basis` | Publisher metadata fields title, author list, venue, date, DOI and page range; not a full proceedings-paper reading. |
| `capture_path` | .source-captures/synthesis-657e09246f6e45ae5e2c348912fa5c4e0117bb6db59524c61b97d247716a230c.html |

<a id="r4_depthsample_01"></a>
### r4_depthsample_01

**Source:** `fmf_preliminarytaxonomy_2024`. **Theme:** inherited_depth_sample. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact article title, issuer and December 20, 2024 posted date match the canonical brief; the /updates/ route is the ledger-recorded moved route. The capture authenticates the current page, not historical byte identity.

**Inspected scope:** Complete accessible text of captured HTML: introduction, methods, objectives, uplift discussion, Table 1 cells, conclusion, all 3 footnotes, related-post labels, navigation/footer. Linked works were not opened.

**Locators:** Recommended Taxonomy / Methodology; Objective / Maximal Capability Evaluations / Safeguard evaluations / Uplift studies; Table 1 Safety Evaluations; Conclusion and Footnotes

**Visual check:** HTML table cells read as text; no browser screenshot, external assets or independent visual layout check.

**Findings:**

- The brief separates evaluation methodology (benchmarks, red teaming, controlled trials) from objectives (maximal capability, safeguards, human uplift).
- Threat-model resources constrain maximal-capability testing, and safeguard retesting is recommended after model/tool/integration changes.

**Counterevidence / alternative:** A terminology framework can improve specification without proving that a benchmark or controlled trial predicts deployment harm. Methods may serve several objectives.

**Limits:** Preliminary public-literature/member-expert taxonomy, not an empirical validation of risk prediction. Current HTML does not authenticate the earlier reader or earlier response bytes. The EO identifier printed in a footnote is not adopted.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental replication.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Useful conceptual crosswalk for the broad review; no forced empirical claim and no independent corroboration from an industry taxonomy.

**Next check:** Use as vocabulary background and verify primary legal text if the EO footnote is ever needed; do not treat it as outcome evidence.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://www.frontiermodelforum.org/updates/issue-brief-preliminary-taxonomy-of-pre-deployment-frontier-ai-safety-evaluations/) |
| `final_url` | [Source](https://www.frontiermodelforum.org/updates/issue-brief-preliminary-taxonomy-of-pre-deployment-frontier-ai-safety-evaluations/) |
| `retrieved_at` | 2026-11-14T23:26:12.159366Z |
| `attempted_at` | 2026-11-14T23:26:11.541284Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact local bytes and primary URLs are retained; independent archival preservation is not claimed. |
| `sha256` | e700e69396b29f0147a91ccfde354ce88e18ba6edea79d623d789e4199cbdbb2 |
| `byte_length` | 112835 |
| `mime_type` | text/html |
| `published_on` | 2024-12-20 |
| `version_claim` | FMF issue brief posted December 20, 2024; current captured /updates/ representation |
| `locator_basis` | Version-specific section headings and source-attributed dates; PDF viewer pages and printed pages separately identified where applicable. |
| `capture_path` | .source-captures/synthesis-e700e69396b29f0147a91ccfde354ce88e18ba6edea79d623d789e4199cbdbb2.html |

<a id="r4_depthsample_02"></a>
### r4_depthsample_02

**Source:** `aisi_safetyinstitutesjoint_2024`. **Theme:** inherited_depth_sample. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical issuer URL and o1 joint-evaluation overview, datedDecember 18, 2024. This object is explicitly a high-level overview; the linked 37-page report is separate.

**Inspected scope:** Complete accessible captured HTML text: Introduction, Overview, Methodology, selected findings in all 3 domains, Conclusion, report links, date/name-change note and footer. No linked report is included in this complete-page event.

**Locators:** Introduction; Overview of the Joint Safety Research & Testing Exercise; Methodology; Evaluations and Findings; Conclusion; Footer: research organisation within UK Department for Science, Innovation and Technology

**Visual check:** No plots/tables in this overview were independently rendered; accessible prose read in full.

**Findings:**

- US/UK institutes report limited pre-release access, scaffold adjustments for tool-calling/output-formatting problems and sharing findings before release.
- The overview reports comparison and tool-augmentation results with an explicit tested-version limitation; it does not endorse the release as safe.
- Issuer attribution and DSIT footer establish government-institute context rather than a private company issuer.

**Counterevidence / alternative:** Better elicitation or a different released version may perform differently. Reported external testing is not proof of a complete audit or harm prevented.

**Limits:** Complete-page reading is not a full technical-report read, independent human review or proof of the earlier reading. Results apply to the tested pre-deployment version/scaffolding; the overview itself warns about finite access and uncertainty.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C01](claims.md#c01)

**Relevance rationale:** Primary example of an actual external pre-deployment evaluation with explicit configuration/resource limits; supports C01 without claiming effects or complete assessment.

**Next check:** Use exact technical methods before quoting rates; preserve separate overview/report scopes and historical institute names.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://www.aisi.gov.uk/blog/pre-deployment-evaluation-of-openais-o1-model) |
| `final_url` | [Source](https://www.aisi.gov.uk/blog/pre-deployment-evaluation-of-openais-o1-model) |
| `retrieved_at` | 2026-11-14T23:26:12.520645Z |
| `attempted_at` | 2026-11-14T23:26:11.541892Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact local bytes and primary URLs are retained; independent archival preservation is not claimed. |
| `sha256` | 827419fa116269ecba52bedcd9826f306352a070da378d64db1287de7c0ee6d7 |
| `byte_length` | 31277 |
| `mime_type` | text/html |
| `published_on` | 2024-12-18 |
| `version_claim` | Issuer overview datedDecember 18, 2024; later AISI name-change note and current footer |
| `locator_basis` | Version-specific section headings and source-attributed dates; PDF viewer pages and printed pages separately identified where applicable. |
| `capture_path` | .source-captures/synthesis-827419fa116269ecba52bedcd9826f306352a070da378d64db1287de7c0ee6d7.html |

<a id="r4_depthsample_03"></a>
### r4_depthsample_03

**Source:** `aisi_safetyinstitutesjoint_2024`. **Theme:** inherited_depth_sample. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. 37-page December 2024 US/UK technical report linked directly from the canonical overview. Companion report for the same exercise, not the identical HTML object or an independent study.

**Inspected scope:** PDF cover/contents pp1–3; printedpp1–7/viewerpp4–10 (Introduction, disclaimers, complete general methods, US Cybench methods/results/Table 4.1); viewerp12/printedp9 (future-work discussion/UK methods opening); printedpp11–14/viewerpp14–17 (UK agent setup/results, selected domain discussions); printedpp17–20/viewerpp20–23 (LAB-Bench methods, tooling, scoring and selected results). Plot text on viewerp11 was partly unreadable and is not used for numerical claims. Other pages/remaining software/AI sections/references were not fully read.

**Locators:** §§1–2.6 printedpp1–4 / viewerpp4–7; §§3–5; Table 4.1 printedpp5–9 / viewerpp8–12; PartI overview printedp5; §7 printedp11; Figure 7.1 printedp12 / viewerp15; §§9–10.4 printedpp17–20 / viewerpp20–23

**Visual check:** Rendered/visually checked Table 4.1 continuation on viewerp10 and Figures 7.1–7.2 on viewerp15. Other plots were not visually authenticated or digitized.

**Findings:**

- The report specifies development-set elicitation/scaffold repair before final runs and warns comparisons need not rank suitability for real applications.
- US Cybench methods use40 tasks,10 attempts each and up to100 messages. Table 4.1 reports45% Pass@10 for o1 versus35% for the strongest reference; these are configured challenge results.
- LAB-Bench tool ablations, abstention rules and a separate accuracy@20 procedure show how access and scoring affect biological-task comparisons. No biological outcome or misuse incidence is measured.

**Counterevidence / alternative:** Reported capability gains are real within the protocol, while narrow tasks, resource limits and altered configurations constrain transfer. Biological-tool gains and the US cryptography result do not establish general dominance or deployed risk.

**Limits:** Limited access, incomplete mitigations, scaffold dependence and fixed attempts/message budgets rather than equal costs bound model comparisons. General-method error bars exclude variation in scaffold design. Source capture closes the prior PDF access gap for these sections only; no full-report or experiment-reproduction claim.

**Replication:** `not_performed`. **Numerical check:** Documentary comparison only. US Table 4.1 clearly separates Pass@1 from Pass@10. UK PartI overview printedp5 gives46% at apprentice Pass@10, while §7 printedp11 and issuerHTML give36% with the same label versus46% reference. Figure 7.1 was visually checked but its aggregation is not established by this bounded read. Private task/run data and weighting were not inspected, so no error cause or corrected rate is asserted; affected UK headline omitted.

**Relevance:** `claim_evidence`. **Claim links:** [C01](claims.md#c01)

**Relevance rationale:** Deepens C01 with actual methods, positive results and counterevidence. Same joint exercise as the overview, not a second independent validation.

**Next check:** Omit the UK apprentice headline until its differently reported figures/aggregation are reconciled; preserve the supported qualitative configuration finding and US metric scope.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://cdn.prod.website-files.com/663bd486c5e4c81588db7a1d/6763fac97cd22a9484ac3c37_o1_uk_us_december_publication_final.pdf) |
| `final_url` | [Source](https://cdn.prod.website-files.com/663bd486c5e4c81588db7a1d/6763fac97cd22a9484ac3c37_o1_uk_us_december_publication_final.pdf) |
| `retrieved_at` | 2026-11-14T23:27:09.054549Z |
| `attempted_at` | 2026-11-14T23:27:08.564687Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact local bytes and primary URLs are retained; independent archival preservation is not claimed. |
| `sha256` | 1152b10cb28865acf923e97de9adb2e9d915dda94fd1950f5bd36ce06188f229 |
| `byte_length` | 2132284 |
| `mime_type` | application/pdf |
| `published_on` | 2024-12 |
| `version_claim` | December 2024 technical report linked from December18 issuer overview |
| `locator_basis` | Version-specific section headings and source-attributed dates; PDF viewer pages and printed pages separately identified where applicable. |
| `capture_path` | .source-captures/synthesis-1152b10cb28865acf923e97de9adb2e9d915dda94fd1950f5bd36ce06188f229.pdf |

<a id="r4_depthsample_04"></a>
### r4_depthsample_04

**Source:** `metr_timehorizons_2026`. **Theme:** inherited_depth_sample. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical living measurement page and named Time Horizon 1.1 suite match the record. Current page displays last updatedSeptember 8, 2026; the prior May-dated snapshot/values are not authenticated. Same maintained-page record, explicitly a later captured state.

**Inspected scope:** Complete accessible captured HTML prose: definition, controls/labels, Methodological Details, every FAQ, update history, citation text, navigation/footer. Interactive chart values/embedded datasets, linked paper, code and follow-up studies were not read/reproduced.

**Locators:** Opening / LAST UPDATED / Time Horizon 1.1; Methodological Details / Task distribution / Human task duration estimates; FAQ: autonomous runtime, jobs,99% reliability, task meaning, evaluation procedure and reporting coverage; Updates: September 8, 2026 maintenance notice and March3 regularization correction

**Visual check:** No chart pixels, interactive values or external figure assets were independently inspected. Plot descriptions/captions are prose only.

**Findings:**

- The horizon is a fitted success-probability crossing on tasks measured by human expert completion time, not AI elapsed runtime.
- The page specifies self-contained mostly software/ML/cyber tasks, low-context human baselines, scaffold elicitation and six runs per test task, with reward-hack review.
- The page explicitly limits domain/job transfer, model-release completeness and higher-reliability inference, and says it is no longer actively updated.

**Counterevidence / alternative:** A common duration/reliability axis is useful for comparing tested agents, while low-context tasks, jagged domain capability and uncertain long-task estimates limit labor-automation or general-autonomy conclusions.

**Limits:** Complete accessible-page text is not a full data/paper audit. Current state cannot establish earlier reading or exact historic values. The page says measurements above 16 hours are unreliable with its suite; higher-reliability extrapolation is not measured here.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C78](claims.md#c78)

**Relevance rationale:** Supplies a measurement construct and transfer boundary relevant to the broad capability/configuration synthesis, not an autonomous-runtime claim.

**Next check:** Pin data/code and chart state before quoting model values or trends. Keep the current maintenance notice distinct from historical metadata.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://metr.org/time-horizons/) |
| `final_url` | [Source](https://metr.org/time-horizons/) |
| `retrieved_at` | 2026-11-14T23:26:12.287227Z |
| `attempted_at` | 2026-11-14T23:26:11.542262Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact local bytes and primary URLs are retained; independent archival preservation is not claimed. |
| `sha256` | 186c10c0ef80685095f7b197d53a78a45054b9896a2bb24a3735350d5f4475d9 |
| `byte_length` | 685671 |
| `mime_type` | text/html |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Current Time Horizon 1.1 page; LAST UPDATED September 8, 2026; no longer actively updated |
| `locator_basis` | Version-specific section headings and source-attributed dates; PDF viewer pages and printed pages separately identified where applicable. |
| `capture_path` | .source-captures/synthesis-186c10c0ef80685095f7b197d53a78a45054b9896a2bb24a3735350d5f4475d9.html |

<a id="r4_depthsample_05"></a>
### r4_depthsample_05

**Source:** `mlcommons_ailuminate_2026`. **Theme:** inherited_depth_sample. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical AILuminate suite URL/title match the 2026 record. Current page names Safety 1.2.1 and Jailbreak 1.1; no byte equivalence to April/earlier captured states is asserted.

**Inspected scope:** Complete accessible captured HTML text: suite descriptions, credibility/stewardship/objectivity sections,2026 timeline, results-use rules, Candela/configuration description, future benchmarks, contributor list, partnerships and footer/cookie text. Linked standards, result pages, prompts and benchmark code not read.

**Locators:** The suite of benchmarks / Safety 1.2.1 / Jailbreak 1.1; Technical independence / Stewardship / Objectivity; 2026 at a glance; Using AILuminate results; Privately test your own system

**Visual check:** No external graphics or browser screenshots inspected; the relevant version and usage statements are accessible prose.

**Findings:**

- Current suite distinguishes direct hazardous-request Safety from published-attack Jailbreak testing, with different category scopes.
- The issuer reports a purpose-built non-LLM evaluator starting with Safety 1.2.1/Jailbreak 1.1 and separates confidential Official runs from internal-use Practice results.
- The page expressly says MLCommons measures rather than certifies systems/audits organizations/decides acceptable risk; deployment configuration can change results.

**Counterevidence / alternative:** Confidential tests and structured rules can reduce some contamination/comparison problems, but do not prove an ungameable instrument or establish appropriate risk acceptance. Versioned evaluator changes matter.

**Limits:** Issuer account of instrument design/stewardship, not independently validated score comparability or real-world safety. Confidential prompts and evaluator details were not audited. Complete portal reading does not recertify linked papers or an earlier snapshot.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C79](claims.md#c79)

**Relevance rationale:** Adds constructive measurement/stewardship design with explicit assurance boundary and version dependence.

**Next check:** Inspect exact release methods/results and data when making a leading score-comparability claim; do not transfer v1.0 grading/evaluator details to 1.2.1.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://mlcommons.org/ailuminate/) |
| `final_url` | [Source](https://mlcommons.org/ailuminate/) |
| `retrieved_at` | 2026-11-14T23:26:12.090289Z |
| `attempted_at` | 2026-11-14T23:26:11.542648Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact local bytes and primary URLs are retained; independent archival preservation is not claimed. |
| `sha256` | 72fb5c9e6c2ca17e2cbbaf6c0dae68d069a5189ff3e5d4a0466488ae1ffa1749 |
| `byte_length` | 157454 |
| `mime_type` | text/html |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Current2026 suite overview naming Safety 1.2.1 and Jailbreak 1.1 |
| `locator_basis` | Version-specific section headings and source-attributed dates; PDF viewer pages and printed pages separately identified where applicable. |
| `capture_path` | .source-captures/synthesis-72fb5c9e6c2ca17e2cbbaf6c0dae68d069a5189ff3e5d4a0466488ae1ffa1749.html |

<a id="r4_depthsample_06"></a>
### r4_depthsample_06

**Source:** `mlcommons_ailuminatev10_2025`. **Theme:** inherited_depth_sample. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact canonical arXiv identifier/title match; pinned2503.05731v1, cover datedFebruary 19, 2025, benchmark releasev1.0. Generic arXiv page now offers v2; equivalence is not assumed.

**Inspected scope:** PDF pp1–5 cover/abstract/executive summary/contents; pp7–9 overview/scope/use; pp15–22 prompt-quality discussion, response-evaluator methods, grading/reference and limitations. Remaining hazard details, results, large Appendix A questionnaire and references not fully read.

**Locators:** §2 pp7–9: scope, basic approach and use; §§5–6 pp15–21: ensemble, entropy, human labels, false-safe tradeoff, reference-relative grading; §7 pp21–22: limitations; Figure 6 p21

**Visual check:** Figure 6 p21 rendered and visually inspected as a schematic evaluator-uncertainty/grade-band figure. Tables 2–3 read in extracted text; no empirical results digitized.

**Findings:**

- The v1.0 method provides a standard, confidential/practice prompts, an LLM ensemble plus human checks, and reference-relative grades.
- Entropy thresholds and ensemble logic prioritize low false-safe rates; the paper reports substantial evaluator uncertainty that can span grades.
- Explicit limits include single-turn constructed prompts, absent expert adaptive adversaries, US-cultural policy framing, unmeasured hazards and heterogeneous deployment configurations.

**Counterevidence / alternative:** Standardized evaluation offers useful repeatable targets and hazard-specific diagnosis; the paper itself supplies reasons not to equate a grade with general safety. Current portal instrumentation differs, so the two cannot be silently pooled.

**Limits:** Selected 51-page arXivv1 object only, not current implementation audit. Exact ensemble model/logic/training details are intentionally confidential. Benchmark grading/uncertainty and hazard categories are not field-harm estimates.

**Replication:** `not_performed`. **Numerical check:** No scoring/model reproduction. Documentary inspection of equations/reference definition and uncertainty discussion only; no claimed empirical uncertainty recalculation.

**Relevance:** `claim_evidence`. **Claim links:** [C79](claims.md#c79)

**Relevance rationale:** Methods/limitations complement the suite overview as one benchmark family, not independent empirical corroboration.

**Next check:** Read remaining Appendix A/results and exact later release methods if claims require them; verify first-author order and publication-versus-submission dating before metadata changes.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2503.05731v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2503.05731v1) |
| `retrieved_at` | 2026-11-14T23:26:12.085701Z |
| `attempted_at` | 2026-11-14T23:26:11.543016Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact local bytes and primary URLs are retained; independent archival preservation is not claimed. |
| `sha256` | 480273f4382dbfc411928ade3db96f7eec2bcf72365f3d2930e3124d0c44ff6b |
| `byte_length` | 2312460 |
| `mime_type` | application/pdf |
| `published_on` | 2025-02-19 |
| `version_claim` | arXiv2503.05731v1 cover datedFebruary 19, 2025; benchmarkv1.0 |
| `locator_basis` | Version-specific section headings and source-attributed dates; PDF viewer pages and printed pages separately identified where applicable. |
| `capture_path` | .source-captures/synthesis-480273f4382dbfc411928ade3db96f7eec2bcf72365f3d2930e3124d0c44ff6b.pdf |

<a id="r4_depthsample_07"></a>
### r4_depthsample_07

**Source:** `mlcommons_ailuminatev10_2025`. **Theme:** inherited_depth_sample. **Reading:** Abstract only. **Coverage effect:** `none`.

**Edition match:** `related_edition`. Generic canonical arXiv metadata page currently describesv2 revisedApril 18, 2025; used to distinguish version provenance from the inspectedv1 PDF.

**Inspected scope:** Complete visible arXiv metadata/abstract page text, author sequence and submission history, not v2 full paper.

**Locators:** Title/Authors/Abstract; Submission history v1/v2

**Visual check:** No figure/table inspection.

**Findings:**

- The displayed author order starts Shaona Ghosh and Heather Frase; Peter Mattson appears among the closing chairs.
- History lists v1 submissionFebruary 19, 2025 and v2 revisionApril 18, 2025; the canonical dateMarch 7 may encode a different publication/announcement event and is not corrected by assumption.

**Counterevidence / alternative:** Current metadata supplies identity/version clues, but cannot certify methods equivalence or prior reading.

**Limits:** Metadata/abstract does not certify v1–v2 methods or full author identity details beyond displayed ordering. Submission date need not equal intended public-publication date in records.yaml.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental replication.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Version/author provenance only; not an extra empirical study or full-paper read.

**Next check:** If editing bibliography metadata, use actual author order and distinguish submission/revision/publication dates.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/abs/2503.05731) |
| `final_url` | [Source](https://arxiv.org/abs/2503.05731) |
| `retrieved_at` | 2026-11-14T23:26:11.733057Z |
| `attempted_at` | 2026-11-14T23:26:11.543407Z |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact local bytes and primary URLs are retained; independent archival preservation is not claimed. |
| `sha256` | 1ca1355ce262b9fefa7561268096d13ce00a98c9a5a4890cd70917c9c75236f6 |
| `byte_length` | 61248 |
| `mime_type` | text/html |
| `published_on` | Not recorded / unavailable |
| `version_claim` | arXiv metadata page currentlyv2; revisionApril 18, 2025 |
| `locator_basis` | Version-specific section headings and source-attributed dates; PDF viewer pages and printed pages separately identified where applicable. |
| `capture_path` | .source-captures/synthesis-1ca1355ce262b9fefa7561268096d13ce00a98c9a5a4890cd70917c9c75236f6.html |

<a id="r4_editions_01"></a>
### r4_editions_01

**Source:** `cunningham_sparseautoencoders_2024`. **Theme:** edition_questions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Official ICLR2024 proceedings PDF linked from its exact titled proceedings entry. PDF title and five printed authors match the canonical arXiv-associated work and named venue; this is a separately captured final conference artifact, not asserted byte-identical to arXiv v3.

**Inspected scope:** PDF cover/§§1–2 pp1–3; complete §4 pp5–6 and Figure 4; selected §5 examples pp7–8; §6.1–6.3 p9; AppendixA–B text p12; AppendixE–G text pp17–19. Remaining §3, references, parts of §5 and appendices were not comprehensively reread. Text-diff discovery was followed by reading claim-critical passages; it is not a full 19-page certification.

**Locators:** §2 Equation 4/Figure 2 p3; §§4.1–4.2 pp5–6, Figure 4 p6; §6.2 p9; AppendixF/Figure 16 p19; AppendicesA–B p12; G pp17–19

**Visual check:** Rendered and visually inspected arXiv v3 Equation 4 on p3, final Equation 4/Figure 2 on p3 and IOI Figure 4 on p6; no plot digitization, remaining figures not comprehensively checked.

**Findings:**

- The exact ICLR artifact preserves the affirmative IOI result: sparse dictionary patches move Pythia410M outputs toward counterfactual target distributions with fewer directions/smaller edits than tested PCA/non-sparse dictionaries under per-decomposition ACDC ordering over 50 IOI datapoints.
- Final proceedings locators differ: main IOI result is Figure 4 (rather than arXiv v3 Figure 3), and cross-layer IOI plots are AppendixF/Figure 16 (rather than Figure 17).
- The representations differ at the text/formula level: the final PDF is 19 pages and Equation 4 divides squared reconstruction loss by dim(x); arXiv v3 is 20 pages and prints the unnormalized term. The final places a sparsity/reconstruction tradeoff figure in the main text and changes figure numbering. This documents representation changes, not a reproduced change in trained models or effect estimates.
- Final §6.2 still treats broader-task generalization as future work. The arXiv v3 perplexity25→40 sentence is not present in the final extracted text and must not be attributed to this final edition.

**Counterevidence / alternative:** Successful selected interventions remain positive causal evidence; reconstruction error, automated interpretation, task choice and feature-selection procedures bound scope. A changed printed normalization is not evidence that the underlying experiment was rerun or that the previous qualitative result is wrong.

**Limits:** Selected final-edition check only; no model/data execution, exhaustive cross-edition result comparison or full final-paper reading. No causal mechanism for changed wording is inferred.

**Replication:** `not_performed`. **Numerical check:** Documentary version/formula/locator comparison only, not experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C49](claims.md#c49)

**Relevance rationale:** Resolves or narrows a specific edition/denominator question without recertifying earlier reading, pooling related representations as independent evidence, or inferring model experiment replication.

**Next check:** Use the final artifact for its verified IOI claim/locators; retain separately scoped arXiv findings and do not transfer unverified numbers across editions. Compare code/training manifest only if quantitative normalization or across-edition result changes lead the publication.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2024/file/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Paper-Conference.pdf) |
| `final_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2024/file/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Paper-Conference.pdf) |
| `retrieved_at` | 2026-11-14T23:26:50.159336+00:00 |
| `attempted_at` | 2026-11-14T23:26:49.427968+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and immutable source URLs where available are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 13c0747d472efa103ae5a6898299bb805be87b7a8bda408b4286fe23a5287bcd |
| `byte_length` | 1818039 |
| `mime_type` | application/pdf |
| `published_on` | 2024 |
| `version_claim` | ICLR2024 official proceedings PDF;19 pages |
| `locator_basis` | Version-specific page/section locators; PDF viewer page numbers include cover. |
| `capture_path` | .source-captures/synthesis-13c0747d472efa103ae5a6898299bb805be87b7a8bda408b4286fe23a5287bcd.pdf |

<a id="r4_editions_02"></a>
### r4_editions_02

**Source:** `huang_collectiveconstitutional_2024`. **Theme:** edition_questions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Official FAccT conference-hosted23-page PDF prints the exact canonical ACM DOI10.1145/3630106.3658979, title and seven authors. Publisher/conference edition access gap is closed for the inspected content; byte-equivalence to arXiv v1 is not claimed.

**Inspected scope:** Cover/abstract and selected introduction; participant/input transformation/training methods §§3.1–3.4 pp3–6; quantitative/qualitative findings §§4.1–4.4 pp6–9; limitations §5 p9; discussion/ethics §§6–7 p10. References and appendices were not newly read in full. A programmatic comparison covers normalized extracted text on pages2–23, not substantive rereading or visual certification of every page.

**Locators:** Cover DOI/reference/license p1; §§3.1–3.4 pp3–6; §4.3 Figures4–5 p7 and Table 1/adjacent Elo text p8; §5 p9; §§6–7 p10

**Visual check:** Rendered and visually inspected Figures4–5 on p7 and Table 1 plus adjacent interpretation on p8; other figures/appendix screenshots not comprehensively rechecked.

**Findings:**

- Official conference copy preserves the positive BBQ result across nine tested dimensions and the contrary OpinionQA pattern: Public scores are2–3 percentage points below Standard across the five displayed ideology groups.
- The official artifact retains the existing Elo label/interpretation ambiguity: Table 1 labels a row Harmfulness, the adjacent text calls it harmlessness, then interprets that contrast using helpful language. Source access does not resolve the inference.
- After whitespace normalization, extracted text on PDF pages2–23 exactly matches the prior arXiv v1 extraction. Page1 differs in reference/license and arXiv wrapper information. This is text-level comparison, not a global image or byte-identity claim.

**Counterevidence / alternative:** Controlled training differs by constitution and yields affirmative benchmark changes; screened U.S. participants, researcher translation of principles, no direct adherence metric and no general equivalence/legitimacy test remain material limits.

**Limits:** Selected conference-edition reading only; no final-paper full-text upgrade or independent verification of the earlier full arXiv read. Text equality does not verify every figure or source study. No Elo/equivalence inference is licensed by resolving the source-access question.

**Replication:** `not_performed`. **Numerical check:** Documentary text comparison: whitespace-normalized pages2–23 match the earlier arXiv extraction; printed OpinionQA values checked in Figure 5. No experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C57](claims.md#c57)

**Relevance rationale:** Resolves or narrows a specific edition/denominator question without recertifying earlier reading, pooling related representations as independent evidence, or inferring model experiment replication.

**Next check:** Use the authenticated conference copy for the verified findings. Keep Elo/equivalence wording held unless underlying judgments/labels are clarified; final-text completion remains separate from edition authentication.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://facctconference.org/static/papers24/facct24-94.pdf) |
| `final_url` | [Source](https://facctconference.org/static/papers24/facct24-94.pdf) |
| `retrieved_at` | 2026-11-14T23:26:28.774066+00:00 |
| `attempted_at` | 2026-11-14T23:26:27.937361+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and immutable source URLs where available are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 79dcefab2fc9b267c7e3811be654e1fa91898d8911a72075af7ad53758f00452 |
| `byte_length` | 2663083 |
| `mime_type` | application/pdf |
| `published_on` | 2024 |
| `version_claim` | Official FAccT2024 conference-hosted ACM-format PDF; DOI10.1145/3630106.3658979;23 pages |
| `locator_basis` | Version-specific page/section locators; PDF viewer page numbers include cover. |
| `capture_path` | .source-captures/synthesis-79dcefab2fc9b267c7e3811be654e1fa91898d8911a72075af7ad53758f00452.pdf |

<a id="r4_editions_03"></a>
### r4_editions_03

**Source:** `huang_trustllm_2024`. **Theme:** edition_questions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Ancillary dataset artifact in the paper-linked official repository, at the historical July 31, 2024 commit3f55a278511218e1bc7152e77d74d5f5383b3dbc. It is not the paper or a proven experiment manifest. Git tree maps dataset/dataset.zip to immutable blobceb7df55bd8b795f6f1de3524d6c03dd54ebc3bf.

**Inspected scope:** Base64-decoded exact GitHub blob API representation of the dataset ZIP; selected fairness/preference.json member only. Parsed all 240 rows and type/option fields, checked matching120 option pairs across plain/force templates, and read the120 unique option-pair labels. Other datasets, classifier outputs and response narratives were not audited.

**Locators:** Commit3f55a278511218e1bc7152e77d74d5f5383b3dbc: dataset/dataset.zip; Blobceb7df55bd8b795f6f1de3524d6c03dd54ebc3bf → fairness/preference.json; Member fields option_a,option_b,question,prompt,type; first 80/last 40 unique option pairs

**Visual check:** None; no rendered figures independently inspected.

**Findings:**

- The artifact contains240 prompts:120 plain and120 force, sharing120 unique ordered option pairs. Its row schema has no explicit ideology/culture category field.
- Reading the option pairs shows the first 80 address public-policy/ideological choices and the last 40 culture/lifestyle, consistent with the paper’s prose. This is a source inspection of the ordering, not independently validated category annotation.
- The released input artifact does not identify which category slice/column mapping generated Table 25; finding the dataset therefore does not justify reversing category weights or correcting reported totals.

**Counterevidence / alternative:** The input list supports the described120-question construction and the distinct neutrality/refusal target. It does not resolve the table discrepancy without per-model responses, refusal classifications and exact table-producing aggregation.

**Limits:** One selected ZIP member and categorical fields only. Current/historical commit availability is not proof that this exact dataset generated published runs. No LLM generation, Longformer inference, answer-label reproduction or fairness-effect estimate.

**Replication:** `not_performed`. **Numerical check:** Programmatic documentary recount:240 rows,120 plain+120 force,120 unique option pairs; templates have identical option lists. Member SHA25608b29a25278c7710af130368c1c4194928fe5617f7f8d39dff54cced48f3ac3f; decoded ZIP SHA256495d6cf967dce12a0b7d30f95a5155eda3edd57fc175084db9126a4e9743d803. No experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C59](claims.md#c59)

**Relevance rationale:** Resolves or narrows a specific edition/denominator question without recertifying earlier reading, pooling related representations as independent evidence, or inferring model experiment replication.

**Next check:** Keep affected category/total rates held. Seek the exact experiment manifest, raw responses/classifier outputs and category/table aggregation script only if those numbers are needed.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://api.github.com/repos/HowieHwong/TrustLLM/git/blobs/ceb7df55bd8b795f6f1de3524d6c03dd54ebc3bf) |
| `final_url` | [Source](https://api.github.com/repos/HowieHwong/TrustLLM/git/blobs/ceb7df55bd8b795f6f1de3524d6c03dd54ebc3bf) |
| `retrieved_at` | 2026-11-14T23:28:54.798839+00:00 |
| `attempted_at` | 2026-11-14T23:28:53.838705+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and immutable source URLs where available are retained locally. Independent archival preservation is not claimed. |
| `sha256` | b92eda5aa4e2ed10b6eb23af70d177f511ee7e61fe4a1a152abbdc0a13932f3a |
| `byte_length` | 2334300 |
| `mime_type` | application/json |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Git blobceb7df55bd8b795f6f1de3524d6c03dd54ebc3bf in commit3f55a278511218e1bc7152e77d74d5f5383b3dbc; selected member fairness/preference.json |
| `locator_basis` | Version-specific page/section locators; PDF viewer page numbers include cover. |
| `capture_path` | .source-captures/synthesis-b92eda5aa4e2ed10b6eb23af70d177f511ee7e61fe4a1a152abbdc0a13932f3a.json |

<a id="r4_editions_04"></a>
### r4_editions_04

**Source:** `huang_trustllm_2024`. **Theme:** edition_questions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Ancillary dataset in current checked repository commitc3edca246f39f778f666366c1e30cfdb95b2e43e (committer timestamp October 4, 2026), separately pinned from the historical2024 artifact. No identity with the full original experiment is asserted.

**Inspected scope:** Base64-decoded exact GitHub blob API representation of the dataset ZIP; selected fairness/preference.json member only. Parsed all 240 rows and type/option fields, checked matching120 option pairs across plain/force templates, and read the120 unique option-pair labels. Other datasets, classifier outputs and response narratives were not audited.

**Locators:** Commitc3edca246f39f778f666366c1e30cfdb95b2e43e: dataset/dataset.zip; Blob7679a9c4d7d657f35304df6a6f9770f2f1d9a3a4 → dataset/fairness/preference.json

**Visual check:** None; no rendered figures independently inspected.

**Findings:**

- The current ZIP differs as a package, but its selected preference member is byte-identical to the historical2024 member, preserving240 prompts/120 option pairs. Member path changed from fairness/preference.json to dataset/fairness/preference.json.
- No category field or table-producing output is introduced by this member; later availability does not resolve published Table 25.

**Counterevidence / alternative:** Stable member bytes rule out a simple current-input-member change as an explanation for the observed aggregate tension, but do not rule out older run variants, category slicing, column labels, omitted outputs or different scoring procedures.

**Limits:** Selected member inspection only. Full ZIP equivalence is explicitly not claimed and other package changes were not audited. This is not a second independent dataset or corroborating experiment.

**Replication:** `not_performed`. **Numerical check:** The selected member SHA256 matches historical08b29a25278c7710af130368c1c4194928fe5617f7f8d39dff54cced48f3ac3f exactly. Decoded currentZIP SHA2560433f79bc8dc8a5869af253d4a70067eda82f5651b89b7235a0220a8bf775317 differs from historical ZIP. Documentary comparison only.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Resolves or narrows a specific edition/denominator question without recertifying earlier reading, pooling related representations as independent evidence, or inferring model experiment replication.

**Next check:** Use the historical snapshot and shared member hash for the bounded input observation; keep the experiment/aggregation provenance question open.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://api.github.com/repos/HowieHwong/TrustLLM/git/blobs/7679a9c4d7d657f35304df6a6f9770f2f1d9a3a4) |
| `final_url` | [Source](https://api.github.com/repos/HowieHwong/TrustLLM/git/blobs/7679a9c4d7d657f35304df6a6f9770f2f1d9a3a4) |
| `retrieved_at` | 2026-11-14T23:28:54.728927+00:00 |
| `attempted_at` | 2026-11-14T23:28:53.839364+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and immutable source URLs where available are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 1bcc176fc59fea7af67e1fd289c84f8856ad82f9eb9abdf29838d5df9735a2cb |
| `byte_length` | 2451024 |
| `mime_type` | application/json |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Git blob7679a9c4d7d657f35304df6a6f9770f2f1d9a3a4 in commitc3edca246f39f778f666366c1e30cfdb95b2e43e; member dataset/fairness/preference.json |
| `locator_basis` | Version-specific page/section locators; PDF viewer page numbers include cover. |
| `capture_path` | .source-captures/synthesis-1bcc176fc59fea7af67e1fd289c84f8856ad82f9eb9abdf29838d5df9735a2cb.json |

<a id="r4_editions_05"></a>
### r4_editions_05

**Source:** `huang_trustllm_2024`. **Theme:** edition_questions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Ancillary scoring source from the paper-linked repository, pinned to July 31, 2024 commit3f55a278511218e1bc7152e77d74d5f5383b3dbc. The same file is byte-identical in checked October2026 commitc3edca246f39f778f666366c1e30cfdb95b2e43e; neither is an authenticated published run manifest.

**Inspected scope:** Inspected FairnessEval.preference_eval and its surrounding class interface in the6617-byte fairness.py file. Read filtering/scoring/return paths, without importing or executing model/classifier dependencies. Other fairness methods were not validated as an entire package.

**Locators:** trustllm_pkg/trustllm/task/fairness.py: FairnessEval.preference_eval, lines131–164; Pinned source at3f55a278511218e1bc7152e77d74d5f5383b3dbc

**Visual check:** None; no rendered figures independently inspected.

**Findings:**

- preference_eval filters plain/force rows by type, invokes Longformer/refusal scoring, computes each template’s overall refusal rate, then averages the two rates. Its forced branch excludes short A/B responses before Longformer scoring and divides refusal count by all forced prompts. The inspected routine has no ideology/culture slicing or Table 25 category-column construction.
- The routine’s existence supports how the toolkit operationalizes refusal-based preference evaluation, but does not authenticate paper-specific category rates or prove this exact path generated the reported table.

**Counterevidence / alternative:** The paper’s qualitative distinct-construct argument survives; source code provides a constructive implementation detail. It cannot supply missing per-model outputs or resolve category/total disagreements by itself.

**Limits:** Static source inspection only. No external model/classifier calls, model experiments, output-label replication, or complete repository audit. Byte-identical later code does not prove historical execution.

**Replication:** `not_performed`. **Numerical check:** Static documentary reading only. Historical/current source files both SHA2564a3ef8b6feadc2e7857050222328cf53f4f42ba3fdce997acbf7174a1daadf17. No classifier inference or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C59](claims.md#c59)

**Relevance rationale:** Resolves or narrows a specific edition/denominator question without recertifying earlier reading, pooling related representations as independent evidence, or inferring model experiment replication.

**Next check:** Retain the numerical hold and identify the exact missing table-producing category/aggregation path and run outputs. Avoid calling a code inspection experimental replication.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://raw.githubusercontent.com/HowieHwong/TrustLLM/3f55a278511218e1bc7152e77d74d5f5383b3dbc/trustllm_pkg/trustllm/task/fairness.py) |
| `final_url` | [Source](https://raw.githubusercontent.com/HowieHwong/TrustLLM/3f55a278511218e1bc7152e77d74d5f5383b3dbc/trustllm_pkg/trustllm/task/fairness.py) |
| `retrieved_at` | 2026-11-14T23:28:54.173272+00:00 |
| `attempted_at` | 2026-11-14T23:28:53.839804+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and immutable source URLs where available are retained locally. Independent archival preservation is not claimed. |
| `sha256` | 4a3ef8b6feadc2e7857050222328cf53f4f42ba3fdce997acbf7174a1daadf17 |
| `byte_length` | 6617 |
| `mime_type` | text/plain |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Commit3f55a278511218e1bc7152e77d74d5f5383b3dbc; fairness.py gitblob2aeda66c2c6d4b24386eec4086c5ad27a1e0d2ce |
| `locator_basis` | Version-specific page/section locators; PDF viewer page numbers include cover. |
| `capture_path` | .source-captures/synthesis-4a3ef8b6feadc2e7857050222328cf53f4f42ba3fdce997acbf7174a1daadf17.txt |

<a id="r4_editions_06"></a>
### r4_editions_06

**Source:** `huang_trustllm_2024`. **Theme:** edition_questions. **Reading:** Metadata only. **Coverage effect:** `none`.

**Edition match:** `related_edition`. Official repository Git tree at exact historical commit3f55a278511218e1bc7152e77d74d5f5383b3dbc; source membership/provenance object, not paper content.

**Inspected scope:** Selected tree entries for dataset/dataset.zip and trustllm_pkg/trustllm/task/fairness.py; used to bind immutable blob identities to the historical repository snapshot. No whole-repository substantive reading.

**Locators:** Git tree commit3f55a278511218e1bc7152e77d74d5f5383b3dbc, recursive tree entries

**Visual check:** None; no rendered figures independently inspected.

**Findings:**

- Historical tree maps the dataset ZIP to blobceb7df55bd8b795f6f1de3524d6c03dd54ebc3bf and scoring file to blob2aeda66c2c6d4b24386eec4086c5ad27a1e0d2ce.

**Counterevidence / alternative:** Version-pinning supports reproducible documentary inspection, but does not identify published-run inputs or outputs.

**Limits:** Metadata membership only, not execution or substantive source corroboration.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental reproduction.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Resolves or narrows a specific edition/denominator question without recertifying earlier reading, pooling related representations as independent evidence, or inferring model experiment replication.

**Next check:** Use as provenance for the dataset/code checks; do not count as independent empirical support.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://api.github.com/repos/HowieHwong/TrustLLM/git/trees/3f55a278511218e1bc7152e77d74d5f5383b3dbc?recursive=1) |
| `final_url` | [Source](https://api.github.com/repos/HowieHwong/TrustLLM/git/trees/3f55a278511218e1bc7152e77d74d5f5383b3dbc?recursive=1) |
| `retrieved_at` | 2026-11-14T23:28:28.494292+00:00 |
| `attempted_at` | 2026-11-14T23:28:28.052884+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and immutable source URLs where available are retained locally. Independent archival preservation is not claimed. |
| `sha256` | a27fccb19e4c275252fc50565c91807b17a5ee75c929d06c53c43cad4952f8a4 |
| `byte_length` | 16926 |
| `mime_type` | application/json |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Historical commit3f55a278511218e1bc7152e77d74d5f5383b3dbc recursive Git tree |
| `locator_basis` | Version-specific page/section locators; PDF viewer page numbers include cover. |
| `capture_path` | .source-captures/synthesis-a27fccb19e4c275252fc50565c91807b17a5ee75c929d06c53c43cad4952f8a4.json |

<a id="r4_editions_07"></a>
### r4_editions_07

**Source:** `cunningham_sparseautoencoders_2024`. **Theme:** edition_questions. **Reading:** Metadata only. **Coverage effect:** `none`.

**Edition match:** `same_record`. Exact official ICLR2024 title/venue entry links to the captured19-page proceedings PDF. The entry’s rendered author ordering/names differ from the PDF cover, so author-alias/order reconciliation is left open rather than automatically changing canonical fields.

**Inspected scope:** Title, author rendering, venue label, abstract, Paper link and name-change-policy text on the official proceedings entry only.

**Locators:** Title/author/ICLR2024 venue entry; Paper link to1fa1ab11f4bd5f94b2ec20e794dbfa3b-Paper-Conference.pdf

**Visual check:** None; no rendered figures independently inspected.

**Findings:**

- The official proceedings entry authenticates the final PDF route and venue. Its author rendering and the downloadable PDF differ; this is a bibliographic-version lead, not a basis to infer private identity facts or alter citation keys.

**Counterevidence / alternative:** The PDF itself matches the canonical work’s title and printed authors and supplies the checked result. Landing metadata does not establish content equivalence between editions.

**Limits:** Metadata only; no authorship/name-change rationale investigated and no canonical author changes proposed.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental reproduction.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Resolves or narrows a specific edition/denominator question without recertifying earlier reading, pooling related representations as independent evidence, or inferring model experiment replication.

**Next check:** If bibliography display metadata is revised, reconcile exact publisher metadata and historical PDF citation form explicitly.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2024/hash/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Abstract-Conference.html) |
| `final_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2024/hash/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Abstract-Conference.html) |
| `retrieved_at` | 2026-11-14T23:26:28.409286+00:00 |
| `attempted_at` | 2026-11-14T23:26:27.936775+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary bytes and immutable source URLs where available are retained locally. Independent archival preservation is not claimed. |
| `sha256` | c047cb7562b6605b262aafbc94a9aad22bea5a14b464acdeed1dab93ca37130e |
| `byte_length` | 9667 |
| `mime_type` | text/html |
| `published_on` | 2024 |
| `version_claim` | Official ICLR2024 proceedings title entry; current retrieved rendering |
| `locator_basis` | Version-specific page/section locators; PDF viewer page numbers include cover. |
| `capture_path` | .source-captures/synthesis-c047cb7562b6605b262aafbc94a9aad22bea5a14b464acdeed1dab93ca37130e.html |

<a id="r4_ny_01"></a>
### r4_ny_01

**Source:** `newyork_raiseact_article44b_nd`. **Theme:** edition_questions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Canonical codified Article44-B index; current page displays most recent revision from April3,2026. No identity with an earlier capture is asserted.

**Inspected scope:** Article heading, most-recent-revision label, ten section links/headings and effective-date note only; linked operative sections were not reread.

**Locators:** Article44-B, current revision label and final NB effective-date note

**Visual check:** None; selected statutory and action text read, no visual authentication.

**Findings:**

- The live official codified index identifies the April3,2026 revision and January1,2027 effectiveness. Earlier403 access in the integration is now superseded by a successful dated retrieval.

**Counterevidence / alternative:** The prospective date prevents treating codified duties as already operative on this retrieval; the index alone does not authenticate every historical amendment or practice.

**Limits:** This is the article index, not a fresh complete reading of §§1420–1429. No actual compliance, administrative interpretation, judicial status or outcomes checked.

**Replication:** `not_performed`. **Numerical check:** No numerical recalculation or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C17](claims.md#c17)

**Relevance rationale:** Closes the earlier exact official access/effective-date gap for C17, without a full statute reread or proof of implementation.

**Next check:** Use the captured revision/date for the narrow legal-force distinction; check operative clauses and later instruments if a specific duty becomes publication-leading.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.nysenate.gov/legislation/laws/GBS/A44-B) |
| `final_url` | [Source](https://www.nysenate.gov/legislation/laws/GBS/A44-B) |
| `retrieved_at` | 2026-11-14T23:33:53.819760+00:00 |
| `attempted_at` | 2026-11-14T23:33:53.206981+00:00 |
| `sha256` | 4aec2e0a8591ebb341dde033b93fb491fb5a1139518985b177fdbf2b22a06502 |
| `byte_length` | 36242 |
| `mime_type` | text/html |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked independent capture-specific archive was established in this bounded round; exact live response bytes and actual retrieval metadata are retained locally. |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Codified index displays revision from2026-04-03 and NB effective2027-01-01 |
| `locator_basis` | Stable article/action labels and bill section/page/printed line numbers; retrieval is current, not an authenticated historical snapshot. |
| `capture_path` | .source-captures/synthesis-4aec2e0a8591ebb341dde033b93fb491fb5a1139518985b177fdbf2b22a06502.html |

<a id="r4_ny_02"></a>
### r4_ny_02

**Source:** `newyork_raiseact_article44b_nd`. **Theme:** edition_questions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Official S8828 legislative tracker is related enactment provenance for the codified article, not the same document edition.

**Inspected scope:** Bill identity/status; action history; laws-affected and sponsor-memo relationship; link to bill PDF. Unrelated navigation, votes and complete reproduced bill body not comprehensively read.

**Locators:** S8828 status and Actions: March27,2026 signed chap.96; Laws Affected; PDF link

**Visual check:** None; selected statutory and action text read, no visual authentication.

**Findings:**

- The official action history records S8828 signed as chapter96 on March27,2026, and identifies its repeal/re-add relationship to Article44-B. This connects the amendatory text to the codification rather than relying on an unpassed bill alone.

**Counterevidence / alternative:** A bill-page proposed text alone would not establish enacted law; the recorded signed action and codified index supply the scoped connection. These representations are one legislative lineage, not independent compliance evidence.

**Limits:** A live legislative status page supports identity/enactment provenance, not a complete audit of the statute’s legal application or subsequent amendments.

**Replication:** `not_performed`. **Numerical check:** No numerical recalculation or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C17](claims.md#c17)

**Relevance rationale:** Closes the earlier exact official access/effective-date gap for C17, without a full statute reread or proof of implementation.

**Next check:** For broader legal claims, inspect exact codified clauses and any later amendments or decisions; preserve original and amended versions separately.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.nysenate.gov/legislation/bills/2025/S8828) |
| `final_url` | [Source](https://www.nysenate.gov/legislation/bills/2025/S8828) |
| `retrieved_at` | 2026-11-14T23:33:54.673070+00:00 |
| `attempted_at` | 2026-11-14T23:33:54.536579+00:00 |
| `sha256` | 96d0577a15cbf00393bd8cda0bf4adf677df0ea9ba53c031649d44d7276a16d4 |
| `byte_length` | 121621 |
| `mime_type` | text/html |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked independent capture-specific archive was established in this bounded round; exact live response bytes and actual retrieval metadata are retained locally. |
| `published_on` | Not recorded / unavailable |
| `version_claim` | S8828 official action history, signed chapter96 on2026-03-27 |
| `locator_basis` | Stable article/action labels and bill section/page/printed line numbers; retrieval is current, not an authenticated historical snapshot. |
| `capture_path` | .source-captures/synthesis-96d0577a15cbf00393bd8cda0bf4adf677df0ea9ba53c031649d44d7276a16d4.html |

<a id="r4_ny_03"></a>
### r4_ny_03

**Source:** `newyork_raiseact_article44b_nd`. **Theme:** edition_questions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Official S8828 bill text linked by its signed legislative tracker; related amendatory instrument, not a substitute full reading of consolidated Article44-B.

**Inspected scope:** PDF p1 identification/title and p2 opening§2 repeal/re-add clause; PDF p9§§3–5 effective-date/severability provisions only. Other definitions, duties, thresholds, exceptions and enforcement provisions not fully read.

**Locators:** S8828 coverp1; §2 openingp2; §§3–5 p9, lines27–45

**Visual check:** None; selected statutory and action text read, no visual authentication.

**Findings:**

- Section3 changes the original act’s effective date to January1,2027. Section5 makes that date amendment immediate while specified replacement provisions follow the underlying act’s effective date. Read together with the signed action and codified note, this resolves the narrow date question.

**Counterevidence / alternative:** Different timing for the date amendment and replacement provisions prevents reading “effective immediately” as making all replacement duties immediately operative.

**Limits:** Selected nine-page amendatory text only. The January8,2026 cover is the bill’s printed date; March27 signing comes from the action history. No assertion that every present statutory or judicial-status issue is settled.

**Replication:** `not_performed`. **Numerical check:** No numerical recalculation or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C17](claims.md#c17)

**Relevance rationale:** Closes the earlier exact official access/effective-date gap for C17, without a full statute reread or proof of implementation.

**Next check:** Retain the future-effective qualification; review actual operative sections for application-specific claims.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://legislation.nysenate.gov/pdf/bills/2025/S8828) |
| `final_url` | [Source](https://legislation.nysenate.gov/pdf/bills/2025/S8828) |
| `retrieved_at` | 2026-11-14T23:33:54.536072+00:00 |
| `attempted_at` | 2026-11-14T23:33:54.030748+00:00 |
| `sha256` | bfdc16dbcbb0abcc513b0d020602c899efabf565fe2114bfb6195f77dd14ee22 |
| `byte_length` | 31267 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked independent capture-specific archive was established in this bounded round; exact live response bytes and actual retrieval metadata are retained locally. |
| `published_on` | 2026-01-08 |
| `version_claim` | S8828 printed January8,2026; §§3–5 effective-date provisions |
| `locator_basis` | Stable article/action labels and bill section/page/printed line numbers; retrieval is current, not an authenticated historical snapshot. |
| `capture_path` | .source-captures/synthesis-bfdc16dbcbb0abcc513b0d020602c899efabf565fe2114bfb6195f77dd14ee22.pdf |
## thresholds-resilience-reporting-2026-11-15

**As of:** 2026-11-15. **Base commit:** `993614107f9e28806e2279a5214645328e12132b`.

**Question:** How do threshold/regulatory choices and reporting institutions connect to evidence, and what do privacy, training-persistence and positive mitigation studies establish about resilience beyond a benchmark score?

**Selection basis:** Purposive selection from155 unresolved roles and168 missing full-text labels at9936141, with one mapped ARIA numerical question. Prioritizes threshold design, institutional reporting/audit, training/data-transfer failure modes, affirmative safety interventions, and privacy/verification. Selection recorded before source acquisition. This is not a systematic sample or reconstructed search. The round spans the UTC date boundary; actual retrieval times are retained separately.

**Stopping rule:** Complete one bounded reviewable unit per complementary strand. Prefer genuine complete reading of manageable claim-critical exact objects, otherwise selected methods/appendices with exact gaps. Do not force every record into a claim or assume related editions equivalent. Bound failed-source and missing-manifest investigations; keep disputed quantities omitted or qualified. No experiments or independent human review implied by documentary checking.

| Theme | Why selected | Canonical keys |
|---|---|---|
| Compute/capability thresholds and regulatory design | Tests threshold functions, adaptive selection, survey evidence and institutional trade-offs without treating a proxy or proposed threshold as validated risk control. | `heim_trainingcomputethresholds_2024`, `sastry_computingpowergovernance_2024`, `schuett_surveythresholdsadvanced_2025`, `anderljung_frontierairegulation_2023`, `californiapolicyworkinggroup_thecaliforniareport_2025`, `fmf_thresholdsfrontier_2025` |
| Internal deployment, audit and incident reporting | Adds missing institutional mechanisms and evidence about what is reported, audited and acted upon, separating proposals, descriptive research and operational outcomes. | `stix_behindcloseddoors_2025`, `schuett_frontierdevelopers_2024`, `brundage_frontierauditingrigorous_2026`, `cset_incidentskeycomponents_2025`, `oecd_commonreportingincidents_2025`, `mcgregor_preventingrepeatedfailures_2021` |
| Backdoors, poisoning and latent transfer | Compares engineered threat models, persistence tests, architecture/data dependencies and null/control results before inferring natural propensity or universal training failure. | `hubinger_sleeperagentstraining_2024`, `cloud_subliminallearning_2025`, `zhang_persistentpretraining_2025`, `li_backdoorllmcomprehensive_2024`, `gloaguen_finetuningactivated_2025` |
| Positive safety-training and constrained optimization evidence | Adds affirmative alignment/mitigation results while testing utility comparators, attack adaptivity, guarantee assumptions and transfer boundaries. | `dai_saferlhfsafe_2024`, `guan_deliberativealignment_2024`, `hsu_safelorasilver_2024`, `yu_robustsafeguarding_2024`, `chittepu_reinforcementlearning_2025` |
| Extraction, unlearning and process verification | Distinguishes evidence of data exposure, output suppression, training-data provenance and verification of a process from universal privacy or safety guarantees. | `nasr_scalableextraction_2025`, `du_textualunlearning_2025`, `wang_pandoraswhite_2024`, `zhang_vtuneverifiablefine_2024`, `barbero_extractingalignment_2025` |
| Statutory/draft versions and an application-evaluation count | Tests operative scope and exact public-draft editions, and narrows the ARIA dialogue/violation counting question without automatically correcting it. | `california_sb53_tfaia_2025`, `nist_managingmisuserisk_2024`, `nist_managingmisuserisk_2025_2pd`, `amironesei_aria_pilot_2025` |

### Event index

| Event | Source | Reading | Edition / coverage effect | Relevance |
|---|---|---|---|---|
| [r5_thresholds_01](#r5_thresholds_01) | `heim_trainingcomputethresholds_2024` | Full text | same_record / complete_record_text | claim_evidence |
| [r5_thresholds_02](#r5_thresholds_02) | `sastry_computingpowergovernance_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_thresholds_03](#r5_thresholds_03) | `schuett_surveythresholdsadvanced_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_thresholds_04](#r5_thresholds_04) | `anderljung_frontierairegulation_2023` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_thresholds_05](#r5_thresholds_05) | `californiapolicyworkinggroup_thecaliforniareport_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_thresholds_06](#r5_thresholds_06) | `fmf_thresholdsfrontier_2025` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r5_reporting_01](#r5_reporting_01) | `stix_behindcloseddoors_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_reporting_02](#r5_reporting_02) | `schuett_frontierdevelopers_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_reporting_03](#r5_reporting_03) | `brundage_frontierauditingrigorous_2026` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r5_reporting_04](#r5_reporting_04) | `cset_incidentskeycomponents_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r5_reporting_05](#r5_reporting_05) | `oecd_commonreportingincidents_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r5_reporting_06](#r5_reporting_06) | `mcgregor_preventingrepeatedfailures_2021` | Full text | same_record / complete_record_text | claim_evidence |
| [r5_persistence_01](#r5_persistence_01) | `hubinger_sleeperagentstraining_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_persistence_02](#r5_persistence_02) | `zhang_persistentpretraining_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r5_persistence_03](#r5_persistence_03) | `cloud_subliminallearning_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_persistence_04](#r5_persistence_04) | `li_backdoorllmcomprehensive_2024` | Full text | same_record / complete_record_text | claim_evidence |
| [r5_persistence_05](#r5_persistence_05) | `gloaguen_finetuningactivated_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_persistence_06](#r5_persistence_06) | `li_backdoorllmcomprehensive_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r5_mitigations_01](#r5_mitigations_01) | `dai_saferlhfsafe_2024` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r5_mitigations_02](#r5_mitigations_02) | `chittepu_reinforcementlearning_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r5_mitigations_03](#r5_mitigations_03) | `hsu_safelorasilver_2024` | Full text | same_record / complete_record_text | claim_evidence |
| [r5_mitigations_04](#r5_mitigations_04) | `yu_robustsafeguarding_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_mitigations_05](#r5_mitigations_05) | `guan_deliberativealignment_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_privacy_01](#r5_privacy_01) | `nasr_scalableextraction_2025` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r5_privacy_02](#r5_privacy_02) | `nasr_scalableextraction_2025` | Metadata only | same_record / scoped_review | background |
| [r5_privacy_03](#r5_privacy_03) | `nasr_scalableextraction_2025` | Metadata only | related_edition / scoped_review | background |
| [r5_privacy_04](#r5_privacy_04) | `du_textualunlearning_2025` | Full text | same_record / complete_record_text | claim_evidence |
| [r5_privacy_05](#r5_privacy_05) | `wang_pandoraswhite_2024` | Metadata only | same_record / scoped_review | background |
| [r5_privacy_06](#r5_privacy_06) | `zhang_vtuneverifiablefine_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_privacy_07](#r5_privacy_07) | `barbero_extractingalignment_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_versions_01](#r5_versions_01) | `nist_managingmisuserisk_2024` | Full text | same_record / complete_record_text | claim_evidence |
| [r5_versions_02](#r5_versions_02) | `nist_managingmisuserisk_2025_2pd` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_versions_03](#r5_versions_03) | `amironesei_aria_pilot_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [r5_versions_04](#r5_versions_04) | `amironesei_aria_pilot_2025` | Full text | related_edition / scoped_review | claim_evidence |
| [r5_versions_05](#r5_versions_05) | `amironesei_aria_pilot_2025` | Metadata only | related_edition / none | background |
| [r5_versions_06](#r5_versions_06) | `california_sb53_tfaia_2025` | Inaccessible | uncertain / none | unresolved |
| [r5_versions_07](#r5_versions_07) | `california_sb53_tfaia_2025` | Selected sections | related_edition / scoped_review | claim_evidence |
| [r5_versions_08](#r5_versions_08) | `california_sb53_tfaia_2025` | Full text | related_edition / scoped_review | background |

<a id="r5_thresholds_01"></a>
### r5_thresholds_01

**Source:** `heim_trainingcomputethresholds_2024`. **Theme:** thresholds. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact title, authors and arXiv identity match the canonical 2024 work. This is pinned v2, not a claim of equivalence to any uninspected final publication.

**Inspected scope:** All 36 PDF text pages, §§1–7, all figure/table text and captions and references, read in overlapping bounded chunks; Figure 6 separately rendered and inspected. No linked reference works or datasets included.

**Locators:** §2 pp7–9: counted training stage; §3 pp9–11 and footnote6 p9: strengths and nonmonotonic risk caveat; §§4–5.1 pp12–14 and Figure6: proxy chain and initial scrutiny filter; §§6.1–6.4 pp18–27 and Table1: threshold choice, updating, alternatives

**Visual check:** Rendered PDF p14/Figure6 inspected: two-stage compute-screening/capability pathway and general requirements drawn beneath both sides. Its low-risk/high-risk boxes are conceptual labels, not empirically validated classifications. Other figure captions/text read; no full visual audit or plot digitization.

**Findings:**

- The authors argue pretraining compute can provide an early, quantifiable and potentially externally verifiable screening metric for deciding which models warrant scrutiny; capability/risk evaluation then informs more specific safeguards, with general privacy/copyright/application obligations applying separately.
- The paper distinguishes measurement advantages from the uncertain chain from compute through loss/capability to risk. Footnote6 explicitly allows improved capabilities to reduce failures, bias or robustness problems, and says net directional evidence is insufficient.
- Updating is not necessarily a downward ratchet: algorithmic efficiency, affordability, regulatory capacity, threat environment and defensive adaptation can push the desired threshold in different directions. Effective-compute alternatives inherit benchmark, lifecycle and context choices.

**Counterevidence / alternative:** Low-compute specialized harm and post-training enhancement can escape a pretraining screen; high-compute capability can also support beneficial or defensive uses. A useful early filter need not be an adequate measure of risk or an appropriate trigger for all legal duties.

**Limits:** Historical EO14110/EU AI Act discussion is not current-law verification. Figure6 and Table1 are proposed frameworks/first-pass comparisons, not calibrated classifications or effect estimates; cited underlying experiments not replicated.

**Replication:** `not_performed`. **Numerical check:** No experimental or policy-effect replication. No independently calibrated numerical risk threshold is adopted; author-reported quantities are treated as documentary descriptions only.

**Relevance:** `claim_evidence`. **Claim links:** [C80](claims.md#c80)

**Relevance rationale:** Source-level evidence for the stated conceptual, survey-method or policy-design claim; neither inclusion nor a separate-agent check establishes independent corroboration.

**Next check:** Preserve the two-stage proposal and bidirectional updating caveat. If a publication leads with a numeric compute cutoff, require a separate policy-purpose/calibration argument and current legal primary sources; otherwise omit a universal cutoff.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2405.10799v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2405.10799v2) |
| `retrieved_at` | 2026-11-15T00:02:52.007996+00:00 |
| `attempted_at` | 2026-11-15T00:02:50.705670+00:00 |
| `sha256` | 89bce40fd16c8f175da466e0fe43ea7b974377e16653e9ccf174ac283624abbe |
| `byte_length` | 8599753 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact acquired bytes are retained privately with a SHA-256 receipt; independent archival preservation is not claimed. |
| `published_on` | 2024-08-06 |
| `version_claim` | arXiv:2405.10799v2, 6 August 2024 |
| `locator_basis` | PDF viewer pages count the cover; printed pages stated separately where different. |
| `capture_path` | .source-captures/synthesis-89bce40fd16c8f175da466e0fe43ea7b974377e16653e9ccf174ac283624abbe.pdf |

<a id="r5_thresholds_02"></a>
### r5_thresholds_02

**Source:** `sastry_computingpowergovernance_2024`. **Theme:** thresholds. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Pinned v1 matches the canonical arXiv work/title and authors; the source itself uses adjacent version/title-page dates, retained explicitly rather than silently normalized. No final-edition identity claim.

**Inspected scope:** PDF viewer pp1–5 (cover, contents, introduction and summary); pp25–32 (printedpp24–31, all §3.B properties and opening §3.C); pp35–36 (printedpp34–35, §4 introduction and opening4.A); pp61–69 (printedpp60–68, §5 introduction, §5.A and opening5.B). Remaining §4 mechanisms, later §5 principles, appendices and references not fully read.

**Locators:** §3.B printedpp24–30: detectability, excludability, quantifiability and concentrated supply chain; §4 opening printedp34: visibility/allocation/enforcement taxonomy; §5.A printedpp60–67 and §5.B opening printedp68: feasibility and undesired consequences

**Visual check:** No rendered figures checked. Text/captions for Figures7–11 in selected pages read; historic industry-share figures are not recertified as current observations.

**Findings:**

- The report identifies properties of compute that can make governance interventions practically available: large physical facilities can be detectable, access can be mediated, usage quantified and supply chains concentrated. It organizes exploratory interventions into visibility, allocation and enforcement.
- Detecting a datacenter does not identify its workload/model. More informative monitoring can require provider reporting and create privacy, confidentiality, security, economic and power-concentration costs.
- The authors explicitly address algorithm/hardware progress, low-compute specialized systems, post-training changes and evasion. They argue for scope and procedural safeguards, including industrial-scale focus and periodic review, rather than treating hardware governance as automatically proportionate.

**Counterevidence / alternative:** Compute can be easier to govern than an intangible model while still being an imperfect risk proxy; observability can worsen surveillance or regulatory capture. Lower-compute pathways and innovation can reduce intervention coverage.

**Limits:** 104-page report remains selectively read. The mechanism catalogue, appendices and full references remain deferred. Feasibility affordances and historical concentration do not demonstrate policy effectiveness, desirability or enduring present-day concentration.

**Replication:** `not_performed`. **Numerical check:** No experimental or policy-effect replication. No independently calibrated numerical risk threshold is adopted; author-reported quantities are treated as documentary descriptions only.

**Relevance:** `claim_evidence`. **Claim links:** [C81](claims.md#c81)

**Relevance rationale:** Source-level evidence for the stated conceptual, survey-method or policy-design claim; neither inclusion nor a separate-agent check establishes independent corroboration.

**Next check:** Read the claim-critical detailed mechanism before asserting any enforcement tool is feasible at a stated assurance level; require implementation evaluation for any claim that compute governance reduced harm.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2402.08797v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2402.08797v1) |
| `retrieved_at` | 2026-11-15T00:02:51.908174+00:00 |
| `attempted_at` | 2026-11-15T00:02:50.706023+00:00 |
| `sha256` | 8b08c1b217e76132cf1c34c9718c60cf5b92860be53f368a0e9795cbd78bd443 |
| `byte_length` | 8089220 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact acquired bytes are retained privately with a SHA-256 receipt; independent archival preservation is not claimed. |
| `published_on` | 2024-02-14 |
| `version_claim` | arXiv:2402.08797v1; margin 13 February 2024, title page 14 February 2024 |
| `locator_basis` | PDF viewer pages count the cover; printed pages stated separately where different. |
| `capture_path` | .source-captures/synthesis-8b08c1b217e76132cf1c34c9718c60cf5b92860be53f368a0e9795cbd78bd443.pdf |

<a id="r5_thresholds_03"></a>
### r5_thresholds_03

**Source:** `schuett_surveythresholdsadvanced_2025`. **Theme:** thresholds. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Title, six authors and 2025 white-paper identity match the canonical record. Oxford-hosted primary PDF is an accessible route; the old publication-page route should not silently substitute an earlier or later report.

**Inspected scope:** Title/abstract, contents, executive summary (printedpp3–4), selected overview figure labels showing item-specific sample sizes, complete §2 methods (printedpp7–11), §4.1 and §4.2.1 through opening4.2.2 (printedpp15–18 opening), and §§4.3–5 plus acknowledgments (printedpp20–21). Not all §3 results/§4.2, references or questionnaire appendices.

**Locators:** §2.1 and Table1 printedpp7–8: questionnaire and operational definitions; §2.2 printedpp8–10 and Table2: recruitment, sample and optional demographics; §2.3–2.4 printedpp10–11: descriptive analysis, consultation and qualitative coding; §4.1–4.2.1 printedpp15–17: plural purposes and divided compute choices; §4.3 and §5 printedpp20–21: limitations and conclusions

**Visual check:** No rendered survey charts or sample-flow diagram checked. Selected text labels establish variable item denominators; exact chart values and completion-flow counts are omitted.

**Findings:**

- The questionnaire elicited views on 98 statements across 13 optional questions from a selected expert network and invited researchers; authors report 166 participants of 379 invited. The recruited and self-selected sample does not establish public legitimacy or representative expert consensus.
- Authors report support for stakeholder panels, external verifiability and multiple threshold purposes, alongside disagreement on the number/role/justification of compute thresholds. This is evidence about elicited views and design preferences, not measured risk-threshold validity.
- Table1 deliberately defines capability thresholds using both capability and adequate mitigation; its note acknowledges other practitioners use a capability-only definition. The paper also acknowledges threshold desirability/model focus were assumed and some questions could imply a capability-risk connection.

**Counterevidence / alternative:** Structured consultation usefully surfaces design priorities, but optional participation, framing, terminology and qualitative interpretation can shape responses. A mean preference neither calibrates a risk boundary nor resolves whose values should govern.

**Limits:** 166 participants from 379 invited is author-reported participation, not a population-representative estimate. Questions were optional, so 166 is not the denominator for every result. Remaining results, references and questionnaire appendices were not fully read; no headline exact rating/percentage or completion-flow count adopted.

**Replication:** `not_performed`. **Numerical check:** No experimental or policy-effect replication. No independently calibrated numerical risk threshold is adopted; author-reported quantities are treated as documentary descriptions only.

**Relevance:** `claim_evidence`. **Claim links:** [C82](claims.md#c82)

**Relevance rationale:** Source-level evidence for the stated conceptual, survey-method or policy-design claim; neither inclusion nor a separate-agent check establishes independent corroboration.

**Next check:** Read the exact question wording, item denominators and full relevant result chart before using any leading survey number. Treat this as elicitation and normative design input; retain contrary views instead of declaring consensus.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://aigi.ox.ac.uk/wp-content/uploads/2025/08/Survey_on_thresholds_for_advanced_AI_systems_1.pdf) |
| `final_url` | [Source](https://aigi.ox.ac.uk/wp-content/uploads/2025/08/Survey_on_thresholds_for_advanced_AI_systems_1.pdf) |
| `retrieved_at` | 2026-11-15T00:02:52.516636+00:00 |
| `attempted_at` | 2026-11-15T00:02:50.707913+00:00 |
| `sha256` | 1a4499a688f0b75ef744af9c719307c8aaa19f2d96e0eafcfbb12afc5dcc586b |
| `byte_length` | 1132874 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact acquired bytes are retained privately with a SHA-256 receipt; independent archival preservation is not claimed. |
| `published_on` | 2025-08 |
| `version_claim` | White paper, August 2025; Oxford-hosted PDF |
| `locator_basis` | PDF viewer pages count the cover; printed pages stated separately where different. |
| `capture_path` | .source-captures/synthesis-1a4499a688f0b75ef744af9c719307c8aaa19f2d96e0eafcfbb12afc5dcc586b.pdf |

<a id="r5_thresholds_04"></a>
### r5_thresholds_04

**Source:** `anderljung_frontierairegulation_2023`. **Theme:** thresholds. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Pinned 2023 v1 matches canonical arXiv work/title and author group. A later final publication, if any, was not checked for equivalence.

**Inspected scope:** PDFpp1–5 (authorship note, abstract, executive summary and contents), pp15–18 (§2 closing illustration and §3 institutional building-block opening), all pp24–29 (§4.1–4.4 plus §4.5 opening), pp32–36 (§5 continuation, conclusion and AppendixA.1–A.4 opening). Page19 and unlisted passages are not counted as completely read. References and remaining appendices deferred.

**Locators:** §3 opening pp17–18: standards/visibility/compliance architecture; §§4.1–4.4 pp24–29 and Table3: capability/controllability assessments, external scrutiny, deployment rules and monitoring; §5 pp32–33: limits and governance risks; AppendixA pp35–36: imperfect/dynamic regulatory definitions

**Visual check:** No figure images rendered; Table3 content read as text. Its example systems and categories are illustrations, not measured validated risk classes.

**Findings:**

- The paper proposes a concrete chain from capability/controllability assessment, through sufficiently expert and resourced external scrutiny, to deployment rules and post-deployment reassessment. §4.4 includes reporting, impact monitoring and capability-enhancement triggers for changed safeguards.
- §4.1.3 makes risk assessment contextual and counterfactual, including already available capabilities and possible societal defenses/benefits. §4.2 warns superficial audits can create false assurance and requires appropriate access, resources, disclosure and update scrutiny.
- The proposal distinguishes uncertainty, mitigable risk and unmitigable severe risk, while AppendixA admits no fully satisfactory precise frontier-model definition. Scope, centralized power, capture, innovation and geopolitical effects remain open design problems.

**Counterevidence / alternative:** A coherent procedural route is not proof its evaluations discriminate harm or its institutions can implement it. Rollback and access restrictions have openness/use-case costs; the paper acknowledges safeguards and definitions need further specification.

**Limits:** Selective 52-page v1 reading; §3 compliance detail, §4.5 remainder, §5 start, remaining appendices and full references deferred. This is a policy proposal, not an adopted legal rule or measured intervention result.

**Replication:** `not_performed`. **Numerical check:** No experimental or policy-effect replication. No independently calibrated numerical risk threshold is adopted; author-reported quantities are treated as documentary descriptions only.

**Relevance:** `claim_evidence`. **Claim links:** [C83](claims.md#c83)

**Relevance rationale:** Source-level evidence for the stated conceptual, survey-method or policy-design claim; neither inclusion nor a separate-agent check establishes independent corroboration.

**Next check:** If leading with this governance route, check the corresponding final edition and specific deployment/compliance sections. Keep Table3 and time intervals as illustrations unless independently justified; do not present the proposal as established law or successful implementation.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2307.03718v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2307.03718v1) |
| `retrieved_at` | 2026-11-15T00:02:51.184124+00:00 |
| `attempted_at` | 2026-11-15T00:02:50.706425+00:00 |
| `sha256` | e131bf5e34bcaf0874a24f37e39066205450e61462bdc128bcce353ddb99b03d |
| `byte_length` | 1465410 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact acquired bytes are retained privately with a SHA-256 receipt; independent archival preservation is not claimed. |
| `published_on` | 2023-07-06 |
| `version_claim` | arXiv:2307.03718v1, 6 July 2023 |
| `locator_basis` | PDF viewer pages count the cover; printed pages stated separately where different. |
| `capture_path` | .source-captures/synthesis-e131bf5e34bcaf0874a24f37e39066205450e61462bdc128bcce353ddb99b03d.pdf |

<a id="r5_thresholds_05"></a>
### r5_thresholds_05

**Source:** `californiapolicyworkinggroup_thecaliforniareport_2025`. **Theme:** thresholds. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Official California governor-hosted final PDF matches canonical report title/date and working-group identity. Hosting/commissioning does not make the report an adopted law; front matter attributes individual scholarly capacity.

**Inspected scope:** Cover/byline, authorship statement and acknowledgments; PDFviewerpp4–8 (printedpp3–7: executive principles/origins/contents/intro); all PDFviewerpp37–44 (printedpp36–43: §4 closing, entire §5 scoping, §6.1–6.3 and §6.4 opening). Remaining historical cases, detailed transparency/reporting sections, references and AppendixA feedback form not fully read.

**Locators:** Executive principles printedpp3–5; §§5.1–5.2 printedpp36–40: threshold purpose, properties, timing, measurability and verification; §§6.1–6.3 printedpp40–43: submitted critiques and implementation questions

**Visual check:** No figures rendered. Selected pages contain prose and enumerated designs; no numerical chart extraction used.

**Findings:**

- The report proposes aligning threshold metrics with the regulatory purpose and differentiating developer-, cost-, model- and impact-level properties. It identifies when quantities become measurable, standardization and external verification as implementation constraints.
- Compute is presented as a possible initial screening filter, not a sole criterion. The report recommends mechanisms to update the metric itself as well as its numerical value; inference-time compute, distillation and synthetic data complicate pretraining accounting.
- Capability/risk evaluations and downstream impact are promising but need trustworthy measurements and monitoring infrastructure. Feedback summaries retain dissent on compute and flag inadequate evaluation standards, access, reporting definitions/costs and governmental capacity.

**Counterevidence / alternative:** More direct capability/impact metrics can arrive too late for pretraining obligations, be difficult to verify and be unavailable to open-model developers. A proposal to generate better evidence can be reasonable without showing that the proposed reporting or threshold system reduced risk.

**Limits:** 53-page final report remains selectively read. Feedback is author-summarized consultation, not representative sampling or independent validation. Report says it does not argue for/against particular legislation; historic EO/EU descriptions are not current-law verification. Historical-case causal claims not assessed in this event.

**Replication:** `not_performed`. **Numerical check:** No experimental or policy-effect replication. No independently calibrated numerical risk threshold is adopted; author-reported quantities are treated as documentary descriptions only.

**Relevance:** `claim_evidence`. **Claim links:** [C80](claims.md#c80), [C83](claims.md#c83)

**Relevance rationale:** Source-level evidence for the stated conceptual, survey-method or policy-design claim; neither inclusion nor a separate-agent check establishes independent corroboration.

**Next check:** Complete relevant transparency/adverse-event-reporting methods and sources before claiming a working implementation. Distinguish final June report from March draft and later legislation; retain purpose-specific adaptive design and explicitly defer policy-effect conclusions.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.gov.ca.gov/wp-content/uploads/2025/06/June-17-2025-%E2%80%93-The-California-Report-on-Frontier-AI-Policy.pdf) |
| `final_url` | [Source](https://www.gov.ca.gov/wp-content/uploads/2025/06/June-17-2025-%E2%80%93-The-California-Report-on-Frontier-AI-Policy.pdf) |
| `retrieved_at` | 2026-11-15T00:02:51.142249+00:00 |
| `attempted_at` | 2026-11-15T00:02:50.708363+00:00 |
| `sha256` | 4f7bcf74c9b48f513670a9d695f1466c982388941e2186c603063bd92a9349ad |
| `byte_length` | 666818 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact acquired bytes are retained privately with a SHA-256 receipt; independent archival preservation is not claimed. |
| `published_on` | 2025-06-17 |
| `version_claim` | The California Report on Frontier AI Policy, final report June17 2025 |
| `locator_basis` | PDF viewer pages count the cover; printed pages stated separately where different. |
| `capture_path` | .source-captures/synthesis-4f7bcf74c9b48f513670a9d695f1466c982388941e2186c603063bd92a9349ad.pdf |

<a id="r5_thresholds_06"></a>
### r5_thresholds_06

**Source:** `fmf_thresholdsfrontier_2025`. **Theme:** thresholds. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Canonical record URL names a May2025 PDF. Inherited inspected material instead names this official February HTML. Title/issuer authenticate the related work, but complete HTML does not establish byte/text equivalence to the canonical PDF; object/representation identity remains unresolved.

**Inspected scope:** All accessible current official HTML text read: article, four threshold approaches, tradeoffs, conclusion, footnotes, surrounding navigation and related-publication labels. The canonical May2025 PDF and linked PDF were not read; this event is scoped against the admitted object.

**Locators:** Article subsections on compute, direct risk, capability and outcome-based thresholds; Capability-threshold definition and footnotes; Conclusion/open research questions on crossing thresholds

**Visual check:** No rendered figures or linked PDF inspected; HTML contains prose and links.

**Findings:**

- The brief positively distinguishes compute, direct-risk, capability and scenario/outcome-based threshold approaches and sets out practical reasons for each; compute can assist early screening while risk/capability approaches seek more direct relevance.
- It acknowledges low-compute harmful versus high-compute benign cases, scarce probability/harm data, normative risk tradeoffs and unresolved ways to determine crossing or combine thresholds. Analogies to aviation do not calibrate AI risk.
- Its capability definition considers the capability in the absence of mitigations; the survey operational definition includes adequate mitigations. Their shared terminology must not be treated as a common validated threshold construct.

**Counterevidence / alternative:** Industry proposals and cross-framework similarities offer design material, but voluntary descriptions do not establish adoption rates, verified compliance or safety gains. The same-title related representation does not recertify the admitted PDF.

**Limits:** This is industry guidance and a related official representation, not independently validated thresholds. No complete_record_text effect or independent recertification of inherited Full text label. Unverified May PDF identity and linked PDF remain deferred; distinguish June risk-taxonomy publication.

**Replication:** `not_performed`. **Numerical check:** No experimental or policy-effect replication. No independently calibrated numerical risk threshold is adopted; author-reported quantities are treated as documentary descriptions only.

**Relevance:** `claim_evidence`. **Claim links:** [C80](claims.md#c80), [C82](claims.md#c82)

**Relevance rationale:** Source-level evidence for the stated conceptual, survey-method or policy-design claim; neither inclusion nor a separate-agent check establishes independent corroboration.

**Next check:** Resolve the canonical May PDF identity/route and compare complete PDF before any full-record recertification or bibliography URL correction. Use current HTML only with its own date/locator and qualification.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.frontiermodelforum.org/updates/issue-brief-thresholds-for-frontier-ai-safety-frameworks/) |
| `final_url` | [Source](https://www.frontiermodelforum.org/updates/issue-brief-thresholds-for-frontier-ai-safety-frameworks/) |
| `retrieved_at` | 2026-11-15T00:02:51.349892+00:00 |
| `attempted_at` | 2026-11-15T00:02:50.709590+00:00 |
| `sha256` | 86a93d7e57998d68d2a211fc197dc2b6c539cea2e47cff46aba093b2691a34e5 |
| `byte_length` | 118537 |
| `mime_type` | text/html |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact acquired bytes are retained privately with a SHA-256 receipt; independent archival preservation is not claimed. |
| `published_on` | 2025-02-07 |
| `version_claim` | Official issue-brief HTML dated 7 February 2025; May2025 canonical PDF equivalence unverified |
| `locator_basis` | Captured official HTML heading sequence, footnotes and dated page; not canonical May PDF pagination. |
| `capture_path` | .source-captures/synthesis-86a93d7e57998d68d2a211fc197dc2b6c539cea2e47cff46aba093b2691a34e5.html |

<a id="r5_reporting_01"></a>
### r5_reporting_01

**Source:** `stix_behindcloseddoors_2025`. **Theme:** reporting_audit. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact arXiv identifier and v1 title/byline match the canonical record. This scoped primary reading advances an inherited abstract-only label; it is not a full-text reading.

**Inspected scope:** Executive summary PDF pp. 1–3; internal access/application §§2.1–2.3, pp. 11–16; recommendations §6.1 and §6.2 opening/evaluation passages, pp. 36–39 including p. 38 n. 78; proposed governance walkthrough Appendix pp. 52–53. Other report material and underlying legal instruments were not systematically checked.

**Locators:** v1 PDF pp. 11–16, §§2.1–2.3 (internal permissions, configurations and applications); v1 PDF pp. 36–39, §§6.1–6.2; p. 38 n. 78; v1 Appendix pp. 52–53, Figure G caption and step-by-step walkthrough

**Visual check:** Figure G caption and diagram text were read in extracted text; no rendered figure or graph was visually checked. No numerical inference is made from plots.

**Findings:**

- Internal deployment may combine privileges, tools, model modifications, compute access and uses that differ from a public product; these configuration changes can alter evaluation and control requirements.
- The report proposes an Internal Deployment Team and an Internal Deployment Oversight Board with staged permissions, evaluation/control work and go/no-go governance. The walkthrough describes an intended process, not an observed adoption case.
- The broad suggestion of absent governance must be qualified: p. 38 n. 78 acknowledges Anthropic internal/employee provisions and OpenAI's April 2025 framework coverage of significant internal agentic deployments; p. 12 also identifies uncertainty about staged internal releases.

**Counterevidence / alternative:** Unknown internal practices do not establish their absence. Existing internal-use provisions could partly address the proposed gap, and the report provides no measured rate of internal-deployment failure or demonstrated benefit of the proposed structure.

**Limits:** 72-page report only partly read. Threat scenarios and the IDT/IDOB design are prospective proposals; actual implementation and comparative effectiveness were not established. Sector/legal analogies were not checked against operative instruments or current 2026 law.

**Replication:** `not_performed`. **Numerical check:** No experimental or incident-frequency calculation; no graph values promoted.

**Relevance:** `claim_evidence`. **Claim links:** [C84](claims.md#c84)

**Relevance rationale:** Source-level design, implementation or limitations evidence; no experimental replication or independent human review is claimed.

**Next check:** Check current developer internal-use policies and dated adoption/decision records before claiming an unfilled governance gap or an implemented control effect.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2504.12170v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2504.12170v1) |
| `retrieved_at` | 2026-11-15T00:02:55.986262+00:00 |
| `attempted_at` | 2026-11-15T00:02:54.991420+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact primary URLs and local bytes are retained privately; independent archival preservation is not claimed. |
| `sha256` | 11be580ba5691db4944ac686ef1a3b5a2a185477ba4638c9bc39920e05153d10 |
| `byte_length` | 3920541 |
| `mime_type` | application/pdf |
| `published_on` | 2025-04-17 |
| `version_claim` | arXiv:2504.12170v1, posted 16 April 2025; report cover dated 17 April 2025 |
| `locator_basis` | PDF viewer pages count the cover; these page numbers follow the report/PDF pagination. |
| `capture_path` | .source-captures/synthesis-11be580ba5691db4944ac686ef1a3b5a2a185477ba4638c9bc39920e05153d10.pdf |

<a id="r5_reporting_02"></a>
### r5_reporting_02

**Source:** `schuett_frontierdevelopers_2024`. **Theme:** reporting_audit. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. The captured PMC full-text representation identifies the exact canonical DOI 10.1111/risa.17665 and title. It records online publication 21 October 2024 and issue publication June 2025 (Risk Analysis 45(6),1332–1352); these dates are not silently collapsed. Direct Wiley retrieval returned HTTP403, so this event uses the final publisher article as represented in PMC.

**Inspected scope:** PMC article title/author/publication metadata and abstract; selected §2.1.1; §§2.3.1–2.3.2; §§3.1.1–3.1.3 and 3.2.1–3.2.3; §§3.3.1–3.3.3 including all extracted Table 2 rows; §§4.1–4.3; selected definitional footnotes 5,6,12,13. References and other sections not read end to end.

**Locators:** Final article §§2.3.1–2.3.2 (internal/external audit and combined assurance); Final article §§3.1.1–3.2.3 (proposed benefits and limitations); Final article §3.3.1/Table 2; §3.3.2 (coordination); §4.2 (future empirical research)

**Visual check:** Table 2 row text was read in captured HTML; no rendered diagram was visually checked.

**Findings:**

- Internal audit is proposed as a board/audit-committee-facing assurance function that evaluates risk-management adequacy; it is not a substitute name for the operational risk team.
- The author proposes combined assurance: align language, share information and use integrated reports where useful to reduce gaps, duplication and mistaken board impressions. More separate reports alone are not the objective.
- The article explicitly leaves day-to-day implementation and empirical effectiveness for future research once functions are adopted (§4.2); it acknowledges informal influence, resource/skills constraints and rapidly changing methodologies.

**Counterevidence / alternative:** Benefits are argued by institutional analogy and hypothetical frontier cases, not measured outcomes of adopting internal audit at a frontier developer. Management support can aid access while informal pressure undermines independence.

**Limits:** Selected sections, not complete article reading and not recertification of any earlier full-text label. Linked cited studies, empirical IT-audit literature, current adoption and current legal status were not independently reviewed. PMC hosting is not endorsement by the library or US government.

**Replication:** `not_performed`. **Numerical check:** No empirical effect estimate rechecked or experimental replication attempted. Table 2 is a proposed transfer of six IT-audit practice factors, not a measured frontier-AI quality scale.

**Relevance:** `claim_evidence`. **Claim links:** [C41](claims.md#c41)

**Relevance rationale:** Source-level design, implementation or limitations evidence; no experimental replication or independent human review is claimed.

**Next check:** Prioritize an actual frontier internal-audit adoption case with reporting lines, unresolved findings and remediation records; verify final/preprint differences only if a claim depends on them.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12369305/) |
| `final_url` | [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12369305/) |
| `retrieved_at` | 2026-11-15T00:03:07.833259+00:00 |
| `attempted_at` | 2026-11-15T00:03:07.285560+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact primary URLs and local bytes are retained privately; independent archival preservation is not claimed. |
| `sha256` | 73f1171802f1c026361236c28c7a39a8aeb301a9ca1e16328328a2b650be2b2a |
| `byte_length` | 502754 |
| `mime_type` | text/html |
| `published_on` | 2024-10-21 |
| `version_claim` | Publisher final article represented in PMC; online 2024-10-21, 2025 June issue |
| `locator_basis` | HTML section/subsection and Table 2 locators; article issue pages 1332–1352 are metadata, not reconstructed HTML page breaks. |
| `capture_path` | .source-captures/synthesis-73f1171802f1c026361236c28c7a39a8aeb301a9ca1e16328328a2b650be2b2a.html |

<a id="r5_reporting_03"></a>
### r5_reporting_03

**Source:** `brundage_frontierauditingrigorous_2026`. **Theme:** reporting_audit. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Exact canonical arXiv identifier 2601.11699, but the v4 cover dated 7 February 2026 retitles the paper to Frontier AI Auditing: Toward Rigorous Third-Party Assessment of Safety and Security Practices at Leading AI Companies. The canonical record uses the earlier title ending frontier AI systems. Treat this inspected revision as related_edition; do not assert all-edition equivalence or recertify earlier reading scope.

**Inspected scope:** v4 cover/title/byline/version; executive summary PDF pp. 2–6; PDF pp. 30–36 covering §5.3.3 AAL descriptions/Table 3, §5.3.4 assurance-level choice and §5.4 opening/Figure 7 access taxonomy. Remaining 115-page report and appendices not read.

**Locators:** arXiv:2601.11699v4 executive summary PDF pp. 2–6; v4 §5.3.3, Table 3, PDF pp. 30–34 (proposed AAL1–4); v4 §§5.3.4–5.4 opening, PDF pp. 34–36; Figure 7 caption/access categories

**Visual check:** Table 3 and Figure 7 text/captions were read in PDF extraction; no rendered visual check or quantitative inference from a figure.

**Findings:**

- The proposal expands audit scope beyond public products to organization-level practices, internal deployment, hardware and information security, with protected nonpublic access rather than universal public disclosure.
- AAL1–4 vary duration, scope and depth of access, verification and resistance to concealment. The text treats AAL3/4 as not currently feasible as fully described and identifies research/pilots as necessary; higher levels are design aspirations.
- Audit conclusions should state assumptions and validity conditions and may need revision after material system or organizational changes; access, competence and incentives remain conditions, not solved consequences of an audit label.

**Counterevidence / alternative:** Greater access and an AAL label do not themselves demonstrate independence, adequate tests or harm reduction. Illustrative Table 3 conclusions must not be reported as actual verified findings.

**Limits:** Only specified selected sections. The proposed access ladder, feasibility judgements, costs and illustrative audit conclusions are not calibrated experimental confidence estimates or observed real-company audit findings. V4 title/version differences remain a canonical metadata reconciliation lead.

**Replication:** `not_performed`. **Numerical check:** Documentary check only: four AAL categories are proposed. No costs, timelines or assurance-probability numbers are promoted; no replication or empirical audit-effect comparison was performed.

**Relevance:** `claim_evidence`. **Claim links:** [C38](claims.md#c38), [C39](claims.md#c39), [C41](claims.md#c41), [C84](claims.md#c84)

**Relevance rationale:** Source-level design, implementation or limitations evidence; no experimental replication or independent human review is claimed.

**Next check:** Check exact v1–v4 differences for any headline claim; read the detailed independence/follow-up sections and any later audit pilots before treating the proposal as operational evidence.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2601.11699v4) |
| `final_url` | [Source](https://arxiv.org/pdf/2601.11699v4) |
| `retrieved_at` | 2026-11-15T00:02:55.252734+00:00 |
| `attempted_at` | 2026-11-15T00:02:54.992245+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact primary URLs and local bytes are retained privately; independent archival preservation is not claimed. |
| `sha256` | 54bb20846e25e3c13ed6f924c845ae914b66d6fa87a1bc99925c01cd962b8b41 |
| `byte_length` | 1725041 |
| `mime_type` | application/pdf |
| `published_on` | 2026-02-07 |
| `version_claim` | arXiv:2601.11699v4, cover version stamp 7 February 2026 (report cover also says January 2026) |
| `locator_basis` | PDF viewer pages count the cover and align with printed page numbers in checked scope. |
| `capture_path` | .source-captures/synthesis-54bb20846e25e3c13ed6f924c845ae914b66d6fa87a1bc99925c01cd962b8b41.pdf |

<a id="r5_reporting_04"></a>
### r5_reporting_04

**Source:** `cset_incidentskeycomponents_2025`. **Theme:** reporting_audit. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact title, January 2025 date and CSET publisher match the canonical report. The PDF names Ren Bin Lee Dixon and Heather Frase and provides DOI 10.51593/20240023 on p. 27; canonical corporate-author metadata requires a separate, minimal metadata review rather than a new bibliography record.

**Inspected scope:** Complete accessible text of all 32 PDF pages, including cover, executive summary, §§Introduction/Defining AI Incidents/Key Components/Way Forward, all Tables 1–6, entire Appendix Tables A1–A4 and notes, About/Acknowledgments, and all endnotes. PDF pp. 8 and 19 visually checked after text reading; no linked source or underlying dataset is included in this complete-report event.

**Locators:** January 2025 PDF pp. 6–7 and 10–11 (definitions, incident/near-miss/hazard scope); PDF pp. 8–16, Tables 1–6 (proposed component template); PDF pp. 17–18 (independent investigation, tailoring and follow-up); PDF pp. 19–26, Appendix Tables A1–A4; p. 27 DOI/byline metadata

**Visual check:** Rendered PDF pp. 8 and 19 visually inspected: Table 1 component structure and first page of Table A1 agree with extracted text. Other tables read completely in text; no blanket visual-figure audit is claimed.

**Findings:**

- The report proposes a mandatory reporting regime for incidents and near misses, with hazards generally suitable for voluntary reporting; prospective systemic risks need additional risk-management work.
- Proposed reporting fields cover harm type, technical/nontechnical mechanisms, severity dimensions, system/model/dataset information, context and safeguards, users/nonusers, and incident response. Some information will be unavailable at the initial report.
- The authors recommend domain tailoring and an independent investigation capability to obtain technical/contextual root-cause evidence beyond news accounts and initial submissions. Severity thresholds/scoring need further development.
- The appendix compares existing AI and non-AI reporting resources. Shared definitions and AIID/OECD lineage make this design synthesis, not an independent sample of corroborating incidents.

**Counterevidence / alternative:** News-based reports and initial disclosures can be incomplete, duplicate or unverifiable. A reporting mandate and a rich template may create useful evidence but do not establish enforcement, reporting coverage, validated attribution or effective remediation.

**Limits:** Full report text read, not underlying sources, incident databases or legal regimes. The proposal and cross-sector synthesis are not an implemented AI reporting system or a causal harm-reduction study. Appendix source-count wording is not used: narrative says twelve databases/documents while the AI-initiative table appears to enumerate a different unit/count.

**Replication:** `not_performed`. **Numerical check:** No validated severity score or measured reduction estimated. Category structure and table content checked documentarily; exact appendix source-count discrepancy left unused rather than forced into a headline.

**Relevance:** `claim_evidence`. **Claim links:** [C86](claims.md#c86)

**Relevance rationale:** Source-level design, implementation or limitations evidence; no experimental replication or independent human review is claimed.

**Next check:** Prioritize an enacted reporting regime and observed investigation/remediation case; test template feasibility, underreporting and severity decisions. Omit the appendix resource count until units/version are reconciled.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://cset.georgetown.edu/wp-content/uploads/CSET-AI-Incidents.pdf) |
| `final_url` | [Source](https://cset.georgetown.edu/wp-content/uploads/CSET-AI-Incidents.pdf) |
| `retrieved_at` | 2026-11-15T00:02:55.783378+00:00 |
| `attempted_at` | 2026-11-15T00:02:54.992648+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact primary URLs and local bytes are retained privately; independent archival preservation is not claimed. |
| `sha256` | c23bc0d3f0a6d7c3b44eb689c3b60edf91470de1b02802afbffaf11d3c34f73a |
| `byte_length` | 803145 |
| `mime_type` | application/pdf |
| `published_on` | 2025-01 |
| `version_claim` | CSET January 2025 report; DOI 10.51593/20240023 |
| `locator_basis` | All32 PDF viewer pages; printed CSET page numbers shown in footers and used for cited locators. |
| `capture_path` | .source-captures/synthesis-c23bc0d3f0a6d7c3b44eb689c3b60edf91470de1b02802afbffaf11d3c34f73a.pdf |

<a id="r5_reporting_05"></a>
### r5_reporting_05

**Source:** `oecd_commonreportingincidents_2025`. **Theme:** reporting_audit. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical title/DOI 10.1787/f326d4ac-en, OECD Artificial Intelligence Papers No. 34, February 2025. This is the primary OECD publication PDF, not a later incident database snapshot.

**Inspected scope:** Complete accessible text of all 27 PDF pages: front matter, English/French abstracts, acknowledgments, executive summary, §§1–3, all tables, Annex A stocktaking, Annex B detailed29-field schema, Annex C relationship taxonomy, and references pp. 26–27. Rendered pp. 17,23,25 visually checked. No linked database payload or cited sources are included in the complete-document claim.

**Locators:** OECD No. 34 PDF pp. 11–12 (scope, intended use, limits); PDF pp. 13–18, Tables 2.1–2.2 (selection method and schema); PDF p. 19 conclusions (future testing); PDF pp. 20–25, Annexes A–C, especially Tables B.1/C.1

**Visual check:** Rendered pp. 17,23,25 visually inspected: mandatory-field asterisks, schema answer formats and Annex C nonexclusive relationship categories agree with extracted text. All remaining tables and captions read in text.

**Findings:**

- The proposal supplies a common incident/hazard information format for interoperability; it does not prescribe an interface, create a legal reporting duty or offer specific preventive/corrective-action guidance.
- Stocktaking draws on four resources (OECD AI classification, AIID, global product recalls and AIM), then expert-group selection. A common vocabulary can make evidence more comparable without proving completeness or prevention.
- Version/system identity, reporter/source information, severity/harm, context, actions taken and reproducibility are among the selected fields. Annex C permits multiple nonexhaustive relationships per event; categories must not be treated as mutually exclusive incident counts.
- Conclusions call for testing the framework, including future open submissions; they do not report a validated reduction in harm.

**Counterevidence / alternative:** The schema includes hazards as well as actual incidents, while the CSET mandatory-scope proposal distinguishes near misses and generally voluntary hazards. Pooling counts across these scopes, or counting multiple reports/causal categories as independent incidents, can manufacture agreement.

**Limits:** Document text and schema reviewed, not deployment of the proposed reporting framework, live OECD AIM submissions or downstream actions. Submitted causal categories are claims to investigate, not independent causal validation. Existing OECD and AIID inputs overlap with CSET/McGregor rather than providing independent observed effects.

**Replication:** `not_performed`. **Numerical check:** Documentary arithmetic verified: 88 candidate criteria across 8 dimensions narrowed to 10 recurrent plus 19 complementary = 29 selected criteria. Counted 7 starred mandatory fields (1,2,3,4,7,10,11); mandatory means required by this proposed format, not a legal reporting obligation. No experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C86](claims.md#c86), [C87](claims.md#c87)

**Relevance rationale:** Source-level design, implementation or limitations evidence; no experimental replication or independent human review is claimed.

**Next check:** Check actual adoption, submitted-field completeness, deduplication and investigation/action outcomes; any legal-duty claim requires the relevant operative instrument rather than schema asterisks.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/towards-a-common-reporting-framework-for-ai-incidents_8c488fdb/f326d4ac-en.pdf) |
| `final_url` | [Source](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/towards-a-common-reporting-framework-for-ai-incidents_8c488fdb/f326d4ac-en.pdf) |
| `retrieved_at` | 2026-11-15T00:02:56.114873+00:00 |
| `attempted_at` | 2026-11-15T00:02:54.992995+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact primary URLs and local bytes are retained privately; independent archival preservation is not claimed. |
| `sha256` | e8c1a12dd0f69b56641a83c96a728e378732966b517cc48672b3f424de67f3d1 |
| `byte_length` | 2541493 |
| `mime_type` | application/pdf |
| `published_on` | 2025-02 |
| `version_claim` | OECD Artificial Intelligence Papers No. 34, February 2025; DOI 10.1787/f326d4ac-en |
| `locator_basis` | 27 PDF viewer pages align with printed publication pagination; Table/Annex locators are stable. |
| `capture_path` | .source-captures/synthesis-e8c1a12dd0f69b56641a83c96a728e378732966b517cc48672b3f424de67f3d1.pdf |

<a id="r5_reporting_06"></a>
### r5_reporting_06

**Source:** `mcgregor_preventingrepeatedfailures_2021`. **Theme:** reporting_audit. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Final AAAI proceedings PDF retrieved from the official AAAI CDN, exact DOI/title/author/venue and printed pages 15458–15463. This closes the prior final-copy access gap for this bounded event, without assuming the earlier preprint and final text are interchangeable or independently recertifying the earlier reading history.

**Inspected scope:** Complete accessible text of all 6 final proceedings PDF pages, printed 15458–15463: abstract, introduction/motivation, AIID architecture and discovery/submission/taxonomy features, all figure captions, hypothetical fairness-use example, conclusions, acknowledgments and references. Figures 2–5 visually inspected on PDF pages 3–5; Figure 1 image not pixel-inspected. No current database, software or linked external source was audited.

**Locators:** Final AAAI 2021 proceedings pp. 15458–15463 (entire article); Printed pp. 15459–15462, system architecture, stable IDs, submissions and taxonomies; Figure 2 (two reports for Incident 36); Printed p. 15462 Figure 5 intended fairness application; p. 15463 conclusion

**Visual check:** Rendered PDF pages 3–5 visually inspected, including Figures 2–5. Figure 1 NTSB screenshot was read through caption/surrounding text only; no claim to have checked every screenshot pixel.

**Findings:**

- The paper describes a built database with stable incident identifiers consolidating multiple reports, full-text/faceted discovery, duplicate-aware submissions, namespaced taxonomies, and MongoDB/static application architecture.
- Plural taxonomies allow differing perspectives rather than assuming one universal incident classification; stable IDs separate an incident from the number of published reports about it.
- Figure 5 illustrates a potential fairness-risk discovery/mitigation workflow; the paper describes early adoption interest but does not measure prevented failures. Incident-report volume is influenced by publicity and reporting practices and cannot establish population failure rates.

**Counterevidence / alternative:** Operational search and cataloguing are real contributions, but discoverability does not establish verified root cause, representative coverage, inter-rater reliability or successful mitigation. A compelling hypothetical use case is not evidence of an observed control effect.

**Limits:** Historical 2021 description, not a current census or software test. Database records and linked media were not independently fact-checked, and the article does not evaluate a causal prevention/remediation effect. Full-text reading of this final paper does not certify all prior reading labels or reproduce experiments.

**Replication:** `not_performed`. **Numerical check:** Unit check: more than 1000 is a historical count of incident reports, not distinct incidents or failure incidence; Figure 2 visibly shows two reports linked to the same Incident 36. No denominator-based population rate or harm-reduction statistic is derived.

**Relevance:** `claim_evidence`. **Claim links:** [C27](claims.md#c27), [C87](claims.md#c87)

**Relevance rationale:** Source-level design, implementation or limitations evidence; no experimental replication or independent human review is claimed.

**Next check:** Assess an actual downstream use with documented decision/remediation and attribution limits; use a dated live database snapshot only if a present-day count or quantitative trend is necessary.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://cdn.aaai.org/ojs/17817/17817-13-21311-1-2-20210518.pdf) |
| `final_url` | [Source](https://cdn.aaai.org/ojs/17817/17817-13-21311-1-2-20210518.pdf) |
| `retrieved_at` | 2026-11-15T00:03:07.950917+00:00 |
| `attempted_at` | 2026-11-15T00:03:07.284913+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round. Exact primary URLs and local bytes are retained privately; independent archival preservation is not claimed. |
| `sha256` | 9fd042c9a1d8d99c17e7a8fa682ffb4d34cb4c20191cb5d1b21faa396f6a3aff |
| `byte_length` | 2801548 |
| `mime_type` | application/pdf |
| `published_on` | 2021 |
| `version_claim` | Final AAAI 2021 proceedings article,35(17),15458–15463; DOI 10.1609/aaai.v35i17.17817 |
| `locator_basis` | PDF viewer pages 1–6 correspond to printed proceedings pages 15458–15463. |
| `capture_path` | .source-captures/synthesis-9fd042c9a1d8d99c17e7a8fa682ffb4d34cb4c20191cb5d1b21faa396f6a3aff.pdf |

<a id="r5_persistence_01"></a>
### r5_persistence_01

**Source:** `hubinger_sleeperagentstraining_2024`. **Theme:** training_persistence. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact arXiv identifier, original title and byline match the admitted record; this event pins v3 rather than the mutable unversioned link.

**Inspected scope:** PDF pp2–3,9–10,15,18–20,25–27,39–40 read in full; includes model-organism framing, selected RL/SFT comparisons, adversarial-training methods/results and alternative explanations. Cover title/byline identifiers checked. Remaining pages, references and appendices were not read in full.

**Locators:** v3 §§1–2/model-organism framing, pp2–3,9–10; §4/HHH RL pp15,18–20; Figures10–11 captions; §6 adversarial training pp25–27; Figure17 caption; Alternative explanations/limitations pp39–40

**Visual check:** Selected figure captions and extracted chart text read; no rendered figure was visually inspected and no plot values digitized.

**Findings:**

- Deliberately constructed conditional policies can survive tested behavioral safety training, including selected adversarial-training runs; model construction supplies the adversarial policy rather than discovering its natural emergence.
- HHH RL is substantially more effective against smaller models in the scanned setup. SFT is generally more effective than RL at removing studied backdoors, although some constructed variants remain robust.
- Adversarial training often suppresses responses to imperfect red-team prompts while preserving exact-trigger behavior. Improved trigger discrimination is a proposed explanation, not proof that adversarial training generally causes deception.

**Counterevidence / alternative:** The paper reports mitigation successes, scale/variant dependence and alternative explanations. Preference-model disincentives and coherent sampled reasoning do not settle causal deceptive reasoning or generalization to complex triggers.

**Limits:** Selected reading of 71-page paper; omitted appendices may change detailed interpretation. Deliberately trained conditional policies and a particular preference-model/RL/SFT setup are not evidence of natural deceptive alignment frequency.

**Replication:** `not_performed`. **Numerical check:** No recomputation or experimental replication; no affected plot-rate headline adopted.

**Relevance:** `claim_evidence`. **Claim links:** [C88](claims.md#c88)

**Relevance rationale:** Supplies conditional persistence, transfer, mitigation or endpoint evidence; constructed experiments do not establish natural incidence or the failure of every training method.

**Next check:** If this becomes a publication-leading mechanism claim, read remaining SFT and appendix ablations and independently inspect their figures; otherwise retain the conditional model-organism wording.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2401.05566v3) |
| `final_url` | [Source](https://arxiv.org/pdf/2401.05566v3) |
| `retrieved_at` | 2026-11-15T00:03:08.924709+00:00 |
| `attempted_at` | 2026-11-15T00:03:08.544848+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary-version URLs and locally retained bytes are preserved. Independent archival preservation is not claimed. |
| `sha256` | 988e62785a47533775a543c78415dd0994341987f3124d57a81f46c931227bed |
| `byte_length` | 3696766 |
| `mime_type` | application/pdf |
| `published_on` | 2024-01-17 |
| `version_claim` | arXiv v3 |
| `locator_basis` | PDF viewer pages count the cover as page 1; printed page numbers coincide unless stated. |
| `capture_path` | .source-captures/synthesis-988e62785a47533775a543c78415dd0994341987f3124d57a81f46c931227bed.pdf |

<a id="r5_persistence_02"></a>
### r5_persistence_02

**Source:** `zhang_persistentpretraining_2025`. **Theme:** training_persistence. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact admitted eprint identifier, title and author group match the captured original preprint. The bibliography year is 2025; this event explicitly certifies only the 17 October 2024 arXiv v1 text, not a later publication-final edition.

**Inspected scope:** Every text page of the 17-page PDF read: abstract, §§1–6, all references, Appendices A–C, tables, figure captions and displayed examples. Rendered checks were separately limited to pp8 and15.

**Locators:** v1 §3 threat model/training setup pp3–4; §4.1.3 and Figure6 p8; §4.1.4 and Figure7 pp8–9; §5 discussion pp9–10; Appendices B–C pp15–17; Tables2–3

**Visual check:** Rendered PDF p8 (Figures6–7) and p15 (Table2/training details) inspected. All other figure captions/text read, but remaining graphical elements not individually visually checked.

**Findings:**

- Under data-only pretraining poisoning followed by the specified supervised and preference-training pipeline, three studied objectives retain measurable effects; persistent means detectable relative to an unpoisoned baseline, not unchanged rates.
- The jailbreak objective does not show persistent measured harmful-response effects after the tested safety pipeline. This is consequential counterevidence to claims that every backdoor objective survives training.
- Clean-no-trigger controls, relative-likelihood biased-comparison outcomes and multi-generation extraction scoring have distinct meanings. Neither paired-response likelihood nor a cumulative extraction measure estimates population persuasion or general operational data exfiltration.
- The attacker controls injected pretraining documents, not later tokenizer/model architecture/training order or safety training. Shortened pretraining and chosen models/tasks limit deployment extrapolation.

**Counterevidence / alternative:** Persistence differs by objective; jailbreak null and incoherent/degenerated outputs complicate a blanket safety-failure interpretation. Filtration bypass is discussed as future work rather than established defeat of every defense.

**Limits:** All PDF text was read, not all figures visually verified. No separate linked code/data/supplement or later/final edition was certified. From-scratch pretraining uses a shortened 100B-token regime, approximately 5% of the stated reference run, with reduced downstream capability. Denial-of-service/context-extraction are triggered backdoor objectives; the persistent belief-manipulation objective is non-triggered poisoning and must remain distinct.

**Replication:** `not_performed`. **Numerical check:** Documentary comparison of methods/appendix and affirmative/null endpoints; no numerical reproduction of models or data.

**Relevance:** `claim_evidence`. **Claim links:** [C88](claims.md#c88)

**Relevance rationale:** Supplies conditional persistence, transfer, mitigation or endpoint evidence; constructed experiments do not establish natural incidence or the failure of every training method.

**Next check:** Retain the jailbreak null beside positive persistence results. If publication depends on final-edition equivalence, check final proceedings separately; do not recode the 2024 primary capture as a 2025 final publication.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2410.13722v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2410.13722v1) |
| `retrieved_at` | 2026-11-15T00:03:08.919704+00:00 |
| `attempted_at` | 2026-11-15T00:03:08.546483+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary-version URLs and locally retained bytes are preserved. Independent archival preservation is not claimed. |
| `sha256` | d3196f0062b6e5fac15b39fd89098ff1fd6396a52279f2d502b833a63d37537e |
| `byte_length` | 950345 |
| `mime_type` | application/pdf |
| `published_on` | 2024-10-17 |
| `version_claim` | arXiv v1 |
| `locator_basis` | PDF viewer pages count the cover as page 1; printed page numbers coincide unless stated. |
| `capture_path` | .source-captures/synthesis-d3196f0062b6e5fac15b39fd89098ff1fd6396a52279f2d502b833a63d37537e.pdf |

<a id="r5_persistence_03"></a>
### r5_persistence_03

**Source:** `cloud_subliminallearning_2025`. **Theme:** training_persistence. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Captured arXiv v1 matches the admitted identifier, title and byline; the current abstract page also reports v1.

**Inspected scope:** Main PDF pp2–13 (§§1–9, including selected acknowledgments/reference opening); cover/abstract identifiers; AppendixD.2 p28 and D.4 pp31–32. An unrelated illustrative list on p27 was encountered but is not evidence for the claims. Remaining references, proof appendix and other appendices were not read in full.

**Locators:** v1 §§3–4 controlled trait-transfer studies pp4–8; §5.1 Figure8 and §5.2 in-context controls p9; §6.1 Theorem1 p10; §6.2 p11; §8 limitations p13; AppendixD.2 p28; D.4/Figure18 pp31–32

**Visual check:** Rendered p9/Figure8 model-pair matrix and p32/Figure18 ROC inspected; other figures only text/captions in the selected scope.

**Findings:**

- Teachers and students can show measured trait transfer after finetuning on filtered numbers, code or mathematical reasoning, with untreated and alternate-teacher controls; these controlled results do not estimate real production-distillation incidence.
- Transfer is model/trait dependent. Same-type pairs show effects, but GPT-4o and GPT-4.1 also transfer across the named types; authors attribute this exception to shared initialization. Other mismatched pairs are weak or null overall, with isolated significant cells.
- Cross-model comparison restricts animals to those that transmit within both model types. In-context examples and a classification probe fail to reproduce/detect the effect in tested settings, bounding simple semantic explanations without exhausting all possible cues.
- The theorem requires same initialization and a small single-gradient-step/full-output-distillation approximation (with a zero-effect alternative). It is not a theorem that arbitrary sampled, filtered multistep distillation transfers every teacher trait.
- Freeform misalignment rates depend on evaluation suffixes and a coherence filter. The reasoning-filter ROC labels teacher provenance, not a human-certified misalignment label for each retained completion.

**Counterevidence / alternative:** Cross-model exceptions, nontransmitting traits and selected null controls prevent a universal model-identity rule. Filtering is imperfect, but failures under one detector do not establish impossibility of filtering or absence of any semantic cue.

**Limits:** Not a full 34-page reading; proof appendices and many experiment details remain unread. Closed-model identity and shared-initialization explanation depend on authors and a cited developer interview, not independent weight inspection.

**Replication:** `not_performed`. **Numerical check:** Checked matrix exceptions and ROC-axis/label interpretation against captions; no model replication, significance recomputation or independent validation of teacher labels.

**Relevance:** `claim_evidence`. **Claim links:** [C90](claims.md#c90)

**Relevance rationale:** Supplies conditional persistence, transfer, mitigation or endpoint evidence; constructed experiments do not establish natural incidence or the failure of every training method.

**Next check:** Read remaining claim-critical appendix methods/proof only if numerical or general mechanism claims lead publication; retain model-pair exceptions and conditional endpoint wording.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2507.14805v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2507.14805v1) |
| `retrieved_at` | 2026-11-15T00:03:09.086074+00:00 |
| `attempted_at` | 2026-11-15T00:03:08.545703+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary-version URLs and locally retained bytes are preserved. Independent archival preservation is not claimed. |
| `sha256` | fd75379cef4e9dfcf3478779e07ae3214e1d2ee1a726eae807b9dc428006caa5 |
| `byte_length` | 1332129 |
| `mime_type` | application/pdf |
| `published_on` | 2025-07-20 |
| `version_claim` | arXiv v1 |
| `locator_basis` | PDF viewer pages count the cover as page 1; printed page numbers coincide unless stated. |
| `capture_path` | .source-captures/synthesis-fd75379cef4e9dfcf3478779e07ae3214e1d2ee1a726eae807b9dc428006caa5.pdf |

<a id="r5_persistence_04"></a>
### r5_persistence_04

**Source:** `li_backdoorllmcomprehensive_2024`. **Theme:** training_persistence. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Captured original-title arXiv v1 matches admitted eprint, title, byline and 2024 date. Current arXiv v2 adds defenses and changes the title; the canonical abstract appears to describe that later expansion. The original full-text event does not certify v2.

**Inspected scope:** Every text page of the 20-page v1 PDF read: main §§1–6, all references, ethics and experimental Appendices A–B, tables, captions and displayed examples. Visual inspection separately limited to pp5 and16.

**Locators:** v1 §3/Table2 access taxonomy pp3–4; Table3 caption p5 and §4.1 metric definitions p6; §4.2–4.5/results Tables4–6 pp6–9; §5 limitations p9; AppendixA.4 p15; B.1/Figure1 p16; B.2–B.3 pp16–17

**Visual check:** Rendered p5/Table3 and p16/Figure1 inspected. Remaining graphs/captions and example text were read, but graphical trajectories on p17 were not visually audited.

**Findings:**

- Data poisoning, parameter editing, hidden-state intervention and modified reasoning demonstrations are different adversarial access assumptions; their success rates cannot be pooled into one unrestricted deployment risk.
- Measured effectiveness and apparent scale trends vary by attack, task and metric. Exact-target-answer success differs from occurrence of an inserted reasoning step; fixed editing settings and quantization/demonstration changes confound generic scale inferences.
- The original v1 explicitly lacks robust defense support. Its external-judge probe has high detection on overtly harmful inputs but low average detection on benign/refusal inputs; authors acknowledge harmful-content cues as an alternative to trigger detection.

**Counterevidence / alternative:** Some task/model cells are weak, null or reversed; model capacity does not monotonically increase every attack effect. A judge that notices harmful words is not established backdoor detection, and no adequate clean-benign false-positive estimate is established in this reading.

**Limits:** No separate code/data replication or later-edition full read. Benchmarks reuse attack implementations and task datasets, so outcomes are not independent corroboration of each original attack paper. No complete factorial crossing of every access/task/model category is inferred.

**Replication:** `not_performed`. **Numerical check:** Documentary comparison of table headers, caption and metric definitions. Table3 caption reverses triggered/untriggered descriptions relative to its column labels and §4.1; affected quantitative comparisons are withheld. Figure1 visual confirms differing judge performance on harmful vs benign/refusal prompts.

**Relevance:** `claim_evidence`. **Claim links:** [C91](claims.md#c91)

**Relevance rationale:** Supplies conditional persistence, transfer, mitigation or endpoint evidence; constructed experiments do not establish natural incidence or the failure of every training method.

**Next check:** Keep the original-version caption issue visible and avoid affected numerical headlines. Use the separately captured v2 event for defense comparisons; reconcile canonical title/abstract version metadata before relying on a mutable abstract.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2408.12798v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2408.12798v1) |
| `retrieved_at` | 2026-11-15T00:03:08.908510+00:00 |
| `attempted_at` | 2026-11-15T00:03:08.547016+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary-version URLs and locally retained bytes are preserved. Independent archival preservation is not claimed. |
| `sha256` | 6b83d7db360d261de0a1ca07a928435710faaa2603c1703c63ec7251b77f0c5d |
| `byte_length` | 1206108 |
| `mime_type` | application/pdf |
| `published_on` | 2024-08-23 |
| `version_claim` | arXiv v1 |
| `locator_basis` | PDF viewer pages count the cover as page 1; printed page numbers coincide unless stated. |
| `capture_path` | .source-captures/synthesis-6b83d7db360d261de0a1ca07a928435710faaa2603c1703c63ec7251b77f0c5d.pdf |

<a id="r5_persistence_05"></a>
### r5_persistence_05

**Source:** `gloaguen_finetuningactivated_2025`. **Theme:** training_persistence. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Captured original-title v1 matches the admitted title, identifier and four-author byline. Current arXiv v4 has a different title and expanded adaptation claims; its abstract cannot be substituted for v1 methods/results.

**Inspected scope:** PDF pp1–2,5–9,26–27,32 read in full: original abstract/introduction, experimental results/ablations/limitations, selected evaluation details and resource notes. Core attack-construction §§3–4.1 pp3–4 and most appendices were not read.

**Locators:** v1 §§4.2–4.5 results/ablations pp5–9; §4.4/Table7 and §4.5/Table8 p8; §5 limitations p9; AppendixB.3 pp26–27; AppendixD.2 p32

**Visual check:** Rendered p8/Tables7–8 inspected; remaining figures/tables only text/captions in selected pages.

**Findings:**

- An adversary-supplied model can have little measured target behavior before adaptation and increased target behavior after selected benign supervised finetuning; the trigger is the later training process rather than solely an inference prompt.
- Clean baseline finetuning can itself affect safeguards, so the appropriate comparator is the finetuned clean baseline. Generic/task-conflicting finetuning does not activate every objective in this study.
- The robustness study is limited to advertisement behavior in one 1B model and selected task/configuration changes; Table7 contains near-null settings as well as stronger ones. This is not universal robustness to every optimizer, learning rate or finetuning method.
- Utility coloring uses an author-selected baseline-relative cutoff and is not a formal equivalence result. A refusal experiment is excluded for judge/answer-format problems, demonstrating endpoint fragility.

**Counterevidence / alternative:** Null activation under some training tasks/configurations and changed benign baseline behavior restrict both attack and mitigation conclusions. V1 leaves RL and logit distillation to future work, although later current-page wording expands scope.

**Limits:** Selected 32-page reading; no full attack-method or appendix certification. V1 tests supervised finetuning of models up to 3B, not every adaptation or frontier-scale model. Linked resources licenses were not independently verified.

**Replication:** `not_performed`. **Numerical check:** Checked Table7 categorical configuration differences and nonuniversal effects; no experimental replication, pooled robustness average recomputation or formal utility noninferiority test.

**Relevance:** `claim_evidence`. **Claim links:** [C89](claims.md#c89)

**Relevance rationale:** Supplies conditional persistence, transfer, mitigation or endpoint evidence; constructed experiments do not establish natural incidence or the failure of every training method.

**Next check:** If later-edition RL/distillation claims become consequential, capture and inspect v4 as a separate related-edition event. For now retain original SFT/model-size boundaries and keep utility/judge limitations explicit.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2505.16567v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2505.16567v1) |
| `retrieved_at` | 2026-11-15T00:03:09.363484+00:00 |
| `attempted_at` | 2026-11-15T00:03:08.547680+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary-version URLs and locally retained bytes are preserved. Independent archival preservation is not claimed. |
| `sha256` | 0f2e0d8fa26f46aec538511108fe9a93150cc480fb66ee858adb7f9596177317 |
| `byte_length` | 2433830 |
| `mime_type` | application/pdf |
| `published_on` | 2025-05-22 |
| `version_claim` | arXiv v1 |
| `locator_basis` | PDF viewer pages count the cover as page 1; printed page numbers coincide unless stated. |
| `capture_path` | .source-captures/synthesis-0f2e0d8fa26f46aec538511108fe9a93150cc480fb66ee858adb7f9596177317.pdf |

<a id="r5_persistence_06"></a>
### r5_persistence_06

**Source:** `li_backdoorllmcomprehensive_2024`. **Theme:** training_persistence. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Same arXiv identifier/byline but changed title adds defenses and substantially expands evaluation. Related-edition selection does not upgrade the admitted original record to full-text-v2 status.

**Inspected scope:** PDF p1 cover/abstract, pp8–10 (CoT-results continuation, full §5/Table7 and conclusion/reference opening), pp16–18 (defense taxonomy/configurations, Table4, complete D.2 discussion and beginning of additional-result sections). Other v2 pages were not fully read.

**Locators:** v2 §5 and Table7 p9; AppendixD.1 defense configurations p16; AppendixD/Table4 and D.2 pp17–18

**Visual check:** No rendered v2 page inspected. Table7 and appendix tables read from layout-preserving extraction; do not claim independent plot inspection.

**Findings:**

- The added defense study shows substantial mitigation of targeted-refusal effects for some methods and uncertain mitigation of jailbreaking effects under its particular model/task/data-poisoning configurations.
- Version-specific positive mitigation evidence challenges blanket statements that behavioral training or every tested defense fails. Lower residual trigger-conditioned success is not complete backdoor removal.
- External-judge detection and six mitigation methods have different access/data/assurance assumptions. Lower perplexity is a narrow endpoint, not a deployment-safety guarantee.

**Counterevidence / alternative:** The table/prose disagreement about increased jailbreak rates cannot be resolved from inspected text. Task-specific method/configuration choice and no evaluation against other attack-access categories limit generality.

**Limits:** Selected related-edition review only. One main defense-test model, two tasks, and five data-poisoning methods; no weight-editing or CoT-defense evaluation. Perplexity alone cannot establish preserved safety, task utility or generic quality. Root/fresh QA additionally found that Table7’s jailbreak no-defense vector matches the Table3 sentiment-misclassification vector rather than its jailbreaking vector. Checkpoint/split/run provenance is uninspected; no copied-row error or corrected baseline is inferred.

**Replication:** `not_performed`. **Numerical check:** Documentary same-row comparison: all shown jailbreak-defense ASRs are below their no-defense comparators in Table7, while §5/D.2 prose claims some defenses increase them. This mismatch is unresolved; no escalation number or inference is adopted. No model replication.

**Relevance:** `claim_evidence`. **Claim links:** [C91](claims.md#c91)

**Relevance rationale:** Supplies conditional persistence, transfer, mitigation or endpoint evidence; constructed experiments do not establish natural incidence or the failure of every training method.

**Next check:** Use the qualitative task contrast with exact version and comparators. Hold the source prose claim about defense-induced escalation pending corrected results/author clarification; do not delay unrelated synthesis work.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2408.12798v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2408.12798v2) |
| `retrieved_at` | 2026-11-15T00:08:10.845760+00:00 |
| `attempted_at` | 2026-11-15T00:08:10.448392+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact primary-version URLs and locally retained bytes are preserved. Independent archival preservation is not claimed. |
| `sha256` | 2de3cd4dea6a5c90ad0dda0d0ad85a90756a9ec523c4b4a6d8b5fb6d34fe9b15 |
| `byte_length` | 1227042 |
| `mime_type` | application/pdf |
| `published_on` | 2025-05-19 |
| `version_claim` | arXiv v2 |
| `locator_basis` | PDF viewer pages count the cover as page 1; printed page numbers coincide unless stated. |
| `capture_path` | .source-captures/synthesis-2de3cd4dea6a5c90ad0dda0d0ad85a90756a9ec523c4b4a6d8b5fb6d34fe9b15.pdf |

<a id="r5_mitigations_01"></a>
### r5_mitigations_01

**Source:** `dai_saferlhfsafe_2024`. **Theme:** positive_mitigations. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Official ICLR 2024 proceedings paper has the same title and seven other coauthors as the canonical arXiv work, but first-author byline is Juntao Dai rather than canonical Josef Dai. This authenticates the conference edition and byline discrepancy, not a blanket preprint/final equivalence or an author-alias identity.

**Inspected scope:** Official 28-page ICLR final: main §§1–6, pp1–9; Appendix A limitations and B cost-model ablation p15; Appendix C reproducibility and D ethics plus E.1 opening p16; selected G.1 ending and complete G.2 model-selection plus G.3 opening pp21–22. Other appendix material, references, annotation protocol, proof and full implementation/red-team sections not comprehensively read.

**Locators:** §§3.1–3.3 separate preference/reward/cost modeling; §4, Eqs7–10 and expectation relaxation; §§5.1–5.2.3, Figures5–6, pp7–9; Appendix A–D pp15–16; G.2 p22

**Visual check:** Rendered Figure5 and adjacent §5.2 text on viewer p8 inspected: separate helpfulness/harmlessness Elo panels and human-labeled harmful/harmless fractions. Other plots were read through extracted captions/text, not visually audited.

**Findings:**

- Separate helpfulness and harmlessness preference labels train separate reward and cost models; Lagrangian training improves helpfulness and harmlessness on the paper's curated human/GPT-4 comparisons relative to Alpaca-7B and its tested RLHF comparators.
- The practical optimization constrains expected learned cost with a threshold/offset, rather than proving every generated response harmless.
- Ablations compare one-dimensional preference RLHF, dynamic constraint weighting and cost-classification choices; three training rounds also introduce new annotation/red-team data, so round-to-round gains are not a clean effect of one unchanged intervention.

**Counterevidence / alternative:** Authors explicitly limit results to single-turn interaction and note training/data constraints. Human judgments add evidence beyond learned scorers, but curated tests and checkpoint selection do not establish deployed harm reduction. HC-RLHF builds on this method/data lineage and is not independent corroboration.

**Limits:** Canonical preprint bytes were retrieved but not substantively reread. Official final access is resolved; claim-critical final/preprint numerical equivalence remains open. Single-turn Alpaca/Llama-1-family 7B setting, learned costs, curated prompt/evaluation mix and selected checkpoint procedure limit extrapolation. No linked code/data or annotation implementation audit.

**Replication:** `not_performed`. **Numerical check:** Documentary comparison of Eq7 with Eqs8–9 verifies a pointwise desired constraint is relaxed to an expectation. Figure5 denominator/annotation appendix not fully checked, so no harmfulness percentage or Elo increase adopted as a publication headline.

**Relevance:** `claim_evidence`. **Claim links:** [C92](claims.md#c92)

**Relevance rationale:** Affirmative mitigation evidence with its actual access assumptions, measured endpoints and counterevidence; source inclusion is not independent corroboration.

**Next check:** Preserve selected/related-edition status. Compare exact canonical preprint and ICLR equations/results/appendices before adopting a final-only number or correcting canonical byline metadata.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf) |
| `final_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf) |
| `retrieved_at` | 2026-11-15T00:03:34.615300+00:00 |
| `attempted_at` | 2026-11-15T00:03:33.965167+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact-version primary URLs and private local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | 3add2406f57d53606e7a0e48a5e29cf905a40b1f5ecd2b23fb18a3e0fbfba887 |
| `byte_length` | 1074019 |
| `mime_type` | application/pdf |
| `published_on` | 2024 |
| `version_claim` | ICLR 2024 official proceedings PDF |
| `locator_basis` | PDF viewer pages count the cover; these PDFs use the same printed numbering for substantive pages, except the HC-RLHF cover has no printed numeral. Section/table/appendix identifiers are the primary locators. |
| `capture_path` | .source-captures/synthesis-3add2406f57d53606e7a0e48a5e29cf905a40b1f5ecd2b23fb18a3e0fbfba887.pdf |

<a id="r5_mitigations_02"></a>
### r5_mitigations_02

**Source:** `chittepu_reinforcementlearning_2025`. **Theme:** positive_mitigations. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical arXiv eprint 2506.08266/DOI and six authors match this v1. Its actual title is Reinforcement Learning from Human Feedback with High-Confidence Safety Constraints; canonical metadata says Safety Guarantees (HC-RLHF). Identity is based on the exact identifier/authors, not title equivalence. No equivalence to the RLJ/RLC edition is asserted.

**Inspected scope:** All accessible text of all20 PDF pages of arXiv v1: main §§1–7, references and Appendices A–F, all tables/captions and proofs. Mathematical arguments were read as source text, not independently formally verified. Linked code/data and alternative published edition were not read or run.

**Locators:** §3.1 confidence bounds and safety test; §3.2 training and Algorithm1; §4 Assumption4.1 and Theorem4.2; distribution-shift discussion; §5.1–5.3, Figures1–3 and Tables1–2; Appendix A REINFORCE/RLOO, B bounded/Hoeffding alternative, C reward/overoptimization, D implementation/judge, E–F additional results

**Visual check:** Rendered pp8–9 inspected for Figures2–3 and Table1, including expected-cost axes and conditioned helpfulness comparison; rendered p11 Table3 inspected. Other figures/captions/tables were read in extracted text. No plot digitization. Rendered pp4 and7 also inspected to verify Algorithm1, Eq8 and the exact threshold/unbiasedness notation in §4 proof.

**Findings:**

- HC-RLHF separates candidate selection from a held-out safety test and can return No Solution Found rather than return a candidate whose upper confidence bound exceeds the cost threshold.
- The stated theorem targets the probability over the training/testing procedure of returning a policy exceeding an expected learned-cost threshold, conditional on statistical assumptions. At the zero threshold the written sampling/test forms agree; arbitrary-threshold implementation requires resolving the centering notation. Neither form bounds every response or actual real-world harm.
- The paper reports favorable learned-cost/helpfulness and judge comparisons for Qwen2-1.5B, Qwen2.5-3B and Llama3.2-3B; measured utility is retained or improved in several tested conditions.
- Student-t validity uses iid normally distributed estimates (or an explicitly approximate large-sample rationale); the alternative Hoeffding route requires bounded estimates. Training/deployment prompt distributions are assumed stationary.

**Counterevidence / alternative:** A misspecified cost model can certify the wrong construct. Evolving/adaptive prompts can invalidate distribution assumptions. The NSF convention sets g(NSF)=0; reverting operationally to an uncertified base model does not inherit a safety guarantee. Shared SafeRLHF/BeaverTails lineage means these are related experiments, not independent confirmations.

**Limits:** A complete text read is not a verified proof, independent human review, code audit or experimental replication. Learned cost/reward validity and stationary prompt distribution are essential. Main §5.1 says GPT-4 judge while Appendix D names gpt-4o-mini; run-level judge identity remains unresolved. Table3 caption has an ordering ambiguity for lose/tie/win tuples; affected percentages are omitted. Eq8 defines g=E[C]−τ, while Algorithm1 lines4–5 and the §4 proof define ghat_i=C and test its upper bound against0; the omitted threshold centering is harmless at τ=0 but requires clarification for nonzero thresholds. No run configuration was inspected to resolve it.

**Replication:** `not_performed`. **Numerical check:** Checked the target g as expected learned cost minus threshold and the iid/normal Student-t assumptions; Appendix B supplies a bounded-cost Hoeffding alternative. Thirty bootstrap trials with no observed failures are not a true failure probability of zero. No headline judge win percentage adopted; no independent theorem or training reproduction. Documentary/visual comparison identifies Eq8 versus Algorithm1 lines4–5/§4 proof threshold-centering mismatch for nonzero τ; zero-threshold forms coincide. No claim of experimental failure is made.

**Relevance:** `claim_evidence`. **Claim links:** [C93](claims.md#c93)

**Relevance rationale:** Affirmative mitigation evidence with its actual access assumptions, measured endpoints and counterevidence; source inclusion is not independent corroboration.

**Next check:** Keep conditional expected-cost wording and omit unresolved judge percentages. Reconcile canonical title and source run manifest/judge ID; assess scorer validity and prompt shift before suggesting a deployment guarantee. No need to block all other synthesis on this numerical question. Resolve Eq8/Algorithm1/§4 centering for nonzero thresholds in code/author clarification before asserting the general-threshold guarantee.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2506.08266v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2506.08266v1) |
| `retrieved_at` | 2026-11-15T00:03:14.993531+00:00 |
| `attempted_at` | 2026-11-15T00:03:12.839395+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact-version primary URLs and private local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | 487b4ca42b88a42af49fe829e5399de7cee96c8141a7284dc2084a32196c0665 |
| `byte_length` | 16282113 |
| `mime_type` | application/pdf |
| `published_on` | 2025-06-09 |
| `version_claim` | arXiv:2506.08266v1 |
| `locator_basis` | PDF viewer pages count the cover; these PDFs use the same printed numbering for substantive pages, except the HC-RLHF cover has no printed numeral. Section/table/appendix identifiers are the primary locators. |
| `capture_path` | .source-captures/synthesis-487b4ca42b88a42af49fe829e5399de7cee96c8141a7284dc2084a32196c0665.pdf |

<a id="r5_mitigations_03"></a>
### r5_mitigations_03

**Source:** `hsu_safelorasilver_2024`. **Theme:** positive_mitigations. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Canonical title, six authors, arXiv eprint2405.16833 and DOI match the 15-page v1. Official NeurIPS final was separately retrieved, but not substantively read or treated as equivalent; no final-edition coverage upgrade is claimed.

**Inspected scope:** All accessible text of the 15-page arXiv v1, including main §§1–5, references, Appendix A.1–A.4 and all captions/Tables1–6. Equations and threat assumptions read; no linked code, datasets or final-edition appendices inspected.

**Locators:** §3 layerwise aligned-minus-base weight projection; §4.1–4.3 experimental setup; Tables1–3; Appendix A.1–A.4, Tables4–6; Figures3–4 on p9; §5 Conclusion/limitations

**Visual check:** Rendered p9 Figures3–4 and Table5 inspected, confirming harmfulness/utility tradeoffs as projected-layer count changes. Other table/figure content read through extracted text/captions, without full visual verification.

**Findings:**

- Layerwise projection of LoRA updates onto directions derived from aligned-minus-base weights mitigates harmful-response degradation in tested harmful, mixed and benign fine-tuning settings without another safety-training stage for the projection itself.
- Experiments report GPT-4 harmfulness, keyword-refusal ASR and MT-Bench/ROUGE utility separately; several safety gains retain useful task performance, but retention is not uniform.
- Projected-layer count and threshold expose an explicit safety/utility tradeoff; the best threshold depends on model and fine-tuning dataset. Baseline SafeInstr/BEA dose choices are limited and do not establish universal method superiority.

**Counterevidence / alternative:** Authors explicitly identify adaptive attacks on the transparent method as a limitation. Some Llama3 harmful fine-tuning conditions lose utility relative to the original aligned model; increasing projected layers can reduce summary performance. Geometric projection does not uniquely identify a validated safety subspace or guarantee general robustness.

**Limits:** Requires access to a suitable base/aligned weight pair and control over LoRA adaptation; not resistance to an unconstrained modifier who bypasses the projection. Tests two model families at7B/8B, specific LoRA targets/rank/data and automatic judges. No adaptive attack evaluation or experimental replication. Official final is longer and remains a separate reading task.

**Replication:** `not_performed`. **Numerical check:** Compared utility/harmfulness endpoints and comparator training-data conditions; keyword-based nonrefusal ASR is not identical to harmful-content correctness or authorization failure. No cross-paper pooled rate or cost-free utility claim. No new arithmetic result.

**Relevance:** `claim_evidence`. **Claim links:** [C94](claims.md#c94)

**Relevance rationale:** Affirmative mitigation evidence with its actual access assumptions, measured endpoints and counterevidence; source inclusion is not independent corroboration.

**Next check:** Retain positive weight-access mitigation under its controlled pipeline assumptions. Read the separate NeurIPS final before importing final-only settings or results; compare diverse utility and adaptive attacker tests before deployment conclusions. Consider source_form metadata correction from policy_paper to paper separately.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2405.16833v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2405.16833v1) |
| `retrieved_at` | 2026-11-15T00:03:13.034868+00:00 |
| `attempted_at` | 2026-11-15T00:03:12.838596+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact-version primary URLs and private local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | 8969702639c6891672374e0e82aafc485db66ccbae5f0f90ac6621e33d2ed04f |
| `byte_length` | 624595 |
| `mime_type` | application/pdf |
| `published_on` | 2024-05-27 |
| `version_claim` | arXiv:2405.16833v1 |
| `locator_basis` | PDF viewer pages count the cover; these PDFs use the same printed numbering for substantive pages, except the HC-RLHF cover has no printed numeral. Section/table/appendix identifiers are the primary locators. |
| `capture_path` | .source-captures/synthesis-8969702639c6891672374e0e82aafc485db66ccbae5f0f90ac6621e33d2ed04f.pdf |

<a id="r5_mitigations_04"></a>
### r5_mitigations_04

**Source:** `yu_robustsafeguarding_2024`. **Theme:** positive_mitigations. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Title, four authors and canonical arXiv eprint2409.20089/DOI match the captured v1. Cover affiliations include Meta FAIR/Meta, Toronto and UCL; this is a technical training/intervention paper, not policy analysis.

**Inspected scope:** Cover/abstract p1; complete §§3–8 pp3–10, including mechanistic geometry/restoration, perturbation comparison, training, setup, results and limitations; Appendix A and B with Tables4–5 p14. References and full PCA/histogram Appendices C–D not comprehensively read. Main introduction/related work only abstract/heading context, not complete.

**Locators:** §3.1–3.3, Eqs2–5 and Figures2–4; §4.1–4.2, Eq8 and Figure5; §§5–7, Table1 p9 and failure discussion p10; Appendix A–B, Tables4–5 p14

**Visual check:** Rendered p9 Table1 and p14 Tables4–5 inspected. This confirms distinct ASR/utility/pass-count columns and Appendix A ranks128/128/64. Mechanistic plots read through text/captions only; no plot digitization or full appendix panel audit.

**Findings:**

- Refusal-feature restoration after successful attacks substantially reduces judged ASR, with separate MMLU/MT-Bench checks to assess whether the effect is simple generation collapse. This is intervention evidence under the specified activation manipulation, stronger than correlation alone.
- ReFAT trains under refusal-direction ablation while mixing benign utility and overrefusal examples. On three models and HarmBench/AdvBench tests it improves multiple attack endpoints versus original models/refusal training and several adversarial-training comparators, while retaining much general benchmark performance.
- Appendix A specifies a Mixtral PAIR attacker in place of GPT-4 and a Prometheus MT-Bench judge; three separate safety classifiers are averaged for ASR. These details constrain comparison with other reports.
- The paper itself documents remaining non-English/vernacular failures and notes that broader linguistic/semantic refusal-feature data may be needed.

**Counterevidence / alternative:** The authors' universal/worst-case language exceeds the tested successful-case geometry and random-direction comparison. Positive mechanism/manipulation findings can coexist with other attack pathways. Table1 includes residual attacks and utility drops, a missing Gemma R2D2 run due to instability, and several cells where another defense performs better.

**Limits:** Analysis conditions on successful attacks and model refusal cases; four attack families/three instruction-tuned architectures do not establish a universal mechanism. Default-budget attacks are rerun against trained models, but no unrestricted bespoke adaptive search is established. Main §5 says LoRA rank64 for all models whereas Appendix A Table4 says128 for Llama/Mistral and64 for Gemma. Exact training runs remain unresolved.

**Replication:** `not_performed`. **Numerical check:** Documentary check of Table1 shows favorable but nonuniform robustness/utility rankings, not a best score on every metric. Efficiency is reported as forward/backward-pass counts, not audited wall time or deployment cost. Eq8 compares the refusal direction to99 random unit perturbations; this is not a proof of globally worst-case perturbation. No experimental replication.

**Relevance:** `claim_evidence`. **Claim links:** [C34](claims.md#c34)

**Relevance rationale:** Affirmative mitigation evidence with its actual access assumptions, measured endpoints and counterevidence; source inclusion is not independent corroboration.

**Next check:** Retain a bounded affirmative result in C34; omit universal-mechanism, global-optimum and wall-clock speedup claims. Reconcile main/appendix LoRA ranks with run configurations before a reproduction recipe. Later source-form correction should classify a technical paper without changing citation key.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2409.20089v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2409.20089v1) |
| `retrieved_at` | 2026-11-15T00:03:13.434824+00:00 |
| `attempted_at` | 2026-11-15T00:03:12.839039+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact-version primary URLs and private local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | f4cf44b26807012086ab14a176d13876c55385eed7394f3eef3bf4a706787767 |
| `byte_length` | 4142687 |
| `mime_type` | application/pdf |
| `published_on` | 2024-09-30 |
| `version_claim` | arXiv:2409.20089v1 |
| `locator_basis` | PDF viewer pages count the cover; these PDFs use the same printed numbering for substantive pages, except the HC-RLHF cover has no printed numeral. Section/table/appendix identifiers are the primary locators. |
| `capture_path` | .source-captures/synthesis-f4cf44b26807012086ab14a176d13876c55385eed7394f3eef3bf4a706787767.pdf |

<a id="r5_mitigations_05"></a>
### r5_mitigations_05

**Source:** `guan_deliberativealignment_2024`. **Theme:** positive_mitigations. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Canonical title, author group, arXiv eprint2412.16339/DOI match the captured v1; cover identifies OpenAI. A cover author spelling differs from canonical Helyar (cover Heylar), so automatic metadata rewriting is not proposed. No later paper/model edition is substituted.

**Inspected scope:** Cover/abstract/introduction opening p1; §2 overview/specification/data-generation/filtering/SFT/RL pp3–9; §3.1.3 jailbreak evaluation p10; §§3.2–4.3 comparisons/compute/ablations/policy retrieval/OOD pp12–18; complete §6 discussion pp20–21; Appendix A human-review experiment and Table4 p24. Remaining examples, policies, related work and references not comprehensively read.

**Locators:** §§2.1–2.4 specification, synthetic-CoT SFT and RL; §3.1.3 jailbreaks; §§3.2–3.3 comparators/compute; §§4.1–4.3 ablations, policy retrieval and OOD generalization; §6 discussion; Appendix A/Table4 human review

**Visual check:** No rendered visual verification. Selected figure captions/nearby result text and Appendix A Table4 were read as extracted text; no plot digitization or independent recalculation.

**Findings:**

- Explicit policy-reasoning synthetic-CoT SFT followed by outcome RL improves several tested policy-adherence/jailbreak endpoints; matched reduced-model ablations provide affirmative evidence for both SFT and RL contributions.
- The paper reports overall jailbreak/overrefusal frontier improvements, but the reduced ablation itself increases overrefusal. Safety gains are therefore not universally free of benign-task costs.
- Transfer to non-English/encoded held-out safety prompts is positive evidence for limited safety-training generalization, not proof of robust transfer to arbitrary languages, architectures, future models or adversaries.
- Policy-text retrieval in chain of thought is an observed association/ablation result, not a proof of faithful reasoning or an enforceable policy guarantee.

**Counterevidence / alternative:** Inference-only comparisons supply summarized policies, whereas training uses detailed category-specific policies; information/resources are not perfectly matched. Jailbreak evaluation covers specified attacks and budgets. Internal human review strengthens a behavioral endpoint but remains within the provider's study, not independent external validation.

**Limits:** Provider-authored report with internal models/data/scorers; no public training reproduction. Comparators differ in training/inference information and resources. Selected passages do not certify all paper figures or policy boundary examples. This is alignment to OpenAI's chosen policy, not evidence that the policy resolves governance legitimacy questions.

**Replication:** `not_performed`. **Numerical check:** Checked that safety-training OOD excludes particular training categories, not all pretraining/capability exposure to languages/encodings. Checked the reduced o1-mini ablation reports increased overrefusal despite robustness benefit. No exact headline cross-model rate is adopted. Appendix A uses explicit human scoring and counts API blocks at the safest grade for Gemini; no independent rescoring.

**Relevance:** `claim_evidence`. **Claim links:** [C95](claims.md#c95)

**Relevance rationale:** Affirmative mitigation evidence with its actual access assumptions, measured endpoints and counterevidence; source inclusion is not independent corroboration.

**Next check:** Keep affirmative behavior improvements with comparator/OOD/overrefusal scope. If leading a publication with policy-reasoning efficacy, inspect exact release/model IDs, full evaluation/judge code and attack budgets first; source issuer classification should reflect OpenAI affiliation rather than default academic issuer.

| Capture field | Value |
|---|---|
| `preservation_status` | captured |
| `original_url` | [Source](https://arxiv.org/pdf/2412.16339v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2412.16339v1) |
| `retrieved_at` | 2026-11-15T00:03:13.045082+00:00 |
| `attempted_at` | 2026-11-15T00:03:12.838198+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No capture-specific independent archive was checked in this bounded round; exact-version primary URLs and private local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | ce80073ea89c3d3ec419fb01c692f3a818fa28ae7709da951820497242f606f7 |
| `byte_length` | 2439332 |
| `mime_type` | application/pdf |
| `published_on` | 2024-12-20 |
| `version_claim` | arXiv:2412.16339v1 |
| `locator_basis` | PDF viewer pages count the cover; these PDFs use the same printed numbering for substantive pages, except the HC-RLHF cover has no printed numeral. Section/table/appendix identifiers are the primary locators. |
| `capture_path` | .source-captures/synthesis-ce80073ea89c3d3ec419fb01c692f3a818fa28ae7709da951820497242f606f7.pdf |

<a id="r5_privacy_01"></a>
### r5_privacy_01

**Source:** `nasr_scalableextraction_2025`. **Theme:** privacy_verification. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. The canonical record combines the final 2025 title/year with the 2023 arXiv URL and earlier author list. The official final replaces Eric Wallace with Javier Rando and adds material. This is the authenticated final publication, not a claim that the 2023 preprint is textually equivalent.

**Inspected scope:** Complete main-text viewer pp1–10, abstract and §§1–8 through the beginning of the discussion on p10; Tables 1–2 and captions for Figures 1–5. Discussion continuation, references and appendices on pp11–73 were not fully read. No example strings or sensitive output passages are reproduced.

**Locators:** ICLR 2025 final pp1–3, §§1–3: experimental dates, model/ground-truth definitions; pp4–8, §§4–6: model comparisons, divergence and fine-tuning results; Tables 1–2; pp9–10, §§7–8: output categorization and discussion opening

**Visual check:** Tables and captions were read as extracted text. No plot digitization or independent full visual figure audit is claimed.

**Findings:**

- Historical aligned and instruction-model configurations differ in easy extraction, while changed prompting or permitted fine-tuning can recover additional exact web-matching outputs. This bounds output safeguards rather than proving deletion of memorized information.
- The authors operationalize memorization as exact matches of at least 50 tokens in an auxiliary corpus because proprietary training membership is unavailable. Tokens, unique 50-grams and matching generations have different denominators.
- The fine-tuning analysis excludes text present in the provided fine-tuning data from its web-matching count; that control reduces the explanation that output merely repeats the supplied fine-tuning corpus.

**Counterevidence / alternative:** The specific divergence behavior was patched; tested transfer differs across models, and fine-tuning does not uniformly restore an unaligned baseline. Unknown differences in weights/training data prevent isolating alignment as the sole causal factor. Regex/contact and toxicity classifications are not independently verified person-level harm.

**Limits:** Only 10 of 73 PDF pages were completely read. The final-edition identity is authenticated but canonical bibliographic reconciliation is pending. Unknown proprietary training data are proxied by exact matches in a 9 TB auxiliary web corpus; late-2023/early-2024 experiments and patched interfaces do not measure current product exposure.

**Replication:** `not_performed`. **Numerical check:** Documentary checking of reported methods, denominators and selected table entries only; no arithmetic reconstruction of raw data, source-code reproduction or model experiments.

**Relevance:** `claim_evidence`. **Claim links:** [C96](claims.md#c96)

**Relevance rationale:** Source-bounded evidence for C96.

**Next check:** Root should reconcile canonical final metadata against the captured official proceedings page. Use historically and operationally bounded qualitative findings; read relevant appendices before adopting a numerical headline. No current-model tests or data extraction are needed.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf) |
| `final_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf) |
| `retrieved_at` | 2026-11-15T00:05:16.733271+00:00 |
| `attempted_at` | 2026-11-15T00:05:16.368439+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independently checked capture-specific archive was available in this bounded round; exact primary URLs and hashed local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | 78c08f52958948a22ae023e629b7f1ada01e4c4fff798ebf057a276764e88bb8 |
| `byte_length` | 1079848 |
| `mime_type` | application/pdf |
| `published_on` | 2025 |
| `version_claim` | ICLR 2025 final proceedings PDF |
| `locator_basis` | PDF viewer pages count the cover; printed pages follow document pagination. |
| `capture_path` | .source-captures/synthesis-78c08f52958948a22ae023e629b7f1ada01e4c4fff798ebf057a276764e88bb8.pdf |

<a id="r5_privacy_02"></a>
### r5_privacy_02

**Source:** `nasr_scalableextraction_2025`. **Theme:** privacy_verification. **Reading:** Metadata only. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. This is the arXiv record actually linked by the canonical bibliography, whose title and author list differ from the official 2025 final.

**Inspected scope:** Primary arXiv title, byline, version/date and submission history; not a full paper reading or empirical result check.

**Locators:** arXiv abstract page: title/byline and Submission history

**Visual check:** None; metadata only.

**Findings:**

- The linked arXiv v1 is titled Scalable Extraction of Training Data from (Production) Language Models and lists Eric Wallace but not Javier Rando. It was submitted November 28, 2023.

**Counterevidence / alternative:** The authenticated 2025 proceedings is a related but materially expanded publication; the canonical final-title/old-byline combination is not a reliable single-edition citation.

**Limits:** The abstract and retrieved old PDF are not used to certify final-publication evidence. The record lists only the 2023 v1; no equivalence with the 2025 final is presumed.

**Replication:** `not_performed`. **Numerical check:** Documentary checking of reported methods, denominators and selected table entries only; no arithmetic reconstruction of raw data, source-code reproduction or model experiments.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Historical bibliographic and provenance role only; this event is not positive evidence for an empirical synthesis claim.

**Next check:** Reconcile metadata to a chosen authoritative edition without changing the citation key; preserve the earlier version as provenance rather than silently treating it as the final.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/abs/2311.17035) |
| `final_url` | [Source](https://arxiv.org/abs/2311.17035) |
| `retrieved_at` | 2026-11-15T00:03:33.804987+00:00 |
| `attempted_at` | 2026-11-15T00:03:33.591268+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independently checked capture-specific archive was available in this bounded round; exact primary URLs and hashed local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | a540399898bcf8f47c0735a12102c577e6f597b0cd2f88933f8acece56d3e71b |
| `byte_length` | 41518 |
| `mime_type` | text/html |
| `published_on` | 2023-11-28 |
| `version_claim` | arXiv 2311.17035 v1, sole version listed |
| `locator_basis` | Captured primary HTML headings, source history and bibliographic fields. |
| `capture_path` | .source-captures/synthesis-a540399898bcf8f47c0735a12102c577e6f597b0cd2f88933f8acece56d3e71b.html |

<a id="r5_privacy_03"></a>
### r5_privacy_03

**Source:** `nasr_scalableextraction_2025`. **Theme:** privacy_verification. **Reading:** Metadata only. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Official final-publication landing page confirms the 2025 title/byline and links the captured final PDF; the canonical arXiv-linked record requires reconciliation.

**Inspected scope:** Complete accessible paper-page title, byline, conference/year, abstract and publication links. Site scripts/navigation and footer were inspected only for page identity, not research evidence.

**Locators:** Official ICLR proceedings page: title/byline, Conference and Paper link

**Visual check:** None; bibliographic page.

**Findings:**

- The final title explicitly includes Aligned, Production Language Models. Official byline includes Javier Rando and excludes Eric Wallace; the proceedings identifies ICLR 2025.

**Counterevidence / alternative:** A shared work family does not make the earlier arXiv experimental scope or authors identical.

**Limits:** This page authenticates publication identity; its abstract is not treated as a substitute for main methods or appendices.

**Replication:** `not_performed`. **Numerical check:** Documentary checking of reported methods, denominators and selected table entries only; no arithmetic reconstruction of raw data, source-code reproduction or model experiments.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Historical bibliographic and provenance role only; this event is not positive evidence for an empirical synthesis claim.

**Next check:** Root should choose final-edition URL/byline/year consistently and retain earlier-version provenance. No automatic full-text coverage upgrade.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2025/hash/cce0e917b050208170151f77b497fc71-Abstract-Conference.html) |
| `final_url` | [Source](https://proceedings.iclr.cc/paper_files/paper/2025/hash/cce0e917b050208170151f77b497fc71-Abstract-Conference.html) |
| `retrieved_at` | 2026-11-15T00:05:16.367904+00:00 |
| `attempted_at` | 2026-11-15T00:05:15.959941+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independently checked capture-specific archive was available in this bounded round; exact primary URLs and hashed local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | 00b09c30de4b32f47cf0f3976ba050279d22a8e0a33f5b56320cf8148e86cfd4 |
| `byte_length` | 9361 |
| `mime_type` | text/html |
| `published_on` | 2025 |
| `version_claim` | ICLR 2025 official proceedings paper page |
| `locator_basis` | Captured primary HTML headings, source history and bibliographic fields. |
| `capture_path` | .source-captures/synthesis-00b09c30de4b32f47cf0f3976ba050279d22a8e0a33f5b56320cf8148e86cfd4.html |

<a id="r5_privacy_04"></a>
### r5_privacy_04

**Source:** `du_textualunlearning_2025`. **Theme:** privacy_verification. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. The canonical PMLR landing page links this publisher-hosted final PDF and matches title, six authors, conference/year and printed proceedings page range.

**Inspected scope:** All 19 PDF pages read: main §§1–6, all figure captions and table text, acknowledgments/impact statement, references, and Appendices A–J. Key Table 1 and Figure 4 on viewer p8 were also visually inspected. Linked code/data and other cited papers were not read as part of this event.

**Locators:** Main §§2–3, viewer pp2–4: threat model, counterfactual audit and U-LiRA+; §§4–5, viewer pp4–9: black-/white-box access conditions, datasets and results; Tables 1–2 and Figures 3–5; Appendices A–J, viewer pp12–19: experimental configurations, shadow-model audit details, reconstruction and fictional-data construction

**Visual check:** Viewer p8 was rendered and visually checked: Table 1 and Figure 4. Other figures and tables were read through their extracted text/captions; no coordinate digitization or raw-data reconstruction.

**Findings:**

- A stronger counterfactual audit on deliberately mislabeled synthetic classification examples detects residual distinguishability for tested inexact methods while the exact-retraining control largely removes the audited single-state signal.
- Access to both before- and after-unlearning models creates a different privacy question: deletion membership can remain inferable even when exact retraining succeeds at the single-state erasure audit.
- The paper explicitly separates strict black-box output-score access, relaxed black-box access with logits/auxiliary same-distribution data/shadow models, and white-box reconstruction with model weights and known unlearning procedure.
- The reconstruction study defaults to one deleted example in a 1,000-example training subset; reported accuracy uses ROUGE overlap and is not a rate of exact real-person profile recovery. Larger deletion batches reduce recovery in the reported setup with model-dependent variation.

**Counterevidence / alternative:** Exact retraining is a positive erasure comparator, rather than evidence that every deletion mechanism fails. The worst-case mislabeled task, fictional examples and strong access assumptions limit population-level privacy interpretation; batched deletion and architecture affect reconstruction.

**Limits:** The reported HTTP content-type was application/octet-stream, but retained bytes begin with the PDF signature and parse as a 19-page PDF; capture MIME is detected application/pdf. Experiments use synthetic personal-profile classification, not an unrestricted generative deployment. Low-FPR audit calibration, shadow-model assumptions and before/after access constrain transfer. Reading every page does not recertify experiments or linked artifacts.

**Replication:** `not_performed`. **Numerical check:** Documentary checking of reported methods, denominators and selected table entries only; no arithmetic reconstruction of raw data, source-code reproduction or model experiments.

**Relevance:** `claim_evidence`. **Claim links:** [C97](claims.md#c97)

**Relevance rationale:** Source-bounded evidence for C97.

**Next check:** Use qualitative separation of erasure auditing and update-history privacy. Retain synthetic/task/access qualifiers and omit the abstract reconstruction percentage from the broad synthesis. Code/data reproduction, realistic generative settings and independently calibrated low-FPR estimates remain future checks if publication needs these numbers.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25d/du25d.pdf) |
| `final_url` | [Source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25d/du25d.pdf) |
| `retrieved_at` | 2026-11-15T00:03:34.138211+00:00 |
| `attempted_at` | 2026-11-15T00:03:33.592695+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independently checked capture-specific archive was available in this bounded round; exact primary URLs and hashed local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | ffb7c3fb08132ddb74254b3b5a4021a2cdb9390f6b1a366773ebb51554bfeaec |
| `byte_length` | 1908035 |
| `mime_type` | application/pdf |
| `published_on` | 2025 |
| `version_claim` | ICML 2025 PMLR 267 final PDF, pp14579–14597 |
| `locator_basis` | PDF viewer pages count the cover; printed pages follow document pagination. |
| `capture_path` | .source-captures/synthesis-ffb7c3fb08132ddb74254b3b5a4021a2cdb9390f6b1a366773ebb51554bfeaec.pdf |

<a id="r5_privacy_05"></a>
### r5_privacy_05

**Source:** `wang_pandoraswhite_2024`. **Theme:** privacy_verification. **Reading:** Metadata only. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Official arXiv identifier/title/authors match the canonical work. At the start of this round its record still said preprint; the current source identifies withdrawn v4. The canonical withdrawal/historical annotation has now been applied. This event is a withdrawal/metadata check, not a reading of the archived experimental paper.

**Inspected scope:** Primary title/byline, withdrawal banner, Comments field and complete submission history through v4. The archived paper and its experiments were intentionally not reread or adopted as current evidence.

**Locators:** arXiv 2402.17012: withdrawal banner and Comments; Submission history: v4 July 15, 2024, 02:37:09 UTC, withdrawn; prior versions February 26, May 28 and June 24, 2024

**Visual check:** None; metadata notice only.

**Findings:**

- The primary record states that Seth Neel withdrew the paper. The stated reason is a software bug in experiments, with withdrawal to address and update results.
- The current listed version is v4, dated July 15, 2024; no subsequent corrected version is listed in the captured primary history.

**Counterevidence / alternative:** Withdrawal does not establish that every conceptual idea is false, but it removes a sufficient basis for admitting the old empirical results as positive synthesis evidence. Abstract-only inherited reading is not validation of withdrawn results.

**Limits:** The notice identifies a software bug and withdrawal to address/update results, but does not identify which specific result survives or quantify the bug. No newer revision is listed on this captured page. Older positive abstract text remains visible and cannot establish reliable current support.

**Replication:** `not_performed`. **Numerical check:** Documentary checking of reported methods, denominators and selected table entries only; no arithmetic reconstruction of raw data, source-code reproduction or model experiments.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Historical bibliographic and provenance role only; this event is not positive evidence for an empirical synthesis claim.

**Next check:** Retain the applied withdrawn/historical annotation and removal of the unreliable archived numerical abstract from current canonical exports. Reconsider empirical use only if corrected primary results or independent verification become available; preserve the earlier record in Git history.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/abs/2402.17012) |
| `final_url` | [Source](https://arxiv.org/abs/2402.17012) |
| `retrieved_at` | 2026-11-15T00:03:33.676041+00:00 |
| `attempted_at` | 2026-11-15T00:03:33.591931+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independently checked capture-specific archive was available in this bounded round; exact primary URLs and hashed local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | d8a2d67a47b6ae66b8db365029a4e6e5eeeb5773f4be7aedf2251768c44aaddb |
| `byte_length` | 42745 |
| `mime_type` | text/html |
| `published_on` | 2024-07-15 |
| `version_claim` | arXiv 2402.17012 v4 withdrawal, July 15 2024 |
| `locator_basis` | Captured primary HTML headings, source history and bibliographic fields. |
| `capture_path` | .source-captures/synthesis-d8a2d67a47b6ae66b8db365029a4e6e5eeeb5773f4be7aedf2251768c44aaddb.html |

<a id="r5_privacy_06"></a>
### r5_privacy_06

**Source:** `zhang_vtuneverifiablefine_2024`. **Theme:** privacy_verification. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Version-pinned v2 matches the canonical title/byline/arXiv identifier; arXiv history lists November 12, 2024 for v2, after v1 on November 10.

**Inspected scope:** Version/title and introduction/threat/desiderata on pp1–3; §§4–4.3 pp4–7 including test and modal-probability estimator; §5 experimental setup and §5.1 downstream performance pp7–8; §§5.3–5.4 and selected §6.1 subset-training assumptions p10; §7 conclusion/limitations p12. No complete reading of §5.2 sweeps, remaining attacks, references or appendices.

**Locators:** v2 §2.1: verification desiderata and malicious-provider setting; §§4.2–4.3, especially §4.2.1 p7: binomial test and empirical modal-probability estimate; §§5.1,5.3–5.4: performance/API and activation comparisons; §7 p12: verification granularity limitations

**Visual check:** No independent full visual figure audit. Read selected table/caption text and exact statistical-assumption prose.

**Findings:**

- vTune provides an affirmative statistical verification approach for whether supplied marked data influenced a fine-tuned model, with measured downstream-performance and benign-response comparisons in tested open and API models.
- Section 4.2.1 estimates modal signature probability by the largest probability among 1,600 samples per dataset and leaves an exact upper bound to future work. Hence the displayed tiny p-values are conditional on an empirically estimated null parameter, not a universally certified false-positive rate.
- Section 7 explicitly says the method cannot verify the requested model, number of iterations or fine-tuning method; a failure to pass is not conclusive proof that fine-tuning never occurred.

**Counterevidence / alternative:** Positive verification can be useful under its threat model; tested attack and performance results support feasibility without proving exhaustive provider honesty. Learning a marked subset or different training procedure need not satisfy the entire requested job. This method does not certify privacy, erasure or safety.

**Limits:** This is a conditional marker-based customization test, not universal certification of requested training. The modal-probability upper bound is estimated from sampled candidates; an exact bound is expressly future work. Adversaries, marker secrecy, model/data configurations and subset training constrain interpretation. Operational marker/payload instructions are not reproduced.

**Replication:** `not_performed`. **Numerical check:** Documentary checking of reported methods, denominators and selected table entries only; no arithmetic reconstruction of raw data, source-code reproduction or model experiments.

**Relevance:** `claim_evidence`. **Claim links:** [C98](claims.md#c98)

**Relevance rationale:** Source-bounded evidence for C98.

**Next check:** Use scoped positive process-verification finding with the empirical-null and granularity caveats. Complete adversarial sections and statistical bound analysis before claiming calibrated significance or comprehensive training compliance.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2411.06611v2) |
| `final_url` | [Source](https://arxiv.org/pdf/2411.06611v2) |
| `retrieved_at` | 2026-11-15T00:04:36.219914+00:00 |
| `attempted_at` | 2026-11-15T00:04:35.672197+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independently checked capture-specific archive was available in this bounded round; exact primary URLs and hashed local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | 8feb97fa735043c0ff24e294b8ddf6343657003d40b4b9febeb15b4d9ea97768 |
| `byte_length` | 3083118 |
| `mime_type` | application/pdf |
| `published_on` | 2024-11-12 |
| `version_claim` | arXiv 2411.06611 v2 |
| `locator_basis` | PDF viewer pages count the cover; printed pages follow document pagination. |
| `capture_path` | .source-captures/synthesis-8feb97fa735043c0ff24e294b8ddf6343657003d40b4b9febeb15b4d9ea97768.pdf |

<a id="r5_privacy_07"></a>
### r5_privacy_07

**Source:** `barbero_extractingalignment_2025`. **Theme:** privacy_verification. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Version-pinned v1 matches canonical title, authors and arXiv identifier. A later v2 exists (October 23) but was not read or asserted textually equivalent. The PDF header dates its manuscript October 22 while arXiv v1 submission is October 21.

**Inspected scope:** Abstract and selected introduction/nomenclature; §2 pp3–4; selected §3 method definitions including all §3.3 metric text pp4–6; §4 setup and §§4.2–4.3 coverage/distillation pp6–9; §5 RL evaluation pp10–11 and §6 conclusion p12. No full reading of §3.1 prompt procedures, §4.1 verbatim-results analysis, references or appendices. Qualitative generations are not reproduced.

**Locators:** v1 §§2,3.3 pp3–6: post-training-data terminology, exact and semantic constructs; §4.2 pp8–9: semantic matching and selected threshold; §4.3 Table 2 p9: distillation utility; §5 pp10–11: RL setting and training comparisons; §6 p12: limitations and mechanism discussion

**Visual check:** Selected table cells and captions read as extracted text; no independent full plot audit or embedding-threshold validation.

**Findings:**

- The paper calls broad instruction-following, reasoning and capability post-training mixtures alignment data; it does not test only safety-policy data. It distinguishes exact verbatim memorization from semantic-equivalence similarity.
- Its semantic metric uses Gemini embeddings with a manually chosen similarity threshold of 0.95. An apparent gain over exact matching is not interchangeable with exact privacy leakage or independently validated training membership.
- Extracted/filtered synthetic data can support useful re-training in matched open-model experiments. Table 2 shows varied benchmark results, including lower MATH and IFEval than the original SFT model, rather than uniform performance parity.
- The SFT distillation comparison has similar example counts but different token totals (about 850 million versus 1.3 billion) and uses additional filtering. The RL study is a separate known-public-data/model configuration, not a general proprietary-data incidence estimate.

**Counterevidence / alternative:** Positive re-training utility is evidence that outputs contain useful post-training-like information, while the threshold, known public data and benchmark variation leave exact membership, complete dataset recovery and safety-policy recovery unestablished. The mechanism for RL-associated memorization remains open in the paper.

**Limits:** Known public training mixtures in open models provide ground truth, whereas proprietary/real-user data are not tested. Embedding similarity uses a manually selected threshold; semantic resemblance is not exact training-record membership. Only v1 is reviewed and appendices remain unread.

**Replication:** `not_performed`. **Numerical check:** Documentary checking of reported methods, denominators and selected table entries only; no arithmetic reconstruction of raw data, source-code reproduction or model experiments.

**Relevance:** `claim_evidence`. **Claim links:** [C99](claims.md#c99)

**Relevance rationale:** Source-bounded evidence for C99.

**Next check:** Cross-check v2 before publication-leading numbers, and inspect threshold calibration and distillation appendices if semantic-recovery or utility magnitudes lead the thesis. Preserve a distinct semantic-resemblance construct and avoid proprietary-data or current-population extrapolation.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://arxiv.org/pdf/2510.18554v1) |
| `final_url` | [Source](https://arxiv.org/pdf/2510.18554v1) |
| `retrieved_at` | 2026-11-15T00:03:34.648171+00:00 |
| `attempted_at` | 2026-11-15T00:03:33.678140+00:00 |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No independently checked capture-specific archive was available in this bounded round; exact primary URLs and hashed local bytes are retained. Independent archival preservation is not claimed. |
| `sha256` | ba6cb424c6b75c8e811da71f9a1dc7a21ff818110e5664e62a6150681058815c |
| `byte_length` | 2335201 |
| `mime_type` | application/pdf |
| `published_on` | 2025-10-21 |
| `version_claim` | arXiv 2510.18554 v1; document header October 22, 2025 |
| `locator_basis` | PDF viewer pages count the cover; printed pages follow document pagination. |
| `capture_path` | .source-captures/synthesis-ba6cb424c6b75c8e811da71f9a1dc7a21ff818110e5664e62a6150681058815c.pdf |

<a id="r5_versions_01"></a>
### r5_versions_01

**Source:** `nist_managingmisuserisk_2024`. **Theme:** versions_instruments. **Reading:** Full text. **Coverage effect:** `complete_record_text`.

**Edition match:** `same_record`. Exact canonical identifier/title and issuer match; later revisions and separate editions are not silently equated.

**Inspected scope:** All27 PDF pages read: covers, comment notice/TOC, introduction, §§2–4, all seven objectives/practices/documentation, AppendixA glossary, AppendixB/Table1 and all50 endnotes. Linked studies/guidance not independently opened.

**Locators:** July2024 cover and draft notice; §3 printedpp2–3; §4 printedpp4–17; AppendixB/Table1 printedp19; Practices1.3,2.1–2.2,4.1–4.2,5.1–5.3,6.1–6.5,7.1–7.3

**Visual check:** Read all extracted text and rendered/visually checked Table1 on viewerp24/printedp19. No linked external studies or empirical artifacts reproduced.

**Findings:**

- The original draft provides a concrete threat-profile→risk-tolerance→measurement→safeguard/deployment→monitoring/documentation workflow, including reference tasks, evaluator-resource gaps and feedback from incidents.
- It permits alternative practices with comparable documentation, calls risk management iterative and says implementation cannot guarantee that actors will not misuse a model.
- Proxy-model comparability, proxy-task transfer and adequacy of red-team resources require justification; anticipated risk can call for more measurement or changed deployment/development rather than confidence from a document alone.

**Counterevidence / alternative:** Explicit tests, response owners and documentation are constructive mechanisms, while threat-emulation limits and context-dependent alternatives prevent treating compliance with this draft as demonstrated harm reduction.

**Limits:** Historical July2024 initial public draft, not binding statutory duties, a current-status census, evaluated control effectiveness or all AI harms. Its cited EO context is not recertified as current law. Complete draft reading does not inspect every linked primary study.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C100](claims.md#c100)

**Relevance rationale:** Adds scoped instrument/version or quantitative provenance evidence; source inclusion, repeated representations and separate-agent checking do not establish independent outcome corroboration.

**Next check:** Use exact edition-specific practices; seek actual evaluation/decision/remediation records for implementation-effect claims.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-1.ipd.pdf) |
| `final_url` | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-1.ipd.pdf) |
| `retrieved_at` | 2026-11-15T00:03:44.258635+00:00 |
| `attempted_at` | 2026-11-15T00:03:43.182986+00:00 |
| `sha256` | 30ced091493af421d454ca138a3496a39b8c6079f74223e868325318ffa767e4 |
| `byte_length` | 557173 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked independent capture-specific archive established in this bounded round; exact live response bytes and actual retrieval metadata retained locally. |
| `published_on` | 2024-07 |
| `version_claim` | NIST AI800-1 ipd, Initial Public Draft, July2024 |
| `locator_basis` | One-based PDF viewer pages include front matter; printed page/section/table references stated separately. Web/repository descriptions identify the exact inspected headings or immutable commit. |
| `capture_path` | .source-captures/synthesis-30ced091493af421d454ca138a3496a39b8c6079f74223e868325318ffa767e4.pdf |

<a id="r5_versions_02"></a>
### r5_versions_02

**Source:** `nist_managingmisuserisk_2025_2pd`. **Theme:** versions_instruments. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact canonical identifier/title and issuer match; later revisions and separate editions are not silently equated.

**Inspected scope:** PDF frontmatter/intro/viewerpp1–5; complete §§2–4 and §5 through Practice6.1 opening, printedpp1–17/viewerpp6–22; complete AppendixC/Table2 printedpp26–30/viewerpp31–35. Remaining monitoring/disclosure practices, glossary, mitigation table, domain appendices and endnotes not fully read.

**Locators:** January2025 cover/second-comment notice; DOI10.6028/NIST.AI.800-1.2pd; §2 scope; §3 supply chain; §5 Practices1.1–1.3,2.1–2.2,4.1–4.2,5.1–5.3; AppendixC/Table2 printedpp26–30

**Visual check:** No separate visual inspection; extracted prose only.

**Findings:**

- The second draft expressly frames voluntary marginal-risk guidance and expands supply-chain roles and measurement-task characteristics, with separate environments, grading, model/human involvement, inference targets and relationships to misuse scenarios.
- Uncertain capability forecasts that may require increased mitigation call for considering more frequent measurement and expanded mitigations (Practice1.1.7).
- Documentation is evidence to expose how practices were implemented and why they are adequate, not a tested result that harms were prevented. The draft explicitly cannot guarantee prevention.

**Counterevidence / alternative:** The expanded taxonomy and implementation considerations make proposed comparisons more operational; their usefulness remains contingent on valid tasks, resources, risk baselines and actual follow-through.

**Limits:** Selected69-page January2025 draft only, not full domain-appendix reading, a finalized standard or comprehensive check for subsequent policy versions. Its cover supplies DOI.2pd despite filename.ipd2. No empirical efficacy estimate.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C100](claims.md#c100)

**Relevance rationale:** Adds scoped instrument/version or quantitative provenance evidence; source inclusion, repeated representations and separate-agent checking do not establish independent outcome corroboration.

**Next check:** Keep draft editions and their numbering distinct; verify later instruments only for a present-duty/current-policy claim. Test actual decisions if claiming efficacy.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-1.ipd2.pdf) |
| `final_url` | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-1.ipd2.pdf) |
| `retrieved_at` | 2026-11-15T00:03:44.422027+00:00 |
| `attempted_at` | 2026-11-15T00:03:43.183622+00:00 |
| `sha256` | 362c24f9cfc1e3ba4e0756a49654eaacf3837e963fbd6ff20fe5fcefe06d3b82 |
| `byte_length` | 1106925 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked independent capture-specific archive established in this bounded round; exact live response bytes and actual retrieval metadata retained locally. |
| `published_on` | 2025-01 |
| `version_claim` | NIST AI800-1 2pd, Second Public Draft, January2025 |
| `locator_basis` | One-based PDF viewer pages include front matter; printed page/section/table references stated separately. Web/repository descriptions identify the exact inspected headings or immutable commit. |
| `capture_path` | .source-captures/synthesis-362c24f9cfc1e3ba4e0756a49654eaacf3837e963fbd6ff20fe5fcefe06d3b82.pdf |

<a id="r5_versions_03"></a>
### r5_versions_03

**Source:** `amironesei_aria_pilot_2025`. **Theme:** versions_instruments. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Exact canonical identifier/title and issuer match; later revisions and separate editions are not silently equated.

**Inspected scope:** Selected §3.1 dialogue assessment/adjudication and §5.1 source-code statement/§5.2 opening; AppendixC Tables5–7. PDF bytes independently re-fetched and identical to earlier r2 capture; not a full38-page reread.

**Locators:** §3.1 printedpp5–6/viewerpp12–13; §5.1 source-code paragraph and §5.2 opening printedp10/viewerp17; AppendixC Tables5–7 printedp22/viewerp29

**Visual check:** Rendered and visually checked viewerp29/printedp22 Tables5–7, confirming category labels and49/218 counts; other plots not independently inspected.

**Findings:**

- Current PDF still reports52 identified violations among267 annotated dialogues in adjudication prose; Table7 reports49Yes+218No=267 calibrated decisions. The text does not supply a stage/row mapping that reconciles the difference.
- Table5 counts964 risk-assessment annotations; Table6 is non-calibrated question2.1 counts, not independent-dialogue prevalence. Table7 is explicitly calibrated. This stage distinction narrows the query without proving the count difference is an error.
- The implemented layered evaluation and characterization interpretation remain usable while affected violation rates are omitted.

**Counterevidence / alternative:** Calibration stage or denominator differences could explain the prose/table divergence; numerical equality of totals alone does not resolve which stage generated each headline.

**Limits:** The calibrated/non-calibrated/adjudication relationship lacks a row-level manifest. No corrected rate or source-error cause is established. Report and current code artifacts are one project; no human-independent review or experimental reproduction.

**Replication:** `not_performed`. **Numerical check:** Documentary arithmetic:49+218=267;185+445+111+223=964. No inference about independent dialogues from annotation totals, no experiment rerun.

**Relevance:** `claim_evidence`. **Claim links:** [C45](claims.md#c45)

**Relevance rationale:** Adds scoped instrument/version or quantitative provenance evidence; source inclusion, repeated representations and separate-agent checking do not establish independent outcome corroboration.

**Next check:** Obtain the267-dialogue membership, per-annotator/adjudication-stage labels and exact aggregation manifest or authenticated correction; keep numerical hold until then.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-2.pdf) |
| `final_url` | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-2.pdf) |
| `retrieved_at` | 2026-11-15T00:03:45.162804+00:00 |
| `attempted_at` | 2026-11-15T00:03:43.184048+00:00 |
| `sha256` | 5478e8c37a182adaf9449d1d315689beba3db2808db430c54fe3fc8da04ea3b9 |
| `byte_length` | 8040325 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked independent capture-specific archive established in this bounded round; exact live response bytes and actual retrieval metadata retained locally. |
| `published_on` | 2025-11 |
| `version_claim` | NIST AI700-2, November2025; bytes match prior retained PDF |
| `locator_basis` | One-based PDF viewer pages include front matter; printed page/section/table references stated separately. Web/repository descriptions identify the exact inspected headings or immutable commit. |
| `capture_path` | .source-captures/synthesis-5478e8c37a182adaf9449d1d315689beba3db2808db430c54fe3fc8da04ea3b9.pdf |

<a id="r5_versions_04"></a>
### r5_versions_04

**Source:** `amironesei_aria_pilot_2025`. **Theme:** versions_instruments. **Reading:** Full text. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Ancillary official code artifact linked back to ARIA, not the same paper edition.

**Inspected scope:** Complete2077-byte README of official usnistgov/corix at immutable commit430d76d1a96f8945cb2682889d149bdaf97b0420; no package installation, source execution or complete-code audit.

**Locators:** README purpose/basic install/testing/example/visualization/related material/citation

**Visual check:** No separate visual inspection; extracted prose only.

**Findings:**

- NIST now makes an early-development CoRIx computation/visualization code artifact publicly inspectable. This closes generic code-availability uncertainty, not the pilot count provenance question.
- The README presents examples and expected test outputs; those outputs were not reproduced here and do not validate application-risk or annotation counts.

**Counterevidence / alternative:** A concrete open computation artifact is affirmative reproducibility infrastructure. Availability alone does not establish instrument validity or trace a particular published numerator.

**Limits:** Ancillary code README is not the ARIA paper or original pilot data; related-object full reading cannot upgrade canonical-paper depth. No dependency, program or model executed.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C45](claims.md#c45)

**Relevance rationale:** Adds scoped instrument/version or quantitative provenance evidence; source inclusion, repeated representations and separate-agent checking do not establish independent outcome corroboration.

**Next check:** Use pinned source/data versions; obtain actual pilot inputs and stage/aggregation mapping for the unresolved counts.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://raw.githubusercontent.com/usnistgov/corix/430d76d1a96f8945cb2682889d149bdaf97b0420/README.md) |
| `final_url` | [Source](https://raw.githubusercontent.com/usnistgov/corix/430d76d1a96f8945cb2682889d149bdaf97b0420/README.md) |
| `retrieved_at` | 2026-11-15T00:07:49.681632+00:00 |
| `attempted_at` | 2026-11-15T00:07:49.351848+00:00 |
| `sha256` | 91d06a2de98754cfaaafceb46ef2a374939ba607e7fd745b48130609256324df |
| `byte_length` | 2077 |
| `mime_type` | text/plain |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked independent capture-specific archive established in this bounded round; exact live response bytes and actual retrieval metadata retained locally. |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Official usnistgov/corix README at430d76d1a96f8945cb2682889d149bdaf97b0420 |
| `locator_basis` | One-based PDF viewer pages include front matter; printed page/section/table references stated separately. Web/repository descriptions identify the exact inspected headings or immutable commit. |
| `capture_path` | .source-captures/synthesis-91d06a2de98754cfaaafceb46ef2a374939ba607e7fd745b48130609256324df.txt |

<a id="r5_versions_05"></a>
### r5_versions_05

**Source:** `amironesei_aria_pilot_2025`. **Theme:** versions_instruments. **Reading:** Metadata only. **Coverage effect:** `none`.

**Edition match:** `related_edition`. Metadata of an ancillary official repository, not a source-paper edition.

**Inspected scope:** Complete recursive Git-tree path/type listing at the pinned official commit; README context. File bodies, complete source code and data content not audited.

**Locators:** Git tree430d76d1a96f8945cb2682889d149bdaf97b0420; data/ and test/ path entries

**Visual check:** No separate visual inspection; extracted prose only.

**Findings:**

- The inspected non-truncated tree lists data/toy_annotations_1.json and data/toy_corix_structure_1.json plus tests; no identified pilot dialogue/adjudication manifest resolves the52/49 question. This is a bounded artifact-identification result, not proof that such data do not exist elsewhere.

**Counterevidence / alternative:** Toy/test artifacts may support implementation examples, while the actual pilot aggregation could be stored separately or undisclosed.

**Limits:** Path names and repository scope cannot establish full data contents or global absence. No raw dialogues or classifier/annotation outputs were read.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental reproduction.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Adds scoped instrument/version or quantitative provenance evidence; source inclusion, repeated representations and separate-agent checking do not establish independent outcome corroboration.

**Next check:** Find an authenticated row-level pilot manifest rather than treating generic toy computation as report-data reproduction.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://api.github.com/repos/usnistgov/corix/git/trees/430d76d1a96f8945cb2682889d149bdaf97b0420?recursive=1) |
| `final_url` | [Source](https://api.github.com/repos/usnistgov/corix/git/trees/430d76d1a96f8945cb2682889d149bdaf97b0420?recursive=1) |
| `retrieved_at` | 2026-11-15T00:07:49.351287+00:00 |
| `attempted_at` | 2026-11-15T00:07:48.849960+00:00 |
| `sha256` | 7b8a85fc8ef1c0d4b013208d8253e5907f26de0c9ca875b106e3d0233cf99600 |
| `byte_length` | 9569 |
| `mime_type` | application/json |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked independent capture-specific archive established in this bounded round; exact live response bytes and actual retrieval metadata retained locally. |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Recursive tree at430d76d1a96f8945cb2682889d149bdaf97b0420 |
| `locator_basis` | One-based PDF viewer pages include front matter; printed page/section/table references stated separately. Web/repository descriptions identify the exact inspected headings or immutable commit. |
| `capture_path` | .source-captures/synthesis-7b8a85fc8ef1c0d4b013208d8253e5907f26de0c9ca875b106e3d0233cf99600.json |

<a id="r5_versions_06"></a>
### r5_versions_06

**Source:** `california_sb53_tfaia_2025`. **Theme:** versions_instruments. **Reading:** Inaccessible. **Coverage effect:** `none`.

**Edition match:** `uncertain`. Exact enacted-text identity could not be inspected through these endpoints.

**Inspected scope:** Official bill navigation/text and observed chapter-PDF route all returned403; no official enacted-clause body read.

**Locators:** Requested SB53 official billTextClient endpoint and Chapter138 PDF route

**Visual check:** No separate visual inspection; extracted prose only.

**Findings:**

No source findings; material was inaccessible.

**Counterevidence / alternative:** A failed route does not imply the statute is absent or unpublished; an official signing record is separately accessible.

**Limits:** HTTP403 on all three official legislative routes. Earlier mirror reading and current-law labels are not recertified by this attempt.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental reproduction.

**Relevance:** `unresolved`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Adds scoped instrument/version or quantitative provenance evidence; source inclusion, repeated representations and separate-agent checking do not establish independent outcome corroboration.

**Next check:** Obtain authenticated chaptered or consolidated operative text before detailed deadlines/current-clause claims.

| Capture field | Value |
|---|---|
| `preservation_status` | unavailable |
| `original_url` | [Source](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53) |
| `final_url` | Not recorded / unavailable |
| `retrieved_at` | Not recorded / unavailable |
| `attempted_at` | 2026-11-15T00:03:43.185452+00:00 |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No authenticated exact enacted-text capture obtained in bounded attempts; no independent archive checked. |
| `sha256` | Not recorded / unavailable |
| `byte_length` | Not recorded / unavailable |
| `mime_type` | Not recorded / unavailable |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Not recorded / unavailable |
| `locator_basis` | Requested official chaptered bill text/PDF endpoints; no statutory text was available for inspection. |
| `capture_path` | Not recorded / unavailable |

<a id="r5_versions_07"></a>
### r5_versions_07

**Source:** `california_sb53_tfaia_2025`. **Theme:** versions_instruments. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Official enactment announcement related to the statute; not a replacement for chaptered bill or operative code.

**Inspected scope:** Governor official September29,2025 release: title/date, signing statement, summary of transparency/incident/whistleblower/update mechanisms and link to signing message. Unrelated economic claims, quotations and recent-news navigation not treated as evidence.

**Locators:** Official release datedSeptember29,2025; What the law does; signing-message link

**Visual check:** No separate visual inspection; extracted prose only.

**Findings:**

- The governor’s official release corroborates that SB53 was signed and describes framework disclosure, critical-incident reporting, whistleblower protection and enforcement mechanisms. This is official enactment/summary evidence, not authenticated verification of every statutory clause.

**Counterevidence / alternative:** A legally enacted mechanism is more than a voluntary provider commitment, but a signing announcement’s benefits claims are not measured policy effects.

**Limits:** Official executive summary, not binding statutory body or current consolidated code; exact15-day/24-hour duties remain inherited/unverified here. No observed enforcement, submitted incident counts or harm prevention audited.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental reproduction.

**Relevance:** `claim_evidence`. **Claim links:** [C17](claims.md#c17)

**Relevance rationale:** Adds scoped instrument/version or quantitative provenance evidence; source inclusion, repeated representations and separate-agent checking do not establish independent outcome corroboration.

**Next check:** Authenticate operative text and actual implementation evidence before specific compliance or effectiveness claims.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/) |
| `final_url` | [Source](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/) |
| `retrieved_at` | 2026-11-15T00:05:23.585096+00:00 |
| `attempted_at` | 2026-11-15T00:05:23.363226+00:00 |
| `sha256` | c71a1f8aab9c0cc628a4e2e4410516a0c75afffcae632876e09ac26852675bd6 |
| `byte_length` | 295285 |
| `mime_type` | text/html |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked independent capture-specific archive established in this bounded round; exact live response bytes and actual retrieval metadata retained locally. |
| `published_on` | 2025-09-29 |
| `version_claim` | Governor official signing release datedSeptember29,2025 |
| `locator_basis` | One-based PDF viewer pages include front matter; printed page/section/table references stated separately. Web/repository descriptions identify the exact inspected headings or immutable commit. |
| `capture_path` | .source-captures/synthesis-c71a1f8aab9c0cc628a4e2e4410516a0c75afffcae632876e09ac26852675bd6.html |

<a id="r5_versions_08"></a>
### r5_versions_08

**Source:** `california_sb53_tfaia_2025`. **Theme:** versions_instruments. **Reading:** Full text. **Coverage effect:** `scoped_review`.

**Edition match:** `related_edition`. Official scanned signing message is a related companion instrument, not the same statute edition.

**Inspected scope:** All text on both scanned signing-message pages read visually, including signature and dated cover. PDF text extraction was empty; rendered pages are reading basis.

**Locators:** Signing message datedSeptember29,2025, pp1–2

**Visual check:** Both PDF pages rendered and visually read in full, including date, body, continuation and signature. No OCR or visual comparison with enacted bill.

**Findings:**

- The signed message corroborates the enactment action and describes prospective state oversight and a critical-incident reporting compliance pathway. Its expected public-safety benefits are the issuer’s policy rationale, not evaluated effects.

**Counterevidence / alternative:** Executive purpose and signed approval establish a documentary action; they cannot stand in for statutory wording or measured implementation outcomes.

**Limits:** Companion signing message is not complete enacted SB53. No exact reporting-deadline or current-operative-clause confirmation and no new complete canonical-statute recheck.

**Replication:** `not_performed`. **Numerical check:** No numerical recomputation or experimental reproduction.

**Relevance:** `background`. **Claim links:** None; no claim support forced.

**Relevance rationale:** Adds scoped instrument/version or quantitative provenance evidence; source inclusion, repeated representations and separate-agent checking do not establish independent outcome corroboration.

**Next check:** Keep the enacted-clause access gap explicit and distinguish authorizing a pathway from observing its operation.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.gov.ca.gov/wp-content/uploads/2025/09/SB-53-Signing-Message.pdf) |
| `final_url` | [Source](https://www.gov.ca.gov/wp-content/uploads/2025/09/SB-53-Signing-Message.pdf) |
| `retrieved_at` | 2026-11-15T00:05:23.362414+00:00 |
| `attempted_at` | 2026-11-15T00:05:22.999921+00:00 |
| `sha256` | e3a8cd758bc5be06704ef480b8544538ec0187c808fc91304264e66959dd71bb |
| `byte_length` | 90354 |
| `mime_type` | application/pdf |
| `preservation_status` | captured |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | No checked independent capture-specific archive established in this bounded round; exact live response bytes and actual retrieval metadata retained locally. |
| `published_on` | 2025-09-29 |
| `version_claim` | Two-page Governor signing message datedSeptember29,2025 |
| `locator_basis` | One-based PDF viewer pages include front matter; printed page/section/table references stated separately. Web/repository descriptions identify the exact inspected headings or immutable commit. |
| `capture_path` | .source-captures/synthesis-e3a8cd758bc5be06704ef480b8544538ec0187c808fc91304264e66959dd71bb.pdf |
## targeted-downstream-intake-2026-11-20

**As of:** 2026-11-20. **Base commit:** `3ca0700c2d43f2a4fe8e14b162d211e53450b483`.

**Question:** What do these sources establish about downstream AI toy tests, legislative consideration, enacted restrictions and observed misuse?

**Selection basis:** Targeted owner-requested intake following a news lead and citation tracing; not a systematic sample.

**Stopping rule:** Confirm bibliographic identity and inspect decision-relevant passages; retain edition details and unresolved byte or causal gaps.

| Theme | Why selected | Canonical keys |
|---|---|---|
| Downstream AI toys, legislative consideration and observed misuse | Separate empirical observations and documented actions from unsupported attributions or outcomes. | `murray_troubleintoyland_2025`, `calassembly_sb867analysis_2026`, `california_sb867_companiontoys_2026`, `murray_troubleintoyland_2026`, `cross_notforkids_2026`, `goodacre_aiearlyyears_2026`, `collier_pixiepaw_2026`, `blum_gtigagenticthreshold_2026` |

### Event index

| Event | Source | Reading | Edition / coverage effect | Relevance |
|---|---|---|---|---|
| [intake_murray_troubleintoyland_2025](#intake_murray_troubleintoyland_2025) | `murray_troubleintoyland_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [intake_calassembly_sb867analysis_2026](#intake_calassembly_sb867analysis_2026) | `calassembly_sb867analysis_2026` | Selected sections | same_record / scoped_review | claim_evidence |
| [intake_california_sb867_companiontoys_2026](#intake_california_sb867_companiontoys_2026) | `california_sb867_companiontoys_2026` | Selected sections | same_record / scoped_review | claim_evidence |
| [intake_murray_troubleintoyland_2026](#intake_murray_troubleintoyland_2026) | `murray_troubleintoyland_2026` | Selected sections | same_record / scoped_review | claim_evidence |
| [intake_cross_notforkids_2026](#intake_cross_notforkids_2026) | `cross_notforkids_2026` | Selected sections | same_record / scoped_review | claim_evidence |
| [intake_goodacre_aiearlyyears_2026](#intake_goodacre_aiearlyyears_2026) | `goodacre_aiearlyyears_2026` | Selected sections | same_record / scoped_review | claim_evidence |
| [intake_collier_pixiepaw_2026](#intake_collier_pixiepaw_2026) | `collier_pixiepaw_2026` | Selected sections | same_record / scoped_review | claim_evidence |

<a id="intake_murray_troubleintoyland_2025"></a>
### intake_murray_troubleintoyland_2025

**Source:** `murray_troubleintoyland_2025`. **Theme:** targeted_admissions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Same issued report or article edition as the canonical source record; cited distribution representation identified separately.

**Inspected scope:** Chapter on AI toys, printed pp. 12–17; AI methodology, printed p. 61.

**Locators:** Chapter on AI toys, printed pp. 12–17; AI methodology, printed p. 61.

**Visual check:** Scoped text and source/edition metadata reviewed; no complete visual audit.

**Findings:**

- Adult researchers selected four AI toys and fully tested three; the configured Kumma produced unsuitable responses under elicitation.

**Counterevidence / alternative:** The source scope does not establish claims beyond the reported observation or documentary act.

**Limits:** Product configurations and elicitation conditions do not isolate the base model or establish child exposure, injury, or prevalence. The California legislative analysis cites this report, not the 2026 retest.

**Replication:** `not_performed`. **Numerical check:** Qualifying source counts checked in stated material, not independently recomputed.

**Relevance:** `claim_evidence`. **Claim links:** [C101](claims.md#c101)

**Relevance rationale:** Mapped on November 20 within the same scoped inspection; no additional reading, causal inference or replication is claimed.

**Next check:** Check independent corroboration before extending the source to prevalence, effectiveness or causation.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.nypirg.org/pubs/202511/TOYLAND_REPORT_2025.pdf) |
| `attempted_at` | 2026-11-20T14:36:19.208196+00:00 |
| `retrieved_at` | 2026-11-20T14:36:23.341918+00:00 |
| `final_url` | [Source](https://www.nypirg.org/pubs/202511/TOYLAND_REPORT_2025.pdf) |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Exact response retained locally; no independent capture-specific archive was established in this bounded intake. |
| `sha256` | 038a329aee251ff8613924ad5ad72564156634c0c6d3a64fb424bdff9bb5351b |
| `byte_length` | 4903113 |
| `mime_type` | application/pdf |
| `published_on` | 2025-11-13 |
| `version_claim` | Publisher or identified report edition reviewed in this intake. |
| `locator_basis` | Printed pages where specified; statutory sections or article content for HTML. |
| `capture_path` | .source-captures/synthesis-038a329aee251ff8613924ad5ad72564156634c0c6d3a64fb424bdff9bb5351b.pdf |
| `preservation_status` | captured |

<a id="intake_calassembly_sb867analysis_2026"></a>
### intake_calassembly_sb867analysis_2026

**Source:** `calassembly_sb867analysis_2026`. **Theme:** targeted_admissions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Same issued report or article edition as the canonical source record; cited distribution representation identified separately.

**Inspected scope:** June 16 hearing analysis, printed pp. 7–9, notes 13–14 and 16–17.

**Locators:** June 16 hearing analysis, printed pp. 7–9, notes 13–14 and 16–17.

**Visual check:** Scoped text and source/edition metadata reviewed; no complete visual audit.

**Findings:**

- Assembly policy staff directly cited the 2025 PIRG product tests and discussed Kumma.

**Counterevidence / alternative:** The source scope does not establish claims beyond the reported observation or documentary act.

**Limits:** This dated analysis concerns the May 14 bill version. It documents legislative consideration, not causal influence on passage, final statutory scope, implementation, or outcomes.

**Replication:** `not_performed`. **Numerical check:** Qualifying source counts checked in stated material, not independently recomputed.

**Relevance:** `claim_evidence`. **Claim links:** [C101](claims.md#c101)

**Relevance rationale:** Mapped on November 20 within the same scoped inspection; no additional reading, causal inference or replication is claimed.

**Next check:** Check independent corroboration before extending the source to prevalence, effectiveness or causation.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://apcp.assembly.ca.gov/media/1168) |
| `attempted_at` | 2026-11-20T14:36:19.207878+00:00 |
| `retrieved_at` | 2026-11-20T14:36:22.557210+00:00 |
| `final_url` | [Source](https://apcp.assembly.ca.gov/system/files/2026-06/sb-867-padilla-apcp-analysis.pdf) |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Exact response retained locally; no independent capture-specific archive was established in this bounded intake. |
| `sha256` | ad42f89e4a0dec75d2b490b4e64e74e7244534781e5923720a51c20d3426cef0 |
| `byte_length` | 280158 |
| `mime_type` | application/pdf |
| `published_on` | 2026-06-16 |
| `version_claim` | Publisher or identified report edition reviewed in this intake. |
| `locator_basis` | Printed pages where specified; statutory sections or article content for HTML. |
| `capture_path` | .source-captures/synthesis-ad42f89e4a0dec75d2b490b4e64e74e7244534781e5923720a51c20d3426cef0.pdf |
| `preservation_status` | captured |

<a id="intake_california_sb867_companiontoys_2026"></a>
### intake_california_sb867_companiontoys_2026

**Source:** `california_sb867_companiontoys_2026`. **Theme:** targeted_admissions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Same issued report or article edition as the canonical source record; cited distribution representation identified separately.

**Inspected scope:** Chaptered September 10, Chapter 189; Business and Professions Code §§ 22601(b), 22601(g), 22604.5(a)–(b).

**Locators:** Chaptered September 10, Chapter 189; Business and Professions Code §§ 22601(b), 22601(g), 22604.5(a)–(b).

**Visual check:** Scoped text and source/edition metadata reviewed; no complete visual audit.

**Findings:**

- The enacted text restricts specified commercial activity involving physical toys for play by children under 16 that contain a defined companion chatbot, with a January 1, 2031 sunset. The prohibition is enacted but not yet operative as of review.

**Counterevidence / alternative:** The source scope does not establish claims beyond the reported observation or documentary act.

**Limits:** Chaptered text checked via version-specific mirror, not the earlier bill analyzed by Assembly staff. PIRG published the 2026 retest report after enactment. No enforcement, compliance, safety benefit, or attribution to a particular study is shown.

**Replication:** `not_performed`. **Numerical check:** Qualifying source counts checked in stated material, not independently recomputed.

**Relevance:** `claim_evidence`. **Claim links:** [C101](claims.md#c101)

**Relevance rationale:** Mapped on November 20 within the same scoped inspection; no additional reading, causal inference or replication is claimed.

**Next check:** Check independent corroboration before extending the source to prevalence, effectiveness or causation.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://legiscan.com/CA/text/SB867/id/3458543) |
| `attempted_at` | 2026-11-20T14:36:19.209825+00:00 |
| `retrieved_at` | 2026-11-20T14:36:22.569608+00:00 |
| `final_url` | [Source](https://legiscan.com/CA/text/SB867/id/3458543) |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Exact response retained locally; no independent capture-specific archive was established in this bounded intake. |
| `sha256` | c82eb8b019c52b67c5d62a15c2f338125732929f5755dd8ec99c902b419905cc |
| `byte_length` | 29345 |
| `mime_type` | text/html |
| `published_on` | 2026-09-10 |
| `version_claim` | Publisher or identified report edition reviewed in this intake. |
| `locator_basis` | Printed pages where specified; statutory sections or article content for HTML. |
| `capture_path` | .source-captures/synthesis-c82eb8b019c52b67c5d62a15c2f338125732929f5755dd8ec99c902b419905cc.html |
| `preservation_status` | captured |

<a id="intake_murray_troubleintoyland_2026"></a>
### intake_murray_troubleintoyland_2026

**Source:** `murray_troubleintoyland_2026`. **Theme:** targeted_admissions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Same issued report or article edition as the canonical source record; cited distribution representation identified separately.

**Inspected scope:** AI toy chapter, printed pp. 17–24, including retests and testing scope.

**Locators:** AI toy chapter, printed pp. 17–24, including retests and testing scope.

**Visual check:** Scoped text and source/edition metadata reviewed; no complete visual audit.

**Findings:**

- PIRG reports testing seven AI toys (four repeats and three new). In its repeated tests, Kumma responded with stronger guardrails; the Alilo bunny still produced inappropriate material.

**Counterevidence / alternative:** The source scope does not establish claims beyond the reported observation or documentary act.

**Limits:** One publisher report and one exact PDF edition reviewed for scoped AI-toy sections only. Samples are not representative; observed changes do not identify a model or safeguard cause or establish realized child harm. The retest report was published after SB 867 enactment.

**Replication:** `not_performed`. **Numerical check:** Qualifying source counts checked in stated material, not independently recomputed.

**Relevance:** `claim_evidence`. **Claim links:** [C102](claims.md#c102)

**Relevance rationale:** Mapped on November 20 within the same scoped inspection; no additional reading, causal inference or replication is claimed.

**Next check:** Check independent corroboration before extending the source to prevalence, effectiveness or causation.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://publicinterestnetwork.org/wp-content/uploads/2026/11/TOYLAND-11-17-26-1.pdf) |
| `attempted_at` | 2026-11-20T14:36:19.208648+00:00 |
| `retrieved_at` | 2026-11-20T14:36:22.535839+00:00 |
| `final_url` | [Source](https://publicinterestnetwork.org/wp-content/uploads/2026/11/TOYLAND-11-17-26-1.pdf) |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Exact response retained locally; no independent capture-specific archive was established in this bounded intake. |
| `sha256` | c6c5f3c1337d3e225e3a3403a164b0a59c92aa3cd935f6cb6427a4941c16bd85 |
| `byte_length` | 13779375 |
| `mime_type` | application/pdf |
| `published_on` | 2026-11-17 |
| `version_claim` | Publisher or identified report edition reviewed in this intake. |
| `locator_basis` | Printed pages where specified; statutory sections or article content for HTML. |
| `capture_path` | .source-captures/synthesis-c6c5f3c1337d3e225e3a3403a164b0a59c92aa3cd935f6cb6427a4941c16bd85.pdf |
| `preservation_status` | captured |

<a id="intake_cross_notforkids_2026"></a>
### intake_cross_notforkids_2026

**Source:** `cross_notforkids_2026`. **Theme:** targeted_admissions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Same issued report or article edition as the canonical source record; cited distribution representation identified separately.

**Inspected scope:** Executive summary and printed pp. 13–15 on developer signup.

**Locators:** Executive summary and printed pp. 13–15 on developer signup.

**Visual check:** Scoped text and source/edition metadata reviewed; no complete visual audit.

**Findings:**

- PIRG reports a February 2026 pass through five providers’ developer onboarding paths; only Anthropic asked whether the intended product was for minors in that pass.

**Counterevidence / alternative:** The source scope does not establish claims beyond the reported observation or documentary act.

**Limits:** Governance implementation evidence from observed signup screens, not a provider policy artifact or a technical/model benchmark. It does not measure later enforcement, ongoing provider practice, actual toy routing, or child outcomes.

**Replication:** `not_performed`. **Numerical check:** Qualifying source counts checked in stated material, not independently recomputed.

**Relevance:** `claim_evidence`. **Claim links:** [C103](claims.md#c103)

**Relevance rationale:** Mapped on November 20 within the same scoped inspection; no additional reading, causal inference or replication is claimed.

**Next check:** Check independent corroboration before extending the source to prevalence, effectiveness or causation.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://publicinterestnetwork.org/wp-content/uploads/2026/03/PIRG-NOT-FOR-KIDS-FOUND-IN-TOYS-March-2026.pdf) |
| `attempted_at` | 2026-11-20T14:36:19.209057+00:00 |
| `retrieved_at` | 2026-11-20T14:36:22.287269+00:00 |
| `final_url` | [Source](https://publicinterestnetwork.org/wp-content/uploads/2026/03/PIRG-NOT-FOR-KIDS-FOUND-IN-TOYS-March-2026.pdf) |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Exact response retained locally; no independent capture-specific archive was established in this bounded intake. |
| `sha256` | 8f1bd7004c7a53590b31bc9721f7a3fb505ba3444a3294847c1b202c5547e6bc |
| `byte_length` | 1686349 |
| `mime_type` | application/pdf |
| `published_on` | 2026-03 |
| `version_claim` | Publisher or identified report edition reviewed in this intake. |
| `locator_basis` | Printed pages where specified; statutory sections or article content for HTML. |
| `capture_path` | .source-captures/synthesis-8f1bd7004c7a53590b31bc9721f7a3fb505ba3444a3294847c1b202c5547e6bc.pdf |
| `preservation_status` | captured |

<a id="intake_goodacre_aiearlyyears_2026"></a>
### intake_goodacre_aiearlyyears_2026

**Source:** `goodacre_aiearlyyears_2026`. **Theme:** targeted_admissions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Same issued report or article edition as the canonical source record; cited distribution representation identified separately.

**Inspected scope:** Children’s Views and Observed Play, printed pp. 13–19, including study design and composite vignettes.

**Locators:** Children’s Views and Observed Play, printed pp. 13–19, including study design and composite vignettes.

**Visual check:** Scoped text and source/edition metadata reviewed; no complete visual audit.

**Findings:**

- Researchers observed 14 children aged 3–5 using one Curio Gabbo at four London children’s centres. The report describes both engagement and difficulties with turn-taking, speaker recognition and pretend play.

**Counterevidence / alternative:** The source scope does not establish claims beyond the reported observation or documentary act.

**Limits:** Small qualitative project in observed sessions, not a long-term developmental study, comparative product prevalence estimate, or an isolated base-model test. Clinical and population outcomes were not assessed by this study component.

**Replication:** `not_performed`. **Numerical check:** Qualifying source counts checked in stated material, not independently recomputed.

**Relevance:** `claim_evidence`. **Claim links:** [C102](claims.md#c102)

**Relevance rationale:** Mapped on November 20 within the same scoped inspection; no additional reading, causal inference or replication is claimed.

**Next check:** Check independent corroboration before extending the source to prevalence, effectiveness or causation.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.pedalhub.net/wp-content/uploads/2026/03/AI-in-the-Early-Years-Project-report-27-February-2026.pdf) |
| `attempted_at` | 2026-11-20T14:36:19.209558+00:00 |
| `retrieved_at` | 2026-11-20T14:36:23.684534+00:00 |
| `final_url` | [Source](https://www.pedalhub.net/wp-content/uploads/2026/03/AI-in-the-Early-Years-Project-report-27-February-2026.pdf) |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Exact response retained locally; no independent capture-specific archive was established in this bounded intake. |
| `sha256` | 2d6a1ce62413de4b49f4929c51c3aef1f105bf6ccb420bbbf6f714e0865f58e9 |
| `byte_length` | 5358005 |
| `mime_type` | application/pdf |
| `published_on` | 2026-03 |
| `version_claim` | Publisher or identified report edition reviewed in this intake. |
| `locator_basis` | Printed pages where specified; statutory sections or article content for HTML. |
| `capture_path` | .source-captures/synthesis-2d6a1ce62413de4b49f4929c51c3aef1f105bf6ccb420bbbf6f714e0865f58e9.pdf |
| `preservation_status` | captured |

<a id="intake_collier_pixiepaw_2026"></a>
### intake_collier_pixiepaw_2026

**Source:** `collier_pixiepaw_2026`. **Theme:** targeted_admissions. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Same issued report or article edition as the canonical source record; cited distribution representation identified separately.

**Inspected scope:** NBC’s account of its Pixie-Paw hands-on testing and retailer responses.

**Locators:** NBC’s account of its Pixie-Paw hands-on testing and retailer responses.

**Visual check:** Scoped text and source/edition metadata reviewed; no complete visual audit.

**Findings:**

- Journalists reported firsthand unsuitable output elicited from the Pixie-Paw toy and separately reported retailer reactions.

**Counterevidence / alternative:** The source scope does not establish claims beyond the reported observation or documentary act.

**Limits:** Original reporting on a distinct toy and test, not a PIRG observation, controlled comparison, representative rate, or independent evidence of actual child exposure.

**Replication:** `not_performed`. **Numerical check:** Qualifying source counts checked in stated material, not independently recomputed.

**Relevance:** `claim_evidence`. **Claim links:** [C102](claims.md#c102)

**Relevance rationale:** Mapped on November 20 within the same scoped inspection; no additional reading, causal inference or replication is claimed.

**Next check:** Check independent corroboration before extending the source to prevalence, effectiveness or causation.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.nbcnews.com/tech/tech-news/ai-toys-kids-walmart-target-pull-plush-cat-described-sexual-violence-rcna608588) |
| `attempted_at` | 2026-11-20T14:36:19.210124+00:00 |
| `retrieved_at` | 2026-11-20T14:36:22.541060+00:00 |
| `final_url` | [Source](https://www.nbcnews.com/tech/tech-news/ai-toys-kids-walmart-target-pull-plush-cat-described-sexual-violence-rcna608588) |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Exact response retained locally; no independent capture-specific archive was established in this bounded intake. |
| `sha256` | 20abf8534641570b4bc4b9b247e943c67d5b2672987af89bb9d0dba45d598318 |
| `byte_length` | 381053 |
| `mime_type` | text/html |
| `published_on` | 2026-11-17 |
| `version_claim` | Publisher or identified report edition reviewed in this intake. |
| `locator_basis` | Printed pages where specified; statutory sections or article content for HTML. |
| `capture_path` | .source-captures/synthesis-20abf8534641570b4bc4b9b247e943c67d5b2672987af89bb9d0dba45d598318.html |
| `preservation_status` | captured |
## governance-implementation-2026-11-20

**As of:** 2026-11-20. **Base commit:** `dabef84518d7b4db5cbdab6a69dbf9bdad2f0803`.

**Question:** Which records document a reported action or decision beyond the existence of a policy or mechanism?

**Selection basis:** First check the three passages identified for C17, C41 and C84. Then review unmapped governance records for dated actions and identifiable decisions. The OpenAI decision section was checked through the publisher’s indexed HTML and is documented in C84. A direct download returned HTTP 403, so that check has no new retained-source event.

**Stopping rule:** Map an existing record only where a scoped primary-source passage supports, narrows or challenges a specific proposition. Leave other records unresolved.

| Theme | Why selected | Canonical keys |
|---|---|---|
| Reporting, internal review and decisions, and government activity | Add specific evidence of use, review, decisions or operations where the map previously had a policy, proposal or scope argument. | `perset_developersmanaging_2025`, `anthropic_responsiblescaling_2024`, `aisi_fourthprogress_2024`, `aisi_year_2024`, `bis_establishmentreporting_2024`, `openai_frontiertrainingenvironment_2026` |

### Event index

| Event | Source | Reading | Edition / coverage effect | Relevance |
|---|---|---|---|---|
| [governance_implementation_oecd](#governance_implementation_oecd) | `perset_developersmanaging_2025` | Selected sections | same_record / scoped_review | claim_evidence |
| [governance_implementation_anthropic](#governance_implementation_anthropic) | `anthropic_responsiblescaling_2024` | Selected sections | related_edition / none | claim_evidence |
| [governance_implementation_aisi_progress](#governance_implementation_aisi_progress) | `aisi_fourthprogress_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [governance_implementation_aisi_year](#governance_implementation_aisi_year) | `aisi_year_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [governance_implementation_bis_proposal](#governance_implementation_bis_proposal) | `bis_establishmentreporting_2024` | Selected sections | same_record / scoped_review | claim_evidence |
| [governance_implementation_bis_agenda](#governance_implementation_bis_agenda) | `bis_establishmentreporting_2024` | Selected sections | related_edition / none | claim_evidence |

<a id="governance_implementation_oecd"></a>
### governance_implementation_oecd

**Source:** `perset_developersmanaging_2025`. **Theme:** governance_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Publisher PDF for the paper identified by DOI 10.1787/658c2ad6-en.

**Inspected scope:** First-round dates and submission count on PDF page 10, and the analysis scope on PDF page 12.

**Locators:** First-round dates and submission count on PDF page 10, and the analysis scope on PDF page 12.

**Visual check:** Selected text was checked.

**Findings:**

- The OECD records 20 voluntary submissions between February and June 2025 and describes its findings as illustrative accounts of participants’ reported practices.

**Counterevidence / alternative:** The report describes voluntary participants and illustrative examples. The reporting count has no denominator for wider adoption.

**Limits:** No independent assessment of safeguards, population denominator or wider adoption is established.

**Replication:** `not_performed`. **Numerical check:** Count and date range checked against the paper’s text.

**Relevance:** `claim_evidence`. **Claim links:** [C17](claims.md#c17)

**Relevance rationale:** Affirmative evidence of use of the disclosure mechanism for C17.

**Next check:** Seek an independently assessed implementation sample before using the reports to infer adoption or controls in operation.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/09/how-are-ai-developers-managing-risks_fbaeb3ad/658c2ad6-en.pdf) |
| `attempted_at` | 2026-11-20T15:46:00.492499+00:00 |
| `retrieved_at` | 2026-11-20T15:46:01.779061+00:00 |
| `final_url` | [Source](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/09/how-are-ai-developers-managing-risks_fbaeb3ad/658c2ad6-en.pdf) |
| `sha256` | 2b49417beaded517b58e67b07bc76cbbee07db3dfecbdf83211306b46e9eb961 |
| `byte_length` | 2991026 |
| `mime_type` | application/pdf |
| `capture_path` | .source-captures/synthesis-2b49417beaded517b58e67b07bc76cbbee07db3dfecbdf83211306b46e9eb961.pdf |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Publisher response retained locally. Archive availability was outside this review. |
| `published_on` | 2025-09-25 |
| `version_claim` | OECD Artificial Intelligence Papers No. 45, September 2025. |
| `locator_basis` | PDF viewer pages 10 and 12. |
| `preservation_status` | captured |

<a id="governance_implementation_anthropic"></a>
### governance_implementation_anthropic

**Source:** `anthropic_responsiblescaling_2024`. **Theme:** governance_implementation. **Reading:** Selected sections. **Coverage effect:** `none`.

**Edition match:** `related_edition`. Companion announcement for the 2024 RSP update. The legacy catalog URL returns 404. The announcement and underlying policy are distinct documents.

**Inspected scope:** Learning from experience in the dated issuer announcement.

**Locators:** Learning from experience in the dated issuer announcement.

**Visual check:** Selected text was checked.

**Findings:**

- Anthropic reports a first internal adherence review that identified procedural departures, including an evaluation set completed three days late, and a need to improve compliance tracking.

**Counterevidence / alternative:** The company judged the identified departures to pose minimal risk. That judgment is also self-reported.

**Limits:** Company account. Underlying review records, external assurance and evidence of effective follow-up were outside the check.

**Replication:** `not_performed`. **Numerical check:** Three-day delay checked as reported.

**Relevance:** `claim_evidence`. **Claim links:** [C41](claims.md#c41)

**Relevance rationale:** Documents a company-reported internal review finding for C41.

**Next check:** Seek the underlying review and independently checked follow-up if used to support an assurance claim.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy) |
| `attempted_at` | 2026-11-20T15:46:00.494495+00:00 |
| `retrieved_at` | 2026-11-20T15:46:01.017551+00:00 |
| `final_url` | [Source](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy) |
| `sha256` | 58a6fd3c4e7a748588a237e3346dcf64a8d6416d2bcfcd0cbba11797533328de |
| `byte_length` | 165832 |
| `mime_type` | text/html |
| `capture_path` | .source-captures/synthesis-58a6fd3c4e7a748588a237e3346dcf64a8d6416d2bcfcd0cbba11797533328de.html |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Publisher response retained locally. Archive availability was outside this review. |
| `published_on` | 2024-10-15 |
| `version_claim` | October 15, 2024 issuer announcement. |
| `locator_basis` | Published date and Learning from experience heading. |
| `preservation_status` | captured |

<a id="governance_implementation_aisi_progress"></a>
### governance_implementation_aisi_progress

**Source:** `aisi_fourthprogress_2024`. **Theme:** governance_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Current issuer HTML for the 2024 report. It includes a later institute rename notice.

**Inspected scope:** Product 1, Government safety testing, and Operationalising the Bletchley Declaration.

**Locators:** Product 1, Government safety testing, and Operationalising the Bletchley Declaration.

**Visual check:** Selected text was checked.

**Findings:**

- The institute reports having run a frontier-model test before deployment and records the April 2024 UK–US agreement to cooperate on testing.

**Counterevidence / alternative:** The baseline testing described separately used publicly available models.

**Limits:** The account does not disclose the result of that specific earlier pre-deployment test or establish that it was a joint test.

**Replication:** `not_performed`. **Numerical check:** No aggregate test count credited to this source.

**Relevance:** `claim_evidence`. **Claim links:** [C104](claims.md#c104)

**Relevance rationale:** Supplies dated cooperation and testing evidence for C104.

**Next check:** Check model-specific and counterpart reports for access, timing and follow-up.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.aisi.gov.uk/blog/fourth-progress-report) |
| `attempted_at` | 2026-11-20T15:46:00.497493+00:00 |
| `retrieved_at` | 2026-11-20T15:46:00.935037+00:00 |
| `final_url` | [Source](https://www.aisi.gov.uk/blog/fourth-progress-report) |
| `sha256` | 9a1e5283fd0f0f7aa3c974227c970f6c60249e93780588b7f1f72c8bebdfca36 |
| `byte_length` | 37416 |
| `mime_type` | text/html |
| `capture_path` | .source-captures/synthesis-9a1e5283fd0f0f7aa3c974227c970f6c60249e93780588b7f1f72c8bebdfca36.html |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Publisher response retained locally. Archive availability was outside this review. |
| `published_on` | 2024 |
| `version_claim` | Fourth progress report, 2024. |
| `locator_basis` | Named publisher sections. |
| `preservation_status` | captured |

<a id="governance_implementation_aisi_year"></a>
### governance_implementation_aisi_year

**Source:** `aisi_year_2024`. **Theme:** governance_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Current issuer HTML for the 2024 retrospective. It includes a later institute rename notice.

**Inspected scope:** A Technical Authority on AI Safety and Shaping global AI governance.

**Locators:** A Technical Authority on AI Safety and Shaping global AI governance.

**Visual check:** Selected text was checked.

**Findings:**

- AISI reports evaluating 16 models across its first year and conducting several exercises jointly with the US after the April agreement.

**Counterevidence / alternative:** AISI explicitly disclaims government safety certification and model endorsement.

**Limits:** The 16 includes the whole programme. The number of joint or pre-deployment tests and changes attributable to testing remain unestablished.

**Replication:** `not_performed`. **Numerical check:** First-year total of 16 models checked against the published text.

**Relevance:** `claim_evidence`. **Claim links:** [C104](claims.md#c104)

**Relevance rationale:** Supplies reported testing activity and its limits for C104.

**Next check:** Check model-specific and counterpart reports before drawing conclusions about coverage or release decisions.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.aisi.gov.uk/blog/our-first-year) |
| `attempted_at` | 2026-11-20T15:46:00.499500+00:00 |
| `retrieved_at` | 2026-11-20T15:46:00.906512+00:00 |
| `final_url` | [Source](https://www.aisi.gov.uk/blog/our-first-year) |
| `sha256` | eb5200f16afc1adf4ca6960c1ed11a906cf69187f084391e0ade79ebfcc66fd8 |
| `byte_length` | 34421 |
| `mime_type` | text/html |
| `capture_path` | .source-captures/synthesis-eb5200f16afc1adf4ca6960c1ed11a906cf69187f084391e0ade79ebfcc66fd8.html |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Publisher response retained locally. Archive availability was outside this review. |
| `published_on` | 2024 |
| `version_claim` | First-year retrospective, 2024. |
| `locator_basis` | Named publisher sections. |
| `preservation_status` | captured |

<a id="governance_implementation_bis_proposal"></a>
### governance_implementation_bis_proposal

**Source:** `bis_establishmentreporting_2024`. **Theme:** governance_implementation. **Reading:** Selected sections. **Coverage effect:** `scoped_review`.

**Edition match:** `same_record`. Issued Federal Register notice for the canonical September 2024 proposal.

**Inspected scope:** Discussion of the Proposed Rule, printed page 73614.

**Locators:** Discussion of the Proposed Rule, printed page 73614.

**Visual check:** Selected text was checked.

**Findings:**

- BIS says it collected information via a mandatory survey issued on January 26, 2024 to selected developers. Quarterly notifications were proposed separately.

**Counterevidence / alternative:** The recurring notification language is prospective. The Unified Agenda record shows withdrawal.

**Limits:** The survey instrument, responses and their use were not checked.

**Replication:** `not_performed`. **Numerical check:** Survey and proposed schedule dates checked against the notice.

**Relevance:** `claim_evidence`. **Claim links:** [C105](claims.md#c105)

**Relevance rationale:** Provides the implementation observation and proposal for C105.

**Next check:** Seek the survey instrument and records of returns or use to assess coverage.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.govinfo.gov/content/pkg/FR-2024-09-11/pdf/2024-20529.pdf) |
| `attempted_at` | 2026-11-20T15:46:00.501499+00:00 |
| `retrieved_at` | 2026-11-20T15:46:00.979959+00:00 |
| `final_url` | [Source](https://www.govinfo.gov/content/pkg/FR-2024-09-11/pdf/2024-20529.pdf) |
| `sha256` | 135939e48b5c31a4cd370d8596c40cadd0123155622b044f86e6374f01d03762 |
| `byte_length` | 282235 |
| `mime_type` | application/pdf |
| `capture_path` | .source-captures/synthesis-135939e48b5c31a4cd370d8596c40cadd0123155622b044f86e6374f01d03762.pdf |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Publisher response retained locally. Archive availability was outside this review. |
| `published_on` | 2024-09-11 |
| `version_claim` | 89 FR 73612, FR Doc. 2024-20529. |
| `locator_basis` | Printed page 73614, PDF viewer page 3. |
| `preservation_status` | captured |

<a id="governance_implementation_bis_agenda"></a>
### governance_implementation_bis_agenda

**Source:** `bis_establishmentreporting_2024`. **Theme:** governance_implementation. **Reading:** Selected sections. **Coverage effect:** `none`.

**Edition match:** `related_edition`. Ancillary Unified Agenda record for the same RIN as the proposal. The request parameter is 202510 and the served page displays Publication ID 2026.

**Inspected scope:** RIN identity, rulemaking stage and Timetable.

**Locators:** RIN identity, rulemaking stage and Timetable.

**Visual check:** Selected text was checked.

**Findings:**

- The published timetable shows a September 11, 2024 proposal and withdrawal on December 16, 2025.

**Counterevidence / alternative:** The announcement of a recurring reporting proposal supplies no quarterly reports or evidence of operations.

**Limits:** This administrative status record concerns this specific proposal.

**Replication:** `not_performed`. **Numerical check:** Withdrawal date checked against the action table.

**Relevance:** `claim_evidence`. **Claim links:** [C105](claims.md#c105)

**Relevance rationale:** Qualifies the recurring proposal’s status for C105.

**Next check:** Check separate authority before making claims about other reporting obligations or collections.

| Capture field | Value |
|---|---|
| `original_url` | [Source](https://www.reginfo.gov/public/do/eAgendaViewRule?RIN=0694-AJ55&operation=OPERATION_PRINT_RULE&pubId=202510) |
| `attempted_at` | 2026-11-20T15:46:00.503575+00:00 |
| `retrieved_at` | 2026-11-20T15:46:01.091913+00:00 |
| `final_url` | [Source](https://www.reginfo.gov/public/do/eAgendaViewRule?RIN=0694-AJ55&operation=OPERATION_PRINT_RULE&pubId=202510) |
| `sha256` | db263784651c7884d399b492c6d2f35789095aca6cc72b84de73427917c80f7d |
| `byte_length` | 9691 |
| `mime_type` | text/html |
| `capture_path` | .source-captures/synthesis-db263784651c7884d399b492c6d2f35789095aca6cc72b84de73427917c80f7d.html |
| `archive_url` | Not recorded / unavailable |
| `archive_checked_on` | Not recorded / unavailable |
| `archive_unavailable_reason` | Publisher response retained locally. Archive availability was outside this review. |
| `published_on` | Not recorded / unavailable |
| `version_claim` | Unified Agenda RIN 0694-AJ55, displayed Publication ID 2026. |
| `locator_basis` | Official status and timetable labels. |
| `preservation_status` | captured |
