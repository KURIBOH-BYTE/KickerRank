# T05 · Datenmodell und ER-Diagramm dokumentieren

**Meilenstein:** M0 · Setup und Planung  
**Schicht/Typ:** Doku, Persistence  
**Schätzung:** 2 h  
**Abhängig von:** –

## Ziel
Die beiden Entitäten Spieler und Spiel sind mit allen Attributen und Beziehungen festgelegt.

## Aufgaben
- [ ] `docs/datenmodell.md` mit ER-Diagramm (Mermaid oder Bild)
- [ ] Alle Attribute mit Datentyp und Regeln (wie in der README-Tabelle)
- [ ] Die doppelte Beziehung Spiel → Spieler (A und B) erklären
- [ ] Designentscheidungen begründen: Abteilung als Text, redundante Wertung (`rating`), Wertung vor dem Spiel im Spiel gespeichert, Gewinner nicht gespeichert, MySQL gemäss Skript
- [ ] Namen für den Code auf Englisch festlegen: Tabellen `player` und `game`, Spalten z. B. `name`, `department`, `rating`, `games_played`, `goals_a`, `goals_b`, `rating_a_before`, `rating_b_before`, `rating_change`
- [ ] Für jede Textspalte eine maximale Länge festlegen (MySQL verlangt z. B. `VARCHAR(100)`)

## Akzeptanzkriterien
- [ ] ER-Diagramm in konzeptueller Notation wie in der DB-Vorlesung
- [ ] Mindestens 4 Designentscheidungen begründet
- [ ] Englische Tabellen- und Spaltennamen festgelegt und von der Gruppe bestätigt

## Tests
- [ ] Review durch ein anderes Gruppenmitglied

## Hinweise
Diese Datei wird direkt Teil der Abgabe-Beschreibung.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
