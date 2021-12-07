from models import VideoVinkki, base
from ui.ui import Ui
from ui.io import Io
from db import DataBase
def main():
    io = Io()
    database = DataBase("tietokanta", base)
    ui = Ui(io, database)
    ui.start()

if __name__ == "__main__":
    main()
