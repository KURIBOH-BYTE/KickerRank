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
- [ ] Designentscheidungen begründen: Abteilung als Text, redundante Elo, `elo_vorher` im Spiel, Gewinner nicht gespeichert

## Akzeptanzkriterien
- [ ] ER-Diagramm in konzeptueller Notation wie in der DB-Vorlesung
- [ ] Mindestens 4 Designentscheidungen begründet

## Tests
- [ ] Review durch ein anderes Gruppenmitglied

## Hinweise
Diese Datei wird direkt Teil der Abgabe-Beschreibung.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
