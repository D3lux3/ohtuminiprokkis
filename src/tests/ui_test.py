import unittest
from unittest.mock import Mock
from ui.ui import Ui

class Stub_io:
    def __init__(self, inputs = []):
        self.inputs = inputs
        self.outputs = []

    def read_input(self, text):
        return self.inputs.pop(0)

    def write(self, text):
        self.outputs.append(text)


class TestUi(unittest.TestCase):

    def setUp(self):
        self.io = Stub_io()
        self.db_mock = Mock()
        self.stub_ui = Ui(self.io, self.db_mock)

    def test_legal_input_command(self):
        self.stub_ui.process_command(1)
        self.assertEqual(len(self.io.outputs), 0)

