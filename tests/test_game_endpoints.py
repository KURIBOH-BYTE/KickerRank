import pytest


@pytest.fixture
def player_ids(client):
    ids = []
    for first_name, last_name in [("Anna", "Keller"), ("Tim", "Brunner")]:
        response = client.post("/api/players",
                               json={"first_name": first_name, "last_name": last_name, "department": "HR"})
        ids.append(response.json()["id"])
    return ids


def create_game(client, player_ids, goals_a=10, goals_b=7):
    anna, tim = player_ids
    return client.post("/api/games",
                       json={"player_a_id": anna, "player_b_id": tim, "goals_a": goals_a, "goals_b": goals_b})


def test_spiel_erfassen_gibt_201(client, player_ids):
    response = create_game(client, player_ids)

    assert response.status_code == 201
    game = response.json()
    assert game["elo_change"] == 16
    assert game["winner_id"] == player_ids[0]
    assert game["player_a"]["elo"] == 1216


def test_ungueltiges_resultat_gibt_400(client, player_ids):
    response = create_game(client, player_ids, 10, 10)

    assert response.status_code == 400
    assert "Exactly one player" in response.json()["error"]


def test_letztes_spiel_ohne_spiele_ist_null(client):
    response = client.get("/api/games/last")

    assert response.status_code == 200
    assert response.json() is None


def test_letztes_spiel_ist_das_neuste(client, player_ids):
    create_game(client, player_ids, 10, 7)
    newest = create_game(client, player_ids, 3, 10).json()

    assert client.get("/api/games/last").json()["id"] == newest["id"]


def test_spiel_korrigieren(client, player_ids):
    game = create_game(client, player_ids).json()

    response = client.put(f"/api/games/{game['id']}", json={"goals_a": 7, "goals_b": 10})

    assert response.status_code == 200
    last = client.get("/api/games/last").json()
    assert (last["goals_a"], last["goals_b"]) == (7, 10)
    assert last["winner_id"] == player_ids[1]


def test_spiel_loeschen_gibt_204(client, player_ids):
    first = create_game(client, player_ids).json()
    second = create_game(client, player_ids, 3, 10).json()

    response = client.delete(f"/api/games/{second['id']}")

    assert response.status_code == 204
    assert client.get("/api/games/last").json()["id"] == first["id"]


def test_unbekanntes_spiel_gibt_404(client):
    response = client.delete("/api/games/999")

    assert response.status_code == 404
    assert response.json() == {"error": "This game does not exist."}
