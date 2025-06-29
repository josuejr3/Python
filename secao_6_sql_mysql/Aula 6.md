
#### <span style="color:rgb(4, 255, 0)">DML - Data Manipulation Language</span> 

Basicamente o DML é uma forma de manipular os dados em uma base de dados out tabela.

![[Opções DML.png]]

DDL nós já vimos antes que é basicamente a definição dos tipos do dados.

-  Como o trabalho do desenvolvedor não é gerar uma base de dados, mas sim utilizar o que há de dados nela, usaremos o seguinte.

	-  SELECT
	-  INSERT
	-  UPDATE
	-  DELETE

Essas opções são divididas em dois grupos, SELECT (DQL - Data Query Language) em um único grupo enquanto que INSERT, UPDATE e DELETE (DML - Data Manipulation Language) estão em outro grupo.

##### <span style="color:rgb(4, 255, 0)">Utilizando o INSERT</span>

-  Para um único dado a ser inserido

```SQL
-- Comentario
-- Repositório para consultas
-- https://github.com/luizomf/sql-e-knex/tree/master/sql

-- Seleciona a base de dados padrão
use base_de_dados;
-- Mostra as tabelas da base de dados
show tables;
-- Descreve as colunas da tabela
describe users;
-- Inserir registros na base de dados
insert into users (first_name, last_name, email, password_hash) VALUES
("Maria", "Moreira", "maria@gmail.com", "m_hash");
```

-  Para vários dados (basta que eu utilize uma vírgula)

```SQL
```SQL
-- Comentario
-- Repositório para consultas
-- https://github.com/luizomf/sql-e-knex/tree/master/sql

-- Seleciona a base de dados padrão
use base_de_dados;
-- Mostra as tabelas da base de dados
show tables;
-- Descreve as colunas da tabela
describe users;
-- Inserir registros na base de dados
insert into users (first_name, last_name, email, password_hash) VALUES
("Joao", "Carlos", "jc@gmail.com", "jc_hash"), ("Felipe", "Souza", "fs@gmail.com", "fs_hash");
```