from datetime import datetime
from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from service.messages import (
    ErrorResponse,
    GameCreate,
    GameResponse,
    PlayerCreate,
    PlayerResponse,
    ResultUpdate,
)


def test_request_messages_accept_valid_payloads():
    assert PlayerCreate.model_validate(
        {"first_name": "Max", "last_name": "Muster", "department": "IT"}
    )
    assert GameCreate.model_validate(
        {"player_a_id": 1, "player_b_id": 2, "goals_a": 10, "goals_b": 7}
    )
    assert ResultUpdate.model_validate({"goals_a": 10, "goals_b": 7})


def test_responses_accept_valid_payloads_and_attributes():
    created_at = datetime(2026, 1, 1)
    player_a = SimpleNamespace(
        id=1,
        first_name="Max",
        last_name="Muster",
        department="IT",
        elo=1200,
        games_played=1,
        created_at=created_at,
    )
    player_b = SimpleNamespace(
        id=2,
        first_name="Lisa",
        last_name="Beispiel",
        department="HR",
        elo=1184,
        games_played=1,
        created_at=created_at,
    )
    game = SimpleNamespace(
        id=1,
        played_at=created_at,
        player_a_id=1,
        player_b_id=2,
        goals_a=10,
        goals_b=7,
        elo_a_before=1200,
        elo_b_before=1200,
        elo_change=16,
        player_a=player_a,
        player_b=player_b,
        winner_id=1,
    )

    player_response = PlayerResponse.model_validate(player_a)
    game_response = GameResponse.model_validate(game)

    assert player_response.id == 1
    assert game_response.player_a.first_name == "Max"
    assert game_response.player_b.first_name == "Lisa"
    assert game_response.winner_id == 1
    assert ErrorResponse.model_validate({"error": "Invalid request"}).error


def test_game_create_rejects_non_integer_goals():
    with pytest.raises(ValidationError):
        GameCreate.model_validate(
            {"player_a_id": 1, "player_b_id": 2, "goals_a": "zehn", "goals_b": 7}
        )


def test_result_update_rejects_non_integer_goals():
    with pytest.raises(ValidationError):
        ResultUpdate.model_validate({"goals_a": "zehn", "goals_b": 7})
