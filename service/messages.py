"""Web/REST Service Layer – Messages.

Pydantic-Modelle, die festlegen, welches JSON ein Endpunkt erwartet (Anfrage)
und welches JSON er zurückgibt (Antwort). FastAPI prüft und konvertiert
diese automatisch.
"""
from datetime import datetime

from pydantic import BaseModel, ConfigDict

# ---------- Anfragen (Client -> Server) ----------


class SpielerErstellen(BaseModel):
    name: str
    abteilung: str


class SpielErfassen(BaseModel):
    spieler_a_id: int
    spieler_b_id: int
    tore_a: int
    tore_b: int


class ResultatKorrigieren(BaseModel):
    tore_a: int
    tore_b: int


# ---------- Antworten (Server -> Client) ----------


class SpielerAntwort(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # direkt aus einem DTO erzeugbar

    id: int
    name: str
    abteilung: str
    elo: int
    anzahl_spiele: int


class SpielAntwort(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    gespielt_am: datetime
    spieler_a: SpielerAntwort
    spieler_b: SpielerAntwort
    tore_a: int
    tore_b: int
    gewinner: str
    elo_aenderung: int


class FehlerAntwort(BaseModel):
    fehler: str
