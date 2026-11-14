# Release and OSF deposit protocol

The published [v2026.10.24 release](https://github.com/madame-architect/AIsafety/releases/tag/v2026.10.24)
targets commit `1bb1672` and was published on October 25, 2026 UTC. Its receipt
records OSF object `s5ey4`, version 1, and prior verification of 63 inventory
hashes. The recorded ZIP is 4,425,513 bytes with SHA-256
`424d4970ef60516223a586be18f6717f3c06b9ca7c6ea6946e18f4e875d47f3d`.
The November 14 integration confirmed the GitHub release and receipt text,
without a fresh OSF byte verification. The [October 16 stabilization note](stabilization-2026-10-16.md)
retains the earlier unconfirmed attempt; its status does not describe this later
release.

GitHub merges do not establish OSF deposits. Each subsequent release requires
a published GitHub release at an immutable tag and a byte-matched deposit in
[OSF project 9ks5m](https://osf.io/9ks5m/), with object/version identifiers and
SHA-256/length in its manifest. New research changes are not part of the
published October 24 package until a separate release is approved and verified.

## Prepare and publish

Release preparation and publication follow the maintainer's approval of the
research scope and exact revision. The [research reconciliation](../research/synthesis/reconciliation.md)
identifies remaining evidence gaps and publication decisions; passing checks does
not resolve them. Review or local integration alone does not authorize a tag,
public branch, release or deposit.

After approval and merge, check out the exact intended commit, run the current
[build and verification commands](../README.md#build-and-verify), and choose a new
release tag. Never move a published tag. `vNEXT` is a placeholder:

```bash
python3 scripts/build.py --check
python3 scripts/build_research.py --check
python3 scripts/build_commitments.py --check
python3 -m unittest discover -s tests -v
git tag -a vNEXT -m 'Frontier AI Governance Evals vNEXT'
git push origin vNEXT
python3 scripts/release.py prepare --tag vNEXT --output-dir dist
python3 scripts/release.py verify dist/vNEXT-manifest.json
gh release create vNEXT dist/vNEXT.zip dist/vNEXT-manifest.json \
  --verify-tag --title 'Frontier AI Governance Evals vNEXT' \
  --notes 'Reviewed research revision. OSF verification pending; see the research reconciliation and manifest preservation limitations.'
python3 scripts/release.py record-github dist/vNEXT-manifest.json
gh release upload vNEXT dist/vNEXT-manifest.json --clobber
```

Preparation reads Git blobs at the tag, validates authoritative YAML and checks
generated bibliography/history bytes. The deterministic ZIP's external JSON
manifest binds the commit/tag and every payload file's SHA-256 and length,
with authoritative inputs and generated outputs identified by the release
script. It exposes legacy and unarchived snapshots; the preservation flag
concerns those snapshots, not publication readiness of the broad synthesis.
Stale outputs and mismatched checkout tooling fail
preparation. `record-github` checks the remote tag/commit, published release
ID and downloaded ZIP asset before recording release/asset IDs.

Upload the generated ZIP itself to GitHub and OSF. Do not substitute GitHub's
automatic source ZIP: its byte identity can differ. Source captures may remain
outside the ZIP when rights prevent redistribution; their provenance remains
in authoritative YAML.

## Deposit and verify OSF

1. Upload `dist/vNEXT.zip` with authorized OSF access. Include the Git commit,
   tag and payload SHA-256 in the deposit description. Retain the actual OSF
   Storage object ID and version number.
2. Verify that particular version, replacing the placeholders below:

```bash
python3 scripts/release.py record-osf dist/vNEXT-manifest.json \
  --object-id ACTUAL_OBJECT_ID --version-id ACTUAL_VERSION_NUMBER \
  --download-url 'https://files.osf.io/v1/resources/9ks5m/providers/osfstorage/ACTUAL_OBJECT_ID?version=ACTUAL_VERSION_NUMBER'
```

The command checks OSF API metadata for project, object, version and length,
downloads that specific version, and verifies the ZIP and every inventory hash.
Only then does it record `deposit_bytes_verified`, object/version IDs, API and
download URLs, verification time, SHA-256 and length. Failure leaves the manifest
unchanged. Inaccessible/private deposits require authorized access or public
release; this read-only verifier never accepts a local upload receipt as proof.

3. Upload the **updated manifest** beside the OSF payload and replace the
   GitHub manifest asset with those same bytes. Retain it in `releases/` in a
   follow-up commit. Re-download both manifest assets and compare SHA-256
   before describing the release as manifest-matched. Record the OSF manifest
   object's ID/version in the release note or a separate receipt: the manifest
   cannot hash and identify its own future upload.
4. Run `release.py verify` again. If the payload changes, use a new tag and
   deposit rather than rewriting the package's manifest.

The immutable ZIP contains tagged research state. The external manifest binds
that state and holds later publication receipts; it deliberately does not
inventory itself or change the payload after upload. OSF payload verification
is narrower than checking both manifest assets: complete step 3 before calling
the release finished. The old stabilization manifest remains historical; this
protocol does not claim its deposit occurred.

API semantics follow the official [OSF documentation](https://developer.osf.io/),
including file-version metadata and version-specific downloads. See also the
[OSF file version guidance](https://help.osf.io/article/387-files).
