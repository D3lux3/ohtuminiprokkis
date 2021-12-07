import os
import unittest
from db import DataBase
from models import KirjaVinkki, Kurssi, base

class Testdb(unittest.TestCase):

    def setUp(self):
        self.tmp_db = DataBase("tmp123db", base)
        self.vinkki = KirjaVinkki(otsikko = "Pro Git Book", kommentti = "Very cool")
        self.kurssi = Kurssi(nimi = "TKT20006 Ohjelmistotuotanto")

    def test_there_are_no_vinkit_in_the_beginning(self):
        query_result = self.tmp_db.session.query(KirjaVinkki).all()
        self.assertEqual(len(query_result), 0)

    def test_adding_adds_correct_kirjavinkki_to_db(self):
        self.tmp_db.add_vinkki_to_db(self.vinkki)
        result = self.tmp_db.find_all_vinkit()
        query_result = self.tmp_db.session.query(KirjaVinkki).all()
        otsikko = query_result[0].otsikko
        kommentti = query_result[0].kommentti
        id = query_result[0].id

        self.assertEqual(len(result), 1)
        self.assertEqual(otsikko, self.vinkki.otsikko)
        self.assertEqual(kommentti, self.vinkki.kommentti)
        self.assertEqual(id, 1)

    def test_course_can_be_added_to_kirjavinkki(self):
        self.tmp_db.add_vinkki_to_db(self.vinkki)
        self.vinkki.add_related_course(self.kurssi)
        query_result = self.tmp_db.session.query(KirjaVinkki).all()
        kurssi = query_result[0].related_courses[0].nimi

        self.assertEqual(kurssi, self.kurssi.nimi)

    def test_course_added_to_kirjavinkki_is_saved_to_Kurssit(self):
        self.tmp_db.add_vinkki_to_db(self.vinkki)
        self.vinkki.add_related_course(self.kurssi)
        query_result = self.tmp_db.session.query(Kurssi).all()
        kurssi = query_result[0]

        self.assertEqual(len(query_result), 1)
        self.assertEqual(kurssi.nimi, self.kurssi.nimi)

    def test_delete_vinkki_removes_vinkki(self):
        self.tmp_db.add_vinkki_to_db(self.vinkki)
        removed = self.tmp_db.delete_vinkki_with_id(1)
        query_result = self.tmp_db.session.query(KirjaVinkki).all()

        self.assertTrue(removed)
        self.assertEqual(len(query_result), 0)

    def test_delete_vinkki_does_nothing_when_given_incorrect_id(self):
        self.tmp_db.add_vinkki_to_db(self.vinkki)
        removed = self.tmp_db.delete_vinkki_with_id(15)
        query_result = self.tmp_db.session.query(KirjaVinkki).all()

        self.assertFalse(removed)
        self.assertEqual(len(query_result), 1)

    def test_deleting_kirjavinkki_deletes_its_related_courses(self):
        pass

    def test_query_with_id_returns_correct_kirja_obect(self):
        pass

    def test_query_with_id_returns_correct_video_obect(self):
        pass

    def test_query_with_nonexisting_id_results_none(self):
        pass

    def tearDown(self):
        os.remove("tmp123db.db")