from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.schema import ForeignKey

base = declarative_base()  # pylint: disable=redefined-outer-name

vinkki_courses = Table('vinkki_courses', base.metadata,
     Column('id', Integer, primary_key=True),
     Column('vinkki_id', ForeignKey('kirjavinkit.id')),
     Column('kurssi_id', ForeignKey('kurssit.id'))
 )

class Kurssi(base):
    __tablename__= 'kurssit'
    id = Column(Integer, primary_key=True)
    nimi = Column(String, nullable= false)
    def __str__(self) -> str:
        return self.nimi

class KirjaVinkki(base):
    __tablename__ = 'kirjavinkit'
    id = Column(Integer, primary_key=True)
    otsikko = Column(String, nullable= false)
    kirjoittaja = Column(String)
    tyyppi = Column(String, nullable= false)
    kommentti = Column(String, nullable= false)
    related_courses = relationship('Kurssi', secondary=vinkki_courses, backref='vinkit')

    def add_related_course(self, kurssi: Kurssi):
        self.related_courses.append(kurssi)

    def __str__(self) -> str:
        kurssit = self.related_courses
        kurssit_listana = []
        for kurssi in kurssit:
            kurssit_listana.append(kurssi.nimi)
        kurssit_str = ' ,'.join(kurssit_listana)

        return f'\n otsikko: {self.otsikko} \nKommentti: {self.kommentti}\n liittyvät kurssit: {kurssit_str}'
