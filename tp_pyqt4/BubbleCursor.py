import sys
import time

from random import randint
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from scipy.spatial import distance
from datetime import datetime

from BubbleWidget import *


class BubbleCursor():

    defaultCol = QColor(Qt.green)

    def __init__(self, targets):
        self.size = 40
        self.x = 0 
        self.y = 0 
        self.targets = targets
        self.closest = None
        self.currentSelect = None
        self.start = time.time()

    def paint(self, painter):
        painter.setRenderHints(QPainter.Antialiasing)
        pen = QPen(QColor(Qt.black))
        pen.setWidth(2)

        ellipse = QRect(QPoint(self.x-(self.size/2), self.y-(self.size/2)),
                        QSize(self.size, self.size))

        painter.setBrush(self.defaultCol)
        painter.setPen(pen)
        painter.drawEllipse(ellipse)

    def move(self, x, y):
        self.x = x 
        self.y = y 
        dstMin = 10000

        for target in self.targets:
            a = (target.x, target.y)
            b = (self.x, self.y)
            dst = distance.euclidean(a, b) - (target.size/2)
            if(dstMin > dst):
                if (self.closest is not None):
                    self.closest.highlighted = False
                self.closest = target
                dstMin = dst

        self.closest.highlighted = True
        self.size = (dstMin * 2) 

    def selectTarget(self):
        random = randint(0, len(self.targets)-1)
        target = self.targets[random]
        target.toSelect = True
        self.currentSelect = target
        end = time.time()
        print(end - self.start)
        self.start = end
