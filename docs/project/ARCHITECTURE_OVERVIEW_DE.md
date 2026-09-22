# Architekturüberblick

Dies ist eine öffentliche, bewusst grobe Übersicht darüber, wie AlgoSphere zusammenspielen soll. Sie beschreibt die Research-Architektur, ohne privaten Anwendungscode, proprietäre Strategieparameter oder Deployment-Details zu veröffentlichen.

## Der Hauptkreislauf

```text
Marktdaten
   ↓
Market Context / State / Struktur
   ↓
Research-Kandidaten
   ↓
Decision-Lanes
   ↓
Paper / Shadow / Research Outcomes
   ↓
Canonical Memory
   ↓
Learning Delta
   ↓
Revalidierung / Lifecycle
   ↺
```

Entscheidend ist der Kreislauf: Eine spätere Entscheidung soll auf die Evidence zurückgeführt werden können, die sie beeinflusst hat.

## 1. Marktinputs

AlgoSphere arbeitet mit Marktinformationen über mehrere Horizonte.

Die öffentliche Dokumentation trennt zwischen:

- Execution Truth zur Outcome-Messung
- Context/Features für Analyse
- breiterem Marktumfeld wie BTC/ETH, Struktur, Volatilität und News, soweit relevant

Future Information soll nicht so behandelt werden, als wäre sie zum Decision-Zeitpunkt bereits bekannt gewesen.

## 2. Marktverständnis

Bevor eine Strategie oder ein Modell bewertet wird, versucht AlgoSphere die Marktumgebung zu beschreiben.

Dazu gehören beispielsweise:

- Range- vs Trend-Verhalten
- Richtung / Market State
- Transition / Volatility Expansion / Shock
- Support/Resistance und Struktur
- Multi-Timeframe-Kontext

Ziel ist nicht anzunehmen, dass eine Strategie in jeder Marktphase gleich gut funktioniert.

## 3. Rule- und ML-Research

Rule-Evidence bleibt getrennt von der ML-Research-Performance erhalten. Exaktes Selector-Design, Feature-Sets und Scoring-Logik bleiben privat.

ML soll einen echten Mehrwert gegenüber einer nachvollziehbaren Baseline beweisen müssen und nicht allein deshalb übernehmen, weil es moderner ist.

Der öffentliche Lifecycle lautet:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

Ein Kandidat darf scheitern, unklar bleiben oder ohne Promotion erhalten werden.

## 4. Decision-Lanes

AlgoSphere trennt unterschiedliche Decision-Populationen bewusst.

Beispiele im aktuellen öffentlichen Stand:

- Paper
- Research Watch / Forward
- Trade Like Che CURRENT
- Trade Like Che CONTEXT_V2 Shadow
- OpenAI AI-only
- Counterfactual Evidence

Diese Lanes werden nicht still vermischt, weil ihre Entscheidungen unter unterschiedlichen Verträgen entstehen können.

## 5. Canonical Memory

Canonical Memory ist die gemeinsame Evidence-Schicht:

`Decision → Trade / NO_TRADE → Outcome → Learning`

Sie soll Identity und Provenienz so erhalten, dass später nachvollziehbar bleibt:

- welche Decision zu welchem Outcome führte
- welche Strategie, Side und Marktphase beteiligt waren
- was nach dem Entry geschah
- welche Evidence daraus gelernt wurde
- ob spätere Selektion tatsächlich verändert wurde

## 6. Learning und Anpassung

Der beabsichtigte Lernkreislauf ist kontrolliert:

`neue Evidence → Evaluation → Revalidierung → Lifecycle-Entscheidung`

Learning darf spätere Strategieauswahl beeinflussen. Promotion und Execution-Berechtigungen bleiben trotzdem separat geregelt.

## 7. Paper / Shadow vor Live

Paper- und Shadow-Pfade sammeln prospektive Evidence, ohne Research-Erfolg mit Live-Readiness gleichzusetzen.

Ein technisches PASS ist nicht automatisch:

- wissenschaftlicher Uplift
- robuste Profitabilität
- Release-Readiness
- sichere Live-Ausführung

Dafür braucht es jeweils eigene Evidence.

## 8. Demo und spätere Execution

Demo / Packaging / Release ist ein eigener Arbeitsbereich.

Eine spätere Connected Demo ist weiterhin kein Live-Trading. Ein öffentliches/clientseitiges Paket braucht eigene Regeln für:

- Berechtigungen
- freigegebenes Modellpaket
- Konfiguration
- Reconnect/Recovery
- Integrity/Update/Rollback
- Schutz von Credentials

Normal-Futures-Live-Readiness bleibt spätere Arbeit. Elite/UTA bleibt bis nach stabilem Normal Futures zurückgestellt.

## Warum diese Architektur?

AlgoSphere soll eine schwierigere Frage beantworten als nur „kann ein Modell den Preis vorhersagen?“

Die eigentliche Frage ist:

> Was funktioniert wo und unter welchen Bedingungen, mit welcher Evidence — und wann ist Nicht-Handeln die bessere Entscheidung?

Dafür müssen auch gescheiterte Experimente erhalten, Populationen getrennt und Learning-Wege nachvollziehbar bleiben.

Siehe auch: [Projektrichtung](PROJECT_DIRECTION_DE.md) · [Aktueller Status](../../CURRENT_STATUS.md) · [Evidence-Übersicht](../../evidence/EVIDENCE_SUMMARY.md)
