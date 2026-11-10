# T29 · Erweiterung: Spielverlauf

**Meilenstein:** M5 · Erweiterungen (volle Punktzahl)  
**Schicht/Typ:** Erweiterung  
**Schätzung:** 3 h  
**Abhängig von:** T27

## Ziel
Alle Spiele werden als Liste angezeigt, neuste zuerst.

## Aufgaben
- [ ] Persistence: `SpielRepository.alle()`
- [ ] Business: `SpielService.verlauf()`
- [ ] Service: `GET /api/spiele`
- [ ] Präsentation: Tabelle im Bereich «Spiel erfassen» oder eigener Bereich

## Akzeptanzkriterien
- [ ] Verlauf aktualisiert sich nach jeder Aktion

## Tests
- [ ] `test_verlauf_neuste_zuerst`
- [ ] API-Test `GET /api/spiele`
- [ ] Manueller Testfall

## Hinweise
Gut als erstes Ticket für jemanden, der eine Funktion einmal durch alle vier Schichten bauen will.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
