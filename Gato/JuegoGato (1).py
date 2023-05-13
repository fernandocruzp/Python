import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
t=1
class gato_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("JuegoGato.ui",self)
        self.B1.clicked.connect(self.tiro1)
        self.B2.clicked.connect(self.tiro2)
        self.B3.clicked.connect(self.tiro3)
        self.B4.clicked.connect(self.tiro4)
        self.B5.clicked.connect(self.tiro5)
        self.B6.clicked.connect(self.tiro6)
        self.B7.clicked.connect(self.tiro7)
        self.B8.clicked.connect(self.tiro8)
        self.B9.clicked.connect(self.tiro9)
    
    def tiro1(self): self.b_disable(1,t)
    def tiro2(self): self.b_disable(2,t)
    def tiro3(self): self.b_disable(3,t)    
    def tiro4(self): self.b_disable(4,t)
    def tiro5(self): self.b_disable(5,t)
    def tiro6(self): self.b_disable(6,t)
    def tiro7(self): self.b_disable(7,t)
    def tiro8(self): self.b_disable(8,t)
    def tiro9(self): self.b_disable(9,t)

    def b_disable(self,boton,turno):
        global t
        if turno == 1 : 
            if boton == 1: self.B1.setIcon(QtGui.QIcon("O.jpg")); self.B1.setEnabled(False)
            if boton == 2: self.B2.setIcon(QtGui.QIcon("O.jpg")); self.B2.setEnabled(False)
            if boton == 3: self.B3.setIcon(QtGui.QIcon("O.jpg")); self.B3.setEnabled(False)
            if boton == 4: self.B4.setIcon(QtGui.QIcon("O.jpg")); self.B4.setEnabled(False)
            if boton == 5: self.B5.setIcon(QtGui.QIcon("O.jpg")); self.B5.setEnabled(False)
            if boton == 6: self.B6.setIcon(QtGui.QIcon("O.jpg")); self.B6.setEnabled(False)
            if boton == 7: self.B7.setIcon(QtGui.QIcon("O.jpg")); self.B7.setEnabled(False)
            if boton == 8: self.B8.setIcon(QtGui.QIcon("O.jpg")); self.B8.setEnabled(False)
            if boton == 9: self.B9.setIcon(QtGui.QIcon("O.jpg")); self.B9.setEnabled(False)
            t = 2
        else : 
            if boton == 1: self.B1.setIcon(QtGui.QIcon("X.jpg")); self.B1.setEnabled(False)
            if boton == 2: self.B2.setIcon(QtGui.QIcon("X.jpg")); self.B2.setEnabled(False)
            if boton == 3: self.B3.setIcon(QtGui.QIcon("X.jpg")); self.B3.setEnabled(False)
            if boton == 4: self.B4.setIcon(QtGui.QIcon("X.jpg")); self.B4.setEnabled(False)
            if boton == 5: self.B5.setIcon(QtGui.QIcon("X.jpg")); self.B5.setEnabled(False)
            if boton == 6: self.B6.setIcon(QtGui.QIcon("X.jpg")); self.B6.setEnabled(False)
            if boton == 7: self.B7.setIcon(QtGui.QIcon("X.jpg")); self.B7.setEnabled(False)
            if boton == 8: self.B8.setIcon(QtGui.QIcon("X.jpg")); self.B8.setEnabled(False)
            if boton == 9: self.B9.setIcon(QtGui.QIcon("X.jpg")); self.B9.setEnabled(False)
            t = 1
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = gato_GUI()
    GUI.show()
    sys.exit(app.exec_())