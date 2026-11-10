# T21 · SpielService: Spiel erfassen mit Regeln und Elo

**Meilenstein:** M3 · Business Service Layer  
**Schicht/Typ:** Business, Test  
**Schätzung:** 3 h  
**Abhängig von:** T18, T20

## Ziel
Beim Erfassen eines Spiels werden alle Regeln geprüft und die Elo beider Spieler berechnet.

## Aufgaben
- [ ] `business/spiel_service.py` mit `spiel_erfassen(...)`
- [ ] Regeln: zwei verschiedene, existierende Spieler; Tore 0–10; genau ein Spieler hat 10
- [ ] Wertung vor dem Spiel und Punkteänderung im Spiel speichern, neue Wertungen mit `new_ratings([a.rating], [b.rating], a_wins)` aus `business/elo.py` berechnen
- [ ] Endpunkt `POST /api/spiele` ruft nur noch den Service auf

## Akzeptanzkriterien
- [ ] Nach einem Spiel 1200 gegen 1200 stehen die Spieler bei 1216 und 1184

## Tests
- [ ] `test_gegen_sich_selbst_gibt_fehler`
- [ ] `test_kein_spieler_mit_10_toren_gibt_fehler`
- [ ] `test_beide_mit_10_toren_gibt_fehler`
- [ ] `test_elo_wird_angepasst`
- [ ] `test_anzahl_spiele_steigt`

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
