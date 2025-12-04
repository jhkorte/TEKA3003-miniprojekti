import unittest
from viiteRepository import ViiteRepository
from viite import Viite
from unittest.mock import Mock

def test_luoViiteInproceedings(monkeypatch):
    repo = ViiteRepository("")
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


def test_TulostaViitteetListasta(monkeypatch):
    repo = ViiteRepository()
    repo.viitteet = ["viite 1", "viite 2", "viite 3"]

    mock_print = Mock()
    monkeypatch.setattr("builtins.print", mock_print)

    repo.tulostaViitteetListasta()

    assert mock_print.call_count == 5
    mock_print.assert_any_call("Tulostetaan tallennetut viitteet")
    mock_print.assert_any_call()
    mock_print.assert_any_call("viite 1")
    mock_print.assert_any_call("viite 2")
    mock_print.assert_any_call("viite 3")


def test_TulostaViitteetListasta_tyhja_lista(monkeypatch):
    repo = ViiteRepository()
    repo.viitteet = []

    mock_print = Mock()
    monkeypatch.setattr("builtins.print", mock_print)

    repo.tulostaViitteetListasta()

    assert mock_print.call_count == 2
    mock_print.assert_any_call("Ei tallennettuja viitteitä")
    mock_print.assert_any_call()


def test_lataaViitteetTiedostosta_ei_tiedostoa(monkeypatch):
    repo = ViiteRepository("ei_ole.json")

    def mock_exists(self):
        return False

    monkeypatch.setattr("pathlib.Path.exists", mock_exists)

    tulos = repo.lataaViitteetTiedostosta()
    assert tulos == []


def test_lataaViitteetTiedostosta(monkeypatch):
    repo = ViiteRepository("test.json")

    monkeypatch.setattr("pathlib.Path.exists", lambda self: True)

    fake_json = [{"key": "a"}, {"key": "b"}]

    monkeypatch.setattr("json.load", lambda f: fake_json)

    file_mock = Mock()
    mock_open = Mock(return_value=file_mock)
    file_mock.__enter__ = Mock(return_value=file_mock)
    file_mock.__exit__ = Mock()

    monkeypatch.setattr("builtins.open", mock_open)

    mock_viite = Mock()
    monkeypatch.setattr("viite.Viite.fromDictionary", lambda d: mock_viite)

    tulos = repo.lataaViitteetTiedostosta()

    assert len(tulos) == 2
    assert tulos[0] is mock_viite
