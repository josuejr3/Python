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

    # botao
    botaoo = Buttons("RESULTADO")
    window.addWidgetToVLayout(botaoo)

    window.show()
    app.exec()