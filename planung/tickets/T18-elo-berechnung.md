# T18 · Elo-Berechnung

**Meilenstein:** M3 · Business Service Layer  
**Schicht/Typ:** Business, Test  
**Schätzung:** 2 h  
**Abhängig von:** T03

## Ziel
Die Elo-Formel aus dem Schach ist als reine Python-Funktion umgesetzt und getestet.

## Aufgaben
- [ ] `business/elo.py` mit `erwartung(elo_a, elo_b)` und `elo_aenderung(elo_gewinner, elo_verlierer, k=32)`
- [ ] Konstanten `START_ELO = 1200` und `K_FAKTOR = 32`

## Akzeptanzkriterien
- [ ] Ergebnisse stimmen mit der Tabelle in `docs/` überein

## Tests
- [ ] `test_gleich_stark_gibt_16`: 1200 gegen 1200 → 16
- [ ] `test_aussenseiter_gewinnt_24`: 1200 schlägt 1400 → 24
- [ ] `test_favorit_gewinnt_8`: 1400 schlägt 1200 → 8
- [ ] `test_erwartung_gleich_stark_ist_halb`: 0.5

## Hinweise
Guter Einstieg in Unit-Tests, weil weder Web noch Datenbank im Spiel sind. Zuerst die Tests schreiben, dann die Funktion.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
