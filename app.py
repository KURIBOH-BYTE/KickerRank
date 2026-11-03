"""Startpunkt der Kicker-Liga.

Start:  python app.py   ->  http://localhost:8000
"""
from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from business.fehler import GeschaeftsFehler
from business.spieler_service import SpielerService
from persistence.data_access import SpielerRepository
from persistence.database import SessionLocal, init_db
from service import spiel_endpoints, spieler_endpoints

DEMO_SPIELER = [
    ("Roy", "Informatik"), ("Lisa", "Marketing"), ("Marco", "Finanzen"),
    ("Sara", "Informatik"), ("Jonas", "Verkauf"), ("Elena", "HR"),
]


def demo_daten_einfuegen() -> None:
    """Legt beim ersten Start ein paar Spieler an, damit die App nicht leer ist."""
    with SessionLocal() as session:
        service = SpielerService(SpielerRepository(session))
        if service.rangliste():
            return
        for name, abteilung in DEMO_SPIELER:
            service.spieler_anlegen(name, abteilung)


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    demo_daten_einfuegen()
    yield


app = FastAPI(title="Kicker-Liga", lifespan=lifespan)


@app.exception_handler(GeschaeftsFehler)
async def geschaeftsfehler_handler(_: Request, fehler: GeschaeftsFehler):
    """Verletzte Geschäftsregel -> HTTP 400 mit verständlicher Meldung."""
    return JSONResponse(status_code=400, content={"fehler": str(fehler)})


# Web/REST Service Layer
app.include_router(spieler_endpoints.router)
app.include_router(spiel_endpoints.router)

# Presentation Layer: HTML, CSS und JavaScript werden als statische Dateien ausgeliefert
app.mount("/", StaticFiles(directory=Path(__file__).parent / "presentation", html=True), name="presentation")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
