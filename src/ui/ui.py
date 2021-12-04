from models import KirjaVinkki


class Ui:
    def __init__(self, io, db):
        self.io = io
        self.db = db


    def start(self):
        self.io.write('Tervetuloa käyttämään Lukuvinkki-sovellusta \n')
        self.print_options()

    def print_options(self):
        while True:
            self.io.write('Valitse toiminto: ')
            self.io.write('1: Listaa lukuvinkit')
            self.io.write('2: Lisää lukuvinkki')
            self.io.write('3: Poista lukuvinkki')
            self.io.write('4: Lopeta')
            user_input = self.process_command(self.io.read_input('Anna komento: '))
            print()

            if user_input == 1:
                self.print_vinkit()
            if user_input == 2:
                otsikko = self.io.read_input('Vinkin otsikko: ')
                kommentti = self.io.read_input('Kommentti: ')
                self.add_new(otsikko, kommentti)
            if user_input == 3:
                self.delete_vinkki()
            if user_input == 4:
                self.io.write('Kiitos ja näkemiin!')
                break
            print()

    def process_command(self, command):
        try:
            user_input = int(command)
            return user_input
        except ValueError:
            self.io.write('Anna kelvollinen komento')

    def add_new(self, otsikko, kommentti):
        vinkki = KirjaVinkki(otsikko = otsikko, kommentti = kommentti)
        self.db.add_vinkki_to_db(kirja = vinkki)

    def print_vinkit(self):
        vinkit = self.db.find_all_vinkit()
        self.io.write('Tallennetut lukuvinkit:\n')
        for vinkki in vinkit:
            self.io.write(f'{vinkki}\n')

    def delete_vinkki(self):
        self.io.write('Anna poistettavan vinkin id:\n')
        self.print_vinkit_with_id()
        user_input = self.process_command(self.io.read_input('Poistettavan vinkin id: '))

        if isinstance(user_input, int):
            if self.db.delete_vinkki_with_id(user_input):
                self.io.write(f'Vinkki id {user_input} poistettu')
            else:
                self.io.write('Vinkin poistaminen epäonnistui')

    def print_vinkit_with_id(self):
        vinkit = self.db.find_all_vinkit()
        for vinkki in vinkit:
            self.io.write(f'id: {vinkki.id} {vinkki}\n')
