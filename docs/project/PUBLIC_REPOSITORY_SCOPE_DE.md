# Umfang des öffentlichen Repositorys

Dieses Repository ist die öffentliche Dokumentations- und Evidence-Schicht von AlgoSphere.

Es ist kein Download-Release der privaten Trading-Anwendung.

## Was hier öffentlich ist

Das Repository kann enthalten:

- Projektstatus und datierte Updates
- Research-Methodik und Lifecycle-Dokumentation
- Validierungs- und Verifikationszusammenfassungen
- ausgewählte öffentliche Evidence-Exporte
- Roadmap und dokumentierte Arbeiten
- FAQ, Contribution- und Support-Hinweise
- kleine Verifikationsskripte/-tests, die den öffentlichen Export selbst prüfen

## Was hier nicht veröffentlicht wird

Bewusst nicht enthalten sind:

- privater Trading-/Runtime-Anwendungscode
- Zugangsdaten, API-Keys und Kontokonfiguration
- Exchange-Kontodaten
- private Marktdatenbanken und rohe operative Logs
- trainierte Model Bundles/Checkpoints
- proprietäre Strategieparameter und private Execution-Konfiguration
- private Deployment- und Infrastrukturdetails

Dass kleine öffentliche Verifikationswerkzeuge unter tools/ oder tests/ liegen, bedeutet nicht, dass die AlgoSphere-Trading-Anwendung Open Source ist.

## Warum die Dokumentation öffentlich ist

Ziel ist ein öffentlich nachvollziehbarer Stand dessen, was tatsächlich gebaut, getestet, verworfen, verbessert oder bewusst offen gelassen wurde.

Dazu gehören ausdrücklich auch negative Ergebnisse.

Ein öffentlicher Status sollte unterscheiden können zwischen:

- implementiert
- getestet
- in Runtime beobachtet
- prospektiv bewiesen
- noch ohne ausreichende Evidence
- bewusst nicht öffentlich

## Releases und Downloads

Aus diesem Repository wird aktuell keine öffentliche Anwendung zum Download angeboten.

Falls später ein Demo- oder Client-Paket veröffentlicht wird, erhält es einen eigenen Release-Track mit eigener Integrity-, Config-, Permission- und Safety-Grenze.

Bis dahin bedeutet die öffentliche Sichtbarkeit des Repositorys weder Produktverfügbarkeit noch Live-Trading-Readiness.

## Lizenzierung

Öffentliche Dokumentation und öffentliche Evidence, die für dieses Repository erstellt wurden, stehen unter **CC BY-SA 4.0**, sofern eine Datei nichts anderes angibt.

Die kleinen öffentlichen Verifikationswerkzeuge unter `tools/` und `tests/` stehen unter der **MIT License**.

Diese Lizenzen gelten nur für tatsächlich in diesem Repository veröffentlichte Inhalte. Sie geben weder die private AlgoSphere-Anwendung noch nicht veröffentlichte Modelle, Strategieinhalte, Zugangsdaten, Kontodaten oder Infrastruktur frei.

Siehe [Lizenzierung](../legal/LICENSING.md).
