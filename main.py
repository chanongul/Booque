import sys, os
from PyQt5 import QtWidgets

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import db, authen


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = authen.LogIn()
    gui.show()
    db.database.initFont()
    app.aboutToQuit.connect(db.database.exit)
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
