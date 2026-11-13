from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from persistence.database import Base


class Player(Base):
    __tablename__ = "player"
    __table_args__ = (UniqueConstraint("first_name", "last_name"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    department: Mapped[str] = mapped_column(String(50))
    elo: Mapped[int] = mapped_column(Integer, default=1200)
    games_played: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)


class Game(Base):
    __tablename__ = "game"

    id: Mapped[int] = mapped_column(primary_key=True)
    played_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    player_a_id: Mapped[int] = mapped_column(ForeignKey("player.id"))
    player_b_id: Mapped[int] = mapped_column(ForeignKey("player.id"))
    goals_a: Mapped[int] = mapped_column(Integer)
    goals_b: Mapped[int] = mapped_column(Integer)
    elo_a_before: Mapped[int] = mapped_column(Integer)
    elo_b_before: Mapped[int] = mapped_column(Integer)
    elo_change: Mapped[int] = mapped_column(Integer)

    player_a: Mapped[Player] = relationship(foreign_keys=[player_a_id])
    player_b: Mapped[Player] = relationship(foreign_keys=[player_b_id])

    @property
    def winner(self) -> Player:
        if self.goals_a > self.goals_b:
            return self.player_a
        return self.player_b
