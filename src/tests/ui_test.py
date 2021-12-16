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
        self.io = Stub_io(["2", "1", "Unknown", "Pro Git Book", "0123456789", "Very nice book", "2", "2", "0"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()

        self.db_mock.add_vinkki_to_db.assert_called()

    def test_print_vinkit_calls_db_find_all_vinkit(self):
        self.io = Stub_io(["1", "5", "0"])
        self.db_mock.find_all_vinkit.return_value = []
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()

        self.db_mock.find_all_vinkit.assert_called()

    def test_random_vinkki(self):
        self.io = Stub_io(["4", "0"])
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
        self.assertEqual(self.io.outputs[9].otsikko, "python-kirja")

    def test_add_podcastvinkki_calls_add_podcast_vinkki_to_db(self):
        self.io = Stub_io([
            "2", "3", "Sami Honkonen", "Boss Level Podcast",
            "Jim Benson on Personal Kanban, Lean Coffee and collaboration",
            "VERY interesting", "2", "2", "0"
        ])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()

        self.db_mock.add_podcast_vinkki_to_db.assert_called()

    def test_delete_vinkki_called_when_selected(self):
        self.io = Stub_io(["3", "1", "1", "0"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.delete_vinkki_with_id.assert_called()

    def test_add_videovinkki_calls_add_video_vinkki_to_db(self):
        self.io = Stub_io(["2", "2", "Never gonna give you up", "youtube.com/abcd", "Ihan ok video", "2", "2", "0"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.add_video_vinkki_to_db.assert_called()
    
    def test_add_blogpostvinkki_calls_add_blogpost_vinkki_to_db(self):
        self.io = Stub_io(["2", "4", "Blogikirjoittaja", "Tietokoneohje", "Miten tietokone sammutetaan", "Ohje ammattilaisille", "2", "2", "0"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.add_blogpost_vinkki_to_db.assert_called()

    def test_adding_tags_to_kirjavinkki_calls_add_tag_to_vinkki(self):
        self.io = Stub_io(["2", "1", "Book person", "Tagikirja", "321654", "tags are cool", "1", "this is a tag", "2", "2", "0"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.add_tag_to_vinkki.assert_called()

    def test_adding_tags_to_podcastvinkki_calls_add_tag_to_podcastvinkki(self):
        self.io = Stub_io([
            "2", "3", "Podcast person", "Podcast about tags",
            "Why tags are nice",
            "Very useful info", "1", "this is a tag too", "2", "2", "0"
        ])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.add_tag_to_podcastvinkki.assert_called()

    def test_adding_tags_to_blogpostvinkki_calls_add_tag_to_blogpostvinkki(self):
        self.io = Stub_io(["2", "4", "Blog person", "importance of tags", "significance of tags", "best tags to use", "1", "this too is a tag", "2", "2", "0"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.add_tag_to_blogpostvinkki.assert_called()

    def test_adding_courses_to_kirjavinkki_calls_add_course_to_kirjavinkki(self):
        self.io = Stub_io(["2", "1", "Book writer", "Kurssikirja", "abcdisbn345", "courses are cool", "2", "1", "TiTo", "2", "0"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.add_course_to_kirjavinkki.assert_called()

    def test_adding_courses_to_videovinkki_calls_add_course_to_videovinkki(self):
        self.io = Stub_io(["2", "2", "Kurssivideo", "videowebsite.org", "i recommend this video", "2", "1", "TiRa", "2", "0"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.add_course_to_videovinkki.assert_called()

    def test_adding_tags_to_podcastvinkki_calls_add_course_to_podcastvinkki(self):
        self.io = Stub_io([
            "2", "3", "Podcast maker", "Podcast about courses",
            "Why courses are nice",
            "Very useful courses", "2", "1", "OhTu", "2", "0"
        ])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.add_course_to_podcastvinkki.assert_called()

    def test_adding_tags_to_blogpostvinkki_calls_add_course_to_blogpostvinkki(self):
        self.io = Stub_io(["2", "4", "Blog creator", "important courses", "best courses", "fun courses to take", "2", "1", "LaMa", "2", "0"])
        self.stub_ui = Ui(self.io, self.db_mock, self.number_generator_mock)
        self.stub_ui.start()
        
        self.db_mock.add_course_to_blogpostvinkki.assert_called()
