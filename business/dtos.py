from dataclasses import dataclass
from datetime import datetime


@dataclass
class PlayerDTO:
    id: int
    first_name: str
    last_name: str
    department: str
    elo: int
    games_played: int
    created_at: datetime


@dataclass
class GameDTO:
    id: int
    played_at: datetime
    player_a_id: int
    player_b_id: int
    player_a: PlayerDTO
    player_b: PlayerDTO
    goals_a: int
    goals_b: int
    elo_a_before: int
    elo_b_before: int
    elo_change: int
    winner_id: int


def to_player_dto(player):
    return PlayerDTO(
        id=player.id,
        first_name=player.first_name,
        last_name=player.last_name,
        department=player.department,
        elo=player.elo,
        games_played=player.games_played,
        created_at=player.created_at,
    )
