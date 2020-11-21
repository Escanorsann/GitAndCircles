from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 500))
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton = QPushButton(self)
        self.pushButton.move(25, 25)
        self.pushButton.resize(121, 51)
        self.pushButton.setText('Circles')


class Main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown', 'Black']
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        for i in range(10):
            self.qp.setBrush(QColor(choice(self.colors)))
            a = randint(25, 100)
            self.qp.drawEllipse(randint(50, 450),
                                randint(50, 450), a, a)
        self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
