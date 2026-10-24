#!/usr/bin/env python3
"""One-time, fail-closed admission of inspected OpenAI Preparedness v2 provisions.

Fetches the exact official PDF, hashes the bytes, retains them locally for a CI
artifact, and only then writes authoritative history YAML and generated views.
Never fabricates archival capture or retrospective retrieval timestamps.
"""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from capture_source import capture
from source_provenance import validate
from build_commitments import check_date, check_url

URL = "https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf"
SNAP = "openai_preparedness_v2_captured_2026_10_24"
DIRECTORY = ROOT / "research/cyber-deployment"

# Source: Preparedness Framework v2 (2025-04-15), PDF viewer pages and sections to verify,
# sections 2.2, 3.1-3.3, 4.1-4.4 and 5.1.
PROVISIONS = [
    ("openai_cyber_high_threshold", "Cyber High capability threshold",
     "Cyber model removes bottlenecks to scaling cyber operations, including automated end-to-end operations against reasonably hardened targets or discovery and exploitation of operationally relevant vulnerabilities.",
     "Classify as High cybersecurity capability and require High security controls and sufficiently effective misuse safeguards before external deployment.",
     "Requirement applies to covered models assessed at the High threshold; capability assessment and safeguards sufficiency remain issuer judgments.",
     "Table 1, Cybersecurity High row, source Table 1 (verify PDF page); sections 2.2 and 4.2.",
     ["task_transfer", "incremental_uplift", "defense_persistence"]),
    ("openai_cyber_critical_threshold", "Cyber Critical capability threshold",
     "Tool-augmented model can autonomously develop functional zero-day exploits across many hardened critical systems, or execute novel end-to-end cyberattack strategies from a high-level goal.",
     "Until Critical safeguard and security-control standards are specified, halt further development.",
     "Critical denotes qualitatively new severe-harm pathways; this is a documentary requirement, not evidence that a model reached the threshold.",
     "Table 1, Cybersecurity Critical row, source Table 1 (verify PDF page); section 2.2.",
     ["workflow_autonomy", "task_transfer", "harm_mapping"]),
    ("openai_cyber_internal_use", "Cyber High internal-use safeguards",
     "High cybersecurity capability with large-scale internal deployment.",
     "Require High-standard safeguards against misalignment for large-scale internal deployment, alongside security controls.",
     "Distinct from the external misuse-safeguard condition; scope is large-scale internal deployment.",
     "Table 1, Cybersecurity High row, PDF viewer p. 6.",
     ["capability_access", "workflow_autonomy"]),
    ("openai_frontier_safeguard_review", "Frontier safeguard sufficiency and deployment decision",
     "Covered frontier model reaches High capability in a Tracked Category, including cybersecurity.",
     "Do not deploy until associated severe-harm risks are sufficiently minimized; Safety Advisory Group reviews capability and safeguard evidence and recommends action to leadership.",
     "Leadership retains decision authority; source does not independently demonstrate safeguard effectiveness.",
     "Sections 1, 2.2, 4.2 and 5.1, source sections 1, 2.2, 4.2, 5.1 (verify PDF pages).",
     ["harm_mapping", "defense_persistence"]),
    ("openai_frontier_reassessment", "Frontier capability evaluation and reassessment",
     "Covered frontier model development and deployment, with emerging capability or risk evidence.",
     "Evaluate covered models during development and before deployment, maintain scalable testing with deeper reviews, and reassess risk categories and safeguards as evidence changes.",
     "Applies within Preparedness Framework tracked categories and covered systems; no external implementation audit is implied.",
     "Sections 2.1, 3.1-3.3, 4.2 and 5.1, source sections 2.1, 3.1-3.3, 4.2, 5.1 (verify PDF pages).",
     ["task_transfer", "defense_persistence"]),
]

def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)

def main() -> None:
    evidence_path = DIRECTORY / "evidence.yaml"
    commitment_path = DIRECTORY / "commitments.yaml"
    link_path = DIRECTORY / "dataset-links.yaml"
    evidence = yaml.safe_load(evidence_path.read_text())
    commitments = yaml.safe_load(commitment_path.read_text())
    links = yaml.safe_load(link_path.read_text())
    if any(s["id"] == SNAP for s in evidence["snapshots"]):
        print("OpenAI v2 already captured; nothing to add")
        return
    payload, meta = capture(URL)
    if meta["mime_type"] != "application/pdf":
        raise ValueError("OpenAI official PDF did not return PDF bytes")
    target = ROOT / ".source-captures" / (meta["sha256"] + ".pdf")
    target.parent.mkdir(exist_ok=True)
    target.write_bytes(payload)
    snap = dict(id=SNAP, record_id="openai_preparednessv2_2025",
                source_url=URL, observed_on=meta["retrieved_at"][:10],
                inspection_scope="AI-assisted clause inspection of official v2 PDF, sections 2-5 and Table 1; not independent coding.",
                preservation_note="Exact official PDF response bytes hashed and retained as CI artifact; no independently checked archive. CI artifacts expire and are not a stable historical archive.",
                **meta, published_on="2025-04-15", version_claim="2",
                locator_basis="One-based PDF viewer pages including cover, and printed section/table headings.",
                preservation_status="captured", capture_path=target.relative_to(ROOT).as_posix(),
                archive_unavailable_reason="No independently verified permanent archive was located in this bounded pass; CI artifact is temporary.")
    validate(snap, check_date, check_url)
    evidence["snapshots"].append(snap)
    for cid, scope, trigger, action, qualification, locator, assumptions in PROVISIONS:
        commitments["observations"].append(dict(
            id=cid+"_v2", commitment_id=cid, issuer="OpenAI", snapshot_id=SNAP,
            evidence_kind="policy_statement", modality="requirement",
            scope=scope, trigger=trigger, action=action, qualifications=qualification,
            locator=locator, change_type="observed",
            source_rationale="OpenAI's stated Preparedness Framework risk-control rationale; not independently verified implementation."))
        for assumption in assumptions:
            links["links"].append(dict(
                id=cid+"_to_"+assumption, commitment_id=cid,
                commitment_observation_ids=[cid+"_v2"], assumption_id=assumption,
                relationship="policy_depends_on",
                rationale="The documented policy provision relies on this benchmark-to-operational-risk assumption; linkage is analytical, not causal attribution."))
    evidence_path.write_text(yaml.safe_dump(evidence, sort_keys=False, allow_unicode=True))
    commitment_path.write_text(yaml.safe_dump(commitments, sort_keys=False, allow_unicode=True))
    link_path.write_text(yaml.safe_dump(links, sort_keys=False, allow_unicode=True))
    run("scripts/build_commitments.py", "--write")
    run("scripts/build_cyber_datasets.py", "--write")
    run("scripts/build.py", "--check")
    run("research/cyber-deployment/operational-risk/build.py", "--check")
    run("scripts/build_commitments.py", "--check")
    run("scripts/build_cyber_datasets.py", "--check")
    run("-m", "unittest", "discover", "-s", "tests", "-v")
    print("Admitted 5 OpenAI v2 provisions with exact-byte source provenance and regenerated history.")

if __name__ == "__main__":
    main()
