from sqlalchemy import func, select

from persistence.entities import Game, Player


class PlayerRepository:
    def __init__(self, session):
        self.session = session

    def all_by_elo(self):
        query = (select(Player)
                 .where(Player.active)
                 .order_by(Player.elo.desc(), Player.last_name, Player.first_name))
        return list(self.session.scalars(query))

    def count(self):
        return self.session.scalar(select(func.count()).select_from(Player))

    def find(self, player_id):
        return self.session.get(Player, player_id)

    def find_by_name(self, first_name, last_name):
        query = select(Player).where(Player.first_name == first_name, Player.last_name == last_name)
        return self.session.scalars(query).first()

    def add(self, player):
        self.session.add(player)
        self.session.flush()
        return player

    def save(self):
        self.session.commit()


class GameRepository:
    def __init__(self, session):
        self.session = session

    def find(self, game_id):
        return self.session.get(Game, game_id)

    def last(self):
        query = select(Game).order_by(Game.id.desc()).limit(1)
        return self.session.scalars(query).first()

    def add(self, game):
        self.session.add(game)
        self.session.flush()
        return game

    def delete(self, game):
        self.session.delete(game)

    def save(self):
        self.session.commit()
