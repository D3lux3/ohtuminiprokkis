from models import KirjaVinkki, VideoVinkki, Kurssi




class Ui:
    def __init__(self, io, db, random_int):
        self.io = io
        self.db = db
        self.number_generator = random_int


    def start(self):
        self.io.write('Tervetuloa käyttämään Lukuvinkki-sovellusta \n')
        self.print_options()

    def print_options(self):
        while True:
            self.io.write('Valitse toiminto: ')
            self.io.write('1: Listaa lukuvinkit')
            self.io.write('2: Lisää lukuvinkki')
            self.io.write('3: Poista lukuvinkki')
            self.io.write('4: Valitse satunnainen lukuvinkki')
            self.io.write('5: Lopeta')
            user_input = self.process_command(self.io.read_input('Anna komento: '))
            print()

            if user_input == 1:
                self.print_vinkit()
            elif user_input == 2:
                self.io.write('Valitse vinkin tyyppi:\n1: Kirjalukuvinkki\n2: Videolukuvinkki\n')
                tyyppi = self.process_command(self.io.read_input('Anna komento: '))

                if tyyppi == 1:
                    self.add_new_kirjavinkki()
                elif tyyppi == 2:
                    self.add_new_videovinkki()
            elif user_input == 3:
                self.delete_vinkki()
            elif user_input == 4:
                self.random_vinkki()
            elif user_input == 5:
                self.io.write('Kiitos ja näkemiin!')
                break
            print()

    def process_command(self, command):
        try:
            user_input = int(command)
            return user_input
        except ValueError:
            return self.io.write('Anna kelvollinen komento')

    def add_new_kirjavinkki(self):
        kirjoittaja = input('Vinkin kirjoittaja: ')
        otsikko = input('Vinkin otsikko: ')
        isbn = input('Kirjan isbn-koodi: ')
        vinkki = KirjaVinkki(kirjoittaja = kirjoittaja, otsikko = otsikko, isbn = isbn)
        self.db.add_vinkki_to_db(kirja = vinkki)

    def add_new_videovinkki(self):
        otsikko = input('Vinkin otsikko: ')
        url = input('Videon url-osoite: ')
        kommentti = input('Vinkin kommentti: ')
        vinkki = VideoVinkki(otsikko = otsikko, url = url, kommentti = kommentti)
        self.db.add_video_vinkki_to_db(kirja = vinkki)

    def print_vinkit(self):
        vinkit = self.db.find_all_vinkit()
        self.io.write('Tallennetut lukuvinkit:\n')
        for vinkki in vinkit:
            self.io.write(f'{str(vinkki)}\n')

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

    def random_vinkki(self):
        vinkit = self.db.find_all_vinkit()
        random_number = self.number_generator(len(vinkit)-1)
        vinkki = vinkit[random_number]
        self.io.write(vinkki)
