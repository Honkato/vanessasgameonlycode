import sys
import time
import os
from threading import Thread
import winsound

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic
from playsound import playsound

class LoseWin(QWidget):
    def __init__(self, condition):
        super(LoseWin, self).__init__()
        if condition:
            uic.loadUi("./archives/telasUI/winUIWidget.ui", self)
            winsound.PlaySound("./archives/musicsSongs/verdefeated.wav", winsound.SND_ASYNC)
            # playsound("vergud.mp3", True)
        else:
            uic.loadUi("./archives/telasUI/loseUIWidget.ui", self)
            winsound.PlaySound("./archives/musicsSongs/idie.wav", winsound.SND_ASYNC)
            # playsound("udie.mp3", True)

            # os.startfile("isorry.mp3")

        self.btnOK = self.findChild(QPushButton, "btnOK")
        self.btnOK.clicked.connect(self.reset)

        self.show()

        # winsound.PlaySound("./archives/musicsSongs/isorry.wav", winsound.SND_ASYNC)
        # t = Thread(target=self.playmusica())
        # t.daemon = True
        # t.start()

        if condition:
            # playsound("vergud.mp3", True)
            # playsound("udie.mp3", True)
            pass
        else:
            # playsound("udie.mp3", True)
            # time.sleep(1)
            # playsound("isorry.mp3", True)
            pass
        # playsound("vergud.mp3", False)


    def reset(self):
        # ui = game
        # ui.show()
        self.close()

    # def playmusica(self):
    #     playsound("udie.mp3", True)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = LoseWin(True)
    app.exec()
