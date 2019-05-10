import csv
import sys
from random import randint

from BubbleWidget import *
from ExpSetup import *
from NormalWidget import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from RopeWidget import *


class XPManager():

    def __init__(self, IDUser, technique, densite, taille, repetitions):
        super().__init__()
        self.IDUser = IDUser
        self.technique = technique
        self.densite = densite
        self.taille = taille
        self.repetitions = repetitions

        if(self.taille == "grande"):
            targetTaille = 50
        else:
            targetTaille = 25

        if(self.densite == "haute"):
            self.file = "bigBubble.csv"
            nb = 30
        else:
            self.file = "littleBubble.csv"
            nb = 60

        targetChoices = list()
        for i in range(10):
            targetChoices.append(randint(0, nb))

       



def main(args):
    app = QApplication(args)
    window = QMainWindow()
    setup = ExpSetup(callback, window)
    window.setCentralWidget(setup)
    window.resize(450, 450)
    window.show()
    app.exec_()

def callback(setup, window):
    manager = XPManager(setup.IDUser, setup.technique,
                            setup.densite, setup.taille, setup.repetitions)

    if (manager.technique == "bubble"):
        bubbleWidget = BubbleWidget(manager.file)
        window.setCentralWidget(bubbleWidget)
    elif (manager.technique== "normal"):
        normalWidget = NormalWidget(manager.file)
        window.setCentralWidget(normalWidget)
        print("ok")
    elif (manager.technique == "rope"):
        ropWidget = RopeWidget(manager.file)
        window.setCentralWidget(ropWidget)
    else:
        raise ValueError('argument missing')

    window.resize(1024, 800)
    window.show()
    return

if __name__ == "__main__":
    print("execution du programme")
    main(sys.argv)
