# Documented engineering work

Items below are dated, reviewed engineering results. They are not claims of profitability, release readiness or global end-to-end closure.

## September 19–20 — latest reviewed engineering state

### Research Forward runtime composition

- Scientific overlay is now bound before VisiblePaperEngine creation.
- Runtime composition receipt added.
- Composition hashes: 35/35 PASS.
- Research Forward hash proof: PASS.
- 170 strategies active, 0 duplicates.
- CURRENT remained unchanged.
- WebUI proof used v90.8.10.199.
- Settled snapshot at proof time: CURRENT 19 / -2.05 USDT; CONTEXT_V2 13 / -0.79 USDT.
- No selector-uplift claim was made from these small populations.

### Canonical Memory core

- Current Canonical Memory / new-write contract reported PROVEN_CLOSED.
- Provenance, readable evidence, no-parallel-truth and Before→Delta→After trace are part of the current path.
- The earlier SQLite-lock report was superseded by a later successful scoped backfill commit and targeted repair.
- PAPER/CURRENT 17/17 exact Outcome→Contribution→Delta chains repaired.
- State fields repaired where exact evidence existed: 1,483 PAPER/CURRENT rows and 10 PAPER/CONTEXT_V2 rows.
- Targeted integrity check passed.
- 1,739 UNVERSIONED and 74 no-evidence legacy gaps remain intentionally unresolved rather than synthesized.

### CONTEXT_V2 learning

- Existing selector connected to Canonical Learning Delta.
- Variant-safe matching by coin, side, strategy family and market state.
- CURRENT remains the control path.
- Counterfactual/NO_TRADE evidence is not treated as executed-trade evidence.
- Technical contract is implemented; trading uplift remains insufficiently evidenced.

### Research handoff

- normalize_report() future projection now preserves compact Candidate / Rule / Nested-Fold / Contract evidence.
- Full active_strategies payload is not copied into Canonical Memory.
- Natural-run proof remains pending: AWAITING_REAL_RUN.

### Research storage and retention

- Future active-strategy snapshot writer no longer stores decoded fields plus duplicate *_json aliases.
- Representative estimate: ~49% smaller future large snapshots.
- Future Summary Identity added with summary hash, schema version, evidence/archive pointers and retention metadata.
- Existing 569 historical runs left unchanged.
- Legacy compaction remains blocked: 0 proven eligible, 173 resumable, 394 missing required evidence, 2 unknown.
- No historical delete / vacuum / broad migration authorized.

### WebUI

- CURRENT / CONTEXT_V2 separation stabilized.
- Variant/filter/scroll state preserved across refresh.
- Shared compact table contract and tooltips.
- Local IP and configured aliases served the same accepted build at proof time.
- Latest runtime proof used WebUI 90.8.10.199.
- Broader information-architecture cleanup remains open.

### Demo / Packaging / Release

No public/client Demo release is claimed.

The Demo track remains explicitly open for:

- Offline / Connected isolation
- signed approved model bundle
- Demo/Testnet E2E
- reconnect/recovery proof
- product-ready client surface
- installer/update/rollback
- secure credentials
- read-only permission enforcement
- release integrity and legal/distribution packaging

Demo work remains separate from Live readiness.

## September 18

See the [September 18 public update](../../updates/2026-09-18-public-status.md) for the ENA one-coin pilot, Robustness Gate, Research Forward Context V2 activation and OpenAI input-contract work.

## Safety / interpretation

A green focused test suite proves the tested contract, not profitability.

A completed training run proves technical execution, not model quality.

A working Demo component would not by itself prove Live readiness.

Negative and insufficient evidence is intentionally retained.

[Current status](../../CURRENT_STATUS.md) · [Outstanding work](ROADMAP.md) · [September 21 update](../../updates/2026-09-21-public-status.md)