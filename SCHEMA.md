# SCHEMA

## Scope and intent

This schema formalizes the *implicit* entry structure used by the consolidated **AI Safety Literature Review + Annotated Bibliography**. It is designed for a governance-to-technical evidence pipeline where each entry can be used as (or traced to) safety-case evidence.

This file is **normative** for new edits: when adding or modifying entries, follow the formatting and controlled vocab rules below.

---

## Record structure

### Entry boundary

An **annotated entry** is a Markdown block consisting of:

1) A level-4 heading:

```
#### `BIBKEY` — Title (Year)
```

2) A bullet list of fields, each on its own line:

```
- **Field name:** value
```

3) Optional sub-headings or notes immediately after the bullet list (allowed but discouraged; prefer putting content in fields).

### Key definitions

- **`BIBKEY`**: a unique identifier, usually matching the `.bib` key.
  - **Required.**
  - Must be stable over time.
  - Must not be reused for different works.

- **Title (in heading)**: human-readable title.
  - **Required.**
  - The title in the heading is treated as display text; the *authoritative metadata* lives in the fields.

- **Year (in heading)**: should match `Year` field.
  - **Required in heading**, but may be `n.d.`.
  - **Consistency rule**: the heading year and the `Year` field must match exactly.

---

## Field catalog

### Field table

| Field (as written) | Required? | Value type | Controlled? | Notes |
| --- | --- | --- | --- | --- |
| `Creators` | required | free-text string | no | Authors or organization responsible for the artifact. |
| `Venue/body` | required | free-text string | no | Publishing venue or responsible body (e.g., arXiv, EU (EUR-Lex), NIST, company name). |
| `Year` | required | `YYYY` \| `n.d.` | partially | Use `n.d.` when no publication year is available. |
| `Type` | required | token | **yes** | See controlled vocab. |
| `Evidence strength` | required | token + maturity | **yes** | Format: `<strength> (maturity: <A|B|C|D>)`. |
| `ID / locator(s)` | required | locator list | partially | Prefer prefixed locators; see locator rules. |
| `Access` | required | token | **yes** | open / controlled-restricted / unknown. |
| `Annotation` | required* | free-text paragraph | no | *Required unless this entry is an alias* via `Relation: same_work_as`. |
| `Safety relevance` | optional | free-text paragraph | no | Why this matters for assurance/governance. |
| `Limitations / open questions` | optional | free-text paragraph | no | Key caveats / failure modes / missing validation. |
| `Risk domain` | required | tag list | **yes** | Multi-select; controlled tokens; see tags. |
| `Lifecycle stage` | required | tag list | **yes** | Multi-select; controlled tokens; see tags. |
| `Assurance function` | required | tag list | **yes** | Multi-select; controlled tokens; see tags. |
| `Threat model` | required | tag list | **yes** | Multi-select; controlled tokens; see tags. |
| `Method area` | optional (recommended) | tag list | **yes** | Lightweight topical index; multi-select. |
| `Where/what` | optional | free-text string | no | Pointer to a specific section/page/figure; helpful for long reports. |
| `Version history` | optional | key list | partially | List of related keys; see versioning rules. |
| `Relation` | optional | relation statement | partially | Currently supports `same_work_as: `…; see versioning rules. |
| `Provenance` | required | free-text string | no | Internal ingestion notes (source lists, pipeline stage, etc.). |

---

## Controlled vocabularies

### Type

**Canonical allowed values**

- `paper`
- `benchmark/evaluation suite`
- `dataset`
- `standard/guidance`
- `regulation`
- `corporate policy/framework`
- `policy report/guidance`
- `industry report/guidance`
- `press coverage`

**Deprecated / legacy values (allowed for backward compatibility, prefer canonical)**

- `industry report` → use `industry report/guidance` (difference is not operationally meaningful for the pipeline).
- `blog/commentary` → use `press coverage` (one-off value; treat as non-peer-reviewed commentary).

### Evidence strength

**Allowed values (strength component)**

- `binding_regulation`
- `operational_standard`
- `benchmark_infra`
- `empirical_scaled`
- `empirical_small`
- `conceptual`

**Required formatting**

```
<EVIDENCE_STRENGTH> (maturity: <A|B|C|D>)
```

Example:

- `empirical_small (maturity: B)`
- `operational_standard (maturity: C)`

### Evidence maturity

**Allowed values**

- `A` — highest maturity: peer-reviewed or widely replicated; or benchmarks/tools with broad adoption and stable reuse.
- `B` — moderate maturity: preprints, early tool releases, or limited replication; strong but not yet “settled.”
- `C` — governance/standards/reporting artifacts; implementable but not *empirical proof*; may also apply to conceptual syntheses.
- `D` — lowest maturity: journalistic coverage, speculative commentary, or highly non-validated analysis.

**Rule:** maturity is **not** a claim of truth. It is a *rough signal* about external validation and reproducibility.

### Access

- `open` — accessible without special permission (public URL, public PDF, arXiv, etc.).
- `controlled-restricted` — requires special access (NDAs, private evaluation access, internal-only docs).
- `unknown` — access status not yet determined.

### Risk domain

Multi-select tags describing which risk area(s) are directly addressed.

Allowed tokens:

- `cyber`
- `bio`
- `CBRN`
- `persuasion`
- `autonomy`
- `open-weights`
- `privacy`

### Lifecycle stage

Multi-select tags describing which part of the system lifecycle the artifact primarily concerns.

Allowed tokens:

- `pretraining`
- `post-training`
- `deployment`
- `post-deployment`

### Assurance function

Multi-select tags describing which assurance function(s) the artifact supports.

Allowed tokens:

- `eval`
- `mitigation`
- `monitoring`
- `auditing`
- `reporting`

### Threat model

Multi-select tags describing the attacker/abuse model assumed by the work (explicitly or implicitly).

Allowed tokens:

- `non-expert uplift`
- `expert uplift`
- `insider`
- `supply chain`
- `adaptive attacker`

### Method area

Optional multi-select topical index.

Allowed tokens:

- `governance`
- `evaluation/benchmarks`
- `monitoring`
- `security`
- `interpretability`
- `post-training/alignment`
- `compute governance`

---

## Formatting and normalization rules

### Multi-select list encoding

For `Risk domain`, `Lifecycle stage`, `Assurance function`, `Threat model`, and `Method area`:

- Use **semicolon + space** as the delimiter: `value1; value2; value3`.
- Do not include duplicates.
- Prefer ordering tokens in the order shown in the “Controlled vocabularies” section (for consistency).

### Unknown / missing values

This schema supports three explicit “non-values”:

- `unknown` — use when a value *should exist* but is not known yet.
  - Allowed in: `Access` and all controlled tag fields.
- `TBD` — use when a value is missing but expected to be found via follow-up QA.
  - Allowed in: `ID / locator(s)` (preferred), and optionally `Where/what`.
  - Do **not** use `TBD` for tag fields; use `unknown`.
- `not_applicable` — use when a field is structurally irrelevant for the artifact.
  - Allowed in: controlled tag fields **only** when you can justify irrelevance.
  - Example: `Threat model: not_applicable` for a purely descriptive taxonomy with no attacker assumptions.
  - Non-example: leaving `Threat model` unset for an eval-gaming paper; that is `unknown` or a specific attacker model.

**Legacy placeholder**

- `—` (em dash) appears in the existing document as a placeholder. Treat it as **legacy-equivalent to `unknown`**.
- For new edits, do **not** introduce `—`; use `unknown`.

### Locator list rules (`ID / locator(s)`)

**Goal:** make the artifact retrievable and uniquely identifiable.

- Encode each locator as `PREFIX: value`.
- Separate multiple locators with `; `.
- Preferred prefix order when present:
  1. `DOI`
  2. `arXiv`
  3. `CELEX`
  4. `URL`
  5. `PDF`

**Allowed locator prefixes (current corpus)**

- `DOI`
- `arXiv`
- `CELEX`
- `URL`
- `PDF`

**Rules**

- Do **not** include bare links without a prefix (legacy entries sometimes do; new entries must not).
- If no stable locator is known: `ID / locator(s): TBD`.

---

## Versioning, aliasing, and duplication control

### Problem statement

Multiple `.bib` keys can refer to the *same* intellectual work (e.g., preprint vs proceedings, mirrored PDFs, renamed web pages). Without constraints, duplicates can drift: tags and annotations can diverge and corrupt downstream evidence claims.

### Canonical entry rule

For each “work family” (set of entries that refer to the same work):

- Exactly **one** entry must be designated the **canonical** entry.
- The canonical entry:
  - contains the **full analytic content** (annotation, tags, limitations, safety relevance),
  - may list other keys under `Version history`.

### `Relation: same_work_as`

**Meaning:** “This entry is a bibliographic alias or publication instance of the same underlying work as the referenced key.”

**Syntax**

```
- **Relation:** same_work_as: `CANONICAL_BIBKEY`
```

**No-divergence rule for `same_work_as` entries**

If an entry contains `Relation: same_work_as`:

- It must be treated as **non-canonical**.
- It must not introduce independent analytic content.

Two compliant patterns are allowed:

1) **Alias-stub pattern (preferred)**  
   Include only bibliographic fields plus `Relation` and `Provenance`:

   - Creators
   - Venue/body
   - Year
   - Type
   - Evidence strength
   - ID / locator(s)
   - Access
   - Where/what (optional)
   - Relation (required)
   - Provenance

   All analytic fields (Annotation; Safety relevance; Limitations; tags; Method area) should be **omitted**.

2) **Mirror pattern (allowed but discouraged)**  
   If analytic fields are included, they must match the canonical entry **exactly** (byte-for-byte) for:
   - `Annotation`
   - `Safety relevance`
   - `Limitations / open questions`
   - `Risk domain`
   - `Lifecycle stage`
   - `Assurance function`
   - `Threat model`
   - `Method area`
   - `Evidence strength` *(strength + maturity)*

### `Version history`

**Meaning:** “Other keys in this file are alternative versions or representations of this same work family.”

**Syntax**

- Single key:

  ```
  - **Version history:** `OTHER_KEY`
  ```

- Multiple keys:

  ```
  - **Version history:** `KEY1`, `KEY2`, `KEY3`
  ```

**Rules**

- `Version history` must appear **only** on the canonical entry of a work family.
- Every key listed in `Version history` must:
  - either use `Relation: same_work_as: `CANONICAL_KEY` (preferred), or
  - be migrated into that form during QA (see “Done when”).

**Allowed differences across versions**

When keys are linked via `Version history` / `same_work_as`, the following bibliographic fields may differ without being considered “divergence”:

- `Venue/body`
- `Year`
- `ID / locator(s)`
- `Access`
- `Where/what`

All analytic fields must remain centralized in the canonical entry (alias-stub pattern) or identical (mirror pattern).

---

## Examples (from the current bibliography)

> These examples are **adapted** from the current Literature_Review entries to illustrate *schema-compliant* formatting. Legacy placeholders (`—`) are rendered as `unknown`/`not_applicable`, and deprecated `Type` tokens are normalized to canonical values where needed. The bibkeys and substantive content are drawn from the bibliography.

### Example 1 — paper (DOI + arXiv)

#### `Charnock2026ExpandingExternalAccess` — Expanding External Access To Frontier AI Models For Dangerous Capability Evaluations (2026)
- **Creators:** Jacob Charnock et al
- **Venue/body:** arXiv
- **Year:** 2026
- **Type:** paper
- **Evidence strength:** empirical_small (maturity: B)
- **ID / locator(s):** DOI: 10.48550/arXiv.2601.11916; arXiv: 2601.11916
- **Access:** open
- **Annotation:** Provides an access taxonomy and “Access Levels” for external evaluators to run dangerous-capability tests securely.
- **Safety relevance:** Directly targets the bottleneck of independent evaluation under confidentiality and security constraints.
- **Limitations / open questions:** Access levels may still be insufficient for deep audits; governance of evaluator trust remains unresolved.
- **Risk domain:** unknown
- **Lifecycle stage:** deployment
- **Assurance function:** auditing; eval
- **Threat model:** unknown
- **Method area:** evaluation/benchmarks
- **Provenance:** GOV-CORE-11 (deep-research-report (1).md)

### Example 2 — regulation (CELEX)

#### `EU2024RegulationEu20241689` — Regulation (EU) 2024/1689 (AI Act) (2024)
- **Creators:** European Union
- **Venue/body:** EU (EUR-Lex)
- **Year:** 2024
- **Type:** regulation
- **Evidence strength:** binding_regulation (maturity: C)
- **ID / locator(s):** CELEX: 32024R1689; URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
- **Access:** open
- **Annotation:** Establishes a binding risk-based regulatory framework that elevates governance, transparency, and accountability requirements.
- **Safety relevance:** Creates a compliance anchor likely to incorporate frontier evaluation and documentation regimes.
- **Limitations / open questions:** Implementation detail and measurement standards remain contested; efficacy depends on enforcement and technical TEVV capacity.
- **Risk domain:** unknown
- **Lifecycle stage:** deployment
- **Assurance function:** reporting
- **Threat model:** not_applicable
- **Method area:** governance
- **Provenance:** GOV-CORE-14 (deep-research-report (1).md)

### Example 3 — standard/guidance (n.d.)

#### `NISTndOutlineDraftTevv` — Outline of Draft TEVV Standard (n.d.)
- **Creators:** NIST
- **Venue/body:** NIST
- **Year:** n.d.
- **Type:** standard/guidance
- **Evidence strength:** operational_standard (maturity: C)
- **ID / locator(s):** URL: https://www.nist.gov/artificial-intelligence
- **Access:** unknown
- **Annotation:** Establishes a standards trajectory for testing/evaluation/verification/validation; strong governance utility, but details are incomplete until full draft and sector profiles mature.
- **Risk domain:** unknown
- **Lifecycle stage:** deployment
- **Assurance function:** eval; reporting
- **Threat model:** not_applicable
- **Method area:** evaluation/benchmarks; governance
- **Provenance:** S2‑T2‑03, S2‑T3‑03 (deep-research-report (2).md)

### Example 4 — corporate policy/framework (with version history)

#### `Anthropic2024ResponsibleScalingPolicy` — Responsible Scaling Policy (RSP-2024) (2024)
- **Creators:** Anthropic
- **Venue/body:** Anthropic
- **Year:** 2024
- **Type:** corporate policy/framework
- **Evidence strength:** operational_standard (maturity: C)
- **ID / locator(s):** URL: https://www.anthropic.com/news/responsible-scaling-policy-update
- **Access:** open
- **Version history:** `Anthropic2024ResponsibleScalingPolicya`
- **Annotation:** Updates RSP with AI Safety Levels, capability thresholds, and paired deployment/security standards.
- **Safety relevance:** Provides concrete “scale only with safeguards” logic and a structured pause/hold governance mechanism.
- **Limitations / open questions:** Still relies on internal evaluation and security claims; verification and independent replication remain hard.
- **Risk domain:** unknown
- **Lifecycle stage:** pretraining; deployment
- **Assurance function:** reporting
- **Threat model:** not_applicable
- **Method area:** governance
- **Provenance:** GOV-CORE-40, S2‑T3‑42 (deep-research-report (1).md, deep-research-report (2).md)

### Example 5 — benchmark/evaluation suite

#### `Mazeika2024HarmbenchStandardizedEvaluatio` — HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal (2024)
- **Creators:** Mazeika et al.
- **Venue/body:** arXiv
- **Year:** 2024
- **Type:** benchmark/evaluation suite
- **Evidence strength:** benchmark_infra (maturity: A)
- **ID / locator(s):** DOI: 10.48550/arXiv.2402.04249; arXiv: 2402.04249
- **Access:** open
- **Version history:** `HarmBench2024HarmbenchStandardizedEvaluatio`
- **Annotation:** Standardizes automated red‑teaming evaluation, comparing many red‑teaming methods and defenses and supporting attack/defense co‑development.
- **Safety relevance:** Directly maps to governance needs for auditable, comparable robustness evidence.
- **Limitations / open questions:** Standardization can create “teaching to the test”; adversaries may pivot to uncovered harm modalities.
- **Risk domain:** unknown
- **Lifecycle stage:** deployment
- **Assurance function:** auditing; eval; mitigation; reporting
- **Threat model:** adaptive attacker
- **Method area:** evaluation/benchmarks; governance
- **Provenance:** S1‑E‑01 (deep-research-report (2).md)

### Example 6 — industry report

#### `FMF2026ChainThoughtMonitorability` — Chain of Thought Monitorability (2026)
- **Creators:** Frontier Model Forum
- **Venue/body:** Frontier Model Forum
- **Year:** 2026
- **Type:** industry report/guidance
- **Evidence strength:** conceptual (maturity: C)
- **ID / locator(s):** URL: https://frontiermodelforum.org/issue-brief-chain-of-thought-monitorability/
- **Access:** open
- **Annotation:** Discusses monitorability issues for reasoning traces and implications for evaluation and control strategies.
- **Safety relevance:** Addresses a key evaluation/oversight question: what evidence is available for auditing model reasoning.
- **Limitations / open questions:** Largely conceptual; operational monitorability standards and validated measurement remain limited.
- **Risk domain:** unknown
- **Lifecycle stage:** deployment; post-deployment
- **Assurance function:** auditing; monitoring; eval; reporting
- **Threat model:** unknown
- **Method area:** monitoring
- **Provenance:** GOV-CORE-38 (deep-research-report (1).md)

### Example 7 — dataset

#### `Wang2024Helpsteer2OpensourceDataset` — HelpSteer2: Open-source dataset for training top-performing reward models (2024)
- **Creators:** Zhilin Wang et al
- **Venue/body:** arXiv
- **Year:** 2024
- **Type:** dataset
- **Evidence strength:** benchmark_infra (maturity: B)
- **ID / locator(s):** DOI: 10.48550/arXiv.2406.08673; arXiv: 2406.08673
- **Access:** open
- **Annotation:** Releases a permissively licensed preference dataset intended to remain effective as models improve, and reports strong RewardBench performance using a reward model trained on HelpSteer2.
- **Limitations / open questions:** Dataset size is relatively small; how well it covers rare catastrophic harms and cross-cultural preferences is unclear.
- **Risk domain:** open-weights
- **Lifecycle stage:** pretraining; post-training
- **Assurance function:** mitigation; reporting
- **Threat model:** unknown
- **Method area:** post-training/alignment
- **Provenance:** TECH-008 (deep-research-report.md)

### Example 8 — alias-stub using `same_work_as` (preferred pattern)

#### `OpenAI2025PreparednessFrameworkV2` — Preparedness Framework v2 (2025)
- **Creators:** OpenAI
- **Venue/body:** OpenAI
- **Year:** 2025
- **Type:** corporate policy/framework
- **Evidence strength:** operational_standard (maturity: C)
- **ID / locator(s):** URL: https://openai.com/index/updating-our-preparedness-framework/; PDF: https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf
- **Access:** unknown
- **Relation:** same_work_as: `OpenAI2025PreparednessFrameworkVersion`
- **Provenance:** S2‑T2‑26, S2‑T3‑40 (deep-research-report (2).md)

---

## Schema migration notes (suggestions; do not apply automatically)

1) **Replace the legacy placeholder `—` with explicit `unknown`** across controlled tag fields and `Access`.  
   Benefit: enables machine validation and avoids ambiguity between “unknown” vs “not applicable.”

2) **Split “Evidence strength” into two orthogonal axes**:
   - *Normative authority* (binding regulation vs non-binding guidance vs internal policy),
   - *Empirical probative weight* (benchmark vs empirical vs conceptual).  
   Benefit: prevents policy artifacts from being mistaken for empirical validation.

3) **Introduce a first-class `work_id`** to represent the canonical work family, separate from `.bib` keys.  
   Benefit: eliminates fragile many-to-many relationships between `Version history` and `same_work_as`.

4) **Normalize `Type` to a smaller set and track source kind separately** (e.g., “blog post” vs “press coverage”).  
   Benefit: reduces one-off types while preserving provenance.

5) **Add `jurisdiction` and `scope` fields for governance instruments** (e.g., EU/US/UK; sectoral scope).  
   Benefit: supports compliance mapping and avoids burying critical context in `Venue/body`.

6) **Add `retrieved_at` + `content_hash` for web resources** (when feasible).  
   Benefit: improves auditability as URLs change.

7) **Formalize locator structure** (e.g., use a YAML list under `ID / locator(s)` instead of a semicolon string).  
   Benefit: reduces parsing errors and allows per-locator metadata (type, verified status, retrieval date).

---

## Done when

- [ ] All fields listed in “Field catalog” are documented with required/optional status, value type, and rules.
- [ ] All controlled vocabularies include explicit allowed tokens and deprecated/legacy tokens (if any).
- [ ] Unknown/missing-value rules explicitly cover `unknown`, `TBD`, and `not_applicable`, and state where each is permitted.
- [ ] Locator formatting rules define allowed prefixes and delimiter conventions.
- [ ] Versioning/aliasing rules define how `Version history` and `Relation: same_work_as` prevent analytic drift.
- [ ] 5–10 concrete examples are included and show compliant formatting.
- [ ] “Schema migration notes” propose improvements without changing the main bibliography.