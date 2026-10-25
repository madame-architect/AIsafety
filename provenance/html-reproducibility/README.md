# Five-page HTML preservation comparison

Review: 2026-10-24 (America/New_York). Fresh network retrievals are separately
dated in UTC in [results.json](results.json). This review leaves the original
retrieval dates, archive-check dates, digests and lengths unchanged.

## What was recovered and compared

The original `cyber-research-source-captures-2026-10-24.zip` was recovered.
Its 15,924,250 bytes match SHA-256
`7d94cdb5c6349ae4b32978a35364980a2d6f6a225c8402f454ad14b186fc3509`.
All five historical HTML files match their original recorded SHA-256 and
length. The other six bundle objects were also verified by the strict source
audit; this comparison concerns only the five HTML pages.

For each page, we retrieved the exact timestamped archive in explicit `id_`
mode twice and ordinary replay mode once. The two raw decoded entities match
byte for byte for every page. Each ordinary replay differs from its retained
historical file. Whole-file comparison identifies the differences below;
normalized article text, numbers, headings, table text and annotations agree
between the original, fresh raw and fresh replay representations.

| Page | Historical bytes | Fresh replay bytes | New raw bytes | Article characters | HTML tables / rows / cells |
| --- | ---: | ---: | ---: | ---: | --- |
| OpenAI development pacing | 474,542 | 474,539 | 451,192 | 10,266 | 0 / 0 / 0 |
| OpenAI training environment | 482,384 | 482,388 | 458,987 | 22,456 | 0 / 0 / 0 |
| Amazon FortiGate campaign | 1,320,664 | 1,320,657 | 1,310,596 | 17,688 | 1 / 3 / 15 |
| Google adversarial AI tracker | 524,637 | 524,633 | 495,047 | 47,846 | 18 / 41 / 90 |
| AISI incident disclosure | 54,136 | 54,143 | 41,426 | 17,264 | 0 / 0 / 0 |

For these five historical-to-fresh **replay pairs**, every changed byte is
accounted for by Wayback-generated analytics server/timing values, the appended
replay retrieval date, and appended playback timings. AISI's toolbar capture
count also changes from 79 to 80. The machine results retain those actual
before/after values. Replacing only these four narrowly specified archive
fields makes every remaining byte identical for all five pairs.

This establishes the cause of the mismatches in these compared pairs. It does
not explain any earlier unretained download, including the previously reported
466,360-byte OpenAI response, or establish that future archive responses will
be identical.

## Content review and boundaries

The comparison uses the one `article` element in each saved document. It
removes script/style/noscript/template descendants and collapses whitespace;
it preserves numbers, punctuation and qualifications. It retains duplicate
contents lists and related cards where the publisher placed them inside that
element. Ordered table text, headings, numeric tokens, footnote containers,
superscripts, captions and image alt text receive separate checksums.
Python 3.12, Beautiful Soup 4.15.0 and `html.parser` define this extraction.

The scoped AI-assisted passage review covered:

| Page | Conclusions and qualifications checked in both original and new representations |
| --- | --- |
| OpenAI development pacing | Astra's provisional Critical assessment; paused workloads and security migration; monitoring scope and escalation timing; alignment requirements; the final asterisk note. These are provider commitments, not verified implementation. |
| OpenAI training environment | No live internet during frontier training, its safeguard-dependent qualification, and the separate qualification covering most evaluations; offline-world design; stated resumption conditions. Claimed security results are not independently verified. |
| Amazon FortiGate | More than 600 devices in more than 55 countries during January 11–February 18; exposed interfaces and weak credentials; absence of observed FortiGate vulnerability exploitation; failures against defended targets; downstream-harm limitations and the indicator table. |
| Google tracker | Campaign completion in less than six hours, thousands of credentials, initial human compromise/configuration and autonomous pipeline operation; disruption/safety-response statements. The account does not establish zero human involvement throughout or a matched no-AI causal effect. All 18 HTML table elements were included. |
| AISI disclosure | 122 runs, 19 actions across 10 runs; internet access and disabled classifiers; maintainer rejection; no resulting harm identified. Four superscripts are date ordinals, and two footnote containers are empty. The linked technical report remains unadmitted. |

The OpenAI asterisk note is ordinary article text rather than a semantic HTML
footnote. No nonempty semantic footnote containers were found in the other
pages. This is a check of the retained HTML, not a claim that no additional
notes could be conveyed by external assets. Image pixels, CSS, JavaScript,
script-rendered content, and linked documents were not downloaded or compared.
Captions and alt text present in HTML were compared. This AI-assisted
documentary review is not independent human coding or experimental replication.

## Public verification and remaining limitation

Permission covering every byte of the complete saved HTML representations,
including embedded publisher and archive code, has not been established.
Accordingly, this PR publishes precise archive URLs, retrieval details,
fingerprints, short passage markers and comparison results, without the full
copyrighted pages. This is an unresolved redistribution scope, not a finding
that redistribution is prohibited. Relevant permission scopes include
[AWS terms](https://aws.amazon.com/terms/),
[Google site policies](https://developers.google.com/terms/site-policies), and
[OpenAI terms](https://openai.com/policies/terms-of-use/). A separate GOV.UK
organization page's licensing does not establish a license over the complete
`aisi.gov.uk`, Webflow and archive payload.

The private historical files were recovered, so this is not a lost-original
gap. These ordinary replay URLs did not reproduce the historical full-file
hashes in this check. Public access to the exact historical files remains
unestablished. The reproducible raw baseline is
a separately dated representation and does not retroactively repair that
limitation. An archive timestamp is an archive assertion, not proof of bytes
published on the article date.

From a clean checkout, install the ordinary repository requirements and run:

```bash
python -m pip install -r requirements.txt
python provenance/html-reproducibility/verify.py
```

The command retrieves the five exact `id_` URLs from `results.json` using the
capture tool's stated request headers, checks the decoded entity SHA-256 and
length, rejects changed archive selection, and checks selected passage markers.
It writes no files and returns failure for any mismatch. A passing marker
check alone does not establish completeness. HTTP compression is decoded
explicitly; the results separately record encoded response-body fingerprints.
The fingerprint being reproduced is the **decoded raw HTML entity**, before
HTML parsing, not gzip transfer bytes or normalized text.
The exact public entry point passed for all five pages at
2026-10-25 00:05:57–00:06:02 UTC (October 24 in America/New_York);
`public_instructions_check` in the results records those separate requests.
The same entry point also passed from a public-file checkout with no private
captures at 00:08:56–00:09:01 UTC; `clean_checkout_instructions_check` records
that additional check.

For reviewers with the retained originals and fresh saved files, reproduce the
full comparison using:

```bash
python -m pip install beautifulsoup4==4.15.0
python provenance/html-reproducibility/compare.py \
  --original-dir .source-captures --fresh-dir /path/to/fresh-html
```

`fresh-html` contains `HISTORICAL_ID.raw.html` and
`HISTORICAL_ID.replay.html`. The comparator checks all supplied file
fingerprints before comparing them. Historical receipt data is never
overwritten. The public verifier and the local comparison serve different
purposes: the former checks publicly retrievable new raw baselines; the latter
also requires access to the recovered historical files. A future failed fetch
or changed fingerprint should be reported and investigated as a new event.
