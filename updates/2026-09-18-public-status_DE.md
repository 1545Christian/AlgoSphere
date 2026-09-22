# Öffentliches Status-Update — 2026-09-18

English: [Public status update](./2026-09-18-public-status.md)

## Zusammenfassung

Am 18. September wurden mehrere Punkte geschlossen, die im öffentlichen Stand vom 17. September noch offen waren.

Die wichtigsten Änderungen:

- Trade Like Che Context V2 ist jetzt im Research-Forward-Shadow aktiv; der neue Vertrag mit 34 Auswertungen je Coin wurde mit 170/170 bestätigt.
- Paper Context V2 Shadow blieb aktiv und wurde durch die Research-Forward-Aktivierung nicht unterbrochen.
- Die WebUI fasst offene Paper-, Watch-, Research-Forward- und OpenAI-Positionen jetzt gemeinsam unter „Offen“ zusammen und lädt deutlich weniger Daten in der Übersicht.
- Research & Modelle besitzt jetzt eine echte, operator-gesteuerte Trainingsoberfläche statt nur einer Statusanzeige.
- Ein Full-History-ENA-1-Coin-Pilot wurde vollständig ausgeführt. Das ML-Ergebnis war gegenüber der Rule-Baseline **DEGRADED** und wurde korrekt nicht promotet.
- Der read-only Market-Intelligence-Robustness-Gate ist implementiert und bleibt evidenzgesteuert.
- OpenAI AI-only erhält jetzt den zuvor fehlenden 3D-/7D-Kontext, explizite Structure-/Support-Resistance-Daten und Open-Position-Context.
- Der OpenAI-Request wird aktuell kompakter aufgebaut, weil der letzte gemessene vollständige Request unnötig groß war. Dieser Umbau ist **noch nicht im Forward-Betrieb bewiesen**.
- Der Legacy-Audit fand keinen alten Pflichtbaustein, der den ENA-Pilot blockiert. Einige sinnvolle Alt-Fähigkeiten sind im aktuellen System aber nur teilweise abgedeckt.

Live-Trading bleibt deaktiviert. Echtgeld bleibt 0. Automatische Promotion bleibt deaktiviert.

## Research Forward / Trade Like Che Context V2

Context V2 ist jetzt im Runtime-Vertrag aktiv.

Der aktuelle Shadow-Vertrag ist aktiv und hat den Health Check bestanden. Exakte Auswertungszahlen pro Markt und Größen der aktiven Population werden bewusst nicht veröffentlicht.


Health Check: **PASS**

Frische Context-V2-Shadow-Decisions sind in der WebUI sichtbar, einschließlich expliziter `NO_TRADE / NO_CURRENT_SETUP`-Evidence. CURRENT und CONTEXT_V2 bleiben in der Runtime-Projektion getrennt.

Für die Aktivierung wurden nur Supervisor und Research Forward minimal neu geladen. Paper Context V2, Point13, OpenAI und Market Data liefen weiter.

## WebUI und Operator-Nutzbarkeit

Eine größere Projektions- und Performance-Reparatur wurde abgeschlossen.

„Offen“ enthält jetzt offene Positionen aus:

- Paper
- Watch
- Research Forward
- OpenAI

Beim Browser-Checkpoint waren die geprüften Open-Position-Ansichten über die relevanten simulierten Lanes konsistent. Exakte Positionszahlen werden bewusst nicht veröffentlicht.

Overview-Payload und Ladepfad wurden deutlich reduziert. Exakte Zeiten, Byte-Größen und Prozentwerte werden bewusst nicht veröffentlicht.


Umfangreiche Rohbelege werden jetzt erst auf Detailseiten geladen.

Die Gesamtstruktur der WebUI bleibt teilweise zu dicht und soll später weiter vereinfacht werden. Die konkreten Fehler bei fehlenden offenen Positionen wurden jedoch repariert.

## Market Intelligence und ENA-Pilot

Der Market-Intelligence-Pfad bewertet mehrere Feature-Gruppen, Modellfamilien und Horizonte unter kausaler OOS-Auswertung bei erhaltener Rule-Baseline. Exakte Modellfamilien, Feature-Gruppen-Anzahlen und Horizon-Anzahlen werden bewusst nicht veröffentlicht.


Der explizite Single-Market-Pilot wurde mit Full-History-Readiness, kausaler OOS-Auswertung und vergleichbarer Rule-/ML-Basis abgeschlossen. Exakte Zeilenzahlen, Architekturanzahlen, Horizonte, Folds und Registry-IDs werden bewusst nicht veröffentlicht.


Das fachliche Ergebnis wird bewusst nicht als Erfolg dargestellt:

`RULE_VS_ML = DEGRADED`

Daher:

- `candidate_eligible = false`
- Challenger-Eligibility = false
- Promotion = nicht erlaubt
- Rule-Artefakt bleibt erhalten

Das ist ein wichtiger Fortschritt der Pipeline: Ein technisch abgeschlossener ML-Lauf wird nicht automatisch als gutes Modell behandelt.

## Robustness Gate

Zwischen OOS-Candidate und späterer Challenger-Eligibility existiert jetzt ein versionierter read-only Robustness Gate.

Er bewertet u. a. Multi-Fold-Walk-Forward, Recent OOS, Coin-/State-/Horizon-/Feature-Stabilität, Cost Stress, Calibration, Tail Risk und Sample Support. Optionale Dimensionen sind kleine kontrollierte Ablationen, Parameter-Nachbarschaft und Daten-Perturbation.

Es gibt keine automatische Promotion.

Der neue Full-History-Single-Market-Pilot muss nun gegen diesen Gate ausgewertet werden. Ein abgeschlossener Trainingslauf ist nicht automatisch `ROBUST_OOS_READY`.

## Canonical Memory und Lifecycle

Die Kette

`Decision → Trade → Outcome → Canonical Memory → Learning → Lifecycle`

ist weitgehend vorhanden, aber noch nicht vollständig geschlossen.

Der Audit zeigte weiterhin:

- historische Decision→Trade-Verknüpfung ist bei einem Teil älterer Outcomes unvollständig
- Memory→Learning arbeitet nur auf eligible Evidence
- ein konkretes Learning-Delta je Trade fehlt in der UI
- CURRENT und CONTEXT_V2 sind in der Runtime getrennt, im Canonical Memory aber noch nicht vollständig
- historische Promotion-Persistenz ist nur teilweise vorhanden
- Challenger ist noch kein aktiv genutzter operativer Promotion-State
- Champion ist derzeit überwiegend ein eingefrorener Paper-Fallback und kein neu promotetes Modell

Paper bleibt simuliert. Es existiert kein Echtgeld-Champion.

## Legacy-Audit

Der ältere Preisvorhersage-/AlgoSphere-Bestand und historische Evidence wurden gegen den aktuellen Main-Stand geprüft.

Der aktuelle Stand ist stärker bei:

- Full-History-/OOS-Governance
- Walk-Forward-/Leakage-Schutz
- Rule-vs-ML-Trennung
- Artifact-/Feature-Hash-Verträgen
- Trade-Evidence
- Signal-/Trade-Identität
- Exit-/MFE-/MAE-Erfassung

Kein alter Pflichtbaustein blockiert den abgeschlossenen Single-Market-Pilot.

Weiterhin nur teilweise abgedeckt und später prüfenswert:

- Telegram-/Manual-Signal-Provenienz
- explizite 1m/5m/15m-Entry-Confirmation
- persistentes Pending/Recheck
- kanonischer Import alter manueller Trades mit vorherigem Signal
- Recency Weighting nur als Forschungsvergleich, nicht als automatische Übernahme

Alte Modellartefakte bleiben historische Evidence und werden nicht als aktuelle kompatible Modelle behandelt.

## OpenAI AI-only

Der OpenAI-Input-Audit zeigte fehlenden höheren Zeitrahmen-, Struktur- und Positionskontext. Exakte Timeframes und Prompt-Felder werden bewusst nicht veröffentlicht.

Der Minimal-Patch liefert jetzt Multi-Timeframe-Kontext, breiteren Marktkontext, Struktur, Volatilität, News, aggregierten Learning-Kontext und gegebenenfalls aktuellen simulierten Positionskontext. Exakte Feldzusammensetzung wird bewusst nicht veröffentlicht.


Eine belastbare Futures-/Spot-Basisquelle war nicht vorhanden und wird deshalb nicht erfunden.

Ein redigierter Request-Export wurde ohne zusätzlichen Paid Call erzeugt.

Ein Effizienzproblem bleibt offen: Der Request vor der Kompaktierung war unnötig groß. Exakte Tokenzahlen und Batching-Details werden bewusst nicht veröffentlicht.

## Was offen bleibt

1. Compact OpenAI Request / Single-Plan-Contract fertigstellen und beim nächsten regulären Paid Call beweisen, ohne Test-Call.
2. Die tatsächliche kausale OpenAI-Decision-Qualität mit mehreren Outcomes belegen.
3. Den neuen ENA-Pilot durch den Robustness Gate bewerten, statt Trainingsabschluss mit Modellqualität gleichzusetzen.
4. Canonical-Memory-Lücken schließen: Learning-Delta je Trade, vollständige CURRENT/V2-Trennung und Promotion-Historie.
5. Legacy-Teilbereiche nur über kontrollierte Evidence/Replays prüfen, nicht alten Code kopieren.
6. WebUI weiter vereinfachen; für große Historien bleiben Pagination/Virtualisierung sinnvoll.
7. Breites Multi-Coin-Training und automatische Promotion blockiert lassen, bis die Evidence genügt.
8. Nach Abschluss der parallelen Arbeiten die vollständige Projekttestsuite erneut laufen lassen bzw. frühere Fehler klassifizieren; fokussierte grüne Suites sind kein globaler wissenschaftlicher Nachweis.

## Sicherheitsgrenze

`LIVE=false` · `REAL_CAPITAL=0` · automatische Promotion deaktiviert.

Das Projekt bleibt research-first und fail-closed.

[Aktueller Status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Dokumentierte Arbeiten](../docs/progress/COMPLETED_WORK.md) · [Testergebnisse](../docs/verification/TEST_RESULTS.md)
