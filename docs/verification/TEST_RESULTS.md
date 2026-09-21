# Test results and verification limits

Reviewed: **2026-09-21**

This page summarizes selected public verification evidence. It does not certify profitability, live readiness or a globally clean private test suite.

## Recent focused verification

Recent project work reported focused green checks including:

- Canonical Learning → CONTEXT_V2 selector focused validation: **75 PASS**
- Research Forward runtime composition hashes: **35/35 PASS**
- Research Forward strategy count at the accepted runtime proof: **170 / 170**, 0 duplicates
- Research Forward hash proof: **PASS**
- focused Context V2 regression checks around the runtime-composition repair: PASS
- Python compilation at that repair checkpoint: PASS
- supervisor smoke state at that repair checkpoint: RUNNING

The latest browser/runtime proof used WebUI **90.8.10.199**.

## Training evidence is separate from test evidence

The ENA full-history one-coin pilot completed technically, but its model-quality result remained:

- Rule vs ML: **DEGRADED**
- candidate eligibility: false
- Challenger promotion: no

A green software test does not turn a degraded scientific result into a successful model.

## Runtime proof is separate from source-code proof

AlgoSphere now treats these as different layers of evidence:

- source/file state
- relevant SHA / composition identity
- running process
- served API/UI state
- browser-visible projection
- prospective outcome evidence

A code edit on disk is therefore not described as active runtime behavior until the relevant runtime proof agrees.

## Full-suite boundary

The public documentation does **not** currently claim that every private application test is globally green.

Older full-suite checkpoints and older runtime blockers remain historical evidence, but they are not used as the current project status when later targeted proof has superseded them.

## Publication verification

The public repository includes a small standard-library verifier for the documentation/evidence export.

That verifier checks public-file boundaries, common privacy/secret patterns, local Markdown links, language counterlinks and export-manifest integrity when used on a staged export.

It does not execute the private trading application.

[Current status](../../CURRENT_STATUS.md) · [September 21 update](../../updates/2026-09-21-public-status.md) · [Roadmap](../progress/ROADMAP.md)
