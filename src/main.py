from ui.ui import Ui
from ui.io import Io

def main():
    io = Io()
    ui = Ui(io)
    ui.start()

if __name__ == "__main__":
    main()