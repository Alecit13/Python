from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainApp(QMainWindow):
    def __init__(self,parent=None,*args):
        super(MainApp,self).__init__(parent)
        self.setWindowTitle("Nivel 1")
        self.setFixedSize(500,500)
        self.setStyleSheet("background-color: black;")
if __name__ == '__main__': 
    app=QApplication([])   #Inicia la aplicación
    window = MainApp() 
    window.show()
    app.exec_()