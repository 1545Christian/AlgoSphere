# Projektrichtung

AlgoSphere hat als Trading-Analyse- und Automatisierungsprojekt begonnen. Das langfristige Ziel ist aber größer als eine einzelne Strategie oder ein einzelnes Modell.

Das Projekt wird zu einem konfigurierbaren quantitativen Research- und Trading-Analyse-System für Kryptomärkte entwickelt, das über ein breites Coin-Universum arbeiten und seine Entscheidungen anhand messbarer Evidence verbessern soll — nicht durch blindes Retraining oder beliebige Parameteränderungen.

## Was das System langfristig können soll

AlgoSphere soll mit der Zeit:

- ein konfigurierbares Universum von Kryptomärkten überwachen
- Marktstruktur, Regime und Market State über mehrere Zeithorizonte einordnen
- verschiedene Strategiefamilien vergleichen, statt anzunehmen, dass eine Strategie überall funktioniert
- Machine-Learning-Modelle trainieren und gegen erhaltene Rule-Baselines validieren
- Decisions → Trades → Outcomes konsistent verfolgen
- aus profitablen, schlechten und NO_TRADE-Entscheidungen lernen
- erkennen, welche Ansätze bei welchem Coin, welcher Seite, Marktphase und welchem Horizont funktionieren
- Strategien und Modelle neu bewerten, wenn genügend neue Evidence vorliegt
- fehlgeschlagene und negative Experimente erhalten statt sie auszublenden
- Research nur dann weiter durch den Lifecycle bewegen, wenn die Evidence es trägt

Der vorgesehene Research-Lifecycle ist:

HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION

Ein neueres Modell soll nicht allein deshalb aktiv werden, weil es neuer ist. Promotion soll von reproduzierbarer Evidence, Robustheit und kontrolliertem Vergleich abhängen.

## Konfigurierbar statt auf wenige Coins begrenzt

Die Coins, die aktuell in Runtime- oder Research-Berichten auftauchen, sind Arbeits-Populationen und nicht das spätere Limit des Systems.

Langfristig soll das Coin-Universum einstellbar sein: so viele unterstützte Märkte, wie unter Daten-, Rechen-, Liquiditäts-, Qualitäts- und Exchange-Grenzen zuverlässig verarbeitet werden können.

Unterschiedliche Coins können unterschiedliche Strategien, Schwellen, Horizonte oder auch gar keinen Trade brauchen.

Das Ziel ist deshalb nicht:

> ein Modell finden, das alles handelt

sondern:

> lernen, was wo und unter welchen Bedingungen funktioniert — und wann Nicht-Handeln die bessere Entscheidung ist.

## Lernen ohne unkontrollierte Selbstveränderung

„Self-improving“ bedeutet bei AlgoSphere nicht, dass sich das System ohne Evidence selbst umschreibt oder selbst promotet.

Der vorgesehene Kreislauf bleibt kontrolliert:

neue Evidence → Evaluation → Learning Delta → Revalidierung → Lifecycle-Entscheidung

Research-Automation kann mit der Zeit autonomer werden. Runtime-Berechtigungen, Promotion, Release-Grenzen und jede spätere Echtgeld-Ausführung bleiben trotzdem ausdrücklich geregelt.

## Analyse, Training und Execution bleiben getrennte Aufgaben

AlgoSphere soll langfristig nutzbar sein als:

1. Marktanalyse-Umgebung,
2. ML- und Strategie-Research-/Training-System,
3. Paper-/Shadow-Validierungsumgebung,
4. später als kontrolliertes Execution-System, wenn Evidence und Sicherheitsvertrag das tragen.

Diese Bereiche bleiben bewusst getrennt, damit ein erfolgreicher Analyse- oder Trainingslauf nie mit Live-Readiness verwechselt wird.

## Öffentliche Projektgrenze

Dieses GitHub-Repository dokumentiert den öffentlichen Research-Stand, Methodik, Evidence und ausgewählte Verifikationswerkzeuge.

Der private Anwendungs-/Runtime-Code, Zugangsdaten, Marktdatenbanken, trainierte Model Bundles und proprietäre Strategieparameter werden hier nicht veröffentlicht.

Diese Trennung ist beabsichtigt: Die Arbeit soll öffentlich verständlich und prüfbar bleiben, ohne das operative Trading-System selbst zu veröffentlichen.