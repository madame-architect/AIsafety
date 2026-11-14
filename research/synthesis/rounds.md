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
