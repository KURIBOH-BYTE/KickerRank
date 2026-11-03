"""Business Service Layer – Spiele erfassen, korrigieren und löschen."""
from fastapi import Depends

from business.dtos import SpielDTO
from business.elo import elo_aenderung
from business.fehler import GeschaeftsFehler
from persistence.data_access import SpielerRepository, SpielRepository
from persistence.entities import Spiel

SIEG_TORE = 10


class SpielService:
    def __init__(self, spiel_repo: SpielRepository = Depends(),
                 spieler_repo: SpielerRepository = Depends()):
        self.spiel_repo = spiel_repo
        self.spieler_repo = spieler_repo

    # ---------- Regeln ----------

    @staticmethod
    def _pruefe_resultat(tore_a: int, tore_b: int) -> None:
        for tore in (tore_a, tore_b):
            if not isinstance(tore, int) or not 0 <= tore <= SIEG_TORE:
                raise GeschaeftsFehler(f"Tore müssen zwischen 0 und {SIEG_TORE} liegen.")
        if (tore_a == SIEG_TORE) == (tore_b == SIEG_TORE):
            raise GeschaeftsFehler(f"Genau ein Spieler muss {SIEG_TORE} Tore haben.")

    @staticmethod
    def _wende_elo_an(spiel: Spiel) -> None:
        """Berechnet die Elo-Änderung aus den Werten vor dem Spiel und setzt
        die neuen Elo-Werte bei beiden Spielern."""
        a_gewinnt = spiel.tore_a > spiel.tore_b
        if a_gewinnt:
            delta = elo_aenderung(spiel.elo_a_vorher, spiel.elo_b_vorher)
        else:
            delta = elo_aenderung(spiel.elo_b_vorher, spiel.elo_a_vorher)

        spiel.elo_aenderung = delta
        spiel.spieler_a.elo = spiel.elo_a_vorher + (delta if a_gewinnt else -delta)
        spiel.spieler_b.elo = spiel.elo_b_vorher + (-delta if a_gewinnt else delta)

    def _hole_neustes(self, spiel_id: int) -> Spiel:
        spiel = self.spiel_repo.finde(spiel_id)
        if spiel is None:
            raise GeschaeftsFehler("Dieses Spiel existiert nicht.")
        if spiel.id != self.spiel_repo.letztes().id:
            raise GeschaeftsFehler("Nur das neuste Spiel darf geändert oder gelöscht werden.")
        return spiel

    # ---------- Business-Funktionen ----------

    def letztes_spiel(self) -> SpielDTO | None:
        spiel = self.spiel_repo.letztes()
        return SpielDTO.aus_entity(spiel) if spiel else None

    def spiel_erfassen(self, spieler_a_id: int, spieler_b_id: int,
                       tore_a: int, tore_b: int) -> SpielDTO:
        if spieler_a_id == spieler_b_id:
            raise GeschaeftsFehler("Ein Spieler kann nicht gegen sich selbst spielen.")
        a = self.spieler_repo.finde(spieler_a_id)
        b = self.spieler_repo.finde(spieler_b_id)
        if a is None or b is None:
            raise GeschaeftsFehler("Mindestens ein Spieler existiert nicht.")
        self._pruefe_resultat(tore_a, tore_b)

        spiel = Spiel(
            spieler_a=a, spieler_b=b, tore_a=tore_a, tore_b=tore_b,
            elo_a_vorher=a.elo, elo_b_vorher=b.elo, elo_aenderung=0,
        )
        self._wende_elo_an(spiel)
        a.anzahl_spiele += 1
        b.anzahl_spiele += 1

        self.spiel_repo.hinzufuegen(spiel)
        self.spiel_repo.speichern()  # Spiel + beide Spieler in einer Transaktion
        return SpielDTO.aus_entity(spiel)

    def spiel_korrigieren(self, spiel_id: int, tore_a: int, tore_b: int) -> SpielDTO:
        spiel = self._hole_neustes(spiel_id)
        self._pruefe_resultat(tore_a, tore_b)

        # Die Elo-Werte von vor dem Spiel gelten weiter, nur das Resultat ändert sich.
        spiel.tore_a = tore_a
        spiel.tore_b = tore_b
        self._wende_elo_an(spiel)

        self.spiel_repo.speichern()
        return SpielDTO.aus_entity(spiel)

    def spiel_loeschen(self, spiel_id: int) -> None:
        spiel = self._hole_neustes(spiel_id)

        # Beide Spieler erhalten ihre Elo von vor dem Spiel zurück.
        spiel.spieler_a.elo = spiel.elo_a_vorher
        spiel.spieler_b.elo = spiel.elo_b_vorher
        spiel.spieler_a.anzahl_spiele -= 1
        spiel.spieler_b.anzahl_spiele -= 1

        self.spiel_repo.loeschen(spiel)
        self.spiel_repo.speichern()
