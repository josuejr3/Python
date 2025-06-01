
#### <span style="color:rgb(4, 255, 0)">Introdução ao módulo os - módulo para comunicação com SO</span>

O módulo os é destinado para que o código fonte possa interagir com o sistema operacional. Um exemplo disso é o módulo de path que fornece funções para conseguirmos trabalhar com caminhos de arquivos, como por exemplo a listagem de arquivos em um determinado diretório. Enquanto que o comando de system permite executar comandos de terminal a partir de um código Python.

```Python
import os  
  
#os.system('echo "hello world"')  
os.system("cls")
```

#### <span style="color:rgb(4, 255, 0)">os.path módulo que manipula caminhos</span>

O módulo os.path trabalha com caminhos em Windows, Linux e Mac sem se preocupar com as diferenças entre esses SOs.

-  Exemplos do que podemos ver com os.path

1. os.path.join - junta strings em um único caminho.
2. os.path.split - divide em diretório e arquivo.
3. os.path.exists - verifica se um caminho especificado existe.
4. os.path - só trabalha com caminhos de arquivos e não faz nenhuma operação de I/O com arquivos em si

```Python
caminho = os.path.join("Desktop", "curso", "arquivo.txt")  
print(caminho)  
diretorio, arquivo = os.path.split(caminho)  
caminho_arquivo, extensao = os.path.splitext(caminho)  
print(caminho_arquivo)  
print(extensao)  
  
# Verifica se existe o diretorio  
print(os.path.exists(caminho))  
  
# caminho absoluto  
print(os.path.abspath(caminho))  
  
# printa o diretorio  
print(os.path.dirname(caminho))
```

-  Links importantes para documentação

	https://docs.python.org/3/library/os.path.html#module-os.path
















