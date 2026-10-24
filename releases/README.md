# Release and OSF deposit protocol

GitHub merges do not establish OSF deposits. The next release requires a
published GitHub release at an immutable tag and a byte-matched deposit in
[OSF project 9ks5m](https://osf.io/9ks5m/), with object/version identifiers and
SHA-256/length in its manifest. **OSF synchronization remains unconfirmed**.
A 2026-10-24 access attempt could not inspect the live OSF page or file listing;
no upload was performed.

## Prepare and publish

After merge, check out the exact intended commit, run the builds/tests and
choose a new release tag. Never move a published tag. `vNEXT` is a placeholder:

```bash
python3 scripts/build.py --check
python3 scripts/build_commitments.py --check
python3 -m unittest discover -s tests -v
git tag -a vNEXT -m 'Frontier AI Governance Evals vNEXT'
git push origin vNEXT
python3 scripts/release.py prepare --tag vNEXT --output-dir dist
python3 scripts/release.py verify dist/vNEXT-manifest.json
gh release create vNEXT dist/vNEXT.zip dist/vNEXT-manifest.json \
  --verify-tag --title 'Frontier AI Governance Evals vNEXT' \
  --notes 'Documentary research pilot. OSF verification pending; see manifest preservation limitations.'
python3 scripts/release.py record-github dist/vNEXT-manifest.json
gh release upload vNEXT dist/vNEXT-manifest.json --clobber
```

Preparation reads Git blobs at the tag, validates authoritative YAML and checks
generated bibliography/history bytes. The deterministic ZIP's external JSON
manifest binds the commit/tag, every payload file's SHA-256 and length, all
three authoritative YAML files and six generated outputs. It exposes legacy
and unarchived snapshots and does not call this pilot longitudinally ready
while those gaps remain. Stale outputs and mismatched checkout tooling fail
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
