# AlgoSphere

**AI × Quant Research für Kryptomärkte**

Unabhängiges Forschungs- und Engineering-Projekt für datengetriebene Marktanalyse, Machine Learning, Decision Intelligence, kanonisches Learning und kontrollierte Research-to-Execution-Workflows.

English: [README.md](README.md)<br>
Aktueller Status: [CURRENT_STATUS.md](CURRENT_STATUS.md)<br>
Neuestes geprüftes Update: [21. September 2026](updates/2026-09-21-public-status_DE.md)<br>
Telegram: https://t.me/AlgoSphereOfficial<br>
Neu hier? [Hier anfangen](docs/START_HERE_DE.md) · [Architektur](docs/project/ARCHITECTURE_OVERVIEW_DE.md) · [Dokumentationsübersicht](docs/README.md)

> **Hinweis zum öffentlichen Repository:** Hier werden das Projekt und ausgewählte Evidence dokumentiert. Dieses Repository ist kein Download der privaten AlgoSphere-Trading-Anwendung.

## Überblick

AlgoSphere verbindet quantitative Marktanalyse, Market-State- und Regime-Research, Rule- und ML-Validierung, kanonische Decision → Outcome → Learning-Evidence, OpenAI-gestützte Analyse, Paper-/Shadow-Ausführung, Lifecycle-Governance und spätere Demo-/Packaging-/Release-Arbeit.

Im Mittelpunkt stehen Reproduzierbarkeit, kausale Auswertung, eindeutige Lineage und der Erhalt positiver wie negativer Evidence.

## Wohin sich AlgoSphere entwickeln soll

AlgoSphere wird zu einem konfigurierbaren quantitativen Research- und Trading-Analyse-System entwickelt, das über ein breites Universum von Kryptomärkten arbeiten kann.

Das langfristige Ziel ist nicht, ein Modell oder eine Strategie auf jeden Coin zu zwingen. Das System soll anhand messbarer Evidence lernen:

- was bei einem bestimmten Coin, einer Side, Marktphase und einem Horizont funktioniert
- wann eine Rule-Strategie stärker ist als ML
- wann ein Modell neu trainiert oder revalidiert werden sollte
- wann eine Strategie im Research bleiben muss statt promotet zu werden
- und wann **NO_TRADE** die bessere Entscheidung ist

Marktanalyse, Strategie-Research, ML-Training, Validierung und evidenzbasierte Anpassung sollen mit der Zeit stärker automatisiert werden. Promotion, Execution-Berechtigungen und jede spätere Echtgeld-Nutzung bleiben trotzdem ausdrücklich geregelt.

Die Coins in aktuellen Berichten sind Arbeits-Populationen und nicht das spätere Limit. Langfristig soll das Coin-Universum einstellbar sein — innerhalb der Grenzen von Daten, Rechenleistung, Liquidität, Qualität und Exchange-Unterstützung.

Mehr dazu: [Projektrichtung](docs/project/PROJECT_DIRECTION_DE.md).

## Research-Lifecycle

HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION

candidate_eligible ist Eligibility-Metadatum und keine eigene operative Stufe. Rule-Evidence bleibt unabhängig vom Erfolg des ML-Selectors erhalten.

Ein neueres Modell wird nicht allein deshalb aktiv, weil es neuer ist. Promotion soll von reproduzierbarer Evidence und kontrolliertem Vergleich abhängen.

## Aktuell geprüfter Stand

| Bereich | Aktueller Stand |
|---|---|
| Active Paper | Läuft / fail-closed |
| Paper Context V2 Shadow | Aktiv |
| Research Watch | Läuft / No-Capital-Research-Pfad |
| Research Forward / Trade Like Che CURRENT | Läuft |
| Trade Like Che Context V2 | Active Shadow / Runtime-Hash-Proof vorhanden |
| CONTEXT_V2 Learning | Canonical Learning Delta an Selector angeschlossen |
| Canonical Memory Core | **Aktueller Contract PROVEN_CLOSED** |
| Historische Canonical-Reparatur | Scoped Backfill committed; exakte Reparatur durchgeführt, soweit beweisbar |
| Market Intelligence V2.1 | Research-Baseline vorhanden |
| ENA 1-Coin-Pilot | Abgeschlossen; Rule vs ML = DEGRADED; keine Promotion |
| Robustness Gate | Implementiert / evidenzgesteuert |
| Research Handoff | Future-Projektion kompakter Candidate-/Rule-Evidence repariert; natürlicher Run-Proof steht aus |
| Research Storage | Future-Writer + Summary-Identity verbessert; Legacy-Compaction nicht freigegeben |
| OpenAI AI-only | Aktiv; Decision-Qualität weiterhin nicht bewiesen |
| WebUI | letzter geprüfter Research-Forward-Proof: v90.8.10.199 |
| Demo / Packaging / Release | **OPEN / BLOCKED** |
| Live-Trading | Deaktiviert |
| Echtgeld | 0 |
| Automatische Promotion | Deaktiviert |

Details zu Status und offenen Punkten stehen in [CURRENT_STATUS.md](CURRENT_STATUS.md).

## Evidence und Transparenz

AlgoSphere veröffentlicht ausgewählte geprüfte Projektstände, Research-Zusammenfassungen, Verifikationsergebnisse, Evidence, Entwicklungshistorie und bekannte Grenzen.

Negative Ergebnisse bleiben sichtbar. Technischer Abschluss wird nicht als Beweis für Modellqualität, Profitabilität oder Live-Readiness dargestellt.

## Öffentlich / privat

Dieses Repository ist die **öffentliche Dokumentations- und Evidence-Schicht** von AlgoSphere.

Es enthält Projektdokumentation, ausgewählte öffentliche Evidence-Exporte und kleine öffentliche Verifikationswerkzeuge. Es enthält **nicht** den privaten Anwendungs-/Runtime-Code, Zugangsdaten, Kontokonfiguration, private Marktdatenbanken, trainierte Model Bundles oder proprietäre Strategieparameter.

Eine öffentliche AlgoSphere-Anwendung wird derzeit nicht über dieses Repository zum Download angeboten.

Die öffentliche Dokumentation/Evidence steht unter CC BY-SA 4.0; die kleinen öffentlichen Verifikationswerkzeuge unter MIT. Keine dieser Lizenzen gilt für die private AlgoSphere-Anwendung oder nicht veröffentlichte Projektinhalte.

Siehe [Umfang des öffentlichen Repositorys](docs/project/PUBLIC_REPOSITORY_SCOPE_DE.md) und [Lizenzierung](docs/legal/LICENSING.md).

## Dokumentation

| Thema | Dokument |
|---|---|
| Hier anfangen | [docs/START_HERE_DE.md](docs/START_HERE_DE.md) |
| Architekturüberblick | [docs/project/ARCHITECTURE_OVERVIEW_DE.md](docs/project/ARCHITECTURE_OVERVIEW_DE.md) |
| Projektrichtung | [docs/project/PROJECT_DIRECTION_DE.md](docs/project/PROJECT_DIRECTION_DE.md) |
| Öffentlicher Repository-Umfang | [docs/project/PUBLIC_REPOSITORY_SCOPE_DE.md](docs/project/PUBLIC_REPOSITORY_SCOPE_DE.md) |
| Aktueller Status | [CURRENT_STATUS.md](CURRENT_STATUS.md) |
| Neuestes geprüftes Update | [Update vom 21. September](updates/2026-09-21-public-status_DE.md) |
| Roadmap | [docs/progress/ROADMAP.md](docs/progress/ROADMAP.md) |
| Dokumentierte Arbeiten | [docs/progress/COMPLETED_WORK.md](docs/progress/COMPLETED_WORK.md) |
| Projektgeschichte | [docs/project/PROJECT_HISTORY.md](docs/project/PROJECT_HISTORY.md) |
| FAQ | [docs/FAQ_DE.md](docs/FAQ_DE.md) |
| Verifikation | [docs/verification/TEST_RESULTS.md](docs/verification/TEST_RESULTS.md) |
| Evidence-Übersicht | [evidence/EVIDENCE_SUMMARY.md](evidence/EVIDENCE_SUMMARY.md) |
| Mitmachen | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Support | [SUPPORT.md](SUPPORT.md) |
| Security | [SECURITY.md](SECURITY.md) |
| Lizenzierung | [docs/legal/LICENSING.md](docs/legal/LICENSING.md) |
| Zitierhinweis | [CITATION.cff](CITATION.cff) |
| Disclaimer | [docs/legal/DISCLAIMER.md](docs/legal/DISCLAIMER.md) |

Datierte [Updates im Archiv](updates/README.md) ansehen.

## Fragen, Ideen und Feedback

AlgoSphere ist auch deshalb öffentlich dokumentiert, damit Research nachvollzogen, hinterfragt und verbessert werden kann.

Hilfreich sind reproduzierbare Bugreports, Dokumentationskorrekturen, Research-Fragen, relevante Papers/Methoden und Verbesserungsideen, die sich fair testen lassen.

Für Bugs, Research-Fragen und Ideen gibt es strukturierte GitHub-Issue-Vorlagen. Bitte vorher [CONTRIBUTING.md](CONTRIBUTING.md) lesen.

## Öffentliche Updates

Kürzere Entwicklungs- und Research-Updates erscheinen auch auf Telegram:

https://t.me/AlgoSphereOfficial

## Disclaimer

AlgoSphere ist ein Forschungs- und Engineering-Projekt. Nichts in diesem Repository ist Finanz- oder Anlageberatung. Krypto- und Derivatehandel sind mit erheblichen Risiken verbunden. Historische, simulierte oder Paper-Ergebnisse garantieren keine zukünftigen Ergebnisse.

Siehe den vollständigen [Disclaimer](docs/legal/DISCLAIMER.md).

Freiwillige Unterstützung: [GitHub Sponsors](https://github.com/sponsors/1545Christian). Sponsoring ist keine Investition und vermittelt keine Trading-Signale, Eigentumsrechte, Rendite oder Ergebnisgarantie.
