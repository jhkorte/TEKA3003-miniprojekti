from viiteRepository import ViiteRepository
from stub_io import StubIO

class mainLibrary:
    def __init__(self):
        self._io = StubIO()
        self._viiteRepository = ViiteRepository()
    
    def input(self, value):
        self._io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )