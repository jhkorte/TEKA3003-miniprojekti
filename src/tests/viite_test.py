import unittest
from viiteRepository import ViiteRepository
from viite import Viite
from unittest.mock import Mock

class TestViite(unittest.TestCase):
    def test_viite_str_with_all(self):
        viite = Viite(
            entryType="article",
            key="123ABC",
            author="Matti",
            year="2025",
            title="Tutkimus jostain",
            booktitle=None,
            journal="Journal of Testing",
            volume="10",
            pages="100-110",
            publisher=None
        )
    
        expected_str = (
            "@article{123ABC,\n"
            "    author = {Matti},\n"
            "    title = {Tutkimus jostain},\n"
            "    year = {2025},\n"
            "    journal = {Journal of Testing},\n"
            "    volume = {10},\n"
            "    pages = {100-110},\n"
            "}"
        )

        self.assertEqual(str(viite), expected_str)

    def test_viite_str_with_two(self):
        viite = Viite(
            entryType="book",
            key="456DEF")
        expected_str = (
            "@book{456DEF,\n"
            "}")
        self.assertEqual(str(viite), expected_str)

