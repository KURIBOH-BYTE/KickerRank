# T32 · Erweiterung (optional): Spielerprofil mit Elo-Verlauf

**Meilenstein:** M5 · Erweiterungen (volle Punktzahl)  
**Schicht/Typ:** Erweiterung  
**Schätzung:** 4 h  
**Abhängig von:** T29

## Ziel
Klick auf einen Spieler zeigt seine Statistik und ein Diagramm seiner Elo über die Zeit.

## Aufgaben
- [ ] Business: Elo-Verlauf aus `elo_a_vorher`/`elo_b_vorher` und `elo_aenderung` berechnen
- [ ] Service: `GET /api/spieler/{id}/profil`
- [ ] Präsentation: Detailansicht wie in Übung 1, Aufgabe 3; Diagramm mit Chart.js

## Akzeptanzkriterien
- [ ] Diagramm zeigt alle Spiele des Spielers in der richtigen Reihenfolge

## Tests
- [ ] `test_profil_elo_verlauf`
- [ ] API-Test

## Hinweise
Aufwendigste Erweiterung, wirkt aber stark in der Präsentation (komplexere Oberfläche).

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
