# T19 · Fehlerklasse und einheitliche Fehlerantwort

**Meilenstein:** M3 · Business Service Layer  
**Schicht/Typ:** Business, Service  
**Schätzung:** 1.5 h  
**Abhängig von:** T12

## Ziel
Verletzte Regeln werden einheitlich als HTTP 400 mit Meldung zurückgegeben.

## Aufgaben
- [ ] `business/fehler.py` mit `class GeschaeftsFehler(Exception)`
- [ ] In `main.py` einen `exception_handler` registrieren: `GeschaeftsFehler` → `JSONResponse(status_code=400, content={"fehler": str(e)})`

## Akzeptanzkriterien
- [ ] Jeder `GeschaeftsFehler` kommt beim Browser als 400 mit `fehler` an

## Tests
- [ ] `test_geschaeftsfehler_wird_zu_400` (mit einer Test-Route oder in T20)

## Hinweise
So bleibt der Business Layer frei von HTTP. Er wirft nur Fehler, der Service Layer übersetzt sie.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
