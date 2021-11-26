from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import false

Base = declarative_base()

class KirjaVinkki(Base):
    __tablename__ = 'kirjavinkit'
    id = Column(Integer, primary_key=True)
    otsikko = Column(String, nullable= false)
    kirjoittaja = Column(String)


    def __str__(self) -> str:
        return f'Otsikko: {self.otsikko} Kirjoittaja: {self.kirjoittaja}'