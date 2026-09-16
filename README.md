# AlgoSphere

Independent crypto-ML research and engineering project.

Building, testing and documenting the path from research and backtesting to paper and shadow execution.

Deutsch: [README_DE.md](README_DE.md)<br>
Latest status: [CURRENT_STATUS.md](CURRENT_STATUS.md)<br>
Latest update: [English status update](updates/2026-09-17-public-status.md)<br>
Telegram: https://t.me/AlgoSphereOfficial

## What AlgoSphere is

AlgoSphere is an independent research and engineering project. The current goal is a consistent, auditable path from research and backtesting to paper/shadow execution, with clear separation between trading, research, OpenAI analysis, ML selection and evidence/memory.

## Current reviewed status

| Scope | Current state |
|---|---|
| Training | **Paused** |
| Factory / hypothesis producer | **Paused** |
| Active Paper | Running / fail-closed |
| Research Watch | Running / no-capital research path |
| Research Forward | **Runtime recovery still open because of direct Bitget socket `WinError 10013`** |
| OpenAI AI-only | V2 multi-scenario analyst active; more causal settled outcomes still needed |
| Trade memory | Unified across Paper / Watch / Research Forward / OpenAI executed trades |
| WebUI | Major projection/layout fixes completed; broad final browser audit still open |
| Live trading | **No** |
| Real capital | **0** |
| Automatic promotion | **No** |

The project remains fail-closed. No documentation change authorizes live trading or real-capital execution.

## What improved recently

- OpenAI now uses `OPENAI_AI_MARKET_ANALYST_V2` with independent multi-scenario analysis instead of inheriting local directional bias.
- A false stale-data condition was fixed: signal age is no longer supposed to be confused with underlying Futures-candle freshness.
- OpenAI paid-call cadence now distinguishes successful calls from blocked attempts.
- Open symbols are excluded from duplicate OpenAI entry analysis until close/settlement.
- Paper / Watch / Research Forward / OpenAI executed trades share one comparable memory contract.
- Unknown historical values are explicitly typed instead of silently being treated as zero.
- Trade-Like-CHE entry-price projection, ADX display, compact ID rendering, Capture projection and OpenAI NO_TRADE projection were repaired or improved.

## Current main blocker

The latest work log shows Research Forward can fail on a direct Bitget refresh with `WinError 10013` even while the central market-data loader already has fresh 1-minute Futures data.

The intended repair remains inside the existing shared reader: on direct-socket failure, use the centrally confirmed hot-file tail only after strict freshness/availability validation. This needs final restart/runtime proof before it can be called closed.

## ML lifecycle

The intended lifecycle remains:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

`candidate_eligible` is metadata/eligibility, not a separate operating stage.

Rule evidence must remain preserved independently from ML-selector success. **ML selector collapse is not Rule failure.**

## Start here

| Purpose | Document |
|---|---|
| Current state and main blockers | [CURRENT_STATUS.md](CURRENT_STATUS.md) |
| Latest reviewed update | [September 17 update](updates/2026-09-17-public-status.md) |
| Tests and verification limits | [Test results](docs/verification/TEST_RESULTS.md) |
| Open work and priorities | [Roadmap](docs/progress/ROADMAP.md) |
| Completed engineering work | [Completed work](docs/progress/COMPLETED_WORK.md) |
| Project history | [Project history](docs/project/PROJECT_HISTORY.md) |
| Evidence guide | [Evidence summary](evidence/EVIDENCE_SUMMARY.md) |

Browse all dated [updates](updates/).

## Public / private boundary

This repository is a public documentation and evidence record. It does not contain the private application source code, credentials, account configuration, market databases, models or proprietary strategy parameters.

Codex and ChatGPT support implementation, debugging, review and documentation, but AlgoSphere is intended to run independently of Codex. Runtime/trading operation must not depend on an AI coding session being present.

## Publication note

The automatic nightly publisher remains paused by the operator because its narrative source selection previously carried stale development text forward. The September 17 status is human-reviewed.

## Future use

AlgoSphere is intended to become a controlled research-to-execution system for personal use. Any future live use requires explicit human approval, complete runtime/data/risk checks and independent safeguards. Live trading is not enabled now, and no profitability or outcome is promised.

## Support and disclaimer

Short updates: [Telegram](https://t.me/AlgoSphereOfficial). Voluntary support: [GitHub Sponsors](https://github.com/sponsors/1545Christian). Sponsorship is not an investment and provides no trading signals, investment advice, ownership, return or guaranteed outcome. See the full [Disclaimer](docs/legal/DISCLAIMER.md).
