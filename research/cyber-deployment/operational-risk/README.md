# Operational cyber-risk evidence

This directory admits a **bounded, AI-assisted research round** on the assumptions
that connect cyber benchmark performance to operational risk. It extends the
longitudinal cyber-safety commitment pilot without treating a benchmark score,
policy statement, operational incident, or modeled estimate as interchangeable
evidence.

## Status and isolation

- Six directly inspected sources are accepted into this **research layer**.
- The companion AISI technical incident PDF is linked but not independently
  admitted because the bounded research environment could not parse it.
- No source in this round validates the entire chain from benchmark score to
  realized harm.
- Canonical admission to `records.yaml` is deliberately deferred. A separate
  concurrent agent is correcting preservation and OSF materials, so this change
  adds only new files under this directory and does **not** modify the
  bibliography, generated BibTeX, intake log, preservation snapshots, release
  manifests, or OSF status.

## Files

| File | Role |
|---|---|
| [assumptions.yaml](assumptions.yaml) | Stable registry of six benchmark-to-risk assumptions and round-level assessments |
| [source-admission.yaml](source-admission.yaml) | Accepted sources, exact versions or dates, duplicate-check result, provenance, and admission limits |
| [risk-evidence.yaml](risk-evidence.yaml) | Source-level observations linked to assumptions with `supports`, `challenges`, `bounds`, or `contextualizes` roles |
| [evidence-map.md](evidence-map.md) | Generated human-readable evidence map |
| [bounded-review.md](bounded-review.md) | Curated research synthesis and methodological limits |
| [build.py](build.py) | Validator and deterministic evidence-map generator |

## Central finding

The strongest admitted evidence concerns **speed, scale, parallelism, and skill
compression**. The weakest links are quantitative uplift against a matched
non-AI baseline, translation from compromise to severe harm, and the net effect
after defenders adapt.

A defensible synthesis is:

> When benchmark-relevant capabilities are available through an effective
> scaffold, supplied with suitable tools and permissions, and inserted into an
> operational workflow, they can reduce expertise, time, and labor requirements
> and automate meaningful stages of cyber operations. The resulting increase
> in successful compromise depends materially on target defenses, human
> orchestration, and downstream bottlenecks.

## Validate and regenerate

From the repository root:

```bash
python3 research/cyber-deployment/operational-risk/build.py --check
python3 research/cyber-deployment/operational-risk/build.py --write
```

The validator checks identifiers, allowed codes, cross-file links, source
admission status, and whether `evidence-map.md` matches the YAML. It does not
verify source truth, causal attribution, completeness, preservation, or
scholarly consensus.

## Next integration step

After the preservation and OSF work lands, rerun duplicate checks against the
new `records.yaml`, create canonical bibliography records for the six accepted
sources, regenerate BibTeX and views, and log the actual integration date. The
linked but unparsed AISI technical report should remain pending until its full
text and relationship to the HTML disclosure are reviewed.
