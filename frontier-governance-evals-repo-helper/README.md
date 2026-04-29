# Frontier AI Governance & Evals Bibliography

This repository contains a curated **BibLaTeX/Biber** bibliography for frontier AI governance, evaluations, assurance, risk frameworks, and adjacent policy/research materials.

## What is in this repo

| File | Purpose |
|---|---|
| `frontier-governance-evals.bib` | Main bibliography file. Copied from `AI - Frontier Governance Evals - Revised(1).bib` without content changes. |
| `bibliography.taxonomy.yml` | Data dictionary for custom fields and `keywords` taxonomy values. |
| `scripts/validate_bib.py` | Lightweight validator for citation keys, required fields, and taxonomy conventions. |
| `.github/workflows/validate-bibliography.yml` | Optional GitHub Actions workflow for validating bibliography pull requests. |

## Current inventory

- **Entries:** 210
- **Entry types:** `@article` 16, `@dataset` 1, `@misc` 103, `@online` 32, `@report` 58
- **Unique keyword tags:** 92 across 10 namespaces
- **Custom fields used throughout:** `review_status`, `issuer_type`, `annotation`
- **Version tracking:** `version` is present on 19 entries where useful

## Format expectations

The file is intended for **BibLaTeX with Biber**, not minimal BibTeX. Entries may include custom fields that are useful for research workflows but may not render directly in every citation style.

Every entry should include:

```bibtex
@report{example_key_2026,
    author = {{Example Organization}},
    title = {Example frontier AI governance report},
    institution = {Example Organization},
    type = {Framework},
    date = {2026},
    year = {2026},
    url = {https://example.org/report.pdf},
    urldate = {2026-04-29},
    version = {1.0},
    keywords = {document_type/corporate_framework, source_status/primary, evidence_basis/procedural, lifecycle_stage/deployment, assurance_function/eval, review_status/institutional, issuer_type/company},
    review_status = {institutional},
    issuer_type = {company},
    annotation = {Use for comparing frontier AI governance frameworks and evaluation requirements.}
}
```

## Citation key convention

Use stable, readable keys:

```text
<lead_author_or_org>_<shorttitle>_<year>
```

Examples:

```text
deepmind_frontiersafetyv31_2026
nist_managingmisuserisk_2024
charnock_expandingexternalaccess_2026
```

For undated online sources, use `_nd` only when no reliable publication date is available.

## Keyword taxonomy

Keywords use this pattern:

```text
namespace/value
```

### Required on every entry

Each entry should have exactly one tag from each of these namespaces:

- `document_type/*`
- `source_status/*`
- `evidence_basis/*`

### Recommended on every entry

These should be present both as custom fields and mirrored in `keywords`:

- `review_status/*`
- `issuer_type/*`

### Optional, multi-value namespaces

Use these as needed:

- `risk_domain/*`
- `lifecycle_stage/*`
- `assurance_function/*`
- `threat_vector/*`
- `release_model/*`

See `bibliography.taxonomy.yml` for the current allowed values.

## Common filters

Find corporate frameworks:

```bash
rg "document_type/corporate_framework" frontier-governance-evals.bib
```

Find cyber-related entries:

```bash
rg "risk_domain/cyber" frontier-governance-evals.bib
```

Find sources relevant to evaluations:

```bash
rg "assurance_function/eval" frontier-governance-evals.bib
```

Find preprints:

```bash
rg "review_status/preprint" frontier-governance-evals.bib
```

## Validation

Run the helper script before opening a pull request:

```bash
python scripts/validate_bib.py frontier-governance-evals.bib bibliography.taxonomy.yml
```

To treat warnings as failures after cleanup work is complete:

```bash
python scripts/validate_bib.py frontier-governance-evals.bib bibliography.taxonomy.yml --strict
```

The validator checks:

- Duplicate citation keys
- Required fields: `author`, `title`, `keywords`, `review_status`, `issuer_type`, `annotation`
- Required taxonomy namespaces: `document_type`, `source_status`, `evidence_basis`
- Mirrored keyword tags for `review_status` and `issuer_type`
- Unknown keyword tags, when PyYAML is available

## Contribution checklist

Before adding or editing an entry:

1. Confirm the source is in scope: frontier AI governance, evaluations, assurance, risk management, incident reporting, dangerous capabilities, or directly relevant policy/research.
2. Use BibLaTeX-friendly entry types and fields.
3. Preserve capitalization with braces where needed, especially `{AI}`, `{NIST}`, `{CBRN}`, `{TEVV}`, and organization names.
4. Add DOI, URL, version, and access date when available.
5. Assign one `document_type`, one `source_status`, and one `evidence_basis` tag.
6. Add `risk_domain`, `lifecycle_stage`, `assurance_function`, `threat_vector`, and `release_model` tags only when they are directly supported by the source.
7. Fill `review_status` and `issuer_type` custom fields, and mirror them in `keywords`.
8. Add a concise `annotation` explaining why the source is useful.
9. Run the validator.

## Current cleanup backlog

These are known documentation/curation issues in the current snapshot, not blocking errors:

- 17 entries have `review_status` and `issuer_type` custom fields but do not yet mirror them as `keywords` tags.
- 8 entries are missing `date`; most appear to be undated online or portal sources.
- 8 entries are missing `url`; most are article-style records where DOI metadata may be sufficient but URL coverage should be checked.
- Some risk-domain tags are intentionally granular, but maintainers may want to decide whether overlapping values such as `bio`, `chemical_biological`, and `cbrn` should remain distinct.

## Maintenance notes

- Prefer small pull requests: one thematic addition or cleanup at a time.
- Do not remove tags only because a citation style does not display them; the taxonomy supports search, evidence mapping, and research synthesis.
- When updating a corporate framework or standard, keep older versions only if they are needed for historical comparison; otherwise update `version`, `date`, `url`, and `urldate` together.
