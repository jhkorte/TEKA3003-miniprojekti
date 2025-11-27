import pytest
from viiteRepository import ViiteRepository
from viite import Viite
from unittest.mock import patch

def test_luoViiteInproceedings():
    testi_viite = Viite()
    testi_viite.viitteet = []

    syotteet = [
        "avain",
        "Jon",
        "otsikko",
        "2025",
        "otsikko"
    ]

    with patch("builtins.input", side_effect=syotteet):
        testi_viite.luoViiteInproceeedings()

    assert len(testi_viite.viitteet) == 1

    viite = testi_viite.viitteet[0]
    assert isinstance(viite, Viite)
    assert viite.key == "avain"
    assert viite.author == "Jon"
    assert viite.title == "otsikko"
    assert viite.year == "2025"
    assert viite.booktitle == "kirjaotsikko"
