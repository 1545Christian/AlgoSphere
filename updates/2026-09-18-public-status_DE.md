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

Aktueller Vertrag:

- 5 aktive Coins
- 26 CURRENT-Auswertungen je Coin
- 8 CONTEXT_V2-Auswertungen je Coin
- 34 Auswertungen je Coin insgesamt
- 170 erwartet
- 170 aktiv bestätigt

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

Beim Browser-Checkpoint waren 2 Paper-, 1 Watch-, 2 Research-Forward- und 0 OpenAI-Positionen offen.

Auch die Ladezeit wurde deutlich reduziert:

- 24h-Übersicht kalt: ca. 2,61 s
- 24h-Übersicht warm: ca. 0,03 s
- 24h-Payload: ca. 0,74 MB statt 4,79 MB
- damit rund 84,5 % weniger Übersichtsdaten

Umfangreiche Rohbelege werden jetzt erst auf Detailseiten geladen.

Die Gesamtstruktur der WebUI bleibt teilweise zu dicht und soll später weiter vereinfacht werden. Die konkreten Fehler bei fehlenden offenen Positionen wurden jedoch repariert.

## Market Intelligence und ENA-Pilot

Der Market-Intelligence-V2.1-Pfad arbeitet weiter mit:

- 3 bestehenden Feature-Arms
- 4 Architekturvarianten
- 7 Horizonten
- Logistic Regression
- HistGradientBoosting
- kausaler OOS-Auswertung
- Erhalt der Rule-Baseline

Der explizite ENA-1-Coin-Pilot wurde abgeschlossen mit:

- bestätigtem Full-History-Vertrag
- revalidierter Feature-Provenienz
- 756 OOS-Ergebniszeilen
- 126 Rule-Baseline-Ergebniszeilen
- 3 Feature-Arms
- 4 Architekturen
- 7 Horizonten
- identischer Fold-Basis für Rule und ML: 2026-07, 2026-08, 2026-09
- Registry-ID 7

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

Der neue Full-History-ENA-Pilot muss nun gegen diesen Gate ausgewertet werden. Ein abgeschlossener Trainingslauf ist nicht automatisch `ROBUST_OOS_READY`.

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

Kein alter Pflichtbaustein blockiert den abgeschlossenen ENA-1-Coin-Pilot.

Weiterhin nur teilweise abgedeckt und später prüfenswert:

- Telegram-/Manual-Signal-Provenienz
- explizite 1m/5m/15m-Entry-Confirmation
- persistentes Pending/Recheck
- kanonischer Import alter manueller Trades mit vorherigem Signal
- Recency Weighting nur als Forschungsvergleich, nicht als automatische Übernahme

Alte Modellartefakte bleiben historische Evidence und werden nicht als aktuelle kompatible Modelle behandelt.

## OpenAI AI-only

Der OpenAI-Input-Audit zeigte, dass im tatsächlich gesendeten Request 3D, 7D, explizite Support/Resistance-Struktur und Open-Position-Context fehlten.

Der Minimal-Patch liefert jetzt:

- 1m / 5m / 15m / 1h / 1D / 3D / 7D
- BTC-/ETH-Kontext
- Regime und Range Position
- explizite Structure-/Support-Resistance-Zusammenfassung
- Volume / Volatility
- News
- aggregierte Learning-Memory
- aktuelle OpenAI-Position, falls vorhanden

Eine belastbare Futures-/Spot-Basisquelle war nicht vorhanden und wird deshalb nicht erfunden.

Ein redigierter Request-Export wurde ohne zusätzlichen Paid Call erzeugt.

Ein Effizienzproblem bleibt offen: Der gemessene Request vor der Kompaktierung umfasste etwa 73.933 Input-Tokens und 4.438 Output-Tokens für fünf Coins. Der Compact-Request-/Single-Plan-Contract wird derzeit lokal umgesetzt und getestet. Er gilt erst nach einem normalen zukünftigen Paid Call als Forward-bewiesen.

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
