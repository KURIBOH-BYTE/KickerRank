# T09 · Formular «Spiel erfassen» mit Eingabeprüfung im Browser

**Meilenstein:** M1 · Presentation Layer  
**Schicht/Typ:** Presentation  
**Schätzung:** 2.5 h  
**Abhängig von:** T08

## Ziel
Ein Spiel lässt sich im Formular eingeben, offensichtliche Fehler werden schon im Browser gemeldet.

## Aufgaben
- [ ] Zwei Dropdowns (Spieler A, Spieler B), gefüllt aus denselben Testdaten wie die Rangliste
- [ ] Zwei Zahlenfelder für die Tore (0–10)
- [ ] Beim Absenden mit jQuery prüfen: zwei verschiedene Spieler, Tore ausgefüllt
- [ ] Fehler unter dem Formular anzeigen (kein `alert`)
- [ ] Vorerst nur `console.log` mit den Formulardaten als Objekt

## Akzeptanzkriterien
- [ ] Gleicher Spieler zweimal → Fehlermeldung
- [ ] Leeres Torfeld → Fehlermeldung
- [ ] Gültige Eingabe → Objekt in der Konsole

## Tests
- [ ] Manuelle Testfälle M3 bis M5 (je ein Fall pro Prüfung)

## Hinweise
Wie eure Übung «Validierung von Eingabefeldern», aber mit jQuery. Wichtig: Die echte Prüfung kommt später im Business Layer. Im Browser prüfen wir nur für die Bedienfreundlichkeit.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
