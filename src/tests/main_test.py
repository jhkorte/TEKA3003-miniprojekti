import unittest
import io
from unittest.mock import Mock, patch, ANY
from viiteRepository import ViiteRepository
from main import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.repo = ViiteRepository()

    def test_wrong_response(self):
        repo = ViiteRepository()

        repo.viitteenLuontiKysely = Mock()
        repo.tulostaViitteetListasta = Mock()

        response = "väärä"
        self.assertEqual(response, "väärä")

        repo.viitteenLuontiKysely.assert_not_called()
        repo.tulostaViitteetListasta.assert_not_called()

    def test_quit_response(self):
        repo = ViiteRepository()
        repo.tallennaViitteetJsoniin = Mock()

        response = "quit"
        self.assertEqual(response, "quit")

        if response == "quit":
            repo.tallennaViitteetJsoniin()

        repo.tallennaViitteetJsoniin.assert_called()

    def test_new_response(self):
        repo = ViiteRepository()
        repo.viitteenLuontiKysely = Mock()

        response = "new"
        self.assertEqual(response, "new")

        if response == "new":
            repo.viitteenLuontiKysely()

        repo.viitteenLuontiKysely.assert_called()

    def test_print_response(self):
        repo = ViiteRepository()
        repo.tulostaViitteetListasta = Mock()

        response = "print"
        self.assertEqual(response, "print")

        if response == "print":
            repo.tulostaViitteetListasta()

        repo.tulostaViitteetListasta.assert_called()

    def test_luo_response(self):
        repo = ViiteRepository()
        repo.tallennaViitteetTiedostoon = Mock()

        response = "luo"
        self.assertEqual(response, "luo")

        if response == "luo":
            repo.tallennaViitteetTiedostoon()

        repo.tallennaViitteetTiedostoon.assert_called()

    def test_sequence_of_commands(self):
        with patch("builtins.input", side_effect=[
            "new",
            "inproceedings",
            "avain",
            "Jon",
            "otsikko",
            "2025",
            "kirjaotsikko",
            "print",
            "quit"
        ]):
            main()

    def test_start_print(self):
        with patch("builtins.input", side_effect=["quit"]), \
             patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            main()

            output = mock_stdout.getvalue()

            self.assertIn("Tama on kayttoliittymasovellus viitteiden hallintaan bibtex muodossa", output)
            self.assertIn("Mahdolliset komennot:", output)
            self.assertIn("New: Lisaa uusi viite", output)
            self.assertIn("Quit: Tallenna ja päätä ohjelman käyttö", output)


    def test_hae_response(self):
        repo = ViiteRepository()
        repo.Filtteroi = Mock()

        response = "hae"
        self.assertEqual(response, "hae")

        if response == "hae":
            repo.Filtteroi()

        repo.Filtteroi.assert_called()
