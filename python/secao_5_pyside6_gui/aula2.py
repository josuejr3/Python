from PySide6.QtWidgets import QApplication, QPushButton

# QApplication é responsável por gerenciar a aplicação
# Ele não exibe nada na tela

# No QApplication eu poderia instanciar ele passando argv
app = QApplication()

# Instancia o botão
botao = QPushButton('Texto Botão')
botao.setStyleSheet("font-size: 25px; color: #0000FF; font-weight: bold;")

# botao2 = QPushButton('Texto Botão')
# botao2.setStyleSheet("font-size: 40px;")

# Adiciona o widget na hierarquia e exibe a janela
botao.show()
# botao2.show()

# Executa o loop da aplicação
app.exec()