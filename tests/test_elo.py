from business.elo  import (
    K_FACTOR,
    START_RATING,
    new_ratings,
    rating_change,
    team_rating,
    win_probability,
)


def test_constants():
    assert START_RATING == 1200
    assert K_FACTOR == 32


def test_win_probability_equal_ratings_is_half():
    assert win_probability(1200, 1200) == 0.5


def test_equal_ratings_change_16():
    assert rating_change(1200, 1200) == 16


def test_underdog_wins_24():
    assert rating_change(1200, 1400) == 24


def test_favourite_wins_8():
    assert rating_change(1400, 1200) == 8


def test_team_rating_is_average():
    assert team_rating([1200, 1400]) == 1300


def test_new_ratings_team_a_wins():
    assert new_ratings([1200], [1200], True) == ([1216], [1184])


def test_new_ratings_team_b_wins():
    assert new_ratings([1200], [1400], False) == ([1192], [1408])


def test_new_ratings_2vs2_both_players_get_same_points():
    assert new_ratings([1200, 1400], [1300, 1300], True) == ([1216, 1416], [1284, 1284])