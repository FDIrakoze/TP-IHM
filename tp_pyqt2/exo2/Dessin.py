import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CanvasDessin import *
      
class Dessin(QMainWindow):

        def __init__(self, canvas):
                super().__init__()
                self.canvas = canvas
                self.setCentralWidget(self.canvas)

        def addMenuAction(self,img, nom, shortcut, tip):
                icon = QIcon(img)
                newAct = QAction(icon, nom, self)
                newAct.setShortcut( shortcut )
                newAct.setToolTip(tip)
                newAct.setStatusTip(tip)
                newAct.setCheckable(True)
                return newAct 

        def open(self):
                color = QColorDialog.getColor()

                if color.isValid():
                        print(color.name())
                        self.canvas.color = color
                        pix = QPixmap("color.jpg")
                        pix.fill(color)
                        self.fileToolBar.actions()[0].setIcon(QIcon(pix))
                        

        def valuechange(self):
                print("width changed to " + str(self.sl.value()))
                self.canvas.width = self.sl.value()
        def reset(self):
                self.canvas = CanvasDessin()
                self.setCentralWidget(self.canvas)
                self.sl.setValue(2)
                pix = QPixmap("color.jpg")
                pix.fill(self.canvas.color)
                self.fileToolBar.actions()[0].setIcon(QIcon(pix))


        def addMenuBar(self):
                self.fileToolBar = QToolBar("file")              
                self.addToolBar(self.fileToolBar)
                
                pix = QPixmap("color.jpg")
                pix.fill(self.canvas.color)
                newColor = self.addMenuAction(pix, "Select Color", "Ctrl+l", "Select Color to Use")
                newColor.triggered.connect(self.open)
                self.fileToolBar.addAction(newColor)

                self.sl = QSlider(Qt.Horizontal)
                self.sl.setMinimum(2)
                self.sl.setMaximum(10)
                self.sl.setValue(2)
                self.sl.setTickPosition(QSlider.TicksBelow)
                self.sl.setTickInterval(2)
                self.sl.valueChanged.connect(self.valuechange)
                self.fileToolBar.addWidget(self.sl)

                self.b1 = QPushButton("Reset")
                self.b1.clicked.connect(self.reset)
                self.fileToolBar.addWidget(self.b1)
                self.setStatusBar(QStatusBar())


def main(args):
        app = QApplication(args)
        canvas = CanvasDessin()
        dessin = Dessin(canvas)
        dessin.addMenuBar()
        dessin.show()
        sys.exit(app.exec_())

        
if __name__ == "__main__":
       
        print("execution du programme")
        main(sys.argv)
       
        
