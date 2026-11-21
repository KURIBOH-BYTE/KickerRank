from fastapi import APIRouter, Depends

from business.game_service import GameService
from persistence.data_access import GameRepository, PlayerRepository
from persistence.database import get_session
from service.messages import GameCreate, GameResponse, ResultUpdate

router = APIRouter(prefix="/api/games")


def get_game_service(session=Depends(get_session)):
    return GameService(PlayerRepository(session), GameRepository(session))


@router.post("", status_code=201)
def create_game(message: GameCreate, service: GameService = Depends(get_game_service)) -> GameResponse:
    return service.create_game(message.player_a_id, message.player_b_id, message.goals_a, message.goals_b)


@router.get("/last")
def get_last_game(service: GameService = Depends(get_game_service)) -> GameResponse | None:
    return service.last_game()


@router.put("/{game_id}")
def update_game(game_id: int, message: ResultUpdate,
                service: GameService = Depends(get_game_service)) -> GameResponse:
    return service.update_game(game_id, message.goals_a, message.goals_b)


@router.delete("/{game_id}", status_code=204)
def delete_game(game_id: int, service: GameService = Depends(get_game_service)) -> None:
    service.delete_game(game_id)
