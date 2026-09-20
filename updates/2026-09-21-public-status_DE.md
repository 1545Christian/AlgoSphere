# Öffentliches Status-Update — 2026-09-21

English: [Public status update](./2026-09-21-public-status.md)

## Warum dieses Update

Am 20. September wurde die Entwicklung von AlgoSphere nicht wesentlich fortgesetzt. Dieses Update gleicht deshalb den letzten bewiesenen Stand aus den Projektbereichen ab, damit die öffentliche Dokumentation weder alte Blocker weiterführt noch unfertige Punkte als abgeschlossen darstellt.

## Runtime und Research Forward

Der letzte Research-Forward-Neustart-Nachweis ist deutlich stärker als frühere reine Code-Checks. Der aktuelle wissenschaftliche Overlay wird vor der Engine-Erzeugung gebunden und der laufende Prozess besitzt einen Composition-/Hash-Beleg.

- Runtime-Composition-Hashes: **35/35 PASS**
- Research Forward: live
- Strategien: **170 erwartet / 170 aktiv / 0 Dubletten**
- CURRENT-Kontrollpfad: unverändert
- WebUI bei diesem Proof: **90.8.10.199**
- CURRENT und CONTEXT_V2 bleiben sichtbar getrennt

Ein Snapshot dieses Nachweises zeigte CURRENT 19 Settled / -2,05 USDT und CONTEXT_V2 13 Settled / -0,79 USDT.

Diese Zahlen sind kein Beweis, dass V2 besser ist. Viele neue Events lieferten weiterhin NO_CURRENT_SETUP; ein kausaler Vorteil des Selector-Rankings ist damit noch nicht bewiesen.

## Canonical Memory und Learning

Der Canonical-Memory-Core und der aktuelle New-Write-Contract wurden inzwischen für den aktuellen Pfad als **PROVEN_CLOSED** gemeldet: Provenienz, Maschinen-/Menschen-/AI-Lesbarkeit, No-Parallel-Truth und Learning-Delta-Before/After sind im aktuellen Vertrag vorhanden.

Das bedeutet nicht, dass der historische Datenbestand vollständig repariert ist. Separat offen bleiben:

- PAPER/CURRENT Contribution-/Delta-Populationsmismatch im Altbestand
- historische State-/Version-Lücken
- PAPER/CONTEXT_V2 besitzt weiterhin keine vergleichbare ausgeführte Outcome-Population
- historische Exact-only-Reparatur/Backfill bleibt eine eigene Legacy-Aufgabe
- einige neue Research-Handoffs brauchen weiterhin natürlichen Forward-Proof

**Aktueller Contract geschlossen bedeutet nicht, dass der historische Altbestand vollständig normalisiert ist.**

## CONTEXT_V2 Learning

Der bestehende CONTEXT_V2-Selector konsumiert jetzt Canonical Learning Delta statt nur Market-State/Context-Fit. CURRENT bleibt Kontrollpfad.

Der Anschluss ist technisch hergestellt und getestet. Eine fachliche Trading-Verbesserung bleibt **INSUFFICIENT_EVIDENCE**, bis natürliche Multi-Candidate-/Settlement-Evidence vorliegt.

## Market Intelligence und Training

Der Full-History-ENA-1-Coin-Pilot bleibt das wichtigste aktuelle Trainingsergebnis:

- RULE_VS_ML = DEGRADED
- candidate_eligible = false
- keine Challenger-Promotion
- keine automatische Promotion
- Rule-Evidence bleibt erhalten

Der Robustness Gate bleibt die notwendige Evidenzschicht vor einer späteren Challenger-Aussage. Breites Multi-Coin-Training bleibt zurückgestellt.

## Research-Evidence-Handoff

Der Research→Standardized-Memory-Handoff wurde future-only repariert. Kompakte Candidate-/Rule-/Nested-Fold-/Contract-Evidence geht nicht mehr vor der Canonical-Memory-Grenze verloren.

Der Contract ist strukturell getestet, aber FUTURE_RESEARCH_HANDOFF_PROVEN bleibt **AWAITING_REAL_RUN**. Nur für diesen Proof soll kein zusätzlicher Trainingslauf gestartet werden.

## Storage / Datenbank

Die lokale Datenbank war auf rund 62 GB angewachsen; research_runs verursachte davon ungefähr 35 GB.

Die Active-Strategy-Snapshots sind überwiegend einzigartig. Klassische Content-Deduplizierung ist daher nicht die Lösung. Der Future-Writer wurde korrigiert, sodass dekodierte kanonische Werte nicht mehr zusammen mit identischen physischen *_json-Aliasfeldern gespeichert werden.

Repräsentative Evidence deutet auf ungefähr **49 % kleinere zukünftige große Snapshots**. Historische Zeilen wurden weder gelöscht noch migriert oder vacuumed.

Retention/Compaction bleibt eine spätere getrennte Aufgabe, weil Checkpoints, Completion Marker und Artifact-Referenzen wissenschaftliche Evidence sicher erhalten müssen.

## WebUI

Trade Like Che / Research sind deutlich klarer: CURRENT und CONTEXT_V2 getrennt, Filter/Variante/Scrollposition bleiben bei Refresh erhalten, Langtexte nutzen Tooltips, und lokale IP plus konfigurierte Aliase lieferten denselben akzeptierten Build.

Die gesamte produktartige Informationsarchitektur gilt trotzdem noch nicht als abgeschlossen. Große Historien brauchen weiterhin sauberere Pagination/Virtualisierung und einzelne Seiten bleiben zu dicht.

## OpenAI AI-only

Der AI-only-Pfad bleibt unabhängig: OpenAI ist in dieser Lane der finale fachliche Trading-Entscheider; der lokale Code soll nach einem gültigen AI-Plan keine zweite Tradingentscheidung treffen.

Der Input-Contract enthält den vorgesehenen Multi-Timeframe-Kontext, BTC/ETH, News, Market Structure/Support-Resistance, Learning Memory und aktuellen OpenAI-Positionskontext.

Offene Positionen werden lokal überwacht und sollen nicht allein wegen ihres Fortbestehens periodisch neue Paid Calls auslösen.

Der kompakte Single-Plan-Request braucht weiterhin normalen Forward-Proof. Die tatsächliche OpenAI-Decision-Qualität und Profitabilität sind **nicht bewiesen**. Die frühere positive PnL-Darstellung darf nicht als Profit-Evidence verwendet werden.

## Demo / Packaging / Release

Demo und Distribution sind **nicht fertig** und werden ausdrücklich als eigener Release-Bereich geführt.

Aktueller Status: **OPEN / BLOCKED**

Vor einer belastbaren öffentlichen/Client-Demo fehlen weiterhin:

- saubere Isolation von Offline Demo und Connected Demo
- keine ungewollte Aktivierung von Training, OpenAI-Paid-Calls, Live-Trading oder Echtgeld
- Approved-/signierter Model-Bundle-Vertrag statt "neuestes Modell"
- Demo-/Testnet-End-to-End-Proof
- Decision → Entry → Exit → Outcome → Reconnect/Recovery-Proof
- produktartige WebUI-/Client-Oberfläche
- Installer / Update / Rollback / Config / Logs
- Entscheidung lokaler PC vs Remote-WebUI/Server
- späterer Webspace-/Server-Deployment-Vertrag
- sichere Credential-Verwaltung
- explizite Read-only-Exchange-Rechte, wo vorgesehen
- Release-Integrity, Lizenz/Terms/Disclaimer und Distribution-Profile-Isolation

**Demo Connected ≠ Live.**
**Bitget Read-only ≠ Trading-Berechtigung.**
**LAST_APPROVED_MODEL_BUNDLE ≠ zuletzt trainiertes Modell.**

Normal-Futures-Live-Readiness bleibt spätere Arbeit hinter Demo-/Stabilitätsnachweis. Elite/UTA bleibt bis nach stabilem Normal Futures zurückgestellt.

## Was wissenschaftlich offen bleibt

Mehr Infrastruktur funktioniert, aber dauerhafter Prognose-/Trading-Uplift ist noch nicht bewiesen:

- ENA-ML schlug die erhaltene Rule-Baseline nicht
- V2-Selector-Vorteil ist noch nicht durch genügend natürliche Candidate-/Outcome-Evidence bewiesen
- OpenAI-Qualität ist noch nicht durch genügend kausale Settlements bewiesen
- ein neu durchlaufener Challenger-/Champion-Zyklus ist noch nicht belegt

## Öffentliche Sicherheitsgrenze

- Live-Trading: **deaktiviert**
- Echtgeld: **0**
- Automatische Promotion: **deaktiviert**
- Demo-Release: **nicht bereit**
- Elite/UTA: **zurückgestellt**

Kein Dokumentationsupdate autorisiert Live-Trading, Echtgeld-Ausführung, automatische Modellpromotion oder Release-Readiness.

[Aktueller Status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Dokumentierte Arbeiten](../docs/progress/COMPLETED_WORK.md) · [Testergebnisse](../docs/verification/TEST_RESULTS.md)