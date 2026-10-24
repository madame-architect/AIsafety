"""Protect the two localized PR19 interpretation corrections without rescoring evidence."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_commitments
import build_cyber_datasets as joint


class CyberReviewCorrectionTests(unittest.TestCase):
    def test_attained_halt_and_forecast_safeguards_remain_distinct(self):
        _, observations = build_commitments.load_history(ROOT)
        by = {item['id']: item for item in observations}
        item = by['openai_cyber_critical_development_gate_v2']
        self.assertIn('attained Critical cyber capability for the Table 1 conditional halt', item['trigger'])
        self.assertIn('attained or forecast Critical capability', item['trigger'])
        self.assertIn('For attained Critical cyber capability, halt further development until', item['action'])
        self.assertIn('For attained or forecast Critical capability, require additional safety and security controls', item['action'])
        self.assertIn('regardless of whether or when external deployment is planned', item['action'])
        self.assertIn('a forecast alone is not coded as triggering the Table 1 halt', item['qualifications'])
        self.assertIn('Prospective safeguards did not disappear', item['change_note'])
        self.assertIn('section 4.4, PDF viewer p. 13', item['locator'])
        self.assertEqual(item['previous_observation_id'], 'openai_cyber_critical_development_gate_beta')
        # This is an extraction correction, not a new source or an invented effective date.
        self.assertEqual(item['snapshot_id'], 'openai_preparedness_v2_captured_2026_10_24')
        self.assertNotIn('claimed_application_on', item)
        history, counts = build_commitments.generate_history(ROOT)
        section = history.split('### Observation openai_cyber_critical_development_gate_v2', 1)[1].split('\n### ', 1)[0]
        self.assertIn('attained or forecast Critical capability', section)
        self.assertIn('a forecast alone is not coded as triggering the Table 1 halt', section)

    def test_defense_persistence_links_preserve_the_direction_of_the_proposition(self):
        _, links, _, assumptions, _ = joint.validate()
        by = {item['id']: item for item in links['links']}
        expected = {
            'deepmind_weights_to_defense_persistence': 'policy_assesses',
            'openai_cyber_high_threshold_to_defense_persistence': 'policy_depends_on',
            'openai_frontier_safeguard_review_to_defense_persistence': 'policy_assesses',
            'openai_frontier_reassessment_to_defense_persistence': 'policy_assesses',
            'openai_cyber_critical_development_gate_to_defense_persistence': 'policy_counters',
            'openai_frontier_research_containment_to_defense_persistence': 'policy_counters',
        }
        for key, relation in expected.items():
            with self.subTest(link=key):
                self.assertEqual(by[key]['relationship'], relation)
        assumption = next(a for a in assumptions['assumptions'] if a['id'] == 'defense_persistence')
        self.assertIn('Offensive uplift', assumption['label'])
        # The original assessment is append-only. This does not freeze future rounds' conclusions.
        original = next(a for a in assumption['assessments'] if a['as_of'] == '2026-10-17')
        self.assertEqual(original['code'], 'challenged')

    def test_generated_map_exposes_relations_and_does_not_invert_evidence(self):
        values = joint.validate()
        before = deepcopy(values)
        rendered = joint.generate(*values)
        self.assertEqual(values, before)
        self.assertIn('Assumption assessment (not safeguard rating)', rendered)
        self.assertIn('does not establish the effectiveness of any particular safeguard', rendered)
        self.assertIn('No assessment is inverted', rendered)
        for link in values[1]['links']:
            with self.subTest(link=link['id']):
                rows = [line for line in rendered.splitlines()
                        if line.startswith('| `' + link['commitment_id'] + '` |')
                        and '| `' + link['assumption_id'] + '` ' in line]
                self.assertEqual(len(rows), 1)
                self.assertIn('(`' + link['relationship'] + '`)', rows[0])
                self.assertIn(joint.cell(link['rationale']), rows[0])
                if link['assumption_id'] == 'defense_persistence':
                    assumption = next(a for a in values[3]['assumptions'] if a['id'] == 'defense_persistence')
                    latest = joint.latest_assessment(assumption)
                    self.assertIn(f"**{latest['code']}** as of {latest['as_of']}", rows[0])

    def test_validator_rejects_missing_invalid_and_unversioned_relations(self):
        baseline = joint.load(joint.LINKS_PATH)
        original_load = joint.load
        for label, value in [('missing', None), ('unknown', 'policy_proves_effective'),
                             ('opposite meaning', 'safeguard_effective'), ('wrong type', [])]:
            with self.subTest(case=label):
                changed = deepcopy(baseline)
                if value is None:
                    changed['links'][0].pop('relationship')
                else:
                    changed['links'][0]['relationship'] = value
                with patch.object(joint, 'load', side_effect=lambda p: changed if p == joint.LINKS_PATH else original_load(p)):
                    with self.assertRaisesRegex(joint.ValidationError, 'invalid relationship'):
                        joint.validate()
        changed = deepcopy(baseline)
        changed['schema_version'] = 'cyber-dataset-links-v1'
        with patch.object(joint, 'load', side_effect=lambda p: changed if p == joint.LINKS_PATH else original_load(p)):
            with self.assertRaisesRegex(joint.ValidationError, 'unsupported schema_version'):
                joint.validate()

    def test_every_declared_relation_is_valid_and_rationales_are_not_truncated(self):
        baseline = joint.load(joint.LINKS_PATH)
        original_load = joint.load
        for relation in joint.ALLOWED_RELATIONSHIPS:
            with self.subTest(relationship=relation):
                changed = deepcopy(baseline)
                changed['links'][0]['relationship'] = relation
                with patch.object(joint, 'load', side_effect=lambda p: changed if p == joint.LINKS_PATH else original_load(p)):
                    self.assertEqual(joint.validate()[1]['links'][0]['relationship'], relation)
        rationale = 'x' * 250 + ' | no control-specific effectiveness inference'
        self.assertEqual(joint.cell(rationale), rationale.replace('|', '\\|'))


if __name__ == '__main__':
    unittest.main()
