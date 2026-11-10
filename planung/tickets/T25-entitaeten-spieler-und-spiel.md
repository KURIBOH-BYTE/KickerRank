# T25 · Entitäten Spieler und Spiel

**Meilenstein:** M4 · Persistence Layer  
**Schicht/Typ:** Persistence, Test  
**Schätzung:** 3 h  
**Abhängig von:** T24

## Ziel
Die beiden Entitäten aus dem ER-Diagramm sind als SQLAlchemy-Klassen umgesetzt.

## Aufgaben
- [ ] `persistence/entities.py` mit `Spieler` und `Spiel` (von `Base` abgeleitet)
- [ ] `Spiel` hat zwei Fremdschlüssel auf `spieler` (`spieler_a_id`, `spieler_b_id`) und zwei `relationship`s mit `foreign_keys`
- [ ] Spalten und Regeln genau wie in `docs/datenmodell.md`
- [ ] `gewinner` als `@property` aus den Toren

## Akzeptanzkriterien
- [ ] Tabellen in `kicker.db` entsprechen dem ER-Diagramm (Prüfen mit DB Browser for SQLite)

## Tests
- [ ] `test_spieler_speichern_und_lesen`
- [ ] `test_spiel_mit_zwei_spielern`
- [ ] `test_gewinner_property`
- [ ] `test_name_ist_eindeutig` (IntegrityError)

## Hinweise
Die doppelte Beziehung braucht `foreign_keys=...`, sonst weiss SQLAlchemy nicht, welcher Fremdschlüssel gemeint ist.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
