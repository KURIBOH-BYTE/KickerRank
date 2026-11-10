# T28 · Demo-Daten beim ersten Start

**Meilenstein:** M4 · Persistence Layer  
**Schicht/Typ:** Persistence  
**Schätzung:** 1 h  
**Abhängig von:** T27

## Ziel
Die App ist beim ersten Start nicht leer, das hilft bei Präsentation und Abgabe.

## Aufgaben
- [ ] Beim Start: wenn keine Spieler existieren, 6 Demo-Spieler anlegen (über den SpielerService, nicht direkt in die DB)

## Akzeptanzkriterien
- [ ] Erster Start mit leerer DB zeigt 6 Spieler
- [ ] Zweiter Start legt keine Duplikate an

## Tests
- [ ] `test_demo_daten_nur_einmal`

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
