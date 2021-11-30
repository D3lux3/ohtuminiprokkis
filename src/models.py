from typing import List
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Table, Text
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()

vinkki_courses = Table('vinkki_courses', Base.metadata,
     Column('id', Integer, primary_key=True),
     Column('vinkki_id', ForeignKey('kirjavinkit.id')),
     Column('kurssi_id', ForeignKey('kurssit.id'))
 )

class Kurssi(Base):
    __tablename__= 'kurssit'
    id = Column(Integer, primary_key=True)
    nimi = Column(String, nullable= false)
    def __str__(self) -> str:
        return self.nimi

class KirjaVinkki(Base):
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
        
        return f'otsikko: {self.otsikko} \nKommentti: {self.kommentti}'

