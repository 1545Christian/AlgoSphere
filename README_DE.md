# AlgoSphere

Zur vollständigen englischen Einführung: [README.md](README.md).

<!-- HUMAN_TEXT_START: von mir geprüft, überarbeitet und vor Veröffentlichung freigegeben -->

## Was AlgoSphere ist

AlgoSphere ist ein unabhängiges Forschungs- und Entwicklungsprojekt für einen nachvollziehbaren Workflow rund um Handelsforschung. Es soll keine Marktergebnisse versprechen. Praktisch geht es darum, Research, Tests, Paper-Beobachtung, Monitoring und mögliche spätere Aktivierungsentscheidungen nachvollziehbar, begrenzt und fail-closed zu gestalten.

## Wie das Projekt begann

Ich arbeite seit ungefähr drei Jahren an den zugrunde liegenden Ideen und Python-Prototypen. Zunächst lernte ich, indem ich Beispiele aus YouTube-Videos und anderem Lehrmaterial nachbaute und anpasste. Aus dieser Lernphase entstanden mehrere eigene Python-Prototypen, die ich wiederholt überarbeitete, als klar wurde, dass stärkere Kontrollen, bessere Belege und eine sauberere Trennung zwischen Forschung und Betrieb nötig sind.

## KI-Unterstützung und persönliche Prüfung

Ich nutze Codex und ChatGPT zur Unterstützung bei Implementierung, Fehlersuche, technischer Prüfung und Dokumentation. KI-unterstützte Entwürfe prüfe, überarbeite und bestätige ich vor der Veröffentlichung selbst. Die Projektentscheidungen und die Verantwortung liegen bei mir.

## Was dieses öffentliche Repository ist

Dieses Repository ist die öffentliche technische Dokumentation von AlgoSphere. Hier lassen sich der aktuelle dokumentierte Status, beobachtete Kontrollen, bekannte Blocker, das Evidenzregister und datierte öffentliche Updates nachvollziehen. GitHub ist die verbindliche öffentliche technische Quelle. Der [Telegram-Kanal](https://t.me/AlgoSphereOfficial) darf kurze Zusammenfassungen mit Verweis hierher veröffentlichen.

Nicht veröffentlicht werden privater Quellcode, Zugangsdaten, Umgebungsdateien, Wallet- oder Kontodaten, Rohberichte, Datenbanken, Marktdaten, trainierte Modelle, Checkpoints, Strategieparameter, proprietäre Handelslogik, private Logs, personenbezogene Daten und interne Pfade.

## So wird dieses Repository verwendet

Beginne mit dem aktuellen Status und lies danach die Testgrenzen sowie die offenen Blocker. Das Evidenzregister zeigt, dass ein Artefakt registriert wurde; es beweist nicht, dass ein Ergebnis unabhängig reproduziert wurde. Historische Updates behalten ihre damaligen Zahlen und sind sichtbar als Momentaufnahmen gekennzeichnet.

## Start hier

| Wenn du prüfen möchtest | Lies |
|---|---|
| Aktuellen technischen Stand und Hauptblocker | [Aktueller Status](CURRENT_STATUS.md) |
| Kontrollen, Tests und nicht erneut ausgeführte Prüfungen | [Testergebnisse](TEST_RESULTS.md) |
| Verbindliche Evidenzübersicht und Registerhinweise | [Evidenzübersicht](evidence/EVIDENCE_SUMMARY.md) |
| Entwicklungsgeschichte | [Projekthistorie](PROJECT_HISTORY.md) |
| Prioritäten und Abnahmekriterien | [Roadmap](ROADMAP.md) |
| Datierte öffentliche Änderungen | [Updates](updates/) |
| Sicherheitsgrenze und Meldeweg | [Sicherheit](SECURITY.md) |
| Finanzielle und technische Abgrenzung | [Disclaimer](DISCLAIMER.md) |

## Öffentlichen Export prüfen

In einem öffentlichen Clone ausführen:

```text
python tools/verify_public_export.py
```

Dieses Skript prüft die Integrität des öffentlichen Exports. Es reproduziert keine privaten Anwendungstests und beweist weder Strategiequalität noch Profitabilität oder Live-Trading-Reife.

## Vorschau der Oberfläche

Bei dieser Prüfung wurden keine geeigneten aktuellen und bereinigten WebUI-Screenshots gefunden. Deshalb enthält diese Revision keine Produktbilder. Benötigt werden künftig eine bereinigte Dashboard-Übersicht, ein Research-Status und eine Runtime-Sicherheitsansicht. Vor Veröffentlichung müssen lokale URLs, interne Pfade, Kontoangaben, private Tabs, Taskleisteninhalte, Zugangsdaten, Kontostände, Strategieeinstellungen und sensible Laufzeitinformationen entfernt werden.

Bei später freigegebenen Screenshots wird folgender Hinweis verwendet: „Die folgenden Bilder zeigen die aktuelle private AlgoSphere-Weboberfläche. Sie dokumentieren den Entwicklungsstand und das Betriebsmodell des Projekts. Die WebUI und die zugrunde liegende Anwendung sind nicht Bestandteil dieses öffentlichen Repositorys.“

## Was Besucher prüfen können

Besucher können prüfen, ob der dokumentierte Export ein Integritätsmanifest besitzt, ob das Evidenzregister ein beschriebenes Schema und eine angegebene Anzahl hat, ob öffentliche Links funktionieren und ob beobachtete skalare Kontrollwerte mit Artefaktzeitpunkten angegeben sind. Außerdem ist die Git-Historie dieses Dokumentations-Repositorys einsehbar.

## Grenzen der öffentlichen Nachprüfbarkeit

Öffentliche Dokumentation kann private Code-, Daten-, Modell-, Konfigurations- oder Strategieergebnisse nicht unabhängig reproduzieren. Ein berichtetes PASS ist nicht automatisch ein unabhängig erneut ausgeführter Test, und ein Registereintrag ist nicht automatisch ein bestandener Test oder eine abgeschlossene Entwicklungsarbeit. Keine Seite hier belegt Profitabilität, Live-Trading-Reife, Modellerfolg oder ein garantiertes Projektergebnis.

## Bedeutung der Kontrollen

- **Canonical-history integrity** prüft, ob der gepflegte historische Bestand seinen dokumentierten Integritätsvertrag erfüllt. Ein PASS ist ein beobachteter Artefaktzustand, kein Leistungsnachweis.
- **Paper-watch guard** ist eine fail-closed-Kontrolle an der Grenze zwischen Paper und Watch. Ein PASS bedeutet, dass das beobachtete Guard-Artefakt einen passierenden Zustand meldete; dadurch wird kein Trading aktiviert.
- **Runtime context gate** prüft, ob benötigter Runtime-Kontext vollständig ist. Ein blockierter Zustand verhindert, den Kontextvertrag als vollständig zu behandeln.
- **Research profile QUICK** ist die beobachtete Profilbezeichnung des Research-Autopiloten. Sie beschreibt einen Berichtskontext, nicht Qualität oder Reife.
- **Activation allowed** zeigt, ob das beobachtete Research-Artefakt eine Aktivierung erlaubt. `False` bedeutet, dass dieses Artefakt keine Aktivierung zulässt.
- **Eligible experiments** ist die beobachtete Anzahl von Experimenten, die die jeweilige Eignungsbedingung erfüllen. Sie ist keine Zahl profitabler oder live-reifer Systeme.

## Kommunikation und Unterstützung

- Öffentliche technische Dokumentation: [GitHub](https://github.com/1545Christian/AlgoSphere)
- Kurze öffentliche Updates: [Telegram](https://t.me/AlgoSphereOfficial)
- Freiwillige Unterstützung: [GitHub Sponsors](https://github.com/sponsors/1545Christian)

Freiwillige Unterstützung hilft bei Forschung, Entwicklung, Testinfrastruktur und öffentlicher technischer Dokumentation. Sponsoring ist keine Investition und gewährt weder Eigentum, Rückzahlung, Gewinnbeteiligung, finanzielle Rendite, Trading-Signale, Anlageberatung, exklusiven Zugang noch einen garantierten Projekterfolg. Der vollständige Hinweis steht im [Disclaimer](DISCLAIMER.md).

## Urheberrecht und Wiederverwendung

Derzeit wird keine Open-Source-Lizenz eingeräumt. Soweit nicht ausdrücklich anders angegeben, bleiben alle Rechte vorbehalten. Die Veröffentlichung dieses Repositorys erlaubt keine Nutzung proprietären Quellcodes, von Daten, Modellen, Strategiematerialien oder der AlgoSphere-Marke.

<!-- HUMAN_TEXT_END -->

<!-- AUTO_VALUES_START: dieser Abschnitt wird aus aktuellen skalaren Artefakten erzeugt -->
## Aktuell beobachtete Kontrollen

| Kontrolle | Beobachteter Wert | Quellartefakt (UTC) | Einordnung | Praktische Auswirkung |
|---|---|---|---|---|
| Canonical-history integrity | `PASS` | `2026-08-31T13:21:57Z` | im aktuellen Artefakt beobachtet | Integritätskontrolle meldet ihren Zustand |
| Paper-watch guard | `PASS` | `2026-08-31T10:15:28Z` | im aktuellen Artefakt beobachtet | die Guard-Beobachtung aktiviert kein Trading |
| Runtime context gate | `FAIL_INCOMPLETE_V3_CONTEXT` | `2026-08-31T10:15:28Z` | blockiert | Kontext wird nicht als vollständig behandelt |
| Verbleibende Runtime-Kontextfälle | `7` | `2026-08-31T10:15:28Z` | blockiert | Remediation mit höchster Priorität bleibt offen |
| Research-Profil | `QUICK` | `2026-08-31T13:21:47Z` | im aktuellen Artefakt beobachtet | nur Profilbezeichnung |
| Aktivierung erlaubt | `False` | `2026-08-31T13:21:47Z` | im aktuellen Artefakt beobachtet | Aktivierung wird vom beobachteten Artefakt nicht erlaubt |
| Geeignete Experimente | `0` | `2026-08-31T13:21:47Z` | im aktuellen Artefakt beobachtet | kein geeignetes Experiment wird gemeldet |

Beobachteter Artefakt-Snapshot: `2026-08-31T13:22:11Z UTC / 2026-08-31 14:22 Westeuropäische Sommerzeit Atlantic/Canary`. Hauptblocker ist `FAIL_INCOMPLETE_V3_CONTEXT` mit `7` verbleibenden abgegrenzten Fällen.

Exportintegrität: verifiziert. Anwendungstest-Suiten: während dieses Exports nicht erneut ausgeführt. Siehe [Aktueller Status](CURRENT_STATUS.md) und [Testergebnisse](TEST_RESULTS.md).
<!-- AUTO_VALUES_END -->
