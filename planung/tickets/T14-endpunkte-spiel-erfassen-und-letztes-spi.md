# T14 · Endpunkte Spiel erfassen und letztes Spiel

**Meilenstein:** M2 · Web/REST Service Layer  
**Schicht/Typ:** Service  
**Schätzung:** 2.5 h  
**Abhängig von:** T13

## Ziel
Spiele werden gespeichert und das neuste kann abgefragt werden. Noch ohne Elo-Berechnung.

## Aufgaben
- [ ] `service/spiel_endpoints.py`
- [ ] `POST /api/spiele` speichert das Spiel in einer Liste, erhöht `anzahl_spiele` beider Spieler
- [ ] `GET /api/spiele/letztes` liefert das neuste Spiel oder `null`

## Akzeptanzkriterien
- [ ] Nach `POST` liefert `letztes` genau dieses Spiel
- [ ] Ohne Spiele liefert `letztes` den Wert `null`

## Tests
- [ ] `test_spiel_erfassen_gibt_201`
- [ ] `test_letztes_spiel_ohne_spiele_ist_null`
- [ ] `test_letztes_spiel_ist_das_neuste`

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
