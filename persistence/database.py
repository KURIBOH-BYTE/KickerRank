from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def init_db(bind=engine):
    from persistence import entities  # noqa: F401

    tables = inspect(bind).get_table_names()
    if tables:
        print(f"Existing tables: {', '.join(tables)}")
    else:
        print("No tables found, creating schema.")

    Base.metadata.create_all(bind=bind)
