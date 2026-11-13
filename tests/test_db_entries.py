from business.elo import START_RATING, rating_change
from persistence.db_entries import DEMO_GAMES, DEMO_PLAYERS, insert_db_entries
from persistence.entities import Game, Player


def test_demo_daten_werden_angelegt(session):
    insert_db_entries(session)

    assert session.query(Player).count() == len(DEMO_PLAYERS) == 6
    assert session.query(Game).count() == len(DEMO_GAMES)


def test_demo_daten_nur_einmal(session):
    insert_db_entries(session)
    insert_db_entries(session)

    assert session.query(Player).count() == 6


def test_jeder_spieler_hat_gespielt(session):
    insert_db_entries(session)

    for player in session.query(Player).all():
        assert player.games_played > 0
        assert player.elo != START_RATING


def test_demo_daten_passen_zur_elo_berechnung():
    elo = {player[0]: START_RATING for player in DEMO_PLAYERS}
    games = {player[0]: 0 for player in DEMO_PLAYERS}

    for _, a, b, goals_a, goals_b, elo_a_before, elo_b_before, elo_change in DEMO_GAMES:
        assert (elo_a_before, elo_b_before) == (elo[a], elo[b])
        if goals_a > goals_b:
            assert elo_change == rating_change(elo[a], elo[b])
            elo[a], elo[b] = elo[a] + elo_change, elo[b] - elo_change
        else:
            assert elo_change == rating_change(elo[b], elo[a])
            elo[a], elo[b] = elo[a] - elo_change, elo[b] + elo_change
        games[a] += 1
        games[b] += 1

    for first_name, _, _, final_elo, games_played in DEMO_PLAYERS:
        assert elo[first_name] == final_elo
        assert games[first_name] == games_played
