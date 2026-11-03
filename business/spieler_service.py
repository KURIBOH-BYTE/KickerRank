"""Business Service Layer – Spieler anlegen und Rangliste."""
from fastapi import Depends

from business.dtos import SpielerDTO
from business.elo import START_ELO
from business.fehler import GeschaeftsFehler
from persistence.data_access import SpielerRepository
from persistence.entities import Spieler

# Feste Auswahl, damit keine Tippfehler in der Abteilung entstehen.
ABTEILUNGEN = ["Informatik", "Marketing", "Finanzen", "HR", "Verkauf"]


class SpielerService:
    def __init__(self, spieler_repo: SpielerRepository = Depends()):
        self.spieler_repo = spieler_repo

    def abteilungen(self) -> list[str]:
        return ABTEILUNGEN

    def rangliste(self) -> list[SpielerDTO]:
        """Alle Spieler, beste Elo zuerst. Bei gleicher Elo nach Name."""
        return [SpielerDTO.aus_entity(s) for s in self.spieler_repo.alle_nach_elo()]

    def spieler_anlegen(self, name: str, abteilung: str) -> SpielerDTO:
        name = (name or "").strip()
        if not name:
            raise GeschaeftsFehler("Bitte einen Namen eingeben.")
        if len(name) > 100:
            raise GeschaeftsFehler("Der Name ist zu lang (max. 100 Zeichen).")
        if abteilung not in ABTEILUNGEN:
            raise GeschaeftsFehler(f"Unbekannte Abteilung. Erlaubt: {', '.join(ABTEILUNGEN)}.")
        if self.spieler_repo.finde_nach_name(name):
            raise GeschaeftsFehler(f"Es gibt bereits einen Spieler namens «{name}».")

        spieler = Spieler(name=name, abteilung=abteilung, elo=START_ELO, anzahl_spiele=0)
        self.spieler_repo.hinzufuegen(spieler)
        self.spieler_repo.speichern()
        return SpielerDTO.aus_entity(spieler)
