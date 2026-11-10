# T18 · Elo-Berechnung

**Meilenstein:** M3 · Business Service Layer  
**Schicht/Typ:** Business, Test  
**Schätzung:** 2 h  
**Abhängig von:** T03

## Ziel
Die Elo-Formel aus dem Schach ist als reine Python-Funktion umgesetzt und getestet.

## Aufgaben
- [x] `business/elo.py` mit den Konstanten `START_RATING = 1200` und `K_FACTOR = 32`
- [x] `team_rating(ratings)`: Durchschnitt eines Teams (1 vs 1: eine Wertung)
- [x] `win_probability(rating_a, rating_b)`: Siegchance von A (0 bis 1)
- [x] `rating_change(rating_winner, rating_loser)`: Punkte für Gewinner bzw. Verlierer
- [x] `new_ratings(team_a, team_b, team_a_wins)`: neue Wertungen beider Teams als Listen, funktioniert für 1 vs 1 und 2 vs 2
## Akzeptanzkriterien
- [x] Ergebnisse stimmen mit der Tabelle im README (Business-Regeln) überein
- [x] `elo.py` kennt nur Zahlen: keine Spieler, keine Datenbank, kein HTTP
- [x] Code auf Englisch, einheitlich `rating` statt `elo` in Variablen- und Funktionsnamen

## Tests
- [x] `test_constants`
- [x] `test_win_probability_equal_ratings_is_half`: 0.5
- [x] `test_equal_ratings_change_16`: 1200 gegen 1200 → 16
- [x] `test_underdog_wins_24`: 1200 schlägt 1400 → 24
- [x] `test_favourite_wins_8`: 1400 schlägt 1200 → 8
- [x] `test_team_rating_is_average`: [1200, 1400] → 1300
- [x] `test_new_ratings_team_a_wins`: ([1200], [1200], True) → ([1216], [1184])
- [x] `test_new_ratings_team_b_wins`: ([1200], [1400], False) → ([1192], [1408])
- [x] `test_new_ratings_2vs2_both_players_get_same_points`
## Hinweise
Erweitert gegenüber der ursprünglichen Planung: `new_ratings` arbeitet mit Teams (Listen),
damit die Berechnung später auch für 2 vs 2 funktioniert. Für 2 vs 2 müsste zusätzlich
das Datenmodell angepasst werden (siehe T05).
## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
