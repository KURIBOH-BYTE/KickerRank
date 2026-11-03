"""Business Service Layer – Data Transfer Objects (DTOs).

Die Business Services geben DTOs statt Datenbank-Entities zurück. So hängt der
Service Layer nicht direkt von SQLAlchemy ab.
"""
from dataclasses import dataclass
from datetime import datetime

from persistence.entities import Spiel, Spieler


@dataclass
class SpielerDTO:
    id: int
    name: str
    abteilung: str
    elo: int
    anzahl_spiele: int

    @staticmethod
    def aus_entity(s: Spieler) -> "SpielerDTO":
        return SpielerDTO(s.id, s.name, s.abteilung, s.elo, s.anzahl_spiele)


@dataclass
class SpielDTO:
    id: int
    gespielt_am: datetime
    spieler_a: SpielerDTO
    spieler_b: SpielerDTO
    tore_a: int
    tore_b: int
    gewinner: str
    elo_aenderung: int

    @staticmethod
    def aus_entity(sp: Spiel) -> "SpielDTO":
        return SpielDTO(
            id=sp.id,
            gespielt_am=sp.gespielt_am,
            spieler_a=SpielerDTO.aus_entity(sp.spieler_a),
            spieler_b=SpielerDTO.aus_entity(sp.spieler_b),
            tore_a=sp.tore_a,
            tore_b=sp.tore_b,
            gewinner=sp.gewinner.name,
            elo_aenderung=sp.elo_aenderung,
        )
