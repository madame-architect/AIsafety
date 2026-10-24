# Cyber commitment history and admitted-source integration

**Review date:** 2026-10-24. **Scope:** complete the six existing operational-source bibliography admissions and broaden the within-issuer OpenAI documentary history. This is AI-assisted source analysis, not independent human coding or an assessment of policy compliance.

## Result and units

| Collection | Result |
| --- | ---: |
| Canonical bibliography | 286 records: 156 technical, 95 governance, 35 contextual |
| Commitment history | 8 scoped commitments, 17 observations, 7 source observations |
| Benchmark-to-risk evidence | 1 research round, 6 assumptions, 6 sources, 6 observations (unchanged) |
| Analytical policy-to-assumption links | 25 |
| Retained source payloads checked | 11: 5 OpenAI policy sources and 6 operational sources |
| Disclosed historical capture gaps | 2 frozen DeepMind observations (unchanged) |

The bibliography gains six sources already admitted to the research layer and four additional OpenAI policy sources relative to main. Relative to the 282-record PR input, this pass corrects those six entries, adds four records, and leaves all 276 other records unchanged. The [audit JSON](integration-audit-2026-10-24.json) identifies the input, duplicate checks, records, and retained bundle. No new empirical evidence observations or assessment judgments are introduced.

## OpenAI: what changed in the compared texts

| Scoped provision | Compared sources | Documentary finding and limit |
| --- | --- | --- |
| High cyber threshold | Beta → v2 | Reframed from autonomous high-value exploit proofs of concept / detailed-strategy operations to removal of scaling bottlenecks. Beta risk levels and v2 capability thresholds are not calibrated equivalents. |
| Critical cyber definition | Beta → v2 | The first alternative changes from all software projects to many hardened real-world critical systems; the high-level-goal attack alternative remains. This does not quantify a change in risk. |
| External deployment gate | Beta → v2 | A post-mitigation Medium ceiling becomes a High-capability safeguards-sufficiency process. Leadership judgment, oversight, and marginal-risk qualifications remain material. |
| Internal-use safeguards | v2 → system-card Note | Preserve v2's safeguard bullet and separate autonomy rationale. The later Note explicitly says the intended trigger combines High cyber capability and long-range autonomy. Its insertion/effective date is unverified; the cover date is not used as that date. |
| Reassessment | Beta → v2 | Retains evidence-responsive reassessment while moving from scorecards to scalable evaluations, deep dives, and tests of report applicability. Annual framework review is not a blanket annual model re-test requirement. |
| Critical development gate | Beta → v2 → August 2026 statement | Compare the post-mitigation ceiling, the conditional halt pending Critical standards, and later stricter alignment/security conditions for continuing Astra training. The August statement extends policy commitments; it is not relabeled a numbered framework revision or proof of compliance with v2. |
| Research containment | August → October 2026 statements | Moves from strictest-security environment and workload migration conditions to an explicit no-live-internet boundary for frontier training, subject to future safeguard advances. The October page's claimed training resumption is not coded as verified implementation. |

The authoritative [observations](commitments.yaml) retain triggers, actions, modality, qualifications, source rationales, page/section locators, and predecessor/change notes. [The generated history](commitment-history.md) exposes those details and the source-capture metadata. All observations are policy statements; none establishes implementation or effectiveness.

### Inspected sources and locators

The beta cybersecurity table is on PDF viewer p. 8; scorecards and evaluation on pp. 13–14; deployment/development baselines and governance on pp. 20–24. The retained beta representation is a later capture of a historically attributed edition, not proof of December 2023 bytes.

Preparedness v2 (2025-04-15) places the High and Critical cyber rows on viewer pp. 6–7; evaluation provisions on pp. 9–11; safeguards, marginal-risk qualifications, internal use and governance on pp. 11–13; annual framework review in Appendix B on p. 16; and misalignment safeguards in Appendix C.2 on pp. 19–20.

The GPT-5.3-Codex system card's clarification is the final Note in §5.2.1.5 on viewer p. 30 (printed p. 29). Its cover is dated 2026-02-05, but no verified insertion date is available. The August 18 development-pacing and October 23 training-environment statements use captured HTML headings and paragraphs; they do not silently overwrite the PDF.

## Bibliographic completion and classification

All six research-accepted operational sources resolve to canonical records and captures. Full author lists, arXiv revision identities, original/revision dates, publication-state qualifications and stable URLs are retained. Normalized title, URL, and arXiv checks found no other matching record in the checked input; a missed semantically disguised duplicate remains possible.

The Amazon and Google threat-intelligence reports and AISI incident disclosure are **contextual operational evidence**, not normative governance merely because they are official publications. The ARTEMIS comparison, quantitative cyber-risk model, and simulated supply-chain evaluation remain technical sources, with their different outcome types and limitations retained. The separate AISI technical incident PDF remains **pending full-text review** and is not counted as a seventh admitted operational source.

## Preservation and reproducibility

All eleven payloads in the retained private bundle match their recorded SHA-256 digests and byte lengths. [The receipt](../../provenance/cyber-source-capture-bundle-2026-10-24.json) preserves the earlier retrieval/archive metadata. Active source records distinguish original URLs, archived representations, capture basis and publication/version claims. Local recovery does not re-date network retrieval, independently repeat the earlier archive check, or establish identity with an original publication-day representation.

The private Library bundle is not dependent on the expiring CI artifact. No full copyrighted source documents are committed to Git. [The capture instructions](../../provenance/source-capture.md) explain restoring the bundle and running the strict byte audit. A normal checkout can validate metadata and generated outputs without those private payloads; its output must not be read as a fresh remote archive verification.

The two DeepMind `legacy_uncaptured` records remain unchanged. **GitHub review/merge, a tagged release, and a verified OSF deposit remain separate states.** This integration publishes no release and makes no OSF synchronization claim.

## Checks

Run the repository bibliography build, semantic linter, commitment build, operational-evidence build, joint-dataset build, cross-source audit, and complete unit suite. The added regression tests reject broken IDs, mismatched source/version/capture data, bad hashes and path escapes, missing mandatory bytes, and improper promotion of the pending AISI PDF. Release packaging also validates the linked datasets and includes their authoritative files and generated views. Successful checks establish structural consistency and byte identity where tested, not the truth or effectiveness of source claims.
