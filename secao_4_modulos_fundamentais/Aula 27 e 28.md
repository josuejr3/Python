
#### <span style="color:rgb(4, 255, 0)">Variáveis de Ambiente</span>

Variáveis de ambiente, como o próprio nome já diz, são variáveis referentes ao próprio ambiente, ou seja, o seu sistema operacional.

Sistemas requerem muitas configurações, como por exemplo, um sistema que se conecta a uma base de dados. Para isso, é necessário saber usuário, senha, host e porta da base de dados. Essas configurações, normalmente são voltadas para o seu ambiente. 

> ~={green}Exemplo=~

Quando um programa que está sendo desenvolvido em um computador PC1 e esse programa necessita de acessar uma base de dados que também está em PC1 significa que como eles estão acessando o mesmo local, o mesmo PC1 as variáveis são locais.

Esse mesmo programa junto com a base de dados pode ir para um *ambiente de teste*, que terá as mesmas coisas que o servidor local, porém servirá como teste. E por fim, todo o bloco de programa vai para um *ambiente de produção.*

Para maximizar a segurança de programas, como proteção de senhas e usuários, nós usamos as variáveis de ambiente.

-  Criação de variável de ambiente no Power Shell

```ps
PS C:\Users\josue> $env:VARIAVEL="VALOR"
```

-  Para ver o valor da variável

```ps
dir env:
```

Lembrando que quando usamos o comando de criação acima e no terminal a variável de ambiente só irá existir enquanto o terminal estiver aberto.

---

#### <span style="color:rgb(4, 255, 0)">Variáveis de ambiente no Python</span>

No Python, há um arquivo que carregamos assim que o programa é iniciado. O nome desse arquivo é "dotenv". Esse arquivo carregará todas as variáveis de ambiente que desejar.

Além do arquivo dotenv eu preciso de um dotenv-example para indicar para o próximo programador que for ver o projeto que ele necessita criar um novo dotenv

```python
# Variáveis de Ambiente  
import os  
  
from dotenv import load_dotenv # type: ignore  
  
# Por padrão, o load_dotenv vai buscar na raiz do projeto  
load_dotenv()  
  
# printa todas as variaveis de ambiente  
#print(os.environ)  
  
# aqui eu vou pegar a variavel que eu quero e ele retorna o valor  
print(os.getenv('PASSWORD_BD'))  
  
# criar um arquivo .env-example
```


-  Outra explicação

```
`python-dotenv` é uma biblioteca Python que permite que você faça uso de arquivos de configuração para armazenar e acessar as suas variáveis de ambiente de forma mais fácil e segura em seus projetos.

As variáveis de ambiente são valores que podem ser usados em seu código e que podem variar dependendo do ambiente em que o seu código está sendo executado (por exemplo, o ambiente de produção ou o ambiente de desenvolvimento).

Para utilizar o `python-dotenv`, basta instalá-lo com o pip e, em seguida, adicionar um arquivo chamado .env na raiz do seu projeto.

1. # Ative seu ambiente virtual
2. pip install python-dotenv

Esse arquivo deve conter as suas variáveis de ambiente e seguir o seguinte formato:

1. # .env
2. VARIAVEL_DE_AMBIENTE_1=valor
3. VARIAVEL_DE_AMBIENTE_2=valor
4. VARIAVEL_DE_AMBIENTE_3=valor

Em seu código, você pode acessar essas variáveis usando o módulo os e a função `os.getenv()`, por exemplo:

1. import os

2. valor_da_variavel_1 = os.getenv("VARIAVEL_DE_AMBIENTE_1")

O `python-dotenv` funciona lendo o arquivo `.env` e adicionando as variáveis de ambiente ao ambiente do sistema operacional, de forma que elas fiquem disponíveis para seu código usando a função `os.getenv()`.

Isso é útil, por exemplo, para não expor senhas ou outras informações confidenciais em seu código ou em repositórios de código compartilhados, pois o arquivo `.env` pode ser adicionado ao `.gitignore` para não ser incluído nos commits. Crie um `.env-example` para exemplificar como usar o seu programa com valores fictícios.

Além disso, o `python-dotenv` também permite que você use um arquivo `.env` para armazenar valores de configuração específicos de cada ambiente, o que pode ser útil quando você estiver trabalhando em um projeto com diferentes ambientes de desenvolvimento, teste e produção.

Doc: [https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)
```











