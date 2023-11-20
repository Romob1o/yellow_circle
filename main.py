import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randrange


class YellowCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.paint = False
        self.pushButton.clicked.connect(self.paint_action)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.paint = False

    def paint_action(self):
        self.paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        d = randrange(20, 300)
        qp.drawEllipse(200, 150, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec())