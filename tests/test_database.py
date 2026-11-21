from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from business.player_service import PlayerService
from persistence.data_access import PlayerRepository
from persistence.database import Base, init_db


def test_init_db_erstellt_tabellen():
    engine = create_engine("sqlite:///:memory:")
    init_db(bind=engine)
    assert set(inspect(engine).get_table_names()) == set(Base.metadata.tables.keys())


def test_daten_bleiben_nach_neuer_session_erhalten(tmp_path):
    database_url = f"sqlite:///{tmp_path / 'kickerrank.db'}"

    first_start = create_engine(database_url)
    init_db(bind=first_start)
    with sessionmaker(bind=first_start)() as session:
        PlayerService(PlayerRepository(session)).create_player("Anna", "Keller", "HR")
    first_start.dispose()

    second_start = create_engine(database_url)
    with sessionmaker(bind=second_start)() as session:
        ranking = PlayerService(PlayerRepository(session)).ranking()
    second_start.dispose()

    assert [player.first_name for player in ranking] == ["Anna"]
