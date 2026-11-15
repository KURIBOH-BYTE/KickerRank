# Manuelle Testfälle

Testfälle für die Oberfläche, die nicht automatisch mit pytest geprüft werden.
Vor jedem Pull Request, der die Oberfläche betrifft, durchführen und das Ergebnis eintragen.

| Nr | Ticket | Schritte | Erwartet | Ergebnis | Datum | Getestet von |
|---|---|---|---|---|---|---|
| M1 | T07 | 1. Seite <http://localhost:8000> öffnen<br>2. Auf «New game» klicken<br>3. Auf «Ranking» klicken | Beim Öffnen ist nur «Ranking» sichtbar. Nach Schritt 2 ist nur «New game» sichtbar, nach Schritt 3 nur «Ranking». Der aktive Button ist jeweils weiss hervorgehoben. Die Seite lädt nicht neu, die Browser-Konsole (F12) zeigt keine Fehler. | ✅ bestanden | 10.11.2026 | Claude (Chromium, 800 px Breite) |
| M2 | T08 | 1. Server starten und <http://localhost:8000> öffnen<br>2. In `presentation/test_data/ranking.json` einen Spieler mit höherem Elo an die erste Stelle setzen<br>3. Seite neu laden | Nach Schritt 1 zeigt die Tabelle alle 5 Spieler aus der JSON-Datei, die Plätze 1 bis 3 sind gold, silber und bronze markiert. Nach Schritt 3 steht der geänderte Spieler auf Platz 1 mit der Goldmarkierung. Die Browser-Konsole zeigt keine Fehler. | ✅ bestanden | 13.11.2026 | Claude (Chromium, 800 px Breite) |
| M3 | T09 | 1. Server starten, <http://localhost:8000> öffnen, «New game» klicken<br>2. Bei Player A und Player B denselben Spieler wählen, Tore 10 und 7<br>3. «Save game» klicken | Unter dem Formular erscheint rot «A player cannot play against themselves.». In der Konsole wird nichts ausgegeben. | ✅ bestanden | 15.11.2026 | Claude (Chromium, 800 px Breite) |
| M4 | T09 | 1. Zwei verschiedene Spieler wählen<br>2. Bei Player A 10 Tore eintragen, das Torfeld von Player B leer lassen<br>3. «Save game» klicken | Unter dem Formular erscheint rot «Please enter the goals for both players.». In der Konsole wird nichts ausgegeben. | ✅ bestanden | 15.11.2026 | Claude (Chromium, 800 px Breite) |
| M5 | T09 | 1. Lukas Müller gegen Sarah Meier wählen, Tore 10 und 7<br>2. «Save game» klicken<br>3. Browser-Konsole (F12) öffnen | Keine Fehlermeldung, grün erscheint «Input is valid. Saving follows in T17.». Die Konsole zeigt `{player_a_id: 3, player_b_id: 1, goals_a: 10, goals_b: 7}`. | ✅ bestanden | 15.11.2026 | Claude (Chromium, 800 px Breite) |
