# Collection stabilization — 2026-10-16

This release reconciles the saved collection with GitHub and makes `records.yaml` authoritative. It generates the complete BibLaTeX bibliography and three reading views. It adds no newly discovered references, selects no research question, and performs no new literature search or synthesis.

## Reconciled baseline

| Item | Result |
|---|---:|
| Records in the previous GitHub bibliography | 218 |
| Records in the recovered May V2 bibliography | 276 |
| Existing GitHub citation keys retained | 218 |
| Additional keys already present in the recovered input | 58 |
| Existing GitHub citation keys removed | 0 |

The GitHub baseline is commit [`a91b597cac08e651957314e5c37cb25895ddd666`](https://github.com/madame-architect/AIsafety/commit/a91b597cac08e651957314e5c37cb25895ddd666). The earlier reported count of **262** does not match the recovered bibliography. Two parsers and a separate entry-header count agree on **276**. The file contents govern this migration; the discrepancy is documented without inventing an explanation for when the earlier report became stale.

All 218 shared records have metadata or keyword changes between the old GitHub copy and the recovered V2 input. Some also have bibliographic changes, including titles, dates, and URLs. Seven records change entry type and contain field removals; those differences are recorded explicitly in the reconciliation report. These are recovered changes, not new source verification performed during this release. The additional 58 keys likewise belong to the recovered input; they are not 58 new discoveries made for this restart.

[`provenance/reconciliation.json`](provenance/reconciliation.json) lists the added keys, field additions and removals, and before/after values for changed fields. Large keyword strings are represented by change flags; the complete original strings remain in the old Git commit and the frozen V2 file. The report also records the import checks and hashes at this migration revision. It is a historical snapshot, not a live report of later collection edits.

## Inputs and preservation

The recovered bibliography, schema, linter, taxonomy, and BibLaTeX data model are retained unchanged in [`provenance/may-2026/`](provenance/may-2026/). [`provenance/source-manifest.json`](provenance/source-manifest.json) records their original filenames, sizes, and SHA-256 hashes. The recovery date is not a new publication, source-access, or screening date.

The conversion from recovered V2 to the current YAML makes these deliberate changes:

- Removes the outer BibTeX field wrapper when storing a string in YAML. Internal TeX braces, corporate-author grouping, escapes, and multiline contents remain intact.
- Stores the five schema-controlled multivalue fields as ordered string lists: `governance_function`, `risk_domain`, `threat_vector`, `lifecycle_stage`, and `release_model`.
- Derives `keywords` from the schema's current and retained-legacy mirror fields. Manual keyword copies are omitted from YAML.
- Adds `synthesis_stream` and its explanatory `stream_note` to each record. The stream is also included in generated keyword mirrors.
- Sorts exported citation keys and field names to make regeneration deterministic.

No inherited citation key, entry type, or substantive field value was silently dropped or revised during this conversion. The existing `supersedes` and `superseded_by` fields remain literal strings rather than acquiring a new YAML list convention.

## Provisional research routing

| Primary route | Records at migration | Export |
|---|---:|---|
| Technical evaluations and methods | 153 | [technical-evals.bib](views/technical-evals.bib) |
| Governance artifacts | 91 | [governance-artifacts.bib](views/governance-artifacts.bib) |
| Contextual sources | 32 | [contextual.bib](views/contextual.bib) |
| **Total** | **276** | [Complete bibliography](frontier-governance-evals.bib) |

Each record appears in exactly one primary view. The complete bibliography resolves any references between records in different views. The live counts are generated in [`views/index.md`](views/index.md).

Every new `stream_note` begins **“Provisional:”**. Routing uses inherited metadata, titles, and available abstracts, with AI assistance. It does not establish renewed full-source inspection or independent human coding. A source can support more than one discussion while retaining one citation identity. A method proposal, technical survey, and empirical benchmark must still be distinguished within the technical stream.

The inherited `classification_confidence` counts remain **158 high, 51 medium, and 67 low**. These annotations concern the earlier classifications. They are not confidence ratings for the new stream assignments and are not evidence-quality scores.

### Boundaries to review before substantive synthesis

| Records or group | Unresolved distinction |
|---|---|
| `aisi_frontiertrends_2025` | Currently contextual: the report-page metadata does not establish whether the underlying report presents original model evaluations. |
| `rao_challengesmonitoring_2026` | Currently technical: supplied metadata describes a synthesis of monitoring challenges; its methodological contribution needs inspection. |
| FMF capability-assessment, monitorability, measurement, and nuclear-security guidance | Currently governance artifacts: determine whether particular documents also make a technical-method contribution. |
| FMF evaluation/mitigation taxonomies and conceptual monitorability papers | Currently technical: proposed taxonomies and conceptual arguments do not establish empirical results. |
| Auditing frameworks, model cards, and datasheets | Operational frameworks introduced through scholarship can belong to governance; publication format alone does not determine the route. |
| Provider-transparency research and incident-catalog methodology | Distinguish analytical papers from live dashboards, registries, or operational mechanisms. |

These are priorities for source inspection when preparing a synthesis. They do not justify deleting records, manufacturing certainty, or changing inherited annotations without evidence.

## Verification performed

The migration checks compare the frozen V2 input with the generated complete bibliography, accounting only for the deliberate transformations above.

| Check | Result |
|---|---|
| Citation keys and entry types | All 276 preserved |
| Inherited scalar field values | 8,081 identical after removing one outer BibTeX wrapper |
| Controlled multivalue field occurrences | 773 preserve the same values and order |
| Existing keyword tokens | All 6,509 retained; new stream mirrors added |
| View coverage | Exact partition of all 276 records, with matching record contents |
| Frozen input hashes | All five match the recovered files |
| Full build and generated-output check | Passed |
| Regression suite | All five tests passed, including 25 corruption cases |
| Semantic linter and advisory checks | 0 failures, 0 warnings at migration |

Reproduce the current build checks from the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/build.py --check
python3 scripts/lint_bibliography.py
python3 -m unittest discover -s tests -v
```

Advisory warnings involving source-access dates can change as time passes. Structural validation and exact export preservation do not establish the accuracy of source metadata or research claims.

The custom BibLaTeX data model retains the recovered V2 definitions and adds the two routing fields. **Biber was unavailable in the stabilization environment**, so this release does not claim a fresh Biber validation or a complete LaTeX typesetting check.

## Remaining historical limits and next work

The earlier May Methods document was not recovered. [`METHODS.md`](METHODS.md) is explicitly dated and reconstructed from available project evidence; it does not claim to reproduce the original or establish a prospective protocol for earlier collection. No complete historical search log, excluded-candidate log, inspection record, or independent coding record was recovered.

[`intake.csv`](intake.csv) begins with headers only. Future discoveries and later inspections can be recorded with their actual dates. No retrospective screening events were created. The retired project atlas, experimental pilot, and scoring machinery are not restored by this release; the unrelated external MITRE ATLAS source remains a normal bibliographic record.

The next decisions are to review this migration, resolve source-level ambiguities relevant to the intended synthesis, and then select the research question. A matching OSF deposit still needs to be verified against the exact reviewed Git revision. Creating the GitHub pull request and its archive does not itself synchronize OSF.
