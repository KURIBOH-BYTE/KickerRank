# T01 · Referenzcode sichern und Projekt-Skelett aufsetzen

**Meilenstein:** M0 · Setup und Planung  
**Schicht/Typ:** Setup  
**Schätzung:** 2 h  
**Abhängig von:** –

## Ziel
Der KI-Entwurf bleibt als Referenz erhalten, auf `main` startet ihr mit einem leeren, lauffähigen Skelett wie im Beispielprojekt aus Übung 0.

## Aufgaben
- [ ] Aktuellen Stand als Branch sichern: `git switch -c referenz-ki` und `git push -u origin referenz-ki`, danach `git switch main`
- [ ] Auf `main` die Ordner `presentation/`, `service/`, `business/`, `persistence/` leeren (nur je eine leere `__init__.py` behalten, `presentation/` mit leerer `index.html`)
- [ ] `app.py` in `main.py` umbenennen und auf das Beispielprojekt reduzieren: FastAPI-App, die `presentation/` als statische Dateien ausliefert
- [ ] `requirements.txt`: `fastapi`, `uvicorn[standard]`, `sqlalchemy`, `pytest`, `httpx`
- [ ] `index.html` zeigt «KickerRank» an und bindet jQuery ein, `js/main.js` schreibt «Hello World» in die Konsole

## Akzeptanzkriterien
- [ ] `python main.py` startet, <http://localhost:8000> zeigt «KickerRank»
- [ ] Branch `referenz-ki` ist auf GitHub sichtbar
- [ ] README-Startanleitung stimmt mit `main.py` überein

## Tests
- [ ] Manuell: Seite lädt, Browser-Konsole (F12) zeigt «Hello World»

## Hinweise
Vorlage: Ordner `Python Webserver Basics/1_WebServerBasic_Python`. Im Referenz-Branch könnt ihr später nachschauen, wenn ihr nicht weiterkommt, aber zuerst selbst versuchen.

## Definition of Done
- [ ] Akzeptanzkriterien erfüllt
- [ ] Tests geschrieben und grün (`pytest`)
- [ ] Von einem anderen Gruppenmitglied gereviewt
- [ ] Quellen in T36 ergänzt (falls etwas Neues verwendet)
