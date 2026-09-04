# Öffentliches Status-Update — 2026-09-04

English: [Public status update](./2026-09-04-public-status.md)

<!-- AUTO_VALUES_START -->
## Kurzfassung

Der 4. September war nicht mehr nur ein v117-Update, sondern ein längerer Reparatur- und Laufzeittag bis zum aktuell beobachteten Runtime-Stand `v90_8_10_125`. Im Mittelpunkt stand, die lokale Lernkette tatsächlich autonom zu machen: Training darf nicht von einem getrennten Research-Evaluator abhängen, neue wissenschaftliche Arbeit darf nicht hinter alten `COIN_DONE`-/Resume-Zuständen verschwinden, Research Forward muss fachlich gesund sein und nicht nur über eine Launcher-PID „laufen“, und die WebUI braucht einen festen lokalen HTTP-Einstieg mit echter Health-/Self-Healing-Prüfung.

Der 23:45-Nachtlauf hat den aktuellen Runtime-Snapshot korrekt veröffentlicht, die Entwicklungszusammenfassung war aber noch zu stark vom älteren v117-Grundtext geprägt. Diese Seite wurde deshalb korrigiert und auf den heute tatsächlich beobachteten, belegten Arbeitsstand gebracht.

## Was heute tatsächlich erreicht wurde

### ML-Autonomie und Lernschleife

- Die v117-Trennung bleibt Grundlage: `LOCAL_ML_AUTOPILOT` ist die normale Trainingsautorität; Codex/Chat sind keine Voraussetzung für den Runtime-Fortschritt.
- v122/v123 korrigieren eine reale P0-Lücke: Die Erzeugung neuer adaptiver Hypothesen darf nicht mehr indirekt vom getrennten Research-Evaluator abhängen. Der Local-ML-Daemon liest dauerhaftes Memory, dedupliziert bereits getestete Arbeit semantisch, erzeugt selbst neue zulässige Hypothesen und kann QUICK starten.
- `factory_exhausted -> WAITING FOR JOB` wird nicht mehr als normaler Betriebszustand akzeptiert. Adaptive Mutation und danach begrenzte Family-Discovery sollen wirklich neue Arbeit erzeugen; nur echte Suchraum-Erschöpfung darf warten.
- Neue semantische Factory-Generationen wurden in den `COIN_DONE`-/`RUN_COMPLETE`-Resume-Vertrag aufgenommen, damit neue wissenschaftliche Arbeit nicht hinter einem alten abgeschlossenen Checkpoint verschwindet.
- Die gewünschte autonome Kette bleibt: QUICK → Ergebnis → Memory → bei promising Evidence BALANCED, sonst nächste neue Hypothese.

### Tatsächlicher wissenschaftlicher Laufnachweis

- Ein QUICK-Lauf erreichte am `2026-09-04T18:42:15Z` einen terminalen Abschluss.
- Der standardisierte Experiment-Memory-Datensatz wurde persistiert (`status=RECORDED`, `scientific_result=COMPLETED`).
- Das war **kein Performance-PASS**: Der gespeicherte Best-Candidate-Eintrag für `ENAUSDT / basis_dislocation / logistic / long` blieb `factory_exhausted` und enthielt keine belastbaren PF-/PnL-/Trade-Kennzahlen. Das ist ein wissenschaftlich abgeschlossener Reject-/Erschöpfungszustand und kein Trading-Erfolg.
- Danach lief autonome QUICK-Arbeit weiter. Beim Nachtlauf war `v90_8_10_125` aktiv in `CHECKPOINT` auf `MYXUSDT`, mit `3/5 Coins` abgeschlossen und `LIVE_STAGE_HEARTBEAT` als aktueller Zustandsquelle.
- Der Research-Autopilot meldete `eligible experiments = 1`; automatische Promotion blieb deaktiviert.

### Research Forward / Watch

- Research Forward ist fachlich vom Research-Evaluator getrennt: eigener Supervisor-Service und eigener no-capital Child-Trader; der Evaluator bleibt separat.
- Health bedeutet nicht mehr nur „Prozess existiert“, sondern umfasst Child-Heartbeat und funktionalen no-capital-Zustand.
- v123 Validate-only: PASS mit 90 Strategien, je 18 für ADA/ENA/MYX/ONDO/TUT, `capital_allowed=false`.
- Watch/Research bleiben Explorations- und Evidence-Rollen. Erkenntnisse daraus müssen segmentiert in Eligibility/Memory zurückfließen und dürfen Paper erst nach weiterer prospektiver Bestätigung beeinflussen.

### WebUI / Runtime-Recovery

- Ein lebender PowerShell-Launcher allein gilt nicht mehr als gesunde WebUI.
- Der Supervisor prüft den echten HTTP-Endpunkt `http://127.0.0.1:8012/api/ping`.
- Ein toter HTTP-Child wird kontrolliert retired und neu gestartet.
- Der lokale Browser öffnet Loopback; ein erinnerter oder zufälliger Port gilt nicht als Runtime-Wahrheit.
- Zusätzliche Fehlerdiagnose wird nach `reports/webui_runtime_error.txt` geschrieben.
- Fester lokaler Einstieg und HTTP-Health sind jetzt Code-Verträge; der längere Self-Healing-Nachweis bleibt weiter zu beobachten.

### OpenAI / Freshness / Kostenkontrolle

- OpenAI bleibt eine zweite Analyse-/Prediction-Engine und ist keine Voraussetzung für die lokale ML-Autonomie.
- v122 setzt die normale Luna-Cadence auf 30 Minuten und trennt Web/News mit 120 Minuten.
- Unveränderter Kontext darf einen neuen Zweitmeinungs-Call höchstens 60 Minuten überspringen.
- Lokaler Kontext älter als 45 Minuten soll nicht an OpenAI geschickt werden; `STALE` muss sichtbar sein.
- Scheduler-Prüfung, API-Versuch, erfolgreicher Request und Prediction-Zeit werden in der WebUI getrennt dargestellt.

## Heute korrigierte Fehlannahmen / Misserfolge

- Frühere Code-PASS-Bewertungen waren teilweise zu optimistisch: Der reale Windows-Betrieb zeigte, dass Local ML trotz vermeintlich fertigem Autonomie-Vertrag in `WAITING FOR JOB` hängen konnte.
- Neue Factory-Arbeit konnte hinter alten `COIN_DONE`-/`RUN_COMPLETE`-Checkpoints verschwinden. Das wurde als Resume-/Novelty-Fehler behandelt.
- Research Forward konnte äußerlich als gestartet erscheinen, obwohl der eigentliche no-capital Child-Trader fachlich nicht gesund war. Der Health-Vertrag wurde deshalb verschärft.
- Ein laufender oder abgeschlossener QUICK ist nicht automatisch ein guter Kandidat. `scientific_result=COMPLETED` und `factory_exhausted` müssen klar von Performance-/Promotion-Erfolg getrennt bleiben.
- WebUI-„Running“ darf nicht mehr aus einer Launcher-PID abgeleitet werden; echter HTTP-Health ist erforderlich.
- Fehlversuche und Blocker bleiben Teil der Evidence und werden nicht nachträglich als Fortschritt umetikettiert.

## Aktueller Betriebszustand beim Nachtlauf

- Runtime-Release: `v90_8_10_125`
- ML-Autopilot: `QUICK_RUNNING`
- Profil: `quick`
- Phase: `CHECKPOINT`
- Symbol: `MYXUSDT`
- Fortschritt: `3/5 Coins`
- Stage-Wahrheit: `LIVE_STAGE_HEARTBEAT`
- Live-Trading: `Nein`
- Real Capital: `0`
- automatische Promotion: `deaktiviert`
- Snapshot: `2026-09-04T22:45:00.015712Z`

## Aktuelles TODO / noch nicht bewiesen

1. Den aktuell laufenden QUICK bis zu einem terminalen Ergebnis beobachten und wissenschaftlichen Abschluss, Reject, promising Candidate und technischen Fehler sauber unterscheiden.
2. Nach jedem terminalen Lauf korrekte Run-/Core-/Factory-Identität, genau eine Terminalisierung, persistiertes Unified Memory und die daraus folgende nächste autonome Aktion nachweisen.
3. Bei promising Evidence prospektiv QUICK → BALANCED beweisen; bei Reject autonom zur nächsten semantisch deduplizierten Hypothese wechseln.
4. P0 bleibt offen: bestehende FeatureCaches sollen inkrementell nur um neue Kerzen erweitert und nicht unnötig komplett neu gebaut werden.
5. Research Forward muss über längeren Windows-Lauf frische Cycle-/Decision-/Watch-Evidence erzeugen und darf nicht nur technisch `RUNNING` aussehen.
6. Die WebUI muss dauerhaft über `127.0.0.1:8012` erreichbar bleiben und einen toten HTTP-Child korrekt ersetzen, ohne unnötig andere schwere Jobs neu zu starten.
7. Market Data / Regime / Watch / Forward brauchen weiterhin Freshness-, Quellenisolations- und gemeinsame Decision-/Feature-/Risk-/Exit-Paritätsprüfungen.
8. OpenAI-Freshness, 30/120-Minuten-Cadence, STALE-Blocking und der echte Prediction→Outcome→Memory-Effekt brauchen weiter Laufzeitnachweis.
9. Watch-/Market-Intelligence-Lernen darf Outcomes nicht nur archivieren; gute/schlechte/zu frühe/zu späte Entscheidungen müssen nach Strategy × Coin × Side × Regime × Volatility × Shock/Event-Kontext attributiert werden und später messbar Paper-Eligibility beeinflussen.
10. `PROVEN_CLOSED` bleibt an aktuellen Runtime-/Browser-/Ledger-Beweis gebunden; Code-PASS allein genügt nicht.

## Sicherheitsgrenze

Die Grenze bleibt `LIVE=false`, `DIRECT_ACTION=0`, `CONSUMER=0`, `REAL_CAPITAL=0`. Kein automatisches Live-Trading und keine automatische Real-Capital-Promotion.

## Technische Evidenz

Hashes, öffentliches Register, Prüfgrenzen und historische Artefakte bleiben separat verfügbar. Sie sind Belege und ersetzen nicht die Entwicklungszusammenfassung oben.

Siehe [Aktueller Status](../CURRENT_STATUS.md), [Testergebnisse](../docs/verification/TEST_RESULTS.md), [Roadmap](../docs/progress/ROADMAP.md) und die [Evidenzübersicht](../evidence/EVIDENCE_SUMMARY.md).
<!-- AUTO_VALUES_END -->
