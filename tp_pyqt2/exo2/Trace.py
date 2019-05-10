import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CanvasDessin import *


        
class Trace(QMainWindow):
        
        def __init__(self, width, color):
                super().__init__()
                self.point = list()
                self.width = width
                self.color = color

# def main(args):
#         app = QApplication(args)
#         dessin = Dessin()
#         dessin.show()
#         app.exec_()

        
# if __name__ == "__main__":
# 	print("execution du programme")
# 	main(sys.argv)
        
