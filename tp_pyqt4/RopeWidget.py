import csv
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from RopeCursor import *
from Target import *


class RopeWidget(QWidget):

    def __init__(self,file):
        super().__init__()
        self.targets = list()
        self.cursor = RopeCursor(self.targets)
        self.setMouseTracking(True)

        with open(file, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                self.targets.append(
                    Target(int(row[0]), int(row[1]), int(row[2])))
        
        self.cursor.selectTarget()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.cursor.paint(painter)
        for target in self.targets:
            target.paint(painter)

    def mouseMoveEvent(self, event):
        point = event.pos()
        self.cursor.move(point.x(), point.y())
        self.update()

    def mouseReleaseEvent(self, event):
        if (self.cursor.currentSelect.highlighted):
            self.cursor.currentSelect.toSelect = False
            self.cursor.selectTarget()
        self.update()
