# T04 · Service-Beschreibung im Schema der Übung 1 erstellen

**Meilenstein:** M0 · Setup und Planung  
**Schicht/Typ:** Doku, Service  
**Schätzung:** 2 h  
**Abhängig von:** –

## Ziel
Die REST-Schnittstelle ist festgelegt, bevor programmiert wird (entspricht Übung 1, Aufgabe 4).

## Aufgaben
- [ ] `docs/service.md` anlegen
- [ ] Für jeden Endpunkt im Schema des «Customer Management»-Service beschreiben: URL, Method, Parameter bzw. Request Body, Response mit Statuscodes
- [ ] Endpunkte: `GET /api/rangliste`, `GET /api/abteilungen`, `POST /api/spieler`, `POST /api/spiele`, `GET /api/spiele/letztes`, `PUT /api/spiele/{id}`, `DELETE /api/spiele/{id}`
- [ ] Je ein JSON-Beispiel für Spieler und Spiel

## Akzeptanzkriterien
- [ ] Alle 7 Endpunkte beschrieben
- [ ] Fehlerfall (400 mit `{"fehler": "..."}`) und 404 dokumentiert
- [ ] Von allen Gruppenmitgliedern gelesen

## Tests
- [ ] Review durch ein anderes Gruppenmitglied (Kommentar im Ticket)

## Hinweise
Vorlage: Kapitel 5 in `e1_ex1_customer_list.pdf`. Im Gesamtentwurf und in der Referenz ist die API schon skizziert.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
