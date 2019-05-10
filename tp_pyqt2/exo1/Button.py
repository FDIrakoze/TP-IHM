import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ButtonModel import *


        
class MainWindow(QMainWindow):

        def __init__(self):
                super().__init__()

        def addCanvasButton(self, CanvasButton):
                self.setCentralWidget(CanvasButton)

class CanvasButton(QWidget):

        defaultCol = QColor(Qt.cyan)
        hoverCol = QColor(Qt.darkCyan)
        pressCol = QColor(Qt.black)
        
        def __init__(self):
                super().__init__()
                self.setMouseTracking(True) 
                self.bbox = QRect(QPoint(100, 200), QSize(250, 300));
                self.cursorOver = False
                self.buttonModel = ButtonModel()

        def paintEvent(self, event):
                painter = QPainter(self)
                painter.setRenderHints(QPainter.Antialiasing)
                pen = QPen(QColor(Qt.black))
                pen.setWidth(2)
                
                if self.buttonModel.state == 2:
                        painter.setBrush(self.hoverCol)
                elif self.buttonModel.state == 3:
                        painter.setBrush(self.pressCol)
                else:
                        painter.setBrush(self.defaultCol)
                        
                painter.setPen(pen)
                painter.drawEllipse(self.bbox)
                self.update()
                

                

        def mouseMoveEvent(self, event): 
                if self.cursorOnEllipse(event.pos()):
                        self.cursorOver = True
                        self.buttonModel.enter()
                else:
                        self.cursorOver = False
                        self.buttonModel.leave()
                self.update()

        

        def mouseReleaseEvent(self, event): 
                if self.cursorOver:
                        self.buttonModel.release()
                self.update()
        
        
        def mousePressEvent(self, event):
                if self.cursorOver:
                        self.buttonModel.press()
                self.update()
                
        def cursorOnEllipse(self, point):
                ellipse = QRegion(self.bbox,QRegion.Ellipse)
                if ellipse.contains(point): 
                        return True
                else:
                        return False

                        

def main(args):
        app = QApplication(args)
        window = MainWindow()
        window.resize(1000,800)
        canvasButton = CanvasButton()
        window.addCanvasButton(canvasButton)
        window.show()
        app.exec_()

        
if __name__ == "__main__":
	print("execution du programme")
	main(sys.argv)
        
