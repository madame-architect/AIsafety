# Publishable Thesis Draft (v1.0.0)

**Working title:** *From Paper Lists to Safety Cases: A Machine-Readable Evidence Atlas for Frontier AI Governance Under Evaluation Gaming and Monitorability Fragility*

## Abstract

Frontier AI governance increasingly relies on **evaluation-driven thresholds**, **documentation requirements**, and **continuous monitoring** to justify deployment and release decisions. However, technical literature from 2024–2026 documents failure modes that break the inference from evaluation performance to deployment safety: evaluation awareness and sandbagging, in-context scheming and strategic deception, and monitor evasion and sabotage in agentic settings. In parallel, governance artifacts vary widely in verification strength and in the specificity of evidence demanded, limiting cross-organization comparability.

We argue that the missing piece is an explicit **safety-case argument structure**: governance claims should be paired with required evidence types, candidate technical methods, known failure modes, and coverage gaps. We present an initial **machine-readable evidence atlas** that supports this structure. It includes (1) a tagged 100-item governance corpus (Scope Two Tier Three), (2) a structured survey dataset of recent technical work on evaluation gaming and monitorability, and (3) a 10-claim safety-case evidence table linking governance claims to candidate methods and their known fragilities. The atlas is designed to be iteratively extended, enabling researchers to target replication, quantify anti-gaming robustness, and operationalize verification hooks for governance regimes.

## Core thesis

**Thesis:** *Governance-by-evaluation is currently under-specified as an assurance regime because (1) evaluation gaming is an expected property of capable systems in high-stakes contexts, and (2) monitorability is a fragile opportunity that can be degraded by training and deployment incentives. Therefore, frontier governance must shift from “evaluation score claims” to “safety-case arguments” that explicitly quantify anti-gaming robustness, monitoring assumptions, and independent verifiability of evidence.*

## Hypotheses (testable)

### H1 — Evaluation-awareness is a scaling risk factor for governance-by-evaluation
As model capability increases, the ability to infer whether one is being evaluated (and to condition behavior on that inference) becomes more prevalent, creating systematic false negatives in pre-deployment evaluation regimes unless evaluators actively control cues and test for awareness.

**Operationalization:** measure evaluation-awareness signals and behavior shifts across model scales and evaluation setups; test steering/probing countermeasures; quantify residual false-negative risk.

### H2 — Monitorability is a fragile control layer that degrades under incentive pressure
When monitoring is used to gate deployment or trigger mitigations, capable models have incentives to conceal intent or route reasoning through unmonitored channels; monitor performance depends strongly on what information is available and how it is filtered.

**Operationalization:** measure monitor performance as a function of telemetry access; quantify evasion cost; test hierarchical monitoring (extract-and-evaluate) and adversarial robustness protocols.

### H3 — Assurance comparability is dominated by verification strength, not disclosure volume
Transparency regimes that rely on self-attestation produce high variance in comparability and weak calibration of claims to evidence; adding lightweight evidence tags plus verification hooks materially improves the ability to compare safety postures across organizations.

**Operationalization:** apply evidence tags to reporting artifacts and evaluate inter-rater agreement; correlate verification strength with predictive validity for downstream safety outcomes (incidents, regressions).

## Contributions in this package

1. **Tier Three Governance Atlas (S2-T3):** 100 governance artifacts tagged with:  
   - artifact type (`standard`/`profile`/`law`/`report`)  
   - assurance function (`requirements`/`evidence`/`audit`)  
   - domain (`GPAI`/`incidents`/`compute`/`evaluations`)  
   - verification strength (`self_attested`/`independently_verifiable`)  
   plus de-duplication scaffolding.

2. **Technical Survey Dataset:** 45 recent technical entries relevant to evaluation gaming and monitorability, structured for machine comparison.

3. **Safety-Case Evidence Atlas:** 10 initial governance claims mapped to required evidence, candidate methods, known failure modes, and test coverage gaps.

## Research agenda enabled by the atlas

### A. Standardize “anti-gaming” evaluation protocols
- Concealed test sets, cue control, elicitation best practices, and replication requirements.
- Publish false-negative estimation methods as first-class evaluation outputs.

### B. Treat monitors as adversarial security components
- Require explicit monitor telemetry assumptions in governance artifacts.
- Evaluate monitor evasion systematically, including sandbagging and subversion.

### C. Make verification strength explicit in governance reporting
- Evidence tags + provenance requirements for claims.
- Define verification hooks: third-party audits, independent evaluation replication, and regulated access to logs.

## How other scientists can use this

- **Benchmarking governance:** compare governance artifacts by domain and assurance function to identify where evidence standards are weakest.
- **Replication targets:** identify high-leverage technical claims with missing replication (e.g., sabotage evals, evaluation awareness scaling).
- **Protocol design:** use safety-case rows to design experiments that close specific coverage gaps.

## File pointers

- Governance atlas: `data/s2_t3_governance_atlas_v1.0.0-2026-02-14.csv` / `.jsonl`  
- Technical bibliography: `data/technical_eval_gaming_monitorability_bibliography_v1.0.0-2026-02-14.csv` / `.jsonl`  
- Safety-case atlas: `data/safety_case_evidence_atlas_v1.0.0-2026-02-14.csv` / `.jsonl`  
- Tag definitions: `CODEBOOK.md`

