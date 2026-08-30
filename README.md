# AlgoSphere

**Building an auditable crypto-ML research and trading system with human judgement and AI-assisted development tools.**

AlgoSphere is an independent research and engineering project focused on a difficult practical question: how can a machine-learning trading workflow produce decisions that remain consistent from research and backtesting through paper, shadow and eventually live execution?

This repository is the public, sanitised project record. It documents progress, verification evidence, failures and open blockers. The proprietary trading code, credentials, market data, models and strategy parameters are not published here.

## Current status — 30 August 2026

| Area | Status |
|---|---|
| Canonical-history integrity | **Pass** |
| Paper-watch guard | **Pass** |
| Runtime entry-snapshot contract | **Blocked — incomplete v3 context** |
| Remaining scoped context failures | **7** |
| Research profile | `QUICK` |
| Research activation | **Disabled** |
| Eligible experiments | **0** |
| Promotion / live readiness | **Not claimed** |

Presence of snapshots for closed paper trades was reported at 100%, but seven scoped cases do not yet satisfy the complete v3 context contract. That distinction is one of the reasons AlgoSphere remains fail-closed.

Read the [full current status](CURRENT_STATUS.md), [latest QA evidence](TEST_RESULTS.md) and [open blockers](ROADMAP.md).

## What we are working toward

- One traceable decision path across research, paper, shadow and live modes.
- Chronological walk-forward evaluation without look-ahead leakage.
- Explicit evidence for data cut-offs, feature versions, eligibility decisions and exit-state transitions.
- Realistic treatment of fees, spread, slippage, latency and exchange constraints.
- Fail-closed promotion gates: missing or contradictory evidence blocks activation.
- Public documentation of both successful checks and failed hypotheses.

## What this repository does not claim

- No profitable model has been proven by this public status package.
- AlgoSphere is not represented as ready for live trading.
- Nothing here is financial or investment advice.
- No return, delivery date or successful project outcome is promised.

## Build in public

Public updates live in [`updates/`](updates/). The supporting evidence summary covers 1,487 discovered Build, Delivery, QA, Test and other report artifacts. Raw reports and file-level metadata remain private because they may contain proprietary research, market information or personal history.

Development uses OpenAI Codex and ChatGPT as development, review and documentation tools. AlgoSphere is an independent project and is not affiliated with or endorsed by OpenAI.

## Public communication

GitHub is the source of truth for technical status and evidence. A read-only Telegram announcement channel may mirror short progress updates and link back to the corresponding GitHub update.

## Support

AlgoSphere is currently self-funded. [Voluntary project support is available through GitHub Sponsors](https://github.com/sponsors/1545Christian) and helps cover development time, testing infrastructure, market-data tooling, security reviews and public technical documentation.

Support is voluntary. It is not an investment and provides no ownership, profit participation, repayment, financial return, trading signals, investment advice, services, exclusive access or guaranteed project outcome.

## Project owner

Maintained by [1545Christian](https://github.com/1545Christian).

## Copyright and reuse

Copyright © 2026 Christian Heftenberger. All rights reserved.

No open-source or documentation licence is granted at this stage. GitHub's platform terms still permit the limited uses needed to display and fork public repository content through GitHub. Any source code published later will receive a separate, explicitly selected software licence after review.
