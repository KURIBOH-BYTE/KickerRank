# Backlog KickerRank

39 Tickets in 7 Meilensteinen, geschätzt 84.5 Stunden für die ganze Gruppe.
Die Reihenfolge folgt der Vorlesung: zuerst Präsentation (Übung 1), dann Service, Business und Persistenz.
Nach M2 läuft die App mit Daten im Speicher, nach M4 mit Datenbank. Damit ist die Mindestanforderung erfüllt. M5 bringt die volle Punktzahl.

Jedes Ticket hat Ziel, Aufgaben, Akzeptanzkriterien, Tests und eine Definition of Done. Details: Ordner `tickets/`.

## M0 · Setup und Planung

Summe: 9.5 h

| Ticket | Titel | Typ | h | Abhängig von |
|---|---|---|---|---|
| T01 | [Referenzcode sichern und Projekt-Skelett aufsetzen](tickets/T01-referenzcode-sichern-und-projekt-skelett.md) | Setup | 2 | – |
| T02 | [Entwicklungsumgebung für alle Gruppenmitglieder](tickets/T02-entwicklungsumgebung-fuer-alle-gruppenmi.md) | Setup | 1 | T01 |
| T03 | [Test-Setup mit pytest einrichten](tickets/T03-test-setup-mit-pytest-einrichten.md) | Setup, Test | 1.5 | T01 |
| T04 | [Service-Beschreibung im Schema der Übung 1 erstellen](tickets/T04-service-beschreibung-im-schema-der-uebun.md) | Doku, Service | 2 | – |
| T05 | [Datenmodell und ER-Diagramm dokumentieren](tickets/T05-datenmodell-und-er-diagramm-dokumentiere.md) | Doku, Persistence | 2 | – |
| T06 | [Arbeitsweise mit Git und Tickets festlegen](tickets/T06-arbeitsweise-mit-git-und-tickets-festleg.md) | Setup | 1 | T02 |

## M1 · Presentation Layer

Summe: 8 h

| Ticket | Titel | Typ | h | Abhängig von |
|---|---|---|---|---|
| T07 | [Grundlayout mit Kopfzeile und zwei Bereichen](tickets/T07-grundlayout-mit-kopfzeile-und-zwei-berei.md) | Presentation | 2 | T01 |
| T08 | [Rangliste aus JSON-Testdaten anzeigen](tickets/T08-rangliste-aus-json-testdaten-anzeigen.md) | Presentation | 2 | T07 |
| T09 | [Formular «Spiel erfassen» mit Eingabeprüfung im Browser](tickets/T09-formular-spiel-erfassen-mit-eingabepruef.md) | Presentation | 2.5 | T08 |
| T10 | [Bereich «Spieler hinzufügen» und Box «Letztes Spiel»](tickets/T10-bereich-spieler-hinzufuegen-und-box-letz.md) | Presentation | 1.5 | T07 |

## M2 · Web/REST Service Layer

Summe: 15 h

| Ticket | Titel | Typ | h | Abhängig von |
|---|---|---|---|---|
| T11 | [Messages (Pydantic-Modelle) für Spieler und Spiel](tickets/T11-messages-pydantic-modelle-fuer-spieler-u.md) | Service | 2 | T04 |
| T12 | [Endpunkte Rangliste und Abteilungen (Daten im Speicher)](tickets/T12-endpunkte-rangliste-und-abteilungen-date.md) | Service | 2 | T11, T03 |
| T13 | [Endpunkt Spieler anlegen](tickets/T13-endpunkt-spieler-anlegen.md) | Service | 1.5 | T12 |
| T14 | [Endpunkte Spiel erfassen und letztes Spiel](tickets/T14-endpunkte-spiel-erfassen-und-letztes-spi.md) | Service | 2.5 | T13 |
| T15 | [Endpunkte Spiel korrigieren und löschen](tickets/T15-endpunkte-spiel-korrigieren-und-loeschen.md) | Service | 2 | T14 |
| T16 | [Frontend an die echte API anbinden: Rangliste und Spieler](tickets/T16-frontend-an-die-echte-api-anbinden-rangl.md) | Presentation, Service | 2 | T08, T10, T13 |
| T17 | [Frontend an die echte API anbinden: Spiele](tickets/T17-frontend-an-die-echte-api-anbinden-spiel.md) | Presentation, Service | 3 | T09, T15, T16 |

## M3 · Business Service Layer

Summe: 13.5 h

| Ticket | Titel | Typ | h | Abhängig von |
|---|---|---|---|---|
| T18 | [Elo-Berechnung](tickets/T18-elo-berechnung.md) | Business, Test | 2 | T03 |
| T19 | [Fehlerklasse und einheitliche Fehlerantwort](tickets/T19-fehlerklasse-und-einheitliche-fehlerantw.md) | Business, Service | 1.5 | T12 |
| T20 | [SpielerService mit Prüfregeln](tickets/T20-spielerservice-mit-pruefregeln.md) | Business, Test | 2.5 | T19 |
| T21 | [SpielService: Spiel erfassen mit Regeln und Elo](tickets/T21-spielservice-spiel-erfassen-mit-regeln-u.md) | Business, Test | 3 | T18, T20 |
| T22 | [SpielService: Korrigieren und Löschen nur beim neusten Spiel](tickets/T22-spielservice-korrigieren-und-loeschen-nu.md) | Business, Test | 2.5 | T21 |
| T23 | [DTOs zwischen Business und Service Layer](tickets/T23-dtos-zwischen-business-und-service-layer.md) | Business, Service | 2 | T22 |

## M4 · Persistence Layer

Summe: 11.5 h

| Ticket | Titel | Typ | h | Abhängig von |
|---|---|---|---|---|
| T24 | [Datenbankverbindung mit SQLAlchemy](tickets/T24-datenbankverbindung-mit-sqlalchemy.md) | Persistence, Test | 2 | T05, T03 |
| T25 | [Entitäten Spieler und Spiel](tickets/T25-entitaeten-spieler-und-spiel.md) | Persistence, Test | 3 | T24 |
| T26 | [Data Access: Repositories für Spieler und Spiele](tickets/T26-data-access-repositories-fuer-spieler-un.md) | Persistence, Test | 2.5 | T25 |
| T27 | [Business Layer auf die Datenbank umstellen](tickets/T27-business-layer-auf-die-datenbank-umstell.md) | Business, Persistence, Test | 3 | T23, T26 |
| T28 | [Demo-Daten beim ersten Start](tickets/T28-demo-daten-beim-ersten-start.md) | Persistence | 1 | T27 |

## M5 · Erweiterungen (volle Punktzahl)

Summe: 12.5 h

| Ticket | Titel | Typ | h | Abhängig von |
|---|---|---|---|---|
| T29 | [Erweiterung: Spielverlauf](tickets/T29-erweiterung-spielverlauf.md) | Erweiterung | 3 | T27 |
| T30 | [Erweiterung: Siegchance vor dem Spiel](tickets/T30-erweiterung-siegchance-vor-dem-spiel.md) | Erweiterung | 2.5 | T27 |
| T31 | [Erweiterung: Spieler bearbeiten und löschen](tickets/T31-erweiterung-spieler-bearbeiten-und-loesc.md) | Erweiterung | 3 | T27 |
| T32 | [Erweiterung (optional): Spielerprofil mit Elo-Verlauf](tickets/T32-erweiterung-optional-spielerprofil-mit-e.md) | Erweiterung | 4 | T29 |

## M6 · Abgabe und Verteidigung

Summe: 14.5 h

| Ticket | Titel | Typ | h | Abhängig von |
|---|---|---|---|---|
| T33 | [README fertigstellen](tickets/T33-readme-fertigstellen.md) | Doku | 1.5 | T27 |
| T34 | [Beschreibung für die Abgabe](tickets/T34-beschreibung-fuer-die-abgabe.md) | Doku | 3 | T05, T27 |
| T35 | [Reflexion schreiben](tickets/T35-reflexion-schreiben.md) | Doku | 1.5 | T34 |
| T36 | [Quellen- und Hilfsmittelverzeichnis](tickets/T36-quellen-und-hilfsmittelverzeichnis.md) | Doku | 1.5 | – |
| T37 | [Abgabetest auf einem fremden Rechner](tickets/T37-abgabetest-auf-einem-fremden-rechner.md) | Test | 1 | T33 |
| T38 | [Präsentation vorbereiten](tickets/T38-praesentation-vorbereiten.md) | Verteidigung | 3 | T27 |
| T39 | [Verteidigung üben: jedes Mitglied erklärt jede Schicht](tickets/T39-verteidigung-ueben-jedes-mitglied-erklae.md) | Verteidigung | 3 | T27 |

## Tickets parallel bearbeiten

- M0: T04 und T05 sind unabhängig vom Code und können sofort starten.
- M1 und T18 (Elo) können parallel laufen, T18 braucht nur das Test-Setup.
- M5: T29, T30 und T31 sind unabhängig voneinander. Gut für «jede Person baut eine Funktion durch alle Schichten».
- T36 (Quellen) läuft die ganze Zeit mit.

## Als GitHub-Issues anlegen

```bash
cd planung
python3 github_issues_erstellen.py --dry-run   # nur anzeigen
python3 github_issues_erstellen.py             # wirklich anlegen
```
Voraussetzung: GitHub CLI installiert und angemeldet (`gh auth login`).
