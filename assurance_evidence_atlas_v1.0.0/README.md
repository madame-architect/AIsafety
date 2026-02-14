# Assurance Evidence Atlas (v1.0.0)

This folder contains **machine-readable downloads + schemas** for the ongoing AI Safety Literature Review.

## Contents

### Data
- `data/s2_t3_governance_atlas_v1.0.0-2026-02-14.csv`
- `data/s2_t3_governance_atlas_v1.0.0-2026-02-14.jsonl`
- `data/s2_t3_governance_dedupe_groups_v1.0.0-2026-02-14.csv`
- `data/technical_eval_gaming_monitorability_bibliography_v1.0.0-2026-02-14.csv`
- `data/technical_eval_gaming_monitorability_bibliography_v1.0.0-2026-02-14.jsonl`
- `data/safety_case_evidence_atlas_v1.0.0-2026-02-14.csv`
- `data/safety_case_evidence_atlas_v1.0.0-2026-02-14.jsonl`
- `data/study_selection_log_v1.0.0.csv`

### Schemas
- `schema/governance_atlas_schema_1.0.0.json`
- `schema/technical_bibliography_schema_1.0.0.json`
- `schema/safety_case_evidence_atlas_schema_1.0.0.json`

### Documentation
- `CODEBOOK.md`
- `METHODOLOGY.md`
- `protocol_lock_v1.0.0.json`

## PRISMA-style flow summary (Protocol v1.0.0)
Based on `data/study_selection_log_v1.0.0.csv`:

- **Records considered:** 157
- **Included (atlas-linked):** 145
  - Linked to governance artifacts (`S2-T3-*`): 100
  - Linked to technical bibliography (`paper_id`): 45
- **Excluded:** 12
  - Out of scope / not AI-specific: 4
  - No assurance method: 3
  - Domain mismatch / wrong outcome: 3
  - Insufficient reporting / secondary commentary / duplicates: 2

Reason-code definitions and full per-record decisions are in `METHODOLOGY.md` and `data/study_selection_log_v1.0.0.csv`.

## Version-locked protocol policy
This atlas release locks evidence-identification methods to **Protocol v1.0.0** using:
- fixed query IDs and exact query strings,
- fixed inclusion/exclusion criteria and reason-code semantics,
- and a lock manifest with SHA-256 digests in `protocol_lock_v1.0.0.json`.

Future atlas versions must either reuse this protocol unchanged or declare drift explicitly so cross-version comparisons remain auditable.

## Notes
- Governance Tier Three inventory is taken verbatim (descriptions + ordering) from `deep-research-report (2).md`.
- Tags are heuristic + manually corrected for obvious misclassifications; review low `tag_confidence` rows first.


## Assurance stress-test pilot v0.1
This release now includes a preregistered pilot package for methodology hardening:
- `ASSURANCE_STRESS_TEST_PILOT_v0.1.md`
- `data/search_execution_log_v0.1.csv`
- `data/gold_set_stratified_v0.1.csv`
- `data/dual_annotation_labels_v0.1.csv`
- `data/adjudication_log_v0.1.csv`
- `data/irr_summary_v0.1.json`
- `data/coverage_matrix_v0.1.csv`
- `data/coverage_gaps_v0.1.csv`
- `data/bias_assessment_v0.1.csv`
- `data/evidence_quality_scores_v0.1.csv`
- `data/sensitivity_analysis_v0.1.csv`

These additions provide: a fixed last-24-month technical search replay log, stratified dual-annotation scaffolding with IRR outputs, an explicit 5-axis coverage matrix with gap diagnostics, and quantitative evidence-quality/sensitivity artifacts.
