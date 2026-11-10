# T03 · Test-Setup mit pytest einrichten

**Meilenstein:** M0 · Setup und Planung  
**Schicht/Typ:** Setup, Test  
**Schätzung:** 1.5 h  
**Abhängig von:** T01

## Ziel
Automatische Tests laufen mit einem Befehl. Ab jetzt hat jedes Ticket Tests.

## Aufgaben
- [ ] Ordner `tests/` mit leerer `__init__.py` anlegen
- [ ] `tests/test_start.py`: mit `fastapi.testclient.TestClient` prüfen, dass `GET /` den Status 200 liefert
- [ ] Im README einen Abschnitt «Tests ausführen» ergänzen: `pytest`

## Akzeptanzkriterien
- [ ] `pytest` im Projektordner zeigt 1 passed

## Tests
- [ ] `test_startseite_ist_erreichbar`

## Hinweise
Doku: <https://fastapi.tiangolo.com/tutorial/testing/>. Jeder Test ist eine Funktion, die mit `test_` beginnt und `assert` verwendet.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
