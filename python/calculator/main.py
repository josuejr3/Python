import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from Info import Info
from MainWindow import MainWindow
from calculator.Buttons import Buttons
from calculator.ButtonsGrid import ButtonsGrid
from calculator.Display import Display
from calculator.Styles import setupTheme
from calculator.constants import WINDOW_ICON_PATH

if __name__ == '__main__':

    app = QApplication(sys.argv)
    setupTheme(app)

    window = MainWindow()

    # Info
    info = Info("2+2=4")

    # Display
    display = Display()
    window.addWidgetToVLayout(info)
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid()
    # adicionando um layout dentro de outro layout
    window.layoutToCenterWidget.addLayout(buttonsGrid)

    # Posicoes de linha e coluna e posicoes de expansao
    # buttonsGrid.addWidget(Buttons('1'), 0, 1, 1, 1)
    # buttonsGrid.addWidget(Buttons('2'), 0, 2, 1, 1)
    # buttonsGrid.addWidget(Buttons('3'), 0, 3, 1, 1)
    # buttonsGrid.addWidget(Buttons('4'), 1, 1, 1, 1)
    # buttonsGrid.addWidget(Buttons('5'), 1, 2, 1, 1)
    # buttonsGrid.addWidget(Buttons('6'), 1, 3, 1, 1)
    # buttonsGrid.addWidget(Buttons('7'), 2, 1, 1, 1)
    # buttonsGrid.addWidget(Buttons('8'), 2, 2, 1, 1)
    # buttonsGrid.addWidget(Buttons('9'), 2, 3, 1, 1)
    # buttonsGrid.addWidget(Buttons('0'), 3, 1, 1, 3)


    window.adjustFixedSize()
    window.show()
    app.exec()