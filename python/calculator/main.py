import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    cw = QWidget()

    vlayout = QVBoxLayout()
    cw.setLayout(vlayout)

    label1 = QLabel('Meu texto')
    vlayout.addWidget(label1)

    window.setCentralWidget(cw)
    window.show()

    app.exec()