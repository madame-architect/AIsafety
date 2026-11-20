# Claim and evidence map

Generated from [claims.yaml](claims.yaml). Source identities resolve through [records.yaml](../../records.yaml); record-level inspection and limitations appear in [coverage.csv](coverage.csv). This is a provisional map of selected synthesis propositions, not a claim that the entire corpus supports them.

Assessment date: **2026-11-20**. `supplied_ledger` means inherited notes; `prior_audit` means a separate AI-assisted source check reported by the supplied audit; `this_run_primary` means scoped primary inspection reported by the project integration or a linked review round, not a recheck whenever this view is generated; `repo_source_review` means an existing dated repository review. None denotes independent human review or replication.

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
| [C48](#c48) | mechanistic_validation | scoped_check | In small chess and Othello language models, SAE features recover formally specified board properties and task-labelled metrics distinguish trained from random-weight models; syntax and position shortcuts still affect which properties count as validation. |
| [C49](#c49) | mechanistic_validation | scoped_check | Selected SAE interventions localize and alter counterfactual indirect-object-identification behavior relative to tested baselines, while supervised task dictionaries expose substantial gaps between interpretable features and sparse control, especially for full-distribution SAEs. |
| [C50](#c50) | mechanistic_validation | scoped_check | Activation reconstruction, output fidelity, interpretable feature descriptions, and sparse causal control test different properties: preserving outputs alone can leave the internal computational pathway underdetermined. |
| [C51](#c51) | evaluator_integrity | scoped_check | Prompt-specific circuit tracing has generated causally testable hypotheses and successful selected original-model interventions, while reconstruction fidelity and graph completeness do not establish a complete or mechanistically faithful account of a model. |
| [C52](#c52) | evaluator_integrity | scoped_check | Automated feature explanations need validation against their intended endpoint: activation-context descriptions and descriptions of intervention-induced output effects can yield different judgments about the same SAE feature. |
| [C53](#c53) | evaluator_integrity | scoped_check | Some filtered SAE feature subspaces align across selected language models under correlation-based matching and representational-similarity measures, providing bounded evidence of analogous structure rather than universal causal feature identity or demonstrated transfer of control. |
| [C54](#c54) | governance | provisional | A layered audit can be designed as an evidence feedback process: governance records, model limitations and deployment-level impacts answer different questions and should inform each other. General model scores cannot alone establish context-specific fairness or legal acceptability in an application. |
| [C55](#c55) | governance | provisional | Reviewing compliance with a frontier developer’s own safety framework can make implementation more inspectable, but it answers a narrower question than whether the framework or system is adequate. Its assurance depends on operationalized commitments, evidence access, reviewer incentives, disclosure and action on findings. |
| [C57](#c57) | fairness_values | scoped_check | Public input can change model behavior and reduce a specified bias benchmark, while the same intervention can reduce alignment with measured public-opinion distributions. |
| [C58](#c58) | fairness_values | scoped_check | A minimax preference objective offers a constructive way to handle intransitive judgments without a single scalar reward ordering, but its optimization guarantee does not validate the preferences or their social legitimacy. |
| [C59](#c59) | fairness_values | scoped_check | Fairness benchmark results depend on distinct constructs and normative choices: group prediction gaps, stereotype behavior and refusal to express subjective preferences cannot be treated as one interchangeable fairness verdict. |
| [C60](#c60) | governance | scoped_check | The inspected 2024 federal-agency-use plans report specific organizational acts alongside prospective or incompletely specified risk-control procedures; these historical self-descriptions do not establish that high-impact testing, waivers or remediation operated effectively. |
| [C61](#c61) | governance | scoped_check | In the April 3, 2025 M-25-21 design for covered federal use, high-impact classification can trigger documented testing, impact assessment, review by a nondeveloper within the agency, risk acceptance, monitoring and discontinuation; scope limits, pilots and waivers qualify that pathway. |
| [C62](#c62) | governance | scoped_check | The pinned January 23, 2025 federal AI inventory can substantiate counts of publicly reported administrative use-case records and their declared categories; it cannot by itself substantiate deployed-system prevalence or effective compliance. |
| [C63](#c63) | policy_implementation | scoped_check | The 2025 Foundation Model Transparency Index measures disclosed information for 13 developers across 100 indicators. Its reported mean of 40.69/100 describes disclosure, rather than verified control effectiveness or a controlled annual change in safety. |
| [C64](#c64) | policy_implementation | scoped_check | NVIDIA’s report, applicable as of August 2025, describes screening, approval, reassessment and pre-release testing mechanisms, including reported Garak use. Its risk-analysis template and issuer descriptions do not demonstrate realized risk reduction. |
| [C65](#c65) | policy_implementation | scoped_check | Meta’s April 7, 2026 v2 framework combines a material-contribution risk trigger with conditional mitigated development/deployment and more explicit accountability. The inspected text alone does not establish overall strengthening or weakening, adherence, or a safety effect. |
| [C66](#c66) | governance | provisional | System-specific safety cases provide an explicit way to connect a deployment claim to evidence and review, while threshold choices, reviewer capacity and update rules still require justification beyond producing a document. |
| [C67](#c67) | governance | scoped_check | Safety-case confidence analysis can expose assumptions and prioritize doubts, but propagated probabilities and an LLM-Delphi pilot do not by themselves calibrate deployment safety or supply independent expert corroboration. |
| [C68](#c68) | governance | provisional | A dynamic safety-case design links changed artifacts or monitored indicators to affected claims and response owners, while correctness of the initial argument, traceability and indicator validity remain prerequisites rather than outputs of consistency checking. |
| [C69](#c69) | governance | provisional | Guarded architectures can place assurance on narrower, more understandable components, but their guarantees depend on correct hazard models, trusted perception and safe enforcement; adding diversity alone does not establish independent failure probabilities. |
| [C70](#c70) | evaluator_integrity | scoped_check | Internal probes can discriminate selected evaluation and deployment prompt distributions, but that readout and its size association do not establish deceptive behavior or a universal scaling law for concealment. |
| [C71](#c71) | evaluator_integrity | scoped_check | Activation steering can alter engineered evaluation-conditional behavior, while simple-prompt and unrelated-feature controls show why eliciting a different output is insufficient to establish an awareness-specific mechanism or unknown deployment behavior. |
| [C72](#c72) | evaluator_integrity | scoped_check | Prompted models can conceal some successful capability underperformance from a reasoning monitor, but conditional approval, noisy success filtering and efficacy/selectivity tradeoffs prevent interpreting this as spontaneous or reliably successful deployment sandbagging. |
| [C73](#c73) | evaluator_integrity | scoped_check | Complex sabotage-agent tests make joint task success and monitor detection separately inspectable and show scoped monitor-training gains; those results remain conditional on instructed goals, observed information, filtering and when detection occurs. |
| [C74](#c74) | evaluator_integrity | scoped_check | Pairwise reward-model discrimination and downstream policy quality require different validation. PPE supplies a controlled example connecting selected proxy metrics to post-DPO human preferences, while showing that familiar benchmark rankings need not predict the same outcome. |
| [C75](#c75) | evaluator_integrity | scoped_check | Synthetic preference and judgment training can improve a generative judge on tested benchmarks, while leaving residual order sensitivity, uneven task gains and dependence on the seed model and constructed labels. |
| [C76](#c76) | evaluator_integrity | scoped_check | A statistical annotator-substitution test can make a task-specific comparison with sampled human judgments explicit, but its pass decision depends on the reference population, cost-benefit threshold, imbalance treatment and intended construct. |
| [C77](#c77) | evaluator_integrity | scoped_check | Joint statistical models of the answer and grading process can separate modeled score-scale shifts, item effects and uncertainty that a single agreement statistic obscures; the demonstrated bias adjustments are simulated, model-dependent counterfactuals. |
| [C78](#c78) | evaluation_configuration | scoped_check | A task-completion time horizon supplies a common difficulty/reliability measure for a specified agent and task suite; it is not the duration an AI operates autonomously or a direct measure of whole-job automation. |
| [C79](#c79) | evaluator_integrity | scoped_check | A standardized hazardous-response benchmark can provide explicit rules, confidential tests and configuration-sensitive feedback without certifying system safety; evaluator, grading and prompt-set versions must remain part of the result. |
| [C80](#c80) | governance | scoped_check | Compute thresholds have a defensible proposed role as early screens for additional scrutiny; the reviewed design sources do not establish a universal compute-to-harm cutoff or make compute an adequate trigger for every governance duty. |
| [C81](#c81) | governance | scoped_check | Compute can provide concrete governance levers through infrastructure visibility, mediated access and measurable resources; those affordances must be assessed separately from risk-proxy validity and the costs of surveillance, concentration and evasion. |
| [C82](#c82) | governance | scoped_check | The 2025 threshold survey is useful evidence about elicited expert design preferences and disagreements; optional selected-sample responses and competing definitions do not validate risk boundaries or establish representative consensus. |
| [C83](#c83) | policy_implementation | scoped_check | The reviewed frontier-governance proposals specify routes from assessment and external scrutiny to deployment conditions, monitoring and adaptive scope; their practical value depends on measurement, access and institutional capacity rather than the existence of a threshold alone. |
| [C84](#c84) | governance | scoped_check | Internal deployment can change model configuration, privileges, tools and applications relative to a public product. The reviewed proposals therefore place internal-use permissions, evaluation and decision authority within governance scope; they do not establish that all internal governance is absent or that their proposed controls have reduced harm. |
| [C86](#c86) | governance | scoped_check | Incident-reporting designs can make system versions, harm, context and response more inspectable, but their evidential value depends on scope, reporting thresholds and investigation. Required fields in a proposed common format do not create a legal reporting duty, and neither a template nor a reporting count demonstrates reduced harm. |
| [C87](#c87) | outcomes | scoped_check | The AI Incident Database paper documents implemented cataloguing mechanisms—stable incident IDs, multiple reports per incident, search and plural taxonomies—that can support learning. It does not establish representative failure rates or demonstrate that database use prevents failures; report counts and illustrative mitigation workflows answer narrower questions. |
| [C88](#c88) | oversight_control | scoped_check | Engineered backdoors can persist through specified safety-training pipelines, but persistence depends on adversarial access, objective, model and training configuration; some tested objectives or models lose the measured backdoor effect. |
| [C89](#c89) | oversight_control | scoped_check | A model can be engineered to display a target behavior only after selected benign supervised finetuning, making pre-adaptation behavior an incomplete assurance test for that constructed threat model. |
| [C90](#c90) | oversight_control | scoped_check | Filtered synthetic training data can transmit measured teacher traits in controlled finetuning experiments, with model-pair, trait and evaluation dependencies that prevent a universal transfer rule. |
| [C91](#c91) | oversight_control | scoped_check | Backdoor benchmarks expose task, access and edition dependence, with positive targeted-refusal mitigation in a later comparison; unresolved jailbreak baseline/task provenance prevents a reliable quantitative jailbreak-defense conclusion. |
| [C92](#c92) | safeguards | scoped_check | Separately modeling helpfulness and harmfulness can improve their measured tradeoff through constrained optimization, while the practical constraint remains an expectation of a learned cost. |
| [C93](#c93) | safeguards | scoped_check | HC-RLHF’s held-out accept-or-abstain procedure supports a conditional bound on the probability of returning a model that violates an expected learned-cost constraint. The written zero-threshold case avoids an unresolved centering discrepancy. |
| [C94](#c94) | safeguards | scoped_check | Safe LoRA provides a positive weight-space mitigation for safety degradation during controlled fine-tuning, with model-dependent projection choices and visible utility tradeoffs. |
| [C95](#c95) | oversight_control | scoped_check | Teaching models to reason over explicit safety policies provides affirmative policy-adherence and jailbreak-resistance evidence, with limits from comparator information, overrefusal and the tested transfer distribution. |
| [C96](#c96) | safeguards | scoped_check | Historical extraction experiments distinguish restricting ordinary output behavior from removing memorized text; their access conditions and web-matching ground truth do not establish current product exposure or certified proprietary-training membership. |
| [C97](#c97) | outcomes | scoped_check | A deletion audit of the resulting model and privacy of the before/after update history are distinct: in Du et al.’s synthetic classification experiments, exact retraining improves single-state erasure while version comparisons can still reveal deletion membership. |
| [C98](#c98) | audit_institutions | scoped_check | vTune supplies positive, conditional evidence of fine-tuning on marked data, while leaving requested training granularity and an exact statistical null bound unverified. |
| [C99](#c99) | safeguards | scoped_check | Open-model post-training extraction can yield semantically similar and useful training-like data, while semantic resemblance, exact record extraction and recovery of a complete safety policy remain distinct claims. |
| [C100](#c100) | governance | scoped_check | Draft misuse-risk guidance can make a threat-to-decision process inspectable by linking risk baselines, evaluation conditions, safeguards, deployment choices and post-deployment feedback; it does not make those choices empirically adequate or legally binding merely by documenting them. |
| [C101](#c101) | governance | scoped_check | California Assembly staff cited PIRG’s 2025 AI toy tests in the June 16, 2026 SB 867 analysis. The subsequent chaptered law documents a separate legal action, not the tests’ causal influence, implementation, or effects. |
| [C102](#c102) | outcomes | scoped_check | Adult-led product elicitation and observed preschool play answer different downstream evaluation questions. The inspected examples show product output under selected tests and interaction difficulties during observed play, not population exposure or long-term effects. |
| [C103](#c103) | governance | scoped_check | PIRG’s February 2026 walkthrough of five developer onboarding paths observed one provider asking whether the intended product was for minors. This documents a visible screening step, not enforcement or the effect of a screening policy. |

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
| `aisi_safetyinstitutesjoint_2024` — supports | [Source](https://www.aisi.gov.uk/blog/pre-deployment-evaluation-of-openais-o1-model); Issuer Overview/Methodology/Conclusion, datedDecember 18, 2024 | A real external pre-release exercise reported limited access, scaffold repair and version-specific comparisons rather than a release-safety endorsement. | `this_run_primary`; Complete accessible captured HTML text: Introduction, Overview, Methodology, selected findings in all 3 domains, Conclusion, report links, date/name-change note and footer. No linked report is included in this complete-page event.; review events: [r4_depthsample_02](rounds.md#r4_depthsample_02) |
| `aisi_safetyinstitutesjoint_2024` — supports | [Source](https://cdn.prod.website-files.com/663bd486c5e4c81588db7a1d/6763fac97cd22a9484ac3c37_o1_uk_us_december_publication_final.pdf); December 2024 technical report §§1–4,9–10.4; Table 4.1 | Exact methods specify attempts/messages rather than equal cost, uncertainty excluding scaffold variation and tool/scoring effects; positive US Cybench and bio-tool results remain configuration-specific. | `this_run_primary`; PDF cover/contents pp1–3; printedpp1–7/viewerpp4–10 (Introduction, disclaimers, complete general methods, US Cybench methods/results/Table 4.1); viewerp12/printedp9 (future-work discussion/UK methods opening); printedpp11–14/viewerpp14–17 (UK agent setup/results, selected domain discussions); printedpp17–20/viewerpp20–23 (LAB-Bench methods, tooling, scoring and selected results). Plot text on viewerp11 was partly unreadable and is not used for numerical claims. Other pages/remaining software/AI sections/references were not fully read.; review events: [r4_depthsample_03](rounds.md#r4_depthsample_03) |

**Limits:** These controlled tests do not estimate general workplace safety or operational harm. Some inherited selected-section locators are extraction spans rather than stable page references. Standalone Cybench is cited in the supplied review but absent from the admitted bibliography. Joint AISI o1 overview and technical report describe one exercise; the newly accessible report remains selectively read. Its UK apprentice headline differs internally across the overview and result section, so no affected rate is adopted.

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

**Next check:** Use the complementary validation evidence in C48–C53 to separate specified-structure recovery, output and pathway fidelity, interpretation, causal control and downstream utility. Heap was not reread in this round; preserve its prior version and scope limits.

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
| `newyork_raiseact_article44b_nd` — contextualizes | [Source](https://www.nysenate.gov/legislation/laws/GBS/A44-B); Article44-B revision/effective-date note; S8828 action history and §§3–5 | The official codification displays the April3,2026 revision and January1,2027 effective date; signed chapter96 history and effective-date clauses support the prospective-duty distinction. This is a legal-text check, not implementation evidence. | `this_run_primary`; Selected official index/action and amendatory timing clauses, not all ten operative sections or subsequent legal status.; review events: [r4_ny_01](rounds.md#r4_ny_01), [r4_ny_02](rounds.md#r4_ny_02), [r4_ny_03](rounds.md#r4_ny_03) |
| `california_sb53_tfaia_2025` — contextualizes | [Source](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/); Governor officialSeptember29,2025 signing release and linked signing message | Official executive evidence authenticates signing and summarizes statutory mechanisms, while direct enacted-clause retrieval still fails. Exact deadlines and current application are not recertified by the summary. | `this_run_primary`; Governor official September29,2025 release: title/date, signing statement, summary of transparency/incident/whistleblower/update mechanisms and link to signing message. Unrelated economic claims, quotations and recent-news navigation not treated as evidence.; review events: [r5_versions_07](rounds.md#r5_versions_07) |

**Limits:** This is a distinction between kinds of evidence, not a determination of every instrument’s present legal force. The supplied patch corrects specified legal-status fields; unreviewed instruments and current application still require dated source checks. ISO evidence is catalog/preview scope only. The Commission template was inspected through a mirror; issuer-byte identity and exact clause locators remain open. The supplied correction package is now integrated; it does not recertify all instruments or editions. The earlier New York access/date hold is closed narrowly by current official codification, signed chapter history and amendatory timing clauses; not all operative sections or later application were reread. California signing is corroborated by official executive material, while this round’s direct official statutory-text attempts returned403. Exact California deadlines/current consolidated application remain unrecertified; signing is not observed implementation.

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
| `blum_gtigagenticthreshold_2026` — contextualizes | [Source](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold); November 16, 2026 publisher page, Executive Summary and opening observations. | A subsequent GTIG and Mandiant report describes additional real-world evidence of AI-assisted components. The selected observations do not provide a denominator, matched comparison, representative prevalence, or independent validation of the earlier GTIG report. | `this_run_primary`; Publisher web-view executive summary and high-level descriptions only. Direct source-byte retrieval returned HTTP 403; no byte-backed reading credit, full-document check, or independent telemetry audit. |

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
| `mcgregor_preventingrepeatedfailures_2021` — bounds | [Source](https://cdn.aaai.org/ojs/17817/17817-13-21311-1-2-20210518.pdf); Final AAAI 2021 pp. 15459–15463; Figures 2/5 | Historical report volume and hypothetical mitigation do not establish population incident rates or observed prevention; stable IDs consolidate repeated reporting. | `this_run_primary`; Complete accessible text of all 6 final proceedings PDF pages, printed 15458–15463: abstract, introduction/motivation, AIID architecture and discovery/submission/taxonomy features, all figure captions, hypothetical fairness-use example, conclusions, acknowledgments and references. Figures 2–5 visually inspected on PDF pages 3–5; Figure 1 image not pixel-inspected. No current database, software or linked external source was audited.; review events: [r5_reporting_06](rounds.md#r5_reporting_06) |

**Limits:** The framework is conceptual with illustrative cases. The incident analysis uses selected media reports; language, reporting, search and classification affect observed coverage and provide no denominator of underlying incidents.

**Counterevidence / alternative:** Level distinctions improve evaluation design and reported incident clusters can identify concrete harms and leads. Neither source supplies matched causal estimates of the effect of an individual model or safeguard.

**Next check:** Complete the claim-critical framework/report methods and stable locators; keep reported-record counts separate from population rates and connect each impact assertion to its own denominator and comparator. Keep AIID source-report IDs distinct from incident IDs and inspect actual causal/response data before any population-rate or prevention-effect claim.

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
| `yu_robustsafeguarding_2024` — supports | [Source](https://arxiv.org/pdf/2409.20089v1); arXiv v1 §§3–7/Table1; Appendix A–B/Tables4–5 | ReFAT links refusal-feature restoration to lower judged attack success with capability controls, then trains on ablation plus utility/overrefusal data and improves several robustness endpoints on three models; residual multilingual failures and comparator/rank limits remain. | `this_run_primary`; Cover/abstract p1; complete §§3–8 pp3–10, including mechanistic geometry/restoration, perturbation comparison, training, setup, results and limitations; Appendix A and B with Tables4–5 p14. References and full PCA/histogram Appendices C–D not comprehensively read. Main introduction/related work only abstract/heading context, not complete.; review events: [r5_mitigations_04](rounds.md#r5_mitigations_04) |

**Limits:** These are scoped model/training experiments with automatic behavioral judges. Neither a mismatched training comparator nor a limited benign benchmark establishes zero utility cost or broad deployed security. ReFAT successful-case geometric alignment and a comparison with99 random directions do not establish a universal attack mechanism or global worst-case perturbation. Main §5 rank64 conflicts with Appendix A ranks128/128/64; exact training recipe remains open. MT-Bench uses Prometheus and PAIR uses Mixtral in the appendix; compare those endpoints accordingly.

**Counterevidence / alternative:** HarmBench finds no model uniformly robust; cross-attack generalization is weaker away from the train-time adversary. Qi reports residual vulnerability, regularization/optimizer dependence and non-monotonic combined-method benefit. ReFAT has residual attack successes, non-English/vernacular failures and utility losses, and is not best on every Table1 metric. Efficiency counts model forward/backward passes rather than wall-clock cost.

**Next check:** Retain affirmative gains without pooling ASRs. Match attack budgets, training pipelines and utility baselines, and verify final-version equivalence before headline numbers. Keep positive intervention evidence; reconcile LoRA rank/run configuration before reproduction and omit universal-mechanism/global-optimum/runtime-speedup claims.

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
| `longpre_inhouseevaluation_2025` — supports | [Source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/longpre25a/longpre25a.pdf); Final PMLR267 §§4.1–4.3,pp5–8; AppendixA.1/A.4,pp18–20; AppendixB.1,p20; §6,p9 | The final proposal defines evaluator relationships as a spectrum and connects reproducible flaw reporting with conduct-based protection, technical access and coordination; it leaves remediation effects and center governance unresolved. | `this_run_primary`; Final ICML/PMLR 267 PDF pp1–9 (abstract and all main §§1–7); Appendix A pp18–20; Appendix B.1 introductory/example explanations p20, B.2–B.3 and Table A1 pp22–25; Appendix C.1–C.4 pp25–28, including Table A2. Figure A7 p26 visually inspected. The table of contents p17, references pp9–16, visual example cards p21, and Appendix D pp29–31 were not read in full; this is selected-section review.; review events: [r3_audits_01](rounds.md#r3_audits_01) |
| `brundage_frontierauditingrigorous_2026` — supports | [Source](https://arxiv.org/pdf/2601.11699v4); v4 §5.3.3/Table 3 pp. 30–34; §5.4 opening/Figure 7 pp. 35–36 | Access comprises scope, duration, interfaces, documentation and verification; upper levels and example audit conclusions are explicitly prospective. | `this_run_primary`; v4 cover/title/byline/version; executive summary PDF pp. 2–6; PDF pp. 30–36 covering §5.3.3 AAL descriptions/Table 3, §5.3.4 assurance-level choice and §5.4 opening/Figure 7 access taxonomy. Remaining 115-page report and appendices not read.; review events: [r5_reporting_03](rounds.md#r5_reporting_03) |

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
| `longpre_inhouseevaluation_2025` — supports | [Source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/longpre25a/longpre25a.pdf); Final PMLR267 §§4.1–4.3,pp5–8; AppendixA.1/A.4,pp18–20; AppendixB.1,p20; §6,p9 | The final proposal defines evaluator relationships as a spectrum and connects reproducible flaw reporting with conduct-based protection, technical access and coordination; it leaves remediation effects and center governance unresolved. | `this_run_primary`; Final ICML/PMLR 267 PDF pp1–9 (abstract and all main §§1–7); Appendix A pp18–20; Appendix B.1 introductory/example explanations p20, B.2–B.3 and Table A1 pp22–25; Appendix C.1–C.4 pp25–28, including Table A2. Figure A7 p26 visually inspected. The table of contents p17, references pp9–16, visual example cards p21, and Appendix D pp29–31 were not read in full; this is selected-section review.; review events: [r3_audits_01](rounds.md#r3_audits_01) |
| `brundage_frontierauditingrigorous_2026` — supports | [Source](https://arxiv.org/pdf/2601.11699v4); v4 executive summary pp. 2–6; §5.3.4 pp. 34–35 | Confidential expert access and audit validity conditions are proposed enabling arrangements; competence, independence and adoption remain constraints. | `this_run_primary`; v4 cover/title/byline/version; executive summary PDF pp. 2–6; PDF pp. 30–36 covering §5.3.3 AAL descriptions/Table 3, §5.3.4 assurance-level choice and §5.4 opening/Figure 7 access taxonomy. Remaining 115-page report and appendices not read.; review events: [r5_reporting_03](rounds.md#r5_reporting_03) |

**Limits:** Cross-industry analogies and proposed arrangements do not measure present frontier-AI audit effectiveness. Outsider Oversight’s AppendixTable2 appears to swap FDAFAERS and FCCTCB descriptions; those two program examples are omitted from this inference pending primary verification. The new Longpre paper is a proposal with counterfactual example report cards, not measured effects. Its third-party category excludes direct contractual relationships; Mökander and Homewood use third-party for external collaborative or commissioned review. Compare the actual relationships rather than pooling these labels.

**Counterevidence / alternative:** Internal audits retain useful access and preventive functions; independence can trade off with expertise, and formal licensing or disclosure can produce exclusion, cost or box-ticking. The five design dimensions are not validated as a universal scoring formula.

**Next check:** For applied cases, record who selected/paid the assessor, what could be tested, who received the findings and who acted on them. Verify affected FDA/FCC program descriptions before reuse.

<a id="c40"></a>
## C40

Legal protection for good-faith research and protection against technical exclusion address different barriers to external evaluation. The safe-harbor proposal links them to disclosure rules, independent access review and appeals; it does not show that legal language alone supplies access or improves safety.

**Status:** provisional. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `longpre_safeharbor_2024` — supports | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/longpre24a/longpre24a.pdf); PMLR 2024 Table1, §4, Figure1 and §§4.1–4.2, PDFpp6–9 | The authors distinguish civil legal protection from account-suspension protections, propose conditional researcher and company commitments, and describe third-party review/appeal mechanisms. | `this_run_primary`; PMLR published PDF pp1–4 (abstract, introduction, definitions/Table1 and researcher-experience discussion/Table2), the sampling-qualification paragraph at the beginning of p5, plus §4, §§4.1–4.2 and Figure1 text on PDFpp6–9. Remaining company-policy text/Table3 and later sections/appendices were not read in full.; review events: [r2_institutions_04](rounds.md#r2_institutions_04) |
| `longpre_inhouseevaluation_2025` — supports | [Source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/longpre25a/longpre25a.pdf); Final PMLR267 §§4.1–4.3,pp5–8; AppendixA.1/A.4,pp18–20; AppendixB.1,p20; §6,p9 | The final proposal defines evaluator relationships as a spectrum and connects reproducible flaw reporting with conduct-based protection, technical access and coordination; it leaves remediation effects and center governance unresolved. | `this_run_primary`; Final ICML/PMLR 267 PDF pp1–9 (abstract and all main §§1–7); Appendix A pp18–20; Appendix B.1 introductory/example explanations p20, B.2–B.3 and Table A1 pp22–25; Appendix C.1–C.4 pp25–28, including Table A2. Figure A7 p26 visually inspected. The table of contents p17, references pp9–16, visual example cards p21, and Appendix D pp29–31 were not read in full; this is selected-section review.; review events: [r3_audits_01](rounds.md#r3_audits_01) |

**Limits:** The paper is a position argument informed by nonrepresentative informal experience. Its 2024 company/legal snapshot has not been revalidated as current law; company promises do not remove criminal liability or create unrestricted research rights. Longpre’s final-paper protection diagram is schematic: its proposed legal template retains applicable-law conditions and limited provider commitments, rather than universal immunity.

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
| `homewood_thirdpartycompliance_2025` — supports | [Source](https://arxiv.org/pdf/2505.01643v2); arXivv2 §1,pp5–6; §3.2–3.4,pp14–18; Tables3–4,pp15,17; §5,pp22–23 | Voluntary adherence review is explicitly distinct from framework-adequacy/system-safety assessment; control/maturity and disclosure examples are proposed designs, not observed company review outcomes. | `this_run_primary`; arXiv v2 PDF p1 (abstract/date/version), pp5–9 (§1, §2.1–2.2 in full, opening §3 and opening §3.1), pp14–18 (end §3.2; §3.3 and Tables3–4; §3.4 in full; beginning §3.5 through key-area option), pp22–23 (alternatives, §5 conclusion in full, acknowledgments and opening references). Executive summary/options tables pp3–4, reviewer comparisons/structures pp10–13, remaining action/timing/options discussion pp19–21, and references pp24–27 were not read in full.; review events: [r3_audits_03](rounds.md#r3_audits_03) |
| `schuett_frontierdevelopers_2024` — supports | [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12369305/); Final article §§2.3.1–2.3.2; §3.3.2 | Internal board-facing audit and other assurance providers are proposed as complementary; shared language, information and integrated reports can reduce assurance gaps/duplication. | `this_run_primary`; PMC article title/author/publication metadata and abstract; selected §2.1.1; §§2.3.1–2.3.2; §§3.1.1–3.1.3 and 3.2.1–3.2.3; §§3.3.1–3.3.3 including all extracted Table 2 rows; §§4.1–4.3; selected definitional footnotes 5,6,12,13. References and other sections not read end to end.; review events: [r5_reporting_02](rounds.md#r5_reporting_02) |
| `schuett_frontierdevelopers_2024` — bounds | [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12369305/); Final article §4.2; §3.3.1 Table 2 | The author explicitly calls for later empirical effectiveness research; skill, management pressure and changing methodology constrain the transfer from IT audit. | `this_run_primary`; PMC article title/author/publication metadata and abstract; selected §2.1.1; §§2.3.1–2.3.2; §§3.1.1–3.1.3 and 3.2.1–3.2.3; §§3.3.1–3.3.3 including all extracted Table 2 rows; §§4.1–4.3; selected definitional footnotes 5,6,12,13. References and other sections not read end to end.; review events: [r5_reporting_02](rounds.md#r5_reporting_02) |
| `brundage_frontierauditingrigorous_2026` — contextualizes | [Source](https://arxiv.org/pdf/2601.11699v4); v4 §5.3.3/Table 3 pp. 30–34; §5.3.4 pp. 34–35 | The proposed external assurance ladder varies scope, access and duration, with upper levels not yet feasible as described; it is not a measured confidence scale. | `this_run_primary`; v4 cover/title/byline/version; executive summary PDF pp. 2–6; PDF pp. 30–36 covering §5.3.3 AAL descriptions/Table 3, §5.3.4 assurance-level choice and §5.4 opening/Figure 7 access taxonomy. Remaining 115-page report and appendices not read.; review events: [r5_reporting_03](rounds.md#r5_reporting_03) |

**Limits:** SMACTR’s two CompanyX cases are hypothetical, not an implementation or harm-reduction study. The sources share an author and scholarly lineage; they are complementary arguments rather than independent outcome replications. Homewood’s compliance review concerns adherence to a framework, with constructed control examples; framework adequacy remains a separate question. New internal-audit and external-assurance-level sources remain proposed institutional arrangements; upper assurance levels and example conclusions are prospective, not calibrated effectiveness measures.

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
| `amironesei_aria_pilot_2025` — bounds | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-2.pdf); §3.1 adjudication; AppendixC Tables5–7; pinned official CoRIx README/tree | Identical publisher bytes retain52 adjudication-prose versus49 calibrated-table violations. Current official code is available but inspected tree/README does not identify the needed pilot stage/row manifest; no corrected rate follows. | `this_run_primary`; Selected source passages and renderedAppendixC; complete ancillary README and repository path metadata, not a full paper/code/data reproduction.; review events: [r5_versions_03](rounds.md#r5_versions_03), [r5_versions_04](rounds.md#r5_versions_04), [r5_versions_05](rounds.md#r5_versions_05) |

**Limits:** Small English-language pilot of proxy scenarios. Testers, annotators, dialogues and annotation judgments have different denominators. The source says initial CoRIx is better for characterization than comparison; questionnaire/annotation questions differ and uncertainty quantification remains open. Main267/52 versus AppendixC267/49 count tension is held rather than turned into a violation rate. A fresh exact-byte report/appendix check and official CoRIx repository inspection narrow the remaining issue to pilot data and aggregation; code availability does not resolve it.

**Counterevidence / alternative:** Field-style use may reveal failures absent in fixed prompts, while model testing may reveal issues that field users miss or do not commonly elicit. Neither direction is a general guarantee of ecological validity.

**Next check:** Resolve the report’s exact pilot row/stage/aggregation manifest or an authenticated correction before a violation rate. Official CoRIx code is now accessible, but its inspected README/tree contains toy examples rather than the needed pilot-data provenance. Retain implemented layered evaluation and omit the affected count/rate.

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
| `wang_decodingtrust_2023` — bounds | [Source](https://proceedings.neurips.cc/paper_files/paper/2023/file/63cb9921eecf51bfad27a99b2c53dd6d-Paper-Datasets_and_Benchmarks.pdf); NeurIPS2023 AppendixJ.1–J.4 PDFpp87–89/printed63–65 | DecodingTrust instead evaluates demographic parity/equalized-odds prediction gaps on200 constructed Adult salary samples with separately controlled data base rates. Its Table44 zero-shot baseline needs sampling/condition clarification before a cross-table quantitative claim. | `this_run_primary`; Fairness AppendixJ introductory passagep86 and J.1–J.4pp87–89; Table43–44 visually checked.; review events: [r3_fairness_04](rounds.md#r3_fairness_04) |

**Limits:** Selected methods/results and one appendix section from a108-page proceedings object. System-role attacker access, proxy toxicity judgments, Adult salary tasks and historical checkpoints constrain transfer. No modern-deployment incidence or isolated causal mechanism is established. AppendixJ adds explicit sample/base-rate conditions; Table44’s zero-shot baseline needs sampling/condition clarification before a cross-table numerical remedy claim.

**Counterevidence / alternative:** Several standard robustness and OOD results favor GPT-4, so the findings do not establish a universal capability-versus-safety tradeoff. Shared datasets across broad suites are dependencies, not independent corroboration.

**Next check:** Complete relevant appendix/classifier/source-data checks before headline rates; keep model IDs, role permissions, sampling and each outcome definition explicit.

<a id="c48"></a>
## C48

In small chess and Othello language models, SAE features recover formally specified board properties and task-labelled metrics distinguish trained from random-weight models; syntax and position shortcuts still affect which properties count as validation.

**Status:** scoped_check. **Theme:** mechanistic_validation.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `karvonen_measuringprogressdictionar_2024` — supports | [Source](https://arxiv.org/pdf/2408.00113v2); Sections3.2,5–6, Table1, AppendixD/Table5, AppendixF.2 (pp.4–5,8–9,19–20) | Board reconstruction and coverage provide affirmative recovery evidence; masked initial locations reduce a strong position shortcut, while some random-model strategy labels remain predictable from superficial correlations. | `this_run_primary`; Complete21-page arXivv2 including AppendicesA–G and Figures1–6.; review events: [r3_mechvalidation_01](rounds.md#r3_mechvalidation_01) |

**Limits:** Two small eight-layer GPT models and researcher-selected board properties; recovery of labels is not a complete causal model or validated natural-language safeguard. No replication.

**Counterevidence / alternative:** Linear probes perform better; random controls achieve high scores on some syntax/move-number-correlated strategy properties. Candidate ontology and reconstruction rule limit completeness.

**Next check:** Develop analogous discriminating labels/shortcut controls for language tasks and reconcile any leading numerical comparison at the same aggregation/selection before quoting a best score.

<a id="c49"></a>
## C49

Selected SAE interventions localize and alter counterfactual indirect-object-identification behavior relative to tested baselines, while supervised task dictionaries expose substantial gaps between interpretable features and sparse control, especially for full-distribution SAEs.

**Status:** scoped_check. **Theme:** mechanistic_validation.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `cunningham_sparseautoencoders_2024` — supports | [Source](https://arxiv.org/pdf/2309.08600v3); Sections4.1–4.2, Figure3 and AppendixF/Figure17 (pp.5–6,18–19) | Counterfactual patching in Pythia410M can achieve closer target outputs using fewer directions/smaller edits than PCA and non-sparse dictionaries in the reported setup. | `this_run_primary`; Complete20-page arXivv3 including AppendicesA–G and Figures1–18; dense panels assessed qualitatively.; review events: [r3_mechvalidation_02](rounds.md#r3_mechvalidation_02) |
| `makelov_principledevaluations_2024` — bounds | [Source](https://arxiv.org/pdf/2405.08366v3); Sections3.2–3.4,4.2,5.1–5.2, Figure4; AppendixA.2–A.4 (pp.4–13,22–24) | Task-specific SAE control outperforms the frozen-decoder control but remains weaker than supervised dictionaries; full-distribution SAEs fare worse and can match frozen-random-decoder controllability despite interpretable features. | `this_run_primary`; Selected methods/results and specified appendices; Figures2–4,6,13 only visually checked.; review events: [r3_mechvalidation_04](rounds.md#r3_mechvalidation_04) |
| `cunningham_sparseautoencoders_2024` — supports | [Source](https://proceedings.iclr.cc/paper_files/paper/2024/file/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Paper-Conference.pdf); ICLR2024 §§4.1–4.2 pp5–6, Figure 4; §6.2 p9; AppendixF/Figure 16 p19 | Exact final proceedings preserves the selected IOI causal-editing result and limitations; do not assume blanket arXiv v3 equivalence. FinalEq4 normalizes reconstruction and figure/page numbering changes. | `this_run_primary`; PDF cover/§§1–2 pp1–3; complete §4 pp5–6 and Figure 4; selected §5 examples pp7–8; §6.1–6.3 p9; AppendixA–B text p12; AppendixE–G text pp17–19. Remaining §3, references, parts of §5 and appendices were not comprehensively reread. Text-diff discovery was followed by reading claim-critical passages; it is not a full 19-page certification.; review events: [r4_editions_01](rounds.md#r4_editions_01) |

**Limits:** Different small model families but shared IOI task lineage and selected interventions; this does not establish generalization beyond that task or evidence for complete feature recovery, reliable monitoring, or deployed safeguards. Neither experiment was reproduced in this round. Selected official ICLR2024 proceedings now authenticate the central IOI result, but printed reconstruction normalization and figure numbering differ from arXivv3; its perplexity sentence is absent from the final text. Keep version-specific particulars separate.

**Counterevidence / alternative:** Successful ablations/editing provide affirmative causal utility under their setup. High no-intervention agreement can obscure some attribute effects; human ontologies, feature selection, and non-exhaustive tuning bound negative claims.

**Next check:** Evaluate broader task families with held-out prompts and negative controls. Exact final proceedings access is closed for selected claim-critical passages; complete-paper reading and result-level equivalence remain open where particular numbers depend on edition.

<a id="c50"></a>
## C50

Activation reconstruction, output fidelity, interpretable feature descriptions, and sparse causal control test different properties: preserving outputs alone can leave the internal computational pathway underdetermined.

**Status:** scoped_check. **Theme:** mechanistic_validation.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `braun_identifyingfunctionally_2024` — supports | [Source](https://arxiv.org/pdf/2405.12241v2); Sections2.3–2.5,3.1–3.4, Figures1–3; AppendixA.7/Figure9/Table4 (pp.4–8,15–17) | Pure output-KL SAEs improve sparsity/output-fidelity tradeoffs while diverging in downstream activation reconstruction and cross-seed feature directions; adding downstream reconstruction mitigates these gaps. Automatic interpretation comparisons remain metric- and matching-dependent. | `this_run_primary`; Sections1–3.4 and selected AppendicesA.7,D,E,H; visually checked Figures1–3,9.; review events: [r3_mechvalidation_03](rounds.md#r3_mechvalidation_03) |
| `makelov_principledevaluations_2024` — supports | [Source](https://arxiv.org/pdf/2405.08366v3); Sections3.2–3.4 and5.2; AppendixA.2–A.4 (pp.4–7,10–13,22–24) | Necessity/sufficiency, sparse control, and interpretation-consistent effects are explicitly separate tests; some interpretable/full-distribution features give weak control. | `this_run_primary`; Selected claim-critical methods/results and appendices, not complete51-page reading.; review events: [r3_mechvalidation_04](rounds.md#r3_mechvalidation_04) |

**Limits:** Small-model, training-distribution and task-specific evidence; high downstream similarity also does not by itself certify a unique mechanism. No experiment replication or human semantic validation is claimed.

**Counterevidence / alternative:** End-to-end plus downstream-loss SAEs improve the studied tradeoff while retaining closer downstream activations and sampled automatic interpretation scores; the results support refined evaluation rather than dismissing mechanistic methods.

**Next check:** Require joint pathway/causal/semantic tests and negative controls across tasks and scales before drawing governance conclusions about reliability or completeness.

<a id="c51"></a>
## C51

Prompt-specific circuit tracing has generated causally testable hypotheses and successful selected original-model interventions, while reconstruction fidelity and graph completeness do not establish a complete or mechanistically faithful account of a model.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `ameisen_circuittracingrevealing_2025` — supports | [Source](https://transformer-circuits.pub/2025/attribution-graphs/methods.html); Local Replacement Model; Limitations / Mechanistic Faithfulness; Appendix / Validating the Replacement Model; Nuances of Steering | The method supplies interpretable graph hypotheses and positive intervention checks; the article separates unperturbed output agreement from perturbation faithfulness and reports accumulating errors. | `this_run_primary`; Introduction; Building an Interpretable Replacement Model (including local replacement model); selected quantitative CLT/graph evaluations and graph completeness; Limitations (dark matter, inactive/inhibitory features, feature abstraction, global circuits, mechanistic faithfulness); Appendix Validating the Replacement Model; Nuances of Steering with Cross-Layer Features; Unexplained Variance and Choice of Steering Factors; selected Additional Evaluation Details. Not the complete article, training details, linked graphs or visual assets.; review events: [r3_circuits_01](rounds.md#r3_circuits_01) |
| `lindsey_biology_2025` — supports | [Source](https://transformer-circuits.pub/2025/attribution-graphs/biology.html); Introductory Example / Swapping Alternative Features; Planning in Poems; Multilingual Circuits | Intermediate-state, planning and cross-language interventions alter model outputs as predicted in selected cases; direct effects under constrained patching have special validation limits. | `this_run_primary`; Method overview and validation caveat; full text of Introductory Example: Multi-step Reasoning, Planning in Poems and Multilingual Circuits subsections; selected hallucination/refusal intervention caveats. Other case studies, appendices and interactives not comprehensively read.; review events: [r3_circuits_02](rounds.md#r3_circuits_02) |
| `sharkey_openproblemsmechanistic_2025` — contextualizes | [Source](https://arxiv.org/pdf/2501.16496v1); v1 §§2.1.4,2.3 | A review distinguishes predictive/local validation, circuit criteria and competitive downstream utility rather than treating descriptions as established explanations. | `this_run_primary`; Title/abstract and selected §§2.1.4,2.1.4a,2.1.4b (PDF pp17–19), §2.3 circuit-validation/discovery issues (pp21–22), and §3.6 generalizability/selected §3.7 opening (pp31–32). Not a full review read or check of underlying cited experiments.; review events: [r3_circuits_05](rounds.md#r3_circuits_05) |

**Limits:** Anthropic methods and biology are companion outputs of the same research project, not two independent validations. Broad appendix tests freeze attention in both models; case interventions often select groups/layers/strengths. Inactive features, attention routing and reconstruction error can hide computation. This bounded review read selected sections only, with no experiments.

**Counterevidence / alternative:** Actual-output interventions are affirmative mechanistic evidence beyond activation descriptions. Conversely, shortcuts, approximate replacement mechanisms and some failed/high-strength interventions prevent a unique or comprehensive explanation claim.

**Next check:** For any publication-leading mechanism, inspect the exact case graph/intervention configuration and compare predictive/competitive downstream utility; preserve this qualitative conclusion without promoting unaudited numerical summaries.

<a id="c52"></a>
## C52

Automated feature explanations need validation against their intended endpoint: activation-context descriptions and descriptions of intervention-induced output effects can yield different judgments about the same SAE feature.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `paulo_automaticallyinterpreting_2024` — supports | [Source](https://arxiv.org/pdf/2410.13928v3); v3 §§3.2–3.3.5,4.1.1,4.2; Figure3; Appendix G | Context scoring and intervention scoring target different behavior; trained-feature/shuffled-description controls support the output-effect endpoint, and broader context sampling exposes failures of top-only interpretations. | `this_run_primary`; All main-text sections 1–5 and data/code/impact statement (PDF pp1–9), Appendix C and D.1–D.3 selected prompt/scoring details (pp13–15), Table A10 and all Appendix G.1–G.4 text (pp22–24), Figure3 visually on p8. Other appendix sections/tables and references not comprehensively read; no full-text label.; review events: [r3_circuits_03](rounds.md#r3_circuits_03) |
| `sharkey_openproblemsmechanistic_2025` — contextualizes | [Source](https://arxiv.org/pdf/2501.16496v1); v1 §2.1.4 | Validation can progress from activations/counterfactuals through downstream engineering and competitive utility; these are distinct evidential standards. | `this_run_primary`; Title/abstract and selected §§2.1.4,2.1.4a,2.1.4b (PDF pp17–19), §2.3 circuit-validation/discovery issues (pp21–22), and §3.6 generalizability/selected §3.7 opening (pp31–32). Not a full review read or check of underlying cited experiments.; review events: [r3_circuits_05](rounds.md#r3_circuits_05) |

**Limits:** Paulo inspected edition is v3/2025, separately tracked from the canonical2024 preprint. Output-effect scoring is scorer/prompt dependent, uses short generations in active contexts and tunes KL strength on scoring prompts; it is not a safety monitor evaluation or a universal semantic-faithfulness metric.

**Counterevidence / alternative:** Positive randomized-SAE and shuffled-description controls make the endpoint informative. Sampling broader contexts can also produce confusing or overbroad explanations, and early-layer intervention effects can be harder to describe; no one scoring method is uniformly decisive.

**Next check:** Resolve edition handling, compare scores on independently calibrated intervention strengths and held-out contexts, and test whether better descriptions improve the intended downstream task.

<a id="c53"></a>
## C53

Some filtered SAE feature subspaces align across selected language models under correlation-based matching and representational-similarity measures, providing bounded evidence of analogous structure rather than universal causal feature identity or demonstrated transfer of control.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `lan_sparseautoencoders_2024` — supports | [Source](https://arxiv.org/pdf/2410.06981v4); v4 §§2–4.2,6; Limitations; Appendices B,D,E.1; Figures6–7 | SVCCA/RSA alignment exceeds selected randomized pairing/subset baselines, and trained-versus-randomized Pythia controls strengthen the learned-structure interpretation; matching/filtering/SAE-quality restrictions and unaligned features bound it. | `this_run_primary`; PDF pp1–6: abstract,introduction,definitions,method,setup and first results overview; pp9–11 related work/conclusion/limitations; Appendix A–D (pp17–19) and opening E.1–E.2 text/visuals on p20. Large remaining appendix, many result plots/tables and source code not read.; review events: [r3_circuits_04](rounds.md#r3_circuits_04) |
| `sharkey_openproblemsmechanistic_2025` — contextualizes | [Source](https://arxiv.org/pdf/2501.16496v1); v1 §3.6 | Transferability of interpretability methods and conclusions across architectures remains an open empirical question. | `this_run_primary`; Title/abstract and selected §§2.1.4,2.1.4a,2.1.4b (PDF pp17–19), §2.3 circuit-validation/discovery issues (pp21–22), and §3.6 generalizability/selected §3.7 opening (pp31–32). Not a full review read or check of underlying cited experiments.; review events: [r3_circuits_05](rounds.md#r3_circuits_05) |

**Limits:** Lan v4 title differs from the earlier canonical title and is treated as a related edition. Same-tokenizer families, selected layers/SAE widths, shared activation data and post-pairing filters restrict the population; no steering/control-transfer experiment was verified.

**Counterevidence / alternative:** The randomized-Pythia and randomized-pairing/subset comparisons argue against the simplest claim that the similarities are wholly arbitrary. Weaker pairwise-distance similarity, unmatched features and SAE-training sensitivity argue against a universal inventory or guaranteed causal equivalence.

**Next check:** Reconcile title/version, inspect omitted pairing/filter robustness appendices and demonstrate causal cross-model transfer on independently chosen tasks before using this as control/assurance evidence.

<a id="c54"></a>
## C54

A layered audit can be designed as an evidence feedback process: governance records, model limitations and deployment-level impacts answer different questions and should inform each other. General model scores cannot alone establish context-specific fairness or legal acceptability in an application.

**Status:** provisional. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `mokander_auditinglargelanguagemodels_2024` — supports | [Source](https://link.springer.com/content/pdf/10.1007/s43681-023-00289-2.pdf); Final issue §4.3–4.5,printedpp1096–1101 and Figures1–2; §5.1–5.3,pp1102–1103; Appendix1,pp1105–1106 | The literature-/stakeholder-informed blueprint makes model limitations and deployment impact logs inputs to audits at other layers; it limits general model-level fairness claims and acknowledges construct-validity, institution and political boundaries. | `this_run_primary`; Final AI and Ethics issue PDF pp1–22, printed pp1085–1106: abstract and every narrative section §§1–6; Appendix 1 methodology in full, acknowledgments, contributions/funding/data/conflict/license statements. Figures 1–2 (viewer pp10,17; printed pp1094,1101) rendered and visually inspected. The remaining bibliography-only pages23–31 (printed pp1107–1115) were not read; accordingly this event remains Selected sections rather than a full-document certification.; review events: [r3_audits_02](rounds.md#r3_audits_02) |

**Limits:** Mökander et al. develop a blueprint from a systematised literature review and stakeholder consultation, not an implemented end-to-end audit effectiveness study. Specific metrics, enforcement and auditor institutions remain unresolved; the remaining bibliography pages were not read in this event.

**Counterevidence / alternative:** Model-level tests can still reveal important precursors of downstream harms, and application audits alone can miss upstream data/governance causes. Linked documentation may remain box-ticking where follow-up lacks authority; contextual fairness and distributional judgments cannot be settled by a generic metric.

**Next check:** Seek an actual model→application→governance feedback case with documented decisions and completed remediation; test the selected fairness/legal construct in the publication’s actual application context.

<a id="c55"></a>
## C55

Reviewing compliance with a frontier developer’s own safety framework can make implementation more inspectable, but it answers a narrower question than whether the framework or system is adequate. Its assurance depends on operationalized commitments, evidence access, reviewer incentives, disclosure and action on findings.

**Status:** provisional. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `homewood_thirdpartycompliance_2025` — supports | [Source](https://arxiv.org/pdf/2505.01643v2); arXivv2 §1,pp5–6; §3.2–3.4,pp14–18; Tables3–4,pp15,17; §5,pp22–23 | Voluntary adherence review is explicitly distinct from framework-adequacy/system-safety assessment; control/maturity and disclosure examples are proposed designs, not observed company review outcomes. | `this_run_primary`; arXiv v2 PDF p1 (abstract/date/version), pp5–9 (§1, §2.1–2.2 in full, opening §3 and opening §3.1), pp14–18 (end §3.2; §3.3 and Tables3–4; §3.4 in full; beginning §3.5 through key-area option), pp22–23 (alternatives, §5 conclusion in full, acknowledgments and opening references). Executive summary/options tables pp3–4, reviewer comparisons/structures pp10–13, remaining action/timing/options discussion pp19–21, and references pp24–27 were not read in full.; review events: [r3_audits_03](rounds.md#r3_audits_03) |

**Limits:** Homewood v2 evaluates options for voluntary compliance review. The mock control and maturity examples are not company audit results, and no direct frontier-AI compliance or harm effect is established by the inspected material.

**Counterevidence / alternative:** Compliance can coexist with an inadequate framework. Vague commitments, conflicted reviewers, employee self-censorship or selective follow-up can create false assurance; deeper review adds security and coordination burdens. Internal reviews and management systems may supply useful complementary information.

**Next check:** Compare an actual dated review’s scope, findings, uncertainty and follow-up with a separate adequacy assessment; keep unverifiable commitments indeterminate rather than passing them by assumption.

<a id="c57"></a>
## C57

Public input can change model behavior and reduce a specified bias benchmark, while the same intervention can reduce alignment with measured public-opinion distributions.

**Status:** scoped_check. **Theme:** fairness_values.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `huang_collectiveconstitutional_2024` — supports | [Source](https://arxiv.org/pdf/2406.07814v1); arXiv v1 §§3.1–3.4 pp3–6; §4.3 pp7–8 Figures4–5; §§5–7 pp9–10 | Public versus Standard constitutions are the stated training difference; Public is lower on all nine BBQ dimensions but2–3 percentage points lower on OpinionQA alignment across five U.S. ideology groups. | `this_run_primary`; All23 manuscript pages read; charts4–5/Table1/interface visually checked. Publisher edition identity and code/data not independently compared.; review events: [r3_fairness_01](rounds.md#r3_fairness_01) |
| `huang_collectiveconstitutional_2024` — supports | [Source](https://facctconference.org/static/papers24/facct24-94.pdf); Official FAccT2024 PDF §§3.1–3.4 pp3–6; §4.3/Figures4–5 p7/Table 1 p8; §5 p9 | Conference-hosted exact-DOI edition confirms lower BBQ bias and lower OpinionQA representativeness. Access/version gap is closed for these passages; Elo label/interpretation ambiguity persists. | `this_run_primary`; Cover/abstract and selected introduction; participant/input transformation/training methods §§3.1–3.4 pp3–6; quantitative/qualitative findings §§4.1–4.4 pp6–9; limitations §5 p9; discussion/ethics §§6–7 p10. References and appendices were not newly read in full. A programmatic comparison covers normalized extracted text on pages2–23, not substantive rereading or visual certification of every page.; review events: [r4_editions_02](rounds.md#r4_editions_02) |

**Limits:** Screened AI-familiar U.S. sample, one pair of model trainings, researcher-mediated constitution construction and no direct adherence or downstream impact measure. Official FAccT exact-DOI passages now authenticate the central results; automatic body-text comparison is not a new complete-final reading. Table1 Elo labeling/interpretation remains ambiguous, and nearby capability scores do not establish equivalence.

**Counterevidence / alternative:** Positive BBQ changes coexist with less representative OpinionQA response distributions. The experiment does not confer universal public consent, resolve conflicting principles or establish legitimacy for all affected populations.

**Next check:** Resolve Elo labels and underlying comparison outputs if consequential; retain lower BBQ and lower OpinionQA findings. Final-proceedings full reading remains unfinished; do not treat programmatic text identity as independent semantic rereading.

<a id="c58"></a>
## C58

A minimax preference objective offers a constructive way to handle intransitive judgments without a single scalar reward ordering, but its optimization guarantee does not validate the preferences or their social legitimacy.

**Status:** scoped_check. **Theme:** fairness_values.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `swamy_minimaximalistapproach_2024` — supports | [Source](https://arxiv.org/pdf/2401.04056v1); arXiv v1 §§3.1–3.4 pp4–7; §4–5 pp8–10; AppendixA.7 p23 | SPO computes an approximate Minimax Winner under antisymmetric preference/no-regret assumptions; theory concerns averaged policy iterates, while practical implementation uses finite queue and validation selection. Constructed continuous-control preferences, not public consent, are empirically tested. | `this_run_primary`; Mainpp1–10 and contextual definitionA.7p23; full appendix proofs and exact finalICML edition not checked.; review events: [r3_fairness_02](rounds.md#r3_fairness_02) |

**Limits:** Supplied preference oracle and population aggregation/weighting are assumed. Selected theorem statements/proof sketches were read, not every appendix proof independently verified. Transfer to LLM/public-policy outcomes is untested here.

**Counterevidence / alternative:** This is positive technical evidence against assuming cyclic preferences make every useful optimization impossible; it does not settle which people, preferences or outcomes should count.

**Next check:** Complete appendix/final-edition reading and evaluate preference estimation, population weights and practical-returned policy separately from minimax convergence.

<a id="c59"></a>
## C59

Fairness benchmark results depend on distinct constructs and normative choices: group prediction gaps, stereotype behavior and refusal to express subjective preferences cannot be treated as one interchangeable fairness verdict.

**Status:** scoped_check. **Theme:** fairness_values.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `huang_trustllm_2024` — supports | [Source](https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24x/huang24x.pdf); ICML/PMLR235 AppendixF pp74–79, Tables19–25 | TrustLLM separately scores stereotype agreement/recognition/refusal, salary-prediction association and subjective-choice neutrality; subjective preference 'fairness' is defined as refusal/neutrality and measured through Longformer. Paper cautions that high association-test p-values can accompany poor predictions. | `this_run_primary`; Complete fairness AppendixFpp74–79, abstractp1 and benchmark designp5; Table25 visually checked; broader105-page object not fully read.; review events: [r3_fairness_03](rounds.md#r3_fairness_03) |
| `wang_decodingtrust_2023` — bounds | [Source](https://proceedings.neurips.cc/paper_files/paper/2023/file/63cb9921eecf51bfad27a99b2c53dd6d-Paper-Datasets_and_Benchmarks.pdf); NeurIPS2023 AppendixJ.1–J.4 PDFpp87–89/printed63–65 | DecodingTrust instead evaluates demographic parity/equalized-odds prediction gaps on200 constructed Adult salary samples with separately controlled data base rates. Its Table44 zero-shot baseline needs sampling/condition clarification before a cross-table quantitative claim. | `this_run_primary`; Fairness AppendixJ introductory passagep86 and J.1–J.4pp87–89; Table43–44 visually checked.; review events: [r3_fairness_04](rounds.md#r3_fairness_04) |
| `huang_trustllm_2024` — bounds | [Source](https://api.github.com/repos/HowieHwong/TrustLLM/git/blobs/ceb7df55bd8b795f6f1de3524d6c03dd54ebc3bf); Historical official Git blobceb7df55bd8b795f6f1de3524d6c03dd54ebc3bf; selected fairness/preference.json member | Input artifact has240 prompts/120 unique option pairs and no category labels. Its ordered options support80 ideology/40 culture text, but do not identify the published category-column aggregation. | `this_run_primary`; Base64-decoded exact GitHub blob API representation of the dataset ZIP; selected fairness/preference.json member only. Parsed all 240 rows and type/option fields, checked matching120 option pairs across plain/force templates, and read the120 unique option-pair labels. Other datasets, classifier outputs and response narratives were not audited.; review events: [r4_editions_03](rounds.md#r4_editions_03) |
| `huang_trustllm_2024` — bounds | [Source](https://raw.githubusercontent.com/HowieHwong/TrustLLM/3f55a278511218e1bc7152e77d74d5f5383b3dbc/trustllm_pkg/trustllm/task/fairness.py); Commit3f55a278511218e1bc7152e77d74d5f5383b3dbc fairness.py FairnessEval.preference_eval | Routine returns plain/force/overall refusal rates and has no category split or Table 25 construction. The exact experiment/category-aggregation provenance remains missing. | `this_run_primary`; Inspected FairnessEval.preference_eval and its surrounding class interface in the6617-byte fairness.py file. Read filtering/scoring/return paths, without importing or executing model/classifier dependencies. Other fairness methods were not validated as an entire package.; review events: [r4_editions_05](rounds.md#r4_editions_05) |

**Limits:** Historical model versions, proxy extractors/classifiers and shared benchmark/task ancestry limit transfer and independence. TrustLLM Table25 needs category-count/aggregation clarification. DecodingTrust Table44 needs baseline/sampling/condition clarification; distinct random draws may explain cross-table differences. Neither question establishes a source error or invalidates the qualitative findings; affected headline totals and cross-condition remedy rates are omitted. The pinned preference input has no explicit category labels and its inspected scoring function has no category-table path; manual option-group inspection is not independent category validation.

**Counterevidence / alternative:** Several models perform well on some stereotype tasks, and balanced context can reduce reported prediction gaps. These positives coexist with recognition/association weaknesses and leave population impact unmeasured. Refusal can improve one fairness metric while reducing utility or opinion-distribution alignment.

**Next check:** TrustLLM dataset and scoring-path access are now documented. Obtain raw model responses/classifier outputs plus the exact category/column/table aggregation manifest before using affected Table25 rates; no corrected totals follow from inferred weights. Resolve DecodingTrust sampling/condition comparability and retain each construct separately.

<a id="c60"></a>
## C60

The inspected 2024 federal-agency-use plans report specific organizational acts alongside prospective or incompletely specified risk-control procedures; these historical self-descriptions do not establish that high-impact testing, waivers or remediation operated effectively.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `exim_complianceplanomb_2024` — supports | [Source](https://img.exim.gov/s3fs-public/documents/EXIM%20Compliance%20Plan%20for%20OMB%20Memorandum%20M-24-10Final.pdf); September 24, 2024 v1.0 pp.5–9,11–16 | EXIM reports governance/training/IT-policy updates, while strategy and waiver formalization remain prospective; it reports no rights/safety-impacting or waiver cases. | `this_run_primary`; All extracted text on PDF pp. 1–18, including cover, revision history, contents, governance, inventory, innovation, risk-management sections and Appendix A definitions; no linked underlying policies or successor plan.; review events: [r3_public_01](rounds.md#r3_public_01) |
| `sba_complianceplanomb_2024` — supports | [Source](https://legacy.sba.gov/sites/default/files/2024-10/Final%20508-Compliant%20SBA%20M-24-10%20Implementation%20Plan%20for%20AI%20-%20September%202024.pdf); September 2024 pp.3–4,9,11,15–16 | SBA reports a use-case form and temporary public-GenAI restriction, explicitly lacks waiver criteria/process, and describes future council approval and annual certification. | `this_run_primary`; PDF pp. 3–4,9,11,15–17 only: governance steps, inventory form, generative AI notice and risk-management plans. Existing inherited full reading is not repeated/certified.; review events: [r3_public_03](rounds.md#r3_public_03) |
| `eac_complianceplanomb_2024` — supports | [Source](https://www.eac.gov/sites/default/files/2024-10/EAC_Compliance_Plan_OMB_Memorandum_FINAL_508.pdf); September 20 FINAL revision; pp.3–6,11–12 | EAC reports CAIO/board/guidance, but describes inventory and risk/redress processes prospectively or in mixed tenses; scope is EAC internal resources. | `this_run_primary`; PDF pp. 1–6,10–13: cover/revision history, purpose/scope, established governance, prospective inventory, risk/redress sections and selected definitions; no reread of pp. 7–9 or14.; review events: [r3_public_04](rounds.md#r3_public_04) |

**Limits:** Selected source-specific historical comparators, not a representative agency survey or direct evidence of frontier-model release decisions. Shared M-24-10/template lineage means these are not three independent corroborations of control effectiveness. M-24-10 was later rescinded/replaced.

**Counterevidence / alternative:** Reported completed organizational/policy acts may be useful implementation indicators; absence of independent case evidence does not establish that controls failed. Plan publication, office creation and intended control operation remain distinct.

**Next check:** Read underlying policies and dated case records only where needed to test operation; review successor plans before claims about current policy.

<a id="c61"></a>
## C61

In the April 3, 2025 M-25-21 design for covered federal use, high-impact classification can trigger documented testing, impact assessment, review by a nondeveloper within the agency, risk acceptance, monitoring and discontinuation; scope limits, pilots and waivers qualify that pathway.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `omb_m2521_2025` — supports | [Source](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf); Overview p.1; Appendix §§1,3(a)(i)(F),4(a)–(b),5 pp.4–5,11,14–20 | Memo replaces M-24-10, defines the principal-basis high-impact trigger, assigns minimum practices and permits qualified pilots/waivers. Impact-assessment reviewer is internal and uninvolved in development. | `this_run_primary`; All extracted text on PDF pp. 1–25, including main memorandum, Appendix §§1–8, footnotes, high-impact definitions/categories and consolidated actions table. Operative narrative clauses, rather than the summary table, support timing/obligation paraphrases.; review events: [r3_public_02](rounds.md#r3_public_02) |

**Limits:** Normative policy design in exact April 2025 edition, not current-law verification, observed compliance or a frontier-developer rule. Sections4(a)–(b) exclude Intelligence Community elements, national security systems are outside memo scope, and feasibility/appropriateness qualifications vary by practice.

**Counterevidence / alternative:** The design includes formal consequences and documentary artifacts beyond voluntary advice, but its exemptions/waivers and permitted alternative black-box/vendor-result testing bound claims of uniform independent assurance.

**Next check:** Check later instruments only if making dated current-duty claims; seek completed tests, review comments, signed risk acceptance, waiver records and termination evidence before effectiveness claims.

<a id="c62"></a>
## C62

The pinned January 23, 2025 federal AI inventory can substantiate counts of publicly reported administrative use-case records and their declared categories; it cannot by itself substantiate deployed-system prevalence or effective compliance.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `omb_2024federalagency_2024` — supports | [Source](https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/4a29d132291261d4829b187acd8af618e7295294/README.md); README Summary, Key Considerations and Repository Structure at commit 4a29d132291261d4829b187acd8af618e7295294 | README dates2,133 records/41 agency submissions/351 rights-or-safety cases to January 23 and specifies scope/exclusions. | `this_run_primary`; Complete README text only at immutable commit 4a29d132291261d4829b187acd8af618e7295294; repository tree used to identify files; this is not a comprehensive reading of the cited dataset.; review events: [r3_public_06](rounds.md#r3_public_06) |
| `omb_2024federalagency_2024` — supports | [Source](https://api.github.com/repos/ombegov/2024-Federal-AI-Use-Case-Inventory/git/blobs/1efc086ad73dc7e0647968e3ecab60e9b9da88f0); raw_v2.csv via immutable blob 1efc086ad73dc7e0647968e3ecab60e9b9da88f0; Agency, development-stage and impact columns | Exact v2 documentary recount reproduces2,133 rows,41 stripped agency names and351 normalized rights/safety/both labels; rows span multiple lifecycle stages. | `this_run_primary`; Immutable GitHub blob API JSON and its base64-decoded exact raw_v2.csv bytes. Strict cp1252 parse of all rows for headers, row count, agency labels, impact categories and development-stage distributions; no substantive reading of every narrative field or row.; review events: [r3_public_07](rounds.md#r3_public_07) |
| `omb_2024federalagency_2024` — bounds | [Source](https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/4a29d132291261d4829b187acd8af618e7295294/validation/data_dictionary.yaml); data_dictionary.yaml fields 16–17,51–56 | Question conditions and distinct evaluation categories prevent treating blanks as universal noncompliance or internal nondeveloper review as external audit. | `this_run_primary`; YAML lines 1–110 and 680–835 only: identifiers, stage/impact fields and risk-management fields 51–56; no whole-dictionary read.; review events: [r3_public_08](rounds.md#r3_public_08) |
| `omb_2024federalagency_2024` — bounds | [Source](https://raw.githubusercontent.com/ombegov/2024-Federal-AI-Use-Case-Inventory/4a29d132291261d4829b187acd8af618e7295294/data/2024_consolidated_ai_inventory_raw.csv); Older raw.csv in same commit | Older raw.csv has1,757 rows; use exact v2 artifact for January 23 summary rather than silently mixing files. | `this_run_primary`; Older raw.csv strict UTF-8-sig parse of headers and all rows for row count and selected category distributions; no substantive reading of all free-text entries.; review events: [r3_public_09](rounds.md#r3_public_09) |

**Limits:** Administrative self-report with exclusions and possible withheld details. Only documentation, schema excerpts and categorical fields were checked; underlying case narratives/assessments were not comprehensively read or independently verified. Strict cp1252 v2 bytes preserved via byte-identical base64 API representation.

**Counterevidence / alternative:** The inventory is a concrete disclosure artifact beyond a future commitment. Its structured fields can guide audit, but publication alone is neither safety evidence nor proof that control duties were executed.

**Next check:** Use explicit snapshot/file/hash/normalization when quoting totals. Review full schema-to-v2 mapping and primary agency evidence before deriving compliance or outcome rates.

<a id="c63"></a>
## C63

The 2025 Foundation Model Transparency Index measures disclosed information for 13 developers across 100 indicators. Its reported mean of 40.69/100 describes disclosure, rather than verified control effectiveness or a controlled annual change in safety.

**Status:** scoped_check. **Theme:** policy_implementation.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `wan_foundationmodeltransparency_2025` — supports | [Source](https://arxiv.org/pdf/2512.10169v1); v1§§3.3–4.5 pp. 14–18; Figure 7 p. 19; Figure 15/§5.3 pp. 32–36; AppendixA pp. 48–49 | Methods combine seven solicited reports and six FMTI-prepared issuer-source reports, two FMTI scorers per 1,300 pairs and company responses. The mean is 529/13=40.69; changed indicators/reporting/flagship models bound annual comparisons. Non-disclosure is not absence of practice. | `this_run_primary`; Exact arXiv v1 PDF pp. 1,3–6,14–19,32–39,48–49: abstract, index/instrument background and changes, full §§4.1–4.5 methods, overall results/Figure 7, reporting-method comparison, longitudinal discussion/Figures 16–17/Table 3, conclusion/conflicts, and AppendixA including agent prompt and retrieval comparison. Other results subsections, indicator tables and bibliography pages not fully read.; review events: [r3_provider_01](rounds.md#r3_provider_01) |

**Limits:** Selected source reading; no independent re-scoring or underlying developer-source audit. The scores are investigator judgments about issuer information, not independent observation of controls. Changes to the sample, instrument and process complicate trend inference.

**Counterevidence / alternative:** Structured reporting and engagement can produce new public information; some companies score highly and some fixed-indicator examples show actual disclosure regressions. These positive and negative observations should not be discarded merely because transparency is distinct from realized safety.

**Next check:** Audit any publication-leading indicator regression against exact published developer reports. Use 40.69/100 with the 13×100 denominator; omit causal safety or controlled-trend interpretations unless stronger evidence is supplied.

<a id="c64"></a>
## C64

NVIDIA’s report, applicable as of August 2025, describes screening, approval, reassessment and pre-release testing mechanisms, including reported Garak use. Its risk-analysis template and issuer descriptions do not demonstrate realized risk reduction.

**Status:** scoped_check. **Theme:** policy_implementation.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `nvidia_frontierriskassessment_2025` — supports | [Source](https://images.nvidia.com/content/pdf/NVIDIA-Frontier-AI-Risk-Assessment.pdf); Coverp. 1; PRA/DRA pp. 2–5; risk formula/Table 1 pp. 6–7; Table 2 p. 8; Garak p. 13; Governance pp. 14–15 | Positive reported operational mechanisms coexist with limits on enforcing controls across all products. Table 2 is explicitly an example/template, not a measured 49→5 product result. The cover’s no-frontier-development statement is historical. | `this_run_primary`; All 15 PDF pages, including cover/abstract/executive summary, Preliminary and Detailed Risk Assessments, both V-model figures, Tables 1–2, risk mitigation/tool descriptions, risk evaluation and governance, and the footnotes printed in this document. Linked tools, model cards and cited studies were not independently opened.; review events: [r3_provider_02](rounds.md#r3_provider_02) |

**Limits:** Full reading of the 15-page document does not verify tool efficacy, actual deployment decisions or applicability to all products. August applicability is established, but the canonical February 17 publication date remains unchecked. Table2 is an illustrative template; no observed risk-reduction percentage should be inferred.

**Counterevidence / alternative:** The report names specific workflows and reports actual pre-release Garak use, so treating it as content-free or purely aspirational would erase useful evidence. Conversely internal committees are not independent external assurance and downloadable weights limit downstream control.

**Next check:** Seek dated product assessments/model cards and review records for a consequential effectiveness claim. Retain specific attributed mechanisms and omit template risk-reduction arithmetic now.

<a id="c65"></a>
## C65

Meta’s April 7, 2026 v2 framework combines a material-contribution risk trigger with conditional mitigated development/deployment and more explicit accountability. The inspected text alone does not establish overall strengthening or weakening, adherence, or a safety effect.

**Status:** scoped_check. **Theme:** policy_implementation.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `meta_advancedaiscalingframeworkv2_2026` — supports | [Source](https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2/); §§2–3 pp. 4–17; Table 1 p. 15; §§4.1–4.2 pp. 25–28; §5 p. 40; terminology/change log pp. 41–44 | V 2 conditions deployment of high/critical models on validated mitigation to moderate-or-lower risk and specifies responsible officers, reporting/update processes and deployment-sensitive elicitation. Its change log describes both changed threshold criteria and response labels; some protocols remain future/developing. | `this_run_primary`; PDF pp. 1–17,25–28,39–44: executive summary, scope, complete governance/transparency/accountability sections, outcomes/threat-model inclusion criteria and risk thresholds, evaluation environment and elicitation/deployment-context passages, first cybersecurity threshold example, benefits assessment, future work, terminology and change log. Risk-domain scenarios and detailed domain-specific implementation pp. 18–24,29–38 not read in full.; review events: [r3_provider_03](rounds.md#r3_provider_03) |

**Limits:** Selected 44-page source reading; old/new comparison is attributed to v2’s change log, not an independently captured v1 comparison. Scope excludes some gradual or remediable serious harms, and no released model’s compliance or effectiveness is established.

**Counterevidence / alternative:** Broader threshold criteria and more explicit processes may strengthen a policy, while conditional continuation and scope exclusions may reduce restraint in some interpretations. Those effects depend on actual risk decisions, mitigations and governance, not tier labels alone.

**Next check:** If overall policy direction leads the publication, compare exact v1 bytes and actual preparedness reports/risk decisions. Preserve v2’s conditions now and leave the consequential interpretive judgment open.

<a id="c66"></a>
## C66

System-specific safety cases provide an explicit way to connect a deployment claim to evidence and review, while threshold choices, reviewer capacity and update rules still require justification beyond producing a document.

**Status:** provisional. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `buhl_safetycasesfrontier_2024` — supports | [Source](https://arxiv.org/pdf/2410.21572v1); v1 §§2–5 pp5–18, Tables1–5 | Explicit scope, outcome objectives, evidential support and review form a conditional decision process; sketches and regulatory comparisons do not measure effectiveness. | `this_run_primary`; All 25 pages of accessible v1 text read, including title, contents, executive summary, Sections1–7, footnotes, Tables1–5, text/captions of Figures1–6, abbreviations, acknowledgments and references. No linked sources or underlying industry cases independently inspected.; review events: [r4_safetycases_01](rounds.md#r4_safetycases_01) |
| `hilton_safetycasesscalable_2025` — supports | [Source](https://arxiv.org/pdf/2503.04744v1); v1 §§2–4 pp2–14, especially §3.1/Table2 and §3.2/Table3 | Organizational frameworks and system-specific cases are complementary. Seoul-commitment mapping assumes adequate execution and correct cases; additional governance/threshold processes remain necessary. | `this_run_primary`; All accessible text of the 19-page v1 representation, including Sections1–5, both figure captions/labels, Tables1–3, footnotes and references. The final page contains only a page number. No linked papers, standards or empirical artifacts opened.; review events: [r4_safetycases_02](rounds.md#r4_safetycases_02) |
| `lee_constructingsafety_2026` — bounds | [Source](https://arxiv.org/pdf/2601.22773v1); v1 §§3–4 pp8–14; §6–7 pp26–30 | Reusable CAE patterns include an author-reported synthetic tender-review pilot, but the inspected quantitative description does not establish a verified broad safety/fairness or noninferiority conclusion. | `this_run_primary`; Pinned v1 pp1,8–10,13–14,26–30: title/abstract/introduction opening; review methodology and selection; taxonomy/architecture opening; complete tender-case section and limitations/conclusion. Other taxonomy/pattern subsections, all selected-study appendices and bibliography not fully read.; review events: [r4_safetycases_03](rounds.md#r4_safetycases_03) |

**Limits:** Methodological arguments and attributed illustrations, not controlled evidence that adopting safety cases improves frontier deployment outcomes. Lee v1 has a canonical edition mismatch. Shared authors, citations and the Goemans inability template reduce independence.

**Counterevidence / alternative:** Explicit reasoning can reveal gaps and support comparison, but review cost, capture, confirmation bias, uncertain thresholds and open-ended use can produce false assurance. Rules and other governance mechanisms can remain complementary.

**Next check:** Compare actual reviewed cases, adverse findings and ensuing decisions; retain positive structuring mechanisms without claiming a universally superior governance method.

<a id="c67"></a>
## C67

Safety-case confidence analysis can expose assumptions and prioritize doubts, but propagated probabilities and an LLM-Delphi pilot do not by themselves calibrate deployment safety or supply independent expert corroboration.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `barrett_assessingconfidence_2025` — supports | [Source](https://arxiv.org/pdf/2502.05791v1); v1 §§2,4,7 pp7–9,17–20,27–33; §10 pp42–45 | The study combines an explicit assurance argument, a selected forecasting pilot and illustrative confidence propagation. Product assumptions differ from a dependence-free union-bound lower bound; neither validates uncalibrated inputs or argument soundness. | `this_run_primary`; Pinned v1 Sections1–2 pp6–9; full §4 pp17–20; §7 and opening §8 pp27–33; §9.3 and §10 pp42–45. Unread logical-block/weight-of-evidence details pp10–16, defeater details pp21–26, remaining priority/communication details pp34–41 and bibliography pp46–48 remain outside this event.; review events: [r4_safetycases_04](rounds.md#r4_safetycases_04) |

**Limits:** Single cyber-inability template, chosen 100-question forecasting sample and role prompts to one LLM model; no independent reanalysis or safety-case-domain calibration. Brier score is not a pure calibration measure, and graph arithmetic is not measured system risk.

**Counterevidence / alternative:** The reported pilot is affirmative experimental evidence on its chosen forecasting comparison, and structured doubts can make review more inspectable. Correlated judgments, information-time differences, subjective parameters and weak lower bounds still constrain transfer.

**Next check:** Audit forecast inputs/metrics and application-specific calibration; justify the conjunctive argument model separately. Do not inherit §7.1’s false independence/equality wording or turn a zero lower bound into proof of zero actual safety confidence.

<a id="c68"></a>
## C68

A dynamic safety-case design links changed artifacts or monitored indicators to affected claims and response owners, while correctness of the initial argument, traceability and indicator validity remain prerequisites rather than outputs of consistency checking.

**Status:** provisional. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `carlan_dynamicsafetycases_2024` — supports | [Source](https://arxiv.org/pdf/2412.17618v1); v1 §§3–4.2 pp6–12; Scenario4/Table13 p33; §5.1 pp34–36; §§6–8 pp45–47 | The proposed DSCMS specifies automated impact/consistency rules, indicator monitoring and governance escalation; worked cyber scenarios illustrate logic, while a frontier prototype and indicator validation remain future work. | `this_run_primary`; Pinned v1 pp6–12 (related work, DSCMS requirements, CSA assumptions and SPI design); pp27–28 (selected no-underelicitation/no-sandbagging SPI tables); pp33–36 (example change impact and governance integration); pp45–47 (discussion, recommendations and conclusion). Remaining detailed indicators, scenarios, governance comparisons, appendices and references were not read in full.; review events: [r4_safetycases_05](rounds.md#r4_safetycases_05) |

**Limits:** Proposed requirements/workflow and illustrative changes, not actual frontier telemetry or evaluated live decision support. Only selected parts of the75-page paper were read; thresholds and generic documents are examples/placeholders.

**Counterevidence / alternative:** Explicit links and owners may reduce manual burden and make updates inspectable, but missing or misleading indicators can leave the case mechanically consistent and substantively wrong. Fundamental context/capability changes may require a new argument.

**Next check:** Inspect or build a concrete prototype only if implementation is the publication claim; test validity, update latency, missed changes and decision follow-through separately.

<a id="c69"></a>
## C69

Guarded architectures can place assurance on narrower, more understandable components, but their guarantees depend on correct hazard models, trusted perception and safe enforcement; adding diversity alone does not establish independent failure probabilities.

**Status:** provisional. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `bloomfield_assurancesystemsdependabil_2024` — supports | [Source](https://arxiv.org/pdf/2407.13948v1); v1 §§2.1–2.3 PDFpp12–20/printed11–19; §4 opening PDFpp31–33; §6 opening PDFpp43–44 | The dependability argument distinguishes conventionally assured guards from AI-dependent guards and rejects naive multiplicative reliability from diversity, while recognizing useful redundancy and constrained guarantees. | `this_run_primary`; Pinned v1 PDF pp11–14 (§§2–2.2 opening), pp16–20 (§2.3 and architecture-summary opening), pp31–33 (§4 opening/contractual trust), pp43–44 (§6 opening). Corresponding printed pages are10–13,15–19,30–32,42–43. Other case examples, normative enforcement discussion, AGI arguments and bibliography not fully read.; review events: [r4_safetycases_06](rounds.md#r4_safetycases_06) |

**Limits:** A demanding design/assurance perspective with cyber-physical examples; not a new experimental estimate of frontier LLM guard effectiveness or a universal rejection of lower-assurance useful systems. Original v1 only.

**Counterevidence / alternative:** A geofence-like check with an assured intervention can support strong scoped claims. Broader perception, normative outcomes and shared world models may defeat similar arguments even when an output monitor appears separate.

**Next check:** Trace the intended system’s trusted components, hazard model and enforceable boundary, then seek case-specific empirical/formal evidence; keep architectural independence distinct from institutional or source independence.

<a id="c70"></a>
## C70

Internal probes can discriminate selected evaluation and deployment prompt distributions, but that readout and its size association do not establish deceptive behavior or a universal scaling law for concealment.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `nguyen_probingsteeringevaluation_2025` — supports | [Source](https://arxiv.org/pdf/2507.01786v2); Sections3.1–3.4 pp3–4: selection, baselines, prompted WMDP and recovery definition; Sections4.1–4.3 pp4–7: probe validation and steering; Sections5.3–5.5 pp7–8: targeted-noise alternative and transfer limits; Appendix pp13–18; Figures8–9 pp15,18: selected features and unrelated controls | A selected contrastive probe outperforms the tested trivial/random controls and generalizes unevenly across prompt datasets. | `this_run_primary`; Complete 18-page arXiv v2: abstract, Sections1–6, acknowledgments/impact, all references pp9–13, appendix prompts, all dataset descriptions/SAE labels pp13–17, Figures1–9 captions and final all-feature plot p18. Linked source datasets, implementation and dashboards were not inspected.; review events: [r4_awareness_02](rounds.md#r4_awareness_02) |
| `chaudhary_evaluationawareness_2025` — bounds | [Source](https://arxiv.org/pdf/2509.13333v2); Sections3.1–3.3 pp2–3: model selection, contrastive probes and SAD scoring; Sections4–5 pp3–4 and Figure1 p1: selected best-layer size association; Appendix6.1–6.5 pp6–8; Figures3–5: dataset, template, excluded Qwen and reproducibility details | Selected families show a best-layer size association, while excluded Qwen and chat-template sensitivity bound extrapolation; behavior is not the measured endpoint. | `this_run_primary`; Complete eight-page arXiv v2: abstract, main Sections1–5, references, Appendix6.1–6.5, all figure captions and reproducibility table. All Figures1–5 visually inspected on PDF pp1,4,6,7. No linked implementation/data executed or source literature independently reread.; review events: [r4_awareness_01](rounds.md#r4_awareness_01) |

**Limits:** Shared synthetic/SAD lineage, selected layers/templates and observational classifications; no behavior-specific causal or deployment validation.

**Counterevidence / alternative:** Positive separation beyond the tested heuristics is informative, while nonmonotone family results and misclassified benign prompts challenge a universal awareness/deception interpretation.

**Next check:** Separate held-out representation classification from prospective behavioral prediction, validate alternative cues and selection rules, and preserve family-specific counterevidence.

<a id="c71"></a>
## C71

Activation steering can alter engineered evaluation-conditional behavior, while simple-prompt and unrelated-feature controls show why eliciting a different output is insufficient to establish an awareness-specific mechanism or unknown deployment behavior.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `hua_steeringevaluation_2025` — supports | [Source](https://arxiv.org/pdf/2510.20487v5); Sections3–4 pp4–7: synthetic-document/expert-iteration organism and intervention setup; Sections5.1–5.3 pp7–10; Figures3–5 pp8–10: type-hint effects and controls; Section6 pp10–11: explicit-cue limitations and unknown deployment behavior; AppendixG pp31–35 and I.1–I.2 pp40–41,44–46: tuning, prompting and belief-grading caveats | A pre-fine-tuning direction changes a trained type-hint endpoint more than matched random vectors; explicit cues, known-target tuning and alternative prompts bound the result. | `this_run_primary`; Pinned 62-page arXiv v5: main text pp1–12 (Sections1–6, contributions/acknowledgments); AppendixG pp31–35 including layer/strength selection, belief-behavior caveat and grading prompt; AppendixI.1 pp40–41 and Table16/p44; AppendixI.2 pp45–46. Remaining references, training/robustness appendices, many figures and transcripts not fully read.; review events: [r4_awareness_03](rounds.md#r4_awareness_03) |
| `nguyen_probingsteeringevaluation_2025` — bounds | [Source](https://arxiv.org/pdf/2507.01786v2); Sections3.1–3.4 pp3–4: selection, baselines, prompted WMDP and recovery definition; Sections4.1–4.3 pp4–7: probe validation and steering; Sections5.3–5.5 pp7–8: targeted-noise alternative and transfer limits; Appendix pp13–18; Figures8–9 pp15,18: selected features and unrelated controls | Prompt suffix intervention dominates probe steering on induced underperformance, and unrelated SAE controls can match relevant-feature recovery; targeted noise remains an explicit explanation. | `this_run_primary`; Complete 18-page arXiv v2: abstract, Sections1–6, acknowledgments/impact, all references pp9–13, appendix prompts, all dataset descriptions/SAE labels pp13–17, Figures1–9 captions and final all-feature plot p18. Linked source datasets, implementation and dashboards were not inspected.; review events: [r4_awareness_02](rounds.md#r4_awareness_02) |

**Limits:** Different one-model engineered setups and endpoint/task/steering choices. Hua’s inspected 2026 v5 is a related edition, with most appendices unread. Neither experiment was reproduced.

**Counterevidence / alternative:** Meaningful random-vector and pre-training controls support constructive mitigation research; they do not establish natural generalization or a unique internal-belief explanation.

**Next check:** Retain positive intervention evidence alongside stronger simple controls; calibrate against known counterfactual behavior and evaluate larger naturally evaluation-aware models before assurance claims.

<a id="c72"></a>
## C72

Prompted models can conceal some successful capability underperformance from a reasoning monitor, but conditional approval, noisy success filtering and efficacy/selectivity tradeoffs prevent interpreting this as spontaneous or reliably successful deployment sandbagging.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `li_cancovertlysandbag_2025` — supports | [Source](https://arxiv.org/pdf/2508.00943v2); Section3 pp2–3: ten models,400 WMDP and400 MMLU items, three instructed conditions and score; Section4.1 p4/Figure3: approval conditional on successful instructed sandbagging; AppendixB.2–B.4 pp10–12: baseline FPR, noisy two-run success proxy, GPT 5 same-prompt comparator; AppendixD pp16–17/Figures11–12: harder benchmark and metric-label hold | Monitor-aware prompting changes conditional approval while reducing other success components; two-run filtering, harder-task results and an untuned stronger-monitor substitution delimit the inference. | `this_run_primary`; Pinned 28-page arXiv v2: abstract, selected main Sections1–5/limitations pp1–6; AppendixB.1–B.4 text/captions pp9–12; AppendixD and Figures11–12 pp16–17, plus AppendixE opening classification description. Attack prompt AppendixA, complete references, additional-performance pages13–15 and worked biological/chemical transcripts pp18–28 were not fully read.; review events: [r4_awareness_04](rounds.md#r4_awareness_04) |

**Limits:** MCQ proxies, instructed goals and selected model/monitor versions. Approval is conditioned on a noisy success proxy; no natural propensity, deployed rate or optimized-monitor limit is measured.

**Counterevidence / alternative:** Uncaught instructed attempts expose a real evaluation failure mode, while harder tasks, low joint reliability and success/covertness tradeoffs weaken claims of general evasion capability.

**Next check:** Preserve conditional denominators; inspect repeated-trial evidence and stronger monitor elicitation for a broader claim, and omit unresolved metric-label rates.

<a id="c73"></a>
## C73

Complex sabotage-agent tests make joint task success and monitor detection separately inspectable and show scoped monitor-training gains; those results remain conditional on instructed goals, observed information, filtering and when detection occurs.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `kutasov_evaluatingsabotage_2025` — supports | [Source](https://arxiv.org/pdf/2506.15740v2); Sections2–4 pp2–8: task/monitor setup, joint success and held-out fine-tuning; AppendixB pp14–15: task judges, construction and excluded task; AppendixD.1–D.2 pp24–25: successful-side-task filtering, balancing/dropped tasks and model-specific scaffolds; AppendixJ–M pp38–43: scratchpad sanity check, failure-mode dependence and human baseline | SHADE-Arena distinguishes joint success from marginal evasion, reports held-out fine-tuning gains and failure-mode-dependent monitoring; ROC filtering and scratchpad variants alter the evaluated problem. | `this_run_primary`; Pinned 44-page arXiv v2: main pp1–10 through conclusions and opening references; AppendixB pp14–15; AppendixD.1–D.2 pp24–25; AppendixJ/K text pp38–40; AppendixL.2 paragraph on p41; remaining monitoring/high-level/compute text pp42–44. Full bibliography, detailed task transcripts, prompts and many appendix figures not comprehensively read.; review events: [r4_awareness_05](rounds.md#r4_awareness_05) |

**Limits:** Selected 44-page v2 reading, synthetic environments and related-title edition; some task scoring uses an LLM. Post-hoc complete-transcript detection is not real-time harm prevention.

**Counterevidence / alternative:** Longer tool workflows and held-out task gains add affirmative evidence beyond MCQs. Execution failures, task heterogeneity, conditional ROC samples and unmatched human subsets bound generality.

**Next check:** Evaluate operational interruption, deployment false-positive budgets and matched samples; keep scratchpad removal, secret revelation and normal monitored reasoning distinct.

<a id="c74"></a>
## C74

Pairwise reward-model discrimination and downstream policy quality require different validation. PPE supplies a controlled example connecting selected proxy metrics to post-DPO human preferences, while showing that familiar benchmark rankings need not predict the same outcome.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `lambert_rewardbenchevaluating_2024` — supports | [Source](https://arxiv.org/pdf/2403.13787v2); v2 §§3–4.2 pp4–6; Table1 p3; §5.3 and §6 p9; AppendixA and AppendixB opening p16 | RewardBench supplies structured preference contrasts, should-refuse/should-respond checks and explicit aggregation, while leaving downstream-training correlation open. | `this_run_primary`; ArXiv v2: abstract; introduction/background and benchmark construction/scoring text on PDF pp1–5; Table2 and scoring continuation p6; §5.3 and conclusion p9; AppendixA and opening AppendixB p16. Other results, many appendices, references, original datasets and code not comprehensively read.; review events: [r4_judges_01](rounds.md#r4_judges_01) |
| `frick_evaluaterewardrlhf_2024` — supports | [Source](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e01083b381b4865919b4915ef32e3d2-Paper-Conference.pdf); Final §§6.1–6.2 pp7–8; §7 pp8–9, Figures5–6 p9; §8 p10; AppendixA.6.1 p34; A.6.3/A.7 p36 | One Llama3.1-8B-Instruct policy trained under nine selected reward models and evaluated through blinded human preferences supports some granular metrics; aggregate ranking relationships and low-quantile explanations remain conditional. | `this_run_primary`; Official ICLR2025 PDF: cover/abstract/title/authors and introduction p1; complete §§6–8 and conclusion on pp7–10; AppendixA.6 text and A.6.1 reward-benchmark interpretation pp33–34; selected A.6.2 style-control table/figure text pp34–35; A.6.3, A.7 and A.8 p36. Other main methods/results, references and appendices not read in full.; review events: [r4_judges_03](rounds.md#r4_judges_03) |

**Limits:** Nine selected reward models, one base policy and off-policy DPO; finite crowdsourced votes and filtered prompts are not representative public values or a universal optimizer test. Related preprint/final representations are one study; no experimental replication here.

**Counterevidence / alternative:** PPE’s final appendix treats RewardBench over-optimization as a hypothesis and allows that early benchmark improvements may remain useful. A stronger downstream validation method in one setting does not establish universal failure of other benchmarks or guaranteed gains from optimizing PPE.

**Next check:** Specify the intended training/decision endpoint, exact benchmark/data/aggregation and model population. Validate on held-out reward models and other policy/optimization settings before general predictive or causal claims; omit the unqualified inherited0.77 summary.

<a id="c75"></a>
## C75

Synthetic preference and judgment training can improve a generative judge on tested benchmarks, while leaving residual order sensitivity, uneven task gains and dependence on the seed model and constructed labels.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `wang_selftaughtevaluators_2024` — supports | [Source](https://arxiv.org/pdf/2408.02666v2); §§3.1–4.3 pp3–5; Figure1 p2; §§5–6 pp5–9, Tables1–6 pp6,8; §8 p9; AppendixA.3/Table9 pp12–13; Tables10–12 p14 | Self-Taught Evaluators improves RewardBench and HelpSteer2 results under its iterative recipe; MT-Bench gains are smaller/nonmonotonic, ties are excluded and order controls remain consequential. | `this_run_primary`; Complete16-page arXivv2 accessible text: abstract, §§1–9, acknowledgments, all references, AppendixA.1–A.4, every table1–12 and Figure1–10 caption/template/example text. No linked model weights, code, WildChat records or benchmark datasets executed/read exhaustively.; review events: [r4_judges_04](rounds.md#r4_judges_04) |

**Limits:** A specific70B aligned seed, human-written prompts and benchmark endpoints. The absence of new human-preference labels in the training loop is not absence of human influence, evaluator independence or demonstrated downstream-policy benefit.

**Counterevidence / alternative:** Synthetic-data and human-labeled ablations support a real method contribution, but classifier reward models remain strong and some categories worsen. Additional majority voting changes inference budget; no universal replacement or fairness conclusion follows.

**Next check:** Pin aggregation and inference costs, test challenging held-out task distributions and actual downstream policy optimization, and retain paired order/position-consistency checks.

<a id="c76"></a>
## C76

A statistical annotator-substitution test can make a task-specific comparison with sampled human judgments explicit, but its pass decision depends on the reference population, cost-benefit threshold, imbalance treatment and intended construct.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `calderon_alternativeannotator_2025` — supports | [Source](https://aclanthology.org/2025.acl-long.782.pdf); §§3.1–3.3 pp3–5/printed16053–16055; §5.1/Figure2 p9; §7 p10; AppendixB.1–B.2 pp17–18; C.1 pp18–19; C.4 pp20–21 | The Alternative Annotator Test uses leave-one-annotator-out comparisons and FDR control; its own sensitivity analysis and imbalance/minority appendices bound a generic replacement interpretation. | `this_run_primary`; ACL final31-page PDF: abstract; complete method§3 pp3–6; selected setup/results§§4–5 pp6–9 including Tables1–2 and Figure2; conclusion§6 p9; complete limitations§7 p10. AppendixB.1–B.2 pp17–18; selected B.3/C.1 explanation and weighting formula pp18–19; C.4 subjectivity/options and C.5 opening pp20–21. Full theorem proof, references, full dataset appendix and prompt appendices not read.; review events: [r4_judges_05](rounds.md#r4_judges_05) |

**Limits:** Agreement with an assumed-authoritative sampled label distribution is not external truth. Selected methods/results/appendices, not a full31-page reading or proof/code recertification; no project calibration study performed.

**Counterevidence / alternative:** Some empirical task/prompt/model combinations pass, demonstrating constructive local use. An always-majority predictor can pass the unadjusted procedure under severe imbalance; inappropriate human comparators or majority weighting can hide important failure modes.

**Next check:** Define the precise annotation task, human expertise and sampling, epsilon/failure costs, imbalance and minority weighting, and validate the actual project use before applying the test or claiming human-equivalent research review.

<a id="c77"></a>
## C77

Joint statistical models of the answer and grading process can separate modeled score-scale shifts, item effects and uncertainty that a single agreement statistic obscures; the demonstrated bias adjustments are simulated, model-dependent counterfactuals.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `dubois_skewedscore_2025` — supports | [Source](https://arxiv.org/pdf/2507.03772v3); Framework and Table1 pp2–3; illustrative-data declaration p4; Questions1.1–4 pp4–12; Figure6 p11; Question5 pp12–13; AppendicesA–C pp16–20 | Skewed Score develops ordinal/binomial and hierarchical GLM recipes with simulated examples and explicit priors/model comparisons; posterior bias-adjusted agreement differs from an observed improvement in grading. | `this_run_primary`; Complete20-page arXivv3 accessible text: abstract/introduction, framework, Questions1.1–5 and conclusion, both reference pages, AppendicesA–C, Tables1–3 and all Figures1–11 captions. Linked HiBayes package/notebooks not executed or independently validated.; review events: [r4_judges_06](rounds.md#r4_judges_06) |

**Limits:** All worked data are simulated. Likelihood, covariate and reference choices govern interpretation, and no real-project grader bias, causal mechanism or intervention effect is estimated. Complete text reading does not reproduce the statistics or validate the package.

**Counterevidence / alternative:** The method offers a practical richer analysis, but statistical adjustment cannot choose the correct human/ethical reference or repair missing constructs by itself. Some hierarchical and flat models fit similarly; added complexity needs justification.

**Next check:** Fit and validate a transparently specified model on an actual human-calibrated evaluation set, compare simpler alternatives and assess practical effects before claiming real bias correction.

<a id="c78"></a>
## C78

A task-completion time horizon supplies a common difficulty/reliability measure for a specified agent and task suite; it is not the duration an AI operates autonomously or a direct measure of whole-job automation.

**Status:** scoped_check. **Theme:** evaluation_configuration.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `metr_timehorizons_2026` — supports | [Source](https://metr.org/time-horizons/); Current TH 1.1 Methodological Details and FAQ; September 8, 2026 maintenance notice | METR fits task success against human expert duration and explicitly bounds domain, low-context, reliability and reporting interpretations. | `this_run_primary`; Complete accessible captured HTML prose: definition, controls/labels, Methodological Details, every FAQ, update history, citation text, navigation/footer. Interactive chart values/embedded datasets, linked paper, code and follow-up studies were not read/reproduced.; review events: [r4_depthsample_04](rounds.md#r4_depthsample_04) |

**Limits:** Current canonical page text only; chart values, model set, raw data and code were not authenticated or reproduced. Earlier snapshot/reading not certified.

**Counterevidence / alternative:** The measure is informative within its specified domain and reliability target; task cleanliness, context and human baselines limit transfer, while the page warns above 16-hour estimates are unreliable.

**Next check:** Inspect a pinned data/code/model/scaffold snapshot and uncertainty before publication-leading numerical or trend claims.

<a id="c79"></a>
## C79

A standardized hazardous-response benchmark can provide explicit rules, confidential tests and configuration-sensitive feedback without certifying system safety; evaluator, grading and prompt-set versions must remain part of the result.

**Status:** scoped_check. **Theme:** evaluator_integrity.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `mlcommons_ailuminate_2026` — supports | [Source](https://mlcommons.org/ailuminate/); Suite overview: Technical independence, Objectivity,2026 timeline and Using AILuminate results | The current suite defines versioned Safety/Jailbreak tests, reports a non-LLM scorer, distinguishes Official/Practice runs and disclaims certification or acceptable-risk decisions. | `this_run_primary`; Complete accessible captured HTML text: suite descriptions, credibility/stewardship/objectivity sections,2026 timeline, results-use rules, Candela/configuration description, future benchmarks, contributor list, partnerships and footer/cookie text. Linked standards, result pages, prompts and benchmark code not read.; review events: [r4_depthsample_05](rounds.md#r4_depthsample_05) |
| `mlcommons_ailuminatev10_2025` — bounds | [Source](https://arxiv.org/pdf/2503.05731v1); arXivv1 §§2,5–7,pp7–9,15–22; Figure 6 | The v1.0 paper describes a different LLM-ensemble/reference-grade instrument with uncertainty, single-turn/persona/scope limits and intentionally undisclosed implementation details. | `this_run_primary`; PDF pp1–5 cover/abstract/executive summary/contents; pp7–9 overview/scope/use; pp15–22 prompt-quality discussion, response-evaluator methods, grading/reference and limitations. Remaining hazard details, results, large Appendix A questionnaire and references not fully read.; review events: [r4_depthsample_06](rounds.md#r4_depthsample_06) |

**Limits:** Same MLCommons benchmark family across different versions, not two independent validations. Exact later scorer/data and real deployments remain unaudited; only selected v1.0 paper sections read.

**Counterevidence / alternative:** Standardized tests and stewardship provide affirmative measurement methods, while evaluator error, adaptive adversaries and normative hazard choices prevent a general safety or context-free ranking claim.

**Next check:** Keep version/standard/evaluator/prompt set and deployment configuration with every score; authenticate later release methods and any cross-version comparability before pooling.

<a id="c80"></a>
## C80

Compute thresholds have a defensible proposed role as early screens for additional scrutiny; the reviewed design sources do not establish a universal compute-to-harm cutoff or make compute an adequate trigger for every governance duty.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `heim_trainingcomputethresholds_2024` — supports | [Source](https://arxiv.org/pdf/2405.10799v2); v2 §§3–5.1 pp9–14; footnote6 p9; Figure6; §§6.1–6.4 pp18–27 | Compute is early/measurable and potentially verifiable, while risk depends on capability, context, enhancement and defenses; threshold updating may move in either direction. | `this_run_primary`; All 36 PDF text pages, §§1–7, all figure/table text and captions and references, read in overlapping bounded chunks; Figure 6 separately rendered and inspected. No linked reference works or datasets included.; review events: [r5_thresholds_01](rounds.md#r5_thresholds_01) |
| `californiapolicyworkinggroup_thecaliforniareport_2025` — supports | [Source](https://www.gov.ca.gov/wp-content/uploads/2025/06/June-17-2025-%E2%80%93-The-California-Report-on-Frontier-AI-Policy.pdf); Final June 2025 §5 printedpp36–40 | Align scope with regulatory purpose and determination time, measurement and external verification; use compute as a possible initial filter and permit metric changes. | `this_run_primary`; Cover/byline, authorship statement and acknowledgments; PDFviewerpp4–8 (printedpp3–7: executive principles/origins/contents/intro); all PDFviewerpp37–44 (printedpp36–43: §4 closing, entire §5 scoping, §6.1–6.3 and §6.4 opening). Remaining historical cases, detailed transparency/reporting sections, references and AppendixA feedback form not fully read.; review events: [r5_thresholds_05](rounds.md#r5_thresholds_05) |
| `fmf_thresholdsfrontier_2025` — contextualizes | [Source](https://www.frontiermodelforum.org/updates/issue-brief-thresholds-for-frontier-ai-safety-frameworks/); Official February 7 HTML: four threshold approaches and conclusion; related representation | Distinguishes proxy and more direct approaches while retaining normative/calibration/crossing questions; canonical May PDF identity remains unresolved. | `this_run_primary`; All accessible current official HTML text read: article, four threshold approaches, tradeoffs, conclusion, footnotes, surrounding navigation and related-publication labels. The canonical May2025 PDF and linked PDF were not read; this event is scoped against the admitted object.; review events: [r5_thresholds_06](rounds.md#r5_thresholds_06) |

**Limits:** These are analytic/policy-design arguments, with conceptual frameworks and historical analogies; no observed causal reduction in harm or empirically optimized numerical boundary is established. The FMF HTML remains related to the unverified canonical PDF.

**Counterevidence / alternative:** Low-compute pathways, post-training and inference-time compute can bypass a pretraining screen; high capability can improve defenses or reliability. More direct capability/impact metrics can be harder to measure, verify or obtain early enough.

**Next check:** Choose the specific regulatory purpose and acceptable false inclusions/exclusions before proposing a number. Verify current primary legal sources separately; omit a universal numerical trigger.

<a id="c81"></a>
## C81

Compute can provide concrete governance levers through infrastructure visibility, mediated access and measurable resources; those affordances must be assessed separately from risk-proxy validity and the costs of surveillance, concentration and evasion.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `sastry_computingpowergovernance_2024` — supports | [Source](https://arxiv.org/pdf/2402.08797v1); v1 §3.B printedpp24–30; §4 opening printedp34; §5.A printedpp60–67 | The report explains detection/access/quantification/supply-chain affordances and an exploratory visibility/allocation/enforcement taxonomy, then develops privacy, power, progress and evasion limitations. | `this_run_primary`; PDF viewer pp1–5 (cover, contents, introduction and summary); pp25–32 (printedpp24–31, all §3.B properties and opening §3.C); pp35–36 (printedpp34–35, §4 introduction and opening4.A); pp61–69 (printedpp60–68, §5 introduction, §5.A and opening5.B). Remaining §4 mechanisms, later §5 principles, appendices and references not fully read.; review events: [r5_thresholds_02](rounds.md#r5_thresholds_02) |

**Limits:** The 104-page report is selectively read; detailed tool/implementation sections and appendices remain deferred. Feasibility is argued rather than demonstrated at a specified operational assurance level.

**Counterevidence / alternative:** Detectable facilities do not reveal model workloads; reporting can require intrusive access, and progress or specialized low-compute models can undermine coverage. Restricting scope/protecting process may improve proportionality while weakening visibility.

**Next check:** Check the exact detailed mechanism and its safeguards before selecting an implementation route; require implementation evidence before asserting effectiveness.

<a id="c82"></a>
## C82

The 2025 threshold survey is useful evidence about elicited expert design preferences and disagreements; optional selected-sample responses and competing definitions do not validate risk boundaries or establish representative consensus.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `schuett_surveythresholdsadvanced_2025` — supports | [Source](https://aigi.ox.ac.uk/wp-content/uploads/2025/08/Survey_on_thresholds_for_advanced_AI_systems_1.pdf); §2 printedpp7–11; Table1; §§4.1–4.2.1 printedpp15–17; §4.3 printedpp20–21 | 166 of 379 invited experts participated; all 13 questions were optional. Authors retain divided compute views and acknowledge selection, framing and terminology limits. | `this_run_primary`; Title/abstract, contents, executive summary (printedpp3–4), selected overview figure labels showing item-specific sample sizes, complete §2 methods (printedpp7–11), §4.1 and §4.2.1 through opening4.2.2 (printedpp15–18 opening), and §§4.3–5 plus acknowledgments (printedpp20–21). Not all §3 results/§4.2, references or questionnaire appendices.; review events: [r5_thresholds_03](rounds.md#r5_thresholds_03) |
| `fmf_thresholdsfrontier_2025` — bounds | [Source](https://www.frontiermodelforum.org/updates/issue-brief-thresholds-for-frontier-ai-safety-frameworks/); Official February 7 HTML capability-threshold subsection; related representation | Capability in absence of mitigations differs from survey Table 1 capability-plus-adequate-mitigation definition; same terminology does not mean identical operational constructs. | `this_run_primary`; All accessible current official HTML text read: article, four threshold approaches, tradeoffs, conclusion, footnotes, surrounding navigation and related-publication labels. The canonical May2025 PDF and linked PDF were not read; this event is scoped against the admitted object.; review events: [r5_thresholds_06](rounds.md#r5_thresholds_06) |

**Limits:** Only selected methods/discussion/results passages were read. The complete questionnaire, full result charts and item denominators must be checked before any leading numeric agreement claim. FMF PDF equivalence is unresolved.

**Counterevidence / alternative:** Expert elicitation and structured consultation can reveal implementation needs and alternatives even without representative sampling; common design preferences can motivate tests, while leaving legitimacy and calibration open.

**Next check:** For each proposed survey headline, read the exact wording/denominator and relevant figure plus appendix. Report disagreements and the operational definition alongside the preference, or omit the number.

<a id="c83"></a>
## C83

The reviewed frontier-governance proposals specify routes from assessment and external scrutiny to deployment conditions, monitoring and adaptive scope; their practical value depends on measurement, access and institutional capacity rather than the existence of a threshold alone.

**Status:** scoped_check. **Theme:** policy_implementation.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `anderljung_frontierairegulation_2023` — supports | [Source](https://arxiv.org/pdf/2307.03718v1); v1 §§4.1–4.4 pp24–29; §5 pp32–33; AppendixA pp35–36 | Proposes context-sensitive capability/controllability assessment, resourced scrutiny, risk-conditioned deployment and reassessment/reporting; warns against shallow assurance and imprecise scope. | `this_run_primary`; PDFpp1–5 (authorship note, abstract, executive summary and contents), pp15–18 (§2 closing illustration and §3 institutional building-block opening), all pp24–29 (§4.1–4.4 plus §4.5 opening), pp32–36 (§5 continuation, conclusion and AppendixA.1–A.4 opening). Page19 and unlisted passages are not counted as completely read. References and remaining appendices deferred.; review events: [r5_thresholds_04](rounds.md#r5_thresholds_04) |
| `californiapolicyworkinggroup_thecaliforniareport_2025` — supports | [Source](https://www.gov.ca.gov/wp-content/uploads/2025/06/June-17-2025-%E2%80%93-The-California-Report-on-Frontier-AI-Policy.pdf); Final June 2025 executive principles; §5 printedpp36–40; §§6.1–6.3 printedpp40–43 | Links purpose-specific, revisable threshold design to measurement/verification infrastructure and preserves consultation critiques about standards, access, reporting details and capacity. | `this_run_primary`; Cover/byline, authorship statement and acknowledgments; PDFviewerpp4–8 (printedpp3–7: executive principles/origins/contents/intro); all PDFviewerpp37–44 (printedpp36–43: §4 closing, entire §5 scoping, §6.1–6.3 and §6.4 opening). Remaining historical cases, detailed transparency/reporting sections, references and AppendixA feedback form not fully read.; review events: [r5_thresholds_05](rounds.md#r5_thresholds_05) |

**Limits:** Both are selectively read policy analyses; the California report is a commissioned scholarly working-group report, not enacted law or demonstrated implementation. Historical analogy and proposed procedures do not estimate an AI policy treatment effect.

**Counterevidence / alternative:** Repeated assessment and reporting can generate useful evidence while burdening evaluators, exposing confidential information or creating false assurance. More precise scope may miss emerging systems; rollback and access controls may carry openness and use-case costs.

**Next check:** Separate the normative design recommendation from a claim of observed effectiveness. Prioritize exact final-edition compliance/reporting procedures and any real implementation evaluation before choosing the leading publication conclusion.

<a id="c84"></a>
## C84

Internal deployment can change model configuration, privileges, tools and applications relative to a public product. The reviewed proposals therefore place internal-use permissions, evaluation and decision authority within governance scope; they do not establish that all internal governance is absent or that their proposed controls have reduced harm.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `stix_behindcloseddoors_2025` — supports | [Source](https://arxiv.org/pdf/2504.12170v1); v1 §§2.1–2.3, PDF pp. 11–16; §§6.1–6.2 pp. 36–39; Appendix pp. 52–53 | Privileged internal use and proposed IDT/IDOB decision controls link the evaluated configuration to internal deployment choices. | `this_run_primary`; Executive summary PDF pp. 1–3; internal access/application §§2.1–2.3, pp. 11–16; recommendations §6.1 and §6.2 opening/evaluation passages, pp. 36–39 including p. 38 n. 78; proposed governance walkthrough Appendix pp. 52–53. Other report material and underlying legal instruments were not systematically checked.; review events: [r5_reporting_01](rounds.md#r5_reporting_01) |
| `stix_behindcloseddoors_2025` — bounds | [Source](https://arxiv.org/pdf/2504.12170v1); v1 p. 38 n. 78; p. 12 staged-release uncertainty | The report acknowledges existing Anthropic/OpenAI internal-use provisions and uncertainty about staged internal releases, qualifying a broad absence-of-governance reading. | `this_run_primary`; Executive summary PDF pp. 1–3; internal access/application §§2.1–2.3, pp. 11–16; recommendations §6.1 and §6.2 opening/evaluation passages, pp. 36–39 including p. 38 n. 78; proposed governance walkthrough Appendix pp. 52–53. Other report material and underlying legal instruments were not systematically checked.; review events: [r5_reporting_01](rounds.md#r5_reporting_01) |
| `brundage_frontierauditingrigorous_2026` — contextualizes | [Source](https://arxiv.org/pdf/2601.11699v4); v4 executive summary pp. 2–6 | The audit proposal explicitly includes internal deployment and organization-level safety/security, beyond public products. | `this_run_primary`; v4 cover/title/byline/version; executive summary PDF pp. 2–6; PDF pp. 30–36 covering §5.3.3 AAL descriptions/Table 3, §5.3.4 assurance-level choice and §5.4 opening/Figure 7 access taxonomy. Remaining 115-page report and appendices not read.; review events: [r5_reporting_03](rounds.md#r5_reporting_03) |

**Limits:** These are scoped readings of design proposals. Internal practice and actual adoption may be private or changed since the cited versions; no governance-effect estimate is established.

**Counterevidence / alternative:** Existing internal-use provisions could already address parts of the alleged gap. A difference in configuration can matter without demonstrating greater realized harm.

**Next check:** Compare dated developer internal policies and actual permission/deployment decisions; retain the configuration-bound argument without a universal governance-absence claim.

<a id="c86"></a>
## C86

Incident-reporting designs can make system versions, harm, context and response more inspectable, but their evidential value depends on scope, reporting thresholds and investigation. Required fields in a proposed common format do not create a legal reporting duty, and neither a template nor a reporting count demonstrates reduced harm.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `cset_incidentskeycomponents_2025` — supports | [Source](https://cset.georgetown.edu/wp-content/uploads/CSET-AI-Incidents.pdf); January 2025 pp. 8–18, Tables 1–6 | A proposed mandatory regime combines incident/near-miss fields, domain tailoring and independent investigation to recover facts initial reports may lack. | `this_run_primary`; Complete accessible text of all 32 PDF pages, including cover, executive summary, §§Introduction/Defining AI Incidents/Key Components/Way Forward, all Tables 1–6, entire Appendix Tables A1–A4 and notes, About/Acknowledgments, and all endnotes. PDF pp. 8 and 19 visually checked after text reading; no linked source or underlying dataset is included in this complete-report event.; review events: [r5_reporting_04](rounds.md#r5_reporting_04) |
| `oecd_commonreportingincidents_2025` — supports | [Source](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/towards-a-common-reporting-framework-for-ai-incidents_8c488fdb/f326d4ac-en.pdf); No. 34 pp. 11–19; Annexes B–C | The common format offers 29 selected criteria and seven required schema fields, but is not an interface or a preventive/corrective-action evaluation. | `this_run_primary`; Complete accessible text of all 27 PDF pages: front matter, English/French abstracts, acknowledgments, executive summary, §§1–3, all tables, Annex A stocktaking, Annex B detailed29-field schema, Annex C relationship taxonomy, and references pp. 26–27. Rendered pp. 17,23,25 visually checked. No linked database payload or cited sources are included in the complete-document claim.; review events: [r5_reporting_05](rounds.md#r5_reporting_05) |
| `cset_incidentskeycomponents_2025` — bounds | [Source](https://cset.georgetown.edu/wp-content/uploads/CSET-AI-Incidents.pdf); January 2025 pp. 6–7,10–11; Appendix pp. 19–26 | CSET distinguishes actual incidents/near misses from hazards and draws on shared reporting resources; its synthesis is not an independent incident-effect sample. | `this_run_primary`; Complete accessible text of all 32 PDF pages, including cover, executive summary, §§Introduction/Defining AI Incidents/Key Components/Way Forward, all Tables 1–6, entire Appendix Tables A1–A4 and notes, About/Acknowledgments, and all endnotes. PDF pp. 8 and 19 visually checked after text reading; no linked source or underlying dataset is included in this complete-report event.; review events: [r5_reporting_04](rounds.md#r5_reporting_04) |
| `oecd_commonreportingincidents_2025` — bounds | [Source](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/towards-a-common-reporting-framework-for-ai-incidents_8c488fdb/f326d4ac-en.pdf); No. 34 Annex C p. 25; conclusions p. 19 | Multiple nonexclusive reported causal relationships and hazards require explicit units; future testing is proposed, not completed effectiveness validation. | `this_run_primary`; Complete accessible text of all 27 PDF pages: front matter, English/French abstracts, acknowledgments, executive summary, §§1–3, all tables, Annex A stocktaking, Annex B detailed29-field schema, Annex C relationship taxonomy, and references pp. 26–27. Rendered pp. 17,23,25 visually checked. No linked database payload or cited sources are included in the complete-document claim.; review events: [r5_reporting_05](rounds.md#r5_reporting_05) |

**Limits:** Full document readings cover the designs and their methods, not live implementation, current legal obligations or independently investigated incidents. CSET/OECD/AIID inputs overlap.

**Counterevidence / alternative:** Richer schemas may be burdensome or incomplete, and mandatory regimes can still underreport. The two proposals define scope differently, so agreement cannot be inferred by pooling raw counts.

**Next check:** Review actual reporting adoption, field completeness, investigations and documented remediation. Verify operative law separately whenever legal status is material.

<a id="c87"></a>
## C87

The AI Incident Database paper documents implemented cataloguing mechanisms—stable incident IDs, multiple reports per incident, search and plural taxonomies—that can support learning. It does not establish representative failure rates or demonstrate that database use prevents failures; report counts and illustrative mitigation workflows answer narrower questions.

**Status:** scoped_check. **Theme:** outcomes.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `mcgregor_preventingrepeatedfailures_2021` — supports | [Source](https://cdn.aaai.org/ojs/17817/17817-13-21311-1-2-20210518.pdf); Final AAAI 2021 pp. 15459–15462; Figures 2–5 | The built architecture distinguishes incidents from source reports, permits namespaced taxonomies and supports searching/submitting reports; Figure 2 has multiple reports for Incident 36. | `this_run_primary`; Complete accessible text of all 6 final proceedings PDF pages, printed 15458–15463: abstract, introduction/motivation, AIID architecture and discovery/submission/taxonomy features, all figure captions, hypothetical fairness-use example, conclusions, acknowledgments and references. Figures 2–5 visually inspected on PDF pages 3–5; Figure 1 image not pixel-inspected. No current database, software or linked external source was audited.; review events: [r5_reporting_06](rounds.md#r5_reporting_06) |
| `mcgregor_preventingrepeatedfailures_2021` — bounds | [Source](https://cdn.aaai.org/ojs/17817/17817-13-21311-1-2-20210518.pdf); Final AAAI 2021 p. 15462 Figure 5; p. 15463 conclusion | The fairness-use workflow and mitigation benefits are intended applications; adoption interest and historical report volume are not a controlled remediation or incidence study. | `this_run_primary`; Complete accessible text of all 6 final proceedings PDF pages, printed 15458–15463: abstract, introduction/motivation, AIID architecture and discovery/submission/taxonomy features, all figure captions, hypothetical fairness-use example, conclusions, acknowledgments and references. Figures 2–5 visually inspected on PDF pages 3–5; Figure 1 image not pixel-inspected. No current database, software or linked external source was audited.; review events: [r5_reporting_06](rounds.md#r5_reporting_06) |
| `oecd_commonreportingincidents_2025` — contextualizes | [Source](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/towards-a-common-reporting-framework-for-ai-incidents_8c488fdb/f326d4ac-en.pdf); No. 34 pp. 13–18 and Annex A | The later schema uses AIID among four stocktaking resources. This methodological reuse is not independent corroboration of the database's prevention effect. | `this_run_primary`; Complete accessible text of all 27 PDF pages: front matter, English/French abstracts, acknowledgments, executive summary, §§1–3, all tables, Annex A stocktaking, Annex B detailed29-field schema, Annex C relationship taxonomy, and references pp. 26–27. Rendered pp. 17,23,25 visually checked. No linked database payload or cited sources are included in the complete-document claim.; review events: [r5_reporting_05](rounds.md#r5_reporting_05) |

**Limits:** The exact final 2021 paper was read, but database data/code, current completeness and actual user decisions were not audited. Historical counts are version-bound.

**Counterevidence / alternative:** Media/reporting selection, duplicate reports and uncertain causal attribution can distort apparent frequencies; plural taxonomies expose disagreement rather than resolving it automatically.

**Next check:** Look for a documented downstream decision/remediation case with causal limitations, and keep current database counts separate from the historical article.

<a id="c88"></a>
## C88

Engineered backdoors can persist through specified safety-training pipelines, but persistence depends on adversarial access, objective, model and training configuration; some tested objectives or models lose the measured backdoor effect.

**Status:** scoped_check. **Theme:** oversight_control.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `hubinger_sleeperagentstraining_2024` — supports | [Source](https://arxiv.org/pdf/2401.05566v3); v3 §§1–2/model-organism framing, pp2–3,9–10; §4/HHH RL pp15,18–20; Figures10–11 captions; §6 adversarial training pp25–27; Figure17 caption; Alternative explanations/limitations pp39–40 | Constructed conditional policies persist in selected settings; smaller models and SFT show mitigation successes. | `this_run_primary`; PDF pp2–3,9–10,15,18–20,25–27,39–40 read in full; includes model-organism framing, selected RL/SFT comparisons, adversarial-training methods/results and alternative explanations. Cover title/byline identifiers checked. Remaining pages, references and appendices were not read in full.; review events: [r5_persistence_01](rounds.md#r5_persistence_01) |
| `zhang_persistentpretraining_2025` — bounds | [Source](https://arxiv.org/pdf/2410.13722v1); v1 §3 threat model/training setup pp3–4; §4.1.3 and Figure6 p8; §4.1.4 and Figure7 pp8–9; §5 discussion pp9–10; Appendices B–C pp15–17; Tables2–3 | Data-only pretraining poisoning leaves three objectives measurably persistent, while the tested jailbreak objective does not persist after safety training. | `this_run_primary`; Every text page of the 17-page PDF read: abstract, §§1–6, all references, Appendices A–C, tables, figure captions and displayed examples. Rendered checks were separately limited to pp8 and15.; review events: [r5_persistence_02](rounds.md#r5_persistence_02) |

**Limits:** Constructed settings do not estimate natural deceptive alignment or deployed-system incidence. Hubinger is selectively read; Zhang uses a shortened pretraining regime with reduced capabilities. Trigger, task, training access and endpoint differ, so the studies are not a matched contradiction or a universal scale experiment.

**Counterevidence / alternative:** Both studies contain successful mitigation or null persistence results. A null measured jailbreak effect need not establish removal of every possible latent policy, while a surviving engineered effect does not show every training method fails.

**Next check:** Retain positive and null findings together. Complete remaining claim-critical model-organism ablations if this becomes a leading mechanism claim; otherwise omit broad incidence and universal-training-failure language.

<a id="c89"></a>
## C89

A model can be engineered to display a target behavior only after selected benign supervised finetuning, making pre-adaptation behavior an incomplete assurance test for that constructed threat model.

**Status:** scoped_check. **Theme:** oversight_control.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `gloaguen_finetuningactivated_2025` — supports | [Source](https://arxiv.org/pdf/2505.16567v1); v1 §§4.2–4.5 results/ablations pp5–9; §4.4/Table7 and §4.5/Table8 p8; §5 limitations p9; AppendixB.3 pp26–27; AppendixD.2 p32 | Original v1 reports dormant-then-active behavior with clean-baseline controls, alongside task/configuration nulls and a narrow robustness study. | `this_run_primary`; PDF pp1–2,5–9,26–27,32 read in full: original abstract/introduction, experimental results/ablations/limitations, selected evaluation details and resource notes. Core attack-construction §§3–4.1 pp3–4 and most appendices were not read.; review events: [r5_persistence_05](rounds.md#r5_persistence_05) |

**Limits:** V1 tests compromised model weights and supervised finetuning in models up to 3B; it does not establish naturally occurring dormancy or all adaptation methods. Selected reading and evaluation-format exclusions limit stronger conclusions.

**Counterevidence / alternative:** Task-conflicting finetuning and multiple robustness settings produce weak or absent effects; clean finetuning can also alter baseline safeguards. Utility thresholds are not formal noninferiority evidence.

**Next check:** Describe adaptation as part of the evaluation boundary, with a finetuned-clean comparator. Inspect later v4 separately only if expanded RL/distillation claims become publication-critical.

<a id="c90"></a>
## C90

Filtered synthetic training data can transmit measured teacher traits in controlled finetuning experiments, with model-pair, trait and evaluation dependencies that prevent a universal transfer rule.

**Status:** scoped_check. **Theme:** oversight_control.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `cloud_subliminallearning_2025` — supports | [Source](https://arxiv.org/pdf/2507.14805v1); v1 §§3–4 controlled trait-transfer studies pp4–8; §5.1 Figure8 and §5.2 in-context controls p9; §6.1 Theorem1 p10; §6.2 p11; §8 limitations p13; AppendixD.2 p28; D.4/Figure18 pp31–32 | Numbers/code/reasoning experiments show transfer with controls; model-pair exceptions, null in-context probes, limited theorem assumptions and teacher-provenance filter labels bound the mechanism claim. | `this_run_primary`; Main PDF pp2–13 (§§1–9, including selected acknowledgments/reference opening); cover/abstract identifiers; AppendixD.2 p28 and D.4 pp31–32. An unrelated illustrative list on p27 was encountered but is not evidence for the claims. Remaining references, proof appendix and other appendices were not read in full.; review events: [r5_persistence_03](rounds.md#r5_persistence_03) |

**Limits:** The study does not estimate prevalence in production data. Shared initialization for named closed models is an author-attributed explanation, not independently inspected weights. The theorem and sampled multistep experiments have different assumptions; proof/appendices were not fully read.

**Counterevidence / alternative:** Some traits and mismatched pairs do not transfer, while GPT-4o/GPT-4.1 are a named cross-type exception. Negative probes narrow possible explanations without excluding every semantic cue or proving filtering impossible.

**Next check:** Keep transfer endpoints, model-pair exceptions and evaluation/filter conditions attached to the claim. Complete specific appendix/proof checks only if stronger mechanistic or numerical claims are retained.

<a id="c91"></a>
## C91

Backdoor benchmarks expose task, access and edition dependence, with positive targeted-refusal mitigation in a later comparison; unresolved jailbreak baseline/task provenance prevents a reliable quantitative jailbreak-defense conclusion.

**Status:** scoped_check. **Theme:** oversight_control.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `li_backdoorllmcomprehensive_2024` — supports | [Source](https://arxiv.org/pdf/2408.12798v1); v1 §3/Table2 access taxonomy pp3–4; Table3 caption p5 and §4.1 metric definitions p6; §4.2–4.5/results Tables4–6 pp6–9; §5 limitations p9; AppendixA.4 p15; B.1/Figure1 p16; B.2–B.3 pp16–17 | Original v1 separates four attacker-access categories and distinct success metrics; judge/scale interpretations have limitations and robust defense support is explicitly absent. | `this_run_primary`; Every text page of the 20-page v1 PDF read: main §§1–6, all references, ethics and experimental Appendices A–B, tables, captions and displayed examples. Visual inspection separately limited to pp5 and16.; review events: [r5_persistence_04](rounds.md#r5_persistence_04) |
| `li_backdoorllmcomprehensive_2024` — supports | [Source](https://arxiv.org/pdf/2408.12798v2); v2 §5 and Table7 p9; AppendixD.1 defense configurations p16; AppendixD/Table4 and D.2 pp17–18 | Related v2 adds defense comparisons with strong reported targeted-refusal mitigation. Jailbreak table/prose escalation wording and the no-defense baseline/task provenance remain unresolved; no affected numerical comparison is adopted. | `this_run_primary`; PDF p1 cover/abstract, pp8–10 (CoT-results continuation, full §5/Table7 and conclusion/reference opening), pp16–18 (defense taxonomy/configurations, Table4, complete D.2 discussion and beginning of additional-result sections). Other v2 pages were not fully read.; review events: [r5_persistence_06](rounds.md#r5_persistence_06) |

**Limits:** Access categories and reused implementations/tasks are not independent replications. The original Table3 caption/definitions conflict and v2 table/prose escalation wording is unresolved. The v2 defense comparison is one model/two tasks/five data-poisoning methods, with perplexity as a limited auxiliary metric. The v2 Table7 jailbreak no-defense vector matches its Table3 sentiment-misclassification rather than jailbreaking vector. Checkpoint, split and run mapping were not inspected, so this is a provenance hold, not an asserted copied-row error or a replacement baseline.

**Counterevidence / alternative:** Selected settings are weak or null, and some defenses strongly reduce targeted-refusal success. Residual effects and uncertain jailbreak baselines prevent universal mitigation or failure conclusions; table/prose disagreements do not establish their cause.

**Next check:** Omit affected rate headlines and defense-induced-escalation language. Reconcile canonical original-title/later-abstract metadata and seek correction/clarification only if the disputed rates become consequential.

<a id="c92"></a>
## C92

Separately modeling helpfulness and harmfulness can improve their measured tradeoff through constrained optimization, while the practical constraint remains an expectation of a learned cost.

**Status:** scoped_check. **Theme:** safeguards.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `dai_saferlhfsafe_2024` — supports | [Source](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf); ICLR2024 final §§3–5, Eqs7–10; Figures5–6; Appendix A/G.2 | Separate labels/scorers and Lagrangian training improve curated human/GPT-4 comparisons and tested ablations; the desired pointwise constraint is relaxed to expected learned cost. | `this_run_primary`; Official 28-page ICLR final: main §§1–6, pp1–9; Appendix A limitations and B cost-model ablation p15; Appendix C reproducibility and D ethics plus E.1 opening p16; selected G.1 ending and complete G.2 model-selection plus G.3 opening pp21–22. Other appendix material, references, annotation protocol, proof and full implementation/red-team sections not comprehensively read.; review events: [r5_mitigations_01](rounds.md#r5_mitigations_01) |

**Limits:** Official final is a related edition of the canonical preprint and only selectively read. Single-turn 7B models, curated data/scorers and changing round data limit the result; no final/preprint equivalence or deployed-harm rate is certified.

**Counterevidence / alternative:** Human pairwise judgments add an endpoint beyond learned scores, but expectation constraints can hide individual harmful responses and changes in prompts/checkpoint selection. HC-RLHF uses related SafeRLHF data/method lineage, not independent confirmation.

**Next check:** Compare exact canonical/preprint and final claim-critical methods and evaluation appendices before adopting numerical final results; evaluate cost construct validity and prompt shift separately.

<a id="c93"></a>
## C93

HC-RLHF’s held-out accept-or-abstain procedure supports a conditional bound on the probability of returning a model that violates an expected learned-cost constraint. The written zero-threshold case avoids an unresolved centering discrepancy.

**Status:** scoped_check. **Theme:** safeguards.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `chittepu_reinforcementlearning_2025` — supports | [Source](https://arxiv.org/pdf/2506.08266v1); arXiv v1 §§3–4/Assumption4.1/Theorem4.2; Appendices A–D | Candidate selection plus held-out confidence-bound test may return No Solution Found. Statistical validity depends on iid/normal estimates for the stated Student-t theorem or bounded estimates for the Hoeffding alternative, and a stationary prompt distribution. Eq8 includes −τ but Algorithm1/§4 use uncentered cost samples and a zero acceptance threshold; zero-threshold forms coincide, while arbitrary-threshold guarantee wording is deferred. | `this_run_primary`; All accessible text of all20 PDF pages of arXiv v1: main §§1–7, references and Appendices A–F, all tables/captions and proofs. Mathematical arguments were read as source text, not independently formally verified. Linked code/data and alternative published edition were not read or run.; review events: [r5_mitigations_02](rounds.md#r5_mitigations_02) |

**Limits:** The bounded object is expected learned cost, not individual-response harm or deployment harm. A read proof is not independent formal verification, and training/judge implementation is not replicated. Main/appendix judge identity differs; affected numerical comparisons are omitted. Nonzero-threshold centering differs between Eq8 and Algorithm1/§4; the general-threshold formulation needs clarification before publication. The risk bound concerns the training/test procedure returning an unsafe output, with No Solution Found defined safe; it is not a posterior or conditional guarantee of operational safety for every accepted model.

**Counterevidence / alternative:** Cost-model misspecification, adaptive prompt shift or uncertified fallback on abstention can break the link to operational safety. Favorable small-model trial results do not prove zero failure probability.

**Next check:** Retain conditional theorem wording, resolve exact judge run IDs/title metadata, and validate scorer/distribution assumptions before applying the procedure to a deployment decision. Check actual nonzero-threshold safety-test centering against Eq8/Algorithm1/§4; otherwise omit the arbitrary-threshold guarantee.

<a id="c94"></a>
## C94

Safe LoRA provides a positive weight-space mitigation for safety degradation during controlled fine-tuning, with model-dependent projection choices and visible utility tradeoffs.

**Status:** scoped_check. **Theme:** safeguards.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `hsu_safelorasilver_2024` — supports | [Source](https://arxiv.org/pdf/2405.16833v1); arXiv v1 §§3–4, Tables1–3; Appendix A/Figures3–4 | Projecting selected LoRA updates using aligned-minus-base weights improves tested harmfulness/refusal endpoints across harmful, mixed and benign adaptation settings; projected-layer sweeps and model/dataset thresholds expose utility tradeoffs. | `this_run_primary`; All accessible text of the 15-page arXiv v1, including main §§1–5, references, Appendix A.1–A.4 and all captions/Tables1–6. Equations and threat assumptions read; no linked code, datasets or final-edition appendices inspected.; review events: [r5_mitigations_03](rounds.md#r5_mitigations_03) |

**Limits:** Requires trusted base/aligned weights and control over the adaptation pipeline; tests are limited to specific7B/8B model/data/LoRA configurations. The separate longer NeurIPS final has not been substantively reread.

**Counterevidence / alternative:** Utility is not uniformly preserved; baseline dose choices constrain superiority claims. Authors explicitly leave adaptive circumvention open. A method called a safety-aligned subspace is not a general proof of a unique safety mechanism.

**Next check:** Use the v1 result under controlled-weight assumptions. Check final-version changes and matched utility/adaptive-attack experiments before broader claims.

<a id="c95"></a>
## C95

Teaching models to reason over explicit safety policies provides affirmative policy-adherence and jailbreak-resistance evidence, with limits from comparator information, overrefusal and the tested transfer distribution.

**Status:** scoped_check. **Theme:** oversight_control.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `guan_deliberativealignment_2024` — supports | [Source](https://arxiv.org/pdf/2412.16339v1); arXiv v1 §§2–4; §6; Appendix A | Synthetic policy-reasoning SFT and outcome RL improve tested behavioral endpoints and contribute in reduced-model ablations; reported OOD transfer is relative to held-out safety-training categories, while one ablation increases overrefusal. | `this_run_primary`; Cover/abstract/introduction opening p1; §2 overview/specification/data-generation/filtering/SFT/RL pp3–9; §3.1.3 jailbreak evaluation p10; §§3.2–4.3 comparisons/compute/ablations/policy retrieval/OOD pp12–18; complete §6 discussion pp20–21; Appendix A human-review experiment and Table4 p24. Remaining examples, policies, related work and references not comprehensively read.; review events: [r5_mitigations_05](rounds.md#r5_mitigations_05) |

**Limits:** Provider study of OpenAI policy/model releases, internal scorers and specified attack budgets. Selected reading, no training reproduction, no faithful-reasoning proof and no policy-legitimacy conclusion.

**Counterevidence / alternative:** Inference comparators receive summarized policies rather than the same detailed training information. Internal human review checks responses but is not external validation. Pretraining/capability exposure bounds the OOD interpretation.

**Next check:** If used as a leading publication finding, inspect exact release IDs, full metrics/judge implementations and attack protocols; retain the scoped affirmative result without universal harmlessness or cost-free improvement language.

<a id="c96"></a>
## C96

Historical extraction experiments distinguish restricting ordinary output behavior from removing memorized text; their access conditions and web-matching ground truth do not establish current product exposure or certified proprietary-training membership.

**Status:** scoped_check. **Theme:** safeguards.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `nasr_scalableextraction_2025` — supports | [Source](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf); ICLR 2025 final §§2–7, pp2–10; Tables 1–2 | Specific historical model/interface comparisons show both reduced easy extraction and additional recoverable web-matching outputs under changed access. The fine-tuning exclusion control helps distinguish recovery from simply replaying supplied fine-tuning text. | `this_run_primary`; Complete main-text viewer pp1–10, abstract and §§1–8 through the beginning of the discussion on p10; Tables 1–2 and captions for Figures 1–5. Discussion continuation, references and appendices on pp11–73 were not fully read. No example strings or sensitive output passages are reproduced.; review events: [r5_privacy_01](rounds.md#r5_privacy_01) |

**Limits:** Main text only; final canonical metadata pending. Unknown proprietary training data are proxied by a 9 TB auxiliary corpus and at-least-50-token matches. Historical interfaces and patched behavior are not current rates.

**Counterevidence / alternative:** Transfer is uneven across models and safeguards can reduce ordinary extraction; unknown training/weight differences prevent isolating alignment as the sole cause. Contact-string classifiers do not establish person-level harm.

**Next check:** Reconcile the final edition and read relevant appendices before numerical headlines; retain version/access/denominator qualifiers.

<a id="c97"></a>
## C97

A deletion audit of the resulting model and privacy of the before/after update history are distinct: in Du et al.’s synthetic classification experiments, exact retraining improves single-state erasure while version comparisons can still reveal deletion membership.

**Status:** scoped_check. **Theme:** outcomes.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `du_textualunlearning_2025` — supports | [Source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/du25d/du25d.pdf); ICML 2025 final §§2–5, Tables 1–2 and Figure 4; Appendices A–J | Strong counterfactual auditing exposes residual distinguishability in tested inexact methods, while before/after access creates a separate membership/reconstruction channel, including an exact-retraining comparator. | `this_run_primary`; All 19 PDF pages read: main §§1–6, all figure captions and table text, acknowledgments/impact statement, references, and Appendices A–J. Key Table 1 and Figure 4 on viewer p8 were also visually inspected. Linked code/data and other cited papers were not read as part of this event.; review events: [r5_privacy_04](rounds.md#r5_privacy_04) |

**Limits:** Synthetic, deliberately mislabeled attribute-classification examples and output-score/logit/weight access do not measure generic generation or real-person exposure. Reconstruction overlap is not exact profile recovery.

**Counterevidence / alternative:** Exact retraining is a positive erasure control, and batch size/model/access change recovery; the paper does not show every unlearning method fails or estimate deployed-attack prevalence.

**Next check:** Cross-link C04/C35 without collapsing their different tasks or final-version status. Reproduce code or calibrate realistic generative/privacy settings only if needed for a numerical claim.

<a id="c98"></a>
## C98

vTune supplies positive, conditional evidence of fine-tuning on marked data, while leaving requested training granularity and an exact statistical null bound unverified.

**Status:** scoped_check. **Theme:** audit_institutions.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `zhang_vtuneverifiablefine_2024` — supports | [Source](https://arxiv.org/pdf/2411.06611v2); arXiv v2 §§4.2–4.3,5.1,5.3–5.4 and7; §4.2.1 p7 | The method tests supplied-data influence and reports feasibility/performance comparisons, but estimates the modal probability from sampled sequences and explicitly cannot verify requested model, iterations or fine-tuning method. | `this_run_primary`; Version/title and introduction/threat/desiderata on pp1–3; §§4–4.3 pp4–7 including test and modal-probability estimator; §5 experimental setup and §5.1 downstream performance pp7–8; §§5.3–5.4 and selected §6.1 subset-training assumptions p10; §7 conclusion/limitations p12. No complete reading of §5.2 sweeps, remaining attacks, references or appendices.; review events: [r5_privacy_06](rounds.md#r5_privacy_06) |

**Limits:** Selected sections; marker secrecy and tested provider threats limit transfer. Sample maxima do not supply a proved upper bound or universally calibrated tiny p-values.

**Counterevidence / alternative:** Useful positive process verification under a defined threat model remains possible. Successful marker learning does not ensure the full requested training job, privacy, erasure or safety.

**Next check:** Complete threat/appendix checks and statistical bound analysis before adopting significance or comprehensive-compliance claims.

<a id="c99"></a>
## C99

Open-model post-training extraction can yield semantically similar and useful training-like data, while semantic resemblance, exact record extraction and recovery of a complete safety policy remain distinct claims.

**Status:** scoped_check. **Theme:** safeguards.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `barbero_extractingalignment_2025` — supports | [Source](https://arxiv.org/pdf/2510.18554v1); arXiv v1 §§2,3.3,4.2–4.3 and5–6; Table 2 | Known public post-training mixtures permit comparison, and selected re-training results show useful downstream information; semantic threshold and benchmark-dependent distillation results bound the interpretation. | `this_run_primary`; Abstract and selected introduction/nomenclature; §2 pp3–4; selected §3 method definitions including all §3.3 metric text pp4–6; §4 setup and §§4.2–4.3 coverage/distillation pp6–9; §5 RL evaluation pp10–11 and §6 conclusion p12. No full reading of §3.1 prompt procedures, §4.1 verbatim-results analysis, references or appendices. Qualitative generations are not reproduced.; review events: [r5_privacy_07](rounds.md#r5_privacy_07) |

**Limits:** Selected v1 only; v2 and appendices pending. Manual embedding threshold, known public training data, filtering and different token budgets do not certify private membership or current-model incidence.

**Counterevidence / alternative:** Some distillation metrics are close to original training, while MATH and IFEval are lower; utility is substantive evidence without uniform parity or complete dataset recovery.

**Next check:** Check v2, threshold calibration and distillation appendices before leading with semantic-recovery magnitudes; keep broad capability alignment separate from safety-policy training data.

<a id="c100"></a>
## C100

Draft misuse-risk guidance can make a threat-to-decision process inspectable by linking risk baselines, evaluation conditions, safeguards, deployment choices and post-deployment feedback; it does not make those choices empirically adequate or legally binding merely by documenting them.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `nist_managingmisuserisk_2024` — supports | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-1.ipd.pdf); Initial draft §3, §4 Objectives1–7 and AppendixB/Table1 | The original lifecycle workflow specifies threat profiles, tolerances, resource-aware measurement, safeguards/deployment decisions and incident/transparency processes, with explicit alternative-practice and no-guarantee caveats. | `this_run_primary`; All27 PDF pages read: covers, comment notice/TOC, introduction, §§2–4, all seven objectives/practices/documentation, AppendixA glossary, AppendixB/Table1 and all50 endnotes. Linked studies/guidance not independently opened.; review events: [r5_versions_01](rounds.md#r5_versions_01) |
| `nist_managingmisuserisk_2025_2pd` — supports | [Source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-1.ipd2.pdf); Second draft §§2–5 Practices1.1–1.3,4.1–4.2,5.1–5.3; AppendixC/Table2 | The later draft explicitly adds marginal-risk/supply-chain framing and a richer task/measurement taxonomy, while retaining contextual, voluntary and no-prevention-guarantee qualifications. | `this_run_primary`; PDF frontmatter/intro/viewerpp1–5; complete §§2–4 and §5 through Practice6.1 opening, printedpp1–17/viewerpp6–22; complete AppendixC/Table2 printedpp26–30/viewerpp31–35. Remaining monitoring/disclosure practices, glossary, mitigation table, domain appendices and endnotes not fully read.; review events: [r5_versions_02](rounds.md#r5_versions_02) |

**Limits:** Two historical public drafts from one issuer lineage, not separate independent efficacy studies, adopted statutory requirements or a complete check of later versions. The69-page second draft remains selectively read; domain appendices were not fully inspected.

**Counterevidence / alternative:** Explicit practices and documentation create useful audit targets and response pathways, while uncertainty in proxy transfer, threat emulation and safeguards remains. Alternatives may be appropriate; documentation alone cannot certify implementation or outcomes.

**Next check:** Match the exact edition and intended decision; inspect actual evaluations, decisions, response records and follow-through before effectiveness claims. Verify later/current instruments separately if relevant.

<a id="c101"></a>
## C101

California Assembly staff cited PIRG’s 2025 AI toy tests in the June 16, 2026 SB 867 analysis. The subsequent chaptered law documents a separate legal action, not the tests’ causal influence, implementation, or effects.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `murray_troubleintoyland_2025` — supports | [Source](https://www.nypirg.org/pubs/202511/TOYLAND_REPORT_2025.pdf); Printed pp. 12–17 and p. 61 (AI methodology). | Originating empirical evidence: adult researchers selected four AI toys and could fully test three. The configured Kumma produced inappropriate outputs under researcher elicitation; the study did not test children. | `this_run_primary`; Chapter on AI toys, printed pp. 12–17; AI methodology, printed p. 61. Scoped inspection; no full-document or reproduction credit.; review events: [intake_murray_troubleintoyland_2025](rounds.md#intake_murray_troubleintoyland_2025) |
| `calassembly_sb867analysis_2026` — supports | [Source](https://apcp.assembly.ca.gov/system/files/2026-06/sb-867-padilla-apcp-analysis.pdf); June 16 hearing analysis, May 14 bill version; printed pp. 7–9, especially pp. 8–9, notes 14, 16 and 17. | Direct documentary evidence of consideration: staff name PIRG’s 2025 investigation and quote Kumma interactions with researchers. The citation is not a second observation or an explanation of why the bill passed. | `this_run_primary`; June 16 hearing analysis, printed pp. 7–9, notes 13–14 and 16–17. Scoped inspection; no full-document or reproduction credit.; review events: [intake_calassembly_sb867analysis_2026](rounds.md#intake_calassembly_sb867analysis_2026) |
| `california_sb867_companiontoys_2026` — supports | [Source](https://legiscan.com/CA/text/SB867/id/3458543); Chapter 189, approved and filed September 10, 2026; Business and Professions Code §§ 22601(b), 22601(g), 22604.5(a)–(b). | Documentary endpoint: the chaptered text restricts specified commercial activity involving physical toys designed, marketed or manufactured for play by children under 16 and containing a defined companion chatbot, with a January 1, 2031 sunset. | `this_run_primary`; Chaptered September 10, Chapter 189; Business and Professions Code §§ 22601(b), 22601(g), 22604.5(a)–(b). Scoped inspection; no full-document or reproduction credit.; review events: [intake_california_sb867_companiontoys_2026](rounds.md#intake_california_sb867_companiontoys_2026) |

**Limits:** The staff document concerns the May 14 bill version; the final statute’s scope comes from the chaptered text. As of November 20, 2026 the law was enacted but not yet in force. The 2026 PIRG retest report was published after enactment.

**Counterevidence / alternative:** A visible legislative citation establishes consideration, not a causal contribution to passage. The adult test did not establish injury or real-world exposure, and enactment is not enforcement, compliance, or a measured safety benefit.

**Next check:** Track implementation or documented enforcement separately and use an outcome design before attributing any change in exposure or harm to the law.

<a id="c102"></a>
## C102

Adult-led product elicitation and observed preschool play answer different downstream evaluation questions. The inspected examples show product output under selected tests and interaction difficulties during observed play, not population exposure or long-term effects.

**Status:** scoped_check. **Theme:** outcomes.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `murray_troubleintoyland_2026` — supports | [Source](https://publicinterestnetwork.org/wp-content/uploads/2026/11/TOYLAND-11-17-26-1.pdf); AI toys chapter, printed pp. 17–24; retest summary and test sample description. | PIRG reports seven commercial toys tested, four repeats and three new. Kumma’s guardrails performed better in the repeated tests, while the Alilo bunny still produced inappropriate material. | `this_run_primary`; AI toy chapter, printed pp. 17–24, including retests and testing scope. Scoped inspection; no full-document or reproduction credit.; review events: [intake_murray_troubleintoyland_2026](rounds.md#intake_murray_troubleintoyland_2026) |
| `goodacre_aiearlyyears_2026` — supports | [Source](https://www.pedalhub.net/wp-content/uploads/2026/03/AI-in-the-Early-Years-Project-report-27-February-2026.pdf); Children’s Views and Observed Play, printed pp. 13–19. | This qualitative study observed 14 children aged 3–5 with one Curio Gabbo at four London children’s centres. It reported engagement alongside difficulties with recognizing speakers, taking turns and pretend play; the vignettes combine observations across children. | `this_run_primary`; Children’s Views and Observed Play, printed pp. 13–19, including study design and composite vignettes. Scoped inspection; no full-document or reproduction credit.; review events: [intake_goodacre_aiearlyyears_2026](rounds.md#intake_goodacre_aiearlyyears_2026) |
| `collier_pixiepaw_2026` — contextualizes | [Source](https://www.nbcnews.com/tech/tech-news/ai-toys-kids-walmart-target-pull-plush-cat-described-sexual-violence-rcna608588); Firsthand Pixie-Paw test and retailer-response passages, captured article. | NBC separately reported eliciting inappropriate output from Pixie-Paw and relayed retailer responses. This is a different toy and separate newsroom investigation, not a matched check of either study or a demonstration of market-wide compliance. | `this_run_primary`; NBC’s account of its Pixie-Paw hands-on testing and retailer responses. Scoped inspection; no full-document or reproduction credit.; review events: [intake_collier_pixiepaw_2026](rounds.md#intake_collier_pixiepaw_2026) |

**Limits:** Product, version and interaction design differ across sources. The PIRG retest is from the original research organization; Cambridge did not estimate developmental effects, and NBC’s test is not a systematic product sample.

**Counterevidence / alternative:** Positive engagement and observed guardrail improvements coexist with interaction difficulties and failures in other selected configurations. None of these designs isolates a base-model cause or supports pooling outcomes across toys.

**Next check:** Specify test setting, product configuration and endpoint before comparing findings. Use separate designs for safeguard behavior, use experience, exposure, and longer-term outcomes.

<a id="c103"></a>
## C103

PIRG’s February 2026 walkthrough of five developer onboarding paths observed one provider asking whether the intended product was for minors. This documents a visible screening step, not enforcement or the effect of a screening policy.

**Status:** scoped_check. **Theme:** governance.

| Source and relation | Version / locator | Scoped finding | Review basis and depth |
|---|---|---|---|
| `cross_notforkids_2026` — supports | [Source](https://publicinterestnetwork.org/wp-content/uploads/2026/03/PIRG-NOT-FOR-KIDS-FOUND-IN-TOYS-March-2026.pdf); Executive summary and printed pp. 13–15, February developer signup test. | PIRG reports that Anthropic asked whether the researchers were building for minors; the other four onboarding paths checked did not ask that question. It is an observation of those particular paths at the time of the check. | `this_run_primary`; Executive summary and printed pp. 13–15 on developer signup. Scoped inspection; no full-document or reproduction credit.; review events: [intake_cross_notforkids_2026](rounds.md#intake_cross_notforkids_2026) |

**Limits:** The comparison is drawn from one bounded pass by one research team, not a repeated audit of all accounts, geographies, or developer paths.

**Counterevidence / alternative:** Visible questions are not proof that a provider enforces answers; an absent signup question does not rule out later enforcement or other safeguards. Toy marketing claims do not verify backend routing.

**Next check:** Look for independent repeated checks and documented later enforcement before making claims about provider compliance or effectiveness.

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
| `F09` | `ameisen_circuittracingrevealing_2025`, `lindsey_biology_2025` | Companion methods and case-study articles from one Anthropic circuit-tracing project. | Shared replacement-model method, authorship and reciprocal article links; r3_circuits_01–02. | One research family; case interventions are affirmative evidence but not two independent validations of comprehensive faithfulness. |
| `F10` | `cunningham_sparseautoencoders_2024`, `makelov_principledevaluations_2024` | Distinct SAE studies with shared indirect-object-identification task lineage; different model families and intervention protocols. | Pinned arXiv methods and limitations; r3_mechvalidation_02,04. | Task-family dependence recorded; exact item overlap and cross-edition equivalence remain unchecked. Not an independent task-generalization replication. |
| `F11` | `sba_complianceplanomb_2024`, `eac_complianceplanomb_2024`, `exim_complianceplanomb_2024` | Historical agency self-descriptions under the same M-24-10 mandate and common reporting structure. | Selected SBA/EAC and complete EXIM plan text; r3_public_01,03–04. | Specific reported acts differ by agency. Three plans are not three independent tests of control effectiveness or frontier-provider governance. |
| `F12` | `huang_trustllm_2024`, `wang_decodingtrust_2023` | Broad evaluation suites with documented shared benchmark/method ancestry, including salary-prediction and robustness tasks. | TrustLLM fairness AppendixF and its explicit DecodingTrust references; r3_fairness_03–04. | Construct definitions and model conditions differ. Exact item overlap is not reconstructed; do not count as independent population-impact corroboration. |
| `F13` | `buhl_safetycasesfrontier_2024`, `hilton_safetycasesscalable_2025`, `barrett_assessingconfidence_2025`, `carlan_dynamicsafetycases_2024`, `bloomfield_assurancesystemsdependabil_2024` | Overlapping safety-case authors, concepts and worked inability templates; confidence and change-management papers build on the same assurance lineage. | Pinned source authorship, references and worked examples; r4_safetycases events. | Conceptual dependency recorded, not an assertion that every paper shares all authors or that these are independent efficacy demonstrations. |
| `F14` | `nguyen_probingsteeringevaluation_2025`, `chaudhary_evaluationawareness_2025`, `hua_steeringevaluation_2025` | Shared evaluation-awareness prompt/probe lineage, with different model, organism and intervention choices. | Primary methods and explicit cited predecessors in r4_awareness_01–03. | Distinct contributions with shared concepts/data sources; exact item overlap is not fully reconstructed and broad independent behavioral replication is not claimed. |
| `F15` | `lambert_rewardbenchevaluating_2024`, `frick_evaluaterewardrlhf_2024`, `wang_selftaughtevaluators_2024`, `wang_helpsteer2opensource_2024` | Reward/judge studies share RewardBench and human-preference reference lineages; Self-Taught also uses HelpSteer2 endpoints. | Primary evaluation/training methods and source references in r4_judges events. | PPE’s preprint/final are one study; benchmark success and downstream validation are different endpoints. No independent broad evaluator-validity corroboration count. |
| `F16` | `mlcommons_ailuminate_2026`, `mlcommons_ailuminatev10_2025` | MLCommons suite portal and v1.0 paper are related objects across changing instrument/evaluator editions. | Current portal and exact arXivv1 methods, r4_depthsample_05–07. | Do not combine later non-LLM scorer descriptions with earlier LLM-ensemble results or count two entries as independent validation. |
| `F17` | `nist_managingmisuserisk_2024`, `nist_managingmisuserisk_2025_2pd` | Initial and second NIST AI800-1 public drafts are a policy-development lineage with changed scope, numbering and methods. | Exact covers, DOI/version labels and methods in r5_versions_01–02. | Historical draft comparison, not two independent efficacy studies or proof of present final/legal status. |
| `F18` | `hubinger_sleeperagentstraining_2024`, `zhang_persistentpretraining_2025`, `li_backdoorllmcomprehensive_2024` | Shared model-organism/benchmark and citation lineage, with different attacker access, objectives and training configurations. | Hubinger is cited/reused by the later benchmark and contrasted by Zhang; primary methods in r5_persistence events. | Transfer/null results are not a matched replication or contradiction across identical conditions; reused implementations/tasks do not give independent outcome samples. |
| `F19` | `dai_saferlhfsafe_2024`, `chittepu_reinforcementlearning_2025` | HC-RLHF extends SafeRLHF’s separated reward/cost and dataset lineage with a held-out acceptance/abstention test. | Primary HC-RLHF §2.2/§5 and selected SafeRLHF final methods, r5_mitigations_01–02. | Different contributions with dependent methods/data. Learned-cost, training-procedure confidence and human/operational outcomes remain distinct endpoints. |
| `F20` | `cset_incidentskeycomponents_2025`, `oecd_commonreportingincidents_2025`, `mcgregor_preventingrepeatedfailures_2021` | Reporting-design stocktaking uses overlapping incident resources, including AIID, while scope and report/incident/hazard units differ. | Complete CSET/OECD methods and AIID final paper, r5_reporting_04–06. | Resource reuse is methodological dependence, not independent prevention-effect evidence. Exact event-level overlap is not reconstructed; raw report counts must not be pooled. |
