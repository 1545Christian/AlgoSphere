# Öffentliches Status-Update — 2026-09-19

English: [Public status update](./2026-09-19-public-status.md)

## Zusammenfassung

Am 19. September lag der Schwerpunkt auf drei wiederkehrenden Projektproblemen: Canonical Memory / V2-Lineage, Wachstum des Research-Speichers und Wahrheit/Bedienbarkeit der WebUI.

Wichtige Fortschritte:

- Die Current- und Shadow-Research-Projektionen wurden erneut repariert und im Browser mit stabilem Zustand geprüft.
- Der Shadow-Research-Pfad konsumiert jetzt governte Learning-Evidence zusätzlich zum Marktkontext.
- Neue Shadow-Writes erzwingen erforderliche State-Evidence strenger; ein eng begrenzter historischer Repair bleibt durch einen aktiven Writer blockiert.
- Ein Verlust im Research→Canonical-Handoff wurde gefunden und für zukünftige Writes repariert; kompakte Research-Evidence bleibt nun über die Grenze erhalten.
- Ein starkes Research-Storage-Wachstum wurde auf doppelte Repräsentationen in zukünftigen Snapshots zurückgeführt. Der Future-Writer wurde deutlich reduziert, ohne historische Evidence zu löschen. Exakte Schema- und Feldnamen werden bewusst nicht veröffentlicht.
- Tabellen-/Filter-Vertrag der WebUI wurde stabiler und kompakter, bei wieder größerer lesbarer Schrift und Tooltips.
- Durch diese Reparaturen wurden kein Training, Replay, Promotion oder Live-Trading gestartet.

Das zentrale wissenschaftliche Problem bleibt unverändert: Mehr Infrastruktur funktioniert, aber ML-Uplift und ein vollständig geschlossener Lernkreislauf sind noch nicht bewiesen.

## Canonical Decision / Learning Contract

Das Projekt nähert sich weiter einer gemeinsamen vergleichbaren Kette:

`Decision → Research-Kandidat → simuliertes/counterfactual Outcome → Evidence Memory → Learning → Lifecycle`

Der Audit zeigte, dass diese Kette je Lane/Variante noch uneinheitlich ist.

Bekannte Lücken bleiben bei Teilen historischer Identity-, Lineage- und Populationskonsistenz. Exakte Feldnamen und Lane-Mappings werden bewusst nicht veröffentlicht.


Neue CONTEXT_V2-Decisions/Outcomes schreiben fail-closed, wenn erforderliche State-Evidence fehlt.

### Historischer Exact-only Repair

Ein eng begrenzter historischer Repair existiert, blieb aber unvollständig, weil ein aktiver Writer keinen sicheren Maintenance-State zuließ. Writes wurden bewusst nicht erzwungen. Exakte Schema-, Tabellen- und Join-Details werden nicht veröffentlicht.

## CONTEXT_V2 konsumiert jetzt Canonical Learning Delta

Ein konkreter fehlender Anschluss wurde repariert:

`governte Learning-Evidence → Shadow-Research-Auswahl`

Die bestehende Learning Engine und Strategy × State Matrix wurden wiederverwendet.

Für neue Shadow-Research-Decisions kann nachvollzogen werden, wie governte Evidence die Auswahl verändert hat. Exakte Score-Komponenten und Decision-Felder werden bewusst nicht veröffentlicht.


CURRENT bleibt Kontrollpfad und wurde nicht verändert.

Counterfactual / NO_TRADE wird nicht als ausgeführter Trade gezählt.

Fokussierte Runtime-/Canonical-/Learning-Checks bestanden; exakte interne Testzahlen werden bewusst nicht veröffentlicht.

## Trade Like Che WebUI und V1/V2-Trennung

Die Trade-Like-Che-Ansicht wurde auf mehreren Ebenen repariert.

Bestätigte Fixes betreffen Populationstrennung, refresh-stabilen UI-State, Erhalt bestehender Evidence und klarere Pending-/Outcome-Darstellung. Exakte IDs, interne Host-Aliase und Feldnamen werden bewusst nicht veröffentlicht.


Der Tabellenvertrag wurde für Lesbarkeit und kompakte Darstellung vereinheitlicht. Exakte CSS-/Layout-Konstanten werden bewusst nicht veröffentlicht.


Ein browser-geprüfter Zwischenstand bestätigte konsistente Current-/Shadow-Projektionen. Exakte Populationszahlen werden bewusst nicht veröffentlicht.


Diese Zahlen sind UI-/Runtime-Evidence und noch kein Beweis, dass die historische Canonical-Population vollständig vergleichbar ist.

## Research-Storage Root Cause

Der Research-Speicher war stark gewachsen. Ursache waren doppelte interne Repräsentationen in zukünftigen Snapshots, nicht identische Gesamtsnapshots. Der Future-Writer wurde korrigiert; historische Evidence blieb unangetastet. Exakte DB-Größen, Zeilenzahlen, Schema-Namen und Feldpaare werden bewusst nicht veröffentlicht.

## Research-Evidence-Handoff

Ein zweiter Research-seitiger Handoff-Gap wurde vor der Evidence-Memory-Grenze gefunden. Ein kompakter future-only Evidence-Subset wird nun weitergereicht, während vollständige private Research-Payloads privat bleiben. Natürlicher Forward-Proof steht noch aus; historische Reprojektion ist nicht erforderlich.

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
