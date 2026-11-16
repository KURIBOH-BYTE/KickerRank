from business.elo import rating_change
from business.errors import BusinessError
from persistence.entities import Game

WINNING_GOALS = 10


class GameService:
    def __init__(self, players, games):
        self.players = players
        self.games = games

    def create_game(self, player_a_id, player_b_id, goals_a, goals_b):
        player_a, player_b = self._get_players(player_a_id, player_b_id)
        check_result(goals_a, goals_b)

        game = Game(
            player_a=player_a,
            player_b=player_b,
            goals_a=goals_a,
            goals_b=goals_b,
            elo_a_before=player_a.elo,
            elo_b_before=player_b.elo,
        )

        adjust_elo(game)

        player_a.games_played += 1
        player_b.games_played += 1

        self.games.add(game)
        self.games.save()
        return game

    def update_game(self, game_id, goals_a, goals_b):
        game = self._get_latest_game(game_id)
        check_result(goals_a, goals_b)

        game.goals_a = goals_a
        game.goals_b = goals_b

        game.player_a.elo = game.elo_a_before
        game.player_b.elo = game.elo_b_before
        
        adjust_elo(game)

        self.games.save()
        return game

    def delete_game(self, game_id):
        game = self._get_latest_game(game_id)

        game.player_a.elo = game.elo_a_before
        game.player_b.elo = game.elo_b_before

        game.player_a.games_played -= 1
        game.player_b.games_played -= 1

        self.games.delete(game)
        self.games.save()

    def _get_latest_game(self, game_id):
        game = self.games.find(game_id)
        if game is None:
            raise BusinessError("This game does not exist.")
        if game is not self.games.last():
            raise BusinessError("Only the latest game can be edited or deleted.")
        return game

    def _get_players(self, player_a_id, player_b_id):
        if not player_a_id or not player_b_id:
            raise BusinessError("Please choose two players.")

        if player_a_id == player_b_id:
            raise BusinessError("A player cannot play against themselves.")

        player_a = self.players.find(player_a_id)
        player_b = self.players.find(player_b_id)
        if player_a is None or player_b is None:
            raise BusinessError("At least one player does not exist.")

        return player_a, player_b


def check_result(goals_a, goals_b):
    for goals in (goals_a, goals_b):
        if not isinstance(goals, int) or not 0 <= goals <= WINNING_GOALS:
            raise BusinessError(f"Goals must be whole numbers from 0 to {WINNING_GOALS}.")

    if (goals_a == WINNING_GOALS) == (goals_b == WINNING_GOALS):
        raise BusinessError(f"Exactly one player must have {WINNING_GOALS} goals.")


def adjust_elo(game):
    change = rating_change(game.winner.elo, game.loser.elo)
    game.elo_change = change
    game.winner.elo += change
    game.loser.elo -= change
