# Frontier AI Governance Evals

A curated, AI-assisted collection of sources about frontier AI evaluation and governance. The collection records source roles, evidence provenance, risk areas, lifecycle stages, and other research annotations.

**Edit `records.yaml`.** BibTeX and the stream views are generated from it. The YAML schema defines permitted fields and classifications; it does not contain the source records.

This stabilization uses the recovered 276-record bibliography. All 218 citation keys previously on `main` are retained. See [MIGRATION.md](MIGRATION.md) for the reconciliation, the correction to the earlier reported count of 262, and verification results.

## Start here

| File or directory | Purpose |
|---|---|
| [records.yaml](records.yaml) | Authoritative editable source records |
| [views/index.md](views/index.md) | Generated index of technical, governance, and contextual sources |
| [frontier-governance-evals.bib](frontier-governance-evals.bib) | Generated complete BibLaTeX bibliography |
| [frontier-governance-evals-schema.yml](frontier-governance-evals-schema.yml) | Schema version, supported entry types, controlled values, and keyword policy |
| [frontier-governance-evals-taxonomy.md](frontier-governance-evals-taxonomy.md) | Definitions and interpretation guidance |
| [METHODS.md](METHODS.md) | Reconstructed collection history, stabilization methods, and prospective intake rules |
| [MIGRATION.md](MIGRATION.md) | Baseline reconciliation and current limitations |
| [provenance/](provenance/) | Frozen input files, checksums, and the record-change report |
| [intake.csv](intake.csv) | Actual discoveries and dated review decisions, including later checks of legacy records |
| [Cyber source verification](research/cyber-deployment/source-verification.md) | Five-source claim, classification, and version check for the next research output |
| [Stabilization release](releases/stabilization-2026-10-16.md) | Exact merged release identity and OSF synchronization status |
| [evals-datamodel.dbx](evals-datamodel.dbx) | Custom BibLaTeX data model for the exported fields |

## Build and verify

Use Python 3.10 or later. From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/build.py --check
python3 -m unittest discover -s tests -v
```

The build validates the YAML records, regenerates keyword mirrors, and writes the complete bibliography and disjoint stream exports. `--check` verifies the same outputs without changing files and fails if an export is missing or stale. Validation checks metadata consistency and export integrity; source findings still require scholarly assessment.

## Research streams

- **Technical evaluations:** evaluations, benchmarks, datasets, and technical methods relevant to assessing systems or safeguards. This category includes proposed methods; membership does not imply an empirical result.
- **Governance artifacts:** actual frameworks, requirements, standards, guidance, commitments, organizational disclosures, and governance portals. Their existence does not establish implementation or effectiveness.
- **Contextual sources:** policy analysis, commentary, and supporting research that belongs in neither primary synthesis stream.

Each record has one primary `synthesis_stream` and a `stream_note`. A mixed-purpose source can inform multiple discussions while retaining one citation identity. Routing began as provisional and AI-assisted, based on inherited metadata, titles, and available abstracts. Five starting sources for the cyber/deployment study received an AI-assisted full-text and version check on 2026-10-16; their dated `stream_note` fields and the [verification report](research/cyber-deployment/source-verification.md) identify that scope. The other 271 records retain their earlier inspection status. Existing `classification_confidence` values were preserved and do not grade the new routing or the quality of the evidence.

## Updating the collection

1. Log a candidate in `intake.csv` with its real discovery date and inspection basis.
2. Check identifiers and versions against the existing collection before accepting it.
3. Edit `records.yaml`; use string lists for the schema's multivalue fields and strings for other fields. Preserve internal BibTeX/TeX braces and commands. Do not add a `keywords` field; it is derived.
4. Record the decision and uncertainty, then regenerate and check the exports.

The stabilization log began empty because that release added no newly discovered sources. It now records five later reviews on their actual review date, with legacy discovery dates left blank. The 58 keys absent from the old GitHub version were already in the recovered bibliography; no original screening events have been reconstructed.

## Releases and citation

GitHub is the working project. The associated [OSF project](https://osf.io/9ks5m/) is intended for matching versioned research deposits. A GitHub update does not automatically update OSF. The project page returned a scheduled-maintenance notice on 2026-10-16, preventing comparison or upload. The [release note and manifest](releases/stabilization-2026-10-16.md) identify the exact merged stabilization package prepared for deposit; synchronization remains unconfirmed.

For a matching deposit, use the ZIP archive of the exact reviewed Git commit and record that commit in the OSF version description. Retain the `provenance/` directory so the import can be inspected. To reference this collection, include its title, maintainer (Cassandra Ansara), revision date, and the exact commit or deposited version. Cite original publications directly for their findings.

Collection stabilization was merged in [PR #13](https://github.com/madame-architect/AIsafety/pull/13). The next research focus is how cyber capability evidence informs deployment safeguards. The targeted five-source check corrects classifications and records version qualifications; it adds no bibliography records and does not reproduce experiments. See [METHODS.md](METHODS.md) for AI assistance and inspection limits.

## License

The repository includes an [MIT license](LICENSE). Rights in quoted abstracts and other third-party source material remain with their respective rights holders.
