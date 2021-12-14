import unittest
from unittest.mock import Mock
from ui.ui import Ui
from models import KirjaVinkki

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
        self.number_generator_mock = Mock()
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.db_mock.find_all_vinkit.return_value = []

    def test_legal_input_command(self):
        self.stub_ui.process_command(1)
        self.assertEqual(len(self.io.outputs), 0)

    def test_illegal_input_command(self):
        self.stub_ui.process_command("illegal command")
        self.assertEqual(self.io.outputs[0], "Anna kelvollinen komento")

    def test_add_new_kirjavinkki_calls_db_add_vinkki_to_db(self):
        self.io = Stub_io(["2", "1", "Unknown", "Pro Git Book", "0123456789", "Very nice book", "2", "2", "5"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()

        self.db_mock.add_vinkki_to_db.assert_called()

    def test_print_vinkit_calls_db_find_all_vinkit(self):
        self.io = Stub_io(["1", "5"])
        self.db_mock.find_all_vinkit.return_value = []
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()

        self.db_mock.find_all_vinkit.assert_called()

    def test_random_vinkki(self):
        self.io = Stub_io(["4", "5"])
        self.number_generator_mock = Mock()
        def find_all_vinkit():
            vinkki1 = KirjaVinkki(otsikko = "Pro Git Book", kommentti = "Very cool")
            vinkki2 = KirjaVinkki(otsikko = "python-kirja", kommentti=  "i loved ittt")
            return [vinkki1, vinkki2]
        def random_int(max_number):
            return 1
        self.number_generator_mock.side_effect = random_int
        self.db_mock.find_all_vinkit.side_effect = find_all_vinkit
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        self.assertEqual(self.io.outputs[7].otsikko, "python-kirja")

    def test_add_podcastvinkki_calls_add_podcast_vinkki_to_db(self):
        self.io = Stub_io([
            "2", "3", "Sami Honkonen", "Boss Level Podcast",
            "Jim Benson on Personal Kanban, Lean Coffee and collaboration",
            "VERY interesting", "2", "2", "5"
        ])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()

        self.db_mock.add_podcast_vinkki_to_db.assert_called()

    def test_delete_vinkki_called_when_selected(self):
        self.io = Stub_io(["3", "1", "1", "5"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.delete_vinkki_with_id.assert_called()

    def test_add_videovinkki_calls_add_video_vinkki_to_db(self):
        self.io = Stub_io(["2", "2", "Never gonna give you up", "youtube.com/abcd", "Ihan ok video", "2", "5"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.add_video_vinkki_to_db.assert_called()
    
    def test_add_blogpostvinkki_calls_add_blogpost_vinkki_to_db(self):
        self.io = Stub_io(["2", "4", "Blogikirjoittaja", "Tietokone ohje", "Miten tietokone sammutetaan", "Ohje ammattilaisille", "2", "2", "5"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.add_blogpost_vinkki_to_db.assert_called()

    def test_incorrect_number_as_input(self):
        pass
