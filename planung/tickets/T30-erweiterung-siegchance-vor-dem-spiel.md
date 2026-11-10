# T30 · Erweiterung: Siegchance vor dem Spiel

**Meilenstein:** M5 · Erweiterungen (volle Punktzahl)  
**Schicht/Typ:** Erweiterung  
**Schätzung:** 2.5 h  
**Abhängig von:** T27

## Ziel
Nach Auswahl der beiden Spieler zeigt das Formular «Lisa gewinnt mit 64 %».

## Aufgaben
- [ ] Business: `prognose(spieler_a_id, spieler_b_id)` nutzt `win_probability()` aus `business/elo.py`
- [ ] Service: `GET /api/prognose?a=1&b=2`
- [ ] Präsentation: bei jeder Änderung eines Dropdowns abfragen und anzeigen

## Akzeptanzkriterien
- [ ] Gleich starke Spieler → 50 %

## Tests
- [ ] `test_prognose_gleich_stark`
- [ ] API-Test mit unbekanntem Spieler → 400

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
