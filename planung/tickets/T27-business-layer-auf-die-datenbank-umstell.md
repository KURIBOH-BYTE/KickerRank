# T27 · Business Layer auf die Datenbank umstellen

**Meilenstein:** M4 · Persistence Layer  
**Schicht/Typ:** Business, Persistence, Test  
**Schätzung:** 3 h  
**Abhängig von:** T23, T26

## Ziel
Die Python-Listen aus M2 verschwinden, alle Daten liegen in der Datenbank.

## Aufgaben
- [ ] Services erhalten die Repositories über `Depends()`
- [ ] Listen im Speicher entfernen
- [ ] Spiel erfassen speichert Spiel und beide Spieler in einer Transaktion (ein `commit`)
- [ ] API-Tests verwenden die Test-Datenbank (`app.dependency_overrides`)

## Akzeptanzkriterien
- [ ] Nach einem Neustart sind alle Spieler und Spiele noch da
- [ ] Alle Tests grün

## Tests
- [ ] Alle bestehenden Tests
- [ ] `test_daten_bleiben_nach_neuer_session_erhalten`

## Hinweise
Zum Testen mit eigener Datenbank: <https://fastapi.tiangolo.com/advanced/testing-dependencies/>

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
