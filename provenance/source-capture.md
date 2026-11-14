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
   optimization, OCR or rewriting. An archive PDF can be captured independently
   when the original is unavailable. Its digest identifies the archived bytes;
   it does not prove identity with an earlier inspection or the original.
   If comparing a live original, require an exact byte match before claiming
   that the two representations share a digest.
3. For mutable HTML, preserve a capture-specific archive where feasible. Hash
   the actual saved representation, and state whether it is raw archive HTML
   or a rewritten replay. Check
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
or explain why archiving is unavailable. When an archive URL is supplied, the
command retrieves and hashes that representation directly, for both PDFs and
HTML, without contacting the original URL. It preserves `original_url` as the
source identity and emits `capture_basis` explaining which bytes were retained
and whether the original was compared. The history displays that explanation.
`retrieved_at` is the actual archive retrieval time, not its historical capture
date. Inspect the archive's edition and completeness separately.

```bash
python3 scripts/capture_source.py \
  --original-url https://issuer.example/policy.pdf \
  --archive-url https://archive.example/capture-id/policy.pdf \
  --id issuer_policy_observed_YYYY_MM_DD --record-id existing_citation_id \
  --published-on YYYY-MM-DD --version-claim 'Issuer version label' \
  --locator-basis 'One-based PDF viewer pages, cover included' \
  --inspection-scope 'Reviewed sections and relevant dependencies' \
  --preservation-note 'Archived PDF inspected; historical byte identity unverified'
```

Replace the placeholder URLs, IDs and dates with actual inspected values. For
an unavailable archive, replace `--archive-url` with
`--archive-unavailable-reason 'Actual legal or technical reason'`.
The draft's `observed_on` defaults to retrieval day; use the actual inspection
date if later. Keep the retrieval timestamp unchanged.
When a live original is available and byte-equivalence is needed, add
`--compare-original`. This optional PDF check fails if the original cannot be
retrieved or differs; it is never required for archive recovery. Omit it for
HTML, whose archival representation may legitimately differ from the live page.

Preserve local captures in durable storage outside Git when redistribution is
inappropriate. Large copyrighted PDFs need not enter Git: retain checked stable
archive references, exact cryptographic provenance and material limitations.
A digest alone does not preserve access. A replay URL may return different
HTML bytes on a later request even at the same archive timestamp. A successful
fresh download never replaces a historical digest or proves historical byte
reproduction. Builds validate structure and any
locally present bytes; they do not recheck remote archives.

## Raw HTML and follow-up verification

For Wayback HTML, use `--raw-archive` to request the timestamped `id_`
representation explicitly. Without that flag the supplied replay URL is used
as written. Raw HTML is a different representation from a rewritten replay;
give it a new retrieval ID and retain the old record, dates and fingerprints.

The tool retains the received HTTP response body and the decoded HTML entity
separately when HTTP content encoding is present. SHA-256 and `byte_length` in
the YAML identify the decoded entity saved without HTML rewriting. The
immutable retrieval sidecar records the requested/final URLs, request/response
headers, content encoding, both fingerprints, and actual retrieval time. This
does not preserve TLS, HTTP chunk framing, linked assets, or browser state.

Use repeated `--expect-text` arguments for article-specific markers from the
beginning, supporting passages and end, including material qualifications,
numbers, table cells and footnotes where present. Checks run against visible
HTML text rather than script/JSON copies. These checks detect specified
omissions; they cannot certify completeness. Inspect the retained article,
tables, notes and relevant dependencies before admitting an observation.
The sidecar states when marker checks were not requested. Retrieval IDs cannot
reuse an existing source record or sidecar, even if the payload hash matches.

The [five-page follow-up](html-reproducibility/README.md) provides historical
fingerprints, new retrieval receipts, comparison scope and public verification
commands. It distinguishes recovery of retained bytes from reproducing those
historical bytes over a public network. The fresh raw captures are separate
verification events and do not backdate or replace the original observations.

## Recovering the October 24 bundle

The owner's private Library retains `cyber-research-source-captures-2026-10-24.zip` (15,924,250 bytes; SHA-256 `7d94cdb5c6349ae4b32978a35364980a2d6f6a225c8402f454ad14b186fc3509`). It contains five policy and six operational-source representations. The [retained receipt](cyber-source-capture-bundle-2026-10-24.json) records the original capture metadata. Active provenance is in the commitment `evidence.yaml` and operational `source-captures.yaml`, not silently replaced by the receipt.

Check the ZIP digest, then restore only its `.source-captures/` directory into a working checkout. Run:

```bash
python3 scripts/audit_cyber_bibliography.py --require-capture-files
```

The strict audit requires and hashes all eleven captured payloads. Ordinary CI checks provenance structure and any available payloads, explicitly reporting how many bytes were actually checked. The two `legacy_uncaptured` observations are not counted as captured. The bundle is a retained private copy, not a publicly accessible release, OSF deposit, or guarantee of archival permanence. Its original retrieval times and prior archive checks remain unchanged; local recovery is not a new network capture. No full copyrighted PDFs or HTML pages are added to Git.
