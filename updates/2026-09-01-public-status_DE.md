# Öffentliches Status-Update — 2026-09-01

English: [Public status update](2026-09-01-public-status.md)

<!-- AUTO_VALUES_START -->

Dieses Update wird aus aktuellen skalaren Artefakten erzeugt. Die grundlegenden Erläuterungstexte werden getrennt in menschlich geprüften Vorlagen gepflegt.

## Nachtrag zum Research-Feature-Contract

- **in geprüfter interner Evidenz beobachtet:** Eine Regression in der Research-Feature-Contract-Komposition wurde korrigiert und ein unveränderlicher Research-Core wurde geprüft.
- **in geprüfter interner Evidenz beobachtet:** Ein zeitlich sauberer Feature-Contract-Lauf bestätigte die Konsistenz zwischen Training, Holdout und Runtime. Das ist ein Vertrags- und Datenverfügbarkeitsnachweis, keine Performance- oder Profitabilitätsaussage.
- **in geprüfter interner Evidenz beobachtet:** Die fachlich relevanten Regressionstests und Runtime-Delivery-Tests bestanden. Sie wurden durch diesen öffentlichen Export nicht erneut ausgeführt.
- **nicht anwendbar:** Es wurden keine Live-Trades, Orders, Exchange-Aktionen, Kapitalaktionen, Paper-Aktivierungen oder Kandidaten-Promotions ausgeführt.
- **in geprüfter interner Evidenz beobachtet:** Der Research-Core ist für den nächsten natürlichen Research-Start vorbereitet. Dieser Start wurde nicht als bereits erfolgt behauptet.

**blockiert:** Dem Runtime-Entry-Snapshot fehlen weiterhin herkunftsgebundene Trade-Window-Candles. Sie müssen unveränderlich erfasst und danach erneut mit exakter Hash-QA sowie einer frischen Trade-Reprüfung geprüft werden.


## Änderung seit der vorherigen veröffentlichten Momentaufnahme

Die vorherige öffentliche Register-Momentaufnahme enthielt 1.742 Einträge. Das aktuelle bereinigte Register enthält 3187 Einträge, eine Differenz von 1445. Das Register veröffentlicht weder Rohdateinamen noch kausale Herkunft. Die Ursache des Anstiegs ist daher nicht verifiziert. Er darf nicht als 1445 neue Tests, abgeschlossene Entwicklungsarbeiten oder Leistungsfortschritt gelesen werden. Die angefragte Zwischenzahl 1.841 ist in dieser aktuellen Re-Inventarisierung nicht der aktuelle Wert und wird nicht als aktueller Fakt ausgegeben.

## Heute geprüfte technische und betriebliche Artefakte

- **Veralteter Slot-B-Guard:** Ein Artefakt mit dem Ergebnis `CLEARED_STALE_RESOURCE_GUARD` dokumentiert die Freigabe erst nach fehlender aufgezeichneter PID und Lease. Die zugehörige Validierung nennt `13 passed` und Compile-Prüfungen. Paper-, Live-, Kapital- und Datenlöschaktionen sind darin als nicht erfolgt dokumentiert.
- **QUICK-Versuch:** Ein echter QUICK-Versuch wurde als durch Ressourcenschutz unterbrochen beobachtet (`ExitCode 15`), nachdem ungefähr `3.63 GiB` privater Speicher gegenüber einem Limit von `2.50 GiB` erfasst wurden. Der Selektor betrachtete 69 Kandidaten in 12 Familien; geeignet und ausgewählt waren jeweils null. Das ist ein Ressourcen-/Betriebsergebnis, kein QUICK PASS und keine Widerlegung der Hypothese. Aktivierung und Promotion blieben deaktiviert.
- **Runtime-Health-Projektion:** Das geprüfte Artefakt nennt Active Paper und Research Forward als nachgewiesen; Watch Scanner und Watch Exit Evaluator bleiben nicht nachgewiesen. Die verknüpfte Validierung nennt `108 passed` und Compile PASS. Das sind historische Artefaktangaben, keine in diesem Export erneut ausgeführten Tests.
- **Storage und Retention:** Das jüngste geprüfte Kapazitätsprofil meldete ungefähr `136.60 GiB` frei gegenüber einer erforderlichen Schwelle von `9.25 GiB` und null bereinigte Bytes. Es gab keine destruktive Bereinigung. Referenzierte Lineage-Backups bleiben geschützt; eine ausdrückliche Retention-Policy bleibt offen.
- **F_META:** Das geprüfte Readiness-Artefakt bleibt `PREPARED_WAITING_CURRENT_INDEPENDENT_RUNTIME_QA_TERMINAL`; eine unabhängige QA-Bestätigung und eine neue terminale Active-Paper-Entscheidung sind weiterhin nicht nachgewiesen.

## Aktuelle Kontrollen

- Canonical-history integrity: `PASS` beobachtet am `2026-09-01T18:20:55Z`.
- Paper-watch guard: `PASS` beobachtet am `2026-09-01T18:10:25Z`.
- Runtime context gate: `FAIL_INCOMPLETE_V3_CONTEXT` beobachtet am `2026-09-01T18:10:25Z`; `7` abgegrenzte Fälle bleiben.
- Research-Profil: `QUICK`; Aktivierung erlaubt: `False`; geeignete Experimente: `0` beobachtet am `2026-09-01T18:21:42Z`.

## Testgrenze und nächster Schritt

Anwendungstest-Suiten wurden während dieses Exports nicht erneut ausgeführt. Der unveränderte Hauptblocker ist das Runtime context gate. Als nächster konkreter Schritt müssen die verbleibenden Kontextfälle gelöst und danach die passende Kontrolle unabhängig erneut ausgeführt werden.

Exportintegrität: verifiziert. Siehe [Aktueller Status](../CURRENT_STATUS.md), [Testergebnisse](../docs/verification/TEST_RESULTS.md) und die verbindliche [Evidenzübersicht](../evidence/EVIDENCE_SUMMARY.md).
<!-- AUTO_VALUES_END -->
