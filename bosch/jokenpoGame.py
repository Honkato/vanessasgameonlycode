import random
import sys

import winsound
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QIcon, QMovie, QPixmap

class JokenpoGame(QWidget):
    def __init__(self):
        super(JokenpoGame, self).__init__()
        uic.loadUi("./archives/telasUI/pptUIWidget.ui", self)
        winsound.PlaySound("./archives/musicsSongs/dragonslayerArmour.wav", winsound.SND_ASYNC)
        # self.background = self.findChild(QLabel, "lblBackground")
        self.btnStart = self.findChild(QPushButton, "btnStart")
        self.btnReset = self.findChild(QPushButton, "btnReset")
        self.btnPedra = self.findChild(QPushButton, "btnPedra")
        self.btnPapel = self.findChild(QPushButton, "btnPapel")
        self.btnTesoura = self.findChild(QPushButton, "btnTesoura")

        self.btnTesoura.clicked.connect(lambda: self.setPlayer(1))
        self.btnPapel.clicked.connect(lambda: self.setPlayer(2))
        self.btnPedra.clicked.connect(lambda: self.setPlayer(3))

        self.btnTesoura.setDisabled(True)
        self.btnPapel.setDisabled(True)
        self.btnPedra.setDisabled(True)

        self.btnStart.clicked.connect(self.timeStart)
        self.btnReset.clicked.connect(self.reset)

        self.lblBright = self.findChild(QLabel, "lblBright")
        self.lblImagem = self.findChild(QLabel, "lblImagem")
        self.lblPCPoints = self.findChild(QLabel, "lblPCPoints")
        self.lblPlayerPoints = self.findChild(QLabel, "lblPlayerPoints")
        self.lblSelection = self.findChild(QLabel, "lblSelection")
        self.lblStatus = self.findChild(QLabel, "lblStatus")
        self.lblStatus_2 = self.findChild(QLabel, "lblStatus_2")
        self.lblRounds = self.findChild(QLabel, "lblRounds")

        self.lblBright.hide()
        self.lblStatus.hide()
        self.lblSelection.hide()


        self.player = 0
        self.pc = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.contador)
        self.reset()

        self.show()

    def timeStart(self):
        if self.timer.isActive:
            print("start")
            self.btnReset.setEnabled(False)
            self.contagem = 0
            self.btnTesoura.setDisabled(False)
            self.btnPapel.setDisabled(False)
            self.btnPedra.setDisabled(False)
            self.lblBright.show()
            self.lblStatus.show()
            self.timer.start(1000)

    def setPlayer(self, number):
        if self.pc == 0:
            return
        self.player = number
        self.lblSelection.show()
        self.lblStatus_2.setStyleSheet("background-color: rgb(85,250,100,50%);border-radius:145px")
        self.lblStatus.setStyleSheet("background-color: rgb(85,250,100,50%);")
        if number == 1:
            self.lblSelection.move(270, 460)
        elif number == 2:
            self.lblSelection.move(144, 380)
        else:
            self.lblSelection.move(18, 460)

    def reset(self):

        self.playerPoints = 0
        self.lblPlayerPoints.setText(str(self.playerPoints))
        self.pcPoints = 0
        self.lblPCPoints.setText(str(self.pcPoints))
        self.lblRounds.setText("0")

    def contador(self):
        self.contagem += 1

        self.lblRounds.setText(str(int(self.lblRounds.text())+1))

        if self.player == self.pc or self.pc == 0:
            pass
        elif self.player == 1 and self.pc == 3 or\
                self.player == 2 and self.pc == 1 or\
                self.player == 3 and self.pc == 2:
            self.playerPoints += 1
            self.lblPlayerPoints.setText(str(self.playerPoints))
        else:
            self.pcPoints += 1
            self.lblPCPoints.setText(str(self.pcPoints))

        self.pc = random.randint(1, 3)
        if self.pc == 1:
            self.lblImagem.setPixmap(QPixmap("./archives/icons/blade.png"))
        elif self.pc == 2:
            self.lblImagem.setPixmap(QPixmap("./archives/icons/bow.png"))
        else:
            self.lblImagem.setPixmap(QPixmap("./archives/icons/shield.png"))
        #       85,250,100,50%  green
        #       255,50,20,50%   red
        #       205,50,200,50%  purple
        self.lblSelection.hide()
        self.lblStatus_2.setStyleSheet("background-color: rgb(255,50,20,50%);border-radius:145px")
        self.lblStatus.setStyleSheet("background-color: rgb(255,50,20,50%);")
        self.player = 0
        if self.contagem >= 10:
            self.lblStatus_2.setStyleSheet("background-color: rgb(205,50,200,50%);border-radius:145px")
            self.lblStatus.setStyleSheet("background-color: rgb(205,50,200,50%);")
            self.btnTesoura.setDisabled(True)
            self.btnPapel.setDisabled(True)
            self.btnPedra.setDisabled(True)
            self.lblBright.hide()
            self.lblStatus.hide()
            self.btnReset.setEnabled(True)
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    joken = JokenpoGame()
    app.exec()
