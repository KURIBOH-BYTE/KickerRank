# T24 · Datenbankverbindung mit SQLAlchemy

**Meilenstein:** M4 · Persistence Layer  
**Schicht/Typ:** Persistence, Test  
**Schätzung:** 2 h  
**Abhängig von:** T05, T03

## Ziel
Die App hat eine SQLite-Datenbank, die Tests eine eigene Datenbank im Speicher.

## Aufgaben
- [ ] `persistence/database.py`: `engine`, `SessionLocal`, `class Base(DeclarativeBase)`, `get_session()`, `init_db()`
- [ ] `init_db()` beim Start in `main.py` aufrufen
- [ ] `kicker.db` in `.gitignore`
- [ ] `tests/conftest.py`: Fixture mit `sqlite:///:memory:` und eigener Session

## Akzeptanzkriterien
- [ ] Beim Start entsteht `kicker.db`
- [ ] Tests schreiben nie in `kicker.db`

## Tests
- [ ] `test_init_db_erstellt_tabellen`

## Hinweise
Für MySQL müsste nur die Verbindungs-URL geändert werden. Das ist ein gutes Argument für die Verteidigung.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
