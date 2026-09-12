# Öffentliches Status-Update — 2026-09-12

English: [Public status update](./2026-09-12-public-status.md)

## Zusammenfassung

In den letzten Tagen ging es vor allem darum, den Daten- und Evidenzpfad rund um die OpenAI-Forschung sauber zu korrigieren — nicht darum, eine alte Equity-Kurve im Nachhinein besser aussehen zu lassen.

Der wichtigste Befund: Mehrere Annahmen aus dem früheren OpenAI-Vergleich waren zu optimistisch oder technisch nicht sauber genug belegt. Gefunden wurden gemischte Spot-/Futures-Eingaben, veralteter Coin-Kontext, ein historisches Problem bei der Interpretation von Exit-Zeitpunkten und eine Vergleichslogik, die aus einer OpenAI-Richtung zu schnell einen Trade ableiten konnte, obwohl der Text selbst teilweise noch auf Bestätigung oder Pullback wartete.

Daraus wurde die aktive Richtung geändert. Der OpenAI-Paper-Pfad wurde als prospektiver **AI-only Futures-Pfad** neu aufgebaut: mit unveränderlichen Entscheidungssnapshots, kausaler Zeitbindung und einem einheitlichen **100-USDT-/12-bps-Vertrag**. Der historische Vergleich bleibt als Forschungsreferenz erhalten, wird aber nicht mehr ungeprüft als Performance-Wahrheit behandelt.

## Was sich zwischen dem 8. und 11. September geändert hat

### Research / Forward: Warm-up und sichtbare Outcomes

Im Research-Pfad wurde ein Warm-up-Problem korrigiert. Zuvor konnte ein Lauf so aussehen, als gäbe es schlicht keine Ergebnisse, obwohl für die Bewertung noch nicht genügend Historie vorlag. Nach der Korrektur wurden wieder frische Zyklen und Outcomes sichtbar.

Das ist wichtig, weil ein Research-System sauber unterscheiden muss zwischen **„es gab kein Setup“** und **„die Pipeline hatte noch nicht genug Daten, um überhaupt eines zu prüfen“**.

### Kanonische Outcomes: vom Zwischenstand 50 USDT zur aktiven 100-USDT-Basis

Zuerst wurde ein 50-USDT-Zwischenstand bereinigt, um Duplikate, uneinheitliche Kostenlogik und unbelegte Zeilen aus dem historischen Bestand herauszunehmen.

Inzwischen gilt als aktive Basis ein **kanonischer 100-USDT-Vertrag mit global 12 bps Kosten**. Im letzten Rebuild wurden **81.283 Outcomes** migriert. Aktive X9-/50-USDT-Outcomes, Duplikate und geprüfte verwaiste Verweise stehen bei **0**. **327 Outcomes bleiben ausdrücklich `UNPROVEN`**, statt sie stillschweigend in gültige Ergebnisse umzuwandeln.

Das ist Absicht: Fehlende Evidenz bleibt fehlende Evidenz.

### Historischer OpenAI-Vergleich erneut gegen Futures-Preise geprüft

Das frühere OpenAI-Kontrollfenster bestand aus 87 historischen Vergleichstrades. Mit der alten 12-bps-Rechnung ergab es rund **+43,49 USDT**.

Nach dem Neuaufbau auf der vorgesehenen **Bitget-Futures-Preisbasis** sank derselbe Kontrollbestand auf rund **+27,07 USDT**.

Die anschließende Fortführung bestätigte die frühe Kurve nicht:

- Kontrollfenster: 87 Trades, nach Futures-Korrektur ca. **+27,07 USDT**
- Fortführung: 672 Trades, ca. **−116,50 USDT**
- zusammen ausgewerteter Bestand: 759 Trades, ca. **−89,43 USDT**

Zum Rebuild-Stand vom 10. September waren 25 OpenAI-Fälle noch offen.

Außerdem zeigte sich, dass der positive Anfang stark von wenigen Trades getragen wurde: Drei ENA-Trades lieferten zusammen etwa **+28,68 USDT**, während die übrigen 84 Kontrolltrades zusammen leicht negativ waren.

In der Fortführung zeigte sich zudem ein deutlicher Unterschied zwischen den Seiten: Shorts blieben insgesamt positiv, während spätere Long-Signale den Hauptteil der Verluste verursachten. Das belegt eine veränderte Ergebnisqualität, aber noch nicht die eine einzelne Ursache oder Regeländerung.

### Das „30-Minuten“-Problem wurde präzisiert

Eine frühere Formulierung konnte so verstanden werden, als wären Trades 30 Minuten nach einer OpenAI-Antwort gefüllt worden. Das zeigte die Prüfung nicht.

Der bestätigte Fehler lag beim **Alter des Eingangskontexts**: Ein neuer Gesamtzyklus konnte eine ältere Coin-Prognose erneut verwenden. Dadurch konnte eine Abfrage frisch aussehen, obwohl einzelne Eingangsdaten bereits deutlich älter waren.

Für die normalen Runtime-Pfade waren die beobachteten Abstände Signal → Fill wesentlich kleiner:

- Paper: bis ca. 85 Sekunden
- Watch: bis ca. 86 Sekunden
- Research Forward: bis ca. 88 Sekunden

Beim historischen OpenAI-Vergleich war der gespeicherte Vergleichs-Entry an den ursprünglichen Prediction-Zeitpunkt gebunden. Wo die Antwortverfügbarkeit belegt werden konnte, lag sie ungefähr 16–33 Sekunden später. Das waren historische Vergleichstrades, keine tatsächlich ausgeführten Orders.

### OpenAI-Requests werden jetzt an das gebunden, was das Modell wirklich gesehen hat

Der Code wurde so geändert, dass der tatsächliche Anfragekontext dauerhaft erhalten bleibt, statt später aus neueren Marktdaten rekonstruiert zu werden.

Die beabsichtigte Bindung umfasst jetzt unter anderem:

- den tatsächlich verwendeten Marktkontext,
- den Futures-Referenzpreis,
- Start- und Antwortzeit der Anfrage,
- den Entscheidungskontext von Paper/Watch,
- und die spätere Abrechnung auf Basis der ursprünglichen Evidenz statt eines ersetzten Lookups.

Ein späterer Writer darf fehlende Preisbelege nicht still ergänzen oder den ursprünglichen Kontext austauschen.

### Der AI-only OpenAI-Paper-Pfad wurde neu aufgebaut

Der prospektive OpenAI-Pfad ist jetzt sauber von lokaler ML-Richtung und altem Legacy-Kontext getrennt.

Die aktive Implementierung folgt diesen Regeln:

- **nur Bitget Futures 1m** für Referenz-, Entry- und Exitpreise,
- frischer 1m-/5m-/15m-/1h-Kontext vor jeder OpenAI-Anfrage,
- keine lokale ML-Richtung im OpenAI-Request,
- kein Spot-Preis-Fallback,
- keine X9-Logik im aktiven OpenAI-Outcome-Pfad,
- Entry erst nach vorhandener OpenAI-Antwort und erfüllter strukturierter Futures-Bedingung,
- neuere Coin-Bewertungen ersetzen ältere offene Ideen, damit keine „Zombie-Entries“ später auftauchen,
- `NO_TRADE`, abgelaufene, invalidierte und abgelöste Prognosen bleiben fürs Lernen erhalten, ohne nachträglich Trades oder PnL zu erfinden,
- aktiver Wirtschaftsvertrag: **100 USDT und 12 bps Kosten**.

API-Takt und Tageslimit wurden nicht erhöht. Das Antwortlimit wurde von 2.200 auf 3.200 Tokens angehoben, damit weniger unvollständige und damit unbrauchbare Antworten entstehen, ohne häufiger neue Requests zu senden.

### Prüfung des neuen prospektiven Pfads

Der Umsetzungsbericht dokumentiert:

- **28 gezielte Tests bestanden**,
- Futures-Preflight: **PASS**,
- aktive X9-Outcomes in diesem Pfad: **0**,
- lokale ML-Felder im OpenAI-Request: **0**,
- durch die Tests ausgelöste API-Aufrufe: **0**.

Der Supervisor hat den geänderten Prozess automatisch neu geladen. Zum Zeitpunkt der Abnahme gab es noch keinen ersten natürlichen neuen AI-only-Fall. Der prospektive End-to-End-Nachweis in der laufenden Runtime steht daher noch aus.

Diese Grenze ist wichtig: Eine implementierte und getestete Änderung ist positive Evidenz, aber noch nicht dasselbe wie ein natürlicher Forward-Nachweis.

## Was noch offen ist

Die nächsten Schritte sind jetzt klarer:

1. Die ersten natürlichen AI-only-Fälle vollständig von Anfrage bis Outcome beobachten.
2. Den Entscheidungssnapshot vom Prompt bis zum Outcome-Memory unverändert halten.
3. Alte OpenAI-Zeilen mit nicht belegbarem Kontext oder Exit sauber neu aufbauen oder als `UNPROVEN` belassen.
4. Historische Referenzvergleiche strikt von prospektiver Paper-Ausführung trennen.
5. Den Lifecycle **Factory → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION** weiterführen, ohne Evidenz-Gates zu überspringen.
6. Die Quellenwahl des öffentlichen Nightly-Publishers reparieren, damit neue Entwicklungsarbeit nicht wieder durch einen alten Stand vom 5. September ersetzt wird.

## Korrektur des öffentlichen Status

Der tägliche GitHub-Upload selbst ist in den letzten Tagen planmäßig gelaufen. Das Problem lag in der **automatischen Auswahl der Tagesgeschichte**: Die Dateien übernahmen immer wieder ältere Entwicklungsinformationen vom 5./6. September, obwohl lokal neuere Arbeit vorhanden war.

Dieses Update vom 12. September ist deshalb eine menschlich geprüfte Korrektur der öffentlichen Darstellung. Es macht alte Ergebnisse nicht rückwirkend zu einem PASS. Es dokumentiert, was sich geändert hat, was widerlegt wurde, was repariert wurde und wo noch natürlicher Runtime-Nachweis fehlt.

## Sicherheitsgrenze

AlgoSphere bleibt ein Research-System. Live-Trading und automatische Freigaben für Echtgeld bleiben deaktiviert. Historische und Paper-Ergebnisse sind Forschungsnachweise und keine Zusage zukünftiger Performance.

[Aktueller Status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Dokumentierte Entwicklungsarbeit](../docs/progress/COMPLETED_WORK.md) · [Tests](../docs/verification/TEST_RESULTS.md)
