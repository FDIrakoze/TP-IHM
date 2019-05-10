import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ExpSetup(QDialog):

    IDUser = None
    technique = None
    densite = None
    taille = None
    repetitions = None

    def __init__(self, onOK, window):
        super().__init__()
        self.setWindowTitle('Display attachment')
        self.onOK = onOK
        self.window = window
        mainLayout = QVBoxLayout()

        line1 = QHBoxLayout()
        line1.addWidget(QLabel("Numero d'utilisateur : "))
        self.spinBoxUser = QSpinBox()
        line1.addWidget(self.spinBoxUser)
        mainLayout.addLayout(line1)

        line2 = QHBoxLayout()
        line2.addWidget(QLabel("Technique: "))
        self.cbTechnique = QComboBox()
        self.cbTechnique.addItems(["normal", "bubble", "rope"])
        line2.addWidget(self.cbTechnique)
        mainLayout.addLayout(line2)

        line3 = QHBoxLayout()
        line3.addWidget(QLabel("Densités : "))
        self.cbDensite = QComboBox()
        self.cbDensite.addItems(["haute", "faible"])
        line3.addWidget(self.cbDensite)
        mainLayout.addLayout(line3)

        line4 = QHBoxLayout()
        line4.addWidget(QLabel("Nombre de tailles de cibles : "))
        self.cbTaille = QComboBox()
        self.cbTaille.addItems(["petite", "grande"])
        line4.addWidget(self.cbTaille)
        mainLayout.addLayout(line4)

        line5 = QHBoxLayout()
        line5.addWidget(QLabel("Nombre de répétitions : "))
        self.spinBoxNb = QSpinBox()
        line5.addWidget(self.spinBoxNb)
        mainLayout.addLayout(line5)

        okButton = QPushButton('&Ok')
        okButton.clicked.connect(self.getInput)
        mainLayout.addWidget(okButton)
        self.setLayout(mainLayout)
        self.input=False

    def getInput(self):
        self.IDUser = self.spinBoxUser.value()
        self.technique = self.cbTechnique.currentText()
        self.densite = self.cbDensite.currentText()
        self.taille = self.cbTaille.currentText()
        self.repetitions = self.spinBoxNb.value()

        self.onOK(self, self.window)
        self.close()


