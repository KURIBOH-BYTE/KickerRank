import pytest

from business.dtos import PlayerDTO
from business.errors import BusinessError, NotFoundError
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


def test_spieler_umbenennen(service):
    anna = service.create_player("Anna", "Keller", "HR")

    updated = service.update_player(anna.id, "Anna", "Meier", "Marketing", True)

    assert (updated.last_name, updated.department) == ("Meier", "Marketing")
    assert service.ranking()[0].last_name == "Meier"


def test_umbenennen_behaelt_elo_und_spiele(service):
    anna = service.create_player("Anna", "Keller", "HR")
    service.players.find(anna.id).elo = 1250
    service.players.save()

    updated = service.update_player(anna.id, "Anna", "Meier", "HR", True)

    assert (updated.elo, updated.games_played) == (1250, 0)


def test_umbenennen_auf_eigenen_namen_ist_erlaubt(service):
    anna = service.create_player("Anna", "Keller", "HR")

    updated = service.update_player(anna.id, "Anna", "Keller", "Support", True)

    assert updated.department == "Support"


def test_umbenennen_auf_vorhandenen_namen_gibt_fehler(service):
    anna = service.create_player("Anna", "Keller", "HR")
    service.create_player("Tim", "Brunner", "HR")

    with pytest.raises(BusinessError, match="already exists"):
        service.update_player(anna.id, "Tim", "Brunner", "HR", True)


def test_bearbeiten_prueft_regeln(service):
    anna = service.create_player("Anna", "Keller", "HR")

    with pytest.raises(BusinessError, match="must not be empty"):
        service.update_player(anna.id, "  ", "Keller", "HR", True)
    with pytest.raises(BusinessError, match="Unknown department"):
        service.update_player(anna.id, "Anna", "Keller", "Kantine", True)


def test_unbekannter_spieler_gibt_fehler(service):
    with pytest.raises(NotFoundError):
        service.update_player(999, "Anna", "Keller", "HR", True)


def test_inaktiver_spieler_fehlt_in_rangliste(service):
    anna = service.create_player("Anna", "Keller", "HR")
    service.create_player("Tim", "Brunner", "HR")

    service.update_player(anna.id, "Anna", "Keller", "HR", False)

    assert [player.first_name for player in service.ranking()] == ["Tim"]


def test_inaktiver_spieler_ist_in_allen_spielern(service):
    anna = service.create_player("Anna", "Keller", "HR")
    service.update_player(anna.id, "Anna", "Keller", "HR", False)

    players = service.all_players()

    assert [(player.first_name, player.active) for player in players] == [("Anna", False)]


def test_spieler_wieder_aktivieren(service):
    anna = service.create_player("Anna", "Keller", "HR")
    service.update_player(anna.id, "Anna", "Keller", "HR", False)

    service.update_player(anna.id, "Anna", "Keller", "HR", True)

    assert [player.first_name for player in service.ranking()] == ["Anna"]


def test_name_eines_inaktiven_spielers_gibt_fehler(service):
    anna = service.create_player("Anna", "Keller", "HR")
    service.update_player(anna.id, "Anna", "Keller", "HR", False)

    with pytest.raises(BusinessError, match="inactive player"):
        service.create_player("Anna", "Keller", "HR")
