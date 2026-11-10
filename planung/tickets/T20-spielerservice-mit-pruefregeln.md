# T20 · SpielerService mit Prüfregeln

**Meilenstein:** M3 · Business Service Layer  
**Schicht/Typ:** Business, Test  
**Schätzung:** 2.5 h  
**Abhängig von:** T19

## Ziel
Alle Regeln zum Spieler liegen im Business Layer, die Endpunkte rufen nur noch den Service auf.

## Aufgaben
- [ ] `business/spieler_service.py` mit `spieler_anlegen(name, abteilung)` und `rangliste()`
- [ ] Regeln: Name nicht leer, max. 100 Zeichen, nicht doppelt, Abteilung aus der festen Liste
- [ ] Endpunkte in `spieler_endpoints.py` rufen den Service auf (via `Depends`)
- [ ] Die Liste der Abteilungen nur noch an einer Stelle im Business Layer

## Akzeptanzkriterien
- [ ] `spieler_endpoints.py` enthält keine `if`-Prüfungen mehr

## Tests
- [ ] `test_leerer_name_gibt_fehler`
- [ ] `test_doppelter_name_gibt_fehler`
- [ ] `test_unbekannte_abteilung_gibt_fehler`
- [ ] API-Test: `POST /api/spieler` mit leerem Namen → 400

## Hinweise
Skript Block 3: Geschäftslogik nur im Business Service Layer, Komponenten über `Depends` verbinden.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
