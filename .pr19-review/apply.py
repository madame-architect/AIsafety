"""Apply the two localized PR19 research-review corrections to the pinned baseline."""
from pathlib import Path
import yaml

ROOT = Path.cwd()
D = ROOT / 'research/cyber-deployment'

def replace_once(path, before, after):
    text = path.read_text(encoding='utf-8')
    if text.count(before) != 1:
        raise ValueError(f'{path}: expected exactly one baseline passage')
    path.write_text(text.replace(before, after, 1), encoding='utf-8')

class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

def save(path, data):
    path.write_text(yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False,
                              allow_unicode=True, width=100), encoding='utf-8')

p = D / 'commitments.yaml'
data = yaml.safe_load(p.read_text(encoding='utf-8'))
item = next(o for o in data['observations'] if o['id'] == 'openai_cyber_critical_development_gate_v2')
assert item['trigger'] == 'A covered system has Critical cyber capability.'
item.update(
    trigger='Two related triggers: (1) attained Critical cyber capability for the Table 1 conditional halt; '
            '(2) attained or forecast Critical capability in a Tracked Category, including cyber, for '
            'the additional development safeguards in section 4.4.',
    action='For attained Critical cyber capability, halt further development until safeguard and '
           'security-control standards meeting a Critical standard are specified (Table 1). '
           'For attained or forecast Critical capability, require additional safety and security '
           'controls during development, regardless of whether or when external deployment is planned '
           '(section 4.4).',
    qualifications='The Table 1 halt is conditional on specifying standards, not an unconditional '
                   'permanent moratorium. Section 4.4 retains prospective safeguard coverage; a forecast '
                   'alone is not coded as triggering the Table 1 halt. The Critical approach must address '
                   'malicious internal/external actors and model misalignment. Read with the general '
                   'risk-minimization process and section 4.3 qualifications. Neither rule demonstrates '
                   'implementation or safeguard effectiveness.',
    locator='Table 1, Critical cybersecurity safeguards, PDF viewer p. 7 (printed p. 6); section 4.4, '
            'PDF viewer p. 13 (printed p. 12); context: section 2.2, p. 5 and sections 4.2-4.3, pp. 11-13.',
    change_note='Retains prospective coverage for attained or forecast Critical capability while '
                'changing the beta post-mitigation ceiling and alignment-evidence gate into additional '
                'development safeguards plus a separate conditional halt for attained Critical cyber '
                'capability pending specified standards. Prospective safeguards did not disappear; '
                'the two triggers and their actions are not interchangeable.'
)
save(p, data)

p = D / 'dataset-links.yaml'
data = yaml.safe_load(p.read_text(encoding='utf-8'))
assert data['schema_version'] == 'cyber-dataset-links-v1'
data['schema_version'] = 'cyber-dataset-links-v2'
# Relationships describe the policy's stance toward the stated risk proposition,
# not a positive/negative score for the policy or its safeguards.
changes = {
    'deepmind_weights_to_defense_persistence': ('policy_assesses',
        'Weighs whether offensive uplift persists after automated defense and societal adaptation '
        'when judging conditional weight-security recommendations. Does not assume persistence or '
        'establish the effectiveness of the recommended controls.'),
    'openai_cyber_high_threshold_to_defense_persistence': ('policy_depends_on',
        'The operational threshold premise requires offensive capability to survive relevant target '
        'defenses. A challenged general persistence assessment bounds that inference; it is not a '
        'rating of a particular provider safeguard.'),
    'openai_frontier_safeguard_review_to_defense_persistence': ('policy_assesses',
        'Assesses whether offensive uplift survives proposed mitigations when judging residual risk. '
        'The challenged assessment concerns offensive persistence, not safeguard effectiveness; '
        'the latter requires control-specific evidence.'),
    'openai_frontier_reassessment_to_task_transfer': ('policy_assesses',
        'Reassesses whether evaluation performance transfers to operational tasks as evaluations, '
        'elicitation and deployment conditions change; it does not assume that transfer always holds.'),
    'openai_frontier_reassessment_to_capability_access': ('policy_assesses',
        'Reassesses whether capability is accessible under changed permissions, fine-tuning, weights '
        'release or new features; it does not assume the assessed access conditions remain fixed.'),
    'openai_frontier_reassessment_to_defense_persistence': ('policy_assesses',
        'Reassesses whether offensive uplift persists as misuse, elicitation and defenses change. '
        'Neither the reassessment duty nor the challenged proposition validates a particular safeguard.'),
    'openai_cyber_critical_development_gate_to_defense_persistence': ('policy_counters',
        'Additional development safeguards seek to prevent offensive capability from persisting '
        'through controls. The conditional development gate is a policy rule; challenged offensive '
        'persistence is not evidence that those controls work.'),
    'openai_frontier_research_containment_to_capability_access': ('policy_counters',
        'Isolation and no-live-internet training seek to restrict access to resources needed for '
        'offensive operations. This identifies the intended control mechanism, not achieved containment.'),
    'openai_frontier_research_containment_to_workflow_autonomy': ('policy_counters',
        'Tool and communication restrictions seek to interrupt unauthorized multi-step workflows. '
        'This identifies an intended interruption, not demonstrated prevention of autonomous actions.'),
    'openai_frontier_research_containment_to_defense_persistence': ('policy_counters',
        'Isolation and defense in depth seek to interrupt offensive workflows, with red-teaming to '
        'test that aim. Evidence challenging offensive persistence does not establish the '
        'effectiveness of these containment measures.'),
}
by = {link['id']: link for link in data['links']}
assert set(changes) <= set(by)
for key, (relationship, rationale) in changes.items():
    by[key].update(relationship=relationship, rationale=rationale)
save(p, data)

p = ROOT / 'scripts/build_cyber_datasets.py'
replace_once(p, 'ALLOWED_RELATIONSHIPS = {"policy_depends_on"}', '''RELATIONSHIP_LABELS = {
    "policy_depends_on": "Depends on risk premise",
    "policy_counters": "Seeks to counter risk pathway",
    "policy_assesses": "Assesses risk premise",
}
ALLOWED_RELATIONSHIPS = set(RELATIONSHIP_LABELS)''')
replace_once(p, 'links.get("schema_version") != "cyber-dataset-links-v1"',
                'links.get("schema_version") != "cyber-dataset-links-v2"')
replace_once(p, '        if link.get("relationship") not in ALLOWED_RELATIONSHIPS:',
                '        if not isinstance(link.get("relationship"), str) or link["relationship"] not in ALLOWED_RELATIONSHIPS:')
replace_once(p, '''def short(value: Any, limit: int = 180) -> str:
    text = " ".join(str(value).split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"''',
'''def cell(value: Any) -> str:
    """Keep the full rationale visible; do not truncate interpretation caveats."""
    return " ".join(str(value).split()).replace("|", "\\\\|")''')
replace_once(p, '''        "| Commitment | Covered observations | Assumption | Latest assessment | Evidence roles | Why the policy depends on it |",
        "|---|---:|---|---|---|---|",''', '''        "The relationship describes the policy's stance toward the stated risk proposition, not whether "
        "the policy succeeds. Assessments and evidence roles below always concern the assumption as written.",
        "",
        "- **Depends on risk premise** (`policy_depends_on`): the policy argument relies on that proposition.",
        "- **Seeks to counter risk pathway** (`policy_counters`): the policy aims to interrupt or reduce it; success is not inferred.",
        "- **Assesses risk premise** (`policy_assesses`): the policy or its stated rationale evaluates whether, or to what extent, it holds.",
        "",
        "**Direction warning:** `defense_persistence` means offensive uplift survives defenses and adaptation, "
        "not that defenses remain effective. Its **challenged** assessment is not evidence against safeguards "
        "and does not establish the effectiveness of any particular safeguard. No assessment is inverted or "
        "converted into a policy-effectiveness score.",
        "",
        "| Commitment | Covered observations | Relationship to assumption | Assumption | Assumption assessment (not safeguard rating) | Evidence roles | Link rationale |",
        "|---|---:|---|---|---|---|---|",''')
replace_once(p, '''            f"`{assumption['id']}` — {assumption['label']} | **{latest['code']}** as of {latest['as_of']} | "
            f"{role_text} | {short(link['rationale'], 210)} |"''', '''            f"{RELATIONSHIP_LABELS[link['relationship']]} (`{link['relationship']}`) | "
            f"`{assumption['id']}` — {assumption['label']} | **{latest['code']}** as of {latest['as_of']} | "
            f"{role_text} | {cell(link['rationale'])} |"''')
replace_once(p, '''        "The link says a policy argument relies on an assumption; it does **not** say that the evidence caused "
        "the policy change, that the policy was implemented, or that the safeguard was effective.",''', '''        "A link distinguishes reliance on, intended counteraction of, and assessment of a risk proposition. "
        "It does **not** say that the evidence caused the policy change, that the policy was implemented, "
        "or that the safeguard was effective. Evidence against a general risk proposition is not a "
        "control-specific effectiveness estimate.",''')

p = D / 'datasets.yaml'
data = yaml.safe_load(p.read_text(encoding='utf-8'))
data['linkage']['semantics'] = (
    'Links distinguish policy_depends_on (relies on the stated risk proposition), policy_counters '
    '(seeks to interrupt or reduce the risk pathway), and policy_assesses (evaluates whether or to '
    'what extent the proposition holds). Evidence roles and assessments always refer to the assumption '
    'as written and are not inverted into policy-effectiveness scores. In particular, challenged '
    'offensive defense_persistence neither challenges safeguards nor establishes effectiveness of '
    'any particular control. No link establishes implementation, effectiveness or causal influence '
    'on a policy revision.')
save(p, data)

p = D / 'README.md'
replace_once(p,
    '`dataset-links.yaml` records when a commitment argument **depends on** an assumption. The benchmark-to-risk dataset then records evidence bearing on that assumption. The bridge is the stable `assumption_id`.',
    '`dataset-links.yaml` (schema v2) distinguishes **depends on** (`policy_depends_on`), **seeks to counter** (`policy_counters`), and **assesses** (`policy_assesses`). These describe the policy argument or intended action relative to the stated risk proposition; they do not score policy effectiveness. The bridge remains the stable `assumption_id`, and evidence judgments always concern that assumption as written.')
replace_once(p,
    "For example, the current DeepMind model-weight security provision depends on assumptions about capability access, transfer to operational tasks, incremental uplift over a no-AI baseline, translation to severe harm, and persistence after defenses and adaptation. Evidence can update those assumptions without being treated as the cause of the policy revision.",
    "For example, the DeepMind model-weight security rationale relies on access, transfer, uplift and harm premises, but weighs whether offensive uplift persists after defensive adaptation. OpenAI containment aims to counter such persistence, while safeguard review and reassessment examine it. **`defense_persistence` means offensive gains survive defenses, not that defenses remain effective.** Its challenged assessment neither disproves safeguards nor establishes the effectiveness of any particular safeguard. Evidence does not become an effectiveness score by reversing its sign.")

p = D / 'expansion-reconciliation-2026-10-24.md'
replace_once(p,
    'Compare the post-mitigation ceiling, the conditional halt pending Critical standards, and later stricter alignment/security conditions for continuing Astra training.',
    'Compare the beta post-mitigation ceiling with two distinct v2 rules: a conditional halt for attained Critical cyber capability pending specified standards, and additional development safeguards for attained **or forecast** Critical capability regardless of external deployment. Prospective safeguards remain present. Later statements add stricter alignment/security conditions for continuing Astra training.')
marker = '### Inspected sources and locators'
replace_once(p, marker, '''### Localized pre-merge review correction

At reviewed baseline `8841f93`, the v2 development-gate trigger omitted forecast capability, and some links conflated offensive persistence with defensive effectiveness. The corrected observation separates Table 1's attained-capability conditional halt (viewer p. 7) from section 4.4's safeguards for attained or forecast capability (viewer p. 13). Forecast capability alone is not coded as triggering the Table 1 halt.

The link schema now distinguishes reliance, intended counteraction, and assessment. The generated map exposes the relationship and labels judgments as assumption assessments, not safeguard ratings. `defense_persistence` retains its offensive meaning and its existing challenged assessment; that judgment cannot establish effectiveness of a particular safeguard. Link rationales are displayed without truncation. The seven OpenAI histories, all 286 bibliography records, source-capture metadata, operational observations and historical evidence judgments remain unchanged apart from this one policy-record correction and link interpretation. This is not a new empirical round or a fresh archive verification.

''' + marker)

p = ROOT / 'METHODS.md'
replace_once(p,
    'Critical capability definitions and the development gate are coded separately.',
    'Critical capability definitions and the development gate are coded separately. Within the v2 development gate, Table 1 specifies the conditional halt for attained Critical cyber capability, while section 4.4 additionally covers attained or forecast Critical capability with development safeguards irrespective of deployment. The forecast provision is not treated as withdrawal of prospective coverage or as automatically triggering the halt.')
replace_once(p, '## Validation, releases, and AI assistance', '''## Direction of policy-to-assumption links

The link schema v2 separates `policy_depends_on` (reliance on the stated risk proposition), `policy_counters` (intended interruption or reduction of its risk pathway), and `policy_assesses` (evaluation or reassessment of whether it holds). Each row has one principal relationship for its stated rationale. An intended counteraction is not proof of its success; an assessment link does not assume a proposition is true. The original assumption IDs, definitions and evidence judgments are preserved, and the generated map displays the relationship next to the assumption assessment.

In particular, `defense_persistence` describes persistence of offensive uplift after defenses and adaptation, not durability of safeguards. Evidence challenging it is neither a negative safeguard rating nor sufficient evidence that a specific safeguard works. No inverse score or automatic effectiveness conclusion is computed. This distinction was added in response to localized pre-merge review of PR #19; no operational research round was reopened.

## Validation, releases, and AI assistance''')
print('Applied the forecast-trigger and directional-link corrections.')
