from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from constants import *

class MainWindow(QMainWindow):
    # O argumento parent é uma "janela pai/mãe"
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configuração Layout básico

        # Definindo o Widget central
        self.centerWidget = QWidget()
        # Definindo o layout do Widget central
        self.layoutToCenterWidget = QVBoxLayout()
        # Aplicando o layout no Widget Central
        self.centerWidget.setLayout(self.layoutToCenterWidget)
        # Aplicando o Widget Central a minha Window
        self.setCentralWidget(self.centerWidget)
        # Alterando o nome da janela principal
        self.setWindowTitle("Calculadora")
        # Criando o ícone e alterando na janela
        self.iconWindow = QIcon(str(WINDOW_ICON_PATH))
        self.setWindowIcon(self.iconWindow)

    def addWidgetToVLayout(self, widget: QWidget) -> None:
        self.layoutToCenterWidget.addWidget(widget)
        #self.adjustFixedSize()

    def adjustFixedSize(self) -> None:
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())





