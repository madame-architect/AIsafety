# Changelog

## v1.0.0 (v1.0.0-2026-02-14)

- Exported Tier Three governance inventory (100 items; IDs S2-T3-01…S2-T3-100) into CSV + JSONL.
- Added evidence tags: artifact_type, assurance_function, domain, verification_strength.
- Added de-duplication scaffolding via canonical_group_id + dedupe groups CSV.
- Exported technical bibliography subset for evaluation gaming / monitorability (45 entries) into CSV + JSONL.
- Created initial safety-case evidence atlas (10 claims) linking governance artifacts to candidate technical methods.

Known limitations:
- URLs/DOIs are not fully normalized for governance artifacts because the authoritative draft stores citations as internal reference markers.
- Some issuer normalizations remain heuristic (see rows with low tag_confidence).



## v1.0.2-methodology (2026-02-15)

Protocol freeze + methodology upgrades (no mutation to v1.0.0 core IDs):
- Upgraded `METHODOLOGY.md` to Protocol v1.1.0 with explicit preregistration + drift policy.
- Added explicit bias scoring model and normalized bias-risk formula.
- Added reliability scoring model tied to Cohen's kappa strata means.
- Added quantified evidence-strength index and tier mapping.
- Added reliability and evidence-strength exports (`data/reliability_scoring_v0.1.csv`, `data/evidence_strength_quantification_v0.1.csv`).
- Updated lock manifest to include protocol-critical scoring artifacts.

## v1.0.1-pilot (2026-02-14)

Methodology hardening add-ons (no mutation to v1.0.0 core IDs):
- Added preregistered stress-test pilot protocol: `ASSURANCE_STRESS_TEST_PILOT_v0.1.md`.
- Added 24-month technical query execution log: `data/search_execution_log_v0.1.csv`.
- Added stratified gold set + dual-annotation artifacts + adjudication + IRR summary.
- Added explicit five-axis coverage matrix and coverage-gap diagnostics.
- Added structured threat-of-bias table and Evidence Quality Score (EQS) export.
- Added sensitivity-analysis table for key robustness scenarios.
