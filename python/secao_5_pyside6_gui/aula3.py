from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication()

botao = QPushButton("Botão 1")
botao.setStyleSheet("font-size: 25px; color: #0000FF; font-weight: bold;")

botao2 = QPushButton("Botão 2")
botao2.setStyleSheet("font-size: 25px; color: #0000FF; font-weight: bold;")

botao3 = QPushButton("Botão 3")
botao3.setStyleSheet("font-size: 25px; color: #0000FF; font-weight: bold;")

# Widget generico
central_widget = QWidget()
# Cria um layout vertical
layout = QGridLayout()
central_widget.setLayout(layout)
# Adicionando o botao ao layout
layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# Mostre na janela
central_widget.show()
app.exec()