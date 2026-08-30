# Current public project status

Status timestamp: `2026-08-30T16:04:31Z`

## Overall assessment

AlgoSphere has recent, scoped QA evidence and remains inside a no-capital, no-automatic-promotion safety boundary. Current research activation is disabled. This status makes no claim of profitability, live-trading readiness or promotion readiness.

## Current state

| Control | Reported state |
|---|---|
| Canonical-history integrity | **PASS** |
| Runtime entry-snapshot coverage | **FAIL_INCOMPLETE_V3_CONTEXT** |
| Closed-paper-trade snapshot presence | Reported as 100% |
| Scoped v3 context failures | **7** |
| Paper-watch guard | **PASS** |
| Research profile | `QUICK` |
| Activation allowed | `False` |
| Eligible experiments | `0` |

Snapshot presence and snapshot-contract completeness are different checks. A record may exist while still lacking required v3 context. The seven scoped failures therefore keep the related gate closed.

## Evidence inventory

- Registered report artifacts: **1,487**
- Paths reported unreadable during inventory: **10**
- Export process reported origins: `DOKUMENTATION/` 193 and `reports/` 1,294
- Categories: Build 159; Delivery 136; Other 886; QA 282; Test 24

Only aggregate inventory counts and the SHA-256 digest of the private sanitised register are published in [`evidence/EVIDENCE_SUMMARY.md`](evidence/EVIDENCE_SUMMARY.md). Filenames, paths, exact timestamps, file sizes and raw report contents remain private.

## Verification boundary

The public export contains summaries and metadata, not the proprietary application or raw evidence. No tests were re-run during creation of the public export. Results are reported as discovered in the current PC project status on 30 August 2026.
