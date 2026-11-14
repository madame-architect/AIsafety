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
