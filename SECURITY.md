# Security and disclosure boundary

## Public / private boundary

AlgoSphere's public repository is intentionally limited to documentation, selected evidence exports and small verification tooling.

It does not publish:

- private application/runtime source code
- credentials, API keys or account configuration
- wallet or exchange account information
- private databases or raw operational logs
- trained private model bundles/checkpoints
- proprietary strategy parameters
- private deployment paths or infrastructure details

## Public repository checks

The repository contains a small standard-library verifier under `tools/verify_public_export.py`.

Two checks are intentionally separated:

- **live repository checks** cover the current public file boundary, common privacy/secret patterns, local Markdown links, language counterlinks and repository structure
- **staged export checks** additionally verify the SHA-256 export manifest and exact staged bytes

The historical `evidence/EXPORT_CONTENTS.md` manifest describes the staged publication it was generated for. It is not treated as a permanent hash lock for every later documentation edit.

Automated checks reduce risk; they cannot prove that every possible sensitive inference is absent. Human review remains necessary.

## Responsible reporting

Please do not publish credentials, tokens, private keys, account data or exploitable security details in a public issue.

For a normal public documentation or tooling problem, use the structured GitHub issue forms.

For a security-sensitive problem, use GitHub Private Vulnerability Reporting if it is available for this repository. If that option is not available, do not disclose the sensitive details publicly.

## Trading and account safety

Nothing in this public repository should require exchange credentials or access to a real trading account.

A future Demo/client release, if one is published, will have its own explicit permission, credential and release-integrity boundaries.
