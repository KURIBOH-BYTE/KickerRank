# T13 · Endpunkt Spieler anlegen

**Meilenstein:** M2 · Web/REST Service Layer  
**Schicht/Typ:** Service  
**Schätzung:** 1.5 h  
**Abhängig von:** T12

## Ziel
Neue Spieler können über die API angelegt werden.

## Aufgaben
- [ ] `POST /api/spieler` nimmt `SpielerErstellen` an
- [ ] Neue ID vergeben, Elo 1200, 0 Spiele
- [ ] Antwort `SpielerAntwort` mit Status 201

## Akzeptanzkriterien
- [ ] Neuer Spieler erscheint danach in `GET /api/rangliste`

## Tests
- [ ] `test_spieler_anlegen_gibt_201`
- [ ] `test_neuer_spieler_startet_mit_1200`

## Hinweise
Die Prüfungen (leerer Name, doppelter Name) kommen erst im Business Layer (T20).

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
