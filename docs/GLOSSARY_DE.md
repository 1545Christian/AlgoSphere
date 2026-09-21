# AlgoSphere Glossar

AlgoSphere verwendet einige projektinterne Begriffe immer wieder. Hier steht die kurze öffentliche Bedeutung, ohne private Implementierungsdetails offenzulegen.

| Begriff | Bedeutung |
|---|---|
| **Rule Baseline** | Deterministische Strategie/Referenz als fairer Vergleich, bevor ML-Uplift behauptet wird. |
| **ML Selector** | ML-Schicht zur Bewertung/Auswahl von Kandidaten; ersetzt die Rule-Baseline nicht automatisch. |
| **OOS** | Out-of-Sample-Evidence: Daten, die nicht zum Fitten des bewerteten Modells verwendet wurden. |
| **Walk-forward** | Zeitlich geordnete Evaluation: auf früheren Daten trainieren, auf späteren Daten prüfen. |
| **Market State** | Kausale Beschreibung der Marktumgebung, z. B. Range, Trend, Transition oder Volatility Expansion. |
| **CURRENT** | Kontrollvariante für den Vergleich. |
| **CONTEXT_V2** | Shadow-Research-Variante mit zusätzlichem Context und Canonical-Learning-Delta-Evidence. |
| **Shadow** | Paralleler Research-Pfad, der beobachtet/entscheidet, ohne als aktiver Live-Pfad zu gelten. |
| **Paper** | Simuliertes Trading/Validierung ohne Echtgeld. |
| **Research Watch** | No-Capital-Research-Pfad zum Beobachten von Kandidaten und Outcomes. |
| **Research Forward** | Prospektiver Research an neuen Markt-Events statt nur historischem Replay. |
| **NO_TRADE** | Explizite Entscheidung, dass Setup/Evidence keinen Entry rechtfertigt. |
| **Canonical Memory** | Gemeinsame Evidence-Schicht, die Decisions, Outcomes und Learning mit stabiler Identity/Provenienz verbindet. |
| **Learning Contribution** | Evidence aus einem eligible, abgeschlossenen Outcome vor der Aggregation. |
| **Learning Delta** | Daraus entstehende Evidence-Änderung, die spätere Bewertung/Selektion beeinflussen kann. |
| **Candidate** | Eligibility-/Artifact-Metadatum, keine eigene Lifecycle-Stufe. |
| **Challenger** | Strategie/Modell, das die nötigen Research-Gates passiert hat und kontrolliert weiter verglichen werden darf. |
| **Champion** | Spätere Lifecycle-Stufe einer ausreichend bewiesenen aktiven Referenz; nicht einfach „das neueste Modell“. |
| **Robustness Gate** | Evidence-Prüfungen über Folds, Recent OOS, States, Horizonte, Kosten, Calibration, Tail Risk und Support vor Promotion. |
| **Runtime Proof** | Evidence, dass der beabsichtigte Code/Contract wirklich im laufenden Prozess aktiv ist und nicht nur auf Disk liegt. |
| **Prospektiver Proof** | Evidence an natürlich eintreffenden Events nach einer Änderung statt nur historisch rekonstruierter Nachweis. |
| **Demo Connected** | Zukünftige verbundene Demo-Umgebung; ausdrücklich nicht dasselbe wie Live-Trading. |
| **Live** | Echte Execution mit echten Berechtigungen/Echtgeld. Laut aktuellem öffentlichen Status deaktiviert. |

Wenn ein datiertes historisches Dokument einen Begriff für seinen damaligen Stand anders verwendet, sollte dies dort ausdrücklich erklärt sein.

Siehe [Hier anfangen](START_HERE_DE.md) und [Architekturüberblick](project/ARCHITECTURE_OVERVIEW_DE.md).
