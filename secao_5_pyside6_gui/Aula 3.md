
#### <span style="color:rgb(4, 255, 0)">Resolvendo o problema de uma janela por widgets</span> 

Para resolver o problema de uma janela por widget vamos usar um widget especial, chamado de central widget.

Basicamente, quando temos uma janela, teremos um widget central que vai ser o único widget presente. A partir desse widget, aplicamos um layout e o layout é que vai "absorver" os widgets restantes.

```Python
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
```

Dessa forma temos a seguinte hierarquia de classes

-  QApplication (app)
	-  CentralWidget (central_widget)
		-  Layout (layout)
			-  Widgets no geral (botao1)
			-  Widgets (botao2)
















