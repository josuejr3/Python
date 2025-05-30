
#### <span style="color:rgb(4, 255, 0)">Uso do if name</span>

Basicamente, utilizamos o if name quando queremos deixar mais restrito a execução do código. 

> *Como assim, Josué?*

	Imagine que tenhamos dois arquivos, um com o código principal (main) e outro com apenas funções, prints, constantes e qualquer outra coisa que queiramos.

	O arquivo main importa o nosso segundo arquivo com todas as coisas. 


> Exemplo

```Python
# Arquivo secundario (modulo)

def soma(x: int, y: int) -> int:  
    return x + y  
  
print("aaaa")
```

```Python
# Arquivo principal (main)

from modulo import soma  
  
print(soma(1, 2))
```

Nessa situação, quando importamos o arquivo "modulo.py" para a nossa main podemos acabar importando algumas coisas desnecessárias, como foi o caso do "print('aaaa')"

Para resolver isso, usamos o if name, que de maneira simples, vai verificar se o arquivo está sendo executado diretamente, e se isso ocorrer ele executa um bloco de código específico, se não ele não executa. 

Ajustando nossos códigos anteriores teríamos o seguinte

```Python
# Arquivo secundario (modulo)

def soma(x: int, y: int) -> int:  
    return x + y  

if __name__ == "__main__":
	print("aaaa")
```

Dessa forma, quando o módulo for executado diretamente, ele vai executar tudo que está fora do if name, como também todo o if name. Já se estivermos executado a partir de outro módulo, como o principal, o que está no if name não será executado. 

Obs: em Python, quando executamos um arquivo diretamente, ele é denominado com __ main __ , enquanto que se ele for executado a partir de um outro arquivo o nome dele será o próprio nome do arquivo, ou seja, quando executo "modulo.py" diretamente o "__ name __ " dele é "main", mas se ele for importado e executado a partir de um outro arquivo .py (ex: principal.py) então o " __ name __ " dele vai ser "modulo.py"

Uma outra alternativa é criar uma função main com todo o código principal e utilizar essa função para ser rodada no if name.

