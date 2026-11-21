from fastapi import APIRouter, Depends

from business.game_service import GameService, winner
from persistence.data_access import GameRepository, PlayerRepository
from persistence.database import get_session
from service.messages import GameCreate, GameResponse, PlayerResponse, ResultUpdate

router = APIRouter(prefix="/api/games")


def get_game_service(session=Depends(get_session)):
    return GameService(PlayerRepository(session), GameRepository(session))


def to_game_response(game) -> GameResponse:
    return GameResponse(
        id=game.id,
        played_at=game.played_at,
        player_a_id=game.player_a_id,
        player_b_id=game.player_b_id,
        goals_a=game.goals_a,
        goals_b=game.goals_b,
        elo_a_before=game.elo_a_before,
        elo_b_before=game.elo_b_before,
        elo_change=game.elo_change,
        player_a=PlayerResponse.model_validate(game.player_a),
        player_b=PlayerResponse.model_validate(game.player_b),
        winner_id=winner(game).id,
    )


@router.post("", status_code=201)
def create_game(message: GameCreate, service: GameService = Depends(get_game_service)) -> GameResponse:
    game = service.create_game(message.player_a_id, message.player_b_id, message.goals_a, message.goals_b)
    return to_game_response(game)


@router.get("/last")
def get_last_game(service: GameService = Depends(get_game_service)) -> GameResponse | None:
    game = service.last_game()
    if game is None:
        return None
    return to_game_response(game)


@router.put("/{game_id}")
def update_game(game_id: int, message: ResultUpdate,
                service: GameService = Depends(get_game_service)) -> GameResponse:
    game = service.update_game(game_id, message.goals_a, message.goals_b)
    return to_game_response(game)


@router.delete("/{game_id}", status_code=204)
def delete_game(game_id: int, service: GameService = Depends(get_game_service)) -> None:
    service.delete_game(game_id)
