from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_startseite_ist_erreichbar():
    antwort = client.get("/")
    assert antwort.status_code == 200