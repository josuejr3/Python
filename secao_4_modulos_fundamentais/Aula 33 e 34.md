
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

```Python
# import sys  
#  
# # printa os argumentos que eu passei  
# # semelhante ao que temos na main do c/c++  
#  
# print(sys.argv)  
#  
#  
# argumentos = sys.argv  
# qtd_argumentos = len(argumentos)  
# print(qtd_argumentos)  
  
  
# argparse.ArgumentParser para argumentos mais complexos  
# Tutorial Oficial:  
# https://doc s.python.orgpt-br/3/howto/argparse.html  
  
from argparse import ArgumentParser  
  
parser = ArgumentParser()  
parser.add_argument(  
    '-b',  
    '--basic',  
    help='Mostra "olá mundo" na tela',  
    #type=str, # tipo do argumento  
    metavar='STRING',  
    #default='Olá mundo', # valor padrão  
    required=True,  
    # action='append', # recebe o argumento mais de uma vez  
    # nargs='?', # recebe mais de um valor)  
args = parser.parse_args()  
  
# Para o algoritmo funcionar deve-se passar -b  
  
if args.basic is None:  
    print('Você não passou o valor de b')  
    print(args.basic)  
else:  
    print('O valor de é: ', args.basic)
```



