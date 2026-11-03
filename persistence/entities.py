"""Persistence Layer – Domain Entities: die SQLAlchemy-Modelle Spieler und Spiel."""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from persistence.database import Base


class Spieler(Base):
    __tablename__ = "spieler"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    # Bewusst nicht normalisiert: Abteilung als Text statt eigene Tabelle.
    abteilung: Mapped[str] = mapped_column(String(50), nullable=False)
    # Bewusst redundant (liesse sich aus allen Spielen berechnen), damit die
    # Rangliste schnell geladen werden kann.
    elo: Mapped[int] = mapped_column(Integer, nullable=False, default=1200)
    anzahl_spiele: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    erstellt_am: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    # Ein Spieler kommt in Spielen entweder als A oder als B vor.
    spiele_als_a: Mapped[list["Spiel"]] = relationship(
        back_populates="spieler_a", foreign_keys="Spiel.spieler_a_id"
    )
    spiele_als_b: Mapped[list["Spiel"]] = relationship(
        back_populates="spieler_b", foreign_keys="Spiel.spieler_b_id"
    )


class Spiel(Base):
    __tablename__ = "spiel"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    gespielt_am: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)

    spieler_a_id: Mapped[int] = mapped_column(ForeignKey("spieler.id"), nullable=False)
    spieler_b_id: Mapped[int] = mapped_column(ForeignKey("spieler.id"), nullable=False)
    tore_a: Mapped[int] = mapped_column(Integer, nullable=False)
    tore_b: Mapped[int] = mapped_column(Integer, nullable=False)

    # Elo vor dem Spiel und die Änderung: nötig zum Korrigieren/Löschen.
    elo_a_vorher: Mapped[int] = mapped_column(Integer, nullable=False)
    elo_b_vorher: Mapped[int] = mapped_column(Integer, nullable=False)
    elo_aenderung: Mapped[int] = mapped_column(Integer, nullable=False)

    spieler_a: Mapped[Spieler] = relationship(back_populates="spiele_als_a", foreign_keys=[spieler_a_id])
    spieler_b: Mapped[Spieler] = relationship(back_populates="spiele_als_b", foreign_keys=[spieler_b_id])

    @property
    def gewinner(self) -> Spieler:
        """Der Gewinner wird nicht gespeichert, sondern aus den Toren abgeleitet."""
        return self.spieler_a if self.tore_a > self.tore_b else self.spieler_b
