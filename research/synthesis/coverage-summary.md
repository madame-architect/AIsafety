# Corpus coverage and checking depth

Read [current adjudications and publication holds](reconciliation.md) before using inherited notes. A populated `current_review_note` takes precedence over contradictory inherited support statements or review leads for current interpretation; it does not rewrite the earlier inspection history. Later dated reading events qualify those earlier notes without changing their provenance.

Generated from [coverage.csv](coverage.csv), [claims.yaml](claims.yaml), and canonical [records.yaml](../../records.yaml) by `python3 scripts/build_research.py --write`.

The CSV preserves source-level contributions, inspection descriptions, limitations and proposed checks for every current bibliography key. These are inherited research notes, not new source verification. Citation identity, titles, metadata and source classification remain authoritative in `records.yaml`.

## Reading labels inherited before later rounds

| Stream | Full text | Selected sections | Abstract only | Metadata only | Inaccessible | Total |
|---|---:|---:|---:|---:|---:|---:|
| `technical_eval` | 38 | 112 | 6 | 0 | 0 | 156 |
| `governance_artifact` | 56 | 33 | 0 | 5 | 1 | 95 |
| `contextual` | 11 | 21 | 2 | 1 | 0 | 35 |
| **Total** | 105 | 166 | 8 | 6 | 1 | **286** |

| Recorded stage | Full text | Selected sections | Abstract only | Metadata only | Inaccessible |
|---|---:|---:|---:|---:|---:|
| First pass in supplied ledger | 58 | 211 | 9 | 7 | 1 |
| Latest inherited label | 105 | 166 | 8 | 6 | 1 |

The supplied review's 104 full-text / 9 abstract-only table is superseded by the latest ledger labels above. **181 records remain short of the inherited full-text label.** Full text refers to the identified object's complete accessible text; linked PDFs, supplements, figures, data and experiments require separate inspection. Records include pages and policies as well as papers. These labels are recorded inspection claims, not certification of earlier reading.

## Separate later checking

The supplied prior AI-assisted audit logs scoped central-claim checks for **105 records**. Its actual depth, source URL, finding, locator and remaining limits appear in the `prior_ai_check_*` columns. A selected-section check remains selected-section checking even when the inherited reading label is full text. `prior_ai_check_reported_on` is the audit reporting date, not a reconstructed source retrieval timestamp. The register is not a complete-document reread and its title does not establish independent human review or independence of the underlying sources. The integration checked the register's keys and content; it did not repeat all its source checks. Later deeper checks outside that register are described where used in the claim map, rather than silently upgrading its rows. The original integration reported no experimental replication; later events record their own replication status.

## Subsequent dated review rounds

[Reading events and thematic decisions](rounds.md) preserve fresh inspection, exact versions, captures, contrary evidence and limitations separately from the inherited CSV. Full-text reading is not experimental replication, and reading a related or uncertain edition does not increase canonical-record coverage.

Later rounds log **34 reading events** for **28 unique keys**. **7 keys** have eligible complete-record-text events, including **6** that lacked an inherited full-text label. These remain recorded reading claims, not independent certification of every figure, supplement or source finding.

| Layer | Full text | Selected sections | Abstract only | Metadata only | Inaccessible |
|---|---:|---:|---:|---:|---:|
| Fresh reading events (representations may repeat a key) | 9 | 20 | 1 | 1 | 3 |
| Combined best same-record inspection | 111 | 161 | 7 | 6 | 1 |

**175 records** remain without a full-text label after eligible new reading. Combined inspection retains earlier full-text labels without recertifying them; a later selected-section check neither erases nor independently confirms an earlier complete read. The reading event records replication and numerical checking separately. Missing local captures are reported by the validator; ordinary CI does not claim byte verification of absent private files.

## Argument coverage

The current map has **45 claims** linked to **83 unique bibliography keys**. The other **203 keys** are not mapped as claim evidence. Of these, **2** have an explicit non-claim relevance decision in later rounds and **201** retain an unresolved role. An unmapped record is neither excluded nor evidence for a claim. A source may bound or challenge a proposition; inclusion is not corroboration. Shared study families are listed in the [claim map](claims.md).

**238 records** have proposed corrections or checks. These are review leads, not established errors. Current adjudications and publication-critical holds belong in the reconciliation note and claim map; inherited notes are retained with that boundary.

## Provenance and scope

Imported from the supplied revised coverage ledger, original byte SHA-256 `60b2ea6456ae11262c29eded7e88191b08a0da5012e60e693dcd82f9cc6d3876`. The review input had SHA-256 `e4a0715b1e7f44720e9a659db784e13ad045fb85ceb43ca15353601d3df0553c`. The derivative CSV omits private patch-disposition fields and bibliography metadata already held in `records.yaml`. It preserves first-pass and subsequent inherited depth stages and dates separately from the prior audit. The full-corpus reading and synthesis objective remains open. This curated collection has no reconstructed exhaustive search or independent human dual coding; completing reads would not retroactively create either.

## Record index

Use the CSV for full source notes. Links below identify explicit claim roles; all other roles remain unresolved.

| Canonical citation key | Latest inherited reading | Prior scoped AI check | Claim roles | Current review note | Later reading events |
|---|---|---|---|---|---|
| `ackerman_mitigatingmanyshot_2025` | Full text | Logged; see CSV scope | [C05](claims.md#c05) | — | — |
| `aiid_snapshot_20260504` | Metadata only | Outside 105-record register | Unresolved | — | — |
| `aisi_fourthprogress_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `aisi_frontiertrends_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `aisi_inspectai_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `aisi_inspectevals_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `aisi_safetyinstitutesjoint_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `aisi_unsanctionedagentincident_2026` | Full text | Logged; see CSV scope | [C23](claims.md#c23) | The supplied correction is integrated: interventions,19 actions across10/122 runs and no identified resulting harm are reported without a prevention counterfactual. Earlier assessments remain; see C23 and reconciliation.md. | — |
| `aisi_year_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `amazon_fortigateaiaugmented_2026` | Full text | Logged; see CSV scope | [C22](claims.md#c22) | — | — |
| `amazon_frontiermodelsafetyframework_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `ameisen_circuittracingrevealing_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `amironesei_aria_pilot_2025` | Selected sections | Outside 105-record register | [C45](claims.md#c45) | Later methods/appendix checking distinguishes testing sessions, dialogues and annotation judgments. Main text reports 52 violations in267 dialogues while Appendix C Table7 reports49; no affected violation rate is adopted. CoRIx characterizes the pilot applications rather than calibrating cross-system ranks. See C45 and r2_sociotechnical_03. | [r2_sociotechnical_03](rounds.md#r2_sociotechnical_03) |
| `anderljung_frontierairegulation_2023` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `andriushchenko_agentharm_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `anil_manyshotjailbreaking_2024` | Selected sections | Outside 105-record register | [C05](claims.md#c05) | — | — |
| `ankner_critiqueoutloud_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `anthropic_anthropicsresponsible_2026` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `anthropic_frontiercomplianceframework_2026` | Metadata only | Outside 105-record register | Unresolved | — | — |
| `anthropic_responsiblescaling_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `anthropic_responsiblescaling_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `anthropic_responsiblescalingv32_2026` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `arike_doesinformationaccess_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `arnesen_trainingwindebates_2024` | Selected sections | Outside 105-record register | [C29](claims.md#c29), [C32](claims.md#c32) | — | [r2_oversight_02](rounds.md#r2_oversight_02) |
| `arrieta_earlyexternalsafety_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `barbero_extractingalignment_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `barrett_assessingconfidence_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `barrett_quantitativecyberrisk_2025` | Full text | Logged; see CSV scope | [C25](claims.md#c25) | — | — |
| `bender_stochasticparrots_2021` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `bengio_internationalsafety_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `bengio_managingextremeairisks_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `benton_sabotageevaluations_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `bhatt_cyberseceval2wide_2024` | Full text | Logged; see CSV scope | [C36](claims.md#c36) | Fresh prompt-injection prose/Figure3 and interpreter-method checks retain a range discrepancy without assigning an unverified explanation. The interpreter evaluates judged responses without executing them; no sandbox-escape rate follows. Retain scoped findings and false-refusal design, omit disputed headline range. See C36 and r2_safeguards_04. | [r2_safeguards_04](rounds.md#r2_safeguards_04) |
| `bhattacharjee_inferencetimecategory_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `bis_artificialintelligence_2025` | Selected sections | Outside 105-record register | Unresolved | The supplied correction distinguishes Diffusion Rule nonenforcement from formal legal status. GAO May12,2026 and the Aug14,2026 plan support the last verified formal position; an exhaustive current-status determination is not claimed. See reconciliation.md. | — |
| `bis_establishmentreporting_2024` | Selected sections | Outside 105-record register | Unresolved | The supplied correction records historical/withdrawn proposal status. Fresh RIN0694-AJ55 text confirms withdrawal12/16/2025; its URL now returns PublicationID2026 rather than a frozen202510 edition. See reconciliation.md. | — |
| `bloomfield_assurancesystemsdependabil_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `braun_identifyingfunctionally_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `brundage_frontierauditingrigorous_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `buhl_safetycasesfrontier_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `bullwinkel_triggerhaystackextracting_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `burns_weakstronggeneralization_2024` | Selected sections | Outside 105-record register | [C28](claims.md#c28) | — | [r2_oversight_04](rounds.md#r2_oversight_04) |
| `cac_interimmeasuresgenai_2023` | Full text | Logged; see CSV scope | Unresolved | This record was outside the specific legal recoding changes in the supplied patch. Existing status/application labels remain inherited and require dated review before current-law use. See reconciliation.md. | — |
| `caisi_deepseekv4pro_2026` | Full text | Logged; see CSV scope | [C16](claims.md#c16) | Current primary-page audit reports the 32% comparator as GPT-5.4 mini and places the imputation asterisk on DeepSeek V4 Pro, contrary to the inherited note. No authenticated historical capture explains the difference. Hold the inherited comparator/imputation wording; see reconciliation.md. | — |
| `calderon_alternativeannotator_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `california_sb53_tfaia_2025` | Full text | Logged; see CSV scope | Unresolved | This record was outside the specific legal recoding changes in the supplied patch. Existing status/application labels remain inherited and require dated review before current-law use. See reconciliation.md. | — |
| `californiapolicyworkinggroup_thecaliforniareport_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `carlan_dynamicsafetycases_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `casper_blackboxaccessaudits_2024` | Selected sections | Outside 105-record register | [C38](claims.md#c38), [C39](claims.md#c39) | — | [r2_institutions_02](rounds.md#r2_institutions_02) |
| `chan_euunveilscode_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `chao_jailbreakbenchopen_2024` | Selected sections | Outside 105-record register | [C33](claims.md#c33) | — | [r2_safeguards_01](rounds.md#r2_safeguards_01) |
| `charnock_expandingexternalaccess_2026` | Selected sections | Outside 105-record register | [C38](claims.md#c38) | — | [r2_institutions_01](rounds.md#r2_institutions_01) |
| `chaudhary_evaluationawareness_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `chee_eustickstimeline_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `chittepu_reinforcementlearning_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `cloud_subliminallearning_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `cohere_secureaifrontiermodelframework_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `controlarena_research_nd` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `coulter_eupicksexperts_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `cset_incidentskeycomponents_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `cui_persistentbackdoor_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `cunningham_constitutionalclassifiers_2026` | Selected sections | Outside 105-record register | [C06](claims.md#c06) | — | — |
| `cunningham_sparseautoencoders_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `dai_saferlhfsafe_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `davies_boundarypointjailbreaking_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `deepmind_frontiersafetyv1_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `deepmind_frontiersafetyv31_2026` | Full text | Logged; see CSV scope | [C18](claims.md#c18) | — | — |
| `deepmind_frontiersafetyv3_2025` | Full text | Logged; see CSV scope | [C18](claims.md#c18) | — | — |
| `deepmind_updatingfrontiersafety_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `dsit_tacklingsecurityrisks_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `du_textualunlearning_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `dubois_skewedscore_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `eac_complianceplanomb_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `ec_approachartificial_nd` | Full text | Logged; see CSV scope | Unresolved | The supplied correction distinguishes this Commission information/guidance page from statutory legal authority. Current legal_status is not_applicable; see reconciliation.md. | — |
| `ec_gpai_codepractice_final_2025` | Full text | Logged; see CSV scope | [C17](claims.md#c17) | The supplied correction codes the GPAI Code nonbinding and identifies its voluntary compliance-tool role. Signing or publishing a code does not prove compliance; see C17 and reconciliation.md. | — |
| `ec_gpai_trainingcontenttemplate_2025` | Selected sections | Outside 105-record register | [C17](claims.md#c17) | The supplied correction separates the explanatory notice from mandatory use of the linked template under Article53(1)(d). Fresh Commission FAQ text supports that linkage. It is not a new duty created by the notice; see reconciliation.md. | — |
| `ec_guidelinesgpaiproviders_2025` | Selected sections | Outside 105-record register | [C17](claims.md#c17) | The supplied correction codes the interpretive guidelines nonbinding. Fresh linked English PDF C(2025)7719final, Nov19,2025, paragraph9 confirms that status, but does not authenticate the inherited July edition. Canonical publication/version reconciliation remains open. See C17 and reconciliation.md. | — |
| `ec_scientificpanel_2025_454` | Full text | Logged; see CSV scope | Unresolved | This record was outside the specific legal recoding changes in the supplied patch. Existing status/application labels remain inherited and require dated review before current-law use. See reconciliation.md. | — |
| `engels_scalinglawsscalable_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `eu_regulationeu2024_2024` | Selected sections | Outside 105-record register | Unresolved | This record was outside the specific legal recoding changes in the supplied patch. Existing status/application labels remain inherited and require dated review before current-law use. See reconciliation.md. | — |
| `exim_complianceplanomb_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `federalregister_safesecuretrustworthy_2023` | Selected sections | Outside 105-record register | Unresolved | The supplied correction sets historical status for revoked EO14110. This run checked EO14148 section2(ggg); no compliance or broader current-law determination is claimed. See reconciliation.md. | — |
| `fmf_bioworkstream_nd` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_capabilityassessments_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `fmf_chainthoughtmonitorability_2026` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_commentnistoutline_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_cyberworkstream_nd` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_earlybestpractices_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_foundationalsecurity_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_introducingtechnical_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_issuebriefmeasuring_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_managingadvancedcyber_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `fmf_mitigations_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `fmf_nuclearsecurity_2026` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_nuclearworkstream_nd` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_preliminarytaxonomy_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_preliminarytaxonomy_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `fmf_publications_nd` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_risktaxonomythresholds_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `fmf_thirdpartyassessments_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `fmf_thresholdsfrontier_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `folkerts_measuringaiagentscyber_2026` | Full text | Logged; see CSV scope | [C01](claims.md#c01), [C03](claims.md#c03) | — | — |
| `frick_evaluaterewardrlhf_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `g42_frontieraisafetyframework_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `gebru_datasheets_2021` | Selected sections | Outside 105-record register | [C44](claims.md#c44) | — | [r2_sociotechnical_01](rounds.md#r2_sociotechnical_01) |
| `glazer_frontiermathbenchmark_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `gloaguen_finetuningactivated_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `goemans_safetycasetemplate_2024` | Full text | Logged; see CSV scope | [C20](claims.md#c20) | — | — |
| `google_gtig_promptingautonomy_2026` | Full text | Logged; see CSV scope | [C22](claims.md#c22) | — | — |
| `greenblatt_alignmentfaking_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `greenblatt_controlimprovingsafety_2024` | Selected sections | Outside 105-record register | [C30](claims.md#c30) | — | [r2_oversight_05](rounds.md#r2_oversight_05) |
| `guan_deliberativealignment_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `habli_bigargumentsafety_2025` | Selected sections | Outside 105-record register | [C20](claims.md#c20) | — | — |
| `hackenburg_evaluatingpersuasive_2024` | Full text | Logged; see CSV scope | [C15](claims.md#c15) | — | — |
| `harmbench_standardizedevaluation_2024` | Selected sections | Outside 105-record register | duplicate work family | Fresh PMLR metadata corroborates the named HarmBench study family, but this record’s DOI/alias and edition mapping remain unverified. It has an explicit related-work role without separate empirical support; no automatic key merge or new full-text label. See F01 and r2_safeguards_03. | [r2_safeguards_03](rounds.md#r2_safeguards_03) |
| `hayes_inexactunlearningneeds_2024` | Abstract only | Outside 105-record register | [C35](claims.md#c35) | Later selected reading of the related arXiv v3 corrects the inherited user-level shorthand to per-example versus population U-MIA and adds retained-data privacy outcomes. The final SaTML edition remains unauthenticated; no final-paper full-text upgrade is claimed. See C35 and r2_safeguards_05/08. | [r2_safeguards_05](rounds.md#r2_safeguards_05), [r2_safeguards_08](rounds.md#r2_safeguards_08) |
| `heap_sparseautoencoders_2025` | Full text | Logged; see CSV scope | [C13](claims.md#c13) | — | — |
| `heim_trainingcomputethresholds_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `hilton_safetycasesscalable_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `homewood_thirdpartycompliance_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `hsu_safelorasilver_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `hu_realignsafetyaligning_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `hua_steeringevaluation_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `huang_collectiveconstitutional_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `huang_endlessjailbreaksbijection_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `huang_trustllm_2024` | Selected sections | Outside 105-record register | background | — | [r2_sociotechnical_06](rounds.md#r2_sociotechnical_06) |
| `hubinger_sleeperagentstraining_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `isoiec_42001_2023` | Metadata only | Outside 105-record register | Unresolved | — | — |
| `isoiec_42006_2025` | Metadata only | Outside 105-record register | [C17](claims.md#c17) | The supplied correction codes legal_status not_applicable for this certification-body standard. Catalog/preview inspection does not verify licensed normative clauses or a statutory duty; see C17 and reconciliation.md. | — |
| `jimenez_swebench_2023` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `jose_strategicobfuscation_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `joshi_robustevaluationunlearning_2024` | Full text | Logged; see CSV scope | [C04](claims.md#c04) | — | — |
| `kamath_tracingattentioncomputatio_2025` | Full text | Logged; see CSV scope | [C13](claims.md#c13) | — | — |
| `kapoor_aiagentsmatter_2024` | Selected sections | Outside 105-record register | [C43](claims.md#c43) | — | [r2_sociotechnical_02](rounds.md#r2_sociotechnical_02) |
| `karvonen_measuringprogressdictionar_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `kenton_scalableoversightweak_2024` | Full text | Logged; see CSV scope | [C11](claims.md#c11), [C12](claims.md#c12) | — | — |
| `khan_debatingmorepersuasive_2024` | Full text | Logged; see CSV scope | [C11](claims.md#c11), [C12](claims.md#c12) | — | — |
| `kirk_sabotageaisafetyresearch_2026` | Selected sections | Outside 105-record register | [C14](claims.md#c14) | — | — |
| `korbak_chainthoughtmonitorability_2025` | Full text | Logged; see CSV scope | [C31](claims.md#c31) | — | [r2_oversight_06](rounds.md#r2_oversight_06) |
| `kressel_safeai_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `kutasov_evaluatingsabotage_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `lambert_rewardbenchevaluating_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `lan_sparseautoencoders_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `lang_debatehelpsweak_2025` | Full text | Logged; see CSV scope | [C28](claims.md#c28), [C29](claims.md#c29) | The newly retained arXiv v1 has9 PDF pages, while the inherited reading description names17. This run checked selected methods/results and does not recertify that earlier full-text label or infer an error without the earlier bytes. Training findings retain task/model-gap/ensemble limits. See C28–C29 and r2_oversight_03. | [r2_oversight_03](rounds.md#r2_oversight_03) |
| `lee_constructingsafety_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `li_backdoorllmcomprehensive_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `li_cancovertlysandbag_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `li_wmdpbenchmarkmeasuring_2024` | Selected sections | Outside 105-record register | [C04](claims.md#c04) | — | — |
| `liang_helm_2023` | Selected sections | Outside 105-record register | [C46](claims.md#c46) | — | [r2_sociotechnical_04](rounds.md#r2_sociotechnical_04) |
| `lin_artemispenetration_2026` | Full text | Logged; see CSV scope | [C21](claims.md#c21) | Later v2 checking confirms the scoped comparison and corrects locators: Cybench is Table2/section3.3, costs section5.4, and human attack-graph design Appendix E opening. Table3/section6 disagree on TinyPilot hint levels, which are omitted. Final OpenReview access remains blocked; no venue upgrade. See C21 and r2_claimchecks_03–04. | [r2_claimchecks_03](rounds.md#r2_claimchecks_03), [r2_claimchecks_04](rounds.md#r2_claimchecks_04) |
| `lindsey_biology_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `liu_agentbench_2023` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `liu_promptinjectionattacks_2025` | Full text | Logged; see CSV scope | [C07](claims.md#c07) | The supplied correction package is integrated, preserving this citation key and identifying the USENIX2024 Liu paper/arXiv2310.12815. The unrelated StruQ identifier/abstract are removed. Inherited full-text depth refers to the intended proceedings paper, not StruQ or the expanded preprint; see C07 and reconciliation.md. | — |
| `liu_rethinkingmachineunlearnin_2024` | Selected sections | Outside 105-record register | [C04](claims.md#c04) | — | — |
| `longpre_inhouseevaluation_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `longpre_safeharbor_2024` | Selected sections | Outside 105-record register | [C40](claims.md#c40) | — | [r2_institutions_04](rounds.md#r2_institutions_04) |
| `macdiarmid_naturalemergentmisalignmen_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `magic_agireadinesspolicy_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `makelov_principledevaluations_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `maple_jailbreak07methodology_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `mazeika_harmbenchstandardized_2024` | Selected sections | Outside 105-record register | [C34](claims.md#c34) | Fresh PMLR metadata and selected final-paper methods corroborate the same named study family as harmbench_standardizedevaluation_2024. Exact DOI/alias mapping and edition equivalence remain open; both keys are retained and not counted as independent corroboration. See F01/C34 and r2_safeguards_02–03. | [r2_safeguards_02](rounds.md#r2_safeguards_02) |
| `mcgregor_preventingrepeatedfailures_2021` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `meinke_frontiercapablecontext_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `meta_advancedaiscalingframeworkv2_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `metr_commonelementsfrontier_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `metr_examplesafetysecurity_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `metr_timehorizons_2026` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `mialon_gaia_2023` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `microsoft_frontiergovernance_2025` | Full text | Logged; see CSV scope | [C18](claims.md#c18) | — | — |
| `microsoft_frontiergovernance_2026` | Full text | Logged; see CSV scope | [C18](claims.md#c18) | — | — |
| `mitchell_modelcards_2019` | Full text | Logged; see CSV scope | [C20](claims.md#c20) | — | — |
| `mitre_atlasdata_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `mlcommons_ailuminate_2026` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `mlcommons_ailuminatejailbreakv05_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `mlcommons_ailuminatev10_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `mokander_auditinglargelanguagemodels_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `murray_mappingbenchmarkdata_2025` | Full text | Logged; see CSV scope | [C25](claims.md#c25) | Use the hypothetical malware-development/deployment step rather than infrastructure-attack shorthand. The strongest elicitation condition covered five selected tasks, not all 40. The estimate is expert judgment, not observed causal uplift; see reconciliation.md. | — |
| `nasr_scalableextraction_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `naver_aisafetyframework_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `ncsc_secureaisystemdevelopment_2023` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `newyork_raiseact_article44b_nd` | Full text | Logged; see CSV scope | Unresolved | The supplied correction records enacted_not_in_force with Jan1,2027 applicability from the prior statute review. Fresh official-page access returned403; the date is inherited rather than newly independently verified. See reconciliation.md. | — |
| `nguyen_probingsteeringevaluation_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `nist_airmf10_2023` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `nist_artificialintelligence_2024` | Selected sections | Outside 105-record register | [C17](claims.md#c17) | — | — |
| `nist_managingmisuserisk_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `nist_managingmisuserisk_2025_2pd` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `nist_outlineproposedzero_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `nist_systemdocumentation_nd` | Inaccessible | Outside 105-record register | Unresolved | — | — |
| `nvidia_frontierriskassessment_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `oecd_commonreportingincidents_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `oecd_dashboardentryhlab_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `oecd_hiroshimaprocesscode_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `oecd_hiroshimaprocessreporting_2025` | Full text | Logged; see CSV scope | [C17](claims.md#c17) | — | — |
| `oecd_launchesglobalmonitor_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `oecd_launchespilotmonitor_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `oecd_trendsincidentshazards_2026` | Selected sections | Outside 105-record register | [C27](claims.md#c27) | — | — |
| `oecd_wonk_nd` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `omb_2024federalagency_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `omb_m2410_2024` | Selected sections | Outside 105-record register | Unresolved | The supplied correction repairs the official URL and retains superseded status. The prior review identifies rescission/replacement by M25-21; no fresh full-history verification is claimed. See reconciliation.md. | — |
| `omb_m2521_2025` | Selected sections | Outside 105-record register | Unresolved | This record was outside the specific legal recoding changes in the supplied patch. Existing status/application labels remain inherited and require dated review before current-law use. See reconciliation.md. | — |
| `omb_m2522_2025` | Selected sections | Outside 105-record register | Unresolved | This record was outside the specific legal recoding changes in the supplied patch. Existing status/application labels remain inherited and require dated review before current-law use. See reconciliation.md. | — |
| `openai_blogupdatingpreparedness_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `openai_frontiertrainingenvironment_2026` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `openai_gpt53codexsystemcard_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `openai_monitoringmonitorability_2025` | Selected sections | Outside 105-record register | [C31](claims.md#c31) | — | [r2_oversight_07](rounds.md#r2_oversight_07) |
| `openai_o1systemcard_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `openai_pacingcyberdevelopment_2026` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `openai_preparednessbeta_2023` | Full text | Logged; see CSV scope | [C19](claims.md#c19) | — | — |
| `openai_preparednessv2_2025` | Full text | Logged; see CSV scope | [C19](claims.md#c19) | — | — |
| `owasp_aitestingguidev1_2025` | Metadata only | Outside 105-record register | Unresolved | — | — |
| `owasp_llmtop10_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `paulo_automaticallyinterpreting_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `pavlova_automatedredteaming_2024` | Full text | Logged; see CSV scope | [C33](claims.md#c33) | — | [r2_safeguards_06](rounds.md#r2_safeguards_06) |
| `perset_developersmanaging_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `phuong_evaluatingfrontier_2024` | Full text | Logged; see CSV scope | [C02](claims.md#c02) | — | — |
| `qi_safetyalignmentshould_2025` | Full text | Logged; see CSV scope | [C34](claims.md#c34) | — | [r2_safeguards_07](rounds.md#r2_safeguards_07), [r2_safeguards_09](rounds.md#r2_safeguards_09) |
| `rai_practicalreviewmechanistic_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `raji_closingaccountabilitygap_2020` | Selected sections | Outside 105-record register | [C41](claims.md#c41) | — | [r2_institutions_05](rounds.md#r2_institutions_05) |
| `raji_outsideroversight_2022` | Selected sections | Outside 105-record register | [C39](claims.md#c39), [C41](claims.md#c41) | — | [r2_institutions_03](rounds.md#r2_institutions_03) |
| `rand_governanceapproaches_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `rao_challengesmonitoring_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `salvi_conversationalpersuasivene_2025` | Full text | Logged; see CSV scope | [C15](claims.md#c15) | — | — |
| `samvelyan_rainbowteamingopen_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `sastry_computingpowergovernance_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `sba_complianceplanomb_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `scheurer_canstrategicallydeceive_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `schuett_frontierdevelopers_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `schuett_surveythresholdsadvanced_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `sehwag_propensitybench_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `sharkey_openproblemsmechanistic_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `sharma_constitutionalclassifiers_2025` | Selected sections | Outside 105-record register | [C06](claims.md#c06) | — | — |
| `sharma_criticalevaluation_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `sheshadri_whydosome_2025` | Abstract only | Outside 105-record register | [C14](claims.md#c14) | — | — |
| `shevlane_modelevaluationextreme_2023` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `souly_astraunsanctioned_2026` | Full text | Logged; see CSV scope | [C24](claims.md#c24) | The supplied correction is integrated: selected simulated scenarios bound generalization; prompt restrictions differ from live controls and defense_persistence has a bounds link. Original assessments remain. See C24 and reconciliation.md. | — |
| `souly_poisoningattacksrequire_2025` | Selected sections | Outside 105-record register | [C07](claims.md#c07) | — | — |
| `statedepartment_complianceplanomb_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `stelling_evaluatingaiproviders_2025` | Abstract only | Outside 105-record register | [C17](claims.md#c17) | — | — |
| `stix_behindcloseddoors_2025` | Abstract only | Outside 105-record register | Unresolved | — | — |
| `sudhir_benchmarkscalableoversight_2025` | Selected sections | Outside 105-record register | [C32](claims.md#c32) | — | [r2_oversight_01](rounds.md#r2_oversight_01) |
| `swamy_minimaximalistapproach_2024` | Abstract only | Outside 105-record register | Unresolved | — | — |
| `tamirisa_tamperresistantsafeguards_2024` | Selected sections | Outside 105-record register | [C07](claims.md#c07) | — | — |
| `taylor_auditinggames_2025` | Selected sections | Outside 105-record register | [C14](claims.md#c14) | — | — |
| `taylor_schoolrewardhacks_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `templeton_scalingmonosemanticity_2024` | Selected sections | Outside 105-record register | [C13](claims.md#c13) | — | — |
| `ukgov_frontiersafetycommitments_2024` | Full text | Logged; see CSV scope | [C17](claims.md#c17) | — | — |
| `ukparliament_securityinstitute_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `unadvisorybodyai_governinghumanityfinal_2024` | Metadata only | Outside 105-record register | Unresolved | — | — |
| `vassilev_adversarialmltaxonomy_2025` | Selected sections | Outside 105-record register | [C07](claims.md#c07) | — | — |
| `vega_bypassingsafetytraining_2024` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `vir_subliminalcorruption_2025` | Full text | Logged; see CSV scope | Unresolved | — | — |
| `wallace_estimatingworstcase_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `wallace_instructionhierarchy_2024` | Full text | Logged; see CSV scope | [C07](claims.md#c07) | — | — |
| `wan_foundationmodeltransparency_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `wang_adversarialpreference_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `wang_catastrophiccertifying_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `wang_decodingtrust_2023` | Abstract only | Outside 105-record register | [C47](claims.md#c47) | — | [r2_sociotechnical_05](rounds.md#r2_sociotechnical_05) |
| `wang_helpsteer2opensource_2024` | Selected sections | Outside 105-record register | [C08](claims.md#c08) | — | — |
| `wang_helpsteer2preference_2024` | Selected sections | Outside 105-record register | [C08](claims.md#c08) | — | — |
| `wang_interpretablepreferences_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `wang_largenotfairevaluators_2024` | Full text | Logged; see CSV scope | [C09](claims.md#c09) | — | — |
| `wang_pandoraswhite_2024` | Abstract only | Outside 105-record register | Unresolved | — | — |
| `wang_selftaughtevaluators_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `wang_star1safer_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `wef_globalcybersecurity_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `wehner_taxonomyopportunities_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `weidinger_sociotechnicalsafety_2023` | Selected sections | Outside 105-record register | [C27](claims.md#c27) | — | — |
| `wijk_rebench_2025` | Selected sections | Outside 105-record register | [C03](claims.md#c03) | Exact final proceedings methods are now checked: the32-hour human result is best of four8-hour attempts, and experts could use LLMs/tools. This is not a no-AI human baseline. Remaining appendices/runs were not fully read or reproduced. See C03 and r2_claimchecks_01–02. | [r2_claimchecks_01](rounds.md#r2_claimchecks_01), [r2_claimchecks_02](rounds.md#r2_claimchecks_02) |
| `xai_frontierartificialintelligenceframework_2025` | Full text | Logged; see CSV scope | [C26](claims.md#c26) | — | — |
| `xie_osworld_2024` | Selected sections | Outside 105-record register | [C01](claims.md#c01) | — | — |
| `xu_benchmarkingleakage_2024` | Full text | Logged; see CSV scope | [C10](claims.md#c10) | Fresh paper/helper/README comparison confirms the formula/threshold mismatch. The helper can preserve preexisting scores and is not an experiment manifest. Affected lenient leakage rates stay omitted; no new186-row or model reproduction is claimed. See C10 and r2_claimchecks_05–07. | [r2_claimchecks_05](rounds.md#r2_claimchecks_05), [r2_claimchecks_06](rounds.md#r2_claimchecks_06), [r2_claimchecks_07](rounds.md#r2_claimchecks_07) |
| `xu_magpiealignmentdata_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `xu_theagentcompany_2024` | Selected sections | Outside 105-record register | [C01](claims.md#c01) | — | — |
| `yao_taubench_2024` | Selected sections | Outside 105-record register | [C01](claims.md#c01) | — | — |
| `ye_learningjudgepreference_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `yousefpour_representationbending_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `yu_robustsafeguarding_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `zhang_activationspaceanchored_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `zhang_agentsafetybench_2024` | Abstract only | Outside 105-record register | Unresolved | — | — |
| `zhang_generativeverifiers_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `zhang_holisticautomatedred_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `zhang_persistentpretraining_2025` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `zhang_safetyoneshot_2026` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `zhang_selfexploringactive_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `zhang_vtuneverifiablefine_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
| `zhao_surveyrecentbackdoor_2024` | Selected sections | Outside 105-record register | Unresolved | — | — |
