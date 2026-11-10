START_RATING = 1200
K_FACTOR = 32


def team_rating(ratings):
    average = sum(ratings) / len(ratings)
    return average


def win_probability(rating_a, rating_b):
    # Elo formula: probability that A beats B (0 to 1).
    # A difference of 400 points means the stronger player wins 10 times as often.
    probability = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    return probability


def rating_change(rating_winner, rating_loser):
    # The more unexpected the win (low probability), the more points.
    # K_FACTOR is the maximum number of points per game.
    expected = win_probability(rating_winner, rating_loser)
    change = round(K_FACTOR * (1 - expected))
    return change


def new_ratings(team_a, team_b, team_a_wins):
    rating_a = team_rating(team_a)
    rating_b = team_rating(team_b)

    if team_a_wins:
        delta = rating_change(rating_a, rating_b)
    else:
        delta = -rating_change(rating_b, rating_a)

    new_team_a = [rating + delta for rating in team_a]
    new_team_b = [rating - delta for rating in team_b]
    return new_team_a, new_team_b