# T12 · Endpunkte Rangliste und Abteilungen (Daten im Speicher)

**Meilenstein:** M2 · Web/REST Service Layer  
**Schicht/Typ:** Service  
**Schätzung:** 2 h  
**Abhängig von:** T11, T03

## Ziel
Erste echte Endpunkte. Die Daten liegen vorerst in einer Python-Liste, die Datenbank kommt in M4.

## Aufgaben
- [ ] `service/spieler_endpoints.py` mit `APIRouter(prefix="/api")`
- [ ] Vorläufig eine Liste mit Testspielern im Modul (wird in T27 ersetzt)
- [ ] `GET /api/rangliste`: Spieler nach Elo absteigend
- [ ] `GET /api/abteilungen`: Liste der 5 Abteilungen
- [ ] Router in `main.py` einbinden, **vor** dem Static-Mount

## Akzeptanzkriterien
- [ ] <http://localhost:8000/api/rangliste> liefert JSON
- [ ] Beide Endpunkte erscheinen in <http://localhost:8000/docs>

## Tests
- [ ] `test_rangliste_ist_nach_elo_sortiert`
- [ ] `test_abteilungen_enthalten_informatik`

## Hinweise
Mit Swagger UI (`/docs`) oder Postman ausprobieren. Testdaten pro Test zurücksetzen (pytest-Fixture), sonst beeinflussen sich die Tests gegenseitig.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
