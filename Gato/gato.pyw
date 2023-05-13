import sys
import numpy as np
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
t=1
A = np.zeros((3,3))
class gato_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("JuegoGato.ui",self)
        self.b1.clicked.connect(self.tiro1)
        self.b2.clicked.connect(self.tiro2)
        self.b3.clicked.connect(self.tiro3)
        self.b4.clicked.connect(self.tiro4)
        self.b5.clicked.connect(self.tiro5)
        self.b6.clicked.connect(self.tiro6)
        self.b7.clicked.connect(self.tiro7)
        self.b8.clicked.connect(self.tiro8)
        self.b9.clicked.connect(self.tiro9)
    
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
            if boton == 1: self.b1.setIcon(QtGui.QIcon("O.jpg")); self.b1.setEnabled(False); A[0,0] = 3
            if boton == 2: self.b2.setIcon(QtGui.QIcon("O.jpg")); self.b2.setEnabled(False); A[0,1] = 3
            if boton == 3: self.b3.setIcon(QtGui.QIcon("O.jpg")); self.b3.setEnabled(False); A[0,2] = 3
            if boton == 4: self.b4.setIcon(QtGui.QIcon("O.jpg")); self.b4.setEnabled(False); A[1,0] = 3
            if boton == 5: self.b5.setIcon(QtGui.QIcon("O.jpg")); self.b5.setEnabled(False); A[1,1] = 3
            if boton == 6: self.b6.setIcon(QtGui.QIcon("O.jpg")); self.b6.setEnabled(False); A[1,2] = 3
            if boton == 7: self.b7.setIcon(QtGui.QIcon("O.jpg")); self.b7.setEnabled(False); A[2,0] = 3
            if boton == 8: self.b8.setIcon(QtGui.QIcon("O.jpg")); self.b8.setEnabled(False); A[2,1] = 3
            if boton == 9: self.b9.setIcon(QtGui.QIcon("O.jpg")); self.b9.setEnabled(False); A[2,2] = 3
            if sum(A[0]) == 9: self.label.setPlainText("Jugador 1, ganaste"); self.b4.setEnabled(False); self.b5.setEnabled(False); self.b6.setEnabled(False); self.b7.setEnabled(False); self.b8.setEnabled(False); self.b9.setEnabled(False)
            if sum(A[1]) == 9: self.label.setPlainText("Jugador 1, ganaste"); self.b1.setEnabled(False); self.b2.setEnabled(False); self.b3.setEnabled(False); self.b7.setEnabled(False); self.b8.setEnabled(False); self.b9.setEnabled(False)
            if sum(A[2]) == 9: self.label.setPlainText("Jugador 1, ganaste"); self.b4.setEnabled(False); self.b5.setEnabled(False); self.b6.setEnabled(False); self.b1.setEnabled(False); self.b2.setEnabled(False); self.b3.setEnabled(False)
            if sum(A[:,0]) == 9: self.label.setPlainText("Jugador 1, ganaste"); self.b2.setEnabled(False); self.b3.setEnabled(False); self.b5.setEnabled(False); self.b6.setEnabled(False); self.b8.setEnabled(False); self.b9.setEnabled(False)
            if sum(A[:,1]) == 9: self.label.setPlainText("Jugador 1, ganaste"); self.b4.setEnabled(False); self.b1.setEnabled(False); self.b6.setEnabled(False); self.b7.setEnabled(False); self.b3.setEnabled(False); self.b9.setEnabled(False)
            if sum(A[:,2]) == 9: self.label.setPlainText("Jugador 1, ganaste"); self.b4.setEnabled(False); self.b5.setEnabled(False); self.b2.setEnabled(False); self.b7.setEnabled(False); self.b8.setEnabled(False); self.b1.setEnabled(False)
            if sum(A.diagonal()) == 9: self.label.setPlainText("Jugador 1, ganaste"); self.b4.setEnabled(False); self.b3.setEnabled(False); self.b6.setEnabled(False); self.b7.setEnabled(False); self.b8.setEnabled(False); self.b2.setEnabled(False)
            if sum(np.fliplr(A).diagonal()) == 9: self.label.setPlainText("Jugador 1, ganaste"); self.b4.setEnabled(False); self.b1.setEnabled(False); self.b6.setEnabled(False); self.b2.setEnabled(False); self.b8.setEnabled(False); self.b9.setEnabled(False)
            if A.sum() == 35: self.label.setPlainText("Gato")
            t = 2
        else : 
            if boton == 1: self.b1.setIcon(QtGui.QIcon("X.jpg")); self.b1.setEnabled(False); A[0,0] = 5
            if boton == 2: self.b2.setIcon(QtGui.QIcon("X.jpg")); self.b2.setEnabled(False); A[0,1] = 5
            if boton == 3: self.b3.setIcon(QtGui.QIcon("X.jpg")); self.b3.setEnabled(False); A[0,2] = 5
            if boton == 4: self.b4.setIcon(QtGui.QIcon("X.jpg")); self.b4.setEnabled(False); A[1,0] = 5
            if boton == 5: self.b5.setIcon(QtGui.QIcon("X.jpg")); self.b5.setEnabled(False); A[1,1] = 5
            if boton == 6: self.b6.setIcon(QtGui.QIcon("X.jpg")); self.b6.setEnabled(False); A[1,2] = 5
            if boton == 7: self.b7.setIcon(QtGui.QIcon("X.jpg")); self.b7.setEnabled(False); A[2,0] = 5
            if boton == 8: self.b8.setIcon(QtGui.QIcon("X.jpg")); self.b8.setEnabled(False); A[2,1] = 5
            if boton == 9: self.b9.setIcon(QtGui.QIcon("X.jpg")); self.b9.setEnabled(False); A[2,2] = 5
            if sum(A[0]) == 15: self.label.setPlainText("Jugador 2, ganaste"); self.b4.setEnabled(False); self.b5.setEnabled(False); self.b6.setEnabled(False); self.b7.setEnabled(False); self.b8.setEnabled(False); self.b9.setEnabled(False)
            if sum(A[1]) == 15: self.label.setPlainText("Jugador 2, ganaste"); self.b1.setEnabled(False); self.b2.setEnabled(False); self.b3.setEnabled(False); self.b7.setEnabled(False); self.b8.setEnabled(False); self.b9.setEnabled(False)
            if sum(A[2]) == 15: self.label.setPlainText("Jugador 2, ganaste"); self.b4.setEnabled(False); self.b5.setEnabled(False); self.b6.setEnabled(False); self.b1.setEnabled(False); self.b2.setEnabled(False); self.b3.setEnabled(False)
            if sum(A[:,0]) == 15: self.label.setPlainText("Jugador 2, ganaste"); self.b2.setEnabled(False); self.b3.setEnabled(False); self.b5.setEnabled(False); self.b6.setEnabled(False); self.b8.setEnabled(False); self.b9.setEnabled(False)
            if sum(A[:,1]) == 15: self.label.setPlainText("Jugador 2, ganaste"); self.b4.setEnabled(False); self.b1.setEnabled(False); self.b6.setEnabled(False); self.b7.setEnabled(False); self.b3.setEnabled(False); self.b9.setEnabled(False)
            if sum(A[:,2]) == 15: self.label.setPlainText("Jugador 2, ganaste"); self.b4.setEnabled(False); self.b5.setEnabled(False); self.b2.setEnabled(False); self.b7.setEnabled(False); self.b8.setEnabled(False); self.b1.setEnabled(False)
            if sum(A.diagonal()) == 15: self.label.setPlainText("Jugador 2, ganaste"); self.b4.setEnabled(False); self.b3.setEnabled(False); self.b6.setEnabled(False); self.b7.setEnabled(False); self.b8.setEnabled(False); self.b2.setEnabled(False)
            if sum(np.fliplr(A).diagonal()) == 15: self.label.setPlainText("Jugador 2, ganaste"); self.b4.setEnabled(False); self.b1.setEnabled(False); self.b6.setEnabled(False); self.b2.setEnabled(False); self.b8.setEnabled(False); self.b9.setEnabled(False)
            if A.sum() == 35: self.label.setPlainText("Gato")
            t = 1
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = gato_GUI()
    GUI.show()
    sys.exit(app.exec_())