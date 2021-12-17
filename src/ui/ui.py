from models import KirjaVinkki, PodcastVinkki, VideoVinkki, BlogpostVinkki, Kurssi, Tagi
from vinkkityyppi import VinkkiTyyppi


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
            self.io.write('5: Hae tagin perusteella')
            self.io.write('0: Lopeta')
            user_input = self.process_command(self.io.read_input('Anna komento: '))
            self.io.write('')

            if user_input == 1:
                self.print_vinkit()
            elif user_input == 2:
                self.choose_type()
            elif user_input == 3:
                self.delete_vinkki()
            elif user_input == 4:
                self.random_vinkki()
            elif user_input == 5:
                self.search_by_tag()
            elif user_input == 0:
                self.io.write('Kiitos ja näkemiin!')
                break
            else:
                self.io.write('Virheellinen syöte')
            self.io.write('')

    def process_command(self, command):
        try:
            user_input = int(command)
            return user_input
        except ValueError:
            return self.io.write('Anna kelvollinen komento')

    def choose_type(self):
        while True:
            self.io.write(
                'Valitse vinkin tyyppi:\n1: Kirjalukuvinkki\n2: Videolukuvinkki\n3: Podcastlukuvinkki\n4: Blogpostvinkki\n5: Palaa päävalikkoon')
            tyyppi = self.process_command(self.io.read_input('Anna komento: '))

            if tyyppi == 1:
                self.add_new_kirjavinkki()
            elif tyyppi == 2:
                self.add_new_videovinkki()
            elif tyyppi == 3:
                self.add_new_podcastvinkki()
            elif tyyppi == 4:
                self.add_new_blogpostvinkki()
            elif tyyppi == 5:
                pass
            else:
                self.io.write('Virheellinen syöte')
                print()
                continue
            break

    def min_information(self, message: str):
        while True:
            user_input = self.io.read_input(message)
            if user_input:
                return user_input
            else:
                self.io.write("tämä on pakollinen tieto")

    def add_new_kirjavinkki(self):
        kirjoittaja = self.min_information('Vinkin kirjoittaja: ')
        otsikko = self.min_information('Kirjan nimi: ')
        isbn = self.io.read_input('Kirjan isbn-koodi: ')
        kommentti = self.io.read_input('Vinkin kommentti: ')
        vinkki = KirjaVinkki(kirjoittaja=kirjoittaja,
                             otsikko=otsikko, isbn=isbn, kommentti=kommentti)
        self.db.add_vinkki_to_db(kirja=vinkki)
        vinkki_id = vinkki.id
        self.add_tags_kirjavinkki(vinkki_id)
        self.add_courses_kirja(vinkki_id)

    def print_all_vinkit(self):
        vinkit = self.db.find_all_vinkit()
        self.io.write('Tallennetut lukuvinkit:\n')
        for vinkki in vinkit:
            self.io.write(f'{str(vinkki)}\n')


    def print_vinkit(self):
        self.ask_for_type()

    def ask_for_type(self) -> VinkkiTyyppi:
        while True:
            self.io.write('Valitse tyyppi: ')
            self.io.write('1: Listaa Kirjavinkit')
            self.io.write('2: Listaa Videovinkit')
            self.io.write('3: Listaa Podcastvinkit')
            self.io.write('4: Listaa Blogivinkit')
            self.io.write('5: Listaa kaikki vinkit')
            self.io.write('6: Palaa päävalikkoon')
            tyyppi = self.process_command(self.io.read_input('Anna komento: '))

            if tyyppi == 1:
                self.print_vinkit_with_type(VinkkiTyyppi.KIRJA)
            elif tyyppi == 2:
                self.print_vinkit_with_type(VinkkiTyyppi.VIDEO)
            elif tyyppi == 3:
                self.print_vinkit_with_type(VinkkiTyyppi.PODCAST)
            elif tyyppi == 4:
                self.print_vinkit_with_type(VinkkiTyyppi.BLOG)
            elif tyyppi == 5:
                self.print_all_vinkit()
            elif tyyppi == 6:
                pass
            else:
                self.io.write('Virheellinen syöte')
                print()
                continue
            break
        

    def print_vinkit_with_type(self, vinkkityyppi):
        vinkit = self.db.find_all_vinkit_with_type(vinkkityyppi)
        self.io.write('Vinkit:\n')
    
        for vinkki in vinkit:
            self.io.write(f'{str(vinkki)}\n')

    def add_new_videovinkki(self):
        otsikko = self.min_information('Vinkin otsikko: ')
        url = self.min_information('Videon url-osoite: ')
        kommentti = self.io.read_input('Vinkin kommentti: ')
        vinkki = VideoVinkki(otsikko = otsikko, url = url, kommentti = kommentti)
        self.db.add_video_vinkki_to_db(video = vinkki)
        vinkki_id = vinkki.id
        self.add_tags_videovinkki(vinkki_id)
        self.add_courses_video(vinkki_id)

    def add_new_podcastvinkki(self):
        author = self.io.read_input('Author: ')
        nimi = self.min_information('Podcastin nimi: ')
        otsikko = self.min_information('Otsikko: ')
        kuvaus = self.min_information('Kuvaus: ')
        vinkki = PodcastVinkki(author = author, nimi = nimi, otsikko = otsikko, kuvaus = kuvaus)
        self.db.add_podcast_vinkki_to_db(podcast = vinkki)
        vinkki_id = vinkki.id
        self.add_tags_podcastvinkki(vinkki_id)
        self.add_courses_podcast(vinkki_id)

    def add_new_blogpostvinkki(self):
        author = self.io.read_input('Author: ')
        nimi = self.io.read_input('Blogpostin nimi: ')
        otsikko = self.min_information('Otsikko: ')
        kommentti = self.io.read_input('Kommentti: ')
        url = self.min_information('url-osoite: ')
        vinkki = BlogpostVinkki(author = author, nimi = nimi, otsikko = otsikko, kommentti = kommentti, url=url)
        self.db.add_blogpost_vinkki_to_db(blogpost = vinkki)
        vinkki_id = vinkki.id
        self.add_tags_blogpostvinkki(vinkki_id)
        self.add_courses_blogpost(vinkki_id)

    def add_tags_kirjavinkki(self, vinkki_id):
        while True:
            valinta = self.process_command(self.io.read_input(f"Haluatko lisätä vinkille uuden tagin?\n1: Kyllä\n2: Ei\n"))
            if valinta == 1:
                teksti = self.io.read_input("Tagi: ")
                self.db.add_tag_to_vinkki(vinkki_id, Tagi(nimi = teksti))
            elif valinta == 2:
                break
            else:
                self.io.write('Virheellinen syöte')

    def add_tags_videovinkki(self, vinkki_id):
        while True:
            valinta = self.process_command(self.io.read_input(f"Haluatko lisätä vinkille uuden tagin?\n1: Kyllä\n2: Ei\n"))
            if valinta == 1:
                teksti = self.io.read_input("Tagi: ")
                self.db.add_tag_to_videovinkki(vinkki_id, Tagi(nimi=teksti))
            elif valinta == 2:
                break
            else:
                self.io.write('Virheellinen syöte')

    def add_tags_podcastvinkki(self, vinkki_id: int):
        while True:
            valinta = self.process_command(self.io.read_input(f"Haluatko lisätä vinkille uuden tagin?\n1: Kyllä\n2: Ei\n"))
            if valinta == 1:
                teksti = self.io.read_input("Tagi: ")
                self.db.add_tag_to_podcastvinkki(vinkki_id, Tagi(nimi = teksti))
            elif valinta == 2:
                break
            else:
                self.io.write('Virheellinen syöte')

    def add_tags_blogpostvinkki(self, vinkki_id: int):
        while True:
            valinta = self.process_command(self.io.read_input(f"Haluatko lisätä vinkille uuden tagin?\n1: Kyllä\n2: Ei\n"))
            if valinta == 1:
                teksti = self.io.read_input("Tagi: ")
                self.db.add_tag_to_blogpostvinkki(vinkki_id, Tagi(nimi = teksti))
            elif valinta == 2:
                break
            else:
                self.io.write('Virheellinen syöte')

    def add_courses_kirja(self, vinkki_id):
        while True:
            valinta = self.process_command(self.io.read_input(f"Haluatko lisätä vinkkiin liittyvän kurssin?\n1: Kyllä\n2: Ei\n"))
            if valinta == 1:
                teksti = self.io.read_input("Kurssin nimi: ")
                self.db.add_course_to_kirjavinkki(vinkki_id, Kurssi(nimi = teksti))
            elif valinta == 2:
                break
            else:
                self.io.write('Virheellinen syöte')

    def add_courses_video(self, vinkki_id):
        while True:
            valinta = self.process_command(self.io.read_input(f"Haluatko lisätä vinkkiin liittyvän kurssin?\n1: Kyllä\n2: Ei\n"))
            if valinta == 1:
                teksti = self.io.read_input("Kurssin nimi: ")
                self.db.add_course_to_videovinkki(vinkki_id, Kurssi(nimi = teksti))
            elif valinta == 2:
                break
            else:
                self.io.write('Virheellinen syöte')

    def add_courses_podcast(self, vinkki_id):
        while True:
            valinta = self.process_command(self.io.read_input(f"Haluatko lisätä vinkkiin liittyvän kurssin?\n1: Kyllä\n2: Ei\n"))
            if valinta == 1:
                teksti = self.io.read_input("Kurssin nimi: ")
                self.db.add_course_to_podcastvinkki(vinkki_id, Kurssi(nimi = teksti))
            elif valinta == 2:
                break
            else:
                self.io.write('Virheellinen syöte')

    def add_courses_blogpost(self, vinkki_id):
        while True:
            valinta = self.process_command(self.io.read_input(f"Haluatko lisätä vinkkiin liittyvän kurssin?\n1: Kyllä\n2: Ei\n"))
            if valinta == 1:
                teksti = self.io.read_input("Kurssin nimi: ")
                self.db.add_course_to_blogpostvinkki(vinkki_id, Kurssi(nimi = teksti))
            elif valinta == 2:
                break
            else:
                self.io.write('Virheellinen syöte')

    def delete_vinkki(self):
        tyyppi = self.ask_for_tyyppi()

        if tyyppi is None:
            self.io.write('Tyyppiä ei löydy')
            return

        self.io.write('Anna poistettavan vinkin id:\n')
        self.print_vinkit_with_id()
        user_input = self.process_command(self.io.read_input('Poistettavan vinkin id: '))
        if isinstance(user_input, int):# and tyyppi is not None:
            if self.db.delete_vinkki_with_id(user_input, tyyppi):
                self.io.write(f'Vinkki tyyppiä {tyyppi}, id {user_input} poistettu')
            else:
                self.io.write('Vinkin poistaminen epäonnistui')

    def ask_for_tyyppi(self):
        self.io.write('Valitse vinkin tyyppi:')
        self.io.write('1: Kirja')
        self.io.write('2: Video')
        self.io.write('3: Podcast')
        self.io.write('4: Blogpost')

        tyyppi = None
        user_input = self.process_command(self.io.read_input('Anna komento: '))
        if user_input == 1:
            tyyppi = VinkkiTyyppi.KIRJA
        elif user_input == 2:
            tyyppi = VinkkiTyyppi.VIDEO
        elif user_input == 3:
            tyyppi = VinkkiTyyppi.PODCAST
        elif user_input == 4:
            tyyppi = VinkkiTyyppi.BLOG
        return tyyppi

    def print_vinkit_with_id(self):
        vinkit = self.db.find_all_vinkit()
        for vinkki in vinkit:
            self.io.write(f'id: {vinkki.id} {vinkki}\n')

    def random_vinkki(self):
        vinkit = self.db.find_all_vinkit()
        if len(vinkit) == 0:
            return
        random_number = self.number_generator(len(vinkit)-1)
        vinkki = vinkit[random_number]
        self.io.write(vinkki)

    def search_by_tag(self):
        self.io.write('Anna tagin id:')
        tagit = self.print_tagit_with_id()
        tagi_id = self.io.read_input('haettavan tagin id: ')
        haettava_tagi = self.process_command(tagi_id)
        if haettava_tagi != None:
            if 0 < int(tagi_id) <= len(tagit):
                vinkit = self.db.search_vinkki_by_tag(haettava_tagi)
                for vinkki in vinkit:
                    self.io.write(vinkki)
            else:
                self.io.write("Tagia ei löytynyt")
        
    def print_tagit_with_id(self):
        tagit = self.db.find_all_tagit()
        for tagi in tagit:
            self.io.write(f'id: {tagi.id} {tagi.nimi}')

        return tagit
