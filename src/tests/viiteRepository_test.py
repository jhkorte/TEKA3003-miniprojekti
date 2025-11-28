import unittest
from viiteRepository import ViiteRepository
from viite import Viite
from unittest.mock import Mock

def test_luoViiteInproceedings(monkeypatch):
    repo = ViiteRepository()
    repo.viitteet = []

    mock_input = Mock(side_effect=[
        "avain",
        "Jon",
        "otsikko",
        "2025",
        "kirjaotsikko"
    ])

    monkeypatch.setattr("builtins.input", mock_input)

    repo.luoViiteInproceedings()
    
    assert len(repo.viitteet) == 1

    viite = repo.viitteet[0]
    assert isinstance(viite, Viite)
    assert viite.key == "avain"
    assert viite.author == "Jon"
    assert viite.title == "otsikko"
    assert viite.year == "2025"
    assert viite.booktitle == "kirjaotsikko"
