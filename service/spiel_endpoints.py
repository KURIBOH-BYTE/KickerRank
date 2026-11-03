"""Web/REST Service Layer – Endpunkte für Spiele.

Keine Geschäftslogik: Anfrage annehmen, Business Service aufrufen,
Resultat als Message zurückgeben.
"""
from fastapi import APIRouter, Depends, Response

from business.spiel_service import SpielService
from service.messages import FehlerAntwort, ResultatKorrigieren, SpielAntwort, SpielErfassen

router = APIRouter(prefix="/api/spiele", tags=["Spiele"])
FEHLER = {400: {"model": FehlerAntwort}}


@router.post("", response_model=SpielAntwort, status_code=201, responses=FEHLER)
def spiel_erfassen(daten: SpielErfassen, service: SpielService = Depends()):
    return service.spiel_erfassen(daten.spieler_a_id, daten.spieler_b_id, daten.tore_a, daten.tore_b)


@router.get("/letztes", response_model=SpielAntwort | None)
def letztes_spiel(service: SpielService = Depends()):
    return service.letztes_spiel()


@router.put("/{spiel_id}", response_model=SpielAntwort, responses=FEHLER)
def spiel_korrigieren(spiel_id: int, daten: ResultatKorrigieren, service: SpielService = Depends()):
    return service.spiel_korrigieren(spiel_id, daten.tore_a, daten.tore_b)


@router.delete("/{spiel_id}", status_code=204, responses=FEHLER)
def spiel_loeschen(spiel_id: int, service: SpielService = Depends()):
    service.spiel_loeschen(spiel_id)
    return Response(status_code=204)
