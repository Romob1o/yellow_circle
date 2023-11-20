import sys
import io

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randrange


class DesignUI:
    def __init__(self):
        self.template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>330</x>
      <y>230</y>
      <width>93</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Нажми меня</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""

    def get_temp(self):
        return self.template


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(DesignUI().get_temp())
        uic.loadUi(f, self)
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
        qp.setBrush(QColor(randrange(10, 240), randrange(10, 240), randrange(10, 240)))
        d = randrange(20, 300)
        qp.drawEllipse(200, 150, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())