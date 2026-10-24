# Cyber capability evidence and safety commitments

This research area asks how evidence about cyber capability informs risk
assessments and safeguard decisions. The first longitudinal pilot tracks one
scoped security recommendation across two existing bibliography records.

**Status:** AI-assisted pilot, prepared on 2026-10-17 UTC. It contains two
document observations and one compared policy provision. Implementation and
effectiveness have not been assessed. It is not a systematic survey of issuers,
a compliance assessment, or a complete comparison of the two frameworks.

## Read and edit

| File | Role |
|---|---|
| [commitment-history.md](commitment-history.md) | Generated, readable history and source provenance |
| [commitments.yaml](commitments.yaml) | Authoritative scoped policy observations and comparison notes |
| [evidence.yaml](evidence.yaml) | Authoritative observations of cited source editions |
| [../../records.yaml](../../records.yaml) | Bibliographic authority; generates BibTeX through the existing build |
| [source-verification.md](source-verification.md) | Earlier five-source review; a historical audit with its original scope |

The companion YAML files reference existing citation IDs. A source observation
can support several policy provisions, so edition information and preservation
notes are stored once. The `snapshots` list is a registry of observations; an
entry does not by itself mean the source bytes were captured or archived.

From the repository root:

```bash
python3 scripts/build_commitments.py
python3 scripts/build_commitments.py --write
python3 scripts/build_commitments.py --check
python3 scripts/build.py --check
python3 -m unittest discover -s tests -v
```

The default commitment command validates without writing. `--write` regenerates
the Markdown history; `--check` also detects a missing or stale history without
writing. Structural validation does not establish that an interpretation is
correct or that a commitment was fulfilled.

## Unit of analysis

Track **one issuer's scoped policy provision as observed in a particular source
edition**, with a stable `commitment_id` linking its history. Record the trigger,
action, scope, modality, qualifications, source rationale, and passage locator.
Keep an analyst's interpretation in `change_note`, separate from the issuer's
reasoning in `source_rationale`.

The pilot is the model-weight security recommendation associated with Google
DeepMind's cyber critical capability level. The generated history contains
extracted policy paraphrases, source locators, and the comparison. This choice exercises the method using
citations already present in the collection; it does not imply representative
selection or company-wide coverage.

## Coding rules

1. **Read a provision with its dependencies.** Inspect definitions, scope,
   exceptions, cross-references, and general decision rules. A changed word in a
   table may have a different meaning once those clauses are considered.
2. **Preserve modality.** `requirement`, `recommendation`, `discretionary`, and
   `intention` describe the provision's wording. None is a numerical safety
   score. Keep qualifications attached to every observation.
3. **Record a supported relationship.** `observed` means a baseline observation
   in this dataset, not the first historical introduction. `revised`,
   `clarified`, `retained`, and `withdrawn` require a predecessor and a reason.
   An explicit withdrawal needs positive source evidence. Wording not located
   during a search is a review gap; check relocation and cross-references
   before coding withdrawal. Record that gap in the inspection or review note.
4. **Separate clocks.** `published_on` describes the source edition;
   `observed_on` describes our actual inspection, in UTC. Optional
   `claimed_application_on` records only a source-attributed application date
   and requires an explanation. An old page's publication date does not date
   a later note added to it. In evidence v2, required unknown publication dates
   are explicit nulls; partial publication dates retain their known precision.
   `retrieved_at` records actual byte retrieval with a full UTC timestamp.
5. **Separate kinds of evidence.** The policy-observation format accepts `policy_statement` only.
   A later implementation report or effectiveness study must be admitted as
   its own source evidence and linked to the provision in a future extension.
   It must not silently replace the earlier policy statement. A claimed
   application date does not verify application.
6. **Capture provenance for every new observation.** Evidence v2 requires
   `original_url`, `retrieved_at`, `archive_url`, `archive_checked_on`, `sha256`,
   `byte_length`, `mime_type`, `published_on`, `version_claim`, and `locator_basis`.
   Hash exact retrieved PDF bytes or the retained HTML representation; preserve
   capture-specific HTML archives where legally and technically feasible.
   Missing archives require an explicit reason and remain a release limitation.
   The two first observations are frozen `legacy_uncaptured` exceptions with
   null capture fields; a later retrieval cannot establish their historical
   bytes. See the [capture procedure](../../provenance/source-capture.md).
   Structure and digest checks do not independently authenticate an archive.
7. **Keep history inspectable.** Add new observations for later source states.
   Correct an extraction error in version control with a reason; do not turn
   the correction into an invented policy-change event. Bibliographic metadata
   can be corrected without silently rewriting historical observation dates
   or source identifiers. Check links when a citation is merged or renamed.

The initial observations are AI-assisted extractions from specified primary
passages. Repeated AI review is not independent human coding. Source review,
research judgment, and maintainer acceptance remain distinct activities.

## Connection to the benchmark-to-risk study

The policy history supports the middle part of the research argument. Each
connection needs its own evidence:

| Connection | Question to examine | Evidence needed |
|---|---|---|
| Evaluation result to risk threshold | Why should performance under the evaluated conditions imply the specified risk capability? | Evaluation setup, elicitation assumptions, operational comparisons, and the issuer's threshold definition |
| Risk threshold to safeguard decision | Which action follows, for which systems, with what discretion or exceptions? | Dated policy provisions, decision rules, and stated rationales |
| Safeguard decision to residual risk | Was the relevant control applied, and what evidence supports its effect in that setting? | Attributed implementation reports and separately assessed effectiveness evidence |

Use the same source identities when evidence informs both studies. Keep
technical findings and governance statements distinguishable. A reported
incident can motivate an assumption check, but temporal proximity to a policy
revision does not establish what caused that revision. Compare the issuer's
explanation with the available evidence and record remaining uncertainty.

## Bounded next steps

First, review this one history for faithful extraction and usable provenance.
Success means another reader can reconstruct the change and see where evidence
stops. Next, add a second issuer and a few provisions concerning capability
assessment, deployment decisions, or monitoring. Add new publications through
the existing intake process after checking the corpus for duplicates.

Before expanding to implementation tracking, add a separate evidence type with
source attribution, model or service scope, event dates, and an explicit link
to the provision it concerns. A provider's implementation report and an
independent assessment should remain distinguishable. Do not create a blanket
`implemented: false` value for provisions we have not investigated.

An initial research output could ask: **How do changes in cyber capability
thresholds and the assumptions behind them alter stated safeguard decisions?**
Compare within an issuer before attempting cross-issuer conclusions. Threshold
names from different frameworks need explicit definitions before comparison.
The pilot has no scheduled monitoring; any future recurring collection should
declare its issuer coverage, sources, cadence, and handling of missed captures.

OSF synchronization remains the separately documented release task. A local
research update or a GitHub merge does not establish a matching OSF deposit.
The [release protocol](../../releases/README.md) requires a tagged GitHub release,
an exact-byte OSF deposit, and object/version identifiers and hashes in the
external release manifest before synchronization can be confirmed.

