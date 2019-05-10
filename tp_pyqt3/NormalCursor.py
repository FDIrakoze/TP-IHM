import sys
import time

from random import randint
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from scipy.spatial import distance

from NormalWidget import *


class NormalCursor():

    defaultCol = QColor(Qt.green)

    def __init__(self, targets):
        self.targets = targets
        self.currentSelect = None
        self.currentHilight = None
        self.start = time.time()

    def move(self, event):
        if (self.currentHilight is not None):
            self.currentHilight.highlighted = False

        for target in self.targets:
            if self.cursorOnTarget(target, event.pos()):
                target.highlighted = True
                self.currentHilight = target

    def cursorOnTarget(self, target, point):
        ellipse = QRegion(QRect(QPoint(target.x-(target.size/2), target.y-(target.size/2)), QSize(
            target.size, target.size)), QRegion.Ellipse)
        if ellipse.contains(point):
            return True
        else:
            return False

    def selectTarget(self):
        random = randint(0, 99)
        target = self.targets[random]
        target.toSelect = True
        self.currentSelect = target
        end = time.time()
        print(end - self.start)
        self.start = end
