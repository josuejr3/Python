
Na computação, um ambiente pode ser definido como um *"estado"*, uma combinação de hardware e software específica.

-  Um servidor com GNU/Linux Slackware;
-  Uma máquina virtual com macOS Mojave;
-  Um container windows server 2022.

> Exemplo 

Um sistema para rodar deve estar em um Windows 11 com a versão X e service pack 2 - Esse seria o ambiente, (físico ou lógico).

*O ambiente é uma captura de um estado em que nosso sistema vai rodar, ou de coisas que ela necessita para rodar.*

<div align="center"><img src="env.png"/></div>

-  O ambiente pode ser composto por arquivos que também fazem parte do ambiente

De maneira geral, uma aplicação depende de três fatores:

-  Ambiente;
-  Dependências (bibliotecas da linguagem);
-  Serviços de apoio (banco de dados, caches, serviços de e-mail e APIs externas).

> O mais importante, o banco de dados por exemplo, onde ele está no sistema?

<mark style="background: #ABF7F7A6;">Obs</mark>

As variáveis de ambiente que criamos no nosso sistema ou que modificamos são validas apenas no nosso sistema.

-  Podemos usar o getenv para verificar se uma variável de ambiente existe;
-  Ou também podemos usar o environ

```Python
from os import environ, getenv  
  
# getenv identifica se a variavel de ambiente existe  
# se sim, ela retorna  
  
print(getenv('SPLASH'))  
print(getenv('XPTO'), 'fritas')  
getenv()
```

---

Para facilitar o carregamento das variáveis de ambiente nós podemos fazer isso em um único arquivo.

O nome de arquivo de configuração de ambiente é *".env"*

> Para ler esse tipo de arquivo, usamos a biblioteca python-dotenv

-  load_dotenv()
-  dotenv_values()
