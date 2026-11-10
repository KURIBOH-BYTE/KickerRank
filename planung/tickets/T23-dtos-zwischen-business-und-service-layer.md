# T23 · DTOs zwischen Business und Service Layer

**Meilenstein:** M3 · Business Service Layer  
**Schicht/Typ:** Business, Service  
**Schätzung:** 2 h  
**Abhängig von:** T22

## Ziel
Der Business Layer gibt DTOs zurück, die Endpunkte wandeln sie in Messages um.

## Aufgaben
- [ ] `business/dtos.py` mit `SpielerDTO` und `SpielDTO` (`@dataclass`)
- [ ] Services geben nur DTOs zurück
- [ ] Endpunkte: `response_model=...` mit `from_attributes=True` in den Messages

## Akzeptanzkriterien
- [ ] Alle bisherigen Tests bleiben grün
- [ ] Kein Endpunkt greift direkt auf interne Daten zu

## Tests
- [ ] Alle bestehenden Tests

## Hinweise
Skript Block 3, Abb. 4: «DTOs» im Business Service Layer. In der Verteidigung den Unterschied DTO ↔ Message erklären können.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
