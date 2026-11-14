# Carbon source candidates prepared for review

This package was prepared against PR #21 head `72bc5de00988e5349937b54f8d7b36cf9a15fe2d`. It preserves the three November 3 deferrals and adds two sources linked to the November 10 expansion. All five bibliography and research admissions remain pending. The proposal does not change `records.yaml`, either admitted dataset, their generated views, the prior corrections, or full-bibliography coverage counts. Publishing this review package does not admit its candidates or publish the retained source payloads. Release and OSF synchronization remain separate tasks.

Actual retrievals occurred on November 14 UTC, November 13 in America/New_York. Source publication, archive-attributed capture time, fresh byte retrieval and actual inspection are separate events. These captures cannot establish which bytes were read on November 3.

## Findings that change the publication

The [November 10 announcement][expansion] and its [Carbon report][carbon-report] supply a Carbon-specific threshold determination and residual-risk rationale. The report carries forward Argon's cyber CCL determination under its material-capability-change rule, supplements it with CyScenarioBench V2 results, and assesses strengthened safeguards as reducing residual cyber risk below the CCL. A present-tense assertion that no Carbon rationale is public is obsolete. The new [dated observation](../carbon-expansion-2026-11-10.md) makes the rationale's sufficiency and configuration coverage the next questions.

The [historical note](../carbon-restricted-access-2026-10-28.md) retains the November 3 evidence boundary and distinguishes announced access phases from safeguards-off benchmark scores. It now identifies the date of its absence finding and the later disclosure. Neither Argon's assessment nor an ExploitGym score supplies a Carbon threshold determination by inference. The later report supplies that determination explicitly.

## Three original candidates and what is now preserved

| Candidate | Fresh preservation and inspection | Still unresolved for the proposed use |
|---|---|---|
| October 28 announcement | Retained original HTML and independently retrieved [November 13 archive][announcement-archive]. Complete article text matches after whitespace normalization; HTML bytes differ. Title, byline, date and relevant passages checked. Chart captured separately. | Identity with the November 3 HTML remains unknown. Announcement is evidence of stated phases and testing participation, not actual first access or a pre-release test outcome. Approve a scoped contextual bibliography record. |
| October evaluation methodology | Retained both the [October 29 archive][method-archive] and the live PDF. Five pages each; cover, methodology and cyber passages inspected; archived results table visually checked. | The live PDF has changed. Choose the October archive for the historical observation while retaining the live revision separately. Publication/revision dates and byte identity with the November 3 reading remain unknown. Task denominator and matching deployed configurations require care before dataset admission. |
| October Argon report | Downloaded the 17,378,918-byte original successfully and checked an independently retrieved [October 20 archive][argon-archive]: exact byte equality. Cover and §3.2.2 opening inspected; printed p. 33 / viewer p. 34 visually checked. | This verifies a new, limited inspection. It cannot reconstruct the earlier reading event or certify all 217 pages. Approve Argon only as the scoped comparator proposed here. |

The two new candidates are the November 10 announcement and November Carbon report. Their [November 12 HTML archive][expansion-archive] and [November 10 PDF archive][carbon-archive] were retrieved and inspected. Normalized article text matches the live HTML while its bytes differ. The 94-page Carbon PDF matches the separately retrieved original byte for byte. Only the cover and specified sections were reviewed; this is not a full-report reading.

The archive timestamp is attributed to the archive. A CDX lookup alone would not establish preservation: this package retains the retrieved archive payloads and checks their actual hashes, lengths, document identities and passage locators. Originals and archives were compared separately. No archive submission was made. Full source payloads remain private under ignored `.source-captures/` and are not included in the proposed text patch.

## Argon inspection history

Three events remain distinct in [source-admission.yaml](source-admission.yaml):

1. The November 3 note records original-PDF title-page and cyber-determination inspection, a third-party transcription search and a model-card cross-check. Its original reading record and source-byte identity were not recovered.
2. The later review is described in the user's private update as unable to independently verify the original full interior through the attempted web route. That account is secondary here; the underlying chat was not reopened. A route's size limit is an access limitation, not a document finding.
3. This fresh review downloads the original and archived PDFs, verifies exact equality, and inspects only the cover and cyber determination. A machine search of the extracted original text returns zero case-insensitive Carbon matches. That is an extracted-text search, not visual inspection of every page or proof of absence in images.

The two earlier accounts can both be true. No error is established. Proposed wording: “The November 3 note records a scoped inspection of the original report's title page and cyber determination, alongside a transcription search. The later review did not independently verify the original PDF interior. Full-document verification is not claimed.” A fresh capture closes the present retrieval gap; the earlier audit trail remains unresolved.

## Methodology revision that must stay visible

| Retained representation | Bytes | SHA-256 |
|---|---:|---|
| October 29 archived PDF | 808,899 | `729c10bcdcd68998f4ba3b0e81376788886e38e473c33c700ea9bd609bca45ad` |
| Live PDF retrieved in this pass | 812,661 | `f6bb6fdc2406db5229e8d2fdf82f8844b6e9da3a5b90c58e6b72d398af81e549` |

The live revision qualifies the ExploitGym language as benchmark mitigations being off, adds a Fairwind qualification above the results table, and revises the CWE-bench attribution. Its general-benchmark wording also changes. Neither PDF supplies a verified numbered revision or revision date. The October announcement separately frames the cyber benchmarks as guardrails-off; the later Carbon report's §7.1.2 setup also describes mitigations-off evaluation. Keep the historical safeguards-off interpretation tied to those identified representations, and do not infer that the later Fairwind qualification demonstrates safeguards-on performance or equivalence with public Carbon.

The captured PNG visually supplies 53.5% at six hours and 54.8% at ten hours. It is an auxiliary asset, outside the document-only provenance MIME allowlist, with its own receipt in [auxiliary-assets.json](auxiliary-assets.json). Preserving the HTML alone would not preserve those time-cap labels. No independent archive of this PNG was verified.

## Admission package and evidence still needed

| File | Purpose |
|---|---|
| [source-admission.yaml](source-admission.yaml) | Five pending source decisions, precise review scopes, and separate historical/fresh inspection events |
| [source-captures.yaml](source-captures.yaml) | Six document observations: five checked archives plus the changed live methodology, with complete v2 provenance fields and the live revision's explicit archive gap |
| [records.proposed.yaml](records.proposed.yaml) | Five schema-valid bibliography drafts, routes and qualifications; not authoritative records |
| [observations.proposed.yaml](observations.proposed.yaml) | Separate announcement, benchmark, Argon comparator, Carbon decision and safeguards-on observations; no assumption rescoring |
| [duplicate-check.json](duplicate-check.json) | Citation ID, normalized-title and primary-URL checks against 286 canonical records; no match found |
| [retrieval-receipts.json](retrieval-receipts.json), [comparisons.json](comparisons.json) | Actual retrieval metadata and explicit original/archive equality results; no historical-byte inference |
| [historical-intake-check.json](historical-intake-check.json) | Exact original CSV prefix fingerprint; five new deferred rows are appended separately |

Preservation required for the three candidates is now materially improved: retained source bytes, hashes, lengths, MIME signatures, archive URLs/check dates, date/edition precision and scoped locators are present. Missing historical byte identity remains missing. The changed live methodology has no verified matching archive; its existing October archive cannot be assigned the live digest. Normalized duplicate checks are bounded and should be rerun immediately before integration.

Admission also requires choosing and accepting the supported claim scope and synthesis route. Proposed routes are contextual for the announcements and technical evaluation for the three PDFs, restricted to the inspected cyber content. A different route for the mixed decision/evaluation reports is a maintainer judgment, not something established by provider authorship. Scoped bibliography admission does not authorize all findings in either long report, an empirical dataset observation, a standing-policy revision, or a full-text coverage increment.

For a benchmark-to-risk observation, retain the model, access, harness, internet, attempt/time budget, safeguards and success criterion. Do not infer actual denominators from rounded percentages or transfer results across public Carbon and Fairwind. The Carbon report provides more denominators and a decision rationale, but configuration correspondence, realized attempt counts in adaptive tests, risk-mapping adequacy, and concrete expansion/pause criteria remain unresolved in the inspected scope. These are analytical evidence gaps; a hash cannot resolve them.

## Decisions for the maintainer

1. **Historical and current presentation:** recommended: retain the October 28 / November 3 note with dated qualifications and add the November 10 observation alongside it. Keep the two earlier Argon accounts as separate scopes; do not label the first inspection erroneous.
2. **Scoped source admission:** accept or defer the five proposed bibliography records and their routes. Recommended: admit only their inspected uses after reviewing this package; keep empirical observations and any change to assumption assessments as a separate explicit decision.
3. **Methodology version:** recommended: use the October archive for the historical benchmark note, preserve the changed live revision separately, and leave its revision date unknown. Do not collapse the hashes or backdate the fresh captures.
4. **Current research question:** evaluate whether the carry-forward rule, cyber cross-check and safeguard tests justify each expansion configuration. The question is now the adequacy of the disclosed rationale. Do not continue asserting that it is absent, or treat its existence as validation.

## Checks

From the repository root, run:

```bash
python3 scripts/audit_carbon_candidates.py --require-capture-files
```

This validates draft bibliography classifications with the real corpus schema, pending statuses, source/capture links, historical CSV preservation, normalized duplicates, SHA-256/length/MIME signatures, and original/archive comparisons. It verifies all 11 retrieval entries representing nine unique retained payloads, including the auxiliary PNG. Without `--require-capture-files`, missing bytes are reported and are not called verified. Ordinary corpus checks do not ingest these proposals; source correctness and the adequacy of Google's reasoning still need substantive review.

The standard corpus validation commands remain in the [research guide](../README.md). Review preparation does not demonstrate provider compliance, independent coding, experimental replication, comprehensive literature coverage, or release synchronization.

This preparation passed the source audit with all new bytes present, the six standard corpus build/lint/audit commands, all 31 existing unit tests, seven rejection checks (corrupt digest/length, missing bytes, escaping path, false PDF equality, accidental admission, and edited historical intake), and local Markdown link checks. The six admitted authority files listed in the admission record are byte-identical to the pinned PR head. The older private corpus capture bundle was not restored: its standard audit checked metadata and reported zero of those older local payloads. Verification of the nine newly retained payloads is separate. See [validation-summary.json](validation-summary.json).

[expansion]: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/
[carbon-report]: https://storage.googleapis.com/deepmind-media/gemini/gemini_4_carbon_safety_report.pdf#page=20
[announcement-archive]: https://web.archive.org/web/20261113174018if_/https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
[method-archive]: https://web.archive.org/web/20261029225211if_/https://storage.googleapis.com/deepmind-media/gemini/gemini_4_carbon_model_evaluation.pdf
[argon-archive]: https://web.archive.org/web/20261020162135if_/https://storage.googleapis.com/deepmind-media/gemini/gemini_4_safety_report.pdf
[expansion-archive]: https://web.archive.org/web/20261112163435if_/https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/
[carbon-archive]: https://web.archive.org/web/20261110162659if_/https://storage.googleapis.com/deepmind-media/gemini/gemini_4_carbon_safety_report.pdf
