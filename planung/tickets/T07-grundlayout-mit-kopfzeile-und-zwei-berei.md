# T07 · Grundlayout mit Kopfzeile und zwei Bereichen

**Meilenstein:** M1 · Presentation Layer  
**Schicht/Typ:** Presentation  
**Schätzung:** 2 h  
**Abhängig von:** T01

## Ziel
Die Seite hat einen Kopf mit Navigation und zwei Bereiche: Rangliste und Spiel erfassen.

## Aufgaben
- [ ] `index.html`: Kopfzeile mit Titel und zwei Buttons
- [ ] Zwei `<section>`-Elemente, eines davon ist versteckt
- [ ] Mit jQuery beim Klick auf einen Button den passenden Bereich anzeigen (`.show()` / `.hide()` oder eine CSS-Klasse)
- [ ] `css/style.css` mit einfachem, einheitlichem Design

## Akzeptanzkriterien
- [ ] Umschalten zwischen den Bereichen funktioniert ohne Neuladen
- [ ] Der aktive Button ist hervorgehoben

## Tests
- [ ] Manueller Testfall M1 in `tests/manuelle_tests.md` anlegen und durchführen

## Hinweise
Ähnlich wie eure Übung «Menüpunkte» und die jQuery-Übung mit `.on("click", ...)`.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
