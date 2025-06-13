from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget,
                               QGridLayout, QMainWindow)

app = QApplication()
window = QMainWindow()
window.setWindowTitle("Meu Programa")
window.setWindowIcon(QIcon("favicon-32x32.png"))
central_widget = QWidget()
window.setCentralWidget(central_widget)

botao = QPushButton("Botão 1")
botao.setStyleSheet("font-size: 25px; color: #0000FF; font-weight: bold;")

botao2 = QPushButton("Botão 2")
botao2.setStyleSheet("font-size: 25px; color: #0000FF; font-weight: bold;")

botao3 = QPushButton("Botão 3")
botao3.setStyleSheet("font-size: 25px; color: #0000FF; font-weight: bold;")

# Widget generico

# Cria um layout vertical
layout = QGridLayout()
central_widget.setLayout(layout)
# Adicionando o botao ao layout
layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# Pegando a statusbar da QMainWindow
status_bar = window.statusBar()
status_bar.showMessage('BARRA DE STATUS')

# Pegando menubar do QMainWindow
menu = window.menuBar()
primeiro_menu = menu.addMenu("Qualquer coisa")
primeira_acao = primeiro_menu.addAction("Primeira ação") #  type:ignore

def slot_example(status_bar):
    status_bar.showMessage('Slot foi executado')

# se o botao for pressionado
primeira_acao.triggered.connect(lambda: slot_example(status_bar))


# Mostre na janela
window.show()
app.exec()