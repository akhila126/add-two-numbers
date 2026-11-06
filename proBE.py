from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from proFE import *


class Akhila(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add)


    def add(self):
        a = float(self.ui.lineEdit.text())
        b = float(self.ui.lineEdit_2.text())
        c = a + b
        self.ui.label_3.setText(f"The sum is : {c}")

if __name__=="__main__":

    app = QApplication(sys.argv)
    w = Akhila()
    w.show()
    sys.exit(app.exec_())

