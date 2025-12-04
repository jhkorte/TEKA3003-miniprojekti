"""Main library module for robot tests."""
from viiteRepository import ViiteRepository
from viite import Viite
from stub_io import StubIO



class mainLibrary:
    """
    Main library class for robot tests.
    """
    def __init__(self):
        self._io = StubIO()
        self._viiteRepository = ViiteRepository()

    def input(self, value):
        self._io.add_input(value)

    def input_book(key, author, title, year, publisher):
        viite = Viite(
            entryType="book",
            key="key1",
            author="Matti Meikäläinen",
            year="2020",
            title="Testikirja",
            publisher="Testikustantaja")
        return f"Luotu: {viite}"

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )
