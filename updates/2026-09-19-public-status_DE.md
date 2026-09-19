# Öffentliches Status-Update — 2026-09-19

English: [Public status update](./2026-09-19-public-status.md)

## Zusammenfassung

Am 19. September lag der Schwerpunkt auf drei wiederkehrenden Projektproblemen: Canonical Memory / V2-Lineage, Wachstum des Research-Speichers und Wahrheit/Bedienbarkeit der WebUI.

Wichtige Fortschritte:

- Trade Like Che CURRENT und CONTEXT_V2 wurden in der Projektion erneut repariert und im Browser mit stabiler Varianten-/Filterauswahl geprüft.
- CONTEXT_V2 konsumiert jetzt das bestehende Canonical Learning Delta statt nur Market-State / Context-Fit zu verwenden.
- Neue CONTEXT_V2-Writes erzwingen State-Evidence strenger; der historische Exact-only-Backfill bleibt aber durch einen aktiven SQLite-Writer blockiert.
- Der erste Verlust im Research→Canonical-Handoff wurde gefunden und future-only repariert: Candidate-/Rule-/Fold-/Contract-Evidence wird jetzt kompakt vor dem Chat-2-Memory-Owner projiziert.
- Das starke Wachstum von `research_runs.summary_json.active_strategies` wurde auf doppelte dekodierte + `*_json`-Repräsentationen in zukünftigen Snapshots zurückgeführt. Der Future-Writer wurde in repräsentativen Größenschätzungen etwa halbiert, ohne historische Evidence zu löschen.
- Tabellen-/Filter-Vertrag der WebUI wurde stabiler und kompakter, bei wieder größerer lesbarer Schrift und Tooltips.
- Durch diese Reparaturen wurden kein Training, Replay, Promotion oder Live-Trading gestartet.

Das zentrale wissenschaftliche Problem bleibt unverändert: Mehr Infrastruktur funktioniert, aber ML-Uplift und ein vollständig geschlossener Lernkreislauf sind noch nicht bewiesen.

## Canonical Decision / Learning Contract

Das Projekt nähert sich weiter einer gemeinsamen vergleichbaren Kette:

`Decision → Candidate → Entry Intent / NO_TRADE → Trade / Watch / Counterfactual → Outcome → Canonical Memory → Learning Contribution → Learning Delta → Lifecycle`

Der Audit zeigte, dass diese Kette je Lane/Variante noch uneinheitlich ist.

Bekannte Lücken:

- historische `market_state_id` / `market_state_version` sind unvollständig
- historische Decision→Trade-Identität ist teilweise unvollständig
- Paper CONTEXT_V2 besitzt derzeit Decisions, aber keine vergleichbare ausgeführte Outcome-Population
- einige Paper-CURRENT-Learning-Zeilen sind weiterhin der Population Trade Like Che zugeordnet
- historische Varianten-/Population-Konsistenz ist noch nicht vollständig bewiesen

Neue CONTEXT_V2-Decisions/Outcomes schreiben fail-closed, wenn erforderliche State-Evidence fehlt.

### Historischer Exact-only Repair

Für PAPER / TLC existiert ein scoped Exact-only-Reparaturoperator.

Der reale Schema-Mismatch wurde korrigiert:

`canonical_trade_outcomes.decision_id → memory_decisions.decision_id`

Contributions / Deltas verknüpfen über `canonical_outcome_id`.

Der historische Apply ist aber **nicht abgeschlossen**. Wiederholte Apply-Versuche wurden blockiert durch:

`sqlite3.OperationalError: database is locked`

Daher gilt weiterhin:

- historische Reparatur committed: **NEIN**
- Runtime/Trading angefasst: **NEIN**
- Training/Promotion: **NEIN**

Writes wurden bewusst nicht gegen einen aktiven SQLite-Writer erzwungen.

## CONTEXT_V2 konsumiert jetzt Canonical Learning Delta

Ein konkreter fehlender Anschluss wurde repariert:

`memory_learning_deltas → CONTEXT_V2 selector`

Die bestehende Learning Engine und Strategy × State Matrix wurden wiederverwendet.

Für neue Trade-Like-Che-CONTEXT_V2-Decisions kann jetzt nachvollzogen werden:

- Base Strategy Score
- Market-State Evidence Delta
- Memory Learning Delta
- Final Strategy Score
- WITHOUT_MEMORY Decision
- WITH_MEMORY Decision
- was sich geändert hat
- warum es sich geändert hat

CURRENT bleibt Kontrollpfad und wurde nicht verändert.

Counterfactual / NO_TRADE wird nicht als ausgeführter Trade gezählt.

Fokussierte Runtime-/Canonical-/Learning-Tests: **75 PASS**.

## Trade Like Che WebUI und V1/V2-Trennung

Die Trade-Like-Che-Ansicht wurde auf mehreren Ebenen repariert.

Bestätigte Fixes:

- CURRENT und CONTEXT_V2 verwenden die richtige Canonical Decision Identity
- vorhandene Settlement-/Capture-Evidence wird nicht mehr durch leere Compact-Projektionen überschrieben
- `PENDING_HORIZON_SETTLEMENT` wird als offener Lernhorizont statt als falsche Exit-Quality dargestellt
- NO_TRADE-Gründe und State-/Context-Felder sind sichtbar
- Variantenwahl bleibt nach Refresh erhalten
- Filter bleiben nach Refresh erhalten
- Scrollposition bleibt nach Refresh erhalten
- CURRENT-/CONTEXT_V2-Compare-KPIs werden getrennt projiziert
- `127.0.0.1`, `algosphere.intern` und `algoshere.intern` wurden im Browser auf demselben ausgelieferten WebUI-Stand geprüft

Auch der Tabellenvertrag wurde vereinheitlicht:

- Haupttext: 14 px
- Nebentext: 12 px
- kompakte Zeilen mit Ellipsis
- vollständige Langtexte per Tooltip
- interner Tabellen-Scroll statt die gesamte Seite breit zu ziehen

Ein browser-geprüfter Zwischenstand zeigte:

- CONTEXT_V2: Decisions 40, Settled 32, Memory 40
- CURRENT: Decisions 72, Settled 77

Diese Zahlen sind UI-/Runtime-Evidence und noch kein Beweis, dass die historische Canonical-Population vollständig vergleichbar ist.

## Research-Storage Root Cause

Die lokale SQLite-Datenbank wurde mit rund 62 GB gemessen; `research_runs` verursacht einen großen Anteil.

Wichtig: Klassische Content-Deduplizierung ist **nicht** die Lösung:

- 418 Runs
- 329 Runs mit `active_strategies`
- 328 einzigartige Active-Strategy-Snapshots
- ca. 33,93 GB inline
- Einsparung durch identische Content-Deduplizierung: ca. 0 GB

Das echte Future-Writer-Problem waren doppelte Repräsentationen in jedem Strategy-Snapshot.

`ResearchDB._decode_strategy()` stellt dekodierte Werte und deren physische `*_json`-Aliases bereit; `snapshot_run_strategies()` kopierte bisher beides.

Bestätigte Duplikate:

- `metrics` + `metrics_json`
- `thresholds` + `thresholds_json`
- `setup_params` + `setup_params_json`
- `exit_policy` + `exit_policy_json`
- `feature_columns` + `feature_columns_json`

Der Future-Writer speichert künftig nur die kanonisch dekodierte Repräsentation; alte Summaries bleiben lesbar.

Repräsentative geschätzte Größenreduktion:

- vorher: ca. 134,50 MB
- nachher: ca. 65,33–71,71 MB
- nominale Reduktion: ca. 49 %

Keine alten DB-Zeilen wurden migriert oder gelöscht. Kein VACUUM wurde ausgeführt.

## Research-Evidence-Handoff

Ein zweiter Research-seitiger Gap wurde vor Canonical Memory gefunden:

`research_runs.summary_json → normalize_report() → standardized experiments`

Der normale QUICK-Handoff rief `normalize_report()` ohne den direkten Run-Summary-Pfad auf. Die Projektion übernahm bisher hauptsächlich `rows/results`; wertvolle Active-Strategy-Evidence wie Nested-Fold- und Strategy-Contract-Provenienz ging vor dem Handoff verloren.

Der bestehende Research-Handoff projiziert jetzt kompakt:

- Artifact-/Strategy-Identität
- Nested-Fold-Metriken
- Data-/Code-/Execution-Identität
- Baseline-/Stress-Evidence
- Hashes für Setup / Thresholds / Exit-Policy / Feature-Columns

Die vollständigen `active_strategies` werden **nicht** in Canonical Memory kopiert.

Der Patch ist future-only. Seitdem existiert noch kein natürlicher Research-/QUICK-Handoff, daher bleibt der Forward-Proof:

`AWAITING_REAL_RUN`

Eine historische Reprojektion ist aktuell nicht erforderlich.

## Was offen bleibt

1. Den scoped historischen PAPER/TLC-Exact-only-Repair erst ausführen, wenn der SQLite-Writer kontrolliert pausiert werden kann; den Lock nicht umgehen.
2. PAPER-CURRENT-Populationsmismatch klären, bevor Learning-Populationen als vollständig vergleichbar gelten.
3. Den neuen Research-Handoff beim nächsten natürlichen QUICK-/Research-Run beweisen.
4. Population-/Variant-/State-Contract für neue Canonical Writes vollständig schließen; historische Lücken klassifizieren, nicht erfinden.
5. V1-vs-V2-Outcomes weiter prospektiv sammeln; aktuelle UI-Zahlen reichen nicht für „V2 ist besser“.
6. ML-Uplift bleibt offene wissenschaftliche Frage; Infrastrukturfortschritt beweist keine bessere Prognose.
7. WebUI weiter vereinfachen, besonders übergroße Header-/Filterbereiche reduzieren, ohne stabilen State und lesbare Tabellen zu verlieren.
8. Den neuen Future-Writer für Research-Snapshots beibehalten; jede historische Storage-Bereinigung bleibt eine separate evidenzbasierte Migrationsentscheidung.

## Sicherheitsgrenze

`LIVE=false` · `REAL_CAPITAL=0` · automatische Promotion deaktiviert.

Kein Dokumentationsupdate autorisiert Live-Trading, erzwungene historische Reparaturen, automatische Modellpromotion oder Echtgeld-Ausführung.

[Aktueller Status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Dokumentierte Arbeiten](../docs/progress/COMPLETED_WORK.md) · [Testergebnisse](../docs/verification/TEST_RESULTS.md)
