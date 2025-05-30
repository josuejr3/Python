
## Conext manager com classes - criando e usando gerenciadores de contexto

Duck typing - você pode implementar seus próprios protocolos apenas implementando os dunder methods que o Python vai usar.

O duck typing é um conceito relacionado a tipagem dinâmica onde o Python não está interessado no tipo. 

-  Basicamente o duck typing o Python associa da seguinte forma, se um ser nada como um pato, voa como um pato e come como um pato, provavelmente aquele ser é um pato. 

	Em relação ao context manager, como nós referimos a eles como arquivos ou coisas que abrem e fecham (um arquivo mesmo), para usar com classes deveremos ter que implementar os métodos mágicos de enter e exit

		O método "exit" deve receber a classe da exceção, a exceção e o traceback. Se ele retornar True, a exceção do with será suprimida.

		O retorno do metodo especial enter vai ser o nosso "as file" no context manager

===Obs: tudo que você for fazer que tenha

-  Abrir / fechar;
-  Conectar / desconectar
-  Capturar / liberar

Podemos fazer um context manager

```Python
# with open('aula149.txt', 'w') as file:  
#     ...  
class MyOpen:  
  
    def __init__(self, caminho_arquivo, modo):  
        self.caminho_arquivo = caminho_arquivo  
        self.modo = modo  
        self._arquivo = None  
  
    def __enter__(self):  
        # abrindo o arquivo  
        print('ABRINDO ARQUIVO')  
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf-8')  
        return self._arquivo  
  
    def __exit__(self, class_exception, exception_, tracebac_):  
        print('Fechando arquivo')  
        self._arquivo.close()  
  
  
with MyOpen('aula149.txt', 'w') as alguma_coisa:  
    alguma_coisa.write('LINHA1')  
    print('WITH', alguma_coisa)
```

Outra forma de criar context manager é usando um decorator que já vem por padrão na linguagem.

-  Como usamos o 'yield' se torna um generator.

```Python
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
	try: 
		print('abrindo arquivo')
		arquivo = open(caminhoo_arquivo, modo, encoding="utf8")
		yield arquivo
	except Exception as e:
		print('Ocorreu uma exceção', e)
	finally: 
		print("Fechando arquivo")
		arquivo.close()

with my_open('aula149.txt', 'w') as arquivo:
	arquivo.write('Linha1\n')
	arquivo.write('Linha2\n')
	arquivo.write('Linha3\n')
	print('WITH', arquivo)
```


