import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

turno = 1
class gato_GUI(QMainWindow):
    
    def __int__(self):
        super().__int__()
        uic.loadUi("Hola.ui",self)
        self.activo.clicked.connect(self.Activar)
        self.desactivo.clicked.connect(self.desactivar)
        
    def activar(self):
        self.activo.setEnabled()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = gato_GUI()
    GUI.show()
    sys.exit(app.exec_())