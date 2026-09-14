# AlgoSphere

Unabhängiges Krypto-ML-Forschungs- und Engineering-Projekt.

Aufbau, Test und Dokumentation eines Weges von Research und Backtesting zu Paper- und Shadow-Ausführung.

English: [README.md](README.md)<br>
Aktueller Status: [CURRENT_STATUS.md](CURRENT_STATUS.md)<br>
Neuestes Update: [deutsches Statusupdate](updates/2026-09-14-public-status_DE.md)<br>
Telegram: https://t.me/AlgoSphereOfficial

## Was AlgoSphere ist

AlgoSphere ist ein unabhängiges Forschungs- und Entwicklungsprojekt. Ich arbeite seit ungefähr drei Jahren an den zugrunde liegenden Ideen und Python-Prototypen; begonnen hat es mit dem Nachbauen und Anpassen von Lernbeispielen, auch aus YouTube-Videos.

Aus dieser Lernphase entstanden mehrere eigene Python-Prototypen, die ich wiederholt überarbeitete. Heute geht es um einen konsistenten und nachvollziehbaren Weg von Research und Backtesting bis Paper- und Shadow-Ausführung.

## Aktueller Stand

| Bereich | Aktuell geprüfter Stand |
|---|---|
| Training | **Pausiert** |
| Factory / Hypothesis Producer | **Pausiert** |
| Active Paper | Läuft / fail-closed |
| Research Watch / Forward | Läuft mit No-Capital-Counterfactual-Beobachtung |
| OpenAI AI-only | Prozess aktiv; natürliche E2E-Trade-Kette noch nicht bewiesen |
| WebUI | Reparierter Prüfstand PASS, Quellversion `v90_8_10_162` |
| Live-Trading | **Nein** |
| Echtgeld | **0** |
| Automatische Promotion | **Nein** |

Das Projekt bleibt fail-closed. Bei unvollständiger Runtime-Evidenz wird kein Research-Ergebnis weiter aktiviert.

Der aktuelle Schwerpunkt liegt nicht auf breitem Retraining, sondern darauf zu beweisen, dass Paper, Watch, Research Forward, OpenAI, Exit, Outcome und Canonical Memory kausal sauber verbunden bleiben und aus der richtigen Evidenz lernen.

## Wichtige Korrekturen der letzten Tage

- Der 0,30%-Expected-Net-Guard bleibt für Paper hart, aber geblockte Research-Setup-Matches werden nun als No-Capital-Counterfactuals erhalten statt verworfen.
- Im ersten Backfill wurden 49 Counterfactuals erzeugt; 13 waren zum dokumentierten Prüfzeitpunkt bis 8h ausgewertet.
- 58 lokale 100-USDT-Trades wurden durch `Decision → Trade → Outcome → Canonical Memory` repariert, inklusive Exit-State und Post-Exit-Horizonten.
- WebUI-Liveness-/Current-Truth-Fehler wurden korrigiert.
- OpenAI bleibt Futures-only und unabhängig von lokalem ML, aber eine frische natürliche AI-only Trade→Learning-Kette ist noch nicht bewiesen.
- Training und Factory bleiben pausiert, weil Rule-Evidenz unabhängig vom Erfolg eines ML-Selectors erhalten bleiben muss.
- Der beabsichtigte Lifecycle lautet jetzt `HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`; `candidate_eligible` ist Metadatum, keine eigene operative Stufe.

Siehe [CURRENT_STATUS.md](CURRENT_STATUS.md) für den aktuellen geprüften Stand und das [Update vom 14.09.](updates/2026-09-14-public-status_DE.md) für Details.

## Was Besucher hier sehen können

Besucher können:

- den aktuellen dokumentierten Projektstand prüfen,
- bestandene und blockierte Kontrollen sehen,
- bekannte technische Probleme und offene Arbeit verfolgen,
- datierte Updates vergleichen,
- das bereinigte Evidenzregister einsehen,
- die Integrität eines öffentlichen Exports prüfen.

Dieses Repository ist ein öffentlicher Dokumentations- und Evidenznachweis. Es ist keine herunterladbare Veröffentlichung der privaten AlgoSphere-Anwendung.

## Was öffentlich ist / was privat bleibt

| Öffentlich | Privat |
|---|---|
| Status, Testgrenzen, Blocker und Geschichte | Anwendungscode und proprietäre Handelslogik |
| Roadmap, datierte EN-/DE-Updates und öffentlicher Prüfer | Zugangsdaten, Konten sowie Exchange-/Telegram-Konfiguration |
| Bereinigtes Evidenzregister | Datenbanken, Marktdaten, Modelle, Checkpoints und Strategieparameter |
| Exportintegrität | Private Logs und Runtime-Pfade |

## Hier beginnen

| Zweck | Dokument |
|---|---|
| Aktueller Stand und Hauptblocker | [CURRENT_STATUS.md](CURRENT_STATUS.md) |
| Neuestes datiertes Update | [deutsches Update](updates/2026-09-14-public-status_DE.md) |
| Tests und Prüfgrenzen | [Testergebnisse](docs/verification/TEST_RESULTS.md) |
| Offene Arbeit und Prioritäten | [Roadmap](docs/progress/ROADMAP.md) |
| Projektgeschichte | [Projektgeschichte](docs/project/PROJECT_HISTORY.md) |
| Evidenzhilfe | [Evidenzübersicht](evidence/EVIDENCE_SUMMARY.md) |

Alle datierten [Updates](updates/) durchsuchen.

## Projektgeschichte und KI-Unterstützung

Codex und ChatGPT unterstützen Implementierung, Fehlersuche, technische Prüfung und Dokumentation. Ihre Ergebnisse werden vor der Veröffentlichung geprüft und überarbeitet. Architektur, Projektentscheidungen und Verantwortung bleiben menschlich.

Weil wiederholte Codex-Übergaben Unsicherheit über den tatsächlichen Projektstand erzeugt haben, werden wichtige Anforderungen derzeit erneut gegen Code, datierte Artefakte und Tests geprüft, bevor breites Training wieder aufgenommen wird. Diese Prüfung hat bereits mehrere Fälle sichtbar gemacht, in denen ein technisch laufender Prozess noch keine bewiesene End-to-End-Lernkette bedeutete.

## Hinweis zur Veröffentlichung

Der automatische Nightly-Upload funktionierte in den letzten Tagen, aber seine Narrative-Source-Selection schleppte mehrfach ältere Texte vom 5./6. September weiter, obwohl neuere Engineering-Arbeit vorlag. Der Nightly-Publisher ist aktuell vom Operator pausiert; der Stand vom 14.09. wurde manuell geprüft, damit kein veralteter Text wieder darübergeschrieben wird.

## Künftige Nutzung

Langfristig soll AlgoSphere ein kontrolliertes Research-to-Execution-System für meine eigene Nutzung werden. Eigener Handel kommt erst infrage, wenn Daten, Runtime, Risiko und Betrieb vollständig geprüft sind. Jede spätere Live-Nutzung erfordert ausdrückliche menschliche Freigabe und unabhängige Schutzmechanismen. Aktuell ist Live-Trading nicht aktiviert. Es wird keine Handelsleistung, Rentabilität oder erfolgreiche Fertigstellung des Projekts versprochen.

## Unterstützung und Disclaimer

Kurze Hinweise: [Telegram](https://t.me/AlgoSphereOfficial). Freiwillige Unterstützung: [GitHub Sponsors](https://github.com/sponsors/1545Christian). Sponsoring ist keine Investition und vermittelt keine Trading-Signale, Anlageberatung, Eigentumsrechte, Rendite oder Ergebnisgarantie. Siehe den vollständigen [Disclaimer](docs/legal/DISCLAIMER.md).
