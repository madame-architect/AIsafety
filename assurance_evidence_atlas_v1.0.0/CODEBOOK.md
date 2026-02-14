# Evidence Atlas Codebook (v1.0.0)

**Package:** assurance_evidence_atlas_v1.0.0  
**Atlas version stamp:** `v1.0.0-2026-02-14`  
**Generated from authoritative drafts:**  
- `deep-research-report (2).md` (Scope Two Tier Three governance inventory; used as source of record for IDs `S2-T3-01`…`S2-T3-100`)  
- `deep-research-report.md` (technical annotated bibliography; used for evaluation gaming / monitorability survey subset)

This codebook defines the **machine-readable schema** and the **tagging rules** used in the accompanying CSV/JSONL downloads.

---

## 1) Governance Atlas (`s2_t3_governance_atlas_*`)

### 1.1 Row identity and provenance

- `id`  
  - **Type:** string  
  - **Format:** `S2-T3-XX` (two or three digit index)  
  - **Meaning:** Stable identifier for Scope Two / Tier Three governance artifact.

- `n`  
  - **Type:** integer  
  - **Meaning:** Human order index from the Tier Three inventory (1–100).

- `raw_description`  
  - **Type:** string  
  - **Meaning:** The original short description of the artifact from the Tier Three inventory (minimally cleaned of citation markers).

- `source_file`, `source_line`  
  - **Meaning:** File name and line number where the record appears in the authoritative draft (traceability hook).

### 1.2 Required evidence tags (requested)

#### (a) `artifact_type` — **one of:** `standard` | `profile` | `law` | `report`

Decision rule (primary):
- **`law`** if the artifact is a legal or regulatory instrument (e.g., Federal Register rulemaking notice; executive order / presidential action).
- **`standard`** if the artifact is a standards-track document or testing/verification standard outline (e.g., TEVV outline, documentation outline).
- **`profile`** if the artifact is an explicit profile (e.g., AI RMF Profile).
- **`report`** otherwise (including portals, dashboards, whitepapers, blog posts, press releases, media coverage).

#### (b) `assurance_function` — **one of:** `requirements` | `evidence` | `audit`

Interpretation:
- **`requirements`**: Sets expectations, obligations, thresholds, or controls (what must/should be done).
- **`evidence`**: Provides information that could support assurance claims (what happened / what exists).
- **`audit`**: Defines or reports assessment procedures, evaluation protocols, or audit-style testing regimes.

Decision rule (primary):
- Choose **`audit`** when the artifact is explicitly about evaluation/TEVV/pre-deployment testing protocols or taxonomy of evaluations.
- Else choose **`requirements`** when the artifact specifies rules, thresholds, policies, or frameworks intended to govern behavior.
- Else choose **`evidence`**.

#### (c) `domain` — list drawn from: `GPAI`, `incidents`, `compute`, `evaluations`

Decision rule:
- Tag `incidents` if the artifact concerns incident reporting, hazards, or incident trends.
- Tag `compute` if the artifact concerns compute thresholds, diffusion/export controls, clusters, chips.
- Tag `evaluations` if it concerns evaluation/testing/assessments/TEVV/system cards/risk assessment.
- Tag `GPAI` as the default governance domain; also include it when an artifact is a general frontier/GPAI governance framework even if it also touches evaluations/compute/incidents.

#### (d) `verification_strength` — **one of:** `self_attested` | `independently_verifiable`

Operational definition for this atlas:
- **`self_attested`** if the artifact is authored by the actor/coalition whose safety practices it describes (developer or industry coalition), or is primarily a self-asserted safety framework.
- **`independently_verifiable`** if the artifact is authored by governments, standards bodies, intergovernmental organizations, independent research orgs, or independent media.

> Note: this is a *publisher/assurance posture* tag, not a guarantee of correctness. Use `verification_basis` and `evidence_dependency` to refine interpretation.

### 1.3 Additional fields (supporting rigor)

- `issuer`  
  - Standardized issuer label (heuristic + manual normalization).

- `artifact_subtype`  
  - More specific type (e.g., `portal_page`, `policy_memo`, `system_card`, `framework_policy`, `news_article`).  
  - Not required by the requested tags, but useful for filtering.

- `verification_basis`  
  - Enum: `issuer_self_or_industry` | `official_or_intergov` | `research_org` | `journalism`  
  - Explains the basis for `verification_strength`.

- `evidence_dependency`  
  - Indicates what the artifact *primarily depends on* as evidence:  
    - `self_report`, `self_report_or_registry`, `primary_source_or_official_report`, `third_party_analysis`, `journalistic_reporting`, etc.

- `bindingness`  
  - Enum: `binding` | `voluntary` | `draft`  
  - Heuristic tag indicating whether the artifact is legally binding, voluntary guidance/framework, or an explicit draft.

- `canonical_group_id`, `is_canonical`, `is_secondary_pointer`, `dedupe_key`  
  - **Purpose:** allow de-duplication while preserving traceability to the original 100-item inventory.  
  - `canonical_group_id` identifies the canonical item for a group (e.g., PDF vs landing page).  
  - `s2_t3_governance_dedupe_groups_*` lists the canonical groups with >1 member.

- `tag_confidence`  
  - 0–1 heuristic confidence score for automated tagging.  
  - Low confidence indicates likely need for manual review (e.g., issuer uncertain).

---

## 2) Technical Bibliography (`technical_eval_gaming_monitorability_bibliography_*`)

This dataset is a structured export of **entries** from the technical draft’s annotated bibliography categories:
- Scalable oversight / monitoring / evaluation gaming
- Robustness / red-teaming / jailbreaks / security
- Scaling risks / deception dynamics / emergent failures

### Fields (core)

- `paper_id`: `T-EGM-001`…  
- `title`, `year`, `arxiv_id`, `doi` (when present in the draft)  
- `annotation`, `significance`, `gaps` (as written in the draft; cleaned of citation markers)

### Tags

- `topic_primary`: `evaluation_gaming` | `monitorability`
- `method_type`: `benchmark_or_suite` | `probing_or_steering` | `defense` | `attack` | `evaluation_protocol` | `survey` | `empirical_study`
- `threat_model_tags`: lightweight keyword-derived tags (e.g., `evaluation_awareness`, `sabotage`, `scheming`, `backdoor`, `jailbreak`).

---

## 3) Safety-Case Evidence Atlas (`safety_case_evidence_atlas_*`)

This table is a **first safety-case crosswalk**:  
**governance claim → required evidence → candidate technical methods → known failure modes → coverage gaps**

It is intended as a *publishable scaffold*: scientists can contribute by (i) tightening the claims, (ii) adding counterexamples, and (iii) providing stronger technical evidence for each row.

---

## 4) Versioning and reproducibility

- The package uses a semantic version (`v1.0.0`) plus an **atlas version stamp** (`v1.0.0-2026-02-14`) tied to the conversation date.
- To extend:
  1. Add new artifacts/papers as new rows with new IDs (do not renumber existing IDs).
  2. Update schemas only when necessary; bump schema versions accordingly.
  3. Record changes in `CHANGELOG.md`.

