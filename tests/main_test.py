import unittest
from unittest.mock import Mock
from src.viiteRepository import ViiteRepository

class TestMain(unittest.TestCase):
    def setUp(self):
        self.repo = ViiteRepository()
    
    def test_response(self):
        repo = ViiteRepository()

        repo.viitteenLuontiKysely = Mock()
        repo.tulostaViitteetListasta = Mock()
        
        response = "väärä"
        self.assertEqual(response, "väärä")
   
        repo.viitteenLuontiKysely().assert_not_called()
        repo.tulostaViitteetListasta().assert_not_called()
