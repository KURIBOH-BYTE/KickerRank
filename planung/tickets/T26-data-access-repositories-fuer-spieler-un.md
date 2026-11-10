# T26 · Data Access: Repositories für Spieler und Spiele

**Meilenstein:** M4 · Persistence Layer  
**Schicht/Typ:** Persistence, Test  
**Schätzung:** 2.5 h  
**Abhängig von:** T25

## Ziel
Alle Datenbankabfragen liegen an einem Ort, der Business Layer enthält kein SQL.

## Aufgaben
- [ ] `persistence/data_access.py` mit `SpielerRepository` (`alle_nach_elo`, `finde`, `finde_nach_name`, `hinzufuegen`, `speichern`)
- [ ] `SpielRepository` (`finde`, `letztes`, `hinzufuegen`, `loeschen`, `speichern`)
- [ ] Session über `Depends(get_session)`

## Akzeptanzkriterien
- [ ] Jede Methode ist durch einen Test abgedeckt

## Tests
- [ ] `test_alle_nach_elo_sortiert`
- [ ] `test_finde_nach_name`
- [ ] `test_letztes_spiel`
- [ ] `test_loeschen`

## Hinweise
Skript Block 3, Abb. 4: «Data Access» im Persistence Layer.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
