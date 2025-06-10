
#### <span style="color:rgb(4, 255, 0)">QApplication e QPushButtom de PySide6.QtWidgets</span>

Como a biblioteca foi escrita em C++, significa que na maioria das vezes nos vamos trabalhar com classes. Em resumo, tudo será um objeto.

> ~={green}Exemplos=~

-  QApplication

Basicamente gerencia o loop de eventos da aplicação. Funciona a classe principal.

-  QPushButton

> ~={green}*O que são Widgets?*=~

Widgets são quaisquer elementos que estejam na tela.

<mark style="background: #FF5582A6;">Obs: o QApplication gerencia uma janela por widget, sendo assim, quando instanciamos dois botões, cada botão será uma janela.</mark>

Código

```Python
from PySide6.QtWidgets import QApplication, QPushButton  
  
# QApplication é responsável por gerenciar a aplicação  
# Ele não exibe nada na tela  
  
# No QApplication eu poderia instanciar ele passando argv  
app = QApplication()  
  
# Instancia o botão  
botao = QPushButton('Texto Botão')  
botao.setStyleSheet("font-size: 40px;")  
  
# botao2 = QPushButton('Texto Botão')  
# botao2.setStyleSheet("font-size: 40px;")  
  
# Adiciona o widget na hierarquia e exibe a janela  
botao.show()  
# botao2.show()  
  
# Executa o loop da aplicação  
app.exec()
```

