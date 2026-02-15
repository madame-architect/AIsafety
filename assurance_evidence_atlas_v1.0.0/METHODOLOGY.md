# Methodology (Protocol v1.1.0)

## Purpose
This protocol documents how records were identified, screened, and linked into the Assurance Evidence Atlas so future versions can be compared for methodological drift.

## Pre-registered protocol freeze
Protocol v1.1.0 hard-freezes the following before scoring or synthesis:
- Search sources, query IDs, and exact query strings.
- Date/language limits.
- Inclusion/exclusion criteria and reason-code semantics.
- Scoring formulas for bias, reliability, sensitivity, and evidence strength.

Any future change must be recorded as declared drift in release notes and a new lock manifest.

## Search databases
Primary databases/search engines used for protocolized retrieval:
- Scopus
- Web of Science Core Collection
- IEEE Xplore
- arXiv
- OpenAlex
- Google Scholar (supplementary backward/forward citation checks only)

## Exact query strings

### Q-GOV-01 (governance artifacts)
```
("AI assurance" OR "AI governance" OR "AI risk management" OR "model evaluation standard" OR "AI audit" OR "safety case")
AND
(standard* OR framework OR guideline* OR policy OR regulation OR profile OR code)
AND
(verification OR "third-party" OR independent OR compliance OR conformance)
```

### Q-TECH-01 (evaluation gaming and monitorability evidence)
```
("evaluation gaming" OR "benchmark overfitting" OR "data contamination" OR monitorability OR "reward hacking" OR "specification gaming")
AND
("foundation model" OR "large language model" OR LLM OR "machine learning")
AND
(detect* OR audit* OR monitor* OR "red team" OR "holdout" OR protocol)
```

### Q-SNOWBALL-01 (citation chaining; supplementary)
```
("cited by" OR references) from included seed records; no standalone keyword query.
```

## Date ranges and limits
- Search execution window: 2026-02-10 through 2026-02-14 (UTC).
- Publication date coverage: 2014-01-01 through 2026-02-14.
- Language limit: English only.
- Document types included for screening: standards, guidance documents, technical reports, peer-reviewed papers, and high-signal preprints.

## Inclusion criteria
A record was included when all of the following held:
1. Direct relevance to AI assurance, governance evidence, or evaluation-gaming/monitorability methods.
2. Contains extractable artifact-level or method-level evidence.
3. Provides sufficient bibliographic metadata for stable ID mapping.
4. Survives deduplication against existing atlas entries.

## Exclusion criteria and reason codes
- `RC01_OUT_OF_SCOPE`: Not about AI assurance/governance/monitorability.
- `RC02_NOT_AI_SPECIFIC`: General software or governance content without AI specificity.
- `RC03_NO_ASSURANCE_METHOD`: No concrete evaluable assurance method/artifact.
- `RC04_DOMAIN_MISMATCH`: Safety domain not transferable to AI model assurance context.
- `RC05_WRONG_OUTCOME`: Focuses on outcomes outside atlas scope (e.g., UX only).
- `RC06_INSUFFICIENT_REPORTING`: Insufficient methodological details for extraction.
- `RC07_SECONDARY_COMMENTARY`: Commentary/review without primary artifact evidence.
- `RC08_DUPLICATE`: Duplicate of an already included record.

## Screening and extraction workflow
1. Run database queries (Q-GOV-01, Q-TECH-01) within stated date/language limits.
2. De-duplicate by title/DOI/arXiv ID and normalized citation strings.
3. Title/abstract screening.
4. Full-text screening.
5. Link included records to stable IDs: `S2-T3-*` (governance artifacts) or `paper_id` (technical bibliography).
6. Record all include/exclude outcomes in `data/study_selection_log_v1.0.0.csv`.

## Bias scoring
Bias is scored on a 0-3 ordinal scale (0 low risk, 3 high risk), then normalized to a 0-1 risk index.
- Governance axes: self-attestation bias, incentive alignment bias, regulatory-capture risk, publication bias.
- Technical axes: benchmark overfitting bias, evaluation leakage bias, distribution shift bias, obfuscation risk.

Formula:
`bias_risk_score = mean(non-empty bias axis scores) / 3`

Export: `data/bias_assessment_v0.1.csv`

## Reliability scoring
Reliability scoring uses inter-rater reliability (Cohen's kappa) from dual annotation.
- Governance reliability is the mean kappa of: `artifact_type`, `assurance_function`, `verification_strength`.
- Technical reliability is the mean kappa of: `threat_model`, `gaming_resistance`.

Formula:
`reliability_score = mean(relevant kappas)`

Exports:
- Raw IRR summary: `data/irr_summary_v0.1.json`
- Record-level reliability assignment: `data/reliability_scoring_v0.1.csv`

## Sensitivity analysis
Sensitivity analysis evaluates robustness under predefined filtering scenarios.
Scenarios:
- Exclude self-attested governance artifacts.
- Independently-verifiable-only governance subset.
- Exclude evaluation-awareness-tagged technical records.
- DOI-only technical subset (replication proxy).

Export: `data/sensitivity_analysis_v0.1.csv`

## Quantified evidence strength
Evidence strength is computed per record from quality, reliability, and bias.

Inputs:
- `eqs_score` from Evidence Quality Score export (`data/evidence_quality_scores_v0.1.csv`)
- `bias_risk_score` from bias scoring
- `reliability_score` from reliability scoring

Formula:
`evidence_strength_index = clamp(0,1, 0.60*(eqs_score/3) + 0.25*reliability_score - 0.15*bias_risk_score)`

Tier mapping:
- `strong`: index >= 0.70
- `moderate`: 0.50 <= index < 0.70
- `preliminary`: index < 0.50

Export: `data/evidence_strength_quantification_v0.1.csv`

## Protocol lock (drift control)
This methodology is frozen as **Protocol v1.1.0**. Any future atlas release must:
- Preserve this file and produce a new protocol lock manifest for that release.
- Explicitly document any query, source, criterion, or scoring-formula change as drift in release notes.
- Keep reason-code semantics stable or provide a migration table.
