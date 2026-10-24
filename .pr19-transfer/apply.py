"""Temporary transport for the already inspected and locally tested PR19 patch."""
import base64
import hashlib
import json
import lzma
from pathlib import Path
import subprocess
import sys

BRANCH = 'cyber-history-bibliography-integration-2026-10-24'
BASE = '35dd6722c2cd7138871515754d40ead2abcd27e0'
PATCH_SHA = 'e660c078a0f6d7bdb792d97cdbbfbade7aab01333e619e49a19dbc305f490cf4'
EXPECTED = {
 '.github/workflows/pr19-review-workspace.yml': None,
 '.github/workflows/validate.yml': '4a317e9eb4fb52d76d26229a819d843bd88f8770b269021b1a89ecfe60a06494',
 'METHODS.md': '8dc4ca8c641ca9ba4760fdf8cb4187c9ab469030647f877a5b46815f1eddfc62',
 'README.md': 'f255a6f80070bfdfce153a061ac68b9c66ca5eba8c2755532fc8ae218b03522f',
 'frontier-governance-evals.bib': '9054dd8bae7d4d89cfaf6aa8c11f3ab6facec4c62295a0a71d4908ca5889db3b',
 'intake.csv': '2d133ecab378b86867f3b2c5501e738bd278fc09b1284a1da67b5499d2937c68',
 'provenance/cyber-source-capture-bundle-2026-10-24.json': 'ea04fee253b4662d0dcc5eab2dda76eb513118c22b838b5084a80ba5b83522ef',
 'provenance/source-capture.md': '53ed845344d66873770f9d1eb1523548abacf51e4cda8617f05c3c4d58d03bfa',
 'records.yaml': 'd8d8a725ea8b04dd8bec912baafca45206d377beefeedb108599b6163f6b1b3f',
 'research/cyber-deployment/README.md': 'ca8cfe48898ca6948db6b1b2a1a422b1597632acbf82ff5e14a0d6ee34bfd723',
 'research/cyber-deployment/commitment-history.md': 'd62836078559ca5789e99c4e6412dd253204a411bd8c60dc973aa5ff3c6270e7',
 'research/cyber-deployment/commitments.yaml': 'cec3d66acb3e4d173239291847a61e1677de4bf46a5c6257c4c0aef15459adc3',
 'research/cyber-deployment/dataset-links.yaml': '1e28f994d85a924c0b2667352e0b2ab80b3307d2c06494c67d4ff5e29492121a',
 'research/cyber-deployment/datasets.yaml': '89751f7762eb0b062343648598f3c544c8dc715687c7a0e9659c51cb337c9b87',
 'research/cyber-deployment/evidence.yaml': 'f7d8978789a1c5541c04d87c6fb4269616e06a245b0c4060c0e42e05bdfbfb5e',
 'research/cyber-deployment/expansion-reconciliation-2026-10-24.md': '9973a845cb67725f700f0abe40894565381bcfe8d7541c480e82d78e8024a241',
 'research/cyber-deployment/integration-audit-2026-10-24.json': 'a7799100f65642566f02e54d34ef20713537690af5dc5295ba5507e1e938c193',
 'research/cyber-deployment/longitudinal-map.md': 'ec2445e4c9bc499218ea8cf4357cf7f3df1879dd75294eda7eb9c8f0c24ca34a',
 'research/cyber-deployment/operational-risk/build.py': '902fd09dfa53e6125750e1a851a1239d020dddb7020a6472579c98e7270ff6b8',
 'research/cyber-deployment/operational-risk/evidence-map.md': '0b1a4421169e4ffa39890f322d04b819cfa0b100a40786426e21acbb9d44bd3d',
 'research/cyber-deployment/operational-risk/source-admission.yaml': '3dc7852f0aaa777cab66aa16df87577fdc3bfc7efa27a4c00c0b7c0750dc5469',
 'research/cyber-deployment/operational-risk/source-captures.yaml': 'bc868395632b8726abc4e9f6e2bbe5132ab6ad8afbd56fb7fa75b529b5771208',
 'scripts/audit_cyber_bibliography.py': '2ede4b642f0155c166532b6324da9c45420f7a95959634d9f91b61946d8fa360',
 'scripts/release.py': '1aac29d62de230ff28d8c1321ab86fcef0f3a9bb434afdb14ddf1651688fd542',
 'tests/test_cyber_integration.py': 'ed7aec57781bc09205f9029f9d9d92b6fe6e37d742ed5f74c8dea6dcad1043d7',
 'views/contextual.bib': '6283085d9a44ce8a91b93511acf41fc126c7be19f814c47a54d45b04c559e0b0',
 'views/governance-artifacts.bib': '6957730cf0b8164fdc824abcf4828deb8d8c5af02ececf8d74fdf4836e95e354',
 'views/index.md': '72faf56b6c929d54ee5268ad811cff15de116f062cb1953670bdb97d66705459',
 'views/technical-evals.bib': '74f139d1f1e93b4eca0b260310cb6b0ef25111226415865f449ba42efdbd50d1'
}

def run(*args):
    subprocess.run(args, check=True)

run('git', 'merge-base', '--is-ancestor', BASE, 'HEAD')
encoded = ''.join((Path('.pr19-transfer') / f'patch.{i:02d}').read_text().strip() for i in range(4))
payload = lzma.decompress(base64.b64decode(encoded, validate=True))
if hashlib.sha256(payload).hexdigest() != PATCH_SHA:
    raise RuntimeError('Transport patch checksum mismatch')
subprocess.run(['git', 'apply', '--check', '-'], input=payload, check=True)
subprocess.run(['git', 'apply', '-'], input=payload, check=True)
for args in [
 ['scripts/build.py'],
 ['scripts/build_commitments.py', '--write'],
 ['research/cyber-deployment/operational-risk/build.py', '--write'],
 ['scripts/build_cyber_datasets.py', '--write']
]:
    run(sys.executable, *args)
for path, expected in EXPECTED.items():
    p = Path(path)
    actual = hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
    if actual != expected:
        raise RuntimeError(f'Locally tested output differs: {path}: {actual} != {expected}')
print('All 29 changed/deleted paths match the locally tested SHA-256 inventory.', flush=True)
for args in [
 ['scripts/build.py', '--check'],
 ['scripts/lint_bibliography.py'],
 ['scripts/build_commitments.py', '--check'],
 ['research/cyber-deployment/operational-risk/build.py', '--check'],
 ['scripts/build_cyber_datasets.py', '--check'],
 ['scripts/audit_cyber_bibliography.py'],
 ['-m', 'unittest', 'discover', '-s', 'tests', '-v']
]:
    run(sys.executable, *args)
run('git', 'diff', '--check')
Path('/tmp/pr19-verified-inventory.json').write_text(json.dumps(EXPECTED, indent=2))
# Workflow changes and temporary transport deletion are finalized through the
# authenticated connector after this branch-only fast-forward push.
paths = [p for p in EXPECTED if not p.startswith('.github/')]
run('git', 'add', '--', *paths)
run('git', 'diff', '--cached', '--check')
run('git', '-c', 'user.name=github-actions[bot]', '-c', 'user.email=41898282+github-actions[bot]@users.noreply.github.com',
    'commit', '-m', 'Complete OpenAI commitment history and six-source bibliography integration')
run('git', 'push', 'origin', f'HEAD:refs/heads/{BRANCH}')
print('Integration committed and pushed; no merge or release performed.', flush=True)
