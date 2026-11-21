from business.departments import DEPARTMENTS, is_valid_department
from business.dtos import to_player_dto
from business.errors import BusinessError
from persistence.entities import Player

MAX_NAME_LENGTH = 50


class PlayerService:
    def __init__(self, players):
        self.players = players

    def ranking(self):
        result = []
        for player in self.players.all_by_elo():
            result.append(to_player_dto(player))
        return result

    def create_player(self, first_name, last_name, department):
        first_name = first_name.strip()
        last_name = last_name.strip()

        check_name(first_name, "First name")
        check_name(last_name, "Last name")

        if not is_valid_department(department):
            raise BusinessError(f"Unknown department. Allowed: {', '.join(DEPARTMENTS)}.")

        if self.players.find_by_name(first_name, last_name):
            raise BusinessError(f"A player named {first_name} {last_name} already exists.")

        player = self.players.add(Player(first_name=first_name, last_name=last_name, department=department))
        self.players.save()
        return to_player_dto(player)


def check_name(name, label):
    if not name:
        raise BusinessError(f"{label} must not be empty.")
    if len(name) > MAX_NAME_LENGTH:
        raise BusinessError(f"{label} is too long (max. {MAX_NAME_LENGTH} characters).")
