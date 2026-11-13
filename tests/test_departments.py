from business.departments import DEPARTMENTS, is_valid_department
from persistence.db_entries import DEMO_PLAYERS


def test_es_gibt_fuenf_abteilungen():
    assert len(DEPARTMENTS) == 5


def test_gueltige_abteilung():
    assert is_valid_department("Marketing")


def test_ungueltige_abteilung():
    assert not is_valid_department("Kantine")
    assert not is_valid_department("marketing")


def test_demo_spieler_haben_gueltige_abteilungen():
    for _, _, department, _, _ in DEMO_PLAYERS:
        assert is_valid_department(department)
