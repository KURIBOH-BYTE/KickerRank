# Kicker-Liga

Web-Applikation für Tischkicker-Spiele (1 vs 1) im Büro mit einer Elo-Rangliste wie im Schach.

Projektarbeit im Modul *Webbasierte Anwendungen*, FHNW, HS2026.

**Gruppe:**   Fabrice Balzan, Ryo Flückiger, Ryan Wolf

---

## Inhalt

1. [Szenario](#szenario)
2. [Installation und Start](#installation-und-start)
3. [Ordnerstruktur](#ordnerstruktur)
4. [Architektur](#architektur)
5. [Datenmodell](#datenmodell)
6. [Business-Regeln](#business-regeln)
7. [REST-API](#rest-api)
8. [Testen](#testen)
9. [Designentscheidungen](#designentscheidungen)
10. [Mögliche Erweiterungen](#mögliche-erweiterungen)
11. [Quellen und Hilfsmittel](#quellen-und-hilfsmittel)

---

## Szenario

Im Büro steht ein Tischkicker, und jeder behauptet, der Beste zu sein. Die Kicker-Liga erfasst die Spiele und berechnet eine faire Rangliste.

- Jeder Spieler startet mit **1200 Elo-Punkten**.
- Nach einem Spiel gibt man nur ein, **wer gegen wen** gespielt hat und **wie es ausging** (z. B. 10 : 7).
- Die App berechnet die neuen Punkte wie im Schach: Wer einen Stärkeren schlägt, gewinnt viel. Wer als Favorit verliert, verliert viel.

**Funktionen**

| Funktion | CRUD |
|---|---|
| Spiel erfassen (1 vs 1), Elo wird automatisch berechnet | Create |
| Rangliste nach Elo anzeigen | Read |
| Letztes Spiel korrigieren (Resultat ändern), Elo wird neu berechnet | Update |
| Letztes Spiel löschen, Elo wird zurückgesetzt | Delete |
| Spieler anlegen (Name, Abteilung) | Create |

---

## Installation und Start

**Voraussetzung:** Python 3.10 oder neuer

```bash
# 1. In den Projektordner wechseln
cd kicker-liga

# 2. Virtuelle Umgebung erstellen und aktivieren
python3 -m venv .venv
source .venv/bin/activate        # Mac / Linux
# .venv\Scripts\activate         # Windows

# 3. Abhängigkeiten installieren
pip install -r requirements.txt

# 4. Starten
python app.py
```

Danach im Browser öffnen: **<http://localhost:8000>**

- Beim ersten Start wird die Datenbank `kicker.db` (SQLite) automatisch angelegt und mit 6 Demo-Spielern gefüllt.
- Datenbank zurücksetzen: `kicker.db` löschen und neu starten.
- Stoppen: `Ctrl + C` im Terminal.
- Die Oberfläche lädt jQuery von einem CDN, braucht also eine Internetverbindung.

---

## Ordnerstruktur

Die Ordner entsprechen den Schichten aus der Architekturübersicht der Vorlesung (Block 3, Abbildung 4).

```
kicker-liga/
├── app.py                      # Startpunkt: FastAPI-App, Router, Fehlerbehandlung, Demo-Daten
├── requirements.txt            # Abhängigkeiten (FastAPI, Uvicorn, SQLAlchemy)
├── README.md                   # Diese Beschreibung
│
├── presentation/               # PRESENTATION LAYER (läuft im Browser)
│   ├── index.html              #   Views: Rangliste, Spiel erfassen
│   ├── css/
│   │   └── style.css           #   Gestaltung
│   └── js/
│       └── app.js              #   View Logic: jQuery, AJAX-Aufrufe, DOM-Manipulation
│
├── service/                    # WEB/REST SERVICE LAYER (FastAPI)
│   ├── messages.py             #   Messages: Pydantic-Modelle für JSON-Anfragen und -Antworten
│   ├── spieler_endpoints.py    #   REST Endpoints: Rangliste, Abteilungen, Spieler anlegen
│   └── spiel_endpoints.py      #   REST Endpoints: Spiel erfassen, korrigieren, löschen
│
├── business/                   # BUSINESS SERVICE LAYER (Geschäftslogik)
│   ├── dtos.py                 #   Data Transfer Objects: SpielerDTO, SpielDTO
│   ├── spieler_service.py      #   Business Service: Spieler anlegen, Rangliste
│   ├── spiel_service.py        #   Business Service: Spiel erfassen, korrigieren, löschen
│   ├── elo.py                  #   Elo-Berechnung
│   └── fehler.py               #   GeschaeftsFehler bei verletzten Regeln
│
└── persistence/                # PERSISTENCE LAYER (SQLAlchemy)
    ├── database.py             #   Engine, Session, Tabellen anlegen
    ├── entities.py             #   Domain Entities: Spieler, Spiel
    └── data_access.py          #   Data Access: SpielerRepository, SpielRepository
```

---

## Architektur

Die Anwendung ist in vier Schichten aufgeteilt. Jede Schicht ruft nur die Schicht direkt darunter auf.

```
┌──────────────────────────────────────────────┐
│  Presentation Layer       (Browser)          │  HTML + CSS + jQuery
│  Views · View Logic                          │
└───────────────────────┬──────────────────────┘
                        │  HTTP + JSON (AJAX)
┌───────────────────────┴──────────────────────┐
│  Web/REST Service Layer   (FastAPI)          │
│  Messages · REST Endpoints                   │
├──────────────────────────────────────────────┤
│  Business Service Layer   (Geschäftslogik)   │
│  DTOs · Business Services                    │
├──────────────────────────────────────────────┤
│  Persistence Layer        (SQLAlchemy)       │
│  Domain Entities · Data Access               │
└───────────────────────┬──────────────────────┘
                        │  SQL
                 ┌──────┴──────┐
                 │   SQLite    │  kicker.db
                 └─────────────┘
```

### Was liegt in welcher Schicht?

| Schicht | Bestandteile | Aufgabe | Enthält keine … |
|---|---|---|---|
| **Presentation** | `index.html` (Views), `app.js` (View Logic) | Daten anzeigen, Eingaben entgegennehmen, Fehlermeldungen zeigen | Berechnungen, Regeln |
| **Web/REST Service** | `messages.py`, `*_endpoints.py` | JSON annehmen und prüfen (Datentypen), Business Service aufrufen, Antwort als JSON zurückgeben | Geschäftslogik |
| **Business Service** | `dtos.py`, `*_service.py`, `elo.py` | Alle Regeln: Validierung, Elo-Berechnung, Korrektur- und Löschregeln, Transaktionen | SQL-Abfragen, HTTP |
| **Persistence** | `entities.py`, `data_access.py` | Tabellen als Python-Klassen, Daten lesen und speichern | Geschäftsregeln |

### Ablauf einer Anfrage: «Spiel erfassen»

1. **Presentation:** `app.js` liest das Formular und schickt `POST /api/spiele` mit JSON per AJAX.
2. **Service:** `spiel_endpoints.spiel_erfassen()` erhält die Daten als Message `SpielErfassen`. FastAPI hat die Datentypen bereits geprüft.
3. **Business:** `SpielService.spiel_erfassen()` prüft die Regeln, berechnet mit `elo.py` die Punkte und erstellt eine `Spiel`-Entity.
4. **Persistence:** `SpielRepository` speichert Spiel und beide Spieler in **einer Transaktion**.
5. Der Business Service gibt ein `SpielDTO` zurück. Der Endpoint wandelt es in die Message `SpielAntwort` (JSON) um.
6. **Presentation:** `app.js` zeigt «Roy +16 (1216), Lisa −16 (1184)» an und lädt die Rangliste neu.

Die Komponenten werden über **Dependency Injection** (`Depends` von FastAPI) verbunden:
Endpoint → `SpielService` → `SpielRepository` / `SpielerRepository` → `Session`.
Beide Repositories erhalten pro Anfrage dieselbe Session.

---

## Datenmodell

Zwei Tabellen: `spieler` und `spiel`. Jedes Spiel verweist zweimal auf die Tabelle `spieler`, einmal für Spieler A und einmal für Spieler B.

```mermaid
erDiagram
    SPIELER ||--o{ SPIEL : "spielt als A"
    SPIELER ||--o{ SPIEL : "spielt als B"
    SPIELER {
        int id PK
        string name
        string abteilung
        int elo
        int anzahl_spiele
        datetime erstellt_am
    }
    SPIEL {
        int id PK
        datetime gespielt_am
        int spieler_a_id FK
        int spieler_b_id FK
        int tore_a
        int tore_b
        int elo_a_vorher
        int elo_b_vorher
        int elo_aenderung
    }
```

**Tabelle `spieler`**

| Spalte | Typ | Regeln |
|---|---|---|
| id | Integer | Primärschlüssel |
| name | String(100) | NOT NULL, eindeutig |
| abteilung | String(50) | NOT NULL, aus fester Liste |
| elo | Integer | NOT NULL, Start 1200 |
| anzahl_spiele | Integer | NOT NULL, Start 0 |
| erstellt_am | DateTime | automatisch |

**Tabelle `spiel`**

| Spalte | Typ | Regeln |
|---|---|---|
| id | Integer | Primärschlüssel |
| gespielt_am | DateTime | automatisch |
| spieler_a_id | Integer | Fremdschlüssel → spieler.id |
| spieler_b_id | Integer | Fremdschlüssel → spieler.id, ≠ spieler_a_id |
| tore_a, tore_b | Integer | 0–10, genau ein Spieler hat 10 |
| elo_a_vorher, elo_b_vorher | Integer | Elo der Spieler vor dem Spiel |
| elo_aenderung | Integer | Punkte, die der Gewinner erhält und der Verlierer abgibt |

---

## Business-Regeln

**Spiel erfassen**

1. Spieler A und Spieler B müssen verschieden sein und existieren.
2. Genau ein Spieler hat 10 Tore, der andere 0 bis 9.
3. Der Gewinner ergibt sich aus den Toren.
4. Spiel und beide Spieler werden in einer Transaktion gespeichert.

**Elo-Berechnung** (`business/elo.py`, K = 32)

```
Erwartung von A:     E_A = 1 / (1 + 10^((Elo_B − Elo_A) / 400))
Punkteänderung:      Δ   = round(32 × (1 − E_Gewinner))
```

| Situation | Sieg | Niederlage |
|---|---|---|
| 1200 gegen 1200 | +16 | −16 |
| 1200 gegen 1400 (Aussenseiter) | +24 | −8 |
| 1400 gegen 1200 (Favorit) | +8 | −24 |

**Korrigieren und Löschen**

1. Nur das **neuste** Spiel darf korrigiert oder gelöscht werden, weil alle späteren Spiele auf dessen Elo-Werten aufbauen.
2. **Korrigieren:** Nur das Resultat ist änderbar. Die Elo wird mit den gespeicherten Werten von vor dem Spiel neu berechnet.
3. **Löschen:** Beide Spieler erhalten ihre Elo von vor dem Spiel zurück, die Anzahl Spiele sinkt um 1.

Verletzte Regeln führen zu einem `GeschaeftsFehler`, den die App als **HTTP 400** mit `{"fehler": "…"}` zurückgibt.

---

## REST-API

| Methode | Endpunkt | Anfrage (JSON) | Antwort |
|---|---|---|---|
| GET | `/api/rangliste` | – | Liste von Spielern, nach Elo sortiert |
| GET | `/api/abteilungen` | – | Liste der erlaubten Abteilungen |
| POST | `/api/spieler` | `name`, `abteilung` | neuer Spieler (201) |
| POST | `/api/spiele` | `spieler_a_id`, `spieler_b_id`, `tore_a`, `tore_b` | erfasstes Spiel (201) |
| GET | `/api/spiele/letztes` | – | neustes Spiel oder `null` |
| PUT | `/api/spiele/{id}` | `tore_a`, `tore_b` | korrigiertes Spiel |
| DELETE | `/api/spiele/{id}` | – | leer (204) |

**Beispiel: Spiel erfassen**

```http
POST /api/spiele
Content-Type: application/json

{ "spieler_a_id": 1, "spieler_b_id": 2, "tore_a": 10, "tore_b": 7 }
```

```json
{
  "id": 1,
  "gespielt_am": "2026-11-01T16:49:20",
  "spieler_a": { "id": 1, "name": "Roy",  "abteilung": "Informatik", "elo": 1216, "anzahl_spiele": 1 },
  "spieler_b": { "id": 2, "name": "Lisa", "abteilung": "Marketing",  "elo": 1184, "anzahl_spiele": 1 },
  "tore_a": 10,
  "tore_b": 7,
  "gewinner": "Roy",
  "elo_aenderung": 16
}
```

---

## Testen

- **Swagger UI:** <http://localhost:8000/docs> zeigt alle Endpunkte. Jeder lässt sich dort direkt ausprobieren («Try it out»).
- **Postman:** Anfragen wie im Beispiel oben an `http://localhost:8000/api/...` senden.
- **Browser:** GET-Endpunkte wie <http://localhost:8000/api/rangliste> lassen sich direkt aufrufen.

---

## Designentscheidungen

- **Nur 2 Tabellen, bewusst nicht vollständig normalisiert**
  - **Abteilung als Text** statt eigener Tabelle. Tippfehler verhindert eine feste Liste im Business Layer, die im GUI als Dropdown erscheint.
  - **`elo` und `anzahl_spiele` beim Spieler** sind redundant, weil sie sich aus allen Spielen berechnen liessen. Sie werden gespeichert, damit die Rangliste mit einer einfachen Abfrage geladen werden kann.
  - **`elo_a_vorher`, `elo_b_vorher` und `elo_aenderung` im Spiel** machen das Korrigieren und Löschen ohne Neuberechnung aller Spiele möglich.
- **Der Gewinner wird nicht gespeichert.** Er ergibt sich aus den Toren, so können sich keine Daten widersprechen.
- **DTOs statt Entities nach oben:** Der Service Layer kennt keine SQLAlchemy-Objekte. Änderungen an der Datenbank wirken sich nicht direkt auf das API aus.
- **Repositories (Data Access):** Alle Abfragen liegen in der Persistenzschicht. Der Business Layer enthält kein SQL.
- **SQLite statt MySQL:** SQLite braucht keine Installation, das Projekt läuft also sofort. Durch SQLAlchemy ist ein Wechsel auf MySQL eine Änderung an `DATABASE_URL` in `persistence/database.py` (plus Treiber `pymysql`).
- **Grenze des Modells:** 2 vs 2 würde weitere Spalten oder eine dritte Tabelle (Spielteilnahme) erfordern.

---

## Mögliche Erweiterungen

- Spielverlauf aller Spiele
- Spieler bearbeiten und löschen
- Siegchance vor dem Spiel anzeigen («Lisa gewinnt mit 64 %»)
- Spielerprofil mit Elo-Verlaufsdiagramm
- Abteilungs-Rangliste (Durchschnitts-Elo pro Abteilung)
- Höherer K-Faktor für neue Spieler, Ränge (Bronze, Silber, Gold)

---

## Quellen und Hilfsmittel

_Nach den Vorgaben der FHNW für schriftliche Arbeiten ergänzen._

- Schaaf, M. (2026). *Webbasierte Anwendungen, Block 3 – Einheit 1: Architekturübersicht und erster Teil Präsentationsschicht.* FHNW.
- FastAPI-Dokumentation: <https://fastapi.tiangolo.com/>
- SQLAlchemy-Dokumentation: <https://docs.sqlalchemy.org/>
- jQuery-Dokumentation: <https://api.jquery.com/>
- Elo-Wertungssystem: <https://de.wikipedia.org/wiki/Elo-Zahl>
- KI-Hilfsmittel: _Einsatz von Claude (Anthropic) für Ideenfindung, Entwurf und Code-Grundgerüst – Umfang hier genau beschreiben_
