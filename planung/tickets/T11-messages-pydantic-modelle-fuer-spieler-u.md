# T11 · Messages (Pydantic-Modelle) für Spieler und Spiel

**Meilenstein:** M2 · Web/REST Service Layer  
**Schicht/Typ:** Service  
**Schätzung:** 2 h  
**Abhängig von:** T04

## Ziel
Das JSON-Format jeder Anfrage und Antwort ist als Python-Klasse festgelegt.

## Aufgaben
- [ ] `service/messages.py` anlegen
- [ ] Anfragen: `SpielerErstellen`, `SpielErfassen`, `ResultatKorrigieren`
- [ ] Antworten: `SpielerAntwort`, `SpielAntwort` (enthält zwei `SpielerAntwort`), `FehlerAntwort`
- [ ] Felder genau wie in `docs/service.md`

## Akzeptanzkriterien
- [ ] Alle Felder aus der Service-Beschreibung vorhanden, mit Datentyp

## Tests
- [ ] `tests/test_messages.py`: gültiges JSON → Objekt wird erstellt
- [ ] Falscher Datentyp (z. B. `tore_a: "zehn"`) → `ValidationError`

## Hinweise
Skript Block 3, Abb. 4: «Messages» im Web/REST Service Layer.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
