
#### <span style="color:rgb(4, 255, 0)">Colunas com tipo datetime (created_at e updated_at)</span> 

Para criarmos campos com a data de criação e a data de update de um dado, precismos usar o código .yml do docker.

-  Após o código modificado no arquivo .yml, devemos criar uma nova coluna em uma tabela desejada.

```yml
version: "3"  
services:  
  mysql_knex:  
    container_name: mysql_knex  
    hostname: mysql_knex  
    image: mysql:8.0.42  
    restart: always  
    command:  
      - --default-authentication-plugin=mysql_native_password  
      - --character-set-server=utf8mb4  
      - --collation-server=utf8mb4_unicode_ci  
      - --innodb_force_recovery=0  
    volumes:  
      - D:\Josue\Cursos\Python\python\secao_6_sql_mysql\docker:/var/lib/mysql  
    ports:  
      - 3306:3306  
    environment:  
      MYSQL_ROOT_PASSWORD: senha  
      MYSQL_DATABASE: base_de_dados  
      MYSQL_USER: usuario  
      MYSQL_PASSWORD: senha  
      TZ: America/Sao_Paulo
```

-  O caminho a se seguir é o seguinte

1. Seleciona a Tabela em que se deseja colocar uma coluna de created_at e updated_at;
2. Ir em propriedades e adicionar uma nova coluna;
3. O tipo da variável pode ser dois, ou datetime ou apenas date. Nesse caso vamos usar datetime;
4. As datas de criação podem ser inseridas manualmente, porém, para automatizar no campo "Padrão", colocamos a função "NOW()" que retorna a hora e data atual e vai salvar no registro;
5. Após salvar, temos o seguinte

```SQL
ALTER TABLE base_de_dados.users ADD created_at DATETIME DEFAULT NOW() NOT NULL;
```

Esse código quer dizer o seguinte.

-  Já temos uma tabela e estamos alterando ela (base_de_dados.users) - Tabela Users
-  Estamos acrescentando a coluna *"created_at"* que é do tipo DATETIME
-  O valor padrão de cada linha nessa coluna é "NOW()" que retorna a data e o horário atual
-  E o valor não pode ser nulo "NOT NULL".

> ~={green}Exemplo=~

![[Exemplo created_at.png]]

<mark style="background: #FF5582A6;">Obs: se for digitada uma data qualquer, o horário vai ser por padrão 00h. Além disso, se o dado for alterado, a coluna created_at não é atualizada</mark>

Para resolver esse problema, basta criarmos uma nova coluna chamada *"updated_at"* que vai monitorar quando nossos dados forem alterados. A única diferença na configuração dessa coluna para a anterior vai ser no campo "Padrão", nessa usaremos o seguinte.

```SQL
NOW() on update NOW()
```

Ela usará o NOW() e quando o dado for atualizado, utilizará o NOW() novamente.

```SQL
ALTER TABLE base_de_dados.users ADD updated_at DATETIME DEFAULT NOW() on update NOW() NOT NULL;
```

> ~={green}Exemplo=~

![[Exemplo updated_at.png]]

































