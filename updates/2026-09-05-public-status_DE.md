# Öffentliches Status-Update — 2026-09-05

English: [Public status update](./2026-09-05-public-status.md)

<!-- AUTO_VALUES_START -->
## Kurzfassung

Der 5. September drehte sich vor allem darum, **echten wissenschaftlichen Fortschritt von technischem Prozess-Erfolg zu trennen** und den Weg zu `LIVE_READINESS` sauberer zu machen.

Der wichtigste Fund war ein konkreter Factory/QUICK-Identitätsfehler. Er wurde repariert und ein neuer Research-Core aktiviert. Trotzdem wurde der Fix bewusst **nicht** als End-to-End abgeschlossen markiert, weil der erste Produktionsversuch danach keine gültige `eligible` Factory-Queue-Zeile hatte und deshalb korrekt **vor** teurer Arbeit stoppte.

Parallel wurden Research Forward / Watch erneut auf echte Liveness geprüft, ein BALANCED-Lauf scheiterte technisch am GPU-Preflight, und bei historischen OpenAI-Settlements wurde ein Datenqualitätsfehler bestätigt. Diese Fehler bleiben als Fehler sichtbar und werden nicht nachträglich als wissenschaftlicher Reject oder Fortschritt umetikettiert.

## Was heute erreicht wurde

### Factory / QUICK Identity Propagation

Exakter Root Cause:

```text
missing_field = factory_queue_id
root_cause = Prebind schrieb queue_id, ResumeStore validierte factory_queue_id
```

Geänderte Pfade:

- `algosphere/research/pipeline.py`
- `algosphere/research/resume.py`
- `research_autopilot_v35.py`

Neuer Research-Core gebaut und aktiviert:

```text
4095edd8490527f55e4da2d86c9fd2dd3a904ccad3a4ba81d6ea25c400235a33
```

Gezielte Validierung:

```text
15 passed
```

Der Produktionsversuch danach stoppte korrekt mit:

```text
FACTORY_QUICK_NO_ELIGIBLE_QUEUE_ROW
EXPENSIVE_WORK_STARTED = false
```

Damit ist der bekannte `factory_queue_id`-Propagationsfehler technisch repariert, aber ein echter neuer kanonischer Factory→QUICK-End-to-End-Lauf bleibt **offen**. Die vorherige Queue-Zeile war bereits von `eligible` auf `selected` gewechselt; AlgoSphere hat deshalb keinen ungültigen Start erzwungen.

### Standalone QUICK korrekt klassifiziert

Ein standalone QUICK lief technisch vollständig durch:

```text
expected = 120
actual = 120
nested_pass = 2
nested_rejected = 46
fast_rejected = 72
exit_code = 0
```

Der Run trug jedoch beim Start nicht die erforderliche Factory-Identity, unter anderem fehlten `factory_attempt_id`, `factory_hypothesis_id` und `hypothesis_fingerprint`.

Deshalb gilt:

```text
run_6ae != canonical B scientific completion
```

Eine nachträgliche Identity-Bindung ist nicht erlaubt. Ein technisch abgeschlossener Lauf ist nicht automatisch kanonische wissenschaftliche Evidence.

### Factory-Identity-Vertrag verschärft

Neue Factory-Runs müssen ihre Identität ab Start durch die gesamte Kette persistent tragen:

```text
factory_attempt_id
factory_hypothesis_id
hypothesis_fingerprint
factory_generation
source_memory_lesson_id
run_id
research_epoch_id
dataset_hash
feature_contract_hash
cost_contract_hash
runtime_core_hash
```

Die gezielte B-Hypothese ist bereits bekannt. Teure Berechnung darf aber erst starten nach:

```text
IDENTITY_AT_START = PASS
```

Der Pflichtpfad bleibt:

```text
B scientific terminal
→ Memory B
→ qualifizierter Candidate Freeze
→ BALANCED/OOS
```

### Research Forward / Research Watch Liveness

Frische Evidenz bis ungefähr 23:35 zeigte, dass Research Watch **nicht tot** war, entgegen einer früheren Vermutung.

Aktuell beobachtet:

```text
RESEARCH_FORWARD_PROCESS          PASS / live
RESEARCH_WATCH_DECISION_CYCLES   PASS / frisch
WATCH_SETUP_EVALUATION            PASS / aktiv
WATCH_CLOSED_OUTCOMES             keine neuen sichtbaren seit ~18:59
```

TUT, ADA, ONDO, MYX und ENA wurden weiter mit echten Setup-Gates ausgewertet. Viele aktuelle Entscheidungen waren legitime `GATE_SETUP_BLOCKED / NO TRADE`-Ergebnisse, unter anderem wegen Regime, fehlendem Setup, Range-Position, Expected Return, Volumen-Z oder Spot/Futures-Basis.

Offen bleibt die Closed-Outcome-Liveness und die korrekte WebUI-Wahrheit. Die Regel bleibt verbindlich:

```text
PROCESS RUNNING != OUTCOME ACTIVITY
```

### Checkpoint / Resume / Prozesshandling

Verbessert bzw. erhalten:

- Windows Checkpoint-Write PermissionError: PASS
- Resume nach technischem Abort verwendet fertige Coins/Phasen weiter: PASS
- explizite Identity-Felder für neue Factory-Runs: PASS
- Duplicate-Research-Worker-Prevention: PASS
- Launcher / venv / Base-Python / Worker sauberer klassifiziert: PASS

Ein technischer Abort darf nicht in einen wissenschaftlichen Reject umgedeutet werden.

## Heute beobachtete Fehler und Blocker

### BALANCED technisch fehlgeschlagen

BALANCED-Run:

```text
run_id = run_96d3dccd5523425ca84f395287ff8464
reason = GPU watchdog / BLOCKED_PREFLIGHT
```

Klassifikation:

```text
TECHNICAL FAILED
```

Das ist **kein** wissenschaftlicher Reject. Evidence bleibt erhalten. Der GPU-/CUDA-/Watchdog-Root-Cause muss gezielt isoliert werden, ohne Folds, Samples oder Qualitätsgates zu lockern und ohne XGBoost künstlich auf CPU zurückzuzwingen.

### Ungebundener QUICK braucht Klassifikation

Ein separater QUICK blieb aktiv/ungebunden:

```text
run_id = run_4725ea54a68343a2ad186d73c08d5765
profile = QUICK
factory binding = missing
```

Er muss zuerst als wissenschaftlich notwendig oder redundant klassifiziert werden. Falls redundant, kontrolliert beenden, Checkpoint/Evidence erhalten und Lease sauber freigeben; **nicht** als REJECT markieren.

### OpenAI Historical Settlement Datenqualitätsfehler

Wiederholt bestätigt wurde dieses historische Muster:

```text
HORIZON_SETTLEMENT
entry_price == exit_price
gross_pnl = 0
net_pnl = -0.12 USDT
```

Das wird als Datenqualitäts-/Settlement-Fehler behandelt und nicht als echte Trading-Evidence.

Alle betroffenen historischen OpenAI-Outcomes müssen lokal neu aufgebaut werden aus Original-Prediction-/Reference-Zeit, Richtung, vorgesehenem Horizon und echtem historischen Settlement-Preis. Dafür sind keine neuen OpenAI-Calls nötig.

Harte Regeln:

- Entry-/Reference-Preis niemals still als Exit-Preis wiederverwenden
- Kosten genau einmal anwenden
- LONG/SHORT-PnL-Richtung korrekt halten
- fehlt der historische Settlement-Preis wirklich, `NOT_CAPTURED`, `DATA_MISSING` oder `BLOCKED` schreiben
- keine doppelten rebuilt Outcomes erzeugen
- WebUI muss exakt das rebuilt Ledger zeigen

Spät am Abend erschien ein neuer TUTUSDT AI-only Outcome von ungefähr `+2.20 USDT`. Das zeigt, dass wieder neue Evaluationseinträge entstehen können. Die konkrete Settlement-Preisquelle dieses Outcomes ist aber **noch nicht vollständig verifiziert** und zählt deshalb noch nicht als belastbarer Performance-Beweis.

### Codex-Budget ausgeschöpft

Der breitere Runtime-Liveness-Repair-Task zu Watch Writer/Reader-Liveness, OpenAI Settlement/Evaluation, WebUI stale/current-truth und Duplicate Writer/Reader Cleanup wurde wegen erreichtem Codex-Limit nicht abgeschlossen.

Daher:

- kein PASS aus dem abgebrochenen Task
- unbekannte Teiländerungen nicht als fertig behandeln
- keine neuen Codex-Aufträge bis Reset/zusätzliche Credits
- lokaler deterministischer Repair und billiger Preflight zuerst

## Aktueller Betriebszustand beim 23:45-Snapshot

Der öffentliche Snapshot meldete:

- Runtime-Release: `v125`
- ML-Autopilot: `QUICK_FAILED`
- Profil: `quick`
- Phase: `ERROR`
- Symbol: `not verified`
- Fortschritt: `0/0`
- Stage-Wahrheit: `LAST_COMPLETED_STAGE`
- Live-Trading: `Nein`
- Real Capital: `0`
- automatische Promotion: `deaktiviert`
- Snapshot: `2026-09-05T22:44:59.312634Z`

Separat weist das Repository Package-/Update-Metadaten `v90_8_10_127` aus. Diese Identifikatoren haben unterschiedliche Gültigkeitsbereiche und dürfen nicht so dargestellt werden, als wären sie dieselbe Runtime-Beobachtung.

## Aktueller Prioritätspfad

Die Projektpriorität lautet jetzt ausdrücklich:

```text
Factory/B sauber
→ qualifizierte Kandidaten
→ Freeze
→ BALANCED/OOS
→ Reference V1
→ Challenger
→ Prospective
→ Paper
→ Champion
→ LIVE_READINESS_GATE
→ Elite Canary
→ kontrollierte Skalierung
```

Ein direkter Sprung von QUICK zu Live ist nicht akzeptabel.

## Aktuelles P0 / noch offen

1. Eine wirklich `eligible` Factory-Queue-Zeile über den kanonischen Selector erhalten.
2. Factory-Identity byte-for-byte durch Guard → Research Channel → aktiven Core → Pipeline/Resume beweisen.
3. Den gezielten identity-bound B-Run erst nach `IDENTITY_AT_START = PASS` starten.
4. B wissenschaftlich terminalisieren und Memory B persistieren.
5. Nur wirklich qualifizierte `nested_pass`-Kandidaten einfrieren.
6. BALANCED/OOS nur auf diesen Gewinnern; vorher keine neue breite Discovery.
7. GPU-Watchdog / `BLOCKED_PREFLIGHT` Root Cause beheben.
8. Reference Benchmark Contract V1 vor dem Vergleich implementieren/frieren.
9. Challenger → Shadow → Prospective → Paper Lifecycle reparieren.
10. Paper Execution Parity und Paper Outcome Memory End-to-End beweisen.
11. Alle falschen historischen OpenAI-Settlements aus lokalen historischen Preisen neu aufbauen.
12. Aktuelle Settlement-Preisquelle für neue OpenAI-Outcomes beweisen.
13. Current Truth / stale detection im Backend und in der WebUI dominant halten.
14. Vollständiges `LIVE_READINESS_GATE` vor jedem Elite Canary abschließen.

## Zusätzlich offen: Lernen und Marktintelligenz

AlgoSphere soll stärker lernen nach:

```text
Strategy × Coin × Side × Regime × Volatility × Outcome
```

und den übergeordneten Markt-Bias klar vom tatsächlichen Entry-Timing trennen. Marktweite Schocks und Post-Shock-Rebounds bleiben ebenfalls explizit offene Arbeit. Die WebUI soll diese Zustände in normaler Sprache erklären und nicht nur technische Labels anzeigen.

## Sicherheitsgrenze

Die öffentliche/operative Sicherheitsgrenze bleibt:

```text
LIVE=false
DIRECT_ACTION=0
CONSUMER=0
REAL_CAPITAL=0
```

Kein automatisches Live-Trading, keine automatische Real-Capital-Promotion und keine Lockerung von Gates, nur um Kandidaten zu erzeugen.

## Technische Evidenz

Hashes, öffentliches Register, Prüfgrenzen und historische Artefakte bleiben separat verfügbar. Sie sind Belege und ersetzen nicht die Entwicklungszusammenfassung oben.

Siehe [Aktueller Status](../CURRENT_STATUS.md), [Testergebnisse](../docs/verification/TEST_RESULTS.md), [Roadmap](../docs/progress/ROADMAP.md) und die [Evidenzübersicht](../evidence/EVIDENCE_SUMMARY.md).
<!-- AUTO_VALUES_END -->
