# Claim and evidence map

Generated from [claims.yaml](claims.yaml). Source identities resolve through [records.yaml](../../records.yaml); record-level inspection and limitations appear in [coverage.csv](coverage.csv). This is a provisional map of selected synthesis propositions, not a claim that the entire corpus supports them.

Assessment date: **2026-11-14**. `supplied_ledger` means inherited notes; `prior_audit` means a separate AI-assisted source check reported by the supplied audit; `this_run_primary` means scoped primary inspection reported by the project integration or a linked review round, not a recheck whenever this view is generated; `repo_source_review` means an existing dated repository review. None denotes independent human review or replication.

Status `provisional` identifies a working synthesis; `scoped_check` identifies a proposition with the stated source-level checking basis (which may be a prior audit); `unresolved` retains a material discrepancy or hold; `historical` limits a finding to its dated record. A scoped check does not verify every source claim.

## Claim index

| Claim | Theme | Status | Proposition |
|---|---|---|---|
| [C01](#c01) | evaluation_configuration | provisional | The reviewed benchmarks add distinct task, workflow and reliability measurements; each result describes its tested configuration. |
| [C02](#c02) | evaluation_configuration | scoped_check | Phuong v2 Table 23 concerns a toy safety-filter modification task in instrumental self-reasoning; its Pro-CoT easy/easy score is 0.5 despite a stated 0.7 passing criterion. |
| [C03](#c03) | evaluation_configuration | scoped_check | Rankings and apparent capability gains can change with inference budgets, attempt aggregation and task selection. |
| [C04](#c04) | evaluation_configuration | provisional | Unlearning evaluations can establish reduced performance on specified probes while leaving format sensitivity, retained knowledge and utility tradeoffs open. |
| [C05](#c05) | safeguards | provisional | Many-shot defenses show both improvements and residual scaling/utility limits under different training and evaluation conditions. |
| [C06](#c06) | safeguards | provisional | Classifier red-team results support resistance to specified attack criteria; rates across defense generations and attack protocols should remain separate. |
| [C07](#c07) | safeguards | provisional | Instruction priority, resistance to weight modification and pretraining poisoning address different attacker access and control surfaces. |
| [C08](#c08) | evaluator_integrity | provisional | HelpSteer2 and its preference extension provide useful reward-learning comparisons but share data lineage. |
| [C09](#c09) | evaluator_integrity | provisional | Position calibration improved agreement with one author-majority reference, and the highest reported agreement included human input. |
| [C10](#c10) | evaluator_integrity | scoped_check | Xu's benchmark exposure indicators are proxies, and its printed edit-similarity rule and threshold disagree with the pinned released helper. |
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
| [C28](#c28) | evaluator_integrity | scoped_check | Weak-to-strong supervision experiments demonstrate recoverable performance beyond a weak supervisor, while the amount recovered depends on task, labels and learning method; recovery is not equivalent to superhuman alignment. |
| [C29](#c29) | evaluator_integrity | scoped_check | Debate has a training strand as well as inference-time oversight results: trained debaters and debate-assisted weak supervisors can improve measured downstream judgments, with evidence exposure, ensembles and training incentives as alternative mechanisms to explicit refutation. |
| [C30](#c30) | evaluator_integrity | scoped_check | Control evaluations can compare system-level monitoring, routing and editing protocols under an explicit intentional-subversion threat model; the published APPS testbed demonstrates conditional safety/usefulness improvements without certifying deployed-model safety. |
| [C31](#c31) | evaluator_integrity | scoped_check | Reasoning-trace access and compute choices can improve measured monitoring performance, while monitorability is a relation between agent, monitor, observation scope and endpoint rather than a general guarantee of faithful reasoning or harm prevention. |
| [C32](#c32) | evaluator_integrity | scoped_check | Judge accuracy and an agent’s incentive to advocate truth are different evaluation targets; a protocol can improve one without establishing the other. |
| [C33](#c33) | safeguards | scoped_check | Standardized jailbreak evaluations can improve comparability through explicit behaviors, judges, attack adaptation and resource accounting; their remaining limits do not erase this methodological progress. |
| [C34](#c34) | safeguards | scoped_check | Adversarial training and recovery-data interventions provide positive model-level defense results under specified tests, with attack-diversity and utility-comparator limits that constrain generalization. |
| [C35](#c35) | outcomes | scoped_check | Inexact-unlearning evaluation needs per-example and retained-data privacy checks: average-case forgetting or weak membership tests can hide remaining or displaced privacy leakage. |
| [C36](#c36) | safeguards | scoped_check | CyberSecEval2 supports configured prompt-injection and malicious-code-compliance findings, while its inconsistent prompt-injection summaries and nonexecuted interpreter tests rule out a single unqualified headline range or sandbox-escape rate. |
| [C38](#c38) | governance | provisional | Audit access is a set of enabling conditions: usable model interfaces, model and process information, evaluator time and resources affect which claims can be tested. A label such as external evaluator or white-box access does not establish adequate evaluation. |
| [C39](#c39) | governance | provisional | The accountability value of an audit depends on its institutional design, including scope, auditor selection and payment, access and legal protection, professional standards, follow-up and disclosure. Restricted public disclosure with fuller regulator access is one proposed pathway, rather than proof that maximum public transparency is always best. |
| [C40](#c40) | governance | provisional | Legal protection for good-faith research and protection against technical exclusion address different barriers to external evaluation. The safe-harbor proposal links them to disclosure rules, independent access review and appeals; it does not show that legal language alone supplies access or improves safety. |
| [C41](#c41) | governance | provisional | Internal lifecycle audits and external scrutiny can play complementary roles. Internal access and documentary records can support prospective testing, remediation and deployment decisions, while external challenge can test organizational priorities and omissions; neither role is validated merely by producing an audit report. |
| [C43](#c43) | evaluation_configuration | scoped_check | Cost-controlled agent comparisons can both overturn apparent architecture gains and improve usable designs; the relevant comparison depends on whether the decision concerns model science or downstream use. |
| [C44](#c44) | governance | scoped_check | Dataset documentation can make intended use, sampling, provenance and maintenance inspectable through a reflective workflow; automated metadata completion is not equivalent to that proposed process or proof of representative data. |
| [C45](#c45) | outcomes | scoped_check | Layered model, red-team and human field testing can expose different application-validity problems and user perceptions; the ARIA pilot demonstrates an implemented method, not a calibrated cross-application safety ranking or a measured reduction in harms. |
| [C46](#c46) | evaluation_configuration | scoped_check | Standardized multi-metric evaluation can produce useful common comparisons and reveal tradeoffs while explicitly restricting the measured subspace; broad coverage should remain distinct from deployment validity. |
| [C47](#c47) | evaluator_integrity | scoped_check | Historical trustworthiness evaluations show both standard-condition improvements and metric/access-specific reversals; higher average accuracy alone does not fix fairness or robustness under an altered threat model. |

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

**Status:** scoped_check. **Theme:** evaluation_configuration.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `wijk_rebench_2025` — supports | [Source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wijk25a/wijk25a.pdf); Final ICML 2025 proceedings: Figure 2 printed p. 3; §§ 3.2–3.3 pp. 5–6; Appendix A.1 p. 14; A.2 pp. 15–16 | Final paper confirms best-of-k resampling and human 32-hour result as best of four 8-hour attempts. Human participants could use LLMs and other tools; agents and expert workflows are compared under wall-clock budgets, not a no-AI human counterfactual. | `this_run_primary`; Selected exact final PDF methods/results/appendix passages and Figure 2 visual check; not all 61 pages or experimental reproduction.; review events: [r2_claimchecks_01](rounds.md#r2_claimchecks_01), [r2_claimchecks_02](rounds.md#r2_claimchecks_02) |
| `folkerts_measuringaiagentscyber_2026` — bounds | [Source](https://arxiv.org/pdf/2603.11214v3); v3 Table 1; Appendix E Table 2; § 3.2 | Higher budgets improve some tested models, but 10M-token results are not monotonically ordered by model release. One inherited recomputation reports 9.6 versus the paper's 9.8 for one appendix-derived cell. | `supplied_ledger`; Inherited full text description: All 30 PDF pages of v3: §§ 1–6, references, Appendices A–E, rendered Figures 1–7, and programmatic verification of all 24 end-to-end summary cells from 1,263 parsed appendix run rows.; not independently repeated in this integration. |

**Limits:** RE-Bench’s32-hour point aggregates attempts rather than one continuous32-hour run. The exact final proceedings PDF has now been retrieved and its relevant methods checked, but remaining appendices/run-level data were not fully reviewed. Experts could use LLMs/tools; human-source heterogeneity and best-observed allocation matter. Folkerts’ single-cell discrepancy remains a separate lead.

**Counterevidence / alternative:** The benchmarks show useful task performance, budget sensitivity and some agent strengths. RE-Bench also notes that lower agent cost and different workflows could make agents economically competitive despite a longer-time score disadvantage; time-matched results do not settle economic automation or causal AI assistance.

**Next check:** Use final-publication locators and aggregate-attempt/comparator qualifications. Omit broad long-horizon/no-AI uplift extrapolations. Complete run-level reproduction or other appendices only if needed by a leading claim; separately resolve or omit the Folkerts cell.

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

**Next check:** Complete the final-version methods and compare each probe with its own base/fine-tuned controls before inferring operational risk reduction or permanent erasure. The related Hayes preprint in C35 adds per-example and retained-data privacy outcomes; it does not authenticate the final SaTML edition.

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

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `xu_benchmarkingleakage_2024` — supports | [Source](https://arxiv.org/html/2404.18824v1); arXiv v1§§ 3.2–3.3,4,5.3; Appendix A.3 Eq5; pinned metric_utils.py lines23–28,40–48; same-revision README Examples paragraph | The formula orientation and >.9 versus >.75 threshold mismatch survive a fresh paper/helper check; pinned README also states >.9. The helper preserves preexisting scores and its main loop is not a complete experiment manifest. | `this_run_primary`; Selected primary paper sections; complete75-line pinned helper and completeREADME text, excluding linked media. No 186-row recomputation or model experiment reproduced.; review events: [r2_claimchecks_05](rounds.md#r2_claimchecks_05), [r2_claimchecks_06](rounds.md#r2_claimchecks_06), [r2_claimchecks_07](rounds.md#r2_claimchecks_07) |

**Limits:** The documentary mismatch is confirmed, but does not identify the code revision or threshold used for every reported experiment. Original/paraphrase familiarity remains an exposure proxy; controlled intentional exposure and exact-match observations do not authenticate each observationally flagged training item.

**Counterevidence / alternative:** Exact string matches and controlled exposure experiments establish proxy behavior; they do not turn each flagged item into a verified leaked training record.

**Next check:** Omit affected lenient edit-similarity leakage rates from leading publication claims. Retain the confirmed documentary discrepancy and scoped proxy findings; pursue an experiment manifest only if those rates become necessary.

<a id="c11"></a>
## C11

Debate can improve inference-time judge accuracy under information asymmetry, while comparison with direct QA depends on task and source access.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `khan_debatingmorepersuasive_2024` — supports | [Source](https://arxiv.org/html/2402.06782v4); v4 abstract and §3 main results; §2 task setup | On filtered binary QuALITY questions, reported LLM/human debate accuracy is 76%/88%, compared with 48%/60% naive and 54%/78% assigned consultancy. | `this_run_primary`; Selected primary abstract/main results and task-setup text checked; no full appendix/human-sampling audit or numerical reproduction. |
| `kenton_scalableoversightweak_2024` — bounds | [Source](https://arxiv.org/html/2407.04622v2); v2 §§3.2,4.1; Figure 2 accompanying prose | Full-article direct QA performs best across tested extractive judge configurations; debate's gains over QA without the article vary by judge/task. | `this_run_primary`; Selected primary protocol definitions, main results and figure-caption prose; no complete reread or statistical recomputation. |

**Limits:** Khan's naive human baseline used a separate experiment and its full-source human comparison is external, as recorded in the supplied ledger. These studies test inference properties, not a complete training protocol. This inference-time comparison is one strand of the corpus; C29 separately assesses debate-training and debate-assisted supervision results.

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

**Next check:** Separate evidence retrieval/verification, correctness-conditioned error detection and judge training effects in any follow-up comparison. Compare the new training and incentive-proxy evidence in C29 and C32 rather than assuming all debate studies share one target.

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

**Next check:** Finish claim-critical appendices/final versions, reconcile inconsistent awareness/refusal figures, and test alternative explanations before inferring motives or deployment rates. Include the affirmative protocol and monitoring evidence in C30–C31 when assessing what this strand establishes.

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
| `lin_artemispenetration_2026` — supports | [Source](https://arxiv.org/html/2512.09882v2); arXiv v2 Table 1 printed p. 2; § 5.4 costs printed p. 8 | A2’s stronger ensemble has nine of eleven valid submissions and $59/hour API cost. The $18.21/hour figure belongs to A1, which outranked five of ten professionals. | `this_run_primary`; Fresh selected exact v2 PDF abstract/Table 1/cost text;9/11rounding check only, no independent finding tally or full reread.; review events: [r2_claimchecks_03](rounds.md#r2_claimchecks_03) |
| `lin_artemispenetration_2026` — bounds | [Source](https://arxiv.org/html/2512.09882v2); arXiv v2§ 3.3 Benchmarks and Table 2 printed p. 5; Appendix E opening p. 22; § 7 limitations pp. 8–9 | Purpose-built orchestration, previously observed human attack-graph information, manual approvals and relaxed interdiction constrain transfer. The reported Cybench comparison did not show significant A1 scaffold uplift over GPT-5 CyAgent. | `this_run_primary`; Fresh selectedv2 PDF benchmark/scaffold/limitation passages and Appendix E opening; not the full appendix or run-level scoring. OpenReview final access failed.; review events: [r2_claimchecks_03](rounds.md#r2_claimchecks_03), [r2_claimchecks_04](rounds.md#r2_claimchecks_04) |

**Limits:** One site, ten professionals and one evaluated run per variant form a small descriptive comparison. API cost excludes oversight/infrastructure. Conference-final equivalence remains unverified after OpenReview 403/challenge. V2Table 3 and§ 6 disagree on TinyPilot successful hint levels, so that specific detail is omitted.

**Counterevidence / alternative:** The stronger ensemble’s observed comparative success is positive evidence within this setting. The null Cybench scaffold result and study-specific defensive allowances prevent a universal agent superiority or defense-effect claim.

**Next check:** Retain the v2 comparison with correctedTable 2/§ 3.3 and§ 5.4 locators. Omit TinyPilot hint-level claims until source data or authenticated later text resolves the inconsistency; retain final-version access as a bounded publication-metadata task.

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

<a id="c28"></a>
## C28

Weak-to-strong supervision experiments demonstrate recoverable performance beyond a weak supervisor, while the amount recovered depends on task, labels and learning method; recovery is not equivalent to superhuman alignment.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `burns_weakstronggeneralization_2024` — supports | [Source](https://arxiv.org/pdf/2312.09390v1); arXiv v1 §§3–4.3, 5.1, 6.1 | Weak-label training can elicit stronger performance; NLP, chess and reward-modeling results differ, and no tested method works universally. | `this_run_primary`; Selected primary preprint text: pp 1–10 abstract/introduction/related work, methodology and main results; §5.1 pp 11–12 overfitting text; §6.1–6.2 pp 16–18 disanalogies/future-work text. Remaining methods/results pages and appendices were not completely read. Large49-page preprint only selected sections; not final ICML verification, complete appendix read, graph transcription or replication. PDF extraction reported a recoverable xref warning; inspected text is coherent, but complete extraction fidelity was not certified.; review events: [r2_oversight_04](rounds.md#r2_oversight_04) |
| `lang_debatehelpsweak_2025` — contextualizes | [Source](https://arxiv.org/pdf/2501.13124v1); Methods; Table 2; Limitations | Improved weak supervision via debate ensembles raises subsequent student accuracy on four converted binary NLP tasks under a small 7B/14B gap. | `this_run_primary`; Selected introduction/related-work distinction, complete methods/setup and main-results/ablation/limitations text, including Tables 1–5 and Figure 2–3 captions. Final references and any final-AAAI-version differences were not completely checked. No complete-document reread, final venue authentication, plot digitization, significance/raw-run verification or replication. The converted binary tasks and model/compute gap constrain transfer.; review events: [r2_oversight_03](rounds.md#r2_oversight_03) |

**Limits:** Burns was read as a related original preprint, not authenticated final proceedings text. Both studies use task labels/representations that may be easier to elicit than future latent capabilities; downstream RL robustness remains open.

**Counterevidence / alternative:** Reward-model recovery is poor for naive transfer; confidence loss can worsen small-gap cases, while bootstrapping helps chess but not all task families. These nulls bound the positive recovery finding rather than erase it.

**Next check:** Verify final Burns proceedings and complete claim-critical appendices; examine optimization against the learned reward model before treating classifier accuracy as an alignment solution.

<a id="c29"></a>
## C29

Debate has a training strand as well as inference-time oversight results: trained debaters and debate-assisted weak supervisors can improve measured downstream judgments, with evidence exposure, ensembles and training incentives as alternative mechanisms to explicit refutation.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `arnesen_trainingwindebates_2024` — supports | [Source](https://arxiv.org/pdf/2409.16636v1); §§3–4.2; §4.3; §5.2; Appendices B,D,G | Self-play DPO-trained debaters improve a fixed calibrated judge’s measured accuracy; double consultancy closes much of the gap and one-turn evidence does not support a simple refutation explanation. | `this_run_primary`; Complete main text §§1–6, printed pp 1–10; acknowledgments/references inspected in the extraction; Appendices A–G, printed pp 16–23, plus H opening/evaluation prompt on p 24. The rest of H and sample transcriptsI pp 31–48 were not read. No full 48-page read, remaining prompt/transcript appendix read, chart transcription, significance recomputation or experiment replication. Main text and captions were checked; graph values were not independently digitized.; review events: [r2_oversight_02](rounds.md#r2_oversight_02) |
| `lang_debatehelpsweak_2025` — supports | [Source](https://arxiv.org/pdf/2501.13124v1); Methods; Tables 2, 4, 5; turn and ensemble ablations | Debate-generated information trains an improved weak supervisor; extra ensemble/sampling compute and a weak single-turn comparator are part of the result. | `this_run_primary`; Selected introduction/related-work distinction, complete methods/setup and main-results/ablation/limitations text, including Tables 1–5 and Figure 2–3 captions. Final references and any final-AAAI-version differences were not completely checked. No complete-document reread, final venue authentication, plot digitization, significance/raw-run verification or replication. The converted binary tasks and model/compute gap constrain transfer.; review events: [r2_oversight_03](rounds.md#r2_oversight_03) |

**Limits:** Arnesen uses information-asymmetric QuALITY reading comprehension, prior human/GPT training transcripts and a fine-tuned judge. Lang uses four converted binary tasks with a modest model-size gap. Neither establishes broad training scalability or independent source-family replication.

**Counterevidence / alternative:** Double/ensembled consultancy, one-turn results, cost differences and null turn-length gains qualify a blanket debate advantage. The whole Arnesen pipeline is not ground-truth-free because its judge/SFT stages use prior labeled data.

**Next check:** Keep C11’s inference-time scope for Khan/Kenton but add this distinct training strand. Omit leading numerical estimates unless final versions, uncertainty and budget matching are checked.

<a id="c30"></a>
## C30

Control evaluations can compare system-level monitoring, routing and editing protocols under an explicit intentional-subversion threat model; the published APPS testbed demonstrates conditional safety/usefulness improvements without certifying deployed-model safety.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `greenblatt_controlimprovingsafety_2024` — supports | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/greenblatt24a/greenblatt24a.pdf); ICML proceedings §§2–3; Table 1; §5; Appendix K and Table 5 | Trusted editing and untrusted monitoring with safeguards improve the studied frontier over simpler protocols, conditional on its auditor, attack-policy and simulated-scenario assumptions. | `this_run_primary`; Published primary main text §§1–6, printed pp 1–9, including Table 1 and figure captions; Appendix K sampling/uncertainty text pp 22–23 and selected Appendix L/M protocol details/Table 5 pp 23–25. Other appendices/examples not fully read. No full 42-page read, remaining detailed red-team prompts/example investigation, raw simulations or replication. The observed HTTP MIME was application/octet-stream; PDF type was verified from%PDF bytes and pdfinfo. Publisher raw URL is mutable; local bytes/hash identify the inspected edition.; review events: [r2_oversight_05](rounds.md#r2_oversight_05) |

**Limits:** Safety is a simulated probability of no submitted backdoor across5000 problems; usefulness is rescaled between model baselines. High-quality trusted auditing labor is simulated with GPT-4, while the weaker trusted model is GPT-3.5, the backdoor definition privileges the auditor, attacks are constrained, and1500 observed problem interactions are resampled without a held-out test split.

**Counterevidence / alternative:** Attack-policy collusion and subtle-backdoor results show that simple upfront or trusted-only monitoring can fail. Conversely, the measured protocol improvements are positive system-level results, so a claim that the corpus offers only model benchmarks would omit useful evidence.

**Next check:** Carry exact metrics, threat model and sampling/auditor assumptions in applied claims; test held-out tasks and stronger auditors/attack policies before extrapolating the numerical safety rates.

<a id="c31"></a>
## C31

Reasoning-trace access and compute choices can improve measured monitoring performance, while monitorability is a relation between agent, monitor, observation scope and endpoint rather than a general guarantee of faithful reasoning or harm prevention.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `openai_monitoringmonitorability_2025` — supports | [Source](https://arxiv.org/pdf/2512.18311v1); §§2.1–2.2, 3.3, 4–7, 9 | The suite finds positive CoT-versus-action and monitor-compute effects, with cost, model-family, label/filter and follow-up failure conditions. | `this_run_primary`; Selected90-page primary PDF: pp 1–3 and5–8 conceptual/metric/scope definitions; pp 15–26 outcome-label limitations and §§4–9 results/scaling/follow-ups/discussion, including captions. Detailed intervention estimators and appendicesA–J not comprehensively read. No full 90-page read, complete appendix, figure digitization, raw metric or experimental reproduction. Agent-vs-monitor comparisons use OpenAI monitors; filters/data differ across plots and only tool-free environments are used for some external-model comparisons.; review events: [r2_oversight_07](rounds.md#r2_oversight_07) |
| `korbak_chainthoughtmonitorability_2025` — contextualizes | [Source](https://arxiv.org/pdf/2507.11473v2); §§1–5 | The conceptual agenda distinguishes necessity from propensity and permits alignment/monitorability tradeoffs; it does not contribute another independent empirical effect. | `this_run_primary`; All 11 PDF pages of accessible extracted text read: §§1–6, Figure 1 caption and references. No separately linked source papers/interactives were read for this event. This is a position/research-agenda paper that synthesizes cited experiments, not a new primary monitoring-effect trial. Architecture diagram was read through caption/text, not independently visually evaluated; references are not audited by reading their citation strings.; review events: [r2_oversight_06](rounds.md#r2_oversight_06) |

**Limits:** Only selected parts of the 90-page empirical report were checked. Non-intervention g-mean² is TPR×TNR; the intervention variant needs separate estimator review. These measures do not determine low-prevalence positive predictive value; some target labels are model-judged and some ambiguous outputs are filtered. Two ordinary RL runs cannot establish a universal scaling trend.

**Counterevidence / alternative:** Direct obfuscation reduces monitorability, but ordinary RL does not consistently reduce its mean in the tested runs. Follow-ups help some settings but can degrade subtle-framing cases; preserving all current CoT behavior can conflict with useful safety training.

**Next check:** For any deployment-leading number, inspect estimators, per-environment filters, operating-point calibration, latency and adaptive evasion. Qualitative channel/compute evidence can enter the synthesis now.

<a id="c32"></a>
## C32

Judge accuracy and an agent’s incentive to advocate truth are different evaluation targets; a protocol can improve one without establishing the other.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `sudhir_benchmarkscalableoversight_2025` — supports | [Source](https://arxiv.org/pdf/2504.03731v1); §§2–3.1; §4; Table 1; §5 | ASD compares rewards across prompted true/false advocacy and differs from raw judge accuracy for consultancy. The demonstrative comparison is based on 100 math questions and one judge, with simplified protocol proxies. | `this_run_primary`; All 15 PDF pages of accessible extracted text read: main §§1–5, captions, Table 1, references, and Appendices A–D including setup, pseudocode and prompts. Linked code was not inspected. Plot coordinates/error bars were not digitized and linked implementation was not inspected. Printed pseudocode duplicates agent_response rather than appending adversary_response; whether this is only a documentation error is unresolved and no implementation-error conclusion is drawn.; review events: [r2_oversight_01](rounds.md#r2_oversight_01) |
| `arnesen_trainingwindebates_2024` — contextualizes | [Source](https://arxiv.org/pdf/2409.16636v1); §4.3 and Appendix G | Evidence exposure and the training objective, rather than observed multi-turn refutation alone, explain competing interpretations of better judge accuracy. | `this_run_primary`; Complete main text §§1–6, printed pp 1–10; acknowledgments/references inspected in the extraction; Appendices A–G, printed pp 16–23, plus H opening/evaluation prompt on p 24. The rest of H and sample transcriptsI pp 31–48 were not read. No full 48-page read, remaining prompt/transcript appendix read, chart transcription, significance recomputation or experiment replication. Main text and captions were checked; graph values were not independently digitized.; review events: [r2_oversight_02](rounds.md#r2_oversight_02) |

**Limits:** ASD is an empirical proposed proxy based on instructed model behavior and known truth, not a formal guarantee of incentive compatibility. Average scores and extrapolated capability trends do not establish worst-case safety.

**Counterevidence / alternative:** Debate’s positive scoped average results survive the metric distinction. Stronger consultancy baselines and grounded evidence can improve accuracy even when an adversarial-incentive argument remains unproven.

**Next check:** Specify whether the applied research target is answer accuracy, relative truthful reward, learned policy behavior, or worst-case harmful failure; retain separate endpoints rather than declare one proxy the sole definition of oversight quality.

<a id="c33"></a>
## C33

Standardized jailbreak evaluations can improve comparability through explicit behaviors, judges, attack adaptation and resource accounting; their remaining limits do not erase this methodological progress.

**Status:** scoped_check. **Theme:** safeguards.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `chao_jailbreakbenchopen_2024` — supports | [Source](https://arxiv.org/pdf/2404.01318v5); §§3.1,3.4–3.7; §4 Tables1–3; AppendicesB–E; data cardI.5.2 | JBB provides artifacts, standardized configurations, judge comparison and matched benign behaviors; its defense tables explicitly use nonadaptive transferred prompts and its data card warns against existing-attack-only robustness conclusions. | `this_run_primary`; All25pages of retained v5 accessible text read; no benchmark execution or plot digitization.; review events: [r2_safeguards_01](rounds.md#r2_safeguards_01) |
| `pavlova_automatedredteaming_2024` — contextualizes | [Source](https://arxiv.org/html/2410.01606v1); §§4–5 success metric, budget and Crescendo comparison | GOAT holds attacker and target-call budget fixed against a Crescendo reimplementation, while using JBB behaviors/judge and cumulative best-of-k success. | `this_run_primary`; Selected setup/results only; shared dataset/judge is not independent replication.; review events: [r2_safeguards_06](rounds.md#r2_safeguards_06) |

**Limits:** Standardized within-benchmark comparisons do not make different threat models or benchmarks interchangeable. Judge reference labels, hidden initialization costs, model revisions and adaptation still matter.

**Counterevidence / alternative:** JBB itself shows defensive reductions against transfer attacks and residual successes; adaptation may change rankings. Its100 benign behaviors are only a sanity check, not a complete utility evaluation.

**Next check:** Pin artifact/model/judge versions and test defense-aware attacks. Record JBB/HarmBench/GOAT behavior and judge lineage before aggregating evidence.

<a id="c34"></a>
## C34

Adversarial training and recovery-data interventions provide positive model-level defense results under specified tests, with attack-diversity and utility-comparator limits that constrain generalization.

**Status:** scoped_check. **Theme:** safeguards.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `mazeika_harmbenchstandardized_2024` — supports | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/mazeika24a/mazeika24a.pdf); ICML/PMLR final §5.2; AppendixA.1; Table12 p33 | R2D2 improves tested robustness, with weaker gains on attacks unlike its training adversary; Table12 explicitly notes that the ZephyrBeta comparator includes DPO whereas R2D2 does not. | `this_run_primary`; Selected final-PDF methods/results/appendix/table text; related edition of canonical arXiv work; no full44page read or experimental reproduction.; review events: [r2_safeguards_02](rounds.md#r2_safeguards_02) |
| `qi_safetyalignmentshould_2025` — supports | [Source](https://arxiv.org/html/2406.05946v1); §§3.1–3.2/Table2; AppendixA.4/C | Recovery augmentation improves tested prefill/jailbreak endpoints while AlpacaEval is somewhat lower; constrained later fine-tuning is a distinct intervention, and combined methods are not consistently better. | `this_run_primary`; Selected v1 results/aggregation/ablation discussion; ICLR final inaccessible in this round.; review events: [r2_safeguards_07](rounds.md#r2_safeguards_07) |

**Limits:** These are scoped7B-model experiments with automatic behavioral judges. Neither a mismatched training comparator nor a limited benign benchmark establishes zero utility cost or broad deployed security.

**Counterevidence / alternative:** HarmBench finds no model uniformly robust; cross-attack generalization is weaker away from the train-time adversary. Qi reports residual vulnerability, regularization/optimizer dependence and non-monotonic combined-method benefit.

**Next check:** Retain affirmative gains without pooling ASRs. Match attack budgets, training pipelines and utility baselines, and verify final-version equivalence before headline numbers.

<a id="c35"></a>
## C35

Inexact-unlearning evaluation needs per-example and retained-data privacy checks: average-case forgetting or weak membership tests can hide remaining or displaced privacy leakage.

**Status:** scoped_check. **Theme:** outcomes.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `hayes_inexactunlearningneeds_2024` — supports | [Source](https://arxiv.org/pdf/2403.01218v3); §§1,3.1–3.3,4.4 and5; pp6–8,13–15 | The related preprint distinguishes per-example from population U-MIA and reports heterogeneous forget-example outcomes and worsened privacy for some retained examples; its PaLM2 setting is constructed fine-tuning, not complete pretraining erasure. | `this_run_primary`; Selected preprint methods/results only; final SaTML edition not authenticated and no37page full read.; review events: [r2_safeguards_05](rounds.md#r2_safeguards_05) |

**Limits:** The audit adversary assumes training/data access and many shadow models. Source findings are version-limited and do not establish that all unlearning or exact-retraining schemes fail.

**Counterevidence / alternative:** Some examples become less distinguishable after unlearning, and exact methods offer a different guarantee/cost tradeoff. Strong audit leakage does not directly estimate practical attacker prevalence.

**Next check:** Replace inherited “user-level” shorthand with per-example U-MIA. Review exact SaTML final and appendices before quantitative claims; preserve the distinction from hazardous-capability probe forgetting.

<a id="c36"></a>
## C36

CyberSecEval2 supports configured prompt-injection and malicious-code-compliance findings, while its inconsistent prompt-injection summaries and nonexecuted interpreter tests rule out a single unqualified headline range or sandbox-escape rate.

**Status:** scoped_check. **Theme:** safeguards.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `bhatt_cyberseceval2wide_2024` — supports | [Source](https://arxiv.org/pdf/2404.13161v1); Abstract/introduction; §§4.1,4.3,5.2,5.4,6; Figure3 p12 | Prompt-injection prose ranges disagree; interpreter evaluation judges500 generated responses acrossfive abuse categories without executing them. False refusal separately probes benign cybersecurity utility. | `this_run_primary`; Selected v1 methods/results plus direct visual page12 Figure3 check; no raw-result reconstruction.; review events: [r2_safeguards_04](rounds.md#r2_safeguards_04) |

**Limits:** Figure3 does not by itself reconcile exact aggregation or source revisions. Iterative/multi-turn/optimization attacks are excluded, API safety defaults vary, and automatic response judging is not execution.

**Counterevidence / alternative:** The benchmark still provides concrete failure observations and a usable false-refusal design. Withholding the disputed range does not invalidate those narrower results.

**Next check:** Omit the affected headline number and continue the synthesis. Use only exact model/variant results after released-data/aggregation reconciliation; do not relabel compliance as escape success.

<a id="c38"></a>
## C38

Audit access is a set of enabling conditions: usable model interfaces, model and process information, evaluator time and resources affect which claims can be tested. A label such as external evaluator or white-box access does not establish adequate evaluation.

**Status:** provisional. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `charnock_expandingexternalaccess_2026` — supports | [Source](https://arxiv.org/pdf/2601.11916v1); v1 §§2–3.4, Tables1–2; §5 | The proposed taxonomy separates model access, information and timeframe and explains their interactions, possible false-positive and false-negative benefits, and security/capacity burdens. | `this_run_primary`; All accessible text of the 20-page arXiv v1 PDF: introduction, §§2–5, Tables 1–5 and references. This is a text reading of the identified PDF, not an audit of cited primary studies or current Code obligations.; review events: [r2_institutions_01](rounds.md#r2_institutions_01) |
| `casper_blackboxaccessaudits_2024` — supports | [Source](https://arxiv.org/pdf/2401.14446v3); arXiv v3 §§2.1,5–7; AppendixD | Access to internals and process information enables techniques unavailable from output-only queries; resources, scope, incentives and representation remain additional conditions. | `this_run_primary`; Selected arXiv v3: §2.1 and Table 1 access definitions; portions of §§3–4.1 reviewing access-enabled testing; §§5–7 on outside-the-box information, security and discussion; Appendix D in full. Not the complete paper or all technical appendices/references.; review events: [r2_institutions_02](rounds.md#r2_institutions_02) |

**Limits:** These are methodological and institutional arguments, not a controlled estimate of better safety outcomes. Charnock’s AL1–AL3 and Code interpretation are proposals; Casper’s ACM-final equivalence was not established in this round.

**Counterevidence / alternative:** Black-box tests can still reveal consequential failures; deeper access adds security and capacity burdens and may be unhelpful without time or relevant information. Shared author and citation lineage do not supply independent experimental corroboration.

**Next check:** Compare concrete evaluation agreements, interfaces, information, time and resources against the publication claim being tested. Avoid an unconditional access ranking.

<a id="c39"></a>
## C39

The accountability value of an audit depends on its institutional design, including scope, auditor selection and payment, access and legal protection, professional standards, follow-up and disclosure. Restricted public disclosure with fuller regulator access is one proposed pathway, rather than proof that maximum public transparency is always best.

**Status:** provisional. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `raji_outsideroversight_2022` — supports | [Source](https://dho.stanford.edu/wp-content/uploads/Outsider_Oversight.pdf); §§3–4.5.2 and §5; mainFigure1 printedp561 | The cross-sector review identifies five design dimensions, mixed evidence for some arrangements, interactions among them, and a registered-report/limited-disclosure proposal. | `this_run_primary`; All accessible text of the 15-page published-format PDF, printed pp557–571: §§1–6, references, Appendix Tables1–2, plus visual inspection of the main audit matrix and the disputed appendix rows.; review events: [r2_institutions_03](rounds.md#r2_institutions_03) |
| `casper_blackboxaccessaudits_2024` — contextualizes | [Source](https://arxiv.org/pdf/2401.14446v3); arXiv v3 AppendixD | The authors identify conflicts, constrained resources, narrow scope, excluded viewpoints and capture as failure modes beyond technical access. | `this_run_primary`; Selected arXiv v3: §2.1 and Table 1 access definitions; portions of §§3–4.1 reviewing access-enabled testing; §§5–7 on outside-the-box information, security and discussion; Appendix D in full. Not the complete paper or all technical appendices/references.; review events: [r2_institutions_02](rounds.md#r2_institutions_02) |

**Limits:** Cross-industry analogies and proposed arrangements do not measure present frontier-AI audit effectiveness. Outsider Oversight’s AppendixTable2 appears to swap FDAFAERS and FCCTCB descriptions; those two program examples are omitted from this inference pending primary verification.

**Counterevidence / alternative:** Internal audits retain useful access and preventive functions; independence can trade off with expertise, and formal licensing or disclosure can produce exclusion, cost or box-ticking. The five design dimensions are not validated as a universal scoring formula.

**Next check:** For applied cases, record who selected/paid the assessor, what could be tested, who received the findings and who acted on them. Verify affected FDA/FCC program descriptions before reuse.

<a id="c40"></a>
## C40

Legal protection for good-faith research and protection against technical exclusion address different barriers to external evaluation. The safe-harbor proposal links them to disclosure rules, independent access review and appeals; it does not show that legal language alone supplies access or improves safety.

**Status:** provisional. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `longpre_safeharbor_2024` — supports | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/longpre24a/longpre24a.pdf); PMLR 2024 Table1, §4, Figure1 and §§4.1–4.2, PDFpp6–9 | The authors distinguish civil legal protection from account-suspension protections, propose conditional researcher and company commitments, and describe third-party review/appeal mechanisms. | `this_run_primary`; PMLR published PDF pp1–4 (abstract, introduction, definitions/Table1 and researcher-experience discussion/Table2), the sampling-qualification paragraph at the beginning of p5, plus §4, §§4.1–4.2 and Figure1 text on PDFpp6–9. Remaining company-policy text/Table3 and later sections/appendices were not read in full.; review events: [r2_institutions_04](rounds.md#r2_institutions_04) |

**Limits:** The paper is a position argument informed by nonrepresentative informal experience. Its 2024 company/legal snapshot has not been revalidated as current law; company promises do not remove criminal liability or create unrestricted research rights.

**Counterevidence / alternative:** Trusted intermediaries and preregistration may narrow participation, preserve company gatekeeping or exclude critical groups. Technical exemptions can add misuse and administration costs; this round did not measure the proposed trade-offs.

**Next check:** Read the implementation appendices and obtain dated operative policy/legal evidence before claiming current protection, participation change or safety effects.

<a id="c41"></a>
## C41

Internal lifecycle audits and external scrutiny can play complementary roles. Internal access and documentary records can support prospective testing, remediation and deployment decisions, while external challenge can test organizational priorities and omissions; neither role is validated merely by producing an audit report.

**Status:** provisional. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `raji_closingaccountabilitygap_2020` — supports | [Source](https://arxiv.org/pdf/2001.00973v1); v1 §2.4, §§4.1–4.6, Figures1–2 and §5 | The proposed SMACTR workflow connects development-stage artifacts and testing to reflection and post-audit action, while acknowledging internal organizational interests and wider checks and balances. | `this_run_primary`; All accessible text of the 12-page arXiv v1 PDF: §§1–6, references and both hypothetical CompanyX examples. Figures1–2 were also rendered and visually inspected. Linked supplementary worked templates were not retrieved/read.; review events: [r2_institutions_05](rounds.md#r2_institutions_05) |
| `raji_outsideroversight_2022` — contextualizes | [Source](https://dho.stanford.edu/wp-content/uploads/Outsider_Oversight.pdf); §5 Limitations; §§4.2–4.5 | The authors explicitly preserve the value of internal audits and argue against relying on them alone; design arrangements shape whether external review adds accountability. | `this_run_primary`; All accessible text of the 15-page published-format PDF, printed pp557–571: §§1–6, references, Appendix Tables1–2, plus visual inspection of the main audit matrix and the disputed appendix rows.; review events: [r2_institutions_03](rounds.md#r2_institutions_03) |

**Limits:** SMACTR’s two CompanyX cases are hypothetical, not an implementation or harm-reduction study. The sources share an author and scholarly lineage; they are complementary arguments rather than independent outcome replications.

**Counterevidence / alternative:** Internal processes can miss affected populations or translate company principles into self-serving criteria; external reviewers can lack data, resources or practical leverage. Lifecycle documentation can become box-ticking if no one owns mitigation and follow-up.

**Next check:** Look for actual audit records, affected-stakeholder participation, decision authority, completed mitigation and response to external challenge before claiming effectiveness.

<a id="c43"></a>
## C43

Cost-controlled agent comparisons can both overturn apparent architecture gains and improve usable designs; the relevant comparison depends on whether the decision concerns model science or downstream use.

**Status:** scoped_check. **Theme:** evaluation_configuration.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `kapoor_aiagentsmatter_2024` — supports | [Source](https://arxiv.org/pdf/2407.01502v1); arXiv v1 §§2–4 pp3–7; TablesA1/A3 pp20/23; AppendixA–B pp18–26 | Simple HumanEval retry/warming baselines lie on or improve the cost–accuracy frontier relative to selected complex architectures; HotPotQA joint optimization lowers variable cost with similar retrieval performance. | `this_run_primary`; Complete main text §§1–7, PDF pp1–11; complete AppendixA–B text/tables/captions pp18–26 plus AppendixC/D opening/selection and NovelQA setup onp26. References pp12–17 and remaining AppendicesC–I/NeurIPS checklist pp27–33 were not read completely; image-only plot values were not digitized. Selected33-page preprint, not a full read. Experiments are the authors' own reproduced/re-evaluated runs in historical2024 model/pricing conditions; this review ran no agents. Five-run confidence intervals omit optimization/resampling variability, as FigureA5 notes. Holdout appropriateness counts include stated intentions, not only existing holdouts. NovelQA comparison was one run and its sequential-cost extrapolation is modeled.; review events: [r2_sociotechnical_02](rounds.md#r2_sociotechnical_02) |

**Limits:** The paper uses selected historical models/benchmarks, modified HumanEval example tests and dated API prices. Its confidence intervals omit optimization/resampling variation; NovelQA was run once. This review does not reproduce its experiments.

**Counterevidence / alternative:** Complex planning/reflection may still help on harder tasks. Autonomous-only evaluations may also understate utility when humans provide feedback; the latter is a review argument relying in part on external studies.

**Next check:** Keep cost, token, task, model, retry and human-supervision conditions attached to any comparison; complete remaining appendix/run-level checks before numerical publication.

<a id="c44"></a>
## C44

Dataset documentation can make intended use, sampling, provenance and maintenance inspectable through a reflective workflow; automated metadata completion is not equivalent to that proposed process or proof of representative data.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `gebru_datasheets_2021` — supports | [Source](https://arxiv.org/pdf/1803.09010v8); arXiv v8 §§1.1–4 pp2–11; AppendixA pp14–18 | Datasheets asks factual lifecycle questions, recommends recording unknowns, and explicitly treats creator reflection as an objective that should not be automated. It reports development feedback and organizational pilots without evaluating causal effects. | `this_run_primary`; All18 pages of arXivv8 accessible extracted text read in three complete six-page blocks: introduction/objectives, development process, all questions/workflow, impact/challenges, acknowledgments/references, AppendixA and all four text-based example datasheet figures. External cited datasets/links were not opened. Published CACM equivalence not authenticated. Reported organizational pilots are author reports, not independently verified adoption or causal evidence of harm reduction. Examples disclose unknowns; full text does not include all linked datasets or web resources.; review events: [r2_sociotechnical_01](rounds.md#r2_sociotechnical_01) |

**Limits:** Full reading covers the18-page arXivv8 object linked by the canonical record. The CACM layout/bytes and linked datasets were not authenticated; reported pilots are author reports rather than verified adoption or measured harm reduction.

**Counterevidence / alternative:** Documentation has a plausible and practical communication/selection role and reported uptake, even though it cannot anticipate every use or guarantee fairness. Organizational incentives, overhead and dynamic-data maintenance constrain implementation.

**Next check:** Use disclosure gaps to guide targeted source checks and creator questions; preserve unknowns. Inspect the published CACM object separately if citing its exact layout/DOI.

<a id="c45"></a>
## C45

Layered model, red-team and human field testing can expose different application-validity problems and user perceptions; the ARIA pilot demonstrates an implemented method, not a calibrated cross-application safety ranking or a measured reduction in harms.

**Status:** scoped_check. **Theme:** outcomes.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `amironesei_aria_pilot_2025` — supports | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-2.pdf); NIST AI700-2 §§2–5, printedpp2–12/viewer9–19; §5.2 and AppendixC | ARIA combines annotations and tester questionnaires in transparent measurement trees; example applications obtain their largest signals from different testing levels, and tester perceptions can diverge from annotated violations. | `this_run_primary`; Abstract/TOC PDF pp4–5; main text §§1–7 PDF pp8–21 (printed1–14), including testing, annotation, crosswalk, CoRIx topology, example interpretations and future work; AppendixC PDFp29/printed22. Other appendices and rendered tree graphics not completely reviewed. Exploratory seven-application pilot with51 red teamers and19 field testers under English scenarios, not representative deployment outcomes. Proxy scenarios differ from severe harms; not every application was tested at every level. Questionnaires and annotations are not directly comparable, and scores are characterized as better for describing than ranking applications. Uncertainty propagation and questionnaire validation remain future work.; review events: [r2_sociotechnical_03](rounds.md#r2_sociotechnical_03) |

**Limits:** Small English-language pilot of proxy scenarios. Testers, annotators, dialogues and annotation judgments have different denominators. The source says initial CoRIx is better for characterization than comparison; questionnaire/annotation questions differ and uncertainty quantification remains open. Main267/52 versus AppendixC267/49 count tension is held rather than turned into a violation rate.

**Counterevidence / alternative:** Field-style use may reveal failures absent in fixed prompts, while model testing may reveal issues that field users miss or do not commonly elicit. Neither direction is a general guarantee of ecological validity.

**Next check:** Retain qualitative findings and omit affected violation numbers pending source clarification. Complete measurement and appendix/visual review before any numerical cross-system inference.

<a id="c46"></a>
## C46

Standardized multi-metric evaluation can produce useful common comparisons and reveal tradeoffs while explicitly restricting the measured subspace; broad coverage should remain distinct from deployment validity.

**Status:** scoped_check. **Theme:** evaluation_configuration.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `liang_helm_2023` — supports | [Source](https://arxiv.org/pdf/2211.09110v2); arXiv v2 §1; §4.1–4.2/Tables2–4 pp25–27; §4.6–4.8; §10.1–10.5 pp78–80 | HELMv2 operationalizes selected scenarios and metrics under common adaptation, exposes cross-metric differences, and makes missing scenario/metric/model coverage explicit. Its seven metrics cover98 of112 selected scenario–desideratum pairs, with exclusions explained. | `this_run_primary`; Title/abstract and §1 overview; selected §1.2 top-level findings pp7–10; selected scenario and metric-method text pp23–32, especially §4.1–4.2 Tables2–4 and §4.6–4.8; missing-scenario/metric/model/adaptation discussion §10.1–10.5 pp78–80. Not a complete162-page read; full appendices, results figures and live raw outputs not audited. Historical30-model comparison. Metric coverage and known omissions are part of the result. Fairness perturbations may miss complex distribution differences; demographic group labels are missing for many scenarios; bias/toxicity proxies have acknowledged validity limits. No underlying prediction matrix or live leaderboard was reproduced. Some PDF diagram text/URLs extract poorly; no graph-coordinate verification.; review events: [r2_sociotechnical_04](rounds.md#r2_sociotechnical_04) |

**Limits:** Selected portions of a162-page historical report, not complete text or raw-output replication. Scalable fairness/bias/toxicity proxies have acknowledged limits; many social/system properties require access and contextual knowledge outside its evaluation interface.

**Counterevidence / alternative:** Recognition of incompleteness does not erase the constructive value of unified comparison. Conversely, adding more metrics does not automatically validate them or produce a single trustworthy-system ranking.

**Next check:** For a publication-leading numerical result, inspect its exact scenario/metric methods, model checkpoint, raw outputs and stakeholder validity rather than reuse overall benchmark coverage as assurance.

<a id="c47"></a>
## C47

Historical trustworthiness evaluations show both standard-condition improvements and metric/access-specific reversals; higher average accuracy alone does not fix fairness or robustness under an altered threat model.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `wang_decodingtrust_2023` — supports | [Source](https://proceedings.neurips.cc/paper_files/paper/2023/file/63cb9921eecf51bfad27a99b2c53dd6d-Paper-Datasets_and_Benchmarks.pdf); NeurIPS2023 §§2–9/Tables1–4 pp4–10; mainp2 footnote3; AppendixB.1 PDFp30 | On fixed March2023 GPT checkpoints, benign toxicity and some robustness/OOD outcomes improve, while adversarial system/demonstration conditions and constructed fairness base rates expose different weaknesses. | `this_run_primary`; Main text PDF/printed pp1–2 and4–10; AppendixB preliminaries/model/role setup PDFp30 (appendix printedp6). Includes text of Tables1–4 and selected method/result discussions for toxicity, robustness, OOD, demonstrations, privacy and fairness. Main Figure1 page3, full108-page appendices and graph values are not fully reviewed. Historical March2023 API checkpoints. Researchers can set system and user roles, so adversarial-system conditions are a particular access threat model rather than all ordinary deployments. Proxy toxic classifiers, prompted stereotype agreement and Adult salary prediction fairness do not estimate population harm. Proposed mechanisms attributing vulnerability to instruction following are hypotheses, not isolated causal tests. No full appendix or code/data reproduction.; review events: [r2_sociotechnical_05](rounds.md#r2_sociotechnical_05) |

**Limits:** Selected methods/results and one appendix section from a108-page proceedings object. System-role attacker access, proxy toxicity judgments, Adult salary tasks and historical checkpoints constrain transfer. No modern-deployment incidence or isolated causal mechanism is established.

**Counterevidence / alternative:** Several standard robustness and OOD results favor GPT-4, so the findings do not establish a universal capability-versus-safety tradeoff. Shared datasets across broad suites are dependencies, not independent corroboration.

**Next check:** Complete relevant appendix/classifier/source-data checks before headline rates; keep model IDs, role permissions, sampling and each outcome definition explicit.

## Source families and dependencies

These family annotations identify shared work, data or incidents where known. They do not comprehensively certify independence across the collection. Citation keys are retained pending identity adjudication.

| Family | Citation keys | Relationship | Basis | Status |
|---|---|---|---|---|
| `F01` | `mazeika_harmbenchstandardized_2024`, `harmbench_standardizedevaluation_2024` | The two records describe the same named HarmBench study family; the preprint and proceedings representations do not supply independent corroboration. | Fresh PMLR metadata and selected final-paper methods identify the title, twelve authors, eighteen red-team methods and thirty-three targets. See r2_safeguards_02–03. | Named-study family corroborated. Exact DOI/alias mapping and edition equivalence remain unresolved; both citation keys are preserved and the second record is not used as separate empirical support. |
| `F02` | `wang_helpsteer2opensource_2024`, `wang_helpsteer2preference_2024` | Distinct contributions with shared dataset/annotation lineage. | The preference extension adds preferences and rationales to HelpSteer2; supplied ledger and C08. | Shared lineage recorded; full splits/annotator dependency review pending. |
| `F03` | `aisi_unsanctionedagentincident_2026` | One incident, with AISI and Anthropic follow-up analyses outside the canonical corpus. | The incident disclosure and cited follow-ups in review.md concern the same July testing event; replays/simulations are different observations. | Incident dependence explicit; candidate sources not assigned new canonical keys or admitted. |
| `F04` | `deepmind_frontiersafetyv3_2025`, `deepmind_frontiersafetyv31_2026` | Within-issuer framework editions, compared clause by clause rather than counted as independent empirical support. | Existing commitment history and C18. | Edition relation established for scoped comparison; implementation unverified. |
| `F05` | `openai_preparednessbeta_2023`, `openai_preparednessv2_2025` | Within-issuer policy lineage with changed risk/capability terminology. | Existing commitment history and C19. | Historical comparison retained; later statements have separate observations. |
| `F06` | `chao_jailbreakbenchopen_2024`, `pavlova_automatedredteaming_2024`, `mazeika_harmbenchstandardized_2024`, `harmbench_standardizedevaluation_2024` | Shared benchmark lineage: JBB reports 27% of behaviors from TDC/HarmBench, 18% from AdvBench and 55% original; GOAT uses JBB behaviors/judging. | JBB v5 §3.1 and Appendix B; GOAT v1 evaluation setup; r2_safeguards_01 and06. | Reuse documented at the reported dataset level; exact item-level overlap across every evaluated condition is not independently reconstructed. Distinct methods are not independent task-distribution replications. |
| `F07` | `khan_debatingmorepersuasive_2024`, `kenton_scalableoversightweak_2024`, `arnesen_trainingwindebates_2024` | QuALITY-centered debate task lineage, with different protocols, judges and training or inference targets. | Existing C11–C12 and fresh Arnesen methods in C29; Kenton also tests other task families. | Task-family overlap is explicit; exact item/split reuse is not fully reconciled. These are distinct contributions, not three independent demonstrations of broad generalization. |
| `F08` | `raji_closingaccountabilitygap_2020`, `raji_outsideroversight_2022` | Shared author and conceptual lineage across internal lifecycle and external-audit arguments. | Fresh source authorship/methods review and C39/C41. | Complementary institutional arguments; no independent causal outcome replication is claimed. |
