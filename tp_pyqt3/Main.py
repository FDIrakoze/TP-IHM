import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from NormalWidget import *
from BubbleWidget import *
from RopeWidget import *


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

def main(args):
    app = QApplication(args)
    window = Main()
    if (args[1] == "bubble"):
        bubbleWidget = BubbleWidget()
        window.setCentralWidget(bubbleWidget)
    elif (args[1] == "normal"):
        normalWidget = NormalWidget()
        window.setCentralWidget(normalWidget)
    elif (args[1] == "rope"):
        ropWidget = RopeWidget()
        window.setCentralWidget(ropWidget)
    else:
        raise ValueError('argument missing')

    window.resize(1024, 800)
    window.show()
    app.exec_()


if __name__ == "__main__":
    print("execution du programme")
    main(sys.argv)
