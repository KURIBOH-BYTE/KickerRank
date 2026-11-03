"""Persistence Layer – Data Access: alle Datenbankabfragen an einem Ort.

Der Business Layer schreibt selbst kein SQL und keine Abfragen, sondern nutzt
nur diese Repositories.
"""
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from persistence.database import get_session
from persistence.entities import Spiel, Spieler


class SpielerRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def alle_nach_elo(self) -> list[Spieler]:
        return list(self.session.scalars(select(Spieler).order_by(Spieler.elo.desc(), Spieler.name)))

    def finde(self, spieler_id: int) -> Spieler | None:
        return self.session.get(Spieler, spieler_id)

    def finde_nach_name(self, name: str) -> Spieler | None:
        return self.session.scalar(select(Spieler).where(Spieler.name == name))

    def hinzufuegen(self, spieler: Spieler) -> None:
        self.session.add(spieler)

    def speichern(self) -> None:
        self.session.commit()


class SpielRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def finde(self, spiel_id: int) -> Spiel | None:
        return self.session.get(Spiel, spiel_id)

    def letztes(self) -> Spiel | None:
        return self.session.scalar(select(Spiel).order_by(Spiel.id.desc()).limit(1))

    def hinzufuegen(self, spiel: Spiel) -> None:
        self.session.add(spiel)

    def loeschen(self, spiel: Spiel) -> None:
        self.session.delete(spiel)

    def speichern(self) -> None:
        """Speichert alle Änderungen der Anfrage in einer Transaktion."""
        self.session.commit()
