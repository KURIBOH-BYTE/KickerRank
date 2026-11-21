import importlib

import pytest

import config


@pytest.fixture(autouse=True)
def restore_config():
    yield
    importlib.reload(config)


def load_config(monkeypatch, **variables):
    for name in ["DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_NAME"]:
        monkeypatch.delenv(name, raising=False)
    for name, value in variables.items():
        monkeypatch.setenv(name, value)
    monkeypatch.setattr("dotenv.load_dotenv", lambda *args, **kwargs: None)
    return importlib.reload(config)


def test_standardwerte_ohne_env(monkeypatch):
    url = load_config(monkeypatch).DATABASE_URL

    assert (url.username, url.host, url.port, url.database) == ("kicker", "localhost", 3306, "kickerrank")


def test_werte_aus_umgebungsvariablen(monkeypatch):
    url = load_config(monkeypatch, DB_USER="anna", DB_PASSWORD="geheim", DB_HOST="db.local",
                      DB_PORT="3307", DB_NAME="liga").DATABASE_URL

    assert (url.username, url.password, url.host, url.port, url.database) == \
        ("anna", "geheim", "db.local", 3307, "liga")


def test_sonderzeichen_im_passwort(monkeypatch):
    url = load_config(monkeypatch, DB_PASSWORD="?sixt#sense@£").DATABASE_URL

    assert url.password == "?sixt#sense@£"
