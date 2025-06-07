
#### <span style="color:rgb(4, 255, 0)">Executando arquivos com argumentos no sistema</span>

Podemos usar o Python do ambiente virtual mesmo que ele não esteja ativado, isso para quando estamos rodando o programa direto no terminal.

Basicamente, basta ir diretmente ao Python que está na pasta venv ou env.

```Python
import sys  
  
# printa os argumentos que eu passei  
# semelhante ao que temos na main do c/c++  
  
print(sys.argv)  
  
argumentos = sys.argv  
qtd_argumentos = len(argumentos)  
print(qtd_argumentos)
```





