import os
import unittest
from db import DataBase
from models import KirjaVinkki, Kurssi, PodcastVinkki, VideoVinkki, BlogpostVinkki, Tagi, base
from models import kirjavinkki_courses, podcastvinkki_courses, podcastvinkki_tagit, blogpostvinkki_courses, blogpostvinkki_tagit
from vinkkityyppi import VinkkiTyyppi

class Testdb(unittest.TestCase):

    def setUp(self):
        self.tmp_db = DataBase("tmp123db", base)
        self.kirjavinkki = KirjaVinkki(otsikko = "Pro Git Book", kommentti = "Very cool")
        self.videovinkki = VideoVinkki(otsikko = "New video vinkki", url = "www.newvinkki.com", kommentti = "Very good kommentti")
        self.podcastvinkki = PodcastVinkki(author = "yle", nimi = "joku podcast", otsikko = "it ja tulevaisuus", kuvaus = "ok")
        self.blogpostvinkki = BlogpostVinkki(author = "Coco", nimi = "travellaus", otsikko = "kambodza", kommentti = "pilalla")
        self.kurssi = Kurssi(nimi = "TKT20006 Ohjelmistotuotanto")
        self.tagi = Tagi(nimi = "tag1")

    def test_there_are_no_vinkit_in_the_beginning(self):
        query_result = self.tmp_db.session.query(KirjaVinkki).all()
        self.assertEqual(len(query_result), 0)

    # vinkin lisäys
    def test_adding_adds_correct_kirjavinkki_to_db(self):
        self.tmp_db.add_vinkki_to_db(self.kirjavinkki)
        result = self.tmp_db.find_all_vinkit()
        query_result = self.tmp_db.session.query(KirjaVinkki).all()
        otsikko = query_result[0].otsikko
        tyyppi = query_result[0].tyyppi
        kommentti = query_result[0].kommentti
        kurssit = query_result[0].related_courses
        luettu = query_result[0].luettu

        self.assertEqual(len(result), 1)
        self.assertEqual(otsikko, self.kirjavinkki.otsikko)
        self.assertEqual(tyyppi, self.kirjavinkki.tyyppi)
        self.assertEqual(kommentti, self.kirjavinkki.kommentti)
        self.assertEqual(len(kurssit), 0)
        self.assertEqual(luettu, self.kirjavinkki.luettu)
        self.assertFalse(self.kirjavinkki.luettu)

    def test_adding_adds_correct_videovinkki_to_db(self):
        self.tmp_db.add_video_vinkki_to_db(self.videovinkki)
        result = self.tmp_db.find_all_vinkit()
        query_result = self.tmp_db.session.query(VideoVinkki).all()

        self.assertEqual(len(result), 1)
        self.assertEqual(query_result[0].otsikko, self.videovinkki.otsikko)
        self.assertEqual(query_result[0].tyyppi, self.videovinkki.tyyppi)
        self.assertEqual(query_result[0].url, self.videovinkki.url)
        self.assertEqual(query_result[0].kommentti, self.videovinkki.kommentti)
        self.assertEqual(len(query_result[0].related_courses), 0)
        self.assertEqual(query_result[0].luettu, self.videovinkki.luettu)
        self.assertFalse(query_result[0].luettu, self.videovinkki.luettu)

    def test_add_new_podcastvinkkit_adds_correct_podcastvinkki_to_db(self):
        self.tmp_db.add_podcast_vinkki_to_db(self.podcastvinkki)
        query_result = self.tmp_db.session.query(PodcastVinkki).all()[0]
        result = self.tmp_db.find_all_vinkit()

        self.assertEqual(len(result), 1)
        self.assertEqual(query_result.author, self.podcastvinkki.author)
        self.assertEqual(query_result.tyyppi , "Podcast")
        self.assertEqual(query_result.nimi , self.podcastvinkki.nimi)
        self.assertEqual(query_result.otsikko , self.podcastvinkki.otsikko)
        self.assertEqual(query_result.kuvaus , self.podcastvinkki.kuvaus)
        self.assertFalse(query_result.luettu)

    def test_add_new_blogpostvinkki_adds_correct_blogpostvinkki_to_db(self):
        self.tmp_db.add_blogpost_vinkki_to_db(self.blogpostvinkki)
        query_result = self.tmp_db.session.query(BlogpostVinkki).all()[0]
        result = self.tmp_db.find_all_vinkit()

        self.assertEqual(len(result), 1)
        self.assertEqual(query_result.author, self.blogpostvinkki.author)
        self.assertEqual(query_result.tyyppi , "Blogpost")
        self.assertEqual(query_result.nimi , self.blogpostvinkki.nimi)
        self.assertEqual(query_result.otsikko , self.blogpostvinkki.otsikko)
        self.assertEqual(query_result.kommentti , self.blogpostvinkki.kommentti)
        self.assertFalse(query_result.luettu)

    # viitteen lisäys vinkille
    def test_course_can_be_added_to_kirjavinkki(self):
        self.tmp_db.add_vinkki_to_db(self.kirjavinkki)
        self.tmp_db.add_course_to_kirjavinkki(self.kirjavinkki.id, self.kurssi)
        query_result = self.tmp_db.session.query(KirjaVinkki).all()
        kurssit = query_result[0].related_courses

        self.assertEqual(kurssit[0].nimi, self.kurssi.nimi)
        self.assertEqual(len(kurssit), 1)
    
    def test_course_can_be_added_to_videovinkki(self):
        self.tmp_db.add_vinkki_to_db(self.videovinkki)
        self.tmp_db.add_course_to_videovinkki(self.videovinkki.id, self.kurssi)
        query_result = self.tmp_db.session.query(VideoVinkki).all()
        kurssit = query_result[0].related_courses

        self.assertEqual(kurssit[0].nimi, self.kurssi.nimi)
        self.assertEqual(len(kurssit), 1)

    def test_course_can_be_added_to_podcastvinkki(self):
        self.tmp_db.add_vinkki_to_db(self.podcastvinkki)
        self.tmp_db.add_course_to_podcastvinkki(self.podcastvinkki.id, self.kurssi)
        query_result = self.tmp_db.session.query(PodcastVinkki).all()
        kurssit = query_result[0].related_courses

        self.assertEqual(kurssit[0].nimi, self.kurssi.nimi)
        self.assertEqual(len(kurssit), 1)

    def test_course_can_be_added_to_blogpostvinkki(self):
        self.tmp_db.add_vinkki_to_db(self.blogpostvinkki)
        self.tmp_db.add_course_to_blogpostvinkki(self.blogpostvinkki.id, self.kurssi)
        query_result = self.tmp_db.session.query(BlogpostVinkki).all()
        kurssit = query_result[0].related_courses

        self.assertEqual(kurssit[0].nimi, self.kurssi.nimi)
        self.assertEqual(len(kurssit), 1)


    def test_tag_can_be_added_to_vinkki(self):
        self.tmp_db.add_vinkki_to_db(self.kirjavinkki)
        self.tmp_db.add_tag_to_vinkki(self.kirjavinkki.id, self.tagi)
        query_result = self.tmp_db.session.query(KirjaVinkki).all()
        tagi = query_result[0].related_tags

        self.assertEqual(tagi[0].nimi, self.tagi.nimi)
        self.assertEqual(len(tagi), 1)

    def test_tag_can_be_added_to_podcastvinkki(self):
        self.tmp_db.add_vinkki_to_db(self.podcastvinkki)
        tagi2 = Tagi(nimi = "tag2")
        self.tmp_db.add_tag_to_podcastvinkki(self.podcastvinkki.id, self.tagi)
        self.tmp_db.add_tag_to_podcastvinkki(self.podcastvinkki.id, tagi2)
        query_result = self.tmp_db.session.query(PodcastVinkki).all()
        tagi = query_result[0].related_tags

        self.assertEqual(tagi[0].nimi, self.tagi.nimi)
        self.assertEqual(tagi[1].nimi, tagi2.nimi)
        self.assertEqual(len(tagi), 2)

    def test_tag_can_be_added_to_blogpostvinkki(self):
        self.tmp_db.add_vinkki_to_db(self.blogpostvinkki)
        tagi2 = Tagi(nimi = "tag2")
        self.tmp_db.add_tag_to_blogpostvinkki(self.blogpostvinkki.id, self.tagi)
        self.tmp_db.add_tag_to_blogpostvinkki(self.blogpostvinkki.id, tagi2)
        query_result = self.tmp_db.session.query(BlogpostVinkki).all()
        tagi = query_result[0].related_tags

        self.assertEqual(tagi[0].nimi, self.tagi.nimi)
        self.assertEqual(tagi[1].nimi, tagi2.nimi)
        self.assertEqual(len(tagi), 2)

    # viitteen tallentuminen
    def test_course_added_to_kirjavinkki_is_saved_to_Kurssit(self):
        self.tmp_db.add_vinkki_to_db(self.kirjavinkki)
        self.kirjavinkki.add_related_course(self.kurssi)
        query_result = self.tmp_db.session.query(Kurssi).all()
        kurssi = query_result[0]

        self.assertEqual(len(query_result), 1)
        self.assertEqual(kurssi.nimi, self.kurssi.nimi)

    def test_course_added_to_kirjavinkki_is_saved_to_kirjavinkki_courses(self):
        self.tmp_db.add_vinkki_to_db(self.kirjavinkki)
        self.kirjavinkki.add_related_course(self.kurssi)
        query_result = self.tmp_db.session.query(kirjavinkki_courses).all()

        self.assertEqual(len(query_result), 1)
        self.assertEqual(query_result[0], (1, self.kirjavinkki.id, self.kurssi.id))


    def test_course_added_to_podcastvinkki_is_added_to_podcastvinkki_courses(self):
        self.tmp_db.add_vinkki_to_db(self.podcastvinkki)
        self.tmp_db.add_course_to_podcastvinkki(self.podcastvinkki.id, self.kurssi)
        query_result = self.tmp_db.session.query(podcastvinkki_courses).all()
        filtered_result = self.tmp_db.session.query(podcastvinkki_courses).filter(podcastvinkki_courses.c.podcastvinkki_id == 1).all()

        self.assertEqual(len(filtered_result), 1)
        self.assertEqual(len(query_result), 1)

    def test_course_added_to_blogpostvinkki_is_added_to_blogpostvinkki_courses(self):
        self.tmp_db.add_vinkki_to_db(self.blogpostvinkki)
        self.tmp_db.add_course_to_blogpostvinkki(self.blogpostvinkki.id, self.kurssi)
        query_result = self.tmp_db.session.query(blogpostvinkki_courses).all()
        filtered_result = self.tmp_db.session.query(blogpostvinkki_courses).filter(blogpostvinkki_courses.c.blogpostvinkki_id == 1).all()

        self.assertEqual(len(filtered_result), 1)
        self.assertEqual(len(query_result), 1)

    def test_tag_added_to_podcastvinkki_is_added_to_podcastvinkki_tagit(self):
        self.tmp_db.add_vinkki_to_db(self.podcastvinkki)
        self.tmp_db.add_course_to_podcastvinkki(self.podcastvinkki.id, self.kurssi)
        query_result = self.tmp_db.session.query(podcastvinkki_courses).all()

        self.assertEqual(len(query_result), 1)

    def test_tag_added_to_blogpostvinkki_is_added_to_blogpostvinkki_tagit(self):
        self.tmp_db.add_vinkki_to_db(self.blogpostvinkki)
        self.tmp_db.add_course_to_blogpostvinkki(self.blogpostvinkki.id, self.kurssi)
        query_result = self.tmp_db.session.query(blogpostvinkki_courses).all()

        self.assertEqual(len(query_result), 1)

    # vinkkien poisto
    def test_delete_vinkki_removes_vinkki_with_correct_tyyppi(self):
        self.tmp_db.add_vinkki_to_db(self.kirjavinkki)
        removed = self.tmp_db.delete_vinkki_with_id(1, VinkkiTyyppi.KIRJA)
        query_result = self.tmp_db.session.query(KirjaVinkki).all()

        self.assertTrue(removed)
        self.assertEqual(len(query_result), 0)

    def test_delete_vinkki_does_nothing_when_given_incorrect_id_and_correct_tyyppi(self):
        self.tmp_db.add_vinkki_to_db(self.kirjavinkki)
        removed = self.tmp_db.delete_vinkki_with_id(15, VinkkiTyyppi.KIRJA)
        query_result = self.tmp_db.session.query(KirjaVinkki).all()

        self.assertFalse(removed)
        self.assertEqual(len(query_result), 1)

    def test_delete_vinkki_returns_false_when_given_incorrect_tyyppi(self):
        self.tmp_db.add_vinkki_to_db(self.kirjavinkki)
        removed = self.tmp_db.delete_vinkki_with_id(1, None)
        self.assertFalse(removed)

    def test_deleting_kirjavinkki_deletes_its_related_courses_from_kirjavinkki_courses(self):
        self.tmp_db.add_vinkki_to_db(self.kirjavinkki)
        self.tmp_db.add_course_to_kirjavinkki(self.kirjavinkki.id, self.kurssi)
        self.tmp_db.delete_vinkki_with_id(self.kirjavinkki.id, VinkkiTyyppi.KIRJA)
        query_result = self.tmp_db.session.query(kirjavinkki_courses).all()

        self.assertEqual(len(query_result), 0)

    def test_deleting_podcastvinkki_deletes_its_related_courses_from_podcastvinkki_courses(self):
        self.tmp_db.add_podcast_vinkki_to_db(self.podcastvinkki)
        self.tmp_db.add_course_to_podcastvinkki(self.podcastvinkki.id, self.kurssi)
        self.tmp_db.delete_vinkki_with_id(self.podcastvinkki.id, VinkkiTyyppi.PODCAST)
        query_result = self.tmp_db.session.query(podcastvinkki_courses).all()

        self.assertEqual(len(query_result), 0)

    def test_deleting_blogpostvinkki_deletes_its_related_courses_from_blogpostvinkki_courses(self):
        self.tmp_db.add_blogpost_vinkki_to_db(self.blogpostvinkki)
        self.tmp_db.add_course_to_blogpostvinkki(self.blogpostvinkki.id, self.kurssi)
        self.tmp_db.delete_vinkki_with_id(self.blogpostvinkki.id, VinkkiTyyppi.BLOG)
        query_result = self.tmp_db.session.query(blogpostvinkki_courses).all()

        self.assertEqual(len(query_result), 0)

    def test_deleting_podcastvinkki_deletes_its_tags_from_podcastvinkki_tagit(self):
        self.tmp_db.add_podcast_vinkki_to_db(self.podcastvinkki)
        self.tmp_db.add_tag_to_podcastvinkki(self.podcastvinkki.id, self.tagi)
        self.tmp_db.delete_vinkki_with_id(self.podcastvinkki.id, VinkkiTyyppi.PODCAST)

        query_result = self.tmp_db.session.query(podcastvinkki_tagit).all()

        self.assertEqual(len(query_result), 0)

    def test_deleting_blogpostvinkki_deletes_its_tags_from_blogpostvinkki_tagit(self):
        self.tmp_db.add_blogpost_vinkki_to_db(self.blogpostvinkki)
        self.tmp_db.add_tag_to_blogpostvinkki(self.blogpostvinkki.id, self.tagi)
        self.tmp_db.delete_vinkki_with_id(self.blogpostvinkki.id, VinkkiTyyppi.BLOG)

        query_result = self.tmp_db.session.query(blogpostvinkki_tagit).all()

        self.assertEqual(len(query_result), 0)

    # queryt
    def test_query_with_id_returns_correct_kirja_obect(self):
        pass

    def test_query_with_id_returns_correct_video_obect(self):
        pass

    def test_query_with_nonexisting_id_results_none(self):
        pass

    def tearDown(self):
        os.remove("tmp123db.db")