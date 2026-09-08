# Öffentliches Status-Update — 2026-09-07

English: [Public status update](./2026-09-07-public-status.md)

<!-- AUTO_VALUES_START -->
## Kurzfassung

Der 7. September war ein aktiver Reparatur- und Laufzeit-Prüftag. Entscheidend war nicht ein weiterer statischer Release-Text: AlgoSphere wurde sichtbar neu gestartet, der lokale Runtime-Stack kam mit Supervisor und Kernkomponenten wieder hoch und der ML-Autopilot setzte einen echten QUICK-Lauf fort. Gleichzeitig wurden zwei weiterhin offene Wahrheitslücken sichtbar, die nicht durch einen generischen Nachtbericht verdeckt werden dürfen: Same-Run-Resume ist noch nicht bewiesen und das unterschiedliche Verhalten von Watch und Research muss kausal geprüft werden, statt einfach Schwellenwerte zu verändern.

Der vorherige Nachtbericht behauptete sinngemäß, es habe heute keinen neuen Entwicklungsnachweis gegeben und übernahm deshalb überwiegend den Stand vom 5. September. Das war unvollständig. Dieses Update korrigiert die Tageschronik und trennt weiterhin sauber zwischen beobachtetem Runtime-Zustand, gemeldeter Umsetzung und noch offenem Nachweis.

## Was heute tatsächlich passiert ist

### Runtime-Neustart und Wiederherstellung

- Im Reparaturlauf wurde ein sichtbarer Neustart erfolgreich durchgeführt.
- Der Runtime-Supervisor war anschließend als einzelne Supervisor-Instanz vorhanden.
- Point13 / ACTIVE_PAPER, Research Forward, Research Autopilot, Local ML Autopilot und WebUI wurden nach dem Neustart als laufend gemeldet.
- Der aktuell laufende QUICK verwendet eine neue Runtime-Run-Identity (`run_f6cf…` im Reparaturverlauf). Der vorherige Lauf war unterbrochen worden und die Arbeit wurde unter einer neuen Run-ID fortgesetzt.
- Weil die Fortsetzung **nicht** dieselbe Run-ID behalten hat, ist `Same-Run-Resume` weiterhin **kein PASS**. Die Wiederherstellung funktioniert, die exakte Fortsetzung desselben Runs bleibt jedoch offen.

### ML-Fortschritt

- Der 23:45-Nachtlauf beobachtete `ML AUTOPILOT QUICK RUNNING`.
- Profil: `quick`.
- Phase: `MODEL_TRAIN`.
- Aktuelles Symbol: `MYXUSDT`.
- Fortschritt: `3/5` Coins.
- Zustandsquelle: `LIVE_STAGE_HEARTBEAT`.
- Freshness: `CURRENT_REPORT`.
- Quellzeitpunkt: `2026-09-07T22:45:00.432722Z`.

Das ist aktueller Runtime-Nachweis, aber noch kein Beweis dafür, dass der Lauf korrekt terminalisiert oder wissenschaftlich einen guten Kandidaten erzeugt.

### Watch vs. Research: Unterschied noch in Prüfung

- WATCH darf Research-/Watch-Trades erzeugen.
- RESEARCH soll diese Trades nicht einfach in derselben Rolle duplizieren; seine Aufgabe bleibt Evaluation/Forschung.
- Heute war sichtbar, dass Watch Trades erzeugen kann, während Research gleichzeitig ohne Trades bleibt.
- Dieser Unterschied darf **nicht** dadurch „repariert“ werden, dass Schwellenwerte gelockert oder Trades erzwungen werden.
- Notwendig ist ein kausaler Watch-vs-Research-Paritätsvergleich auf identischen Zeitpunkten, Coins und Marktständen: Eligibility → Assignment → Setup-Gates → Decision → Outcome.
- Damit muss geklärt werden, ob der Unterschied ein korrektes `NO SETUP / NO TRADE` ist oder ein Fehler in Assignment/Pipeline.
- Das aktuell laufende QUICK-Training darf für diese Analyse nicht unterbrochen werden.

## Wichtige Korrekturen bisheriger Annahmen

- Erfolgreicher Neustart ist nicht dasselbe wie Same-Run-Resume. Die Runtime wurde wiederhergestellt, aber die Fortsetzung unter exakt derselben Run-ID ist noch nicht bewiesen.
- Ein bloßes `RUNNING`-Label genügt nicht; frischer Stage-Heartbeat und aktueller Fortschritt sind erforderlich.
- `NO TRADE` in Research ist nicht automatisch ein Fehler. Es kann ein korrektes Ergebnis der Setup-Gates sein. Der Code muss zuerst beweisen, an welcher Stelle Watch und Research auseinanderlaufen.
- Watch-Aktivität allein beweist nicht, dass Research-Assignment, Funnel-Parität oder Outcome-Persistenz korrekt funktionieren.
- Der öffentliche Publisher darf nicht `NO_NEW_DEVELOPMENT_PROOF_TODAY` ausgeben, wenn aktuelle Reparatur-/Runtime-Belege vorhanden sind, die nur von seiner Quellenauswahl noch nicht eingelesen werden.

## Aktueller Betriebszustand aus lokalen Berichten

- Runtime-Release laut explizitem Feld: `not verified`.
- Acceptance-Berichtskennung (keine ausführende Runtime-Version): `v125`.
- WebUI-Quellversion: `v90_8_10_127`.
- Paket-/Update-Manifest: `not verified`.
- Anwendungs-Quellversion: `v90_8_5`.
- Historische Source-Hotfix-Kennung: `v90_8_5_23`.
- ML: `ML AUTOPILOT QUICK RUNNING` · `quick` · `MODEL_TRAIN` · `MYXUSDT` · `3/5`.
- Zustandsquelle: `LIVE_STAGE_HEARTBEAT`.
- Freshness: `CURRENT_REPORT`.
- Live-Trading laut Quelle: `Nein`.
- Real Capital: `0`.
- Automatische Promotion: `Nein`.

Die WebUI-Quellversion wird nicht als ausführende Runtime-Version ausgegeben. Das explizite Runtime-Release-Feld bleibt unverifiziert.

## Aktuelle Blocker / noch nicht bewiesen

- **P0:** Same-Run-Resume — Wiederherstellung nach Unterbrechung funktioniert, Fortsetzung unter exakt derselben Run-ID ist noch nicht bewiesen.
- **P0:** QUICK-Terminalisierung — der aktive Lauf muss mit korrekter Identity, genau einem terminalen Ergebnis und persistiertem Learning-Memory abschließen.
- **P0:** QUICK → BALANCED — nur ein wirklich vielversprechender QUICK darf BALANCED auslösen; prospektiver Runtime-Nachweis fehlt noch.
- **P0:** Watch-vs-Research-Parität — klären, ob der aktuelle Trade/No-Trade-Unterschied fachlich korrekt oder ein Assignment-/Pipeline-Fehler ist.
- **P0:** Research-Forward-Freshness/Outcomes — weiter frische funktionale Zyklen beweisen, nicht nur Prozess-Existenz.
- **P0:** Current Truth / Stale Detection — Runtime und WebUI müssen frische Worker-Wahrheit von historischem Stage-Zustand unterscheiden.
- **P0:** Historische OpenAI-Outcome-Reparatur — ältere verdächtige Settlements mit `entry_price == exit_price` bleiben ein separater offener Datenqualitäts-Punkt, bis Provenance und Neuaufbau bewiesen sind.
- **P0:** Runtime-Context-Gate — das zuletzt beobachtete Artefakt bleibt `FAIL_INCOMPLETE_V3_CONTEXT`; der Publisher hat das Gate nicht erneut ausgeführt.
- **P0:** Live Readiness bleibt geschlossen. Keine automatische Live- oder Real-Capital-Promotion.

## Was der automatische Nachtbericht weiterhin falsch macht

Scheduler und GitHub-Upload funktionieren. Das verbleibende Problem ist die Quellenauswahl und die automatische Tageserzählung.

Der Publisher bevorzugt derzeit datierte Review-Zusammenfassungen und eine kleine Menge projizierter Reports. Wenn frische Arbeit nur in neueren Reparatur-/Runtime-Artefakten steht, die der Publisher noch nicht erkennt, fällt er auf ältere Entwicklungstexte zurück und kann `NO_NEW_DEVELOPMENT_PROOF_TODAY_PREVIOUS_DATED_WORK_PRESERVED` melden, obwohl an diesem Tag nachweislich gearbeitet wurde.

Die nächste Publisher-Version soll den Tagesbericht daher deterministisch aus strukturierten Belegen des jeweiligen Tages zusammensetzen:

1. `today_completed`
2. `today_verified`
3. `today_failed_or_blocked`
4. `runtime_state`
5. `active_scientific_run`
6. `important_corrections`
7. `current_todo`
8. `still_not_proven`

Vor einem Fallback auf ältere Review-Texte müssen aktuelle Acceptance-/Repair-Zusammenfassungen, Runtime-Heartbeats, Scientific-Run-Events, Experiment-Memory, Watch-/Forward-Status und Blocker-Reports eingelesen werden. Alte Release Notes bleiben Historie und dürfen nicht automatisch zur Tageshauptgeschichte werden.

## Sicherheitsgrenze

Die Grenze bleibt `LIVE=false`, `DIRECT_ACTION=0`, `CONSUMER=0`, `REAL_CAPITAL=0`. Kein automatisches Live-Trading und keine automatische Real-Capital-Promotion.

[Aktueller Status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Tests](../docs/verification/TEST_RESULTS.md) · [Quellprojektion](../evidence/DAILY_SUMMARY.json)
<!-- AUTO_VALUES_END -->