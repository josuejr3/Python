import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

from MainWindow import MainWindow
from calculator.constants import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    label1 = QLabel('1')
    label2 = QLabel('2')
    window.addWidgetToVLayout(label1)
    window.addWidgetToVLayout(label2)

    window.show()

    app.exec()