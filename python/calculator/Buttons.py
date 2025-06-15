from PySide6.QtWidgets import QPushButton

from calculator.constants import MEDIUM_FONT_SIZE


class Buttons(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()
        #self.setCheckable(True)
        #self.resize(40, 40)

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        # Não foi usado o setStyleSheet para não sobreescrever o estilo dark
        # font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(1, 60)
        #self.setProperty('cssClass', "specialButton")
