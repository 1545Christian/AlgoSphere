# Öffentliches Status-Update — 2026-09-17

English: [Public status update](./2026-09-17-public-status.md)

## Zusammenfassung

Der Nightly-Publisher bleibt pausiert. Dieses Update ist deshalb ein manuell geprüfter Stand für die Arbeiten vom 15.–16. September und den aktuellen frühen Stand vom 17. September.

In drei Bereichen gibt es echten Fortschritt: Der OpenAI-AI-only-Pfad ist deutlich unabhängiger und brauchbarer geworden, der Trade-Memory-Vertrag wurde für Paper / Watch / Research / OpenAI vereinheitlicht, und mehrere echte WebUI-/Projektionsfehler wurden repariert. Gleichzeitig ist ein wichtiger Runtime-Fehler noch offen: Research Forward kann beim direkten Bitget-Socket-Refresh mit `WinError 10013` abbrechen, obwohl der zentrale Market-Data-Loader bereits frische 1-Minuten-Futuresdaten besitzt. Ein strenger Fresh-Data-Fallback über den bestehenden gemeinsamen Reader wurde begonnen, aber der angehängte Arbeitsstand enthält noch keinen finalen Acceptance-Nachweis für diese Reparatur.

Training und Factory bleiben bewusst pausiert. Live-Trading bleibt deaktiviert und Echtgeld bleibt bei 0.

## OpenAI AI-only Market Analyst V2

Der OpenAI-Pfad wurde deutlich überarbeitet, ohne eine zweite Architektur, Queue, Evaluator- oder Writer-Struktur einzuführen.

### Datenfrische-Root-Cause repariert

Ein echter Fehler lag in der Freshness-Prüfung: Das Alter eines bereits berechneten Signals wurde mit der Frische der zugrunde liegenden Bitget-Kerzen vermischt. Dadurch konnten tatsächlich frische Futures-Daten als `TECHNICAL_UNAVAILABLE` erscheinen, nur weil das Signalobjekt selbst ungefähr 100 Sekunden alt war.

Der reparierte V2-Pfad trennt diese beiden Dinge und beurteilt technische Verfügbarkeit anhand der tatsächlichen Futures-Marktdaten.

### Unabhängiger Analysevertrag

Der V2-Abnahmebericht dokumentiert:

- unabhängige Analyse: PASS
- lokale Richtung im Prompt: NEIN
- Rule-/ML-/Watch-/Research-/Trade-Like-CHE-/Paper-Richtungsfelder werden vor dem API-Aufruf abgewiesen
- BTC und ETH dienen nur als Kontext
- aktive Analysecoins: ADA, ENA, MYX, ONDO, TUT

Der neue Ablauf lautet:

`frische Futures-Daten → unabhängige OpenAI-Analyse → konditionale Szenarien → bestehender lokaler Paper-Monitor → bestätigter Trigger → lokale Positionsverwaltung → Settlement → bestehendes OpenAI-Memory`

### Multi-Szenario-Modell

Der neue Vertrag `OPENAI_AI_MARKET_ANALYST_V2` / `STRICT_INDEPENDENT_MULTI_SCENARIO_JSON_SCHEMA_V2` kann mehrere maschinenlesbare Szenarien ausdrücken, unter anderem Range Fade, Trend Pullback/Rally, Continuation, Breakout/Breakdown, Failed Breakout/Breakdown, Reversal und NO_TRADE.

Jedes Szenario enthält Trigger, Entry-Zone, Invalidation, Emergency Stop, zwei Targets, Runner-Bedingung, Ablaufzeit und stabile IDs.

Der erste echte V2-Nachweis dokumentierte:

- 5 Coin-Analysen
- 9 Szenarien im Zyklus
- 6 bewaffnete Szenarien unter lokaler Beobachtung
- 0 Schemafehler
- 0 echte Orders

Später in derselben Arbeitssitzung meldete der vereinheitlichte Memory-Audit drei aktuelle ausgeführte OpenAI-AI-only-Trades im aktuellen Trade-Bestand und eine offene TUTUSDT-Position unter Beobachtung. Die Profitabilität des neuen V2-Vertrags ist trotzdem noch nicht belegt; dafür braucht es mehrere abgeschlossene, kausale V2-Outcomes.

### Cadence / Kostenkontrolle

Die neue Cadence ist ereignisorientiert:

- lokale Prüfung etwa alle 5 Minuten
- Paid Call bei relevantem Ereignis oder spätestens nach 30 Minuten
- mindestens 5 Minuten zwischen Paid Calls
- blockierte Versuche aktualisieren nur `last_blocked_attempt`
- der nächste Refresh richtet sich nach `last_successful_paid_call`

Damit verschiebt ein blockierter Versuch nicht mehr den nächsten verpflichtenden Analysezeitpunkt.

Im V2-Abnahmezustand wurde `gpt-5.6-luna` verwendet. Call- und Tokenlimits bleiben aktiv. Ein exakter USD-Kostenwert wird bewusst nicht veröffentlicht, solange im Projekt kein bestätigter lokaler Modellpreis hinterlegt ist.

### Ausschluss offener Positionen

Pro Symbol darf höchstens eine offene OpenAI-Position existieren. Nach einem Entry werden konkurrierende Szenarien desselben Analysezyklus blockiert und der Coin wird bis Close/Settlement nicht erneut für neue OpenAI-Entries analysiert. Die lokale Überwachung läuft weiter.

## Einheitlicher Trade-Memory-Vertrag

Paper, Watch, Research Forward und OpenAI nutzen jetzt denselben bestehenden Capture-Pfad für die Informationen, die für Vergleich und Lernen aus ausgeführten Trades nötig sind.

Gespeichert werden unter anderem:

- stabile Trade-/Strategie-/Setup-IDs
- Bereich / Strategy Family
- Symbol / Side
- Entry-/Exit-Zeit und tatsächliche Preise
- Marktphase
- Expected Net mit Quelle und Status
- MFE / MAE inklusive Zeitpunkt
- Gebühren, Slippage, Funding und Nettoergebnis
- Stop, Target und Exit-Grund
- Entry-/Exit-Datenqualität
- Marktdaten-Provenienz
- Margin / Notional, soweit historisch belegbar

Beim dokumentierten Prüfstand hatten die aktuellen ausgeführten Trade-Bestände keine fehlenden Pflicht-Kernfelder:

- Paper Market Context: 35
- Watch: 19
- Research Forward: 28
- OpenAI AI-only: 3

Auch alle 66 bisherigen echten OpenAI-AI-only-Outcomes besitzen laut Audit jetzt Trade-ID, Strategie, Setup, Marktphase sowie MFE-/MAE-Zeit.

Bei 38 sehr alten OpenAI-Trades bleibt `source_margin_usdt` unbekannt, weil die ursprünglichen Entry-Daten weder Margin, Notional noch Leverage enthielten. Diese Werte werden nicht erfunden. Unbekannte Werte erhalten stattdessen eindeutige Zustände wie `PENDING_PATH_SETTLEMENT`, `NOT_APPLICABLE` oder `NOT_RECONSTRUCTABLE` statt stillschweigend als 0 zu gelten.

Die 854 `openai_market_evaluations` bleiben korrekt Analysen/Counterfactuals und werden nicht künstlich zu ausgeführten Trades gemacht.

## WebUI / Trade-Like-CHE Verbesserungen

Mehrere sichtbare Probleme waren echte Projektions-/UI-Fehler und keine fehlenden Trades.

### Trade-Like-CHE Entry-Preis

Der ONDOUSDT-Entry war korrekt mit `0.3391` gespeichert. Das Repository lieferte `entry_price` / `opened_at`, während die UI `entry_price_raw` / `entry_time` erwartete. Die Projektion liefert nun die erwarteten Aliase plus sichere Fallbacks.

### ADX / Indikatoranzeige

Ein negatives Volume-Z färbte vorher fälschlich die ganze Indikatorzelle rot und ließ ADX / ATR / RSI negativ wirken. Die Anzeige wurde getrennt. ADX wurde außerdem kausal aus abgeschlossenen 5-Minuten-Futures-Kerzen ergänzt. ADX ist aktuell nur Anzeige-/Analyseinformation und kein ML- oder Entry-Feature.

Eine natürliche Runde meldete 40/40 aktuelle Varianten mit numerischem ADX und 0 fehlenden ADX-Werten.

### Kompakte IDs / Tabellenlayout

Vollständige SHA-/Decision-/Trade-/Outcome-IDs bleiben für Audit, Tooltip und Details erhalten. Sichtbar werden kompakte Suffixe angezeigt. Dieselbe Darstellungsregel wurde auf aktive/geschlossene Trades, Watch/Research, OpenAI, Strategien und Kandidaten vereinheitlicht.

### Capture und NO_TRADE

Spät in der Sitzung wurden zwei weitere Projektionsfehler gefunden:

- Trade-Like-CHE `Capture` nutzte ein nicht befülltes Alias, obwohl der kanonische Netto-Return vorhanden war.
- OpenAI `NO_TRADE` las nur den Evaluations-Ledger, obwohl viele gültige NO_TRADE-Predictions im kanonischen Prediction-Ledger liegen.

Beide Fehler wurden im bestehenden Projektionspfad korrigiert und die Regressionstests liefen grün. Die finale Browser-E2E-Prüfung wurde anschließend durch das noch offene Start-/Runtime-Problem unterbrochen.

## Runtime- / Startproblem noch offen

Das sichtbare Startproblem hat zwei Ebenen:

1. `START_ALGOSPHERE.cmd` kann scheinbar nichts tun, wenn der Supervisor bereits gesund läuft, weil ein Doppelstart absichtlich verhindert wird. Der Startpfad wurde so angepasst, dass dieser Zustand sichtbarer wird und die WebUI geöffnet wird, statt still zu wirken.
2. Wichtiger: Research Forward wurde beim Start beobachtet, brach aber beim ersten ADAUSDT-Refresh am direkten Bitget-Socket mit `WinError 10013` ab.

Gleichzeitig hatte der zentrale Market-Data-Loader bereits frische 1-Minuten-Futuresdaten. Die geplante Reparatur bleibt innerhalb des bestehenden gemeinsamen Readers: Nur wenn der direkte Socket ausfällt, darf nach strenger Frische-/Verfügbarkeitsprüfung der vom zentralen Loader bestätigte Hot-File-Tail verwendet werden. Veraltete Dateien müssen weiterhin abgewiesen werden.

Der angehängte Arbeitsstand endet während der Ausarbeitung dieses Fallbacks. **Diese Runtime-/Datenquellen-Reparatur bleibt deshalb OFFEN, bis ein frischer Restart plus Research-Forward-Zyklus sie beweist.**

## Unabhängigkeit von Codex

AlgoSphere muss ohne Codex laufen. Codex wird zum Verstehen, Reparieren und Testen des Projekts genutzt, nicht als notwendiger Runtime- oder Trading-Controller. Die letzten Arbeiten hielten diese Grenze ein: keine zweite Runtime-Helper-Schicht, keine zweite Memory-Pipeline, kein zweiter OpenAI-Evaluator und kein neues Queue-Subsystem.

## ML / Factory / Testsuite

Breites Training und Factory bleiben pausiert. Der Lifecycle bleibt:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

Rule-Evidenz muss unabhängig vom Erfolg eines ML-Selectors erhalten bleiben: ML-Selector-Kollaps ist nicht Rule-Failure.

Die fokussierten Regressionstests vom 16. September waren stark (263/263 rund um OpenAI V2, 264 relevante Tests rund um Unified Memory, 154 fokussierte Tests rund um ADX/Anzeige sowie kleinere fokussierte Suites). Diese Prüfungen sind relevant, beweisen aber noch nicht automatisch, dass der frühere vollständige Suite-Stand mit 1.307 Tests / 64 Fehlern komplett abgeschlossen ist. Die Full-Suite-Hygiene bleibt deshalb offen, bis die komplette Suite erneut läuft und jeder frühere Fehler geschlossen oder bewusst klassifiziert ist.

## Was jetzt wirklich besser ist

- OpenAI ist tatsächlich von lokaler Richtungs-Vorgabe getrennt.
- Frische Kerzen sollen nicht mehr wegen eines älteren Signalobjekts als stale gelten.
- OpenAI erzeugt flexible konditionale Szenarien statt einer starren Sofortrichtung.
- Paid-Call-Cadence richtet sich nach dem letzten erfolgreichen Call, nicht nach blockierten Versuchen.
- Offene Coins werden von doppelten OpenAI-Entry-Analysen ausgeschlossen.
- Paper / Watch / Research / OpenAI ausgeführte Trades nutzen einen vergleichbaren Memory-Vertrag.
- Unbekannte historische Werte werden explizit typisiert statt als 0 interpretiert.
- Trade-Like-CHE Entry-Projektion ist repariert.
- ADX ist für neue Entscheidungen als Analysewert vorhanden.
- IDs und große Tabellen sind besser lesbar.
- NO_TRADE- und Capture-Projektionsfehler wurden identifiziert und im bestehenden Pfad korrigiert.

## Was offen bleibt

1. Research-Forward-`WinError 10013`-Fallback fertigstellen und beweisen, ohne zweiten Datenpfad.
2. `START_ALGOSPHERE.cmd` sowohl im Already-Running- als auch im wirklich gestoppten/orphaned Zustand sauber nachweisen.
3. Den breiten isolierten Browser-Audit für Cockpit, Trading, OpenAI und Research nach stabiler Runtime abschließen.
4. Forecast-Weitergabe und Research-Open-Position-Anzeige nach Restart erneut prüfen; im Arbeitslog fehlt noch der finale Abschlussnachweis.
5. Capture und NO_TRADE im laufenden Browser nach dem Runtime-Fix erneut verifizieren.
6. Genug kausale OpenAI-V2-Outcomes sammeln, um die tatsächliche Trading-Qualität zu beurteilen.
7. Verifizierte Modellpreisquelle konfigurieren, bevor exakte OpenAI-USD-Kosten veröffentlicht werden.
8. Komplette Projekttestsuite erneut laufen lassen und die früheren 64 Full-Suite-Fehler schließen/klassifizieren.
9. Training und Factory pausiert lassen, bis Runtime/Evidenzpfad stabil genug ist.
10. Live aus und Echtgeld bei 0 lassen.

## Sicherheitsgrenze

`LIVE=false` · `REAL_CAPITAL=0` · `ORDERS=0` · Training pausiert · Factory pausiert.

Kein Dokumentationsupdate autorisiert Live-Trading, automatische Modellpromotion oder Echtgeld-Ausführung.

[Aktueller Status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Dokumentierte Arbeiten](../docs/progress/COMPLETED_WORK.md) · [Testergebnisse](../docs/verification/TEST_RESULTS.md)
