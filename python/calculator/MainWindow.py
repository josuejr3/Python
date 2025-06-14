from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    # O argumento parent é uma "janela pai/mãe"
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Definindo o Widget central
        self.central_widget = QWidget()

        # Definindo o layout do Widget central
        self.layout_to_cwidget = QVBoxLayout()

        # Aplicando o layout no Widget Central
        self.central_widget.setLayout(self.layout_to_cwidget)

        # Aplicando o Widget Central a minha Window
        self.setCentralWidget(self.central_widget)

        # Alterando o nome da janela principal
        self.setWindowTitle("Calculator")


    def adjustFixedSize(self):
        
        # Última coisa a ser feita
        # self.adjustSize()
        # self.setFixedSize(self.width(), self.height())





