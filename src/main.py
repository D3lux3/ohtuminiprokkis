from models import Base
from ui.ui import Ui
from ui.io import Io
from db import db
from models import Base

def main():
    io = Io()
    database = db("tietokanta", Base)
    ui = Ui(io, database)
    ui.start()

if __name__ == "__main__":
    main()