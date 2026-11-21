from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PlayerCreate(BaseModel):
    first_name: str
    last_name: str
    department: str


class PlayerUpdate(BaseModel):
    first_name: str
    last_name: str
    department: str
    active: bool


class GameCreate(BaseModel):
    player_a_id: int
    player_b_id: int
    goals_a: int
    goals_b: int


class ResultUpdate(BaseModel):
    goals_a: int
    goals_b: int


class PlayerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    department: str
    elo: int
    games_played: int
    created_at: datetime
    active: bool


class GameResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    played_at: datetime
    player_a_id: int
    player_b_id: int
    goals_a: int
    goals_b: int
    elo_a_before: int
    elo_b_before: int
    elo_change: int
    player_a: PlayerResponse
    player_b: PlayerResponse
    winner_id: int


class ErrorResponse(BaseModel):
    error: str
