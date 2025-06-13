
#### <span style="color:rgb(4, 255, 0)">Utilizando</span> <span style="color:rgb(4, 255, 0)">QMainWindow</span> 

O widget que usamos como base, o QWidget é muito genérico e simples. Sendo assim, nós podemos usar um melhor, chamado de QMainWindow. Ficamos com a seguinte hierarquia.

-  QApplication (app)
	-  QMainWindows
		-  CentralWidget (central_widget)
			-  Layout (layout)
				-  Widget 1 (botao1)
				-  Widget 2 (botao2)
				-  Widget 3 (botao3)