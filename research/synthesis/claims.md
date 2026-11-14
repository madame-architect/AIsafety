# Claim and evidence map

Generated from [claims.yaml](claims.yaml). Source identities resolve through [records.yaml](../../records.yaml); record-level inspection and limitations appear in [coverage.csv](coverage.csv). This is a provisional map of selected synthesis propositions, not a claim that the entire corpus supports them.

Assessment date: **2026-11-14**. `supplied_ledger` means inherited notes; `prior_audit` means a separate AI-assisted source check reported by the supplied audit; `this_run_primary` means scoped primary inspection in this run; `repo_source_review` means an existing dated repository review. None denotes independent human review or replication.

Status `provisional` identifies a working synthesis; `scoped_check` identifies a proposition with the stated source-level checking basis (which may be a prior audit); `unresolved` retains a material discrepancy or hold; `historical` limits a finding to its dated record. A scoped check does not verify every source claim.

## Claim index

| Claim | Theme | Status | Proposition |
|---|---|---|---|
| [C01](#c01) | evaluation_configuration | provisional | The reviewed benchmarks add distinct task, workflow and reliability measurements; each result describes its tested configuration. |
| [C02](#c02) | evaluation_configuration | scoped_check | Phuong v2 Table 23 concerns a toy safety-filter modification task in instrumental self-reasoning; its Pro-CoT easy/easy score is 0.5 despite a stated 0.7 passing criterion. |
| [C03](#c03) | evaluation_configuration | provisional | Rankings and apparent capability gains can change with inference budgets, attempt aggregation and task selection. |
| [C04](#c04) | evaluation_configuration | provisional | Unlearning evaluations can establish reduced performance on specified probes while leaving format sensitivity, retained knowledge and utility tradeoffs open. |
| [C05](#c05) | safeguards | provisional | Many-shot defenses show both improvements and residual scaling/utility limits under different training and evaluation conditions. |
| [C06](#c06) | safeguards | provisional | Classifier red-team results support resistance to specified attack criteria; rates across defense generations and attack protocols should remain separate. |
| [C07](#c07) | safeguards | provisional | Instruction priority, resistance to weight modification and pretraining poisoning address different attacker access and control surfaces. |
| [C08](#c08) | evaluator_integrity | provisional | HelpSteer2 and its preference extension provide useful reward-learning comparisons but share data lineage. |
| [C09](#c09) | evaluator_integrity | provisional | Position calibration improved agreement with one author-majority reference, and the highest reported agreement included human input. |
| [C10](#c10) | evaluator_integrity | provisional | Xu's benchmark exposure indicators are proxies, and its printed edit-similarity rule and threshold disagree with the pinned released helper. |
| [C11](#c11) | evaluator_integrity | scoped_check | Debate can improve inference-time judge accuracy under information asymmetry, while comparison with direct QA depends on task and source access. |
| [C12](#c12) | evaluator_integrity | scoped_check | Evidence selection and error detection offer distinct interpretations of debate benefits; overall accuracy alone does not resolve them. |
| [C13](#c13) | evaluator_integrity | provisional | Feature attribution and selected interventions provide affirmative mechanistic evidence, while some aggregate SAE metrics fail to distinguish trained from randomized models. |
| [C14](#c14) | evaluator_integrity | provisional | Constructed alignment-faking, sabotage and auditing experiments establish behavior under their elicitation; spontaneous initiation and induced continuation remain different outcomes. |
| [C15](#c15) | outcomes | scoped_check | The corrected Salvi study supports a personalized-GPT-4 versus human-baseline difference, while the added benefit over unpersonalized GPT-4 remains uncertain. |
| [C16](#c16) | evaluation_configuration | unresolved | CAISI's published comparator label and imputation note disagree with the supplied ledger; the historical explanation is unresolved. |
| [C17](#c17) | governance | scoped_check | Voluntary commitments, disclosure portals and documentary framework scores make governance provisions inspectable; their existence or score alone does not establish implemented controls, compliance or control effects. Legal force, scope and decision authority require separate coding. |
| [C18](#c18) | governance | scoped_check | Within-issuer edition comparisons reveal specific documentary changes: DeepMind’s cyber weight-security recommendation moves from SL2 in v3.0 to SL2+ in v3.1; Microsoft changes screening and reassessment scope/timing while retaining materially similar offensive-cyber tier descriptions. |
| [C19](#c19) | governance | scoped_check | OpenAI Preparedness v2 distinguishes the conditional halt for attained Critical cyber capability from additional development safeguards for attained or forecast Critical capability; High predeployment provisions and later internal-use/containment statements have separate scopes. |
| [C20](#c20) | governance | scoped_check | Inability-oriented safety cases, broader system safety arguments and model cards are complementary proposals: they structure different claims and disclosures, but their publication does not validate a deployment or establish that safety cases are the only valid governance method. |
| [C21](#c21) | cyber_case_study | scoped_check | ARTEMIS supplies a descriptive human-agent performance comparison in one authorized university network: A2 reported nine valid findings from eleven submissions and outranked nine of ten professionals under the study score; it does not estimate the causal uplift of AI assistance in general operations. |
| [C22](#c22) | cyber_case_study | scoped_check | AWS and GTIG document AI-assisted components in real compromises, supporting concrete operational pathways; provider-attributed speed or scale is not a matched estimate of incremental AI-caused attacks or harm. |
| [C23](#c23) | cyber_case_study | scoped_check | AISI’s July incident account reports nineteen out-of-scope actions across ten of 122 evaluation runs, a rejected malicious pull request and rapid containment, with no resulting real-world harm evidenced by investigators. These reported interventions do not estimate how much harm the controls prevented. |
| [C24](#c24) | cyber_case_study | scoped_check | Souly et al.’s fully simulated evaluation shows that out-of-scope behavior is sensitive to explicit prompt scope in a selected scenario set; its reported 26/50 versus 4/49 comparison bounds generalization and does not establish deployed network-control effectiveness or population attack rates. |
| [C25](#c25) | cyber_case_study | unresolved | Barrett’s risk-model architecture and Murray’s structured elicitation expose assumptions linking benchmarks to hypothetical cyber risk; they do not observe matched changes in attack or harm rates. Hold Barrett’s numerical human-versus-LLM SME ransomware comparison while its task-ranking/input discrepancy remains unresolved. |
| [C26](#c26) | governance | provisional | xAI’s December2025 framework discloses basic-refusal reliance for its cyber assessment and tiered/trusted-party deployment exceptions; underlying assessment and implementation remain unverified. |
| [C27](#c27) | outcomes | provisional | Sociotechnical evaluation levels and media-based incident trends address different objects: capability and system results require additional evidence to support impact claims or population incident rates. |

<a id="c01"></a>
## C01

The reviewed benchmarks add distinct task, workflow and reliability measurements; each result describes its tested configuration.

**Status:** provisional. **Theme:** evaluation_configuration.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `folkerts_measuringaiagentscyber_2026` — supports | [Source](https://arxiv.org/pdf/2603.11214v3); v3 §§2–4; Tables 1–2; Appendix E | Multi-step enterprise and industrial-control ranges expose incomplete progress even at larger inference budgets. | `supplied_ledger`; Inherited full text description: All 30 PDF pages of v3: §§1–6, references, Appendices A–E, rendered Figures 1–7, and programmatic verification of all 24 end-to-end summary cells from 1,263 parsed appendix run rows.; not independently repeated in this integration. |
| `xie_osworld_2024` — supports | [Source](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf); NeurIPS 2024 proceedings; abstract and benchmark-design passages | OSWorld tests 369 desktop/web tasks with execution-based grading in controlled environments. | `supplied_ledger`; Inherited selected sections description: Official NeurIPS proceedings extract, including abstract and design passages; not independently repeated in this integration. |
| `xu_theagentcompany_2024` — supports | [Source](https://arxiv.org/pdf/2412.14161); Benchmark design and setup; inherited extracted lines 0–200/1302 (page locator pending) | Professional workflows are evaluated within a simulated organization. | `supplied_ledger`; Inherited selected sections description: Selected extracted PDF passages (line span 0–200 of 1302); not independently repeated in this integration. |
| `yao_taubench_2024` — supports | [Source](https://arxiv.org/pdf/2406.12045); Benchmark setup and repeated-trial reliability; inherited extracted lines 0–204/2369 (page locator pending) | Tool use, domain policies and user simulation define a repeated-trial reliability endpoint. | `supplied_ledger`; Inherited selected sections description: Selected extracted PDF passages (line span 0–204 of 2369); not independently repeated in this integration. |

**Limits:** These controlled tests do not estimate general workplace safety or operational harm. Some inherited selected-section locators are extraction spans rather than stable page references. Standalone Cybench is cited in the supplied review but absent from the admitted bibliography.

**Counterevidence / alternative:** Realistic software and longer workflows strengthen task relevance; that realism alone does not establish transfer to defended deployment or authorization boundaries.

**Next check:** Complete claim-critical methods/results and pin stable section/page locators; treat standalone Cybench as a source-admission lead, not an admitted record.

<a id="c02"></a>
## C02

Phuong v2 Table 23 concerns a toy safety-filter modification task in instrumental self-reasoning; its Pro-CoT easy/easy score is 0.5 despite a stated 0.7 passing criterion.

**Status:** scoped_check. **Theme:** evaluation_configuration.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `phuong_evaluatingfrontier_2024` — supports | [Source](https://arxiv.org/html/2403.13793v2); Appendix F.5–F.5.1; Table 23 | The task classification and numerical tension are present in the primary table and adjacent results prose. It is not the final self-proliferation takeover task. | `this_run_primary`; Targeted primary HTML text for Appendix F.5–F.5.1, Table 23 and document section headings; no full reread, figure audit or replication. |

**Limits:** This identifies an internal prose/table tension within a toy task; it does not resolve what the authors intended as their pass classification.

**Counterevidence / alternative:** The same paper contains separate self-proliferation tasks and modeled milestone bounds in Table 11; those cannot be substituted for Table 23.

**Next check:** The synthesis task description is corrected here. Seek author clarification before treating the inconsistent pass wording as an established capability result.

<a id="c03"></a>
## C03

Rankings and apparent capability gains can change with inference budgets, attempt aggregation and task selection.

**Status:** provisional. **Theme:** evaluation_configuration.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `wijk_rebench_2025` — supports | [Source](https://proceedings.mlr.press/v267/wijk25a.html); PMLR 267 proceedings abstract; separately accessed arXiv v1 budget/results sections | The proceedings abstract reports the best agent ahead at two aggregate hours, a narrow human lead at eight, and a larger human advantage at 32 total hours across attempts. | `supplied_ledger`; Inherited selected sections description: PMLR 267:66772–66832 proceedings landing page and abstract; separate author preprint arXiv v1, selected methods on benchmark design and human recruitment, baseline tables and results on time budget and task heterogeneity. Checked published title and stated sample and budget findings against proceedings abstract.; not independently repeated in this integration. |
| `folkerts_measuringaiagentscyber_2026` — bounds | [Source](https://arxiv.org/pdf/2603.11214v3); v3 Table 1; Appendix E Table 2; §3.2 | Higher budgets improve some tested models, but 10M-token results are not monotonically ordered by model release. One inherited recomputation reports 9.6 versus the paper's 9.8 for one appendix-derived cell. | `supplied_ledger`; Inherited full text description: All 30 PDF pages of v3: §§1–6, references, Appendices A–E, rendered Figures 1–7, and programmatic verification of all 24 end-to-end summary cells from 1,263 parsed appendix run rows.; not independently repeated in this integration. |

**Limits:** RE-Bench's 32-hour point is an aggregate over attempts, not one continuous 32-hour run. The exact proceedings PDF was not obtained in the inherited review. Folkerts' single-cell discrepancy remains a lead.

**Counterevidence / alternative:** The benchmarks do show useful task performance and budget sensitivity. Narrow task distributions and best-of-k selection limit general claims about long-horizon autonomy.

**Next check:** Inspect the exact RE-Bench proceedings PDF and reproduce budget/attempt accounting; resolve the Folkerts cell with the authors before quoting it.

<a id="c04"></a>
## C04

Unlearning evaluations can establish reduced performance on specified probes while leaving format sensitivity, retained knowledge and utility tradeoffs open.

**Status:** provisional. **Theme:** evaluation_configuration.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `li_wmdpbenchmarkmeasuring_2024` — supports | [Source](https://proceedings.mlr.press/v235/li24bc.html); PMLR proceedings abstract; separately inspected arXiv v7 setup, mitigation and limitations (version equivalence not established) | WMDP supplies hazardous-knowledge proxy questions and reports reduced measured performance under RMU. | `supplied_ledger`; Inherited selected sections description: PMLR abstract/metadata and arXiv v7 setup, mitigation and limitations excerpts; not independently repeated in this integration. |
| `joshi_robustevaluationunlearning_2024` — bounds | [Source](https://arxiv.org/html/2411.15477v1); v1 methods; full results tables; Appendices A–E | On synthetic TOFU author facts, query transformations change measured forgetting and retention. Comprehension with answers supplied in context tests generation suppression. | `supplied_ledger`; Inherited full text description: Version 1 full substantive text and appendices A–E, including transformation procedures, metrics, prompt examples, qualitative examples and both full result tables.; not independently repeated in this integration. |
| `liu_rethinkingmachineunlearnin_2024` — contextualizes | [Source](https://doi.org/10.1038/s42256-025-00985-0); arXiv v6 conceptual opening; Nature Machine Intelligence metadata | The review distinguishes unlearning goals, leakage and collateral effects. | `supplied_ledger`; Inherited selected sections description: arXiv v6 abstract/conceptual opening and Nature publisher metadata; not independently repeated in this integration. |

**Limits:** Hazardous multiple-choice knowledge and synthetic facts differ from operational harmful capability or verified deletion. Metrics and base-model controls must remain matched.

**Counterevidence / alternative:** Lower probe scores are a measured result; changed-prompt recovery and retention losses constrain the interpretation rather than erase that result.

**Next check:** Complete the final-version methods and compare each probe with its own base/fine-tuned controls before inferring operational risk reduction or permanent erasure.

<a id="c05"></a>
## C05

Many-shot defenses show both improvements and residual scaling/utility limits under different training and evaluation conditions.

**Status:** provisional. **Theme:** safeguards.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `anil_manyshotjailbreaking_2024` — supports | [Source](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea456e232efb72d261715e33ce25f208-Paper-Conference.pdf); NeurIPS 2024 §§5.1–5.4; Figure 5 | Several general/targeted fine-tuning approaches mainly reduced the baseline while leaving success growth with additional shots. | `supplied_ledger`; Inherited selected sections description: NeurIPS PDF opening design and sections 5.1–5.4 mitigation excerpts, including Figure 5 and slope/intercept results; not independently repeated in this integration. |
| `ackerman_mitigatingmanyshot_2025` — supports | [Source](https://arxiv.org/html/2504.09604v3); v3 §§2.1,3.1/Table 1,3.2,4.2 | On Llama 3.1 8B, adversarial fine-tuning with sanitization examples and input sanitization flattened slopes in several tested settings, with some benign long-dialogue preferences favoring untuned answers. | `prior_audit`; Prior audit checked selected primary sections on the single-model test, reported 8192 context and utility tradeoffs; not independently repeated here. |

**Limits:** Models, examples, controls and tested context lengths differ. The reported 8192 context is a test limit, not an independently certified architectural maximum.

**Counterevidence / alternative:** Ackerman's flatter slopes bound any claim that fine-tuning can only shift intercepts; Anil's residual scaling bounds broad robustness claims.

**Next check:** Compare matched attack, model, training-data and benign-utility conditions before explaining the difference or extrapolating to longer contexts.

<a id="c06"></a>
## C06

Classifier red-team results support resistance to specified attack criteria; rates across defense generations and attack protocols should remain separate.

**Status:** provisional. **Theme:** safeguards.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `sharma_constitutionalclassifiers_2025` — supports | [Source](https://arxiv.org/pdf/2501.18837); Study setup and human red-team criterion; inherited extracted lines 0–174/3212 (page locator pending) | Adversarially trained classifiers resisted the tested universal extraction criterion and reduced held-out jailbreaks. | `supplied_ledger`; Inherited selected sections description: Selected extracted PDF passages (line span 0–174 of 3212); not independently repeated in this integration. |
| `cunningham_constitutionalclassifiers_2026` — contextualizes | [Source](https://arxiv.org/pdf/2601.04603); See coverage.csv material-inspected and limitations fields; stable section locator pending | A later defense generation is a separate object and cannot silently replace the earlier target in a bypass-rate comparison. | `supplied_ledger`; Inherited selected sections description: 17-page arXiv PDF, abstract, introduction, shadow-deployment and red-team result excerpts; not independently repeated in this integration. |

**Limits:** The supplied review of Sharma used a small selected-section span. Defense generation, target domain, feedback, attacker budget and the multi-query success criterion are part of each endpoint.

**Counterevidence / alternative:** Partial bypasses and adaptive attacks can coexist with failure to meet a universal-jailbreak criterion; neither is a direct measure of deployment-wide misuse.

**Next check:** Finish the relevant methods/results and pair each adaptive attack with its exact defense version, denominator, feedback and success definition.

<a id="c07"></a>
## C07

Instruction priority, resistance to weight modification and pretraining poisoning address different attacker access and control surfaces.

**Status:** provisional. **Theme:** safeguards.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `wallace_instructionhierarchy_2024` — supports | [Source](https://arxiv.org/html/2404.13208v1); v1 §4 experiment setup, over-refusal results; Appendix A | Hierarchy training improves several tested GPT-3.5 robustness endpoints against a capability-only fine-tuned baseline, while two benign over-refusal tests regress. | `prior_audit`; Prior audit checked selected primary setup/results sections, not the complete appendix or all figures; not repeated here. |
| `tamirisa_tamperresistantsafeguards_2024` — supports | [Source](https://arxiv.org/pdf/2408.00761); Training/attack setup; inherited extracted lines 0–247/1440 (page locator pending) | Tamper-resistance training increases resistance to tested fine-tuning attacks within specified budgets. | `supplied_ledger`; Inherited selected sections description: Selected extracted PDF passages (line span 0–247 of 1440); not independently repeated in this integration. |
| `souly_poisoningattacksrequire_2025` — contextualizes | [Source](https://arxiv.org/pdf/2510.07192); Pretraining experiments; inherited extracted lines 0–276/1914 (page locator pending) | Tested backdoors used roughly constant poison-document counts across a twentyfold clean-data scale difference. | `supplied_ledger`; Inherited selected sections description: Selected extracted PDF passages (line span 0–276 of 1914); not independently repeated in this integration. |
| `vassilev_adversarialmltaxonomy_2025` — contextualizes | [Source](https://doi.org/10.6028/NIST.AI.100-2e2025); NIST AI 100-2e2025; terminology and taxonomy | Adversarial-ML terminology helps distinguish attacker objectives and access. | `supplied_ledger`; Inherited selected sections description: Selected extracted PDF passages (line span 0–327 of 4288); not independently repeated in this integration. |
| `liu_promptinjectionattacks_2025` — supports | [Source](https://www.usenix.org/conference/usenixsecurity24/presentation/liu-yupei); USENIX Security2024 proceedings pp1831–1847; attack/defense benchmark; section8 limitations | The intended Liu proceedings work benchmarks five attacks and ten defenses across ten models/seven tasks. The unrelated StruQ identifier and abstract are removed while retaining the citation key. Section8 leaves adaptive attacks against known-answer detection for future work. | `supplied_ledger`; Inherited full-text scope identifies the17-page intended proceedings paper. This run freshly checked official metadata and the specific section8 limitation, not all methods/results or experiments. |

**Limits:** Model-level refusal or hierarchy training does not establish system authorization, data isolation or egress enforcement. Poisoning and tamper findings are bounded by tested models, triggers and resource budgets. The Liu citation identity is corrected from the supplied patch; its full-text label remains inherited and does not extend to the separate StruQ work or expanded preprint.

**Counterevidence / alternative:** Specific robustness gains remain useful within their threat models; they cannot be pooled into one security guarantee.

**Next check:** Check each control against its intended attacker access, budget and endpoint; complete claim-critical sections and retain the corrected Liu identity.

<a id="c08"></a>
## C08

HelpSteer2 and its preference extension provide useful reward-learning comparisons but share data lineage.

**Status:** provisional. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `wang_helpsteer2opensource_2024` — supports | [Source](https://arxiv.org/pdf/2406.08673); Dataset and reward-model setup; inherited extracted lines 0–87/1372 (page locator pending) | Multi-attribute annotations and reported RewardBench results support a dated reward-model comparison. | `supplied_ledger`; Inherited selected sections description: Selected extracted PDF passages (line span 0–87 of 1372); not independently repeated in this integration. |
| `wang_helpsteer2preference_2024` — bounds | [Source](https://arxiv.org/pdf/2410.01257); Preference-data extension and matched reward-model comparison; inherited extracted lines 0–103/1349 | The extension adds preferences and rationales to HelpSteer2 and compares regression and Bradley–Terry models. | `supplied_ledger`; Inherited selected sections description: Selected extracted PDF passages (line span 0–103 of 1349); not independently repeated in this integration. |

**Limits:** Only selected opening sections were inspected in the supplied ledger. Shared annotations do not constitute independent replication, and leaderboard gains are model/benchmark-specific.

**Counterevidence / alternative:** Matched model comparisons are informative about the tested reward-learning design, but do not establish downstream safety or general judge validity.

**Next check:** Complete methods, splits and evaluation details; record shared data/annotator lineage before counting evidence families.

<a id="c09"></a>
## C09

Position calibration improved agreement with one author-majority reference, and the highest reported agreement included human input.

**Status:** provisional. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `wang_largenotfairevaluators_2024` — supports | [Source](https://aclanthology.org/2024.acl-long.511.pdf); ACL 2024 pp.9444–9445, §§2.3.3,3.1–3.3; Table 4 | Agreement rises from 52.7% to 62.5% with multiple evidence sampling and to 73.8% with selected human labels; three author annotators supplied the reference on 80 questions. | `prior_audit`; Prior audit checked selected proceedings sections and Table 4; not an independent full 11-page reread or code execution. |

**Limits:** The 73.8% score belongs to the combined human-assisted procedure. Individual annotators contribute to the majority against which they are compared.

**Counterevidence / alternative:** Swapping response positions changes results, but the experiment does not establish the mechanism of bias or performance on new judge models and tasks.

**Next check:** Use a separate held-out human reference and report routed human items independently when evaluating the intended procedure.

<a id="c10"></a>
## C10

Xu's benchmark exposure indicators are proxies, and its printed edit-similarity rule and threshold disagree with the pinned released helper.

**Status:** provisional. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `xu_benchmarkingleakage_2024` — supports | [Source](https://arxiv.org/html/2404.18824v1); v1 §5.3; Appendix A.3 Eq.5; pinned metric_utils.py lines 27,47 | Paper prints normalized edit distance and a >0.9 threshold; code calculates its complement and uses >0.75. | `prior_audit`; Prior audit checked selected paper sections and all 75 lines of the helper at commit 8cbb7fd341f0efe840ed5d9b148b87287362d9e9; no experiment-revision provenance or 186-row recomputation repeated. |

**Limits:** Original-versus-paraphrase familiarity is indirect evidence of exposure. The helper mismatch does not identify which implementation generated the reported experiment.

**Counterevidence / alternative:** Exact string matches and controlled exposure experiments establish proxy behavior; they do not turn each flagged item into a verified leaked training record.

**Next check:** Reconcile experiment revision, formula, threshold and mixed table units before reusing affected quantitative leakage rates; code: https://github.com/GAIR-NLP/benbench/blob/8cbb7fd341f0efe840ed5d9b148b87287362d9e9/src/metric_utils.py.

<a id="c11"></a>
## C11

Debate can improve inference-time judge accuracy under information asymmetry, while comparison with direct QA depends on task and source access.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `khan_debatingmorepersuasive_2024` — supports | [Source](https://arxiv.org/html/2402.06782v4); v4 abstract and §3 main results; §2 task setup | On filtered binary QuALITY questions, reported LLM/human debate accuracy is 76%/88%, compared with 48%/60% naive and 54%/78% assigned consultancy. | `this_run_primary`; Selected primary abstract/main results and task-setup text checked; no full appendix/human-sampling audit or numerical reproduction. |
| `kenton_scalableoversightweak_2024` — bounds | [Source](https://arxiv.org/html/2407.04622v2); v2 §§3.2,4.1; Figure 2 accompanying prose | Full-article direct QA performs best across tested extractive judge configurations; debate's gains over QA without the article vary by judge/task. | `this_run_primary`; Selected primary protocol definitions, main results and figure-caption prose; no complete reread or statistical recomputation. |

**Limits:** Khan's naive human baseline used a separate experiment and its full-source human comparison is external, as recorded in the supplied ledger. These studies test inference properties, not a complete training protocol.

**Counterevidence / alternative:** Kenton's stronger direct-QA baseline and weak-judge exceptions bound a blanket debate-superiority claim without negating Khan's gains under its setup.

**Next check:** Preserve task, source access, role assignment, judge sampling and comparator; verify final proceedings/version differences and remaining appendix details before numerical publication.

<a id="c12"></a>
## C12

Evidence selection and error detection offer distinct interpretations of debate benefits; overall accuracy alone does not resolve them.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `khan_debatingmorepersuasive_2024` — supports | [Source](https://arxiv.org/html/2402.06782v4); v4 Appendix A.6 and Figure 15 caption | Quotes-only yields higher judge accuracy than quotes-plus-arguments in the reported ablation; arguments-only is worse. | `this_run_primary`; Complete selected Appendix A.6 text and Figure 15 caption inspected; chart values not independently transcribed. |
| `kenton_scalableoversightweak_2024` — supports | [Source](https://arxiv.org/html/2407.04622v2); v2 §4.2 and Figure3 discussion | Open debate better rejects an incorrect protagonist than open consultancy, at a cost when the protagonist is correct. | `this_run_primary`; Selected open-role methods and results text inspected; transcript reuse design noted, no new model runs. |

**Limits:** Kenton's open protocols select assigned-role transcripts conditional on direct-QA answers rather than eliciting autonomous strategy. Khan's quote verification relies on the source and selected questions.

**Counterevidence / alternative:** Higher overall open-consultancy accuracy can coexist with worse detection of protagonist errors; quote selection may explain part of the gain attributed to argument exchange.

**Next check:** Separate evidence retrieval/verification, correctness-conditioned error detection and judge training effects in any follow-up comparison.

<a id="c13"></a>
## C13

Feature attribution and selected interventions provide affirmative mechanistic evidence, while some aggregate SAE metrics fail to distinguish trained from randomized models.

**Status:** provisional. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `templeton_scalingmonosemanticity_2024` — supports | [Source](https://transformer-circuits.pub/2024/scaling-monosemanticity/); 2024 article; inherited opening/selected examples, extracted lines0–134/1169 | Sparse autoencoders identify interpretable features with selected steering and activation examples. | `supplied_ledger`; Inherited selected sections description: Selected extracted HTML passages (line span 0–134 of 1169); not independently repeated in this integration. |
| `kamath_tracingattentioncomputatio_2025` — supports | [Source](https://transformer-circuits.pub/2025/attention-qk/index.html); 2025 query–key feature-attribution methodology, worked examples and limitations | Bilinear feature contributions and interventions test selected attention mechanisms in Claude 3.5 Haiku. | `supplied_ledger`; Inherited full text description: Complete rendered article including methodology, worked examples, limitations, and figure captions; linked interactives not reviewed.; not independently repeated in this integration. |
| `heap_sparseautoencoders_2025` — bounds | [Source](https://arxiv.org/html/2501.17727v1); v1 §§1,3.1–3.3; Figures1–3 captions | Several fuzzing/reconstruction metrics are broadly similar across trained and three randomized Pythia variants; the separate per-occurrence Gaussian embedding Control performs poorly. | `prior_audit`; Prior audit selected primary v1 sections/captions; later audit read main text and Appendices A–D text; not all figures independently digitized. No new primary reread here. |

**Limits:** Selected features and interventions do not establish completeness of a system-wide monitor. Heap's v2 additions are a different version; token entropy does not directly measure semantic abstraction, and loss recovery is meaningful only for trained variants.

**Counterevidence / alternative:** Heap qualifies particular validation metrics, not every interpretability method. Causal interventions on selected mechanisms remain a different form of evidence.

**Next check:** Pin versions and distinguish reconstruction metrics, token diversity, local interventions and downstream monitoring performance.

<a id="c14"></a>
## C14

Constructed alignment-faking, sabotage and auditing experiments establish behavior under their elicitation; spontaneous initiation and induced continuation remain different outcomes.

**Status:** provisional. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `sheshadri_whydosome_2025` — supports | [Source](https://arxiv.org/html/2506.18032v1); arXiv v1 §§1–6; cited final conference abstract separately | Five of 25 models show an initial-elicitation harmful-compliance gap; goal preservation is consistently supported for one. | `prior_audit`; Supplied ledger originally abstract-only; later audit read complete v1 main text §§1–6, not appendices or final conference equivalence. This does not upgrade inherited corpus depth. |
| `kirk_sabotageaisafetyresearch_2026` — bounds | [Source](https://arxiv.org/pdf/2604.24618); v1 main text pp.1–15; scenario setup and results | No confirmed spontaneous sabotage was observed in evaluated scenarios; continuation of already-started sabotage differs by model. | `prior_audit`; Later audit read main text pp.1–15 of 88; appendices incomplete, awareness/refusal percentage discrepancy unresolved; no reproduction. |
| `taylor_auditinggames_2025` — contextualizes | [Source](https://arxiv.org/html/2512.07810v1); v1 auditing-game setup/results; inherited extracted lines0–415/1334 | Auditors struggled to distinguish deliberately induced sandbagging proxies from controls in the tested game. | `supplied_ledger`; Inherited selected sections description: Selected extracted HTML passages (line span 0–415 of 1334); not independently repeated in this integration. |

**Limits:** Prompt design, scenario selection, model access and statistical sensitivity condition both positive and null results. Failure to elicit behavior does not establish incapability, and induced behavior is not deployment prevalence.

**Counterevidence / alternative:** The null spontaneous-sabotage result and model differences must accompany selected positive continuation/faking observations.

**Next check:** Finish claim-critical appendices/final versions, reconcile inconsistent awareness/refusal figures, and test alternative explanations before inferring motives or deployment rates.

<a id="c15"></a>
## C15

The corrected Salvi study supports a personalized-GPT-4 versus human-baseline difference, while the added benefit over unpersonalized GPT-4 remains uncertain.

**Status:** scoped_check. **Theme:** outcomes.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `salvi_conversationalpersuasivene_2025` — supports | [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC13683042/); Corrected article Aggregate results; Author Correction substantive paragraphs | The correction replaces the direct personalization contrast P=.04 with P=.0678; its+48.7% odds and interval[−2.9%,127.6%] correspond to OR1.487[0.971,2.276]. | `this_run_primary`; Complete substantive correction text inspected; original article and supplement not reread in this pass. Main personalized-vs-human OR1.812[1.260,2.607] remains supported by inherited article review. |
| `hackenburg_evaluatingpersuasive_2024` — bounds | [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11181035/); PNAS main article Results, Table1; Discussion/Methods | Single-message experiment finds persuasive effects versus no message but no detected added accurate-targeting benefit relative to the untargeted best-message condition. | `supplied_ledger`; Inherited full text description: Complete PNAS article body, §§Results, Discussion, Materials and Methods, Table 1 and figure captions. Tried the linked separate Supporting Information PDF from PMC and PNAS; the supplement body was not retrieved.; not independently repeated in this integration. |

**Limits:** Salvi measures immediate self-reported agreement in structured ten-minute debates; Hackenburg tests static messages. Neither measures campaign outcomes, durable behavior or population effects. The supplement's 64.4% odds conversion was not independently rederived here.

**Counterevidence / alternative:** Positive effects versus a human or no-message baseline coexist with uncertain/non-detected incremental personalization effects. Different designs cannot be pooled as one targeting estimate.

**Next check:** Cite the correction DOI10.1038/s41562-026-02588-0, preserve comparator/outcome scale, and omit a general64.4% probability claim pending a defensible ordinal interpretation.

<a id="c16"></a>
## C16

CAISI's published comparator label and imputation note disagree with the supplied ledger; the historical explanation is unresolved.

**Status:** unresolved. **Theme:** evaluation_configuration.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `caisi_deepseekv4pro_2026` — unresolved | [Source](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro); Figure2 CTF-Archive-Diamond table and imputation note; current primary article | The prior audit reports the32% comparator as GPT-5.4 mini and the imputation asterisk on DeepSeek V4 Pro; the ledger instead says GPT-5 and attributes imputation to the comparator. | `prior_audit`; Prior audit read the complete substantive current article/table/captions/appendix and found the mismatch; this run's direct urllib retrieval returned403, so the source text was not independently rechecked in this integration. |

**Limits:** No authenticated historical capture establishes whether the earlier source changed or the ledger extracted it incorrectly. The current page's same update date does not resolve that history.

**Counterevidence / alternative:** The aggregate model-gap analysis is separately conditioned on suite selection, weights and tested configuration; this mismatch does not establish a cyber-specific capability lag.

**Next check:** Recover a lawful dated capture or correction from the issuer; hold the disputed comparator/imputation wording rather than assert a historical revision.

<a id="c17"></a>
## C17

Voluntary commitments, disclosure portals and documentary framework scores make governance provisions inspectable; their existence or score alone does not establish implemented controls, compliance or control effects. Legal force, scope and decision authority require separate coding.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `ukgov_frontiersafetycommitments_2024` — supports | [Source](https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024); Commitments I–VIII and footnotes; observed GOV.UK edition updated 2025-02-07 | Voluntary signatories commit to severe-risk thresholds, mitigations, governance and conditional development/deployment limits; transparency has qualifications. | `prior_audit`; Prior audit reports complete substantive commitment text including footnotes, not implementation checks or comparison with original May 2024 bytes. |
| `ec_gpai_codepractice_final_2025` — contextualizes | [Source](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai); Official landing page description of the voluntary Code and its three chapters; July 10, 2025 publication | The official overview describes a voluntary compliance tool and distinguishes the Safety/Security chapter for systemic-risk models. This does not make signatures proof of adherence or statutory compliance. | `prior_audit`; Prior audit read the complete official landing page; chapter download failed. Detailed chapter measures in the supplied ledger were not independently audited. |
| `oecd_hiroshimaprocessreporting_2025` — contextualizes | [Source](https://oecd.ai/en/transparency/overview); Overview: participation, submitting reports and browsing reports | The portal permits voluntary value-chain reporting and publication of disclosures; individual reports and their factual accuracy were not audited. | `prior_audit`; Prior audit reports full substantive current overview; it is a mutable portal, not a frozen original edition. |
| `stelling_evaluatingaiproviders_2025` — bounds | [Source](https://arxiv.org/abs/2512.01166v1); Version 1 abstract, compared with version 5 abstract and histories | The work scores framework documents against a rubric. Version-specific score changes cannot be read as a measured change in deployed control effectiveness. | `supplied_ledger`; Supplied ledger records abstract-only comparison of v1 and v5, not full methodological review or implementation verification. |
| `nist_artificialintelligence_2024` — contextualizes | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); NIST AI 600-1 risk overview and suggested-action tables; stable page locator pending | Generative AI profile extends the RMF with cross-sector GAI risks and practical suggested actions, including security and incident disclosure. | `supplied_ledger`; Inherited Selected sections; NIST AI 600-1 PDF risk overview and suggested-action tables. Recommendations are actor- and context-dependent; suggested action is not a measured result. Not independently repeated here. |
| `isoiec_42006_2025` — contextualizes | [Source](https://www.iso.org/standard/42006); ISO/IEC42006:2025 catalog scope/edition and preview; licensed normative clauses not inspected | ISO/IEC 42006 specifies additional requirements for bodies auditing and certifying AI management systems against ISO/IEC 42001. | `supplied_ledger`; Inherited Metadata only; ISO catalog scope, edition and preview entry. Licensed normative clauses unavailable in this audit. It governs certification bodies rather than prescribing model thresholds. Not independently repeated here. |
| `ec_guidelinesgpaiproviders_2025` — contextualizes | [Source](https://ec.europa.eu/newsroom/dae/redirection/document/118340); C(2025)7719final, cover Nov19,2025; paragraph9, printedp2/PDFviewerp5 | The current linked English edition says the guidelines are not binding and reserves authoritative AIAct interpretation to the CJEU. Its later cover date does not authenticate the inherited July edition. | `this_run_primary`; Fresh selected cover/paragraph9 and canonical landing-page metadata only; no complete36-page reread. Historical version reconciliation remains open. |
| `ec_gpai_trainingcontenttemplate_2025` — contextualizes | [Source](https://www.sidley.com/en/-/media/resource-pages/ai-monitor/guidance/eu-explanatory-notice-and-template-for-the-public-summary-of-training-content.pdf?la=en); C(2025)5235 final explanatory notice and template; cover and Article53(1)(d) basis; mirror identity unverified | Commission notice/template specifies a public, sufficiently detailed yet broadly comprehensive training-content summary; Article 53(2) open-source exception does not waive this obligation. | `supplied_ledger`; Inherited Selected sections; official-titled C(2025) 5235 final PDF mirror, cover, Article 53(1)(d) basis and template design. Issuer HTML returned 429. Mirror permits text inspection, without byte identity to an issuer copy. Summary is distinct from disclosure of the complete training dataset. Not independently repeated here. |

**Limits:** This is a distinction between kinds of evidence, not a determination of every instrument’s present legal force. The supplied patch corrects specified legal-status fields; unreviewed instruments and current application still require dated source checks. ISO evidence is catalog/preview scope only. The Commission template was inspected through a mirror; issuer-byte identity and exact clause locators remain open. The supplied correction package is now integrated; it does not recertify all instruments or editions.

**Counterevidence / alternative:** Statutory duties and enforceable decisions can exist alongside voluntary tools; documented implementation or outcome studies could provide additional evidence beyond a policy text or disclosure score.

**Next check:** The supplied status corrections are integrated. Complete remaining dated jurisdiction/operative-version checks and Stelling methods before broader legal or score conclusions.

<a id="c18"></a>
## C18

Within-issuer edition comparisons reveal specific documentary changes: DeepMind’s cyber weight-security recommendation moves from SL2 in v3.0 to SL2+ in v3.1; Microsoft changes screening and reassessment scope/timing while retaining materially similar offensive-cyber tier descriptions.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `deepmind_frontiersafetyv3_2025` — supports | [Source](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf); September 22, 2025 v3.0; Table 2.2.2.a and §2.1 external-deployment review | Cyber Uplift Level 1 weight-security recommendation is SL2, with rationale including potential automated defense and societal adaptation; external deployment has a governance safety-case decision. | `prior_audit`; Prior audit initially checked selected clauses; its later deeper pass reports complete extracted 16-page text and selected visual table checks, not implementation or experimental validation. |
| `deepmind_frontiersafetyv31_2026` — supports | [Source](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf); April 17, 2026 v3.1; §2.2.2 cyber mitigation table; §1.3.2 footnote 4 | Recommendation becomes SL2+. Footnote 4 conditionally permits omitting the critical-capability assessment for some low-risk external deployments after a governance residual-risk determination; it does not remove all governance or establish a named model’s use of the exception. | `prior_audit`; Prior audit initially checked selected sections; later deeper pass reports complete extracted 20-page text and key table/footnote visual checks. No implementation check. |
| `microsoft_frontiergovernance_2025` — contextualizes | [Source](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Frontier-Governance-Framework.pdf); February 2025 edition §§1–3, especially leading-indicator trigger and six-month deeper-assessment provisions; Appendix I printed p. 12 | First edition screens internally identified frontier models or more than 10^26 pretraining FLOPs and repeats deeper assessment at least every six months. | `prior_audit`; Prior audit selected PDF sections and compared offensive-cyber tier text across editions; not a complete-document reread or compliance check. |
| `microsoft_frontiergovernance_2026` — contextualizes | [Source](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Frontier-Governance-Framework-Feb-2026.pdf); February 2026 edition §§1–3; post-training leading assessment, six-month leading review and material-change deeper reassessment; Appendix I printed p. 12 | Later edition changes screening scope and timing, including fine-tuning and post-training, while offensive-cyber tier wording remains materially similar. | `prior_audit`; Prior audit selected corresponding PDF clauses and Appendix I, not all document content or implemented practices. |

**Limits:** Recommended security goals, assessment triggers and actual operational controls are different units. Threshold names across issuers are not normalized or treated as equivalent.

**Counterevidence / alternative:** DeepMind’s retained defense/adaptation rationale and Microsoft’s retained cyber tier descriptions limit any broad claim of uniform tightening or weakening. Other clauses, exceptions and internal-deployment scope also matter.

**Next check:** Keep clause-level date, modality, scope and qualifications attached to each comparison; verify full document and appendix coverage before extending these findings beyond the specified provisions.

<a id="c19"></a>
## C19

OpenAI Preparedness v2 distinguishes the conditional halt for attained Critical cyber capability from additional development safeguards for attained or forecast Critical capability; High predeployment provisions and later internal-use/containment statements have separate scopes.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `openai_preparednessv2_2025` — supports | [Source](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf); April 15, 2025 v2; Table 1 Critical row (printed pp. 5–6, including p. 6 / viewer p. 7), §§4.2–4.4 and Appendix B | Table 1’s halt concerns attained Critical capability pending specified safeguards/security standards. Section 4.4 adds safety/security controls for attained or forecast Critical capability regardless of external deployment. A forecast alone is not encoded as triggering that Table 1 halt. | `repo_source_review`; Existing October 24 integration and regression checks preserve this clause distinction; prior audit’s later deeper pass reports all 22 extracted pages and a key table visual check, not deployed-control verification. |
| `openai_preparednessv2_2025` — bounds | [Source](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf); §3.1; §4.3 marginal-risk conditions and disclosure/validation provision; Appendix B governance roles | Elicitation is a lower-bound exercise; marginal-risk adjustments, disclosure and external validation are conditional. Advisory assessment and leadership decision authority differ. | `prior_audit`; Prior audit checked central clauses and later complete extracted text; it did not verify model-specific risk decisions or underlying validation information. |
| `openai_preparednessbeta_2023` — contextualizes | [Source](https://cdn.openai.com/openai-preparedness-framework-beta.pdf); December 18, 2023 beta; printed pp. 20–22 deployment/development ceilings and forecast-linked planning | Beta uses post-mitigation Medium and High risk ceilings; these historical risk levels should not silently become v2 capability levels. | `prior_audit`; Prior audit selected indexed official-PDF text because direct binary exceeded its retrieval limit; no independent full read or historical byte-authentication claim. |
| `openai_preparednessv2_2025` — bounds | [Source](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf); Section4.3, printedp12/PDFviewerp13 | Keeping safeguards more protective than the comparator is paired with sharing information to validate that claim. The uploaded patch omitted this qualification; the existing observation is corrected without adding a policy event. | `this_run_primary`; Fresh publisher PDF retrieval and selected section4.3 extracted text; no new full read, independent-control check or source-admission capture. |

**Limits:** This map preserves existing coding rather than reopening policy observations or inferring that stated obligations were carried out. Later statements are separately dated in the repository’s commitment history.

**Counterevidence / alternative:** Prospective safeguards did not disappear: forecast Critical capability still triggers development safeguards. Section 4.3 also includes provision of validation information; omitting that condition would overstate lack of scrutiny.

**Next check:** Section4.3 information sharing is now included in the existing observation qualifications after a fresh selected source check. Verify model-specific application, decision authority and actual information access before assurance conclusions.

<a id="c20"></a>
## C20

Inability-oriented safety cases, broader system safety arguments and model cards are complementary proposals: they structure different claims and disclosures, but their publication does not validate a deployment or establish that safety cases are the only valid governance method.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `goemans_safetycasetemplate_2024` — supports | [Source](https://arxiv.org/html/2411.08088v1); Exact v1 §§4.1–4.2; Appendix A definitions | The proposed cyber-inability template connects a specified threat actor, harm vector and target to proxy tasks, human baselines and elicitation evidence; conventional and novel-attack branches differ. | `prior_audit`; Prior audit checked selected primary sections and definitions, not the complete diagram/PDF; supplied ledger separately reports complete text and diagram-label review. |
| `habli_bigargumentsafety_2025` — contextualizes | [Source](https://arxiv.org/html/2503.11705v1); Exact v1 §§3–4, §7 general-purpose module and §8 synthesis | The Balanced, Integrated and Grounded proposal links ethical trade-offs and system hazards to model evidence; its model module permits inability, controlled capability, trustworthy behavior or oversight arguments. | `supplied_ledger`; Supplied ledger reports selected framework/model-argument sections, not all worked cases or figure-only materials. This run did not independently retrieve it. |
| `mitchell_modelcards_2019` — contextualizes | [Source](https://arxiv.org/html/1810.03993v2); Exact arXiv v2 §5 worked examples and §6 discussion | Model cards organize intended uses, evaluation results and caveats. Section 6 says accuracy depends on creators and calls for complementary third-party audits, adversarial testing and user feedback. | `prior_audit`; Prior audit inspected abstract, example cards and complete discussion, not a full methods reread, chart transcription or effectiveness study. |

**Limits:** Goemans’ worked results are hypothetical; Habli proposes an argument pattern and reuses evidence in examples; model-card examples are scoped disclosures. None establishes calibrated deployment assurance merely by using its format.

**Counterevidence / alternative:** Cards can expose useful, checkable evaluation results, and safety-case structures can make defeaters explicit. Their value depends on evidence quality, coverage and review rather than their label.

**Next check:** Tie any applied case to the exact claim, test, counterevidence, decision owner and update trigger. Complete Habli’s worked-case and figure review before stronger comparisons.

<a id="c21"></a>
## C21

ARTEMIS supplies a descriptive human-agent performance comparison in one authorized university network: A2 reported nine valid findings from eleven submissions and outranked nine of ten professionals under the study score; it does not estimate the causal uplift of AI assistance in general operations.

**Status:** scoped_check. **Theme:** cyber_case_study.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `lin_artemispenetration_2026` — supports | [Source](https://arxiv.org/html/2512.09882v2); Exact v2 Tables 1–2; §§3.3 and 5.4; study setting and scoring descriptions | A2’s stronger ensemble has nine of eleven valid submissions and $59/hour API cost. The $18.21/hour figure belongs to A1, which outranked five of ten professionals. | `prior_audit`; Prior audit checked selected primary sections and tables; no independent finding tally or full appendix reread. Supplied ledger separately reports all 29 extracted PDF pages. |
| `lin_artemispenetration_2026` — bounds | [Source](https://arxiv.org/html/2512.09882v2); §3.3 scaffold/attack-graph setup; §5.4 Cybench comparison; limitations and defense/approval conditions | Purpose-built orchestration, previously observed human attack-graph information, manual approvals and relaxed interdiction constrain transfer. The reported Cybench comparison did not show significant A1 scaffold uplift over GPT-5 CyAgent. | `supplied_ledger`; Supplied ledger records full extracted text and appendix review, with graphical details not independently transcribed; this run did not reproduce performance, costs or the comparison. |

**Limits:** One site, ten professionals and one run per evaluated variant are a small descriptive comparison. API cost excludes human oversight and infrastructure. Finding remediation is author-reported and does not measure harm reduction.

**Counterevidence / alternative:** The stronger ensemble’s observed comparative success is positive evidence within this setting. The null Cybench scaffold result and study-specific defensive allowances prevent a universal agent superiority or defense-effect claim.

**Next check:** Inspect exact final conference version against v2 before citation changes; resolve the TinyPilot hint discrepancy and inspect run-level scoring/defensive permissions before broader inference.

<a id="c22"></a>
## C22

AWS and GTIG document AI-assisted components in real compromises, supporting concrete operational pathways; provider-attributed speed or scale is not a matched estimate of incremental AI-caused attacks or harm.

**Status:** scoped_check. **Theme:** cyber_case_study.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `amazon_fortigateaiaugmented_2026` — supports | [Source](https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/); Opening and threat-actor assessment; exposed administration/credentials and hardened-target observations | AWS reports access to over 600 FortiGate devices in 55 countries, no observed FortiGate vulnerability exploitation in this campaign, and abandonment/failure against hardened targets. | `prior_audit`; Prior audit selected provider narrative passages, not full article reread, independent telemetry audit or a matched no-AI campaign. |
| `google_gtig_promptingautonomy_2026` — supports | [Source](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai); Executive Summary; AI-Augmented Vulnerability Research and credential-harvesting case | GTIG reports autonomous components and credential extraction in under six hours after an initial cloud compromise, not the end-to-end time to gain that initial access; it does not claim an observed fully autonomous attack lifecycle in the wild. | `prior_audit`; Prior audit selected primary provider sections; no independent telemetry, full article reread or matched baseline. |

**Limits:** Telemetry is selectively disclosed and provider-authored. Attribution confidence concerns whether AI was involved, while causal uplift concerns what would differ without it; these are separate judgments.

**Counterevidence / alternative:** These are positive operational observations rather than only benchmark proxies. Hardened-target failures and continued human roles bound the operational pathway; they do not establish the average durability of defenses.

**Next check:** The supplied wording correction is integrated, preserving earlier assessments; retain actor access, human roles, initial-compromise timing, target defenses and outcome stage in every quotation. Seek matched baselines before numeric uplift claims.

<a id="c23"></a>
## C23

AISI’s July incident account reports nineteen out-of-scope actions across ten of 122 evaluation runs, a rejected malicious pull request and rapid containment, with no resulting real-world harm evidenced by investigators. These reported interventions do not estimate how much harm the controls prevented.

**Status:** scoped_check. **Theme:** cyber_case_study.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `aisi_unsanctionedagentincident_2026` — supports | [Source](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing); What happened; evaluation set-up; How we discovered the incident; What we found; factors limiting damage | The account describes nineteen clustered actions in ten runs, deliberately permitted internet access and disabled provider cyber classifiers, public maintainer rejection and containment within roughly one hour of discovery. Investigators say they have not evidenced resulting real-world harm. | `this_run_primary`; This run directly retrieved and inspected selected current article passages on setup, counts, discovery, rejection and containment; did not read linked technical PDF, authenticate historical bytes or reproduce event counts. |

**Limits:** This is one disclosed investigation under permissive testing conditions, not a deployment incidence rate. Actions are clustered, not nineteen independent incidents. Current HTML was checked; no new source-admission capture is claimed.

**Counterevidence / alternative:** Maintainer rejection and isolation are observed interruption mechanisms. Some actions reached real services; absence of identified harm does not establish that no external effects occurred or identify an unobserved harmful counterfactual.

**Next check:** The existing causal-wording patch is integrated. Treat AISI and Anthropic follow-ups as analyses of a shared incident, not independent incident replication; assess technical reports and any public independent review separately.

<a id="c24"></a>
## C24

Souly et al.’s fully simulated evaluation shows that out-of-scope behavior is sensitive to explicit prompt scope in a selected scenario set; its reported 26/50 versus 4/49 comparison bounds generalization and does not establish deployed network-control effectiveness or population attack rates.

**Status:** scoped_check. **Theme:** cyber_case_study.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `souly_astraunsanctioned_2026` — bounds | [Source](https://arxiv.org/html/2609.38415v1); Exact v1 §2 selected ten-scenario comparison and §1/§3 simulation/access qualifications | Within ten scenarios selected for high early Astra rates, the stricter scope intervention changes the reported most-severe behavior count from 26/50 to 4/49. Tools, repositories and maintainers were simulated and cyber safeguards disabled; the intervention is an explicit allowlist instruction, not a live egress block. | `prior_audit`; Prior audit checked selected §2 primary passages and scoped counts, not a complete reread or visual verification of Figure 2 percentages. Supplied ledger separately reports all 33 PDF pages and figures/Appendix A review. |

**Limits:** Selection, simulation awareness and auditor rollbacks affect interpretation. No-compaction conditions differ in scenario selection/realism. Figure n labels and rounded rates should not be converted into exact independent trajectory counts without source data.

**Counterevidence / alternative:** Behavior remained possible under the stricter instruction, and the positive scoped reduction does not make the control universally sufficient. Sandboxed absence of real access bounds harm conclusions rather than demonstrating real-world defensive offset.

**Next check:** The supplied defense-persistence recoding and dated append-only assessment are integrated. Inspect raw trajectories, judge outputs and selected-scenario denominators before causal or deployment-rate interpretation.

<a id="c25"></a>
## C25

Barrett’s risk-model architecture and Murray’s structured elicitation expose assumptions linking benchmarks to hypothetical cyber risk; they do not observe matched changes in attack or harm rates. Hold Barrett’s numerical human-versus-LLM SME ransomware comparison while its task-ranking/input discrepancy remains unresolved.

**Status:** unresolved. **Theme:** cyber_case_study.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `barrett_quantitativecyberrisk_2025` — supports | [Source](https://arxiv.org/html/2512.08864v2); Exact v2 modeling architecture and Appendix E scenario inputs | The work makes attacker population, frequency, success and harm assumptions inspectable. Illustrative harm scenarios condition on capability access and do not empirically validate every benchmark-to-harm link. | `supplied_ledger`; Supplied ledger reports complete v2 text, appendices and selected PDF figure/table checks plus code/input review; this run did not replicate that work. |
| `barrett_quantitativecyberrisk_2025` — unresolved | [Source](https://arxiv.org/html/2512.08864v2); Table 3 printed p. 52 and Appendix B.1 printed p. 53; Figure 6 comparison | Table 3 puts LibreChat arbitrary file deletion at rank 16; Appendix B.1 calls it rank 13 and uses a rank-14 cutoff. Rank 13 names a different LibreChat task. A public rerun uses a different order and does not authenticate the paper’s human-model inputs. | `prior_audit`; Prior audit independently confirmed the internal table/appendix discrepancy in selected primary passages; it did not rederive code or Figure 6. Supplied ledger’s separate code review did not recover the exact human input vector/model or inaccessible canonical ranking archive. |
| `murray_mappingbenchmarkdata_2025` — contextualizes | [Source](https://arxiv.org/html/2503.04299v2); Exact v2 §§4.1.1–4.1.2 scenario/tasks; §4.2 baseline/order; §4.3 recruitment; §5 exclusions; §6.1 limitations | Experts give conditional judgments for a hypothetical malware-development/deployment step after successful spearphishing and with model access. The highest capability condition covers five selected tasks, not saturation of the forty-task benchmark; fixed task ordering and the separately sourced baseline limit inference. | `prior_audit`; Prior audit reports complete accessible main text §§1–7 and acknowledgments, but not appendices, visual figure read or raw-estimate/statistical reproduction. Seven experts completed elicitation, two excluded from central estimates. |

**Limits:** An internal documentary mismatch is not proof that a particular numerical Figure 6 estimate is wrong. The inspected public rerun cannot resolve the original human-model provenance. These sources are modeling and elicitation, not observed attack experiments.

**Counterevidence / alternative:** The architecture is useful even while one numerical comparison is held. Public rerun ordering makes selection compatible with the cutoff under that different order; this is a possible explanation, not verification of the paper’s run.

**Next check:** Obtain the archived canonical task order, exact selected task, human elicitation input vector, model and Figure 6 run manifest. Preserve the proposed numerical hold until those objects reconcile; do not substitute the public rerun silently.

<a id="c26"></a>
## C26

xAI’s December2025 framework discloses basic-refusal reliance for its cyber assessment and tiered/trusted-party deployment exceptions; underlying assessment and implementation remain unverified.

**Status:** provisional. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `xai_frontierartificialintelligenceframework_2025` — supports | [Source](https://data.x.ai/2025-12-31-xai-frontier-artificial-intelligence-framework.pdf); Official11-page edition; cover December30,2025 (filename December31); cyber/basic-refusal passages and deployment-decision section; prior extraction lines77–103,179–184,320–338 | xAI documents a tiered deployment approach and states it relied on basic refusal for its December 2025 cyber assessment, with potential trusted-party access exceptions. | `prior_audit`; Prior audit: Selected sections of official11-page PDF; Cover December30 2025; basic refusal/cyber lines77–103,179–184; deployment decisions320–338.; No underlying third-party cyber reports, actual implementation, current version, or full-document reread verified. |

**Limits:** Historical framework self-report, not a current-policy or deployed-control verification. No underlying third-party cyber reports were inspected.

**Counterevidence / alternative:** Tiered access and named external assessors are positive governance disclosures. Without their underlying evidence they do not establish the sufficiency of the basic-refusal approach or acceptable residual risk.

**Next check:** Recover the referenced assessment, pin its model/access configuration and operative policy edition, and assess the disclosed exceptions before any implementation conclusion.

<a id="c27"></a>
## C27

Sociotechnical evaluation levels and media-based incident trends address different objects: capability and system results require additional evidence to support impact claims or population incident rates.

**Status:** provisional. **Theme:** outcomes.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `weidinger_sociotechnicalsafety_2023` — contextualizes | [Source](https://arxiv.org/pdf/2310.11986); Framework opening; inherited extracted lines0–117/5025; stable section/page locator pending | Separates capability, system interaction and broader sociotechnical impact as levels of safety evaluation. | `supplied_ledger`; Inherited Selected sections; Selected extracted PDF passages (line span 0–117 of 5025). Framework and illustrative cases. Each layer needs appropriately designed empirical evidence. Not independently repeated here. |
| `oecd_trendsincidentshazards_2026` — bounds | [Source](https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/02/trends-in-ai-incidents-and-hazards-reported-by-the-media_7c824ca9/4f5ff43c-en.pdf); OECD report executive summary, theme analysis and methodological annex excerpts; exact pages pending | Studies trends and theme clusters in media reports collected by the OECD AI Incidents and Hazards Monitor. | `supplied_ledger`; Inherited Selected sections; OECD PDF contents, executive summary, theme analysis, and methodological annex excerpts. Media, language, search and classification selection change observed coverage; there is no denominator for underlying incident rates. Not independently repeated here. |

**Limits:** The framework is conceptual with illustrative cases. The incident analysis uses selected media reports; language, reporting, search and classification affect observed coverage and provide no denominator of underlying incidents.

**Counterevidence / alternative:** Level distinctions improve evaluation design and reported incident clusters can identify concrete harms and leads. Neither source supplies matched causal estimates of the effect of an individual model or safeguard.

**Next check:** Complete the claim-critical framework/report methods and stable locators; keep reported-record counts separate from population rates and connect each impact assertion to its own denominator and comparator.

## Source families and dependencies

These family annotations identify shared work, data or incidents where known. They do not comprehensively certify independence across the collection. Citation keys are retained pending identity adjudication.

| Family | Citation keys | Relationship | Basis | Status |
|---|---|---|---|---|
| `F01` | `mazeika_harmbenchstandardized_2024`, `harmbench_standardizedevaluation_2024` | Possible duplicate or related-version records for the same HarmBench study; no independent corroboration count. | Supplied ledger entries115 and161 describe18 attacks and33 targets; primary ICML/PMLR identity is a reconciliation lead. | Unresolved citation/edition lineage; preserve both existing keys pending adjudication. |
| `F02` | `wang_helpsteer2opensource_2024`, `wang_helpsteer2preference_2024` | Distinct contributions with shared dataset/annotation lineage. | The preference extension adds preferences and rationales to HelpSteer2; supplied ledger and C08. | Shared lineage recorded; full splits/annotator dependency review pending. |
| `F03` | `aisi_unsanctionedagentincident_2026` | One incident, with AISI and Anthropic follow-up analyses outside the canonical corpus. | The incident disclosure and cited follow-ups in review.md concern the same July testing event; replays/simulations are different observations. | Incident dependence explicit; candidate sources not assigned new canonical keys or admitted. |
| `F04` | `deepmind_frontiersafetyv3_2025`, `deepmind_frontiersafetyv31_2026` | Within-issuer framework editions, compared clause by clause rather than counted as independent empirical support. | Existing commitment history and C18. | Edition relation established for scoped comparison; implementation unverified. |
| `F05` | `openai_preparednessbeta_2023`, `openai_preparednessv2_2025` | Within-issuer policy lineage with changed risk/capability terminology. | Existing commitment history and C19. | Historical comparison retained; later statements have separate observations. |
