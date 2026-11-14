# Frontier AI Governance Evals

A curated, AI-assisted research project about what frontier AI evaluations establish, how governance uses them, and where the evidence remains limited. The broad bibliography and provisional review are central; the linked cyber datasets provide a worked case study.

Start with the [provisional synthesis](research/synthesis/review.md) for findings, then use its [claim-and-evidence map](research/synthesis/claims.md) and [coverage summary](research/synthesis/coverage-summary.md) to examine their basis. The map is generated from [claims.yaml](research/synthesis/claims.yaml). This is an integration of existing research, not a completed independent rereading of the corpus or a publication endorsement. [Reconciliation and remaining decisions](research/synthesis/reconciliation.md) identify unresolved work.

**Edit `records.yaml`.** BibTeX and the stream views are generated from it. The YAML schema defines permitted fields and classifications; it does not contain the source records.

The current collection contains **286 records**: 156 technical evaluations/methods, 95 governance artifacts, and 35 contextual sources. The October 16 stabilization recovered 276 records and retained all 218 earlier GitHub citation keys; [MIGRATION.md](MIGRATION.md) documents that historical reconciliation. The [October 24 integration report](research/cyber-deployment/expansion-reconciliation-2026-10-24.md) documents the ten subsequent admissions and the linked cyber datasets.

## Start here

| Reader task | Start here |
|---|---|
| Understand findings and limitations | [Broad synthesis](research/synthesis/review.md) and [research guide](research/README.md) |
| Check a substantive claim | [Claim-and-evidence map](research/synthesis/claims.md), with source versions, locators and review limits |
| Inspect reading coverage | [Generated summary](research/synthesis/coverage-summary.md), [inherited ledger](research/synthesis/coverage.csv), and [later reading events](research/synthesis/rounds.md) |
| Find and cite a source | [Source index](views/index.md), [complete BibLaTeX export](frontier-governance-evals.bib), and authoritative [records.yaml](records.yaml) |
| Understand methods and history | [METHODS.md](METHODS.md), [migration](MIGRATION.md), and [provenance](provenance/) |
| Examine the cyber case study | [Research guide and linked datasets](research/cyber-deployment/README.md), including dated Carbon observations and pending source candidates |
| Review unresolved work and publication decisions | [Reconciliation](research/synthesis/reconciliation.md) |
| Add or correct source records | [Intake log](intake.csv), [schema](frontier-governance-evals-schema.yml), and [taxonomy](frontier-governance-evals-taxonomy.md) |
| Reproduce or deposit an exact revision | Commands below and [release protocol](releases/README.md); the [stabilization note](releases/stabilization-2026-10-16.md) remains historical |
| Inspect the published October 24 revision | [v2026.10.24 release and deposit receipt](https://github.com/madame-architect/AIsafety/releases/tag/v2026.10.24) |

## Build and verify

Use Python 3.10 or later. From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/build.py --check
python3 scripts/build_research.py --check
python3 scripts/lint_bibliography.py
python3 scripts/build_commitments.py --check
python3 research/cyber-deployment/operational-risk/build.py --check
python3 scripts/build_cyber_datasets.py --check
python3 scripts/audit_cyber_bibliography.py
python3 -m unittest discover -s tests -v
```

The bibliography build validates `records.yaml`, regenerates keyword mirrors, and writes the complete bibliography and disjoint stream exports. The research check reconciles the coverage ledger and claim references with that authority and checks generated research outputs. `--check` does not change files. These checks demonstrate consistency; source findings still require scholarly assessment.

The [cyber commitment pilot](research/cyber-deployment/README.md) uses companion
YAML linked to the bibliography. Run `python3 scripts/build_commitments.py --write`
to regenerate its Markdown history and `python3 scripts/build_commitments.py --check`
to validate the data and detect a stale history. These annotations describe
scoped policy statements; implementation and effectiveness require separate
evidence.

## Research streams

- **Technical evaluations:** evaluations, benchmarks, datasets, and technical methods relevant to assessing systems or safeguards. This category includes proposed methods; membership does not imply an empirical result.
- **Governance artifacts:** actual frameworks, requirements, standards, guidance, commitments, organizational disclosures, and governance portals. Their existence does not establish implementation or effectiveness.
- **Contextual sources:** policy analysis, commentary, and supporting research that belongs in neither primary synthesis stream.

Each record has one primary `synthesis_stream` and a `stream_note`. A mixed-purpose source can inform multiple discussions while retaining one citation identity. Routing began as provisional and AI-assisted, based on inherited metadata, titles, and available abstracts. The [coverage ledger](research/synthesis/coverage.csv) now records the supplied research's inspection labels and source-level qualifications, separately from later checking and replication. Those inherited labels have not been recertified by this integration. Earlier targeted checks retain their dated scope in [METHODS.md](METHODS.md). Existing `classification_confidence` values do not grade the routing or the quality of the evidence.

## Updating the collection

1. Log a candidate in `intake.csv` with its real discovery date and inspection basis.
2. Check identifiers and versions against the existing collection before accepting it.
3. Edit `records.yaml`; use string lists for the schema's multivalue fields and strings for other fields. Preserve internal BibTeX/TeX braces and commands. Do not add a `keywords` field; it is derived.
4. Record the decision and uncertainty, then regenerate and check the exports.

The stabilization log began empty because that release added no newly discovered sources. It now records those later reviews, the initial DeepMind observations, and the October 24 bibliography integration and scoped OpenAI reviews; unknown discovery dates remain blank. The 58 keys absent from the old GitHub version were already in the recovered bibliography; no original screening events have been reconstructed.

## Releases and citation

GitHub is the working project, with matching versioned research deposits in the associated [OSF project](https://osf.io/9ks5m/). The published [v2026.10.24 release](https://github.com/madame-architect/AIsafety/releases/tag/v2026.10.24) targets commit `1bb1672` and records a verified OSF deposit receipt for object `s5ey4`, version 1. The November 14 integration confirmed the GitHub release and its receipt text; it did not freshly re-download or verify the OSF bytes. The [October 16 stabilization note](releases/stabilization-2026-10-16.md) describes an earlier, separately unconfirmed deposit attempt. A later GitHub update does not automatically update either published package.

For the next release, follow the [release and OSF deposit protocol](releases/README.md).
It binds the exact tagged commit, authoritative YAML, generated outputs and hashes
to a deterministic release ZIP, then records the verified GitHub asset and OSF
object/version identifiers. A merge, tag or upload receipt alone does not confirm
OSF synchronization. The two initial cyber snapshots retain their disclosed
capture gaps; new observations require the [source capture fields](provenance/source-capture.md).
To reference this collection, include its title, maintainer (Cassandra Ansara),
revision date, and exact commit or deposited version. Cite original publications
directly for their findings.

Collection stabilization was merged in [PR #13](https://github.com/madame-architect/AIsafety/pull/13). The [research guide](research/README.md) connects the broad review with the cyber case study and the remaining full-corpus objective. Source admission, synthesis judgments, and publication are separate decisions; the pending Carbon package does not enlarge the admitted bibliography or its reading counts. See [METHODS.md](METHODS.md) for AI assistance and inspection limits.

## License

The repository includes an [MIT license](LICENSE). Rights in quoted abstracts and other third-party source material remain with their respective rights holders.

