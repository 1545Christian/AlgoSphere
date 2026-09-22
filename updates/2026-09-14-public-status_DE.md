# Öffentliches Status-Update — 2026-09-14

English: [Public status update](./2026-09-14-public-status.md)

## Zusammenfassung

In den letzten Tagen ging es nicht darum, das breite ML-Training wieder zu starten. Der Schwerpunkt lag darauf, Trading, Research, Counterfactual-Lernen, OpenAI AI-only und Canonical Outcome Memory so sauber voneinander zu trennen, dass späteres Training wirklich aus der richtigen Evidenz lernen kann.

Der öffentliche Nightly-Publisher ist vom Operator aktuell pausiert. Dieses Update ist deshalb ein manuell geprüfter Stand auf Basis der aktuellen lokalen Acceptance- und Repair-Berichte.

Die wichtigste Korrektur ist konzeptionell: **„nicht traden“ darf nicht „nicht beobachten und nicht lernen“ bedeuten.** Paper behält den harten Expected-Net-Schutz, während Research Watch / Research Forward geblockte Setup-Matches jetzt als No-Capital-Counterfactuals erhalten und später über mehrere Horizonte auswerten können.

Gleichzeitig lebt der OpenAI-AI-only-Prozess technisch, ist aber **noch nicht als vollständige natürliche Forward-Trade-Kette bewiesen**. Ein `TICK_COMPLETE`-Heartbeat ist nicht dasselbe wie ein frischer AI-only Fill mit gemanagtem Exit, Outcome und anschließendem Lernen.

## Aktuelle Betriebsgrenze

- Training: **pausiert**
- Factory / Hypothesis Producer: **pausiert**
- Live-Trading: **deaktiviert**
- Echtgeld: **0**
- automatische Promotion: **deaktiviert**
- OpenAI bleibt unabhängig von lokaler ML-Richtung
- Proven-Rule-Schwellen und Exit-Parameter wurden in den letzten Reparaturschritten nicht verändert

Die aktuelle Priorität ist: zuerst die Trading-/Research-Evidenzkette beweisen, danach den Trainings-Lifecycle wieder aufnehmen.

## Paper / Watch / Research: Expected-Net-Semantik repariert

Der 0,30%-Expected-Net-Guard wurde auf `VisiblePaperEngine._forward_fill` zurückgeführt und verwendet das kanonische 12-bps-Kostenmodell.

Für Paper / später Live ist dieser Schutz weiterhin korrekt. Das Problem war, dass derselbe Blocker Research-Setups faktisch löschen konnte, bevor sie weiter beobachtet wurden.

Jetzt gilt:

- `NO_SETUP` → kein Setup vorhanden; kein Counterfactual nötig.
- `SETUP_MATCH + expected_net unproven` → **kein Paper-/Live-Trade**, aber No-Capital-Counterfactual behalten.
- `SETUP_MATCH + expected_net >= 0,30%` → darf durch die normale Paper-Economics weiterlaufen.

So bleibt der Kapitalschutz streng, ohne Research-Information zu verlieren.

## No-Capital-Counterfactual-Pfad

Der neue Research-Counterfactual-Pfad ist inzwischen in der fail-closed Runtime autorisiert.

Dokumentierter Stand:

- Research Watch: `ACTIVE_NO_CAPITAL`
- Research Forward: `WATCH_NO_CAPITAL`
- 90 Strategien im Forward geladen
- Paper-Promotion aus Counterfactuals: `false`
- Counterfactual-Forward-Pfad in der WebUI sichtbar
- Live bleibt unverändert deaktiviert

Der erste Backfill erzeugte **49 Counterfactuals**. Zum dokumentierten Prüfzeitpunkt waren **13 bis 8h ausgewertet** und **36 noch offen**.

Jedes geblockte Setup kann damit später bei 15m / 45m / 1h / 3h / 8h sowie mit MFE, MAE und kostenbereinigtem Ergebnis ausgewertet werden, ohne einen Kapital-Trade zu erzeugen.

## Missed-Edge-Audit

Der Forward-Path-Audit zeigte, dass Marktchancen vorhanden waren, auch wenn Paper korrekt nicht traden durfte.

Unter **49 eindeutigen geblockten Markt-Setups** wurden gefunden:

- 13 eindeutige verpasste Scalp-Chancen (15–45m)
- 2 eindeutige verpasste Intraday-Chancen (1–3h)
- 0 bestätigte verpasste Swing-Chancen (3–8h)
- 4 Bad-Entry-/Adverse-First-Fälle
- 15 Fälle, bei denen Edge erst nach zu hohem Drawdown auftrat
- 15 Fälle waren zum Prüfzeitpunkt noch unklar / pending

Damit ist bestätigt: Ein Teil der Information ging im Research-Funnel verloren, obwohl der Paper-Schutz selbst korrekt arbeitete.

## Marktphase / Strategy-Family-Evidenz

Der Audit zeigt außerdem, dass Edge nicht in jeder Marktphase gleich ist.

Beispiele aus dem derzeit noch begrenzten Sample:

- Range-Regime waren insgesamt positiv; `privater Rule-Kandidat` war im dokumentierten Range-Sample besonders stark.
- Up-Regime waren im dokumentierten Sample ebenfalls positiv.
- Down-Regime waren insgesamt schwächer; `volatility_scaled_momentum` hielt sich besser als `relative_strength_pullback`.
- Strong-Down hatte wenig Daten und schwache Ergebnisse.

Das sind Research-Hinweise, noch keine Produktionsregeln. Ziel ist, später Strategy × Coin × Side × Regime × Outcome zu lernen, statt alles nur auf Win/Loss zu reduzieren.

## Lokaler Trade-Outcome-/Canonical-Memory-Fix

Auch in der lokalen Paper-/Watch-/Forward-Kette gab es Lücken.

Die aktuelle Reparatur verknüpfte **58 lokale 100-USDT-Trades** vollständig:

- Active Paper: 4/4 Decision-IDs verlinkt
- Research Watch: 26/26
- Research Forward: 28/28

Dokumentierte Kette:

`Decision → Trade → Outcome → Canonical Memory`

Für diese 58 Trades wurden zusätzlich persistiert:

- Exit-Subreason
- Trailing-State
- MFE / MAE
- Post-Exit 30m / 60m / 120m / Horizon
- Learning-Klassifikation

Historische Werte, die sich nicht belegen lassen, bleiben ausdrücklich `NOT_CAPTURED` / `NOT_APPLICABLE` statt nachträglich erfunden zu werden.

## WebUI / Current-Truth-Fixes

Zwei echte Liveness-Projektionsfehler wurden korrigiert:

1. Die API nutzte fälschlich 72 Stunden statt des vorgesehenen 1-Stunden-Liveness-Fensters.
2. Datenfrische wurde gegen die aktuelle Uhrzeit statt gegen den Zeitpunkt der jeweiligen Entscheidung geprüft.

Der reparierte WebUI-Bericht zeigte:

- Integrity: `PASS`
- Operational: `true`
- Signed Baselines: 7/7 PASS
- Live-Input-Provenance: proven
- Historical Fallback: nicht beobachtet

Trade-Management-Felder zeigen nun erfasste Entry-/Exit-Zustände, MFE/MAE, Decision-IDs, Canonical-Outcome-IDs, Post-Exit-Horizonte und Learning-Klassifikationen. Fehlende Quelldaten werden ausdrücklich angezeigt.

## OpenAI AI-only: technisch aktiv, aber noch nicht vollständig bewiesen

Der OpenAI-Zweig meldet aktuell:

- Policy: `OPENAI_AI_ONLY_FUTURES_PAPER_V1`
- Futures-only Preisbasis
- kanonischer Notional: 100 USDT
- Position Manager: `CAUSAL_FUTURES_MARKET_MANAGEMENT_V1`
- Integrity: PASS
- Horizon Settlement und Exit-too-early-Erkennung vorhanden

Im letzten dokumentierten Stand gab es jedoch **keine neuen natürlichen AI-only Fills**. Beobachtet wurde `OPENAI_AI_ONLY_PAPER_TICK_COMPLETE`.

Die korrekte öffentliche Aussage lautet deshalb:

**Der OpenAI-Prozess läuft, aber eine frische natürliche AI-only Kette Decision → Entry → gemanagter Exit → Outcome → Learning ist noch nicht bewiesen.**

Auch die frühere historische OpenAI-Kurve muss relativiert bleiben. Frühere Audits fanden veralteten Coin-Kontext, Spot-bezogene Eingaben, übernommene lokale Richtung, Sofort-Entry-Annahmen und Probleme bei der historischen Exit-Zeit-Interpretation. Nach Futures-Rekonstruktion war das frühe Kontrollfenster schwächer als ursprünglich veröffentlicht, und die Fortführung deutlich negativ.

Der prospektive OpenAI-Pfad wurde deshalb neu aufgesetzt: frischer Futures-Kontext, keine lokale ML-Richtung, kein Spot-Fallback, keine X9-Logik und Entry erst nach OpenAI-Antwort und erfüllter strukturierter Bedingung.

Im OpenAI-Research-Layer noch unvollständig:

- 45m- und 8h-Horizontvarianten
- Multi-Horizon-Kandidaten
- `selected_variant_id`
- getrennt gespeicherte verworfene Varianten
- vollständige NO_TRADE-Missed-Opportunity-Klassifikation je Horizon

Diese Erweiterungen wurden bewusst nicht in die letzten Paper-/Research-Reparaturen hineingemischt.

## ML / Factory: warum Training pausiert bleibt

Das jüngste ML-Problem war nicht einfach „das Modell hat eine schlechte Strategie abgelehnt“.

Der Trainings-/Research-Pfad war vom früheren privaten Rule-Vertrag abgedriftet. Änderungen bei History-Länge, Schwellen und frühem Filtering konnten aus einer historisch aktiven Rule nur noch wenige Signale machen, bevor ML sie überhaupt sah.

ein privater Referenzkandidat ist dafür der wichtigste Referenzfall. Der ältere privaten Rule-Vertrag wurde mit deutlich mehr kausalen Signalen und einem reproduzierbaren OOS-Trade-Set wiederhergestellt. Daraus folgt verbindlich:

**ML-Selector-Kollaps ist nicht dasselbe wie Rule-Failure.**

Ein Rule-Artefakt, das seine eigene Evidenz besteht, darf nicht gelöscht werden, nur weil der ML-Selector ablehnt oder keine sinnvolle Auswahl erzeugt.

Der beabsichtigte Lifecycle lautet:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

`candidate_eligible` ist Eligibility-/Metadatum, keine eigene operative Stufe.

Training und Factory bleiben pausiert, bis die aktiven Trading-/Research-Pfade ausreichend bewiesen sind und der korrigierte Rule-Preservation-Vertrag wieder aufgenommen werden kann, ohne denselben Fehler zu wiederholen.

## Aktuelle Prioritäten

1. Natürliche neue Paper-/Watch-/Forward-/Counterfactual-Outcomes sammeln.
2. Erste vollständige natürliche OpenAI-AI-only-Forward-Kette beweisen.
3. Counterfactual-Backlog weiter settlen und messen, welche geblockten Setup-Familien tatsächlich Edge enthalten.
4. Reparierte Exit-/Post-Exit-Evidenz später fürs Lernen nutzen, nicht sofort Exit-Parameter verändern.
5. Rule-Evidenz bei erneutem Training unabhängig vom ML-Selector-Erfolg erhalten.
6. `HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION` erst wieder aufnehmen, wenn die aktiven Pfade vertrauenswürdig sind.
7. Die öffentliche GitHub-Dokumentation manuell geprüft halten, solange der Nightly-Publisher pausiert ist.

## Sicherheitsgrenze

AlgoSphere bleibt ein Research-System. Live-Trading und Echtgeld-Promotion sind deaktiviert. Paper-, Watch-, Research- und OpenAI-Ergebnisse sind Research-Evidenz und keine Aussage über künftige Profitabilität.

[Aktueller Status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Dokumentierte Arbeiten](../docs/progress/COMPLETED_WORK.md) · [Tests](../docs/verification/TEST_RESULTS.md)
