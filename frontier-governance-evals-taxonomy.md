# Frontier Governance/Evals Bibliography Taxonomy

Generated: 2026-04-30

This guide defines the custom fields used in `frontier-governance-evals.bib`. The fields are mirrored into `keywords` as `field/value` tags where practical, so the bibliography can be filtered either through BibLaTeX fields or through keyword searches.

## Core source fields

| Field | Meaning | Current controlled values |
|---|---|---|
| `source_relation` | Relationship between the source and the claim or artifact being studied. `primary` is used for original artifacts or direct issuer statements; `secondary` is used for analysis, reporting, comments, or interpretation of another artifact; `tertiary` is reserved for aggregators and indexes. | `primary`, `secondary`, `tertiary` |
| `scope_relevance` | How central the source is for frontier governance/evals research. | `core`, `supporting`, `contextual`, `peripheral` |
| `artifact_type` | The kind of object represented by the entry. | `company_framework`, `policy_framework`, `policy_report`, `technical_paper`, `eval_method`, `benchmark`, `guidance`, `regulation`, `standard`, `system_card`, `blog_post`, `portal`, `policy_page`, `code_of_practice`, `commitment`, `working_paper`, `policy_paper`, `press_release`, `written_statement`, `dashboard_entry`, `dataset`, `news`, `risk_report`, `research_page`, `public_comment` |
| `version_status` | Whether the cited artifact is current, draft, superseded, historical, or explicitly maintained as a living document. Omit this field when status is unknown. | `current`, `draft`, `superseded`, `historical`, `living_document` |

## Issuer and review fields

| Field | Meaning | Current controlled values |
|---|---|---|
| `issuer_type` | The type of entity issuing the source. Intergovernmental bodies are separated from domestic government bodies. | `company`, `government`, `intergovernmental`, `academic_or_research`, `standards_body`, `ngo_research`, `industry_forum`, `media` |
| `issuer_sector` | The broader sector of the issuer. This field is intentionally aligned with `issuer_type` except that `academic_or_research` is shortened to `academic`. | `company`, `government`, `intergovernmental`, `academic`, `standards_body`, `ngo_research`, `industry_forum`, `media` |
| `review_status` | The source’s evidentiary status: whether it is peer reviewed, preprint-only, institutionally issued, editorial, legal/regulatory, or standards/community guidance. | `peer_reviewed`, `preprint`, `institutional`, `editorial`, `legal_or_regulatory`, `standard_or_community_guidance` |
| `review_process` | The process that produced or reviewed the source. This may match `review_status`, but it is process-oriented rather than status-oriented. | `peer_reviewed`, `preprint`, `institutional`, `editorial`, `legal`, `community_standard` |
| `evidence_independence` | The independence relationship between the source and the evidence it provides. This field should not duplicate review process. | `self_attested`, `issuer_attested`, `author_attested`, `third_party`, `regulatory`, `journalistic`, `community_or_industry_consensus` |

### `evidence_independence` usage notes

- `self_attested`: a company or industry forum describing its own practices, safeguards, frameworks, or model behavior.
- `issuer_attested`: an official institutional source describing its own policy, reporting process, dashboard, or framework without third-party verification.
- `author_attested`: a preprint or author-posted research source that has not been independently peer reviewed.
- `third_party`: external analysis or peer-reviewed work where the evidentiary review is independent of the author/issuer.
- `regulatory`: legal, regulatory, or formally authoritative materials such as statutes, official rules, executive orders, memoranda, or code-of-practice guidance.
- `journalistic`: news/editorial reporting.
- `community_or_industry_consensus`: standards, community-maintained guidance, or consensus artifacts.

## Governance-function fields

| Field | Meaning | Current controlled values |
|---|---|---|
| `governance_function` | One or more governance functions the source supports. This field is optional for contextual, technical, journalistic, or background sources that do not directly support evaluation, audit, monitoring, reporting, or mitigation. | `evaluation`, `audit`, `monitoring`, `reporting`, `mitigation` |
| `supersedes` | Citation key for the earlier artifact superseded by this entry. | Citation key |
| `superseded_by` | Citation key for the later artifact that supersedes this entry. | Citation key |
| `evidence_note` | Free-text note explaining special validation or interpretation cases. | Free text |

## Undated online sources

Some portal, workstream, and documentation pages have no stable publication date in the available citation metadata. These remain `@online` entries without `date`/`year`, carry an `urldate`, and include `evidence_note`.

The accompanying `.dbx` intentionally uses `\ResetDatamodelConstraints` and then rebuilds the needed standard constraints so that `@online` entries can validate with title plus URL/DOI/eprint and `urldate`, without inventing publication dates. This is a local validation policy for this bibliography, not a general-purpose BibLaTeX datamodel replacement.

## Validation target

Use the canonical filenames:

```bash
pdflatex -interaction=nonstopmode test.tex
biber --validate-datamodel test
pdflatex -interaction=nonstopmode test.tex
pdflatex -interaction=nonstopmode test.tex
```

The expected target is `0` Biber errors and `0` Biber warnings when `frontier-governance-evals-datamodel.dbx` is loaded. The final LaTeX pass should clear ordinary citation/rerun warnings from the minimal validation document.
