import random
import sys

import winsound
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QIcon, QMovie, QPixmap

from loseWin import LoseWin


class HangmanGame(QWidget):
    def __init__(self):
        super(HangmanGame, self).__init__()
        uic.loadUi("./archives/telasUI/forcaUIWidget.ui", self)
        winsound.PlaySound("./archives/musicsSongs/curseRotted.wav", winsound.SND_ASYNC)

        self.background = self.findChild(QLabel, "lblBackground")
        self.btnConfirm = self.findChild(QPushButton, "btnConfirm")
        self.btnReset = self.findChild(QPushButton, "btnReset")
        self.lblCorrect = self.findChild(QLabel, "lblCorrect")
        self.lblPalavra = self.findChild(QLabel, "lblPalavra")
        self.lblTema = self.findChild(QLabel, "lblTema")
        self.lblTypped = self.findChild(QLabel, "lblTypped")
        self.lblWrong = self.findChild(QLabel, "lblWrong")
        self.txtLetter = self.findChild(QLineEdit, "txtLetter")
        self.btnConfirm.setFocus()


        self.btnReset.clicked.connect(self.reset)
        self.btnConfirm.clicked.connect(lambda: self.confirm(True))
        # self.btnConfirm.clicked.connect(self.confirm)
        self.fundoImg = ["Forca.png", "Forca (2).png", "Forca (3).png", "Forca (4).png"]
        self.pixmap = [f"./archives/img/{self.fundoImg[0]}",
                       f"./archives/img/{self.fundoImg[1]}",
                       f"./archives/img/{self.fundoImg[2]}",
                       f"./archives/img/{self.fundoImg[3]}",
                       ]
        self.reset()

        self.show()
    def reset(self):
        tema, self.palavra = self.definirPalavra()
        self.palavra = self.palavra.upper()

        self.lblPalavra.setText("_ " * (len(self.palavra)))
        self.lblTema.setText(tema)
        self.letrasT = []
        self.letrasC = []
        self.letrasW = []
        self.lblTypped.setText("")
        self.lblWrong.setText("")
        self.lblCorrect.setText("")
        self.fundo = 0
        self.back()

    def back(self):
        if self.fundo < 4:
            # self.background.setStyleSheet(f"background-image: url:(archives/img/{self.fundoImg[self.fundo]})")
            # self.background.setStyleSheet(f"background-image: url:(archives/img/Forca (2).png)")
            self.background.setPixmap(QPixmap(self.pixmap[self.fundo]))
        elif self.fundo == 4:
            self.gif = QMovie("./archives/img/Forca (5).gif")
            self.background.setMovie(self.gif)
            self.gif.start()

            self.timer = QTimer()
            self.timer.timeout.connect(self.time)
            self.timer.start(5900)
        else:
            pass
            self.reset()
            self.lose = LoseWin(False)

    def time(self):
        self.gif = QMovie("./archives/img/Forca (5).gif")
        self.background.setMovie(self.gif)
        self.gif.start()

    def confirm(self, placeholder):
    # def confirm(self):
        self.txtLetter.setFocus()
        letra = self.txtLetter.text()
        letra = letra.upper()
        self.txtLetter.setText("")
        confirma = 0
        palavra = ""
        if letra == "":
            return
        if not self.letrasT.__contains__(letra):
            self.letrasT.append(letra)

        if self.palavra.__contains__(letra):
            if not self.letrasC.__contains__(letra):
                self.letrasC.append(letra)
            for i in self.palavra:
                if self.letrasC.__contains__(i):
                    palavra += i
                    palavra += " "
                    confirma += 1
                else:
                    palavra +="_ "
            self.lblPalavra.setText(palavra.capitalize())
            if confirma == len(self.palavra):
                self.reset()
                self.lose = LoseWin(True)
        else:
            if not self.letrasW.__contains__(letra):
                self.letrasW.append(letra)
                self.fundo += 1
                self.back()
        print(self.letrasT)
        print(self.letrasC)
        print(self.letrasW)
        self.lblTypped.setText(str(self.letrasT).replace('[','').replace(']','').replace("'",""))
        self.lblWrong.setText(str(self.letrasW).replace('[','').replace(']','').replace("'",""))
        self.lblCorrect.setText(str(self.letrasC).replace('[','').replace(']','').replace("'",""))




    def definirPalavra(self):
        tamLista = 0
        indexTemas = []
        indexPalavras = []
        indexPalaTema = []
        palavraDoTema = []
        lista = []
        arq = open("./bosch/Palavras.txt", "r", encoding="utf-8")
        txtArq = arq.read()
        palavra = ""
        for ponteiro in txtArq:
            if ponteiro == "\n":
                continue
            if ponteiro == "|":
                continue
            if ponteiro != ",":
                palavra += ponteiro
            else:
                lista.append(palavra)
                palavra = ""
        arq.close()
        for i in lista:
            if i == i.upper():
                indexTemas.append(tamLista)
            else:
                indexPalavras.append(tamLista)

            tamLista += 1

        aleaT = random.choice(indexTemas)
        for i in range(aleaT + 1, (len(lista) - 1)):
            if indexPalavras.__contains__(i):
                indexPalaTema.append(i)
                palavraDoTema.append(lista[i])
            else:
                break
        aleaP = random.choice(indexPalaTema)
        tema = lista[aleaT]
        palavra = lista[aleaP]
        # print("\n\nFIM DE 'definirPalavra\n\n")
        return tema, palavra


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hang = HangmanGame()
    app.exec()
