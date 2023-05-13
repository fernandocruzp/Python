import sys
from PyQt5.QtCore import *
from PyQt5  import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)
        atras = QAction('ATRAS', self)
        atras.triggered.connect(self.browser.back)
        navbar.addAction(atras)

        delante = QAction('Delante', self)
        delante.triggered.connect(self.browser.forward)
        navbar.addAction(delante)

        recarga = QAction('recarga', self)
        recarga.triggered.connect(self.browser.reload)
        navbar.addAction(recarga)

        inicio = QAction('inicio', self)
        inicio.triggered.connect(self.navega_casa)
        navbar.addAction(inicio)

        self.url_bar= QLineEdit()
        self.url_bar.returnPressed.connect(self.navega_url)
        navbar.addWidget(self.url_bar)

    def navega_casa(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navega_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))





app = QApplication(sys.argv)
QApplication.setApplicationName('Browser')
window = MainWindow()
app.exec_()
