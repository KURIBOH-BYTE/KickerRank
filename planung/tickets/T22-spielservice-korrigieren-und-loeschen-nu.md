# T22 · SpielService: Korrigieren und Löschen nur beim neusten Spiel

**Meilenstein:** M3 · Business Service Layer  
**Schicht/Typ:** Business, Test  
**Schätzung:** 2.5 h  
**Abhängig von:** T21

## Ziel
Korrigieren und Löschen setzen die Elo korrekt zurück und sind nur beim neusten Spiel erlaubt.

## Aufgaben
- [ ] `spiel_korrigieren(id, tore_a, tore_b)`: mit `elo_vorher` neu rechnen
- [ ] `spiel_loeschen(id)`: Elo auf `elo_vorher` zurücksetzen, `anzahl_spiele` minus 1
- [ ] Älteres Spiel → `GeschaeftsFehler`

## Akzeptanzkriterien
- [ ] Nach dem Löschen haben beide Spieler wieder genau die Elo von vorher

## Tests
- [ ] `test_korrigieren_dreht_sieger`: aus 10:7 wird 7:10, Elo wechselt die Seite
- [ ] `test_loeschen_setzt_elo_zurueck`
- [ ] `test_altes_spiel_loeschen_gibt_fehler`

## Hinweise
Begründung für die Verteidigung: Alle späteren Spiele bauen auf den Elo-Werten des älteren Spiels auf.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
