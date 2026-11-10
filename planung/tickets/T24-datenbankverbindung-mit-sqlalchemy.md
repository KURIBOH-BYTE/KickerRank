# T24 · Datenbankverbindung mit SQLAlchemy und MySQL

**Meilenstein:** M4 · Persistence Layer  
**Schicht/Typ:** Persistence, Test  
**Schätzung:** 3.5 h  
**Abhängig von:** T05, T03

## Ziel
Die App speichert ihre Daten wie im Skript vorgesehen in MySQL. Die Tests verwenden eine eigene SQLite-Datenbank im Arbeitsspeicher.

## Aufgaben
- [ ] Alle Gruppenmitglieder installieren MySQL lokal (siehe README, Abschnitt «MySQL einrichten»)
- [ ] `docs/setup.sql`: legt Datenbank `kickerrank` (utf8mb4) und Benutzer `kicker` an
- [ ] `config.py` mit `DATABASE_URL = "mysql+pymysql://kicker:kicker@localhost:3306/kickerrank"`
- [ ] `requirements.txt`: `pymysql` und `cryptography` ergänzen
- [ ] `persistence/database.py`: `engine` (aus `config.DATABASE_URL`), `SessionLocal`, `class Base(DeclarativeBase)`, `get_session()`, `init_db()`
- [ ] `init_db()` beim Start in `main.py` aufrufen
- [ ] `tests/conftest.py`: Fixture mit `sqlite:///:memory:` und eigener Session

## Akzeptanzkriterien
- [ ] Beim Start werden die Tabellen in der MySQL-Datenbank `kickerrank` angelegt
- [ ] `uv run pytest` läuft auch ohne laufenden MySQL-Server
- [ ] README-Abschnitt «MySQL einrichten» stimmt mit dem Vorgehen überein

## Tests
- [ ] `test_init_db_erstellt_tabellen`

## Hinweise
Das Skript (Block 3) verlangt MySQL. Dank SQLAlchemy steckt die Datenbank nur in `DATABASE_URL`, das ist ein gutes Argument für die Verteidigung. Bevor ihr startet: prüfen, ob der Dozent in der Vorlesung zur Persistenz ein bestimmtes Vorgehen zeigt, und dieses übernehmen.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
