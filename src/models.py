from typing import List
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Table, Text
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()

vinkki_courses = Table('post_keywords', Base.metadata,
     Column('kirjavinkit', ForeignKey('kirjavinkit.id'), primary_key=True),
     Column('kurssit', ForeignKey('kurssit.id'), primary_key=True)
 )

class Kurssi(Base):
    __tablename__= 'kurssit'
    id = Column(Integer, primary_key=True)
    kurssin_nimi: Column(String, nullable= false)
    vinkit = relationship('KirjaVinkki',
                                    secondary="vinkki_courses",
                                    back_populates="related_courses")

class KirjaVinkki(Base):
    __tablename__ = 'kirjavinkit'
    id = Column(Integer, primary_key=True)
    otsikko = Column(String, nullable= false)
    kirjoittaja = Column(String)
    tyyppi = Column(String, nullable= false)

    related_courses = relationship('Kurssi',
                                    secondary="vinkki_courses",
                                    back_populates="vinkit")

    def add_related_course(self, kurssi: Kurssi):
        self.related_courses.append(kurssi)

    def __str__(self) -> str:
        return f'Otsikko: {self.otsikko} Kirjoittaja: {self.kirjoittaja} Related courses: {self.related_courses}'

