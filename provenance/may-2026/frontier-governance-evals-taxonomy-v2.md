# Frontier Governance/Evals Bibliography Taxonomy — v2

Generated: 2026-05-04

This version refactors the earlier taxonomy into a schema-first model. The main change is that the old `artifact_type`/keyword mix is split into separate fields for document form, source role, and governance artifact. Legacy fields are retained for one migration cycle, but v2 filters should prefer the new fields.

## What changed in v2

| Change | Result |
|---|---|
| Promoted legacy keyword namespaces | `risk_domain`, `threat_vector`, `lifecycle_stage`, `release_model`, and `evidence_basis` are now first-class fields. |
| Split mixed artifact semantics | `source_form` describes the citation object; `governance_artifact` describes the governance/evals object; `source_role` describes how the source functions evidentially. |
| Reworked issuer sector | `issuer_sector` is now broad sectoral provenance: `private`, `public`, `multilateral`, `academic`, `standards`, `civil_society`, `industry`, or `media`. |
| Reworked review process | `review_process` now uses process-oriented values such as `author_posted_preprint`, `institutional_review`, and `legal_process`. |
| Split evidence independence | `attestation_relation` and `independence_from` make the evidence relationship clearer while retaining legacy `evidence_independence`. |
| Added directness semantics | `function_role` distinguishes `direct`, `enabling`, `background`, and `commentary` uses. |
| Added maintenance/legal status | `maintenance_status` and `legal_status` separate lifecycle maintenance from legal force. |
| Added auditable rationale | `inclusion_reason` and `classification_confidence` make entry-level classification more reviewable. |

## Core v2 fields

| Field | Meaning | Controlled values |
|---|---|---|
| `source_form` | The document or citation form. | `paper`, `working_paper`, `policy_paper`, `report`, `policy_report`, `industry_report`, `issue_brief`, `corporate_framework`, `framework`, `benchmark`, `regulation`, `executive_order`, `memorandum`, `guidance`, `code_of_practice`, `compliance_plan`, `policy_page`, `portal`, `workstream_page`, `documentation_portal`, `report_page`, `research_page`, `dashboard_entry`, `dataset`, `survey`, `tool`, `press_release`, `blog_post`, `news_article`, `comment_letter`, `commitment_statement`, `written_statement`, `progress_report`, `annual_report`, `outline`, `standard` |
| `source_role` | The evidential role played by the source. | `original_research`, `official_statement`, `official_guidance`, `legal_or_regulatory_instrument`, `standards_or_consensus_artifact`, `industry_guidance`, `public_comment`, `news_reporting`, `aggregator_or_portal`, `external_analysis` |
| `governance_artifact` | The governance/evals artifact represented or analyzed. | `research_analysis`, `policy_analysis`, `eval_method`, `benchmark`, `company_framework`, `policy_framework`, `implementation_guidance`, `legal_instrument`, `standard`, `system_card`, `official_communication`, `portal_or_registry`, `policy_page`, `code_of_practice`, `commitment`, `official_statement`, `transparency_dashboard`, `dataset`, `news_reporting`, `risk_report`, `research_index`, `public_comment` |
| `scope_relevance` | Centrality to frontier governance/evals research. | `core`, `supporting`, `contextual`, `peripheral` |
| `function_role` | How directly the source supports its governance functions. | `direct`, `enabling`, `background`, `commentary` |
| `classification_confidence` | Confidence in the classification assignment, not in the truth of source claims. | `high`, `medium`, `low` |

## Issuer, review, and evidence fields

| Field | Meaning | Controlled values |
|---|---|---|
| `issuer_type` | Entity type issuing the source. | `company`, `government`, `intergovernmental`, `academic_or_research`, `standards_body`, `ngo_research`, `industry_forum`, `media` |
| `issuer_sector` | Broad sectoral provenance. | `private`, `public`, `multilateral`, `academic`, `standards`, `civil_society`, `industry`, `media` |
| `review_process` | Process that produced or reviewed the source. | `peer_reviewed`, `author_posted_preprint`, `institutional_review`, `editorial_review`, `legal_process`, `standards_consensus` |
| `attestation_relation` | Who is attesting to the evidence or claim. | `self_attested`, `issuer_attested`, `author_attested`, `external_analysis`, `regulatory_authority`, `journalistic_reporting`, `community_consensus` |
| `independence_from` | Whether the source is independent of the subject whose evidence or practice is being described. | `subject_self`, `issuer_self`, `not_independently_verified`, `independent_of_subject`, `regulatory_authority`, `editorial_independence`, `community_consensus` |
| `evidence_basis` | Broad evidentiary basis. | `research`, `procedural`, `policy`, `legal`, `reference`, `journalistic`, `dataset`, `research_synthesis`, `tooling`, `benchmark`, `commentary` |

## Governance-function and risk fields

| Field | Meaning | Controlled values |
|---|---|---|
| `governance_function` | One or more governance functions supported by the source. | `evaluation`, `audit`, `monitoring`, `reporting`, `mitigation` |
| `risk_domain` | One or more risk domains discussed or governed. | `cyber`, `autonomy`, `cbrn`, `privacy`, `systemic_risk`, `persuasion`, `bio`, `misuse`, `safety`, `loss_of_control`, `chemical`, `fairness`, `model_interpretability`, `multimodal`, `agentic_reliability`, `model_security` |
| `threat_vector` | One or more threat vectors or failure modes. | `adaptive_attacker`, `supply_chain`, `insider`, `expert_uplift`, `non_expert_uplift`, `jailbreak`, `intentional_subversion`, `prompt_injection`, `excessive_agency`, `self_replication`, `red_teaming`, `flaw_disclosure`, `agentic_misalignment` |
| `lifecycle_stage` | AI lifecycle stages covered. | `pretraining`, `post_training`, `deployment`, `post_deployment`, `procurement` |
| `release_model` | Model release or access mode where relevant. | `closed`, `open_weights` |

## Version, maintenance, and legal fields

| Field | Meaning | Controlled values |
|---|---|---|
| `version_status` | Artifact lineage status. Omit when unknown. | `current`, `draft`, `superseded`, `historical`, `living_document` |
| `maintenance_status` | Whether the cited object is static or maintained. | `static`, `maintained_page`, `living_document` |
| `legal_status` | Legal force for legal/regulatory instruments; `not_applicable` otherwise. | `not_applicable`, `authoritative`, `proposed`, `superseded`, `historical` |
| `supersedes` | Citation key for an earlier artifact superseded by this entry. | Citation key |
| `superseded_by` | Citation key for the later artifact that supersedes this entry. | Citation key |
| `evidence_note` | Free-text explanation for special validation or interpretation cases. | Free text |
| `inclusion_reason` | Generated rationale for why the source is included and how it is being used. | Free text |
| `classification_note` | Optional manual note for non-obvious classification decisions. | Free text |

## Retained legacy fields

The following fields remain in `frontier-governance-evals-v2.bib` for compatibility, but new filtering should prefer the v2 fields above.

| Legacy field | Prefer |
|---|---|
| `source_relation` | `source_role` plus, where needed, `attestation_relation` |
| `artifact_type` | `source_form` and `governance_artifact` |
| `review_status` | `review_process` |
| `evidence_independence` | `attestation_relation` and `independence_from` |

## Keyword mirror policy

The `keywords` field is regenerated from the formal fields. Current v2 field mirrors are included as `field/value` tags. The four retained legacy fields are also mirrored for one migration cycle. The old duplicate namespaces `document_type`, `source_status`, and `assurance_function` are removed from the v2 keywords.

## Validation rules

Use the canonical v2 filenames:

```bash
pdflatex -interaction=nonstopmode test-v2.tex
biber --validate-datamodel test-v2
pdflatex -interaction=nonstopmode test-v2.tex
pdflatex -interaction=nonstopmode test-v2.tex
python frontier-governance-evals-lint-v2.py frontier-governance-evals-v2.bib
```

Expected target: `0` Biber datamodel errors, `0` Biber datamodel warnings, and `0` semantic-linter failures.

## Current v2 corpus summary

| Measure | Count |
|---|---:|
| Entries | 236 |
| Entries with `source_form` | 236 |
| Entries with `source_role` | 236 |
| Entries with `governance_artifact` | 236 |
| Entries with `risk_domain` | 96 |
| Entries with `threat_vector` | 68 |
| Entries with `lifecycle_stage` | 183 |
| Entries with `release_model` | 10 |
