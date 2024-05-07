import random
import sys, os

import winsound
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QIcon, QMovie, QPixmap

class MementoGame(QWidget):
    def __init__(self):
        super(MementoGame, self).__init__()
        uic.loadUi("./archives/telasUI/mementomoriUIWidget.ui", self)
        # winsound.PlaySound("./archives/musicsSongs/namelessKing.wav", winsound.SND_ASYNC)
        self.btns = []
        for x in range(0,30):
            btn = self.findChild(QPushButton, "btn_"+str(x))
            self.btns.append(btn)
        self.lblBackground = self.findChild(QLabel, "lblBackground")
        self.lblPlayerPoints = [0, 0]
        self.lblPlayerPoints[0] = self.findChild(QLabel, "lblPlayer1Points")
        self.lblPlayerPoints[1] = self.findChild(QLabel, "lblPlayer2Points")
        self.lblTurn = self.findChild(QLabel, "lblTurn")
        self.lblp = [[0, 0, 0, 0], [0, 0, 0, 0]]

        self.btnJoin = self.findChild(QPushButton, "btnSecondPlayer")

        self.btnJoin.clicked.connect(self.join)
        self.btns[0].clicked.connect(lambda: self.num(0, True))
        self.btns[1].clicked.connect(lambda: self.num(1, True))
        self.btns[2].clicked.connect(lambda: self.num(2, True))
        self.btns[3].clicked.connect(lambda: self.num(3, True))
        self.btns[4].clicked.connect(lambda: self.num(4, True))
        self.btns[5].clicked.connect(lambda: self.num(5, True))
        self.btns[6].clicked.connect(lambda: self.num(6, True))
        self.btns[7].clicked.connect(lambda: self.num(7, True))
        self.btns[8].clicked.connect(lambda: self.num(8, True))
        self.btns[9].clicked.connect(lambda: self.num(9, True))
        self.btns[10].clicked.connect(lambda: self.num(10, True))
        self.btns[11].clicked.connect(lambda: self.num(11, True))
        self.btns[12].clicked.connect(lambda: self.num(12, True))
        self.btns[13].clicked.connect(lambda: self.num(13, True))
        self.btns[14].clicked.connect(lambda: self.num(14, True))
        self.btns[15].clicked.connect(lambda: self.num(15, True))
        self.btns[16].clicked.connect(lambda: self.num(16, True))
        self.btns[17].clicked.connect(lambda: self.num(17, True))
        self.btns[18].clicked.connect(lambda: self.num(18, True))
        self.btns[19].clicked.connect(lambda: self.num(19, True))
        self.btns[20].clicked.connect(lambda: self.num(20, True))
        self.btns[21].clicked.connect(lambda: self.num(21, True))
        self.btns[22].clicked.connect(lambda: self.num(22, True))
        self.btns[23].clicked.connect(lambda: self.num(23, True))
        self.btns[24].clicked.connect(lambda: self.num(24, True))
        self.btns[25].clicked.connect(lambda: self.num(25, True))
        self.btns[26].clicked.connect(lambda: self.num(26, True))
        self.btns[27].clicked.connect(lambda: self.num(27, True))
        self.btns[28].clicked.connect(lambda: self.num(28, True))
        self.btns[29].clicked.connect(lambda: self.num(29, True))

        self.vez = False
        self.pc = True
        self.num1 = -1
        self.num2 = -1

        self.setStyle1 = ""
        self.setStyle2 = ""

        self.player = 1

        self.timer = QTimer()
        self.timer.timeout.connect(self.tempo)

        self.auto = QTimer()
        self.auto.timeout.connect(self.autoPlay)

        # self.btns[0].setStyleSheet("border-image: url(./archives/icons/blademooncard.png);")
        # RESPONSAVEL POR RANDOMIZAR
        self.reset()
        self.btnReset = self.findChild(QPushButton, "btnReset")
        self.btnReset.clicked.connect(self.reset)
        # self.btnReset.hide()

        self.show()

    def join(self):
        self.pc = False
        self.btnJoin.hide()

    def autoPlay(self):
        print("iniciou")
        while True:
            num = random.randint(0,29)
            if not self.btns[num].isHidden():
                print("escolheu")
                self.num(num, False)
                break
        if not self.vez:
            print("parou")
            self.auto.stop()

    def reset(self):
        self.player = 1
        self.lblTurn.setText("Player 1 Turn")
        self.lblPlayerPoints[0].setText("0")
        self.lblPlayerPoints[1].setText("0")
        indexes1 = []
        indexes2 = []
        filePng = []

        for x in range(4):
            self.lblp[0][x] = self.findChild(QLabel, "lblp1_"+str(x+1))
            self.lblp[0][x].hide()
            self.lblp[1][x] = self.findChild(QLabel, "lblp2_"+str(x+1))
            self.lblp[1][x].hide()

        for file in os.listdir('./archives/icons'):
            if file.__contains__("card.png"):
                filePng.append("(./archives/icons/" + file + ")")
        for file in os.listdir('./archives/icons'):
            if file.__contains__("card.png"):
                filePng.append("(./archives/icons/" + file + ")")

        for x in range(30):
            indexes1.append(x)
            indexes2.append(x)

        for x in range(30):
            escolha1 = random.choice(indexes1)
            escolha2 = random.choice(indexes2)
            while True:
                if self.btns[escolha1].styleSheet() != "":
                    self.btns[escolha1].setObjectName("border-image: url"+filePng[escolha2])
                    self.btns[escolha1].setStyleSheet("border-image: url(./archives/icons/backcards.png)")
                    self.btns[escolha1].show()
                    break
            indexes1.remove(escolha1)
            indexes2.remove(escolha2)

    def num(self, num, player):
        print("passou")
        if self.player == 2 and self.pc and player:
            return
        if self.timer.isActive() or self.btns[num].objectName() == "border-image: url(./archives/icons/backcards.png)":
            return
        self.vez = not self.vez
        if self.vez:
            self.num1 = num
            self.setStyle1 = self.btns[num].objectName()
            self.btns[num].setStyleSheet(self.setStyle1)
            self.btns[num].setObjectName("border-image: url(./archives/icons/backcards.png)")
        elif not self.vez:
            self.num2 = num
            self.setStyle2 = self.btns[num].objectName()
            self.btns[num].setStyleSheet(self.setStyle2)
            self.btns[num].setObjectName("border-image: url(./archives/icons/backcards.png)")
            if self.btns[self.num1].styleSheet() != self.btns[self.num2].styleSheet():
                self.timer.start(2100)
            else:
                # com ou sem?
                self.btns[self.num1].hide()
                self.btns[self.num2].hide()
                if self.player == 1:
                    # player 1 placar sobe
                    self.lblPlayerPoints[0].setText(str((int(self.lblPlayerPoints[0].text()))+2))
                else:
                    # player 2 placar sobe
                    self.lblPlayerPoints[1].setText(str((int(self.lblPlayerPoints[1].text()))+2))

            self.vez = 0
        self.points()

    def tempo(self):
        if self.player == 1:
            self.player = 2
            self.lblTurn.setText("Player 2 Turn")
        else:
            self.player = 1
            self.lblTurn.setText("Player 1 Turn")
        self.btns[self.num1].setObjectName(self.setStyle1)
        self.btns[self.num1].setStyleSheet("border-image: url(./archives/icons/backcards.png)")
        self.btns[self.num2].setObjectName(self.setStyle2)
        self.btns[self.num2].setStyleSheet("border-image: url(./archives/icons/backcards.png)")
        if self.player == 2 and self.pc:
            self.auto.start(1100)
        self.timer.stop()

    def points(self):
        for x in range(len(self.lblPlayerPoints)):
            if int(self.lblPlayerPoints[x].text()) > 10:
                self.lblp[x][3].show()
            if int(self.lblPlayerPoints[x].text()) > 6:
                self.lblp[x][2].show()
            if int(self.lblPlayerPoints[x].text()) > 4:
                self.lblp[x][1].show()
            if int(self.lblPlayerPoints[x].text()) >= 2:
                self.lblp[x][0].show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    memento = MementoGame()
    app.exec()
