from models import base
from ui.ui import Ui
from ui.io import Io
from db import DataBase
from random_generator import random_int

def main():
    io = Io()
    database = DataBase("tietokanta", base)
    ui = Ui(io, database, random_int)
    ui.start()

if __name__ == "__main__":
    main()
