# T31 · Erweiterung: Spieler bearbeiten und löschen

**Meilenstein:** M5 · Erweiterungen (volle Punktzahl)  
**Schicht/Typ:** Erweiterung  
**Schätzung:** 3 h  
**Abhängig von:** T27

## Ziel
CRUD ist auch für Spieler vollständig.

## Aufgaben
- [ ] `PUT /api/spieler/{id}`: Name und Abteilung ändern (gleiche Regeln wie beim Anlegen)
- [ ] `DELETE /api/spieler/{id}`: nur erlaubt, wenn der Spieler noch keine Spiele hat
- [ ] Präsentation: Bearbeiten und Löschen in der Rangliste

## Akzeptanzkriterien
- [ ] Spieler mit Spielen kann nicht gelöscht werden, verständliche Meldung

## Tests
- [ ] `test_spieler_umbenennen`
- [ ] `test_spieler_mit_spielen_loeschen_gibt_fehler`
- [ ] `test_spieler_ohne_spiele_loeschen`

## Hinweise
Alternative zu Löschen: Spieler deaktivieren. Das wäre eine zusätzliche Spalte, also im ER-Diagramm nachführen.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
