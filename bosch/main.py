import sys

import winsound
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QMovie

from hangmanGame import HangmanGame
from hashGame import HashGame
from jokenpoGame import JokenpoGame
from mementoGame import MementoGame


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        uic.loadUi("./archives/telasUI/menuPrincipalUI.ui", self)
        # DEFINING OBJECTS
        self.background = self.findChild(QLabel, "lblbackground")
        winsound.PlaySound("./archives/musicsSongs/opening.wav", winsound.SND_ASYNC)

        self.gif = QMovie("./gifMenu/MenuPy.gif")
        self.background.setMovie(self.gif)
        self.gif.start()

        self.timer = QTimer()
        self.timer.timeout.connect(self.time)
        self.timer.start(1500)

        self.btnHangman = self.findChild(QPushButton, "btnHangman")
        self.btnHash = self.findChild(QPushButton, "btnHash")
        self.btnJokenpo = self.findChild(QPushButton, "btnJokenpo")
        self.btnMemento = self.findChild(QPushButton, "btnMemento")

        # DEFINING FUNCTIONS
        self.btnHangman.clicked.connect(self.hangmanFunc)
        self.btnHash.clicked.connect(self.hashFunc)
        self.btnJokenpo.clicked.connect(self.jokenpoFunc)
        self.btnMemento.clicked.connect(self.mementoFunc)

        self.screensOppened = []

        self.show()
    def closeAll(self):
        for x in range(len(self.screensOppened)):
            self.screensOppened[x].deleteLater()
            self.screensOppened.pop(x)

    def time(self):
        self.gif = QMovie("./gifMenu/MenuPy.gif")
        self.background.setMovie(self.gif)
        self.gif.start()

    def hangmanFunc(self):
        self.closeAll()
        self.hgG = HangmanGame()
        self.screensOppened.append(self.hgG)
        self.hgG.show()
        print("hangman")

    def hashFunc(self):
        self.closeAll()
        self.hG = HashGame()
        self.screensOppened.append(self.hG)
        self.hG.show()
        print("hashFunc")

    def jokenpoFunc(self):
        self.closeAll()
        self.jG = JokenpoGame()
        self.screensOppened.append(self.jG)
        self.jG.show()
        print("jokenpoFunc")

    def mementoFunc(self):
        self.closeAll()
        self.mG = MementoGame()
        self.screensOppened.append(self.mG)
        self.mG.show()
        print("mementoFunc")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu()
    app.exec()
