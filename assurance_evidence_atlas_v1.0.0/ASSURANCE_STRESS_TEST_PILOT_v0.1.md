# Assurance Stress-Test Pilot v0.1 (Preregistered)

## Objective
Freeze the evidence codebook and audit coverage on two pressure points:
1. **Evaluation integrity** (resistance to gaming/evaluation-awareness failure modes).
2. **Comprehensiveness** (coverage across governance claims, evidence types, domains, threat models, and failure modes).

## Scope freeze
- Codebook freeze reference: `CODEBOOK.md` (v1.0.0 definitions retained without mutation).
- Protocol lock reference: `protocol_lock_v1.0.0.json`.
- This pilot appends new artifacts under `data/*_v0.1.*` without renumbering prior IDs.

## Preregistered search replay (technical pressure point)
- Query ID: `Q-TECH-24M-01`
- Date window: **2024-02-14 to 2026-02-14** (last 24 months from execution date)
- Language: English
- Databases: Scopus, Web of Science, IEEE Xplore, arXiv, OpenAlex
- Logged execution: `data/search_execution_log_v0.1.csv`

## Inclusion criteria (technical, pilot replay)
- Empirical or protocol-bearing work relevant to evaluation gaming, evaluation awareness, monitorability, or monitor evasion.
- Bibliographic metadata sufficient for stable linking.
- Publication date within the preregistered 24-month window.

## Exclusion criteria (technical, pilot replay)
- Commentary-only works lacking evaluable methods.
- Non-AI-specific or non-transferable domain material.
- Records lacking sufficient methodological detail for evidence coding.

## Dual-annotation plan
- Stratified gold set: `data/gold_set_stratified_v0.1.csv`
- Dual labels: `data/dual_annotation_labels_v0.1.csv`
- Disagreement protocol log: `data/adjudication_log_v0.1.csv`
- IRR summary: `data/irr_summary_v0.1.json`

### Stratification axes
- Governance: `assurance_function` strata (`requirements`, `evidence`, `audit`).
- Technical: `topic_primary` strata (`evaluation_gaming`, `monitorability`).

## Bias model
Structured bias tables are exported to `data/bias_assessment_v0.1.csv`:
- Governance: self-attestation bias, incentive alignment bias, regulatory-capture risk, publication bias.
- Technical: benchmark overfitting bias, evaluation leakage bias, distribution shift bias, obfuscation risk.

## Quantitative evidence model
Evidence Quality Score (EQS), 0–3 components:

`EQS = 0.25*reproducibility + 0.20*adversarial_robustness + 0.25*independent_verification + 0.20*ecological_validity - 0.10*gaming_susceptibility`

Export: `data/evidence_quality_scores_v0.1.csv`.

## Reliability scoring
Reliability scoring is derived from preregistered dual-annotation IRR outputs (`data/irr_summary_v0.1.json`) using stratum means:
- Governance reliability: mean kappa(`artifact_type`, `assurance_function`, `verification_strength`).
- Technical reliability: mean kappa(`threat_model`, `gaming_resistance`).

Export: `data/reliability_scoring_v0.1.csv`.

## Quantified evidence strength
Evidence strength combines quality, reliability, and bias into a single calibrated index:

`evidence_strength_index = clamp(0,1, 0.60*(eqs_score/3) + 0.25*reliability_score - 0.15*bias_risk_score)`

Tiering:
- strong (>= 0.70)
- moderate (0.50-0.69)
- preliminary (< 0.50)

Export: `data/evidence_strength_quantification_v0.1.csv`.

## Coverage matrix requirement
Five-axis matrix export: `data/coverage_matrix_v0.1.csv`
- Governance claims
- Evidence types
- Domains
- Threat models
- Failure modes

Gap report: `data/coverage_gaps_v0.1.csv`.

## Sensitivity tests
`data/sensitivity_analysis_v0.1.csv` includes baseline vs filtered scenarios:
- Exclude self-attested governance artifacts.
- Independently-verifiable-only governance subset.
- Exclude evaluation-awareness-tagged technical records.
- DOI-only technical subset (replication proxy).

## Limitations (v0.1)
- Pilot dual annotation is a process dry-run and must be replicated with genuinely independent annotators in v0.2.
- EQS uses heuristic component scoring and is intended for calibration, not definitive causal inference.
