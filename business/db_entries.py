from datetime import datetime

from business.game_service import GameService
from business.player_service import PlayerService
from persistence.data_access import GameRepository, PlayerRepository

DEMO_PLAYERS = [
    ("Lukas", "Müller", "Development"),
    ("Sarah", "Meier", "Marketing"),
    ("Elena", "Rossi", "HR"),
    ("Giovanni", "Bernasconi-Hofstetter", "Finance"),
    ("Tim", "Brunner", "Support"),
    ("Anna", "Keller", "Development"),
]

# played_at, player_a, player_b, goals_a, goals_b
DEMO_GAMES = [
    ("2026-11-02 12:10", "Lukas", "Sarah", 10, 7),
    ("2026-11-02 16:45", "Anna", "Tim", 10, 4),
    ("2026-11-03 12:20", "Giovanni", "Elena", 8, 10),
    ("2026-11-04 12:05", "Lukas", "Anna", 10, 6),
    ("2026-11-05 17:30", "Sarah", "Tim", 10, 9),
    ("2026-11-06 12:15", "Elena", "Lukas", 7, 10),
    ("2026-11-09 12:40", "Giovanni", "Anna", 10, 8),
    ("2026-11-09 16:50", "Tim", "Elena", 10, 6),
    ("2026-11-10 12:10", "Sarah", "Giovanni", 10, 5),
    ("2026-11-11 12:25", "Lukas", "Tim", 10, 3),
    ("2026-11-12 17:15", "Anna", "Elena", 9, 10),
    ("2026-11-13 12:05", "Sarah", "Anna", 10, 8),
]


def insert_db_entries(session):
    players = PlayerRepository(session)
    player_service = PlayerService(players)
    game_service = GameService(players, GameRepository(session))

    if players.count() > 0:
        return

    player_ids = {}
    for first_name, last_name, department in DEMO_PLAYERS:
        player = player_service.create_player(first_name, last_name, department)
        player_ids[first_name] = player.id

    for played_at, a, b, goals_a, goals_b in DEMO_GAMES:
        game_service.create_game(player_ids[a], player_ids[b], goals_a, goals_b,
                                 played_at=datetime.strptime(played_at, "%Y-%m-%d %H:%M"))
