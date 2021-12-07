from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean

base = declarative_base()  # pylint: disable=redefined-outer-name

kirjavinkki_courses = Table('kirjavinkki_courses', base.metadata,
     Column('id', Integer, primary_key=True),
     Column('kirjavinkki_id', ForeignKey('kirjavinkit.id')),
     Column('kurssi_id', ForeignKey('kurssit.id'))
 )

videovinkki_courses = Table('videovinkki_courses', base.metadata,
     Column('id', Integer, primary_key=True),
     Column('videovinkki_id', ForeignKey('videovinkit.id')),
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
    isbn = Column(String)
    tyyppi = Column(String, nullable= false, default="Kirja")
    kommentti = Column(String, nullable= false)
    related_courses = relationship('Kurssi', secondary=kirjavinkki_courses, backref='vinkit')
    luettu = Column(Boolean, nullable= false, default=False)


    def add_related_course(self, kurssi: Kurssi):
        self.related_courses.append(kurssi)

    def __str__(self) -> str:
        kurssit = self.related_courses
        kurssit_listana = []
        for kurssi in kurssit:
            kurssit_listana.append(kurssi.nimi)
        kurssit_str = ' ,'.join(kurssit_listana)

        return f'\nOtsikko: {self.otsikko}\nTyyppi: {self.tyyppi}\nKommentti: {self.kommentti}\nLiittyvät kurssit: {kurssit_str}\nTyyppi: {self.tyyppi}\nLuettu: {self.luettu}'


class VideoVinkki(base):
    __tablename__ = 'videovinkit'
    id = Column(Integer, primary_key=True)
    otsikko = Column(String, nullable= false)
    url = Column(String)
    tyyppi = Column(String, nullable= false, default="Video")
    kommentti = Column(String, nullable= false)
    related_courses = relationship('Kurssi', secondary=videovinkki_courses, backref='kurssit')
    luettu = Column(Boolean, nullable= false, default=False)

    def add_related_course(self, kurssi: Kurssi):
        self.related_courses.append(kurssi)

    def __str__(self) -> str:
        kurssit = self.related_courses
        kurssit_listana = []
        for kurssi in kurssit:
            kurssit_listana.append(kurssi.nimi)
        kurssit_str = ' ,'.join(kurssit_listana)

        return f'\nOtsikko: {self.otsikko}\nTyyppi: {self.tyyppi} \nKommentti: {self.kommentti}\nLiittyvät kurssit: {kurssit_str}\nLuettu: {self.luettu}'
