from sqlalchemy import create_engine, inspect

from persistence.database import Base, init_db


def test_init_db_erstellt_tabellen():
    engine = create_engine("sqlite:///:memory:")
    init_db(bind=engine)
    assert set(inspect(engine).get_table_names()) == set(Base.metadata.tables.keys())