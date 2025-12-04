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


def test_tallennaViitteetJsoniin_onnistuu(monkeypatch):
    tiedostonimi = "test_viitteet.json"
    repo = ViiteRepository(tiedostonimi)
    viite1 = Viite(author="Testaaja1",year="2000",title="title1")
    viite2 = Viite(author="Testaaja2",year="2001",title="title2")
    repo.viitteet = [viite1]

    mock_file = Mock()
    mock_open = Mock(return_value=mock_file)
    mock_file.__enter__ = Mock(return_value=mock_file)
    mock_file.__exit__ = Mock()
    monkeypatch.setattr("builtins.open", mock_open)

    mock_json_dump = Mock()
    monkeypatch.setattr("json.dump", mock_json_dump)

    mock_print = Mock()
    monkeypatch.setattr("builtins.print", mock_print)

    repo.tallennaViitteetJsoniin()

    mock_open.assert_called_with(tiedostonimi, "w", encoding="utf-8")
    dictionary = [viite1.toDictionary()]
    mock_json_dump.assert_called_with(dictionary, mock_file, indent=4)
    mock_print.assert_any_call(f"\nViitteet tallennettu tiedostoon: {tiedostonimi}.")


def test_tallennaViitteetJsoniin_virheilmoitus(monkeypatch):
    repo = ViiteRepository("virheellinen.json")
    viite1 = Viite(author="Testaaja1",year="2000",title="title1")
    repo.viitteet = [viite1]

    mock_open = Mock(side_effect=IOError("Levyvirhe"))
    monkeypatch.setattr("builtins.open", mock_open)

    mock_print = Mock()
    monkeypatch.setattr("builtins.print", mock_print)

    repo.tallennaViitteetJsoniin()

    loytyi_virheviesti = False
    for call in mock_print.call_args_list:
        args, _ = call
        if args and "Tallennus epäonnistui" in str(args[0]):
            loytyi_virheviesti = True
            break

    assert loytyi_virheviesti


def test_tallennaViitteetTiedostoon(monkeypatch):
    repo = ViiteRepository()
    viite1 = Viite(author="Testaaja1",year="2000",title="title1")
    repo.viitteet = [viite1]

    mock_file = Mock()
    mock_open = Mock(return_value=mock_file)

    monkeypatch.setattr("builtins.open", mock_open)
    mock_file.__enter__ = Mock(return_value=mock_file)
    mock_file.__exit__ = Mock()

    repo.tallennaViitteetTiedostoon()
    mock_open.assert_called_with("references.bib", "w")
    mock_file.write.assert_any_call(str(viite1))
    mock_file.write.assert_any_call("\n")
    assert mock_file.write.call_count == 2


def test_Filtteroi(monkeypatch):
    repo = ViiteRepository()
    viite1 = Viite(author="Testaaja1",year="2000",title="title1")
    viite2 = Viite(author="Testaaja2",year="2001",title="title2")
    repo.viitteet = [viite1, viite2]

    mock_input = Mock(side_effect=["author", "Testaaja1"])
    monkeypatch.setattr("builtins.input", mock_input)

    mock_print = Mock()
    monkeypatch.setattr("builtins.print", mock_print)

    repo.Filtteroi()
    mock_print.assert_any_call(str(viite1))

    kutsut = mock_print.call_args_list
    assert str(viite2) not in str(kutsut)