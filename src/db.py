from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import KirjaVinkki, Kurssi, VideoVinkki, Tagi
from vinkkityyppi import VinkkiTyyppi

class DataBase:
    def __init__(self, db_name: str, base):
        self.engine = create_engine('sqlite:///' + db_name + ".db")#, echo=True)
        session = sessionmaker(bind=self.engine)
        self.session = session()
        base.metadata.create_all(self.engine)

    def add_vinkki_to_db(self, kirja: KirjaVinkki):
        """Lisää kirjavinkin tietokantaan."""
        self.session.add(kirja)
        self.session.commit()

    def add_video_vinkki_to_db(self, kirja: VideoVinkki):
        """Lisää videovinkki tietokantaan."""
        self.session.add(kirja)
        self.session.commit()

    def add_course_to_kirjavinkki(self, vinkin_id: int, kurssi: Kurssi):
        vinkki = self.session.query(KirjaVinkki).get(vinkin_id)
        vinkki.related_courses.append(kurssi)
        self.session.commit()
        
    def add_course_to_videovinkki(self, vinkin_id: int, kurssi: Kurssi):
        vinkki = self.session.query(VideoVinkki).get(vinkin_id)
        vinkki.related_courses.append(kurssi)
        self.session.commit()

    def add_tag_to_vinkki(self, vinkin_id: int, tagi: Tagi):
        vinkki = self.session.query(KirjaVinkki).get(vinkin_id)
        vinkki.related_tags.append(tagi)
        self.session.commit()

    def find_all_vinkit(self) -> List:
        """Hakee kaikki kirjavinkit tietokannasta, ja palauttaa ne listana."""
        kaikki_vinkit = []
        kaikki_vinkit.extend(self.session.query(KirjaVinkki).all())
        kaikki_vinkit.extend(self.session.query(VideoVinkki).all())
        return kaikki_vinkit

    def delete_vinkki_with_id(self, vinkin_id: int, vinkin_tyyppi: VinkkiTyyppi):
        """Poistaa vinkin id perusteella"""
        query_result = self.query_with_id(vinkin_id, vinkin_tyyppi)
        if query_result is not None:
            self.session.delete(query_result)
            self.session.commit()
            return True

        return False

    def query_with_id(self, vinkin_id: int, vinkin_tyyppi: VinkkiTyyppi):
        """Hakee vinkin id perusteella"""
        query_result = None
        if vinkin_tyyppi == VinkkiTyyppi.KIRJA:
            query_result = self.session.query(KirjaVinkki).get(vinkin_id)
        elif vinkin_tyyppi == VinkkiTyyppi.VIDEO:
            query_result = self.session.query(VideoVinkki).get(vinkin_id)
        return query_result
