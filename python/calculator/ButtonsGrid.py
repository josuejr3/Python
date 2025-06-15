from typing import TYPE_CHECKING

# Basicamente essa variavel serve so para checar tipos
# quando estiver checando tipo essa variavel é True
# quando o codigo estiver executado ela é False

if TYPE_CHECKING:
    from Display import Display
    from Info import Info

# Usado para circular import


from PySide6.QtWidgets import QGridLayout
from Buttons import Buttons
from calculator.utils import isValidNumber
from utils import isNumOrDot, isEmpty
# from Display import Display
from PySide6.QtCore import Slot
# from Info import Info

class ButtonsGrid(QGridLayout):
    def __init__(self, display: "Display", info: "Info", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', 'xⁿ', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '=']
        ]

        self.display = display
        self.info = info
        self._makeGrid()


    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Buttons(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', "specialButton")
                    #button.style().unpolish(button)
                    #button.style().polish(button)

                self.addWidget(button, i, j)
                buttonSlot = self._makeButtonDisplaySlot(self._insertButtonTextToDisplay,button)
                button.clicked.connect(buttonSlot)


    def _makeButtonDisplaySlot(self, method, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            method(*args, **kwargs)
        return realSlot


    def _insertButtonTextToDisplay(self, button):

        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText
        print(newDisplayValue)

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(button.text())
