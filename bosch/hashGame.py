import sys

import winsound
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5 import uic, QtGui


class HashGame(QWidget):
    def __init__(self):
        super(HashGame, self).__init__()
        uic.loadUi("./archives/telasUI/velhaUIWidget.ui", self)
        winsound.PlaySound("./archives/musicsSongs/premonition.wav", winsound.SND_ASYNC)

        # DEFINING OBJECTS
        self.btn = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, 9):
            self.btn[i] = self.findChild(QPushButton, "btn_" + str(i+1))
        self.btnReset = self.findChild(QPushButton, "btnReset")
        self.lblFinish = self.findChild(QLabel, "lblFinish")
        self.lblSun = self.findChild(QLabel, "lblSun")
        self.scoreSun = 0
        self.lblMoon = self.findChild(QLabel, "lblMoon")
        self.scoreMoon = 0
        self.btnStatus(True)

        self.icon = "border-image: url(./archives/icons/moonblade.png)"
        self.player = 2

        # DEFINING FUNCTIONS
        # for j in range(1,9):
        #     self.btn[j].clicked.connect(lambda : self.tictactoeFunction(j))

        self.btn[0].clicked.connect(lambda: self.tictactoeFunction(0))
        self.btn[1].clicked.connect(lambda: self.tictactoeFunction(1))
        self.btn[2].clicked.connect(lambda: self.tictactoeFunction(2))
        self.btn[3].clicked.connect(lambda: self.tictactoeFunction(3))
        self.btn[4].clicked.connect(lambda: self.tictactoeFunction(4))
        self.btn[5].clicked.connect(lambda: self.tictactoeFunction(5))
        self.btn[6].clicked.connect(lambda: self.tictactoeFunction(6))
        self.btn[7].clicked.connect(lambda: self.tictactoeFunction(7))
        self.btn[8].clicked.connect(lambda: self.tictactoeFunction(8))
        self.btnReset.clicked.connect(lambda: self.btnStatus(True))

        self.show()

    def tictactoeFunction(self, number):
        print(number)
        translate = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
        markA = int(translate[number][0])
        markB = int(translate[number][1])
        if self.player == 1:
            self.icon = "border-image: url(./archives/icons/moonblade.png)"
            self.player = 2
        else:
            self.icon = "border-image: url(./archives/icons/sun.png)"
            self.player = 1

        self.hash[markA][markB] = self.player
        self.btn[number].setStyleSheet(self.icon)
        self.btn[number].setEnabled(False)
        if self.verifyWinner():
            self.btnStatus(False)


    def verifyWinner(self):
        l0 = self.hash[0]
        l1 = self.hash[1]
        l2 = self.hash[2]
        c0 = [self.hash[0][0], self.hash[1][0], self.hash[2][0]]
        c1 = [self.hash[0][1], self.hash[1][1], self.hash[2][1]]
        c2 = [self.hash[0][2], self.hash[1][2], self.hash[2][2]]
        d0 = [self.hash[0][0], self.hash[1][1], self.hash[2][2]]
        d1 = [self.hash[2][0], self.hash[1][1], self.hash[0][2]]

        tudo = [l0, l1, l2, c0, c1, c2, d0, d1]
        for i in tudo:
            print(i)
            if i == [1, 1, 1]:
                self.scoreSun += 1
                self.lblSun.setText(str(self.scoreSun))
                return True
            elif i == [2, 2, 2]:
                self.scoreMoon += 1
                self.lblMoon.setText(str(self.scoreMoon))
                return True

        for i in tudo:
            if i.__contains__(0):
                return False
        return True

    def btnStatus(self, condition):
        for i in self.btn:
            i.setEnabled(condition)
            if condition:
                i.setStyleSheet("background-color:rgb(0,0,0,0%)")
        if condition:
            self.lblFinish.hide()
            self.hash = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
        else:
            self.lblFinish.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hash = HashGame()
    app.exec()
