# AlgoSphere FAQ

Kurze, verständliche Antworten auf Fragen, die zum Projekt häufig auftauchen.

## Was ist AlgoSphere?

AlgoSphere ist ein unabhängiges AI-×-Quant-Forschungs- und Engineering-Projekt für Kryptomärkte.

Untersucht wird, wie Market Context, regelbasierte Strategien, Machine Learning, OpenAI-gestützte Analyse, Canonical Memory sowie Paper-/Shadow-Ausführung so zusammenarbeiten können, dass Ergebnisse messbar und nachvollziehbar bleiben.

AlgoSphere wird nicht als fertiges Trading-Produkt dargestellt.

## Handelt AlgoSphere bereits live mit Echtgeld?

Nein.

Der aktuell veröffentlichte Stand bleibt:

- Live-Trading: deaktiviert
- Echtgeld: 0
- automatische Modell-Promotion: deaktiviert
- Demo-Release: noch nicht bereit

Paper- und Shadow-Pfade werden für Research und Validierung genutzt.

## Ist das ein Signal-Service?

Nein.

Das öffentliche Repository und der Telegram-Kanal dokumentieren Entwicklung und Forschung. Sie sind kein Trading-Signal-Service und keine Anlageberatung.

## Ist der komplette Quellcode öffentlich?

Nein.

Dieses Repository ist die öffentliche Dokumentations- und Evidence-Schicht.

Privater Anwendungscode, Zugangsdaten, Kontokonfiguration, Marktdatenbanken, trainierte Modelle und proprietäre Strategieparameter werden nicht veröffentlicht.

## Ist das ML bereits besser als das Rule-System?

Nicht bewiesen.

Der aktuelle ENA-1-Coin-Pilot lief technisch vollständig durch, aber der ML-Selector war schwächer als die erhaltene Rule-Baseline. Deshalb erfolgte keine Promotion.

Dieses negative Ergebnis bleibt bewusst sichtbar.

## Was ist CURRENT und was ist CONTEXT_V2?

CURRENT ist der Kontrollpfad.

CONTEXT_V2 ist eine Shadow-Research-Variante, die Market-State-Kontext und Canonical-Learning-Delta-Evidence bei der Strategieauswahl berücksichtigen kann.

Beide Pfade bleiben getrennt, damit Evidence nicht still vermischt wird.

## Ist CONTEXT_V2 besser?

Noch nicht bewiesen.

Dafür gibt es bisher nicht genügend natürliche, vergleichbare und abgeschlossene Outcomes.

## Was bedeutet Canonical Memory?

Canonical Memory ist die gemeinsame Evidence-Schicht für Decisions, Trades, Outcomes und Learning.

Damit sollen Fragen nachvollziehbar beantwortet werden können wie:

- Welche Decision führte zu diesem Trade?
- Welche Strategie und Marktphase waren beteiligt?
- Was geschah nach dem Entry?
- Was wurde aus dem Outcome gelernt?
- Hat diese Evidence spätere Entscheidungen verändert?

## Welche Rolle hat OpenAI?

OpenAI wird als unabhängige Analyseebene im AI-only-Research-Pfad genutzt.

Innerhalb dieser Lane soll ein gültiger AI-Plan nicht anschließend durch eine zweite lokale Trading-Engine fachlich neu entschieden werden.

Die tatsächliche OpenAI-Decision-Qualität und Profitabilität sind weiterhin nicht bewiesen.

## Warum werden negative oder fehlgeschlagene Ergebnisse veröffentlicht?

Weil ein Research-System wenig wert ist, wenn nur gut aussehende Resultate erhalten bleiben.

FAILED_OOS, unzureichende Evidence, degradierte ML-Ergebnisse und offene Grenzen gehören deshalb zum Projektstand.

## Was bedeutet Demo / Packaging / Release?

Das ist ein eigener zukünftiger Arbeitsbereich, um Teile von AlgoSphere kontrolliert als Demo-/Client-Erlebnis bereitzustellen.

Demo bedeutet nicht Live.

Vor einem Release fehlen unter anderem Offline-/Connected-Demo-Isolation, Approved Model Bundles, Demo/Testnet-End-to-End-Proof, Installer/Update/Rollback, sichere Credentials und Release-Integrity.

## Kann ich helfen?

Ja — besonders hilfreich sind:

- reproduzierbare Bugreports
- Hinweise auf veraltete oder missverständliche Dokumentation
- Research-Fragen mit klarer Hypothese
- relevante Papers oder Methoden
- Hinweise auf Widersprüche zwischen öffentlichem Status und Evidence

Bitte vorher [CONTRIBUTING.md](../CONTRIBUTING.md) lesen.

## Wo anfangen?

- [README](../README_DE.md)
- [Aktueller Status](../CURRENT_STATUS.md)
- [Neuestes Update](../updates/2026-09-21-public-status_DE.md)
- [Roadmap](progress/ROADMAP.md)
- [Evidence-Übersicht](../evidence/EVIDENCE_SUMMARY.md)
