from sqlalchemy import create_engine
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
    from persistence import entities  # noqa: F401  (Klassen registrieren, damit ihre Tabellen bekannt sind)

    Base.metadata.create_all(bind=bind)
