import pytest

from business.errors import BusinessError
from business.game_service import GameService
from persistence.data_access import GameRepository, PlayerRepository
from persistence.entities import Game, Player


@pytest.fixture
def players(session):
    repository = PlayerRepository(session)
    for first_name, last_name in [("Anna", "Keller"), ("Tim", "Brunner")]:
        repository.add(Player(first_name=first_name, last_name=last_name, department="HR"))
    repository.save()
    return repository


@pytest.fixture
def service(session, players):
    return GameService(players, GameRepository(session))


def anna_and_tim(players):
    return players.find_by_name("Anna", "Keller"), players.find_by_name("Tim", "Brunner")


def test_elo_wird_angepasst(service, players):
    anna, tim = anna_and_tim(players)

    service.create_game(anna.id, tim.id, 10, 7)

    assert (anna.elo, tim.elo) == (1216, 1184)


def test_sieg_von_spieler_b(service, players):
    anna, tim = anna_and_tim(players)

    service.create_game(anna.id, tim.id, 4, 10)

    assert (anna.elo, tim.elo) == (1184, 1216)


def test_anzahl_spiele_steigt(service, players):
    anna, tim = anna_and_tim(players)

    service.create_game(anna.id, tim.id, 10, 7)

    assert (anna.games_played, tim.games_played) == (1, 1)


def test_spiel_speichert_werte_vor_dem_spiel(service, players):
    anna, tim = anna_and_tim(players)

    game = service.create_game(anna.id, tim.id, 10, 7)

    assert game.id is not None
    assert (game.elo_a_before, game.elo_b_before, game.elo_change) == (1200, 1200, 16)
    assert game.winner is anna


def test_gegen_sich_selbst_gibt_fehler(service, players):
    anna, _ = anna_and_tim(players)

    with pytest.raises(BusinessError, match="against themselves"):
        service.create_game(anna.id, anna.id, 10, 7)


@pytest.mark.parametrize("player_a_id, player_b_id", [(0, 0), (0, 1), (1, 0)])
def test_kein_spieler_gewaehlt_gibt_fehler(service, player_a_id, player_b_id):
    with pytest.raises(BusinessError, match="Please choose two players"):
        service.create_game(player_a_id, player_b_id, 10, 7)


def test_unbekannter_spieler_gibt_fehler(service, players):
    anna, _ = anna_and_tim(players)

    with pytest.raises(BusinessError, match="does not exist"):
        service.create_game(anna.id, 999, 10, 7)


def test_kein_spieler_mit_10_toren_gibt_fehler(service, players):
    anna, tim = anna_and_tim(players)

    with pytest.raises(BusinessError, match="Exactly one player"):
        service.create_game(anna.id, tim.id, 9, 7)


def test_beide_mit_10_toren_gibt_fehler(service, players):
    anna, tim = anna_and_tim(players)

    with pytest.raises(BusinessError, match="Exactly one player"):
        service.create_game(anna.id, tim.id, 10, 10)


@pytest.mark.parametrize("goals", [-1, 11, 2.5])
def test_ungueltige_tore_geben_fehler(service, players, goals):
    anna, tim = anna_and_tim(players)

    with pytest.raises(BusinessError, match="whole numbers"):
        service.create_game(anna.id, tim.id, 10, goals)


def test_bei_fehler_wird_nichts_gespeichert(service, players, session):
    anna, tim = anna_and_tim(players)

    with pytest.raises(BusinessError):
        service.create_game(anna.id, tim.id, 10, 10)

    assert session.query(Game).count() == 0
    assert (anna.elo, anna.games_played) == (1200, 0)
