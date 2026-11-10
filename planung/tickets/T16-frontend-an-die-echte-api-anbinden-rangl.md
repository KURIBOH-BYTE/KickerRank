# T16 · Frontend an die echte API anbinden: Rangliste und Spieler

**Meilenstein:** M2 · Web/REST Service Layer  
**Schicht/Typ:** Presentation, Service  
**Schätzung:** 2 h  
**Abhängig von:** T08, T10, T13

## Ziel
Die Seite holt ihre Daten vom eigenen Server statt aus der JSON-Datei.

## Aufgaben
- [ ] In `main.js` die URL von `testdaten/rangliste.json` auf `/api/rangliste` ändern
- [ ] Abteilungs-Dropdown aus `/api/abteilungen` füllen
- [ ] Formular «Spieler hinzufügen» schickt `POST /api/spieler` mit `$.ajax` (JSON), danach Rangliste neu laden
- [ ] Testdaten-Ordner löschen

## Akzeptanzkriterien
- [ ] Neu angelegter Spieler erscheint sofort in der Rangliste, ohne Neuladen der Seite

## Tests
- [ ] Manuelle Testfälle M7, M8

## Hinweise
Für POST mit JSON braucht `$.ajax` die Optionen `method: "POST"`, `contentType: "application/json"` und `data: JSON.stringify(...)`.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
