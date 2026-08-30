# Security and disclosure boundary

This public repository intentionally excludes:

- source code and proprietary strategy logic;
- credentials, API keys, private keys, wallet details and environment files;
- databases, models, market data and raw runtime logs;
- personal trading history and instrument-level configuration;
- raw QA, Build, Test and Delivery reports.

The source public-status package reports that high-risk secret-pattern scans were run over staged files and ZIP entries. The package was independently checked after upload for archive integrity, declared checksums, sequential register IDs, valid timestamps and common high-risk secret patterns. Only aggregated report counts are published; file-level timestamps and sizes remain private.

Security concerns should not be posted with live credentials or exploitable private details. A private reporting channel will be added before any public code component is released.
