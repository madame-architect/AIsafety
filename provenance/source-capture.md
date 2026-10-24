# Source capture for documentary observations

Evidence schema `cyber-commitment-evidence-v2` applies to every new source
observation. `source_url` remains a compatibility alias of `original_url`.
Citation metadata in `records.yaml` does not override observation provenance.

| Field | Meaning and validation |
| --- | --- |
| `original_url` | Issuer/source location, separate from the archival location |
| `retrieved_at` | Actual byte retrieval time as a full UTC timestamp |
| `archive_url` | Capture-specific preserved representation; a live source URL is insufficient |
| `archive_checked_on` | Actual date the preserved representation was retrieved and inspected |
| `sha256` | Lowercase SHA-256 of the retained representation's exact bytes |
| `byte_length` | Positive integer length of those same bytes |
| `mime_type` | `application/pdf`, `text/html`, or `application/xhtml+xml` |
| `published_on` | Source-attributed date at its known precision; null if unknown |
| `version_claim` | Source-attributed edition/version label; null if unknown |
| `locator_basis` | How page/section/paragraph locators map to the captured representation |

New observations use `preservation_status: captured`. Every listed field must
exist. A missing archive URL and check date must both be null, with an explicit
`archive_unavailable_reason` describing the legal or technical obstacle.
Unarchived observations are identified in release manifests and do not support
a claim that the corpus is ready for longitudinal use.

The two original 2026-10-17 snapshots use `legacy_uncaptured`. Unavailable
capture fields are null; original inspection dates and limitations remain
intact. The validator permits only those exact migrated records, using
canonical fingerprints in `scripts/source_provenance.py`. These fingerprints
identify our YAML annotations, **not source-document bytes**. Corrections need
an explicit migration and reviewed fingerprint update. A new retrieval or
reinspection needs a new snapshot ID and actual date; it cannot establish
which bytes were inspected earlier.

## Capture procedure

1. Check archival and redistribution permissions. Use lawful archives and
   respect access controls and archive restrictions.
2. For PDFs, retain and hash the exact response bytes before extraction,
   optimization, OCR or rewriting. An archive PDF must match those bytes
   exactly to share the digest.
3. For mutable HTML, preserve a capture-specific archive where feasible. Hash
   the actual saved representation, including any archive rewriting. Check
   completeness and record its relationship to the original. A current URL,
   extracted text, or archive search page is insufficient. When remote
   archiving is unavailable, retain a local HTML representation and explain
   the limitation.
4. Read the retained representation. Check the edition, publication date and
   passage locators. Record whether PDF pages count the cover or how HTML
   headings/paragraphs identify a passage. Successful retrieval and a hash do
   not authenticate a publisher's claim or an archive's historical capture date.
5. Add the reviewed record to `evidence.yaml`, link its policy observation,
   then regenerate/check the history. When a local `capture_path` exists,
   the build checks length, SHA-256 and basic content signatures.

`scripts/capture_source.py` saves content-addressed bytes under ignored
`.source-captures/` and prints a YAML draft. It does not create a remote
archive or certify content. Supply an existing capture-specific archive URL,
or explain why archiving is unavailable. For HTML, the saved/hash target is
the archive response when supplied. For PDFs, source and archive must match.

```bash
python3 scripts/capture_source.py \
  --original-url https://issuer.example/policy.pdf \
  --archive-url https://archive.example/capture-id/policy.pdf \
  --id issuer_policy_observed_YYYY_MM_DD --record-id existing_citation_id \
  --published-on YYYY-MM-DD --version-claim 'Issuer version label' \
  --locator-basis 'One-based PDF viewer pages, cover included' \
  --inspection-scope 'Reviewed sections and relevant dependencies' \
  --preservation-note 'Exact issuer PDF bytes; archive compared byte for byte'
```

Replace the placeholder URLs, IDs and dates with actual inspected values. For
an unavailable archive, replace `--archive-url` with
`--archive-unavailable-reason 'Actual legal or technical reason'`.
The draft's `observed_on` defaults to retrieval day; use the actual inspection
date if later. Keep the retrieval timestamp unchanged.

Preserve local captures in durable storage outside Git when redistribution is
inappropriate. Large copyrighted PDFs need not enter Git: retain checked stable
archive references, exact cryptographic provenance and material limitations.
A digest alone does not preserve access. Builds validate structure and any
locally present bytes; they do not recheck remote archives.
