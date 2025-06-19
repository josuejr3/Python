from typing import TYPE_CHECKING

# Basicamente essa variavel serve so para checar tipos
# quando estiver checando tipo essa variavel é True
# quando o codigo estiver executado ela é False

if TYPE_CHECKING:
    from Display import Display
    from Info import Info
    from calculator.MainWindow import MainWindow

# Usado para circular import

from math import pow
from PySide6.QtWidgets import QGridLayout, QMessageBox
from Buttons import Buttons
from calculator.utils import isValidNumber
from utils import isNumOrDot, isEmpty, convertToNumber
# from Display import Display
from PySide6.QtCore import Slot
# from Info import Info

class ButtonsGrid(QGridLayout):
    def __init__(self, display: "Display", info: "Info", window: "MainWindow", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '=']
        ]

        self.window = window
        self.display = display
        self.info = info
        self._makeGrid()
        self._equation = ""
        self._equationInitialValue = "Sua Conta"

        self.equation = self._equationInitialValue

        self._left = None
        self._right = None
        self._operator = None

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):

        self.display.entPressed.connect(self._eq)
        self.display.delPressed.connect(self._backSpace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self.configLeftOp)

        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Buttons(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', "specialButton")
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertToDisplay, buttonText)
                self._connectButtonClicked(button, slot)

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.setWindowTitle('Erro')
        msgBox.exec()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.setWindowTitle('Informação')
        msgBox.exec()

    # def _showError(self, text):
    #     msgBox = self._makeDialog(text)
    #     msgBox.setIcon(msgBox.Icon.Warning)
    #     msgBox.setWindowTitle('Erro')
    #     msgBox.setStandardButtons(
    #         # msgBox.StandardButton.Ok | msgBox.StandardButton.Cancel | msgBox.StandardButton.Close
    #         msgBox.StandardButton.Ok
    #     )
    #     # Botão personalizado
    #     # msgBox.button(msgBox.StandardButton.NoToAll).setText("Não para Todos")
    #     msgBox.exec()
    #     # Para capturar qual botão foi obtido, basta criar uma variavel para o exec



    def _configSpecialButton(self, button):
        text = button.text()

        if text == "C":
            #slot = self._makeSlot(self.display.clear)
            self._connectButtonClicked(button, self._clear)

        if text in "+-/*^":
            self._connectButtonClicked(
                button,
                self._makeSlot(self.configLeftOp, text)
            )

        if text == '◀':
            self._connectButtonClicked(button, self._backSpace)

        if text == "=":
            self._connectButtonClicked(button, self._eq)

        if text == "N":
            self._connectButtonClicked(button, self._invertNumber)

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            #self._showInfo("Não há outro número para formar a expressão")
            return

        newNumber = convertToNumber(displayText) * -1

        self.display.setText(str(newNumber))


    @Slot()
    def _backSpace(self):
        self.display.backspace()
        self.display.setFocus()


    @Slot()
    def _eq(self):
        displayText = self.display.text()
        # tipando a variavel _left
        self._left: float

        if not isValidNumber(displayText) or self._left is None:
            self._showInfo("Não há outro número para formar a expressão")
            return

        self._right = convertToNumber(displayText)
        self.equation = f"{self._left}{self._operator}{self._right}"

        result = 'Error'
        try:
            if '^' in self.equation and isinstance(self._left, (float | int)):
                result = pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError("Divisão por Zero")
        except OverflowError:
            self._showError("Erro de sobrecarga")

        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")
        self._left = convertToNumber(result)
        self._right = None

        if result == "Error":
            self._left = None

        self.display.setFocus()


    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    @Slot()
    def _makeSlot(self, method, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            method(*args, **kwargs)
        return realSlot

    @Slot()
    def _insertToDisplay(self, text):

        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()


    @Slot()
    def configLeftOp(self, text):
        displayText = self.display.text()                  # deverá ser o numero da esquerda
        self.display.clear()
        self.display.setFocus()
        # limpa o display

        # Se clicou no operador sem escolher um número antes
        if not isValidNumber(displayText) and self._left is None:
            self._showError("Não há nenhum valor inserido no campo esquerdo")
            return

        # Se já existe algo no número da esquerda
        if self._left is None:
            self._left = convertToNumber(displayText)

        self._operator = text
        self.equation = f"{self._left} {self._operator}"

        print(self.equation)











