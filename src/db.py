from typing import List
from models import KirjaVinkki, Base, Kurssi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class db:
    def __init__(self, db_name: str, Base):
        self.engine = create_engine('sqlite:///' + db_name + ".db")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)

    def add_vinkki_to_db(self, kirja: KirjaVinkki):
        """Lisää kirjavinkin tietokantaan."""
        self.session.add(kirja)
        self.session.commit()

    def find_all_vinkit(self) -> List[KirjaVinkki]:
        """Hakee kaikki kirjavinkit tietokannasta, ja palauttaa ne listana."""
        return self.session.query(KirjaVinkki).all()



database = db("tietokanta", Base)

vinggi = KirjaVinkki(otsikko = "Hello World", kirjoittaja = "Dani")
vinggi.related_courses.append(Kurssi("TKT20006 Ohjelmistotuotanto"))
database.add_vinkki_to_db()

for kirjavinkki in database.find_all_vinkit():
    print(kirjavinkki)