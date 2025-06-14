from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from constants import *

class MainWindow(QMainWindow):
    # O argumento parent é uma "janela pai/mãe"
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configuração Layout básico

        # Definindo o Widget central
        self.central_widget = QWidget()

        # Definindo o layout do Widget central
        self.layout_to_central_widget = QVBoxLayout()

        # Aplicando o layout no Widget Central
        self.central_widget.setLayout(self.layout_to_central_widget)

        # Aplicando o Widget Central a minha Window
        self.setCentralWidget(self.central_widget)

        # Alterando o nome da janela principal
        self.setWindowTitle("Calculator")

        # Criando o ícone e alterando na janela
        self.icon = QIcon(str(WINDOW_ICON_PATH))
        self.setWindowIcon(self.icon)

    def addWidgetToVLayout(self, widget: QWidget) -> None:
        self.layout_to_central_widget.addWidget(widget)
        # self.adjustFixedSize()

    def adjustFixedSize(self) -> None:
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())





