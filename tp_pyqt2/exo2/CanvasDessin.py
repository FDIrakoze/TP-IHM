import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Trace import *


class CanvasDessin(QWidget):
        #trace = Trace(2,QColor(Qt.red))
        
        def __init__(self):
                super().__init__()
                self.setMinimumSize(1000,800)
                self.listTrace = list()
                self.trace = None
                self.width = 2
                self.color = QColor(Qt.red)
        
        def paintEvent(self, event):
                painter = QPainter(self)
                pen = QPen(QColor())
                if len(self.listTrace)!=0:
                        for trace in self.listTrace:
                                path = QPainterPath()
                                pen.setColor(trace.color)
                                pen.setWidth(trace.width)
                                path.moveTo(trace.point[0].x(), trace.point[0].y())
                                i=1
                                while i < len(trace.point):
                                        path.lineTo(trace.point[i].x(), trace.point[i].y())
                                        i+=1
                                painter.setPen(pen)
                                painter.drawPath(path)
                
                
        def mouseReleaseEvent(self, event):
                print("release")
                self.listTrace.append(self.trace)
                self.trace = None
                self.update()
                      
        def mousePressEvent(self, event):
                print("press")
                self.trace = Trace(self.width, self.color)
                self.trace.point.append(event.pos())                
                self.update()
        
        def mouseMoveEvent(self, event):
                print("drag")
                self.trace.point.append(event.pos())
                self.update()
        def setColor(self, color):
                print('changing the color')
                self.color = color
        def setWidth(self, width):
                print("changing the width of the trace")
                self.width = width

        

