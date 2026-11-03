"""Business Layer: Fehler, wenn eine Geschäftsregel verletzt wird."""


class GeschaeftsFehler(Exception):
    """Wird geworfen, wenn eine Eingabe gegen eine Regel verstösst.

    Der Service Layer übersetzt diesen Fehler in eine HTTP-400-Antwort.
    """
