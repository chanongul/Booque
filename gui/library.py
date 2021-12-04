import sys, os, sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, uic

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from gui import authen, book
import rsrc.rsrc
import rsrc.style.library as style


class Library(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("rsrc/ui/library.ui", self)
        global libApp
        libApp = self
        self.setStyleSheet(style.default)
        self.db = sqlite3.connect("rsrc/db/data.db")
        self.curs = self.db.cursor()
        self.curs.execute("SELECT book_id, title, cover_img, author FROM books")
        self.books_db = self.curs.fetchall()
        self.book_ids = [str(i[0]) for i in self.books_db]
        self.book_titles = [str(i[1]) for i in self.books_db]
        self.book_imgs = [str(i[2]) for i in self.books_db]
        self.book_authors = [str(i[3]) for i in self.books_db]
        self.column = 4
        self.pos = [
            [r, c]
            for r in range(int(len(self.books_db) / self.column) + 1)
            for c in range(self.column)
        ]
        self.button = [
            [[] for c in range(self.column)]
            for r in range(int(len(self.books_db) / self.column) + 1)
        ]
        print(self.button)
        for [r, c], id, title, img, author in zip(
            self.pos, self.book_ids, self.book_titles, self.book_imgs, self.book_authors
        ):
            self.title_label = QtWidgets.QLabel()
            self.title_label.setText(title)
            self.title_label.setFont(QtGui.QFont("Product Sans", 14))
            self.title_label.setWordWrap(True)
            self.title_label.setAlignment(QtCore.Qt.AlignCenter)
            self.author_label = QtWidgets.QLabel()
            self.author_label.setText(author)
            self.author_label.setFont(QtGui.QFont("Product Sans", 10))
            self.author_label.setWordWrap(True)
            self.author_label.setAlignment(QtCore.Qt.AlignCenter)
            self.button[r][c] = QtWidgets.QPushButton()
            self.pixmap = QtGui.QPixmap(img)
            self.button[r][c].setIcon(QtGui.QIcon(self.pixmap))
            self.button[r][c].setSizePolicy(
                QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
            )
            self.button[r][c].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.button[r][c].setMinimumSize(250, 380)
            self.button[r][c].setIconSize(QtCore.QSize(250, 380))
            self.button[r][c].clicked.connect(lambda x, id=id: self.goToBook(id))
            self.book_container = QtWidgets.QVBoxLayout()
            self.book_container.setSpacing(5)
            self.book_container.addWidget(self.button[r][c], 0)
            self.book_container.addWidget(self.title_label, 1)
            self.book_container.addWidget(self.author_label, 2)
            self.book_shelf.addLayout(self.book_container, *[r, c])
        self.search_btn.clicked.connect(self.search)
        self.sort_box.activated.connect(lambda x: self.handleSortBox(x))
        self.genre_box.activated.connect(lambda x: self.handleGenreBox(x))

    def goToBook(self, book_id):
        authen.mainApp.setWindowTitle("Booque - ")
        authen.mainApp.app_panel.setCurrentIndex(6)
        book.bookApp.setId(int(book_id))

    def search(self):
        if self.search_bar.text():
            pass

    def handleSortBox(self, index):
        if index == 0:
            print("a-z")
        elif index == 1:
            print("z-a")
        elif index == 2:
            print("Rating (most)")
        elif index == 3:
            print("Rating (least)")

    def handleGenreBox(self, index):
        if index == 0:
            print("All")
        elif index == 1:
            print("Fiction")
        elif index == 2:
            print("Thriller")
        elif index == 3:
            print("Fantasy")
        elif index == 4:
            print("Romance")
        elif index == 5:
            print("Biography")
        elif index == 6:
            print("Comedy")
        elif index == 7:
            print("Horror")
        elif index == 8:
            print("Adventure")
