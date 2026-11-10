# Manuelle Testfälle

Testfälle für die Oberfläche, die nicht automatisch mit pytest geprüft werden.
Vor jedem Pull Request, der die Oberfläche betrifft, durchführen und das Ergebnis eintragen.

| Nr | Ticket | Schritte | Erwartet | Ergebnis | Datum | Getestet von |
|---|---|---|---|---|---|---|
| M1 | T07 | 1. Seite <http://localhost:8000> öffnen<br>2. Auf «New game» klicken<br>3. Auf «Ranking» klicken | Beim Öffnen ist nur «Ranking» sichtbar. Nach Schritt 2 ist nur «New game» sichtbar, nach Schritt 3 nur «Ranking». Der aktive Button ist jeweils weiss hervorgehoben. Die Seite lädt nicht neu, die Browser-Konsole (F12) zeigt keine Fehler. | ✅ bestanden | 10.11.2026 | Claude (Chromium, 800 px Breite) |
