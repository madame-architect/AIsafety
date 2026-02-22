# AI Safety Evidence Atlas (Working Repository)

This repository contains a **structured AI safety annotated bibliography** and its supporting schema documents.

It is best understood as an **evidence curation project** for assurance/safety-case workflows, not as a conventional software codebase.

## What this repo is for

The main artifact maps literature and policy sources into a consistent evidence format so you can answer:

- what claim an item supports,
- how strong that evidence is,
- which threat model it assumes,
- where it applies in the lifecycle,
- and what limitations remain.

## Repository contents

- `ai-safety-Literature_Review.md`
  - Primary artifact: the consolidated annotated bibliography and synthesis.
  - Includes executive synthesis, evidence gaps, a safety-case crosswalk table, and per-source entries.

- `SCHEMA.md`
  - **Normative record schema** for entries.
  - Defines required fields, formatting rules, controlled-value expectations, and consistency checks.

- `TAG_VOCAB.md`
  - Controlled vocabulary definitions for tagging dimensions (risk domain, lifecycle stage, assurance function, threat model, method area).
  - Includes clarifications and tagging decision guidance.

- `ai-safety-literature_review.bib`
  - Bibliographic database corresponding to sources used in the review.

- `LICENSE`
  - Licensing terms for repository materials.

## Current status

- **Status:** Active draft / work in progress.
- Content is being iterated for coverage, locator quality, and tagging consistency.
- Not a final publication.

## How to contribute safely

When editing or adding entries in `ai-safety-Literature_Review.md`:

1. Follow `SCHEMA.md` as the source of truth for required fields and structure.
2. Use only controlled tags defined in `TAG_VOCAB.md`.
3. Prefer improving free-text annotations over inventing new one-off tags.
4. Keep identifiers/locators stable and auditable (DOI, arXiv, CELEX, official URLs where possible).

## Intended users

- AI safety and governance researchers.
- Assurance, audit, and policy analysis teams.
- Collaborators maintaining evidence pipelines across governance and technical domains.

## Practical note

If you expected executable code, tests, or packaged tooling: this repository currently focuses on **research artifacts and metadata governance**, not software deliverables.
