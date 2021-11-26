class Ui:

    def __init__(self):
        pass


    def start(self):
        print('Tervetuloa käyttämään Lukuvinkki-sovellusta \n')
        self.print_options()
    

    def print_options(self):
        while True:
            print('Valitse toiminto: ')
            print('1: Hae lukuvinkki')
            print('2: Lisää lukuvinkki')
            print('3: Lopeta')
            try:
                user_input = int(input('Anna komento: '))
            except ValueError:
                print('Anna kelvollinen komento')
            print()

