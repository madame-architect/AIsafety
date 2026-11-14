# Gemini 4 Carbon’s November 10 expansion

This dated observation supplements the [October 28 restricted-access note](carbon-restricted-access-2026-10-28.md). It was prepared from a fresh, scoped inspection with actual retrieval timestamps in the [source records](carbon-source-review/source-captures.yaml). Source and observation admission remain pending. The November 3 observation and its original deferred intake rows are retained.

## Announced access and assessed configurations

Google's [November 10 announcement][expansion] offers public Carbon through paid API access and rollout to Ultra subscribers. It separately offers Carbon for cyber through Fairwind on a rolling basis. It retrospectively reports that a defender cohort received access two weeks earlier; this does not identify the first partner's access date. The original October 28 announcement described phases and pre-release testing participation, without a testing outcome. These remain provider announcements rather than independently verified access events.

The [new Carbon report][report] §2.5.1 (printed p. 10 / PDF viewer p. 11) describes Fairwind mitigations tailored to permit authorized specialist cyber tasks. Its safeguarded API tests must therefore be mapped to the configuration being assessed. Public product access, Fairwind access, unmitigated capability testing, and sandboxed safeguarded testing are separate conditions.

## Carbon-specific threshold and residual-risk decision

The report now supplies a Carbon determination and rationale. Under §3.1.1 (printed pp. 12–15 / viewer pp. 13–16), Google applies an aggregate general-capability change rule to decide whether another full critical-capability assessment is needed. Carbon falls below that trigger, so the report carries forward Argon's determinations. Google acknowledges larger gains on focused cyber exploit benchmarks and describes stronger safeguards. This is a disclosed application of the decision rule, not a fresh full Carbon assessment or a standing-policy revision established by this observation.

In §3.2.2 (printed pp. 19–20 / viewer pp. 20–21), Google carries forward the determination that unmitigated Carbon may reach the cyber CCL. Its CyScenarioBench V2 cross-check reports Carbon completing 12/14 end-to-end challenges and 88/104 segments, against Argon's 13/14 and 90/104, without out-of-model safeguards. On the 12-challenge subset used in the earlier Argon report, the comparison is 11/12 against 12/12; do not mix the denominators. Google judges the strengthened mitigations sufficient to bring residual cyber risk below the CCL. That is an attributed assessment requiring scrutiny, not independent evidence of acceptable deployed risk. [Carbon report, §§3.1.1 and 3.2.2][report]

The earlier review's failure to locate a Carbon rationale is thus historical. This report's publication does not establish that the same rationale was public or used for the initial cohort on November 3.

## Safeguard evidence and remaining questions

| Test reported in §3.3 | Observed measure and limit |
|---|---|
| Standard agentic coverage (printed p. 22 / viewer p. 23) | Google reports blocking every evaluated end-to-end exploit milestone with deployed safeguards enabled. The passage does not give the number of these baseline rollouts; do not invent a denominator. |
| Adaptive agentic red team (printed p. 26 / viewer p. 27) | 18 rollouts across six vulnerability/network scenarios, with up to 40 trajectory attempts and 300 inner turns per attempt. Carbon has 0.8% per-attempt breaches and 27.8% cumulative rollout breaches; Argon has 3.1% and 72.2%. A low per-attempt rate is not a low probability after repeated attempts. Raw realized denominators and the relation between the rounded 99.0% blocking claim and 0.8% breach claim need clarification. |
| Gray Swan cyber (printed p. 27 / viewer p. 28) | 25 harmful tasks with 200 attempts per seed prompt. Carbon's query success is 2.17%, while objective success is 40%; Argon's are 9.86% and 56%. This differs from the earlier indirect prompt-injection test. |
| Trajectory Labs (same page) | 132 hours and over 13,000 requests found no new universal jailbreak. The report also describes successful individual tasks with substantial human intervention. Universal-jailbreak absence does not mean zero successful misuse. |

The next assessment should examine whether an aggregate capability-change rule and this domain cross-check adequately address improved exploitation performance; which model checkpoints, safeguards, privileges, tools and retry budgets each test covers; how those match public Carbon and Fairwind; and how the measured breaches connect to the claimed residual risk. Concrete expansion or pause thresholds, longitudinal misuse outcomes, and configuration-specific acceptance criteria were not established by this selected-section review. General monitoring and safeguards are disclosed; the unresolved issue is their adequacy and applicability.

The October ExploitGym observations remain safeguards-off benchmark results: 53.5% at six hours and 54.8% at ten hours. They are not safeguarded deployment outcomes or operational-harm estimates. The archived methodology, its changed live revision, and the chart are separately identified in the [source review](carbon-source-review/README.md).

[expansion]: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/
[report]: https://storage.googleapis.com/deepmind-media/gemini/gemini_4_carbon_safety_report.pdf#page=20
