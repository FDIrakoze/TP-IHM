import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class MainWindow(QMainWindow):
        def __init__(self):
                super().__init__()

        def closeEvent(self, event):
                msg = QMessageBox()
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                returnVal = msg.exec_()
                print(returnVal)
                if returnVal == 16384:
                        self.close()
                else:
                    event.ignore()

        def new(self):
                print("new")

        def open(self):
                print("open")
                fileName = QFileDialog.getOpenFileName( self,"Open file", "/home/m1/lepretreg/Master",'*')
                file = open(fileName[0], 'r')
                text = file.read()
                textEdit = QTextEdit(self);
                textEdit.setPlainText(text)
                self.setCentralWidget(textEdit);
                file.close()


        def copy(self):
                print("copy")

        def save(self):
                print("save")
                fileName = QFileDialog.getOpenFileName( self,"Save file", "/home/m1/lepretreg/Master",'*')
                print(fileName)

        def quit(self):
               self.close()


        def addMenuAction(self,img, nom, shortcut, tip):
                newAct = QAction(QIcon(img), nom, self)
                newAct.setShortcut( shortcut )
                newAct.setToolTip(tip)
                newAct.setStatusTip(tip)
                newAct.setEnabled( True )
                return newAct

        def addMenuBar(self):
                bar = self.menuBar()
                fichierMenu = bar.addMenu("Fichier")

                newAct = self.addMenuAction("new.png", "New", "Ctrl+N", "New file")

                fichierMenu.addAction(newAct)
                newAct.triggered.connect(self.new)

                openAct = self.addMenuAction("open.png", "Open", "Ctrl+O", "Open file")
                fichierMenu.addAction(openAct)
                openAct.triggered.connect(self.open)

                saveAct = self.addMenuAction("save.png", "Save", "Ctrl+S", "Save file")
                fichierMenu.addAction(saveAct)
                saveAct.triggered.connect(self.save)

                copyAct = self.addMenuAction("copy.png", "Copy", "Ctrl+C", "Copy file")
                fichierMenu.addAction(copyAct)
                copyAct.triggered.connect(self.copy)

                quitAct = self.addMenuAction("quit.png", "Quit", "Ctrl+Q", "Quit")
                fichierMenu.addAction(quitAct)
                quitAct.triggered.connect(self.quit)

                fileToolBar = QToolBar("file")
                fileToolBar.addAction(newAct)
                fileToolBar.addAction(openAct)
                fileToolBar.addAction(saveAct)
                fileToolBar.addAction(copyAct)
                fileToolBar.addAction(quitAct)
                self.addToolBar(fileToolBar)
                self.setStatusBar(QStatusBar())

        def addTextEdit(self):
                textEdit = QTextEdit( self );
                self.setCentralWidget( textEdit );








def main(args):
        app = QApplication(args)
        window = MainWindow()
        window.addMenuBar()
        window.addTextEdit()
        window.show()
        app.exec_()


if __name__ == "__main__":
	print("execution du programme")
	main(sys.argv)
