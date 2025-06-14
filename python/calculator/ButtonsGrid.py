from PySide6.QtWidgets import QGridLayout
from Buttons import Buttons

class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', 'xⁿ', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '=']
        ]

        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Buttons(buttonText)

                if buttonText not in '0123456789.':
                    button.setProperty('cssClass', "specialButton")
                    #button.style().unpolish(button)
                    #button.style().polish(button)

                self.addWidget(button, i, j)