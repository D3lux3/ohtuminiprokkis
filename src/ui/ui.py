class Ui:

    def __init__(self, io):
        self.io = io


    def start(self):
        self.io.write('Tervetuloa käyttämään Lukuvinkki-sovellusta \n')
        self.print_options()
    
    def print_options(self):
        while True:
            self.io.write('Valitse toiminto: ')
            self.io.write('1: Hae lukuvinkki')
            self.io.write('2: Lisää lukuvinkki')
            self.io.write('3: Lopeta')
            self.process_command(self.io.read_input('Anna komento: '))

    def process_command(self, command):
        try:
            user_input = int(command)
        except ValueError:
            self.io.write('Anna kelvollinen komento')
        print()

