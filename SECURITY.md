# Security and disclosure boundary

<!-- HUMAN_TEXT_START -->

## Excluded material

Public documentation excludes private source code, credentials, environment files, private configuration, wallet or account information, databases, market data, models, checkpoints, strategy materials, internal paths, personal data and raw private logs.

## Export checks and their limits

The export uses a fixed allowlist and scans staged public files for common secret, personal-data, path and prohibited-metric patterns. These automated scans reduce risk; they cannot prove that every possible secret or sensitive inference is absent. Human review remains necessary.

## Responsible reporting

Do not post credentials, tokens, private keys or exploitable details in public issues. Use GitHub Private Vulnerability Reporting if it is enabled for this repository. If it is not enabled, a secure reporting route remains an open organisational item; no email address is invented here.

<!-- HUMAN_TEXT_END -->

<!-- AUTO_VALUES_START -->
- **export verified:** fixed allowlist, ZIP inspection, hash manifest, link check and pattern scan passed.
- **not verified:** automated scanning cannot establish the absence of every possible sensitive inference.
- **not applicable:** no credential was read, stored or transmitted by this export.
<!-- AUTO_VALUES_END -->
