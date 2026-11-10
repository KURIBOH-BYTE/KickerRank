# T17 · Frontend an die echte API anbinden: Spiele

**Meilenstein:** M2 · Web/REST Service Layer  
**Schicht/Typ:** Presentation, Service  
**Schätzung:** 3 h  
**Abhängig von:** T09, T15, T16

## Ziel
Spiele lassen sich über die Oberfläche erfassen, korrigieren und löschen.

## Aufgaben
- [ ] Formular «Spiel erfassen» schickt `POST /api/spiele`
- [ ] Box «Letztes Spiel» lädt `/api/spiele/letztes`
- [ ] Buttons «Korrigieren» (`PUT`) und «Löschen» (`DELETE`) anbinden
- [ ] Fehler vom Server (`.fail(...)`) unter dem Formular anzeigen

## Akzeptanzkriterien
- [ ] Kompletter Ablauf erfassen → korrigieren → löschen funktioniert im Browser
- [ ] Rangliste und Box aktualisieren sich nach jeder Aktion

## Tests
- [ ] Manuelle Testfälle M9 bis M11

## Hinweise
Ab hier ist die Mindestanforderung «CRUD im GUI genutzt» technisch erfüllt. Es fehlen aber noch Logik und Datenbank.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
