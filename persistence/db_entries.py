from datetime import datetime

from persistence.entities import Game, Player

# first_name, last_name, department, elo, games_played (state after all DEMO_GAMES)
DEMO_PLAYERS = [
    ("Lukas", "Müller", "Development", 1260, 4),
    ("Sarah", "Meier", "Marketing", 1230, 4),
    ("Elena", "Rossi", "HR", 1199, 4),
    ("Giovanni", "Bernasconi-Hofstetter", "Finance", 1185, 3),
    ("Tim", "Brunner", "Support", 1173, 4),
    ("Anna", "Keller", "Development", 1153, 5),
]

# played_at, player_a, player_b, goals_a, goals_b, elo_a_before, elo_b_before, elo_change
DEMO_GAMES = [
    ("2026-11-02 12:10", "Lukas", "Sarah", 10, 7, 1200, 1200, 16),
    ("2026-11-02 16:45", "Anna", "Tim", 10, 4, 1200, 1200, 16),
    ("2026-11-03 12:20", "Giovanni", "Elena", 8, 10, 1200, 1200, 16),
    ("2026-11-04 12:05", "Lukas", "Anna", 10, 6, 1216, 1216, 16),
    ("2026-11-05 17:30", "Sarah", "Tim", 10, 9, 1184, 1184, 16),
    ("2026-11-06 12:15", "Elena", "Lukas", 7, 10, 1216, 1232, 15),
    ("2026-11-09 12:40", "Giovanni", "Anna", 10, 8, 1184, 1200, 17),
    ("2026-11-09 16:50", "Tim", "Elena", 10, 6, 1168, 1201, 18),
    ("2026-11-10 12:10", "Sarah", "Giovanni", 10, 5, 1200, 1201, 16),
    ("2026-11-11 12:25", "Lukas", "Tim", 10, 3, 1247, 1186, 13),
    ("2026-11-12 17:15", "Anna", "Elena", 9, 10, 1183, 1183, 16),
    ("2026-11-13 12:05", "Sarah", "Anna", 10, 8, 1216, 1167, 14),
]


def insert_db_entries(session):
    if session.query(Player).count() > 0:
        return

    players = {}
    for first_name, last_name, department, elo, games_played in DEMO_PLAYERS:
        player = Player(first_name=first_name, last_name=last_name, department=department,
                        elo=elo, games_played=games_played)
        players[first_name] = player
        session.add(player)

    for played_at, a, b, goals_a, goals_b, elo_a_before, elo_b_before, elo_change in DEMO_GAMES:
        session.add(Game(
            played_at=datetime.strptime(played_at, "%Y-%m-%d %H:%M"),
            player_a=players[a], player_b=players[b],
            goals_a=goals_a, goals_b=goals_b,
            elo_a_before=elo_a_before, elo_b_before=elo_b_before, elo_change=elo_change,
        ))

    session.commit()
