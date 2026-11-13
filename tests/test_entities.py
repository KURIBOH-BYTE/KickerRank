import pytest
from sqlalchemy.exc import IntegrityError

from persistence.entities import Game, Player


def create_player(session, first_name, last_name="Muster", department="IT"):
    player = Player(first_name=first_name, last_name=last_name, department=department)
    session.add(player)
    session.commit()
    return player


def test_spieler_speichern_und_lesen(session):
    create_player(session, "Max", "Muster", "IT")

    player = session.query(Player).filter_by(first_name="Max").one()

    assert player.last_name == "Muster"
    assert player.department == "IT"
    assert player.elo == 1200
    assert player.games_played == 0
    assert player.created_at is not None


def test_spiel_mit_zwei_spielern(session):
    max_ = create_player(session, "Max")
    lisa = create_player(session, "Lisa")
    game = Game(player_a=max_, player_b=lisa, goals_a=10, goals_b=7,
                elo_a_before=1200, elo_b_before=1200, elo_change=16)
    session.add(game)
    session.commit()

    saved = session.query(Game).one()

    assert saved.player_a.first_name == "Max"
    assert saved.player_b.first_name == "Lisa"
    assert saved.played_at is not None


def test_gewinner_property(session):
    max_ = create_player(session, "Max")
    lisa = create_player(session, "Lisa")

    a_wins = Game(player_a=max_, player_b=lisa, goals_a=10, goals_b=7)
    b_wins = Game(player_a=max_, player_b=lisa, goals_a=4, goals_b=10)

    assert a_wins.winner is max_
    assert b_wins.winner is lisa


def test_name_ist_eindeutig(session):
    create_player(session, "Max", "Muster")

    with pytest.raises(IntegrityError):
        create_player(session, "Max", "Muster")


def test_gleicher_vorname_ist_erlaubt(session):
    create_player(session, "Max", "Muster")
    create_player(session, "Max", "Meier")

    assert session.query(Player).count() == 2
