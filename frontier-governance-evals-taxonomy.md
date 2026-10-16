# Frontier Governance/Evals Bibliography Taxonomy — v3

Updated: 2026-10-16

This guide defines the classification fields in the authoritative [records.yaml](records.yaml). The [schema](frontier-governance-evals-schema.yml), version `frontier-governance-evals-v3`, specifies controlled values, required fields, supported entry types, and keyword mirrors. The complete BibTeX bibliography and the [stream index](views/index.md) are generated outputs.

This stabilization preserves the useful v2 distinctions between document form, source role, artifact, evidence provenance, risk, and lifecycle. It adds a primary synthesis route and explanatory note without replacing inherited classifications. It introduces no newly discovered references, literature search, or research synthesis. See [METHODS.md](METHODS.md) for provenance and interpretation limits.

## Authoritative record structure

Each record has an `id` (its citation key), an `entry_type`, and a `fields` mapping. Supported entry types are `article`, `dataset`, `inproceedings`, `misc`, `online`, and `report`. The entry type controls the citation format; it does not determine the synthesis stream or evidence quality.

Use YAML string lists for the five controlled multivalue fields: `governance_function`, `risk_domain`, `threat_vector`, `lifecycle_stage`, and `release_model`. Other fields use strings. Preserve internal BibTeX/TeX braces and commands in bibliographic values. Required controlled fields and allowed values come from the schema; ordinary bibliographic metadata and free-text notes remain within `fields`.

## Synthesis streams

| Field | Meaning | Values |
|---|---|---|
| `synthesis_stream` | One primary route for later synthesis. Required scalar field. | `technical_eval`, `governance_artifact`, `contextual` |
| `stream_note` | Brief explanation of the assigned route, including mixed contributions or uncertainty where relevant. Required scalar field. | Free text |

| Stream | Use for | Limits of interpretation |
|---|---|---|
| `technical_eval` | Evaluations, benchmarks, evaluation datasets, and technical methods or tools for assessing systems or safeguards. | Includes proposed methods; membership does not imply observed experimental results or demonstrated effectiveness. |
| `governance_artifact` | Actual frameworks, requirements, regulations, standards, guidance, commitments, organizational disclosures, and governance portals. | An artifact's existence does not establish implementation, compliance, independent verification, or effectiveness. |
| `contextual` | Policy analysis, commentary, and supporting research that is neither a technical evaluation or method nor an operational governance artifact. | Useful for interpretation; not automatically direct technical evidence or an operational requirement. |

Current routing is provisional and AI-assisted, based on inherited metadata, titles, and available abstracts. It does not represent renewed full-source verification. A mixed-purpose source keeps one citation identity and one primary route; relevant passages may inform other discussions without creating an additional independent source. Review ambiguous routes before using them in a substantive synthesis.

### Distinctions that matter

- The inherited **field** `governance_artifact` describes the kind of object represented or analyzed, including values such as `eval_method`, `research_analysis`, and `policy_analysis`. The new **value** `synthesis_stream: governance_artifact` identifies one synthesis route. The inherited field's presence does not put a record in that route.
- `source_role: original_research` can describe a technical evaluation or a contextual analysis. The contribution determines the route, not the publication format, issuer, or role alone.
- `scope_relevance` expresses centrality to this collection. Its value `contextual` is distinct from the synthesis route of the same name: a contextual analysis can still be central to the project's research scope.
- Inherited `classification_confidence` values are unchanged. They describe legacy classification confidence, not confidence in the new routes, source correctness, or evidence quality. `stream_note` explains routing without supplying a new confidence score.

## Retained v2 foundations

| Change | Result |
|---|---|
| Promoted legacy keyword namespaces | `risk_domain`, `threat_vector`, `lifecycle_stage`, `release_model`, and `evidence_basis` are now first-class fields. |
| Split mixed artifact semantics | `source_form` describes the citation object; `governance_artifact` describes the governance/evals object; `source_role` describes how the source functions evidentially. |
| Reworked issuer sector | `issuer_sector` is now broad sectoral provenance: `private`, `public`, `multilateral`, `academic`, `standards`, `civil_society`, `industry`, or `media`. |
| Reworked review process | `review_process` now uses process-oriented values such as `author_posted_preprint`, `institutional_review`, and `legal_process`. |
| Split evidence independence | `attestation_relation` and `independence_from` make the evidence relationship clearer while retaining legacy `evidence_independence`. |
| Added directness semantics | `function_role` distinguishes `direct`, `enabling`, `background`, and `commentary` uses. |
| Added maintenance/legal status | `maintenance_status` and `legal_status` separate lifecycle maintenance from legal force. |
| Retained classification rationale | `inclusion_reason`, `classification_note`, and `classification_confidence` support inspection of inherited annotations; their presence does not establish independent review. |

## Core source fields

| Field | Meaning | Controlled values |
|---|---|---|
| `source_form` | The document or citation form. | `paper`, `working_paper`, `policy_paper`, `report`, `policy_report`, `industry_report`, `issue_brief`, `corporate_framework`, `framework`, `benchmark`, `regulation`, `executive_order`, `memorandum`, `guidance`, `code_of_practice`, `compliance_plan`, `policy_page`, `portal`, `workstream_page`, `documentation_portal`, `report_page`, `research_page`, `dashboard_entry`, `dataset`, `survey`, `tool`, `press_release`, `blog_post`, `news_article`, `comment_letter`, `commitment_statement`, `written_statement`, `progress_report`, `annual_report`, `outline`, `standard` |
| `source_role` | The evidential role played by the source. | `original_research`, `official_statement`, `official_guidance`, `legal_or_regulatory_instrument`, `standards_or_consensus_artifact`, `industry_guidance`, `public_comment`, `news_reporting`, `aggregator_or_portal`, `external_analysis` |
| `governance_artifact` | The governance/evals artifact represented or analyzed. | `research_analysis`, `policy_analysis`, `eval_method`, `benchmark`, `company_framework`, `policy_framework`, `implementation_guidance`, `legal_instrument`, `standard`, `system_card`, `official_communication`, `portal_or_registry`, `policy_page`, `code_of_practice`, `commitment`, `official_statement`, `transparency_dashboard`, `dataset`, `news_reporting`, `risk_report`, `research_index`, `public_comment` |
| `scope_relevance` | Centrality to frontier governance/evals research. | `core`, `supporting`, `contextual`, `peripheral` |
| `function_role` | How directly the source supports its governance functions. | `direct`, `enabling`, `background`, `commentary` |
| `classification_confidence` | Preserved confidence in legacy classifications; does not rate the new synthesis route or truth of source claims. | `high`, `medium`, `low` |

## Issuer, review, and evidence fields

| Field | Meaning | Controlled values |
|---|---|---|
| `issuer_type` | Entity type issuing the source. | `company`, `government`, `intergovernmental`, `academic_or_research`, `standards_body`, `ngo_research`, `industry_forum`, `media` |
| `issuer_sector` | Broad sectoral provenance. | `private`, `public`, `multilateral`, `academic`, `standards`, `civil_society`, `industry`, `media` |
| `review_process` | Process that produced or reviewed the source. | `peer_reviewed`, `author_posted_preprint`, `institutional_review`, `editorial_review`, `legal_process`, `standards_consensus` |
| `attestation_relation` | Who is attesting to the evidence or claim. | `self_attested`, `issuer_attested`, `author_attested`, `external_analysis`, `regulatory_authority`, `journalistic_reporting`, `community_consensus` |
| `independence_from` | Whether the source is independent of the subject whose evidence or practice is being described. | `subject_self`, `issuer_self`, `not_independently_verified`, `independent_of_subject`, `regulatory_authority`, `editorial_independence`, `community_consensus` |
| `evidence_basis` | Broad evidentiary basis. | `research`, `procedural`, `policy`, `legal`, `reference`, `journalistic`, `dataset`, `research_synthesis`, `tooling`, `benchmark`, `commentary` |

These dimensions describe the source and its relationship to the subject. They are not interchangeable quality grades. Peer review does not itself establish independence from the evaluated organization; an external issuer does not itself establish independent replication. Inherited values are preserved annotations and should be checked against the actual source before supporting such claims.

## Governance-function and risk fields

| Field | Meaning | Controlled values |
|---|---|---|
| `governance_function` | One or more governance functions supported by the source. | `evaluation`, `audit`, `monitoring`, `reporting`, `mitigation` |
| `risk_domain` | One or more risk domains discussed or governed. | `cyber`, `autonomy`, `cbrn`, `privacy`, `systemic_risk`, `persuasion`, `bio`, `misuse`, `safety`, `loss_of_control`, `chemical`, `fairness`, `model_interpretability`, `multimodal`, `agentic_reliability`, `model_security` |
| `threat_vector` | One or more threat vectors or failure modes. | `adaptive_attacker`, `supply_chain`, `insider`, `expert_uplift`, `non_expert_uplift`, `jailbreak`, `intentional_subversion`, `prompt_injection`, `excessive_agency`, `self_replication`, `red_teaming`, `flaw_disclosure`, `agentic_misalignment` |
| `lifecycle_stage` | AI lifecycle stages covered. | `pretraining`, `post_training`, `deployment`, `post_deployment`, `procurement` |
| `release_model` | Model release or access mode where relevant. | `closed`, `open_weights` |

These five fields are optional and can contain multiple values. Missing values indicate that a property is uncoded or unavailable, not that the source demonstrably lacks it. The inherited `threat_vector` vocabulary mixes threat mechanisms, failure modes, and evaluation activities such as `red_teaming`; it is preserved for compatibility and should not be treated as a homogeneous set of attacker categories.

## Version, maintenance, and legal fields

| Field | Meaning | Controlled values |
|---|---|---|
| `version_status` | Artifact lineage status. Omit when unknown. | `current`, `draft`, `superseded`, `historical`, `living_document` |
| `maintenance_status` | Whether the cited object is static or maintained. | `static`, `maintained_page`, `living_document` |
| `legal_status` | Legal force for legal/regulatory instruments; `not_applicable` otherwise. | `not_applicable`, `authoritative`, `proposed`, `superseded`, `historical` |
| `supersedes` | Citation key for an earlier artifact superseded by this entry. | Citation key |
| `superseded_by` | Citation key for the later artifact that supersedes this entry. | Citation key |
| `evidence_note` | Free-text explanation for special validation or interpretation cases. | Free text |
| `inclusion_reason` | Inherited explanation of inclusion and intended use; may be AI-generated and is not a reconstructed screening event. | Free text |
| `classification_note` | Optional note for non-obvious classification decisions. | Free text |

Version, maintenance, legal status, and access dates are inherited descriptions, not a claim that every source was checked again on the v3 revision date. Do not invent publication dates for undated pages. Preserve available access dates and explain missing or changing source information in the relevant note; new checks use their actual dates.

## Retained legacy fields

The following fields remain in the authoritative records and generated [BibTeX export](frontier-governance-evals.bib) for compatibility. New filtering should prefer the more specific fields above. This release does not remove legacy fields or promise an automatic conversion between concepts that are not equivalent.

| Legacy field | Prefer |
|---|---|
| `source_relation` | `source_role` plus, where needed, `attestation_relation` |
| `artifact_type` | `source_form` and `governance_artifact` |
| `review_status` | `review_process` |
| `evidence_independence` | `attestation_relation` and `independence_from` |

## Keyword mirror policy

Do not store or edit `keywords` in `records.yaml`. The build generates the BibTeX `keywords` field from the schema's `keyword_mirror_policy`, using `field/value` tags for controlled values. This includes `synthesis_stream` and the four retained legacy fields. Free-text `stream_note` is exported as a field but is not mirrored as a keyword. The duplicate historical namespaces `document_type`, `source_status`, and `assurance_function` are not generated.

Change authoritative fields and rebuild to change the mirrors. A keyword mirror repeats an annotation for filtering; it is not additional evidence or an independently derived classification.

## Build, validation, and counts

From the repository root:

```bash
python3 scripts/build.py
python3 scripts/build.py --check
```

The build validates the records and generates the complete bibliography, keyword mirrors, and disjoint stream views. `--check` checks the same outputs without writing files and fails if an export is absent or stale. Validation checks structural and semantic consistency of the metadata; it does not establish source accuracy, empirical reliability, or literature coverage. The [README](README.md) gives setup instructions, and [MIGRATION.md](MIGRATION.md) records validation results and limitations.

The [generated index](views/index.md) is the source for current record and stream counts. Historical counts in frozen provenance files describe earlier artifacts and are not current collection statistics. Stream totals count one primary membership per record, not separate claims, experiments, or independent sources of corroboration.
