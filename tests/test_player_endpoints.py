from business.departments import DEPARTMENTS
from persistence.entities import Player


def test_rangliste_ist_nach_elo_sortiert(client, session):
    session.add_all([
        Player(first_name="Tim", last_name="Brunner", department="Support", elo=1180),
        Player(first_name="Lukas", last_name="Müller", department="Development", elo=1260),
        Player(first_name="Sarah", last_name="Meier", department="Marketing", elo=1230),
    ])
    session.commit()

    response = client.get("/api/ranking")

    assert response.status_code == 200
    assert [player["first_name"] for player in response.json()] == ["Lukas", "Sarah", "Tim"]


def test_rangliste_enthaelt_alle_felder(client, session):
    session.add(Player(first_name="Anna", last_name="Keller", department="HR"))
    session.commit()

    player = client.get("/api/ranking").json()[0]

    assert player["last_name"] == "Keller"
    assert player["department"] == "HR"
    assert player["elo"] == 1200
    assert player["games_played"] == 0
    assert "id" in player


def test_leere_rangliste(client):
    assert client.get("/api/ranking").json() == []


def test_abteilungen(client):
    response = client.get("/api/departments")

    assert response.status_code == 200
    assert response.json() == DEPARTMENTS
    assert "Development" in response.json()


def test_spieler_anlegen_gibt_201(client):
    response = client.post("/api/players",
                           json={"first_name": "Anna", "last_name": "Keller", "department": "HR"})

    assert response.status_code == 201
    assert response.json()["id"] is not None


def test_neuer_spieler_startet_mit_1200(client):
    client.post("/api/players", json={"first_name": "Anna", "last_name": "Keller", "department": "HR"})

    ranking = client.get("/api/ranking").json()

    assert ranking[0]["first_name"] == "Anna"
    assert (ranking[0]["elo"], ranking[0]["games_played"]) == (1200, 0)


def test_doppelter_spieler_gibt_400(client):
    player = {"first_name": "Anna", "last_name": "Keller", "department": "HR"}
    client.post("/api/players", json=player)

    response = client.post("/api/players", json=player)

    assert response.status_code == 400
    assert "already exists" in response.json()["error"]


def test_fehlendes_feld_gibt_422(client):
    response = client.post("/api/players", json={"first_name": "Anna", "last_name": "Keller"})

    assert response.status_code == 422
