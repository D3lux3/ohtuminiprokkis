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

    def test_add_new_calls_db_add_vinkki_to_db(self):
        self.io = Stub_io(["2", "Pro Git Book", "Very cool", "4"])
        self.stub_ui = Ui(self.io, self.db_mock)
        self.stub_ui.start()

        self.db_mock.add_vinkki_to_db.assert_called()

    def test_print_vinkit_calls_db_find_all_vinkit(self):
        self.io = Stub_io(["1", "4"])
        self.db_mock.find_all_vinkit.return_value = []
        self.stub_ui = Ui(self.io, self.db_mock)
        self.stub_ui.start()

        self.db_mock.find_all_vinkit.assert_called()
