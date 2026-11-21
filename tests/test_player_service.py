import pytest

from business.dtos import PlayerDTO
from business.errors import BusinessError
from business.player_service import PlayerService
from persistence.data_access import PlayerRepository


@pytest.fixture
def service(session):
    return PlayerService(PlayerRepository(session))


def test_spieler_anlegen(service):
    player = service.create_player("Anna", "Keller", "Development")

    assert player.id is not None
    assert player.elo == 1200
    assert player.games_played == 0


def test_leerzeichen_werden_entfernt(service):
    player = service.create_player("  Anna ", " Keller  ", "HR")

    assert (player.first_name, player.last_name) == ("Anna", "Keller")


def test_leerer_name_gibt_fehler(service):
    with pytest.raises(BusinessError, match="First name must not be empty"):
        service.create_player("   ", "Keller", "HR")


def test_zu_langer_name_gibt_fehler(service):
    with pytest.raises(BusinessError, match="too long"):
        service.create_player("Anna", "K" * 51, "HR")


def test_unbekannte_abteilung_gibt_fehler(service):
    with pytest.raises(BusinessError, match="Unknown department"):
        service.create_player("Anna", "Keller", "Kantine")


def test_doppelter_name_gibt_fehler(service):
    service.create_player("Anna", "Keller", "HR")

    with pytest.raises(BusinessError, match="already exists"):
        service.create_player("Anna", "Keller", "Marketing")


def test_rangliste_nach_elo(service):
    anna = service.create_player("Anna", "Keller", "HR")
    tim = service.create_player("Tim", "Brunner", "Support")
    service.players.find(anna.id).elo = 1250
    service.players.save()

    assert [player.id for player in service.ranking()] == [anna.id, tim.id]


def test_service_gibt_dtos_zurueck(service):
    player = service.create_player("Anna", "Keller", "HR")

    assert isinstance(player, PlayerDTO)
    assert all(isinstance(entry, PlayerDTO) for entry in service.ranking())


def test_aenderung_am_dto_aendert_datenbank_nicht(service):
    player = service.create_player("Anna", "Keller", "HR")

    player.elo = 9999
    service.players.save()

    assert service.ranking()[0].elo == 1200
