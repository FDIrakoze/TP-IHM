import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Target():

    defaultCol = QColor(Qt.cyan)
    toSelectCol = QColor(Qt.red)
    highlightCol = QColor(Qt.darkBlue)

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.toSelect = False
        self.highlighted = False

    def paint(self, painter):
        painter.setRenderHints(QPainter.Antialiasing)
        pen = QPen(QColor(Qt.black))
        pen.setWidth(2)

        ellipse = QRect(QPoint(self.x-(self.size/2), self.y -
                               (self.size/2)), QSize(self.size, self.size))

        if self.toSelect:
            painter.setBrush(self.toSelectCol)
        elif self.highlighted:
            painter.setBrush(self.highlightCol)
        else:
            painter.setBrush(self.defaultCol)

        painter.setPen(pen)
        painter.drawEllipse(ellipse)