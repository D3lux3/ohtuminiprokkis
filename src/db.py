from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import KirjaVinkki, Kurssi, PodcastVinkki, VideoVinkki, BlogpostVinkki, Tagi
from vinkkityyppi import VinkkiTyyppi


class DataBase:
    def __init__(self, db_name: str, base):
        self.engine = create_engine(
            'sqlite:///' + db_name + ".db")  # , echo=True)
        session = sessionmaker(bind=self.engine)
        self.session = session()
        base.metadata.create_all(self.engine)

    def add_vinkki_to_db(self, kirja: KirjaVinkki):
        """Lisää kirjavinkin tietokantaan."""
        self.session.add(kirja)
        self.session.commit()

    def add_video_vinkki_to_db(self, video: VideoVinkki):
        """Lisää videovinkki tietokantaan."""
        self.session.add(video)
        self.session.commit()

    def add_podcast_vinkki_to_db(self, podcast: PodcastVinkki):
        """Lisää podcastvinkki tietokantaan."""
        self.session.add(podcast)
        self.session.commit()

    def add_blogpost_vinkki_to_db(self, blogpost: BlogpostVinkki):
        """Lisää blogpostvinkki tietokantaan."""
        self.session.add(blogpost)
        self.session.commit()

    def add_course_to_kirjavinkki(self, vinkin_id: int, kurssi: Kurssi):
        vinkki = self.session.query(KirjaVinkki).get(vinkin_id)
        vinkki.related_courses.append(kurssi)
        self.session.commit()

    def add_course_to_videovinkki(self, vinkin_id: int, kurssi: Kurssi):
        vinkki = self.session.query(VideoVinkki).get(vinkin_id)
        vinkki.related_courses.append(kurssi)
        self.session.commit()

    def add_course_to_podcastvinkki(self, vinkin_id: int, kurssi: Kurssi):
        vinkki = self.session.query(PodcastVinkki).get(vinkin_id)
        vinkki.related_courses.append(kurssi)
        self.session.commit()

    def add_course_to_blogpostvinkki(self, vinkin_id: int, kurssi: Kurssi):
        vinkki = self.session.query(BlogpostVinkki).get(vinkin_id)
        vinkki.related_courses.append(kurssi)
        self.session.commit()

    def add_tag_to_vinkki(self, vinkin_id: int, tagi: Tagi):
        vinkki = self.session.query(KirjaVinkki).get(vinkin_id)
        vinkki.related_tags.append(tagi)
        self.session.commit()

    def add_tag_to_podcastvinkki(self, vinkin_id: int, tagi: Tagi):
        vinkki = self.session.query(PodcastVinkki).get(vinkin_id)
        vinkki.related_tags.append(tagi)
        self.session.commit()

    def add_tag_to_blogpostvinkki(self, vinkin_id: int, tagi: Tagi):
        vinkki = self.session.query(BlogpostVinkki).get(vinkin_id)
        vinkki.related_tags.append(tagi)
        self.session.commit()

    def add_tag_to_videovinkki(self, vinkin_id: int, tagi: Tagi):
        vinkki = self.session.query(VideoVinkki).get(vinkin_id)
        vinkki.related_tags.append(tagi)
        self.session.commit()

    def find_all_vinkit(self) -> List:
        """Hakee kaikki kirjavinkit tietokannasta, ja palauttaa ne listana."""
        kaikki_vinkit = []
        kaikki_vinkit.extend(self.session.query(KirjaVinkki).all())
        kaikki_vinkit.extend(self.session.query(VideoVinkki).all())
        kaikki_vinkit.extend(self.session.query(PodcastVinkki).all())
        kaikki_vinkit.extend(self.session.query(BlogpostVinkki).all())
        return kaikki_vinkit

    def delete_vinkki_with_id(self, vinkin_id: int, vinkin_tyyppi: VinkkiTyyppi):
        """Poistaa vinkin id perusteella"""
        query_result = self.query_with_id(vinkin_id, vinkin_tyyppi)
        if query_result is not None:
            self.session.delete(query_result)
            self.session.commit()
            return True

        return False

    def find_all_vinkit_with_type(self, vinkin_tyyppi) -> List:
        kaikki_vinkit = []
        if vinkin_tyyppi == VinkkiTyyppi.KIRJA:
            kaikki_vinkit.extend(self.session.query(KirjaVinkki).all())
        elif vinkin_tyyppi == VinkkiTyyppi.VIDEO:
            kaikki_vinkit.extend(self.session.query(VideoVinkki).all())
        elif vinkin_tyyppi == VinkkiTyyppi.PODCAST:
            kaikki_vinkit.extend(self.session.query(PodcastVinkki).all())
        elif vinkin_tyyppi == VinkkiTyyppi.BLOG:
            kaikki_vinkit.extend(self.session.query(BlogpostVinkki).all())
        return kaikki_vinkit

    def query_with_id(self, vinkin_id: int, vinkin_tyyppi: VinkkiTyyppi):
        """Hakee vinkin id perusteella"""
        query_result = None
        if vinkin_tyyppi == VinkkiTyyppi.KIRJA:
            query_result = self.session.query(KirjaVinkki).get(vinkin_id)
        elif vinkin_tyyppi == VinkkiTyyppi.VIDEO:
            query_result = self.session.query(VideoVinkki).get(vinkin_id)
        elif vinkin_tyyppi == VinkkiTyyppi.PODCAST:
            query_result = self.session.query(PodcastVinkki).get(vinkin_id)
        elif vinkin_tyyppi == VinkkiTyyppi.BLOG:
            query_result = self.session.query(BlogpostVinkki).get(vinkin_id)
        return query_result

    def search_vinkki_by_tag(self, tagin_id):
        """Hakee vinkit tagin id:n perusteella"""
        tagi  = self.session.query(Tagi).get(tagin_id)
        vinkit = []
        vinkit.extend(tagi.kirjavinkit)
        vinkit.extend(tagi.videovinkit)
        vinkit.extend(tagi.podcastvinkit)
        vinkit.extend(tagi.blogpostvinkit)
        return vinkit

    def find_all_tagit(self):
        """Hakee tagit

        Returns:
            List
        """
        return self.session.query(Tagi).all()

