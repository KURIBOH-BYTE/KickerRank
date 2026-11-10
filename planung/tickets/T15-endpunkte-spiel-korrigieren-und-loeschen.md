# T15 · Endpunkte Spiel korrigieren und löschen

**Meilenstein:** M2 · Web/REST Service Layer  
**Schicht/Typ:** Service  
**Schätzung:** 2 h  
**Abhängig von:** T14

## Ziel
CRUD ist auf API-Ebene vollständig.

## Aufgaben
- [ ] `PUT /api/spiele/{id}` ändert die Tore
- [ ] `DELETE /api/spiele/{id}` entfernt das Spiel (Status 204)
- [ ] Unbekannte ID → 404

## Akzeptanzkriterien
- [ ] Korrigiertes Resultat ist in `letztes` sichtbar
- [ ] Nach dem Löschen ist das vorherige Spiel das neuste

## Tests
- [ ] `test_spiel_korrigieren`
- [ ] `test_spiel_loeschen_gibt_204`
- [ ] `test_unbekanntes_spiel_gibt_404`

## Hinweise
Die Regel «nur das neuste Spiel» kommt in T22 im Business Layer.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
