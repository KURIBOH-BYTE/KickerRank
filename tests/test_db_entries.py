from business.db_entries import DEMO_GAMES, DEMO_PLAYERS, insert_db_entries
from business.elo import START_RATING
from business.player_service import PlayerService
from persistence.data_access import PlayerRepository
from persistence.entities import Game, Player


def test_demo_daten_werden_angelegt(session):
    insert_db_entries(session)

    assert session.query(Player).count() == len(DEMO_PLAYERS) == 6
    assert session.query(Game).count() == len(DEMO_GAMES) == 12


def test_demo_daten_nur_einmal(session):
    insert_db_entries(session)
    insert_db_entries(session)

    assert session.query(Player).count() == 6
    assert session.query(Game).count() == 12


def test_jeder_spieler_hat_gespielt(session):
    insert_db_entries(session)

    for player in session.query(Player).all():
        assert player.games_played > 0
        assert player.elo != START_RATING


def test_elo_wird_vom_game_service_berechnet(session):
    insert_db_entries(session)

    ranking = session.query(Player).order_by(Player.elo.desc()).all()

    assert [(player.first_name, player.elo, player.games_played) for player in ranking] == [
        ("Lukas", 1260, 4),
        ("Sarah", 1230, 4),
        ("Elena", 1199, 4),
        ("Giovanni", 1185, 3),
        ("Tim", 1173, 4),
        ("Anna", 1153, 5),
    ]


def test_spiele_behalten_ihr_datum(session):
    insert_db_entries(session)

    last = session.query(Game).order_by(Game.id.desc()).first()

    assert last.played_at.strftime("%d.%m.%Y %H:%M") == "13.11.2026 12:05"


def test_keine_demo_daten_wenn_alle_spieler_geloescht(session):
    insert_db_entries(session)
    service = PlayerService(PlayerRepository(session))
    for player in service.ranking():
        service.delete_player(player.id)

    insert_db_entries(session)

    assert session.query(Player).count() == 6
