from persistence.data_access import GameRepository, PlayerRepository
from persistence.entities import Game, Player


def add_player(repository, first_name, last_name, elo=1200):
    player = repository.add(Player(first_name=first_name, last_name=last_name,
                                   department="Development", elo=elo))
    repository.save()
    return player


def add_game(repository, player_a, player_b, goals_a=10, goals_b=7):
    game = repository.add(Game(player_a=player_a, player_b=player_b, goals_a=goals_a, goals_b=goals_b,
                               elo_a_before=player_a.elo, elo_b_before=player_b.elo, elo_change=16))
    repository.save()
    return game


def test_alle_nach_elo_sortiert(session):
    players = PlayerRepository(session)
    add_player(players, "Tim", "Brunner", elo=1180)
    add_player(players, "Lukas", "Müller", elo=1260)
    add_player(players, "Sarah", "Meier", elo=1230)

    ranking = players.all_by_elo()

    assert [player.first_name for player in ranking] == ["Lukas", "Sarah", "Tim"]


def test_gleiche_elo_nach_nachname_sortiert(session):
    players = PlayerRepository(session)
    add_player(players, "Tim", "Brunner")
    add_player(players, "Anna", "Keller")
    add_player(players, "Elena", "Bauer")

    ranking = players.all_by_elo()

    assert [player.last_name for player in ranking] == ["Bauer", "Brunner", "Keller"]


def test_finde_spieler(session):
    players = PlayerRepository(session)
    anna = add_player(players, "Anna", "Keller")

    assert players.find(anna.id) is anna
    assert players.find(999) is None


def test_finde_nach_name(session):
    players = PlayerRepository(session)
    add_player(players, "Anna", "Keller")

    assert players.find_by_name("Anna", "Keller").first_name == "Anna"
    assert players.find_by_name("Anna", "Meier") is None


def test_hinzufuegen_vergibt_id(session):
    players = PlayerRepository(session)

    anna = players.add(Player(first_name="Anna", last_name="Keller", department="HR"))

    assert anna.id is not None


def test_speichern_aendert_spieler(session):
    players = PlayerRepository(session)
    anna = add_player(players, "Anna", "Keller")

    anna.elo = 1250
    players.save()
    session.expire_all()

    assert players.find(anna.id).elo == 1250


def test_letztes_spiel(session):
    players = PlayerRepository(session)
    games = GameRepository(session)
    anna = add_player(players, "Anna", "Keller")
    tim = add_player(players, "Tim", "Brunner")
    add_game(games, anna, tim)
    newest = add_game(games, tim, anna)

    assert games.last() is newest


def test_letztes_spiel_ohne_spiele(session):
    assert GameRepository(session).last() is None


def test_finde_spiel(session):
    players = PlayerRepository(session)
    games = GameRepository(session)
    game = add_game(games, add_player(players, "Anna", "Keller"), add_player(players, "Tim", "Brunner"))

    assert games.find(game.id) is game
    assert games.find(999) is None


def test_loeschen(session):
    players = PlayerRepository(session)
    games = GameRepository(session)
    game = add_game(games, add_player(players, "Anna", "Keller"), add_player(players, "Tim", "Brunner"))

    games.delete(game)
    games.save()

    assert games.last() is None
    assert len(players.all_by_elo()) == 2
