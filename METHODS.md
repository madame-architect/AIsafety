# Methods

**Frontier AI Governance Evals - v3; reconstructed account, 2026-10-16**

## Purpose and status

This document records the confirmed history and current stabilization procedures for Frontier AI Governance Evals, a curated collection about frontier AI evaluation and governance. The earlier May 2026 Methods text remains unavailable. This dated reconstruction does not reproduce that document or establish a protocol that preceded collection.

The stabilization merged in PR #13 reconciles existing artifacts, makes YAML records authoritative, generates BibTeX, and introduces provisional synthesis routing. That work added no newly discovered references or literature search. A subsequent targeted review, documented below, prepares the cyber capability evaluations and deployment safeguards research focus.

## Legacy collection and provenance

An independent researcher assembled the collection iteratively with substantial generative AI assistance in discovery, bibliographic normalization, classification, quality checks, and documentation. The legacy artifacts include a bibliography, taxonomy, YAML schema, and Python linter. Their existence does not establish that every proposed research procedure was performed.

The recovered May V2 bibliography contains **276 records**, independently counted using two parsers. It retains all **218 citation keys** on the pre-migration GitHub baseline and contains **58 additional keys**. The historical report of 262 entries was stale. These are counts of bibliographic records, not independently verified studies. The frozen inputs are retained in [`provenance/may-2026/`](provenance/may-2026/); [`MIGRATION.md`](MIGRATION.md) and [`provenance/reconciliation.json`](provenance/reconciliation.json) account for the migration.

A complete history of legacy searches, excluded candidates, screening decisions, and source-inspection depth is unavailable. This release therefore makes no claim of systematic or exhaustive search, independent dual coding, inter-rater reliability, preregistration, or original experiments. Missing provenance remains unknown. A later inspection is recorded on its actual date, rather than presented as an original screening decision. Retired research material remains historical unless explicitly restored.

## Authoritative records and generated export

[`records.yaml`](records.yaml) is the authoritative editable collection. Its root `schema_version` is `frontier-governance-evals-v3`; each record has `id`, `entry_type`, and `fields`. The stabilization preserved the six inherited entry types and substantive field values; later supported corrections are recorded separately. Controlled multivalue fields use string lists. BibTeX and its keyword mirrors are generated from these records. Do not add a `keywords` field to the records. The schema defining allowed structures and values is separate from the records themselves. The generated [index](views/index.md) reports the current record and stream counts.

Citation keys identify records. DOI, URL, title, and source version can help identify possible duplicates or related versions, but no single match establishes equivalence in every case. Distinct versions should remain distinguishable when their content matters. Renames, merges, exclusions, and substantive corrections require a recorded reason.

Migration and source verification are separate activities. Preserving a field does not certify its accuracy; a corrected format does not establish that a publication was inspected again. Existing publication and access dates retain their inherited meanings.

## Synthesis routing

Two substantive synthesis streams are accompanied by a contextual category. The scalar fields `synthesis_stream` and `stream_note` record the route and its explanation.

| Value | Intended contribution |
|---|---|
| `technical_eval` | Technical evaluations, benchmarks, evaluation methods, or tools for assessing AI systems or safeguards |
| `governance_artifact` | Operational policies, frameworks, regulations, standards, guidance, commitments, or oversight mechanisms |
| `contextual` | Analysis, commentary, or other research that is neither a technical evaluation or method nor an operational governance artifact |

The initial routing was **provisional and AI-assisted**, based on inherited metadata, titles, and available abstracts. The five sources identified in the targeted review now have dated AI-assisted full-text checks; this does not extend to the other 271 records. Publication format or issuer alone does not establish a route. Ambiguous contributions should be reviewed before inclusion in a substantive synthesis; relevant passages can serve multiple discussions while retaining one record identity.

A later technical synthesis should examine what was tested, the threat model, design, conditions, results, reproducibility, and limitations. It should distinguish proposed methods from observed results. A governance synthesis should examine authority, scope, requirements or commitments, and evidence of implementation. Policy existence does not establish effectiveness. Contextual sources can inform interpretation without being counted as direct technical findings or operational governance commitments.

## Confidence and evidence quality

The inherited `classification_confidence` values are unchanged. They do not rate the newly assigned synthesis routes or the quality of the underlying evidence. Classification confidence concerns an annotation; evidence quality concerns how well a source supports a particular claim.

A confidently identified policy can provide no empirical evidence of implementation. An empirical finding may have important limitations despite clear classification. Source type, independence, review status, and reproducibility are informative dimensions, not interchangeable quality scores. Missing annotations indicate uncoded or unavailable information rather than proven absence of a property.

## Future intake and maintenance

Future additions use a small intake log. These procedures apply prospectively and do not reconstruct legacy screening events.

1. Record the actual discovery date, source or service, candidate identifier, and exact query when applicable. Identify direct recommendations and citation following as such.
2. Check existing identifiers, titles, and versions before accepting a candidate as new.
3. Record the material inspected: full text, abstract, or specified sections. Search snippets and AI summaries alone do not establish results or full verification.
4. Record inclusion, exclusion, or deferral with a short reason and unresolved questions. Inclusion requires a stated connection to the collection's scope, not agreement with the conclusions.
5. Record supported annotations, validate the records, and regenerate the export.

For changing documents, record version/publication claims and actual access dates.
Every new documentary observation must follow the [source capture procedure](provenance/source-capture.md),
including exact-byte provenance and a checked archival representation where
legally and technically feasible. Bibliographic metadata alone does not establish
a historical snapshot. Later reviews of legacy entries retain actual review dates.

## Targeted source review: 2026-10-16

The [cyber/deployment verification report](research/cyber-deployment/source-verification.md) records a bounded check of five existing sources: Phuong, Goemans, Murray, OpenAI Preparedness v2, and DeepMind Frontier Safety Framework v3.1. It links claims and corrections to primary texts and page/section locators, records inspected PDF hashes, and distinguishes document revisions from later issuer clarifications. The collection remains at 276 records. The exact field changes are in the accompanying [audit JSON](research/cyber-deployment/source-verification.json).

AI assistants inspected the primary full texts, including relevant appendices, checked official version histories and selected institutional/author publication pages, and compared the evidence with the inherited records. Version searches were bounded; failure to locate a later publication is not proof of its absence. No experiments or elicitation analyses were reproduced. Five rows in `intake.csv` record these actual later reviews, not legacy discovery or screening dates.

For the three inspected arXiv papers, `url` pins the version, `date` records that revision's submission date, and `origdate` records the first submission when different. The Phuong PDF's different cover date is preserved in a note. The papers' optional `version_status` remains unset: latest listed arXiv revision is narrower than verified overall publication lineage. OpenAI's unsupported `current` label is removed; DeepMind's is retained with dated positive evidence from its official latest-version link. Both framework records cite a static PDF; later webpage statements do not silently rewrite that object.

For the mixed GovAI/AISI and SaferAI/academic papers, scalar issuer tags use the documented lead institution, supported by both affiliations and institutional publication pages. Evidence notes retain the other institutions. This is a stated coding convention for these records, not a claim of exclusive authorship or independent verification. Coverage tags describe what a document addresses; they do not mean every tagged domain has empirical results or every discussed safeguard is mandatory.

## Longitudinal cyber commitment pilot: 2026-10-17 UTC

The [cyber research guide](research/cyber-deployment/README.md) introduces a
bounded comparison of one model-weight security recommendation in two existing
DeepMind framework editions. Companion YAML records source observations and
scoped policy provisions; a separate build generates the readable history.
The bibliography remains at 276 records. This pilot does not revise the earlier
five-source audit or reclassify other entries.

The unit is a scoped provision, linked across observations by a stable ID.
Publication, actual inspection, and any source-claimed application date have
different meanings. Modality, qualifications, source rationale, exact locators,
and the analyst's comparison are retained. Absence from an inspected passage is
not coded as withdrawal. The current format accepts policy statements only;
implementation and effectiveness require separate attributed evidence and have
not been assessed in this pilot.

AI assistants compared specified primary passages, including definitions and
general qualifications. This was targeted document analysis, not a systematic
search, independent human coding, experimental reproduction, or compliance
audit. Both observations disclose a preservation gap: edition-specific issuer
URLs were inspected, but no new source-byte capture or independent archive was
retained for these observations. Existing earlier inspection hashes keep their
original provenance.

## Prospective capture and release protocol: 2026-10-24

Evidence v2 requires `original_url`, `retrieved_at`, `archive_url`,
`archive_checked_on`, `sha256`, `byte_length`, `mime_type`, `published_on`,
`version_claim`, and `locator_basis` for every new source observation. Unknown
publication/version claims remain null. Missing archives require a specific
explanation. Hash exact retrieved PDF bytes or the preserved HTML representation;
keep the current source location distinct from a historical capture.

The two original pilot records are explicitly frozen as `legacy_uncaptured`,
with unavailable capture fields null. No historical hash or archive has been
invented, and no new retrieval is attributed to their 2026-10-17 inspection.
The regenerated history exposes these fields and limitations. This migration
changes preservation structure, not the extracted policy provisions or the
276-record bibliography. Implementation and effectiveness remain unassessed.

The [release protocol](releases/README.md) binds an exact tagged commit and all
payload files, including authoritative YAML and generated outputs, to SHA-256
and byte lengths. GitHub publication and OSF deposit have separate byte-verified
receipts. OSF verification records actual project/object/version identifiers;
a GitHub merge or successful local build never establishes synchronization.
The capture and release tooling and tests were developed with AI assistance;
mocked network tests do not establish a live archive or OSF deposit.

## Bounded cyber integration and OpenAI comparison: 2026-10-24

The [integration report](research/cyber-deployment/expansion-reconciliation-2026-10-24.md) and [audit JSON](research/cyber-deployment/integration-audit-2026-10-24.json) document this pass. Six sources already accepted into the operational-risk dataset are reconciled into canonical bibliography records; four policy sources are added to support an OpenAI within-issuer history. The corpus grows from the stabilized 276 records to 286. This is not a new empirical research round: the six evidence observations and dated assumption assessments remain unchanged.

Duplicate screening compares normalized titles, source URLs, and arXiv identifiers with the checked 282-record PR input, excluding the candidate's own already-created ID. Reinspection restores full author lists and version metadata. Provider threat reports and an incident disclosure are routed to the contextual stream, not treated as normative governance merely because they are official. Three research papers remain technical methods/evaluations. The system card enters the governance stream for its specifically inspected policy clarification; its other experimental findings are not admitted by this act.

Seven scoped OpenAI provisions are compared across the beta and v2 frameworks, a later system-card clarification, and two 2026 policy statements. Stable IDs and explicit predecessor links represent documentary continuity without asserting equivalence of beta risk ratings and v2 capability labels. Critical capability definitions and the development gate are coded separately. The internal-use clarification preserves v2's ambiguous wording; its system card's cover date does not establish when the Note was inserted. No inferred application date is assigned. Later policy statements are not mislabeled as a new numbered framework edition or proof of compliance.

Eleven exact source representations recovered from the retained private capture bundle were re-read and checked for identity, SHA-256, length, and relevant locators. The original retrieval and archive-check dates remain attached to those earlier capture events; the recovery/reinspection is not relabeled as a fresh network capture. Metadata and archived locators are committed, while copyrighted full-text payloads remain outside Git. The existing v2 retrieval event retains its own timestamp and is linked to an identical earlier retained payload. The two frozen DeepMind observations retain their missing-capture disclosures. No OSF deposit, original-publication byte identity, independent human coding, or experimental reproduction is claimed.

## Validation, releases, and AI assistance

Run `python3 scripts/build.py` to generate the outputs and `python3 scripts/build.py --check` to check them. Automated validation addresses data structure and export consistency. Successful checks do not establish source accuracy, evidence quality, comprehensive coverage, or scholarly validity. Tag distributions describe this collection rather than the prevalence of findings in the field.

GitHub pull requests prepare changes for maintainer review. OSF synchronization is a separate release task: on 2026-10-16 the project page returned a maintenance notice, so no comparison or upload was completed. The [prepared deposit](releases/stabilization-2026-10-16.md) uses the already merged stabilization commit, excluding this later source-review update. Synchronization must be confirmed against deposited files before being reported as complete.

AI assisted the migration, provisional routing, code, this reconstructed document, and the separately logged targeted source review. A complete retrospective list of models and prompts is unavailable and is not invented. The maintainer is responsible for accepting releases and research claims. An AI-assisted second pass is not independent human coding. Future syntheses should document the source inspection, review, and AI assistance actually performed.

