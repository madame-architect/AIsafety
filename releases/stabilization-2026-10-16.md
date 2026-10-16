# Stabilization release prepared for OSF

**Status checked: 2026-10-16. OSF synchronization is unconfirmed.**

The [OSF project](https://osf.io/9ks5m/) returned a scheduled-maintenance notice during the synchronization attempt. Its file list could not be compared and no files were uploaded. This is an observed availability blocker; no conclusion about the deposited version or account permissions follows from it.

## Exact release identity

| Item | Value |
|---|---|
| Reviewed release | [Merged PR #13](https://github.com/madame-architect/AIsafety/pull/13) |
| Commit | `12287bab1a763371a48660330ff9bc90a222e628` |
| Tree | `c7e5c088dd0c46142d6318369dc5fe8d6d802326` |
| Local package name | `AIsafety-stabilization-2026-10-16-12287ba.zip` |
| Package size | 652,299 bytes |
| Package SHA-256 | `025c4afc45d9b9af66096214b54010a1c92f13db9e684bc82ad7afbbdfe3ae6b` |
| Contents | 28 tracked files from that commit, including provenance |
| Manifest | [Per-file byte counts and SHA-256 digests](stabilization-2026-10-16-manifest.json) |

Each packaged file was checked byte-for-byte against the Git object at the release commit. The package excludes the later five-source verification changes and this release-status documentation.

The source can also be obtained from the [GitHub archive of the exact commit](https://github.com/madame-architect/AIsafety/archive/12287bab1a763371a48660330ff9bc90a222e628.zip). GitHub's ZIP packaging can differ from the locally prepared ZIP, so the package hash above must not be attributed to that download; compare the manifest's per-file hashes.

## Recreate the prepared package

From a checkout containing the release commit:

```bash
git archive --format=zip --prefix=AIsafety-stabilization-2026-10-16/ --output=AIsafety-stabilization-2026-10-16-12287ba.zip 12287bab1a763371a48660330ff9bc90a222e628
```

The recorded byte count and package hash describe the package actually prepared on the check date. When recreating it with a different Git version, validate the extracted files against the manifest even if ZIP-container bytes differ.

## Complete synchronization when access resumes

Compare OSF's actual files with this release before uploading. Deposit the exact package as a versioned release, preserving any previous deposit, and record the full Git commit in its description. Then verify the uploaded/downloaded bytes and record the OSF file or version URL. Change the status to synchronized only after that comparison succeeds. The absence of an OSF confirmation does not block drafting the research synthesis.
