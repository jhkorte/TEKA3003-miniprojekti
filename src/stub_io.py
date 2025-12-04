"""Stub IO module for testing purposes."""
class StubIO:
    """
    A stub IO class that simulates input and output operations.
    """
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)

    def read(self):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""

    def add_input(self, value):
        self.inputs.append(value)
