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
