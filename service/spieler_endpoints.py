"""Web/REST Service Layer – Endpunkte für Spieler und Rangliste.

Keine Geschäftslogik: Anfrage annehmen, Business Service aufrufen,
Resultat als Message zurückgeben.
"""
from fastapi import APIRouter, Depends

from business.spieler_service import SpielerService
from service.messages import FehlerAntwort, SpielerAntwort, SpielerErstellen

router = APIRouter(prefix="/api", tags=["Spieler"])


@router.get("/rangliste", response_model=list[SpielerAntwort])
def rangliste(service: SpielerService = Depends()):
    return service.rangliste()


@router.get("/abteilungen", response_model=list[str])
def abteilungen(service: SpielerService = Depends()):
    return service.abteilungen()


@router.post("/spieler", response_model=SpielerAntwort, status_code=201,
             responses={400: {"model": FehlerAntwort}})
def spieler_anlegen(daten: SpielerErstellen, service: SpielerService = Depends()):
    return service.spieler_anlegen(daten.name, daten.abteilung)
