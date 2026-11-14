# Research guide

The broad bibliography and review examine what frontier AI evaluation research establishes and how governance translates evidence into decisions. The cyber work is a case study within that project. The current synthesis is provisional: it integrates substantial existing research while keeping incomplete reading, disputed interpretations and publication decisions visible.

## Read, verify, and use

| Question | Route |
|---|---|
| What has the research established, under which conditions? | [Broad synthesis](synthesis/review.md), organized across evaluation, safeguards, oversight, governance and cyber evidence |
| Which evidence supports or qualifies a claim? | [Claim-and-evidence map](synthesis/claims.md), including versions, locators and review limits; generated from authoritative [claims.yaml](synthesis/claims.yaml) |
| What was actually read or checked? | [Coverage summary](synthesis/coverage-summary.md) and [source-level ledger](synthesis/coverage.csv) |
| What changed in later thematic research? | [Review rounds and source events](synthesis/rounds.md), with explicit relevance decisions, reading scopes and preservation limits |
| What remains unresolved? | [Reconciliation and decisions](synthesis/reconciliation.md) |
| Where are the original source identities? | Authoritative [records.yaml](../records.yaml), [stream index](../views/index.md), and [complete bibliography](../frontier-governance-evals.bib) |
| How was this assembled, and how can I reproduce the outputs? | [Methods](../METHODS.md) and [root build instructions](../README.md#build-and-verify) |
| How does this work in a concrete domain? | [Cyber capability evidence and commitments](cyber-deployment/README.md), with documentary history, operational evidence and dated deployment observations |

Technical readers can trace a result through its task, model, scaffold, comparator and outcome. Governance readers can examine authority, decision scope, exceptions and the distinction between stated controls and observed implementation. Reviewers should use both the claim records and coverage ledger: a source's inclusion does not mean that it supports a particular conclusion, and a coverage label does not measure evidence quality.

## Scope and remaining work

The November 8 review supplies the broad organizing argument and source-level notes; the November 14 audit and evidence update qualify that work. Their adapted research content is integrated here without reproducing private conversations. Original reading labels, subsequent checking depth and experimental replication remain separate. The prior audit's central-claim pass across 105 full-text-labeled records was not 105 complete-document rereads. This integration does not certify those labels or complete the remaining sources.

The complete-corpus objective remains: deepen reading where needed, connect claim-critical evidence and counterevidence, reconcile source families and versions, and test the synthesis against alternative interpretations. The claim map is a curated starting set rather than an exhaustive account of every possible claim. All current bibliography records belong in coverage; they need not all support an argument.

Later rounds preserve the inherited ledger and append source-reading events. A source can acquire a background, related-work or exclusion role without supporting a claim. Complete reading counts advance only for a captured, completely read text whose edition matches the record; related preprints and scoped checks remain separately labeled. Read the generated summary for current counts and the reconciliation queue for numbers omitted or qualified after checking.

Some gaps concern evidence: incomplete appendices, uncertain historical versions, missing comparators, shared data lineage and unverified implementation or causal effects. Others concern research organization: precise locators, relevance decisions, consistent counts and navigable links. Better organization makes the first group visible; it does not resolve it.

The cyber datasets retain their own admission rules and dated observations. [Carbon's source-review package](cyber-deployment/carbon-source-review/README.md) remains pending despite its merged documentation. The synthesis may discuss that provisional case with its status explicit; it does not admit its proposed records automatically.

The maintainer decides the final thesis, publication venue and whether to publish. A bounded cyber note is one possible output alongside the broad synthesis. Repository checks, source inclusion and separate-agent review do not constitute independent human review, source independence or publication approval.
