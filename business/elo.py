"""Business Layer: Elo-Berechnung wie im Schach."""

START_ELO = 1200
K_FAKTOR = 32


def erwartung(elo_a: int, elo_b: int) -> float:
    """Wahrscheinlichkeit, dass A gegen B gewinnt (zwischen 0 und 1)."""
    return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))


def elo_aenderung(elo_gewinner: int, elo_verlierer: int, k: int = K_FAKTOR) -> int:
    """Punkte, die der Gewinner erhält und der Verlierer abgibt.

    Beispiele mit K = 32:
      1200 schlägt 1200 -> +16
      1200 schlägt 1400 -> +24  (Aussenseiter gewinnt)
      1400 schlägt 1200 -> +8   (Favorit gewinnt)
    """
    return round(k * (1 - erwartung(elo_gewinner, elo_verlierer)))
