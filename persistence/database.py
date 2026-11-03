"""Persistence Layer: Datenbankverbindung und Session.

Die Datenbank ist SQLite (eine Datei im Projektordner). Für MySQL genügt es,
DATABASE_URL anzupassen, z. B. "mysql+pymysql://user:pw@localhost/kicker".
"""
from collections.abc import Iterator
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DB_PFAD = Path(__file__).resolve().parent.parent / "kicker.db"
DATABASE_URL = f"sqlite:///{DB_PFAD}"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    """Basisklasse für alle Domain Entities."""


def get_session() -> Iterator[Session]:
    """Liefert pro Anfrage eine Session (wird von FastAPI via Depends injiziert)."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def init_db() -> None:
    """Legt die Tabellen an, falls sie noch nicht existieren."""
    from persistence import entities  # noqa: F401  (Entities registrieren)

    Base.metadata.create_all(engine)
