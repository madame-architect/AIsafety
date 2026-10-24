"""Canonical admission, preserved byte identity and documentary-history regressions."""
from copy import deepcopy
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import audit_cyber_bibliography as audit
import build_commitments


def read(path):
    return yaml.safe_load(path.read_text(encoding='utf-8'))


class CyberIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = read(ROOT / 'records.yaml')
        directory = ROOT / audit.DIRECTORY
        cls.sources = read(directory / 'source-admission.yaml')
        cls.captures = read(directory / 'source-captures.yaml')

    def test_current_cross_file_integrity(self):
        counts = audit.audit(ROOT)
        self.assertEqual(counts['accepted_sources'], counts['canonical_sources'])
        self.assertEqual(counts['canonical_sources'], counts['operational_captures'])
        self.assertEqual(counts['legacy_uncaptured'], 2)

    def test_rejects_canonical_and_capture_corruption(self):
        cases = [
            ('missing canonical ID', lambda r,s,c: s['sources'][0].update(record_id='missing')),
            ('duplicate record', lambda r,s,c: r['records'].append(deepcopy(r['records'][0]))),
            ('duplicate source', lambda r,s,c: s['sources'].append(deepcopy(s['sources'][0]))),
            ('capture identity', lambda r,s,c: c['snapshots'][0].update(record_id='wrong')),
            ('capture version', lambda r,s,c: c['snapshots'][-1].update(version_claim='arXiv v99')),
            ('canonical version', lambda r,s,c: next(x for x in r['records'] if x['id']==s['sources'][-1]['record_id'])['fields'].update(version='arXiv v99')),
            ('missing capture', lambda r,s,c: s['sources'][0].pop('capture_id')),
            ('invalid hash', lambda r,s,c: c['snapshots'][0].update(sha256='invalid')),
            ('no canonical exception', lambda r,s,c: s['sources'][0].update(bibliography_admission='pending')),
            ('no capture explanation', lambda r,s,c: s['sources'][0].update(preservation_status='pending')),
            ('unpaired archive', lambda r,s,c: c['snapshots'][0].update(archive_checked_on=None)),
            ('path traversal', lambda r,s,c: c['snapshots'][0].update(capture_path='../outside.html')),
        ]
        for label, change in cases:
            with self.subTest(label=label):
                r,s,c = deepcopy(self.records),deepcopy(self.sources),deepcopy(self.captures)
                change(r,s,c)
                with self.assertRaises(ValueError):
                    audit.validate_documents(r,s,c,ROOT)

    def test_optional_bytes_are_required_only_in_strict_mode_and_never_ignored(self):
        payload=b'<html>retained exact bytes</html>'
        item={'id':'fixture','capture_path':'.source-captures/source.html','sha256':hashlib.sha256(payload).hexdigest(),'byte_length':len(payload),'mime_type':'text/html'}
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            self.assertFalse(audit.check_bytes(item,root,False))
            with self.assertRaisesRegex(ValueError,'missing'):
                audit.check_bytes(item,root,True)
            target=root/item['capture_path'];target.parent.mkdir();target.write_bytes(payload)
            self.assertTrue(audit.check_bytes(item,root,True))
            target.write_bytes(payload+b'changed')
            with self.assertRaisesRegex(ValueError,'mismatch'):
                audit.check_bytes(item,root,False)

    def test_openai_history_is_linked_without_backdating_clarification(self):
        snapshots, observations=build_commitments.load_history(ROOT)
        by={o['id']:o for o in observations}
        note=by['openai_cyber_internal_use_codex_clarification']
        self.assertEqual(note['previous_observation_id'],'openai_cyber_internal_use_v2')
        self.assertEqual(note['change_type'],'clarified')
        self.assertNotIn('claimed_application_on',note)
        self.assertIn('insertion/effective date',note['qualifications'])
        self.assertIn('does not repeat',by['openai_cyber_internal_use_v2']['qualifications'])
        self.assertEqual(by['openai_cyber_high_threshold_v2']['previous_observation_id'],'openai_cyber_high_threshold_beta')
        self.assertEqual(by['openai_frontier_research_containment_containment_2026']['previous_observation_id'],'openai_frontier_research_containment_pacing_2026')
        self.assertTrue(all(o['evidence_kind']=='policy_statement' for o in observations))

    def test_pending_aisi_pdf_not_promoted(self):
        source=next(s for s in self.sources['sources'] if s['source_id']=='aisi_unsanctioned_agent_incident_2026')
        self.assertEqual(source['related_unadmitted_object']['status'],'pending_full_text_review')
        self.assertTrue(source['primary_url'].endswith('cyber-testing'))
        self.assertEqual(next(c for c in self.captures['snapshots'] if c['source_id']==source['source_id'])['mime_type'],'text/html')

    def test_reports_not_misclassified_as_normative_governance(self):
        by={r['id']:r['fields'] for r in self.records['records']}
        for source in self.sources['sources']:
            fields=by[source['record_id']]
            expected='technical_eval' if source.get('arxiv_id') else 'contextual'
            self.assertEqual(fields['synthesis_stream'],expected)
            if source.get('authors'):
                self.assertEqual(fields['author'],' and '.join(source['authors']))

if __name__=='__main__':
    unittest.main()
