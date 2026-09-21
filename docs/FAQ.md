# AlgoSphere FAQ

A short, plain-language answer to the questions that come up most often around the project.

## What is AlgoSphere?

AlgoSphere is an independent AI × Quant research and engineering project for crypto markets.

The project explores how market context, rules, machine learning, OpenAI-assisted analysis, canonical memory and Paper/Shadow execution can be combined in a way that is measurable and auditable.

It is not presented as a finished trading product.

## Is AlgoSphere live trading with real money?

No.

The current public status remains:

- Live trading: disabled
- Real capital: 0
- Automatic model promotion: disabled

Paper and Shadow paths are used for research and validation.

## Is this a signal service?

No.

The public repository and Telegram channel document research and development progress. They are not a trading-signal service and do not provide investment advice.

## Is the full source code public?

No.

This repository is the public documentation and evidence layer.

Private application source code, credentials, account configuration, market databases, trained models and proprietary strategy parameters are not published here.

## Does the machine learning already beat the rule-based system?

Not proven.

The latest ENA one-coin pilot completed technically, but the ML selector performed worse than the preserved Rule baseline. It was therefore not promoted.

That negative result is intentionally kept visible.

## What is CURRENT vs CONTEXT_V2?

CURRENT is the control path.

CONTEXT_V2 is a Shadow research variant that can use market-state context and Canonical Learning Delta evidence when evaluating strategy candidates.

The two are kept separate so they can be compared without silently mixing evidence.

## Is CONTEXT_V2 better?

Not proven yet.

There is not enough natural, comparable settled evidence to make that claim.

## What does “Canonical Memory” mean here?

It is the project’s common evidence layer for connecting decisions, trades, outcomes and learning.

The goal is to preserve enough identity and provenance to answer questions such as:

- Which decision produced this trade?
- What market state and strategy were involved?
- What happened after entry?
- What did the system learn from the outcome?
- Did that evidence change later selection?

## What role does OpenAI have?

OpenAI is used as an independent analysis layer inside the AI-only research path.

Within that lane, a valid OpenAI plan is not supposed to be re-decided by a second local trading engine.

OpenAI decision quality and profitability are still not proven.

## Why are failed or negative results published?

Because a research system is not useful if it only preserves good-looking results.

FAILED_OOS, insufficient evidence, degraded ML results and unresolved limitations are part of the project record.

## What is the Demo / Packaging / Release track?

It is a separate future workstream for turning parts of AlgoSphere into a controlled demo/client experience.

Demo does not mean Live.

The project still needs clear Offline/Connected Demo isolation, approved model bundles, Demo/Testnet end-to-end proof, installer/update/rollback handling, secure credentials and release integrity before a release can be called ready.

## Can I contribute?

Feedback, reproducible bug reports, research questions and documentation corrections are welcome.

Please read [CONTRIBUTING.md](../CONTRIBUTING.md) before opening an issue.

## Where should I start?

- [README](../README.md)
- [Current Status](../CURRENT_STATUS.md)
- [Latest Update](../updates/2026-09-21-public-status.md)
- [Roadmap](progress/ROADMAP.md)
- [Evidence Summary](../evidence/EVIDENCE_SUMMARY.md)
