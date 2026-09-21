# AlgoSphere glossary

AlgoSphere uses a few project-specific terms repeatedly. This page gives the short public meaning without exposing private implementation details.

| Term | Meaning |
|---|---|
| **Rule baseline** | A deterministic strategy/reference used as a fair comparison point before claiming ML improvement. |
| **ML selector** | A machine-learning layer that helps evaluate or select candidates; it does not automatically replace the Rule baseline. |
| **OOS** | Out-of-sample evidence: data not used to fit the model being evaluated. |
| **Walk-forward** | Time-ordered evaluation that repeatedly trains on earlier data and evaluates on later data. |
| **Market State** | A causal description of the current market environment, such as range, trend, transition or volatility expansion. |
| **CURRENT** | The control variant used as the comparison path. |
| **CONTEXT_V2** | A Shadow research variant that can incorporate additional context and Canonical Learning Delta evidence. |
| **Shadow** | A parallel research path that observes/decides without being treated as the active live path. |
| **Paper** | Simulated trading/validation without real capital. |
| **Research Watch** | A no-capital research path for observing candidates and outcomes. |
| **Research Forward** | Prospective research on new market events rather than only historical replay. |
| **NO_TRADE** | An explicit decision that the available setup/evidence does not justify an entry. |
| **Canonical Memory** | The common evidence layer linking decisions, outcomes and learning with stable identity/provenance. |
| **Learning Contribution** | Evidence derived from an eligible settled outcome before aggregation. |
| **Learning Delta** | The resulting evidence change that can influence later evaluation/selection. |
| **Candidate** | Eligibility/artifact metadata, not a separate lifecycle stage. |
| **Challenger** | A strategy/model that has passed the required research gates and is eligible for controlled forward comparison. |
| **Champion** | A later lifecycle state for a sufficiently proven active reference; not simply “the newest model”. |
| **Robustness Gate** | Evidence checks across folds, recent OOS, states, horizons, costs, calibration, tail risk and support before promotion. |
| **Runtime proof** | Evidence that the intended code/contract is actually present in the running process, not only on disk. |
| **Prospective proof** | Evidence observed on naturally arriving events after a change, rather than recreated from historical data. |
| **Demo Connected** | A future connected demo environment; explicitly not the same as Live trading. |
| **Live** | Real execution with real permissions/capital. It is currently disabled in the public project status. |

If a public document uses one of these terms differently for a specific historical period, the dated document should say so.

See [Start Here](START_HERE.md) and [Architecture Overview](project/ARCHITECTURE_OVERVIEW.md).
