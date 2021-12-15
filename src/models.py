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
     Column('videovinkki1_id', ForeignKey('videovinkit.id')),
     Column('kurssi1_id', ForeignKey('kurssit.id'))
)

podcastvinkki_courses = Table('podcastvinkki_courses', base.metadata,
     Column('id', Integer, primary_key=True),
     Column('podcastvinkki_id', ForeignKey('podcastvinkit.id')),
     Column('kurssi_id', ForeignKey('kurssit.id'))
)

blogpostvinkki_courses = Table('blogpostvinkki_courses', base.metadata,
     Column('id', Integer, primary_key=True),
     Column('blogpostvinkki_id', ForeignKey('blogpostvinkit.id')),
     Column('kurssi_id', ForeignKey('kurssit.id'))
)

kirjavinkki_tagit = Table('kirjavinkki_tagit', base.metadata, 
        Column('id', Integer, primary_key=True),
        Column('kirjavinkki2_id',ForeignKey('kirjavinkit.id')),
        Column('tagi2_id', ForeignKey('tagit.id'))
)

videovinkki_tagit = Table('videovinkki_tagit', base.metadata,
        Column('id', Integer, primary_key=True),
        Column('videovinkki_id',ForeignKey('videovinkit.id')),
        Column('tagi_id', ForeignKey('tagit.id'))
)

podcastvinkki_tagit = Table('podcastvinkki_tagit', base.metadata,
        Column('id', Integer, primary_key=True),
        Column('podcastvinkki_id',ForeignKey('podcastvinkit.id')),
        Column('tagi_id', ForeignKey('tagit.id'))
)

blogpostvinkki_tagit = Table('blogpostvinkki_tagit', base.metadata,
        Column('id', Integer, primary_key=True),
        Column('blogpostvinkki_id',ForeignKey('blogpostvinkit.id')),
        Column('tagi_id', ForeignKey('tagit.id'))
)

class Tagi(base):
    __tablename__= 'tagit'
    id = Column(Integer, primary_key= True)
    nimi = Column(String, nullable= false)
    def __str__(self) -> str:
        return self.nimi

class Kurssi(base):
    __tablename__= 'kurssit'
    id = Column(Integer, primary_key=True)
    nimi = Column(String, nullable= false)
    def __str__(self) -> str:
        return self.nimi

class KirjaVinkki(base):
    __tablename__ = 'kirjavinkit'
    related_courses = relationship(
        'Kurssi', secondary=kirjavinkki_courses, backref='kirjavinkit')
    related_tags = relationship(
        'Tagi', secondary=kirjavinkki_tagit, backref='kirjavinkit')
    id = Column(Integer, primary_key=True)
    otsikko = Column(String, nullable= false)
    kirjoittaja = Column(String)
    isbn = Column(String)
    tyyppi = Column(String, nullable= false, default="Kirja")
    kommentti = Column(String, nullable= false)
    luettu = Column(Boolean, nullable= false, default=False)


    def add_related_course(self, kurssi: Kurssi):
        self.related_courses.append(kurssi)

    def __str__(self) -> str:
        kurssit = self.related_courses
        kurssit_listana = []
        for kurssi in kurssit:
            kurssit_listana.append(kurssi.nimi)
        kurssit_str = ' ,'.join(kurssit_listana)
        tagit = self.related_tags
        tagit_listana = []
        for tagi in tagit:
            tagit_listana.append(tagi.nimi)
        tagit_str = ','.join(tagit_listana)

        return f'\nOtsikko: {self.otsikko}\nTyyppi: {self.tyyppi}\nKommentti: {self.kommentti}\nLiittyvät kurssit: {kurssit_str}\nTyyppi: {self.tyyppi}\nLuettu: {self.luettu}\nTagit: {tagit_str}'


class VideoVinkki(base):
    __tablename__ = 'videovinkit'
    id = Column(Integer, primary_key=True)
    otsikko = Column(String, nullable= false)
    url = Column(String)
    tyyppi = Column(String, nullable= false, default="Video")
    kommentti = Column(String, nullable= false)
    related_courses = relationship('Kurssi', secondary=videovinkki_courses, backref='kurssit')
    related_tags = relationship('Tagi', secondary = videovinkki_tagit, backref='videovinkit')
    luettu = Column(Boolean, nullable= false, default=False)

    def add_related_course(self, kurssi: Kurssi):
        self.related_courses.append(kurssi)

    def __str__(self) -> str:
        kurssit = self.related_courses
        kurssit_listana = []
        for kurssi in kurssit:
            kurssit_listana.append(kurssi.nimi)
        kurssit_str = ' ,'.join(kurssit_listana)

        return f'\nOtsikko: {self.otsikko}\nTyyppi: {self.tyyppi}\nKommentti: {self.kommentti}\nLiittyvät kurssit: {kurssit_str}\nLuettu: {self.luettu}'

class PodcastVinkki(base):
    __tablename__ = 'podcastvinkit'
    id = Column(Integer, primary_key=True)
    author = Column(String, nullable=False)
    nimi = Column(String, nullable=False)
    otsikko = Column(String, nullable=False)
    kuvaus = Column(String, nullable=False)
    tyyppi = Column(String, nullable=False, default="Podcast")
    related_tags = relationship(
        'Tagi', secondary=podcastvinkki_tagit, backref='podcastvinkit')
    related_courses = relationship(
        'Kurssi', secondary=podcastvinkki_courses, backref='podcastvinkit')
    luettu = Column(Boolean, nullable=False, default=False)


    def add_related_course(self, kurssi: Kurssi):
        self.related_courses.append(kurssi)

    def __str__(self) -> str:
        kurssit = self.related_courses
        kurssit_listana = []
        for kurssi in kurssit:
            kurssit_listana.append(kurssi.nimi)
        kurssit_str = ' ,'.join(kurssit_listana)
        tagit = self.related_tags
        tagit_listana = []
        for tagi in tagit:
            tagit_listana.append(tagi.nimi)
        tagit_str = ','.join(tagit_listana)

        return f'\nAuthor: {self.author}\nPodcastin nimi: {self.nimi}\nOtsikko: {self.otsikko}\nKuvaus: {self.kuvaus}\nTyyppi: {self.tyyppi}\nTagit: {tagit_str}\nLiittyvät kurssit: {kurssit_str}\nLuettu: {self.luettu}'


class BlogpostVinkki(base):
    __tablename__ = 'blogpostvinkit'
    id = Column(Integer, primary_key=True)
    author = Column(String, nullable=False)
    nimi = Column(String, nullable=False)
    otsikko = Column(String, nullable=False)
    kommentti = Column(String, nullable=False)
    tyyppi = Column(String, nullable=False, default="Blogpost")
    related_tags = relationship(
        'Tagi', secondary=blogpostvinkki_tagit, backref='blogpostvinkit')
    related_courses = relationship(
        'Kurssi', secondary=blogpostvinkki_courses, backref='blogpostvinkit')
    luettu = Column(Boolean, nullable=False, default=False)


    def add_related_course(self, kurssi: Kurssi):
        self.related_courses.append(kurssi)

    def __str__(self) -> str:
        kurssit = self.related_courses
        kurssit_listana = []
        for kurssi in kurssit:
            kurssit_listana.append(kurssi.nimi)
        kurssit_str = ' ,'.join(kurssit_listana)
        tagit = self.related_tags
        tagit_listana = []
        for tagi in tagit:
            tagit_listana.append(tagi.nimi)
        tagit_str = ','.join(tagit_listana)

        return f'\nAuthor: {self.author}\nBlogpostin nimi: {self.nimi}\nOtsikko: {self.otsikko}\nKommentti: {self.kommentti}\nTyyppi: {self.tyyppi}\nTagit: {tagit_str}\nLiittyvät kurssit: {kurssit_str}\nLuettu: {self.luettu}'

