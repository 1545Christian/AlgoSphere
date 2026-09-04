# Öffentliches Status-Update — 2026-09-04

English: [Public status update](./2026-09-04-public-status.md)

<!-- AUTO_VALUES_START -->
## Kurzfassung

v117 trennt Trainingsautorität, Evaluation, History/Cache und OpenAI-Kostenkontrolle klarer. Der Nachtlauf veröffentlicht künftig verständlich, was umgesetzt wurde, was tatsächlich verifiziert ist und was noch offen bleibt.

## Was AlgoSphere fachlich leisten soll

- Lokales ML-Training soll selbständig laufen, neue Strategien finden und identische Experimente semantisch deduplizieren.
- Paper, Research Forward, Watch, Challenger, Champion und OpenAI bleiben fachlich getrennte Rollen mit gemeinsamer nachvollziehbarer Decision-/Risk-/Exit-Kette.
- Memory soll Trainings- und Outcome-Wissen standardisiert schreiben und später nachweislich für neue Hypothesen und Auswahlentscheidungen lesen.
- WebUI soll pro Kachel eine vertrauenswürdige Datenquelle zeigen, Rollen nicht vermischen und Training/Markt/OpenAI verständlich darstellen.
- Kein Live-Trading oder Real-Capital-Pfad wird automatisch freigegeben; Promotion bleibt fail-closed bis zum erforderlichen Betriebsnachweis.

## In v90_8_10_117 umgesetzt

- `LOCAL_ML_AUTOPILOT` ist die einzige normale Trainings-Startautorität; Research Forward wird als `--evaluate-only`-Evaluator geführt und soll keinen zweiten Trainingsstart erzeugen.
- `training_forensic_hold` wurde aus dem Normalbetrieb entfernt; Ressourcen- und Crash-Schutz bleiben getrennt bestehen.
- QUICK → BALANCED bleibt als autonomer Folgepfad im Local-ML-Autopilot erhalten.
- History-Sync wurde auf einen Vollscan pro Lauf plus gezielte neue Archive und gebündelte Ledger-Lookups umgestellt.
- Der gemeinsame FeatureCache-Identitätsvertrag lautet `v90_8_5_117_unified_feature_cache_contract_1`; alte Cache-Namensräume werden getrennt behandelt.
- Codex-/Candidate-Builder-/Dispatcher-Lineage wird als historische Evidence archiviert und vom normalen Runtime-Pfad nicht verwendet.
- Der v84-Vertrag für versionsunabhängiges semantisches Memory bleibt erhalten.
- OpenAI wurde auf das Standardmodell `gpt-5.6-luna`, niedrige Reasoning-Stufe und maximal 2200 Output-Tokens begrenzt; Standard-Cadence 120 Minuten, Web-News 360 Minuten, Tageslimits 12/4 Calls.
- Unveränderter OpenAI-Kontext soll keinen neuen API-Call erzeugen (`UNCHANGED_CONTEXT_SKIPPED`).
- Ein neuer immutable v117 Research-Core wird aus dem korrigierten aktuellen Source gebaut.
- Der GitHub-Nachtlauf arbeitet ohne Codex-Abhängigkeit und veröffentlicht Runtime-Status sowie menschlich geprüfte Release-Notizen getrennt.

## Für dieses Release verifiziert

- Python-Compile der geänderten/neuen Python-Dateien: PASS.
- Kern-Regressionsatz: 149 Tests PASS; exakte Installer-Testliste: 194 Tests PASS.
- Archivierungs-Probelauf: PASS; 214 Lineage-Dateien hash-verifiziert, v84-Memory erhalten, keine Quelldatei gelöscht.
- Research-Core-Probelauf: PASS.
- v117 Acceptance-Probelauf: `PASS_CODE_CONTRACT_AWAITING_RUNTIME_PROOF` — ausdrücklich noch kein vollständiger Windows-/Betriebsbeweis.

## Aktueller Betriebszustand

- Beobachteter Runtime-Release: `v90_8_10_125`.
- ML-Autopilot: `QUICK_RUNNING` · Profil `quick` · Phase `CHECKPOINT` · Symbol `MYXUSDT` · Coins `3/5`.
- Quelle des Stage-Zustands: `LIVE_STAGE_HEARTBEAT`.
- Live-Trading: `Nein` · Real-Capital-Flag: `0` · automatische Promotion: `deaktiviert`.
- Beobachteter Snapshot: `2026-09-04T22:45:00.015712Z`.

## Noch offen / noch nicht bewiesen

- P0 offen: bestehende FeatureCaches werden noch nicht inkrementell nur um neue Kerzen erweitert; dieser Punkt bleibt ausdrücklich ungelöst.
- Windows-Langlauf muss beweisen, dass QUICK ausschließlich über Local ML startet und Research Forward keinen zweiten Trainingsstart erzeugt.
- Ein echter QUICK-Abschluss mit anschließendem BALANCED-Start muss prospektiv beobachtet werden.
- History-Sync-Laufzeit und Importmengen müssen auf Windows gegen den früheren Doppelscan gemessen werden.
- OpenAI-Tageszählung, Reset, Web-Fälligkeit und `UNCHANGED_CONTEXT_SKIPPED` müssen in echten Scheduler-Läufen bestätigt werden.
- Code-PASS allein schließt keinen Punkt: `PROVEN_CLOSED` erfordert aktuellen Runtime-/Browser-/Ledger-Beweis.

## Technische Evidenz

Hashes, öffentliches Register, Prüfgrenzen und historische Artefakte bleiben separat verfügbar. Sie sind Belege und ersetzen nicht die Entwicklungszusammenfassung oben.

Siehe [Aktueller Status](../CURRENT_STATUS.md), [Testergebnisse](../docs/verification/TEST_RESULTS.md), [Roadmap](../docs/progress/ROADMAP.md) und die [Evidenzübersicht](../evidence/EVIDENCE_SUMMARY.md).
<!-- AUTO_VALUES_END -->
