# T08 · Rangliste aus JSON-Testdaten anzeigen

**Meilenstein:** M1 · Presentation Layer  
**Schicht/Typ:** Presentation  
**Schätzung:** 2 h  
**Abhängig von:** T07

## Ziel
Die Rangliste wird per AJAX geladen, zuerst noch aus einer statischen JSON-Datei.

## Aufgaben
- [ ] `presentation/testdaten/rangliste.json` mit 5 Spielern (id, name, abteilung, elo, anzahl_spiele)
- [ ] Tabelle mit `<thead>` (Platz, Name, Abteilung, Elo, Spiele) und leerem `<tbody>`
- [ ] Mit `$.getJSON(...).done(...)` laden, `empty()` und pro Spieler eine Zeile mit `append()` einfügen
- [ ] Platz aus dem Index berechnen (1, 2, 3, ...)

## Akzeptanzkriterien
- [ ] Tabelle zeigt alle Spieler aus der JSON-Datei, sortiert nach Elo
- [ ] Erste Zeile ist hervorgehoben

## Tests
- [ ] Manueller Testfall M2: JSON-Datei ändern, Seite neu laden, Änderung sichtbar

## Hinweise
Genau das Muster aus Übung 1, Aufgabe 1 (`handleCustomerlistReply`). In M2 wird nur die URL ausgetauscht.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
