
#### <span style="color:rgb(4, 255, 0)">Manipulação de Arquivos, Caminhos e Pastas com pathlib</span> 

A pathlib é boa para ser usada pois ela ajusta os caminhos de acordo com o sistema operacional. Isto é, ela "verifica" qual sistema está sendo utilizado e seleciona a barra ou a contra barra.

Isso evita que caminhos sejam escritos de forma hard coding, ou seja, caminhos escritos "manualmente".

-  Visualização de caminhos

```Python
from pathlib import Path  
  
caminho_projeto = Path()  
  
# Esse camuinho vai retornar o caminho relativo  
# Basicamente ele vai retornar o local atual, nesse caso um ponto  
  
print(caminho_projeto)  
  
# Caso seja necessário ver o caminho absoluto, basta chamar o método  
  
print(caminho_projeto.absolute())  
  
# Obtendo o caminho com o arquivo em si  
  
caminho_projeto = Path(__file__)  
print(caminho_projeto)  
  
# Obtendo a pasta anterior, ou "mãe/pai" da pasta analisada  
print(caminho_projeto.parent)  
# Como path retorna um path, então podemos chamar parent e depois um novo parent  
print(caminho_projeto.parent.parent)
```

-  Criação diretórios e acessando a pasta home

```Python
# Criando um novo caminho para uma nova pasta  
teste = Path().absolute() / "aula19_teste"  
print(teste / "ideias" / "file.txt")

print(Path.home())


# Criando de fato um novo arquivo  
Path.mkdir(teste)  
arquivo = teste / 'arquivoo_teste19.txt'  
arquivo.touch()  
print(arquivo)
```

Basicamente no código acima, antes de criar o arquivo, foi necessário criar a pasta, uma vez que ela não existia. Após isso, o arquivo txt foi criado. Ainda sobre o código acima, outra opção de criação de pasta seria chamar pelo diretório.

```Python
teste.mkdir(exist_ok=True)

# Podemos verificar a existência da pasta com um argumento da função mkdir, ou com uma função particular

if (teste.exists()):
	...
```

-  Exclusão, escrita e leitura de arquivos.

```Python
# Apagando o arquivo  
# Lembrando que o arquivo excluido nao vai pra lixeira  
# nao é possível recuperar  
arquivo.unlink()  
  
# Escrevendo arquivo  
arquivo = teste / 'arquivoo_teste19.txt'  
arquivo.touch()  
arquivo.write_text('OPA')  
  
print(arquivo.read_text())

# Removendo arquivos e pastas  
# Podemos remover pastas usando rmdir, porém ela so remove se a pasta estiver vazia  
# do contrario, é necessario fazer uma exclusão recursiva.

# Além disso, podemos usar funções da shutil para remoção em cascata ou "arvore"
```

