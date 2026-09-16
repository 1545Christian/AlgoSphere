# AlgoSphere

Unabhängiges Krypto-ML-Forschungs- und Engineering-Projekt.

Aufbau, Test und Dokumentation eines Weges von Research und Backtesting zu Paper- und Shadow-Ausführung.

English: [README.md](README.md)<br>
Aktueller Status: [CURRENT_STATUS.md](CURRENT_STATUS.md)<br>
Neuestes Update: [deutsches Statusupdate](updates/2026-09-17-public-status_DE.md)<br>
Telegram: https://t.me/AlgoSphereOfficial

## Was AlgoSphere ist

AlgoSphere ist ein unabhängiges Forschungs- und Entwicklungsprojekt. Aktuelles Ziel ist ein konsistenter und nachvollziehbarer Weg von Research und Backtesting bis Paper-/Shadow-Ausführung, mit sauberer Trennung zwischen Trading, Research, OpenAI-Analyse, ML-Selektion und Evidenz/Memory.

## Aktuell geprüfter Stand

| Bereich | Aktueller Stand |
|---|---|
| Training | **Pausiert** |
| Factory / Hypothesis Producer | **Pausiert** |
| Active Paper | Läuft / fail-closed |
| Research Watch | Läuft / No-Capital-Research-Pfad |
| Research Forward | **Runtime-Recovery noch offen wegen direktem Bitget-Socket `WinError 10013`** |
| OpenAI AI-only | V2 Multi-Szenario-Analyst aktiv; weitere kausale Settlements nötig |
| Trade Memory | Für ausgeführte Trades über Paper / Watch / Research Forward / OpenAI vereinheitlicht |
| WebUI | Wichtige Projektions-/Layoutfehler repariert; breiter finaler Browser-Audit noch offen |
| Live-Trading | **Nein** |
| Echtgeld | **0** |
| Automatische Promotion | **Nein** |

Das Projekt bleibt fail-closed. Kein Dokumentationsupdate autorisiert Live-Trading oder Echtgeld-Ausführung.

## Was zuletzt wirklich besser wurde

- OpenAI nutzt jetzt `OPENAI_AI_MARKET_ANALYST_V2` mit unabhängiger Multi-Szenario-Analyse statt lokaler Richtungsübernahme.
- Ein falscher Stale-Data-Zustand wurde repariert: Signalalter soll nicht mehr mit der Frische der zugrunde liegenden Futures-Kerzen verwechselt werden.
- Die OpenAI-Paid-Call-Cadence unterscheidet jetzt erfolgreiche Calls von blockierten Versuchen.
- Offene Coins werden bis Close/Settlement von doppelten OpenAI-Entry-Analysen ausgeschlossen.
- Paper / Watch / Research Forward / OpenAI ausgeführte Trades verwenden einen vergleichbaren Memory-Vertrag.
- Unbekannte historische Werte werden explizit typisiert statt stillschweigend als 0 behandelt.
- Trade-Like-CHE Entry-Preis-Projektion, ADX-Anzeige, kompakte IDs, Capture-Projektion und OpenAI-NO_TRADE-Projektion wurden repariert oder verbessert.

## Aktueller Hauptblocker

Der jüngste Arbeitsstand zeigt, dass Research Forward bei einem direkten Bitget-Refresh mit `WinError 10013` abbrechen kann, obwohl der zentrale Market-Data-Loader bereits frische 1-Minuten-Futuresdaten besitzt.

Die vorgesehene Reparatur bleibt im bestehenden gemeinsamen Reader: Bei direktem Socket-Ausfall darf nur nach strenger Frische-/Verfügbarkeitsprüfung der zentral bestätigte Hot-File-Tail verwendet werden. Dafür fehlt noch der endgültige Restart-/Runtime-Nachweis.

## ML-Lifecycle

Der beabsichtigte Lifecycle bleibt:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

`candidate_eligible` ist Metadatum/Eligibility, keine eigene operative Stufe.

Rule-Evidenz muss unabhängig vom Erfolg eines ML-Selectors erhalten bleiben. **ML-Selector-Kollaps ist nicht Rule-Failure.**

## Hier beginnen

| Zweck | Dokument |
|---|---|
| Aktueller Stand und Hauptblocker | [CURRENT_STATUS.md](CURRENT_STATUS.md) |
| Neuestes geprüftes Update | [Update vom 17. September](updates/2026-09-17-public-status_DE.md) |
| Tests und Prüfgrenzen | [Testergebnisse](docs/verification/TEST_RESULTS.md) |
| Offene Arbeit und Prioritäten | [Roadmap](docs/progress/ROADMAP.md) |
| Dokumentierte Arbeiten | [Completed Work](docs/progress/COMPLETED_WORK.md) |
| Projektgeschichte | [Projektgeschichte](docs/project/PROJECT_HISTORY.md) |
| Evidenzhilfe | [Evidenzübersicht](evidence/EVIDENCE_SUMMARY.md) |

Alle datierten [Updates](updates/) durchsuchen.

## Öffentlich / privat

Dieses Repository ist ein öffentlicher Dokumentations- und Evidenznachweis. Es enthält nicht den privaten Anwendungscode, Zugangsdaten, Konto-Konfiguration, Marktdatenbanken, Modelle oder proprietäre Strategieparameter.

Codex und ChatGPT unterstützen Implementierung, Fehlersuche, Review und Dokumentation, aber AlgoSphere soll unabhängig von Codex laufen. Runtime-/Trading-Betrieb darf nicht davon abhängen, dass eine AI-Coding-Session aktiv ist.

## Hinweis zur Veröffentlichung

Der automatische Nightly-Publisher bleibt vom Operator pausiert, weil seine Narrative-Source-Selection zuvor veraltete Entwicklungsstände weitergezogen hat. Der Stand vom 17. September wurde manuell geprüft.

## Künftige Nutzung

AlgoSphere soll langfristig ein kontrolliertes Research-to-Execution-System für die eigene Nutzung werden. Jede spätere Live-Nutzung erfordert ausdrückliche menschliche Freigabe, vollständige Runtime-/Daten-/Risiko-Prüfung und unabhängige Schutzmechanismen. Aktuell ist Live-Trading nicht aktiviert; Rentabilität oder ein bestimmtes Ergebnis werden nicht versprochen.

## Unterstützung und Disclaimer

Kurze Hinweise: [Telegram](https://t.me/AlgoSphereOfficial). Freiwillige Unterstützung: [GitHub Sponsors](https://github.com/sponsors/1545Christian). Sponsoring ist keine Investition und vermittelt keine Trading-Signale, Anlageberatung, Eigentumsrechte, Rendite oder Ergebnisgarantie. Siehe den vollständigen [Disclaimer](docs/legal/DISCLAIMER.md).
