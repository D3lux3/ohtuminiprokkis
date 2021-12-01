from db import db
from models import KirjaVinkki, Base

class Ui:

    def __init__(self, io):
        self.io = io
        self.db = db("tietokanta", Base)


    def start(self):
        self.io.write('Tervetuloa käyttämään Lukuvinkki-sovellusta \n')
        self.print_options()

    def print_options(self):
        while True:
            self.io.write('Valitse toiminto: ')
            self.io.write('1: Hae lukuvinkki')
            self.io.write('2: Lisää lukuvinkki')
            self.io.write('3: Lopeta')
            user_input = self.process_command(self.io.read_input('Anna komento: '))
            if user_input == 2:
                otsikko = self.io.read_input('Vinkin otsikko: ')
                kommentti = self.io.read_input('Kommentti: ')
                self.add_new(otsikko, kommentti)
            if user_input == 3:
                break

    def process_command(self, command):
        try:
            user_input = int(command)
            return user_input
        except ValueError:
            self.io.write('Anna kelvollinen komento')
        print()

    def add_new(self, otsikko, kommentti):
        vinkki = KirjaVinkki(otsikko = otsikko, kommentti = kommentti)
        self.db.add_vinkki_to_db(kirja = vinkki)
