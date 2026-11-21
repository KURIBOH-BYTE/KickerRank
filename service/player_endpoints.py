from fastapi import APIRouter, Depends

from business.departments import DEPARTMENTS
from business.player_service import PlayerService
from persistence.data_access import PlayerRepository
from persistence.database import get_session
from service.messages import PlayerCreate, PlayerResponse, PlayerUpdate

router = APIRouter(prefix="/api")


def get_player_service(session=Depends(get_session)):
    return PlayerService(PlayerRepository(session))


@router.get("/ranking")
def get_ranking(service: PlayerService = Depends(get_player_service)) -> list[PlayerResponse]:
    return service.ranking()


@router.get("/departments")
def get_departments() -> list[str]:
    return DEPARTMENTS


@router.post("/players", status_code=201)
def create_player(message: PlayerCreate, service: PlayerService = Depends(get_player_service)) -> PlayerResponse:
    return service.create_player(message.first_name, message.last_name, message.department)


@router.get("/players")
def get_players(service: PlayerService = Depends(get_player_service)) -> list[PlayerResponse]:
    return service.all_players()


@router.put("/players/{player_id}")
def update_player(player_id: int, message: PlayerUpdate,
                  service: PlayerService = Depends(get_player_service)) -> PlayerResponse:
    return service.update_player(player_id, message.first_name, message.last_name,
                                 message.department, message.active)
