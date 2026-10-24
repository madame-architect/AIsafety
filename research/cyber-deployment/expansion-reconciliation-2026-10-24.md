# Commitment-history expansion and admitted-source bibliography reconciliation

Status: **work in progress**. This file is a review ledger, not a claim of canonical admission, source preservation, or completed policy coding.

## Canonical bibliography reconciliation

The six research-admitted operational-risk sources in `operational-risk/source-admission.yaml` need matching records in authoritative `../../records.yaml` (repository root), then generated BibTeX and views. The stable proposed IDs are:

| Source ID | Proposed canonical record ID | Evidence type |
| --- | --- | --- |
| `amazon_fortigate_ai_augmented_2026` | `amazon_fortigateaiaugmented_2026` | Provider operational threat intelligence |
| `google_gtig_prompting_to_autonomy_2026` | `google_gtig_promptingautonomy_2026` | Provider operational threat intelligence |
| `aisi_unsanctioned_agent_incident_2026` | `aisi_unsanctionedagentincident_2026` | Government incident disclosure (HTML only) |
| `lin_artemis_pentest_2026` | `lin_artemispenetration_2026` | Authorized live comparative study; arXiv 2512.09882v2 |
| `barrett_quantitative_cyber_risk_2025` | `barrett_quantitativecyberrisk_2025` | Quantitative modeled risk; arXiv 2512.08864v2 |
| `souly_astra_unsanctioned_supply_chain_2026` | `souly_astraunsanctioned_2026` | Simulated alignment evaluation; arXiv 2609.38415v1 |

Before changing admission status, rerun normalized duplicate checks against current `records.yaml`; inspect version-pinned originals; retain byte length, SHA-256, MIME type, retrieval time and independent archive reference or documented obstacle. A URL is not a historical capture. The separate AISI technical incident PDF remains **unadmitted** until full-text inspection.

## Commitment-history expansion scope

Start with within-issuer version comparisons for OpenAI's Preparedness Framework, then link to existing DeepMind FSF cyber weight-security observations. Track separate provisions for:

1. Cyber capability threshold and the evaluation/elicitation conditions that define it.
2. Deployment or release decision and any exception authority.
3. Development-stage access, model-weight security and internal-use restrictions.
4. Monitoring, red-teaming, reassessment and incident escalation.
5. Later public clarifications, with their own dated observations and document locators.

Do not equate a publication date with the date an undated web clarification was inserted. Do not infer withdrawal from silence. Record the exact scope, modality, trigger, action, qualification, rationale, source edition and predecessor for each provision. A commitment link to an operational-risk assumption does not establish causation or implementation.

## Required acceptance checks

- `python3 scripts/build.py --check`
- `python3 scripts/build_commitments.py --check`
- `python3 research/cyber-deployment/operational-risk/build.py --check`
- `python3 scripts/build_cyber_datasets.py --check`
- `python3 -m unittest discover -s tests -v`
- Verify bibliography and research-admission identifiers resolve; check no duplicate citations.
- Preserve source provenance; do not manufacture historical checksums.
- Keep GitHub merge, tagged release and verified OSF synchronization as separate states.

This ledger intentionally does not mark these checks passed.
