# Öffentliches Status-Update — 2026-09-17

English: [Public status update](./2026-09-17-public-status.md)

## Zusammenfassung

Der Nightly-Publisher bleibt pausiert. Dieses Update ist deshalb ein manuell geprüfter Stand für die Arbeiten vom 15.–16. September und den aktuellen frühen Stand vom 17. September.

In drei Bereichen gibt es echten Fortschritt: Der OpenAI-AI-only-Pfad ist deutlich unabhängiger und brauchbarer geworden, der Trade-Memory-Vertrag wurde für Paper / Watch / Research / OpenAI vereinheitlicht, und mehrere echte WebUI-/Projektionsfehler wurden repariert. Gleichzeitig ist ein wichtiger Runtime-Fehler noch offen: ein Research-Runtime-Pfad kann bei der Datenaktualisierung ausfallen, obwohl eine gemeinsame Marktdatenquelle weiterhin frisch ist. Ein strenger Fallback über den bestehenden gemeinsamen Reader wurde begonnen; der finale Acceptance-Nachweis stand noch aus.

Training und Factory bleiben bewusst pausiert. Live-Trading bleibt deaktiviert und Echtgeld bleibt bei 0.

## OpenAI AI-only Market Analyst V2

Der OpenAI-Pfad wurde deutlich überarbeitet, ohne eine zweite Architektur, Queue, Evaluator- oder Writer-Struktur einzuführen.

### Datenfrische-Root-Cause repariert

Ein echter Fehler lag in der Freshness-Prüfung: Signalalter und tatsächliche Marktdatenfrische waren nicht sauber genug getrennt.

Der reparierte V2-Pfad trennt diese beiden Dinge und beurteilt technische Verfügbarkeit anhand der tatsächlichen Futures-Marktdaten.

### Unabhängiger Analysevertrag

Der V2-Abnahmebericht dokumentiert unabhängige Analyse, das Abweisen lokaler Richtungs-Hinweise vor dem externen Modellaufruf und die Verwendung von breiterem Marktkontext. Exakte Marktlisten und Prompt-Feldverträge werden bewusst nicht veröffentlicht.


Der neue Ablauf lautet:

`frische Marktdaten → unabhängige Analyse → konditionale Szenarien → kontrollierte Simulation → Outcome → Evidence`

### Multi-Szenario-Modell

Der aktuelle private Analysevertrag kann mehrere maschinenlesbare Szenarien ausdrücken, unter anderem Range Fade, Trend Pullback/Rally, Continuation, Breakout/Breakdown, Failed Breakout/Breakdown, Reversal und NO_TRADE.

Jedes Szenario besitzt maschinenlesbare Bedingungen und Lifecycle-Metadaten; exakte Execution-Felder werden bewusst nicht veröffentlicht.

Der erste echte V2-Nachweis lief ohne Schemafehler und ohne echte Orders durch. Exakte Markt-/Szenariozahlen werden bewusst nicht veröffentlicht.


Später in derselben Arbeitssitzung wurden weitere simulierte Outcomes beobachtet. Exakte Symbole, Trade-Anzahlen und Positionsdetails werden bewusst nicht veröffentlicht.

### Cadence / Kostenkontrolle

Die neue Cadence ist ereignisorientiert und rate-limited. Exakte Timing-Schwellen, Retry-Marker und Paid-Call-Regeln werden bewusst nicht veröffentlicht.


Damit verschiebt ein blockierter Versuch nicht mehr den nächsten verpflichtenden Analysezeitpunkt.

Die externe Modellintegration blieb budgetkontrolliert. Exaktes Modell-Routing und Kostenkonfiguration werden bewusst nicht veröffentlicht.

### Ausschluss offener Positionen

Der OpenAI-Pfad besitzt Duplicate-Exposure-Kontrollen während der simulierten Überwachung; exakte Symbolregeln werden bewusst nicht veröffentlicht.

## Einheitlicher Trade-Memory-Vertrag

Paper, Watch, Research Forward und OpenAI nutzen jetzt denselben bestehenden Capture-Pfad für die Informationen, die für Vergleich und Lernen aus ausgeführten Trades nötig sind.

Der vereinheitlichte Evidence-Vertrag bewahrt genügend Identität, Provenienz, Outcome- und Kostenkontext für spätere Vergleiche. Exakte Feldnamen und Schema-Details werden bewusst nicht veröffentlicht.


Beim dokumentierten Prüfstand erfüllten die geprüften Evidence-Populationen die geforderte Integrität. Historisch unbekannte Werte bleiben explizit unbekannt. Exakte Zeilenzahlen, Feldnamen, Schema-Labels und interne Ledger-Namen werden bewusst nicht veröffentlicht.

## WebUI / Trade-Like-CHE Verbesserungen

Mehrere sichtbare Probleme waren echte Projektions-/UI-Fehler und keine fehlenden Trades.

### Trade-Like-CHE Entry-Preis

Ein gespeicherter Entry war vorhanden, wurde aber wegen eines Projektions-Alias-Mismatches von der UI nicht korrekt gelesen. Die Projektion wurde korrigiert; exaktes Symbol, Preis und Feldnamen werden bewusst nicht veröffentlicht.

### ADX / Indikatoranzeige

Ein Fehler in der Indikatoranzeige wurde korrigiert und eine kausale Analyseanzeige ergänzt. Exakte Indicator-Wiring- und Feature-Eligibility-Details werden bewusst nicht veröffentlicht.

Eine natürliche Runde bestätigte den korrigierten Anzeigepfad über die geprüften Varianten.

### Kompakte IDs / Tabellenlayout

Audit-IDs bleiben intern verfügbar, während öffentliche Tabellen kompakte Darstellungen verwenden. Exakte ID-Layouts und interne Tabellenzuordnungen werden bewusst nicht veröffentlicht.

### Capture und NO_TRADE

Spät in der Sitzung wurden zwei weitere Projektionsfehler gefunden und im bestehenden Pfad korrigiert. Exakte interne Aliase und Ledger-Zuordnungen werden bewusst nicht veröffentlicht.


Beide Fehler wurden im bestehenden Projektionspfad korrigiert und die Regressionstests liefen grün. Die finale Browser-E2E-Prüfung wurde anschließend durch das noch offene Start-/Runtime-Problem unterbrochen.

## Runtime- / Startproblem noch offen

Das sichtbare Startproblem hat zwei Ebenen:

1. `START_ALGOSPHERE.cmd` kann scheinbar nichts tun, wenn der Supervisor bereits gesund läuft, weil ein Doppelstart absichtlich verhindert wird. Der Startpfad wurde so angepasst, dass dieser Zustand sichtbarer wird und die WebUI geöffnet wird, statt still zu wirken.
2. Wichtiger: Research Forward wurde beim Start beobachtet, brach aber beim ersten ein Research-Markt-Refresh am direkten Bitget-Socket mit `WinError 10013` ab.

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
