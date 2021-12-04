from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import KirjaVinkki, Kurssi


class DataBase:
    def __init__(self, db_name: str, base):
        self.engine = create_engine('sqlite:///' + db_name + ".db")
        session = sessionmaker(bind=self.engine)
        self.session = session()
        base.metadata.create_all(self.engine)

    def add_vinkki_to_db(self, kirja: KirjaVinkki):
        """Lisää kirjavinkin tietokantaan."""
        self.session.add(kirja)
        self.session.commit()

    def add_course_to_vinkki(self, vinkin_id: int, kurssi: Kurssi):
        vinkki = self.session.query(KirjaVinkki).get(vinkin_id)
        vinkki.related_courses.append(kurssi)
        self.session.commit()

    def find_all_vinkit(self) -> List[KirjaVinkki]:
        """Hakee kaikki kirjavinkit tietokannasta, ja palauttaa ne listana."""
        return self.session.query(KirjaVinkki).all()
