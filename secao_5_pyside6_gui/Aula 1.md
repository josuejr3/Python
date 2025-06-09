
#### <span style="color:rgb(4, 255, 0)">PySide6</span> 

PySide6 para GUI (Interface Gráfica) com Qt em Python. As bibliotecas PySide e PyQt tem como base o uso de bibliotecas Qt. 

Qt é uma biblioteca usada para criação de GUI escrita em C++. O PySide e o PyQt conseguem fazer a ponte (binding) entre o Python e a biblioteca para criação de interfaces gráficas sem ter que usar outra linguagem de programação. 

-  O PySide6 é uma referência à versão 6 do Qt (Qt 6)
-  O Qt é uma multiplataforma, ou seja, deve funcionar em Wndows, Linux e Mac.

A mudança de PyQt para PySide

-  A mudança foi necessária, pois PySide foi desenvolvida pela The Qt Company (da Nokia), como parte do projeto Qt for Python Project - https://doc.qt.io/qtforpython/
-  Por usarem a mesma biblioteca (Qt), PySide e PyQt são etremamente similares, muitas vezes os códigos são idênticos. Portanto, mesmo que você ainda queira usar PyQt será muito simples de portar os códigos. Muitas vezes basta trocar o nome de PySide para PyQt e vice-versa.
-  A maior diferença entre os dois está na licença 

	-  PyQt usa GPL ou comercial;
	-  PySide usa LGPL

