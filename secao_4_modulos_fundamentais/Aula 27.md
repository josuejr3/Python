
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













