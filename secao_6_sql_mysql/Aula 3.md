
#### <span style="color:rgb(4, 255, 0)">Algumas observações sobre SQL</span> 

Durante o curso vamos apenas resumir alguns aspectos importantes sobre o SQL, porém, não é um curso voltado para SQL. Dessa forma, para saber mais você pode verificar o link abaixo

	https://www.geeksforgeeks.org/sql/sql-ddl-dql-dml-dcl-tcl-commands/

Tópicos Importantes

-  DDL - Data Definition Language 
-  DQL - Data Query Language
-  DML - Data Manipulation Language
-  DCL  - Data Control Language

---

Passos para criação de Database 

-  Conectar ao banco de dados do Docker;
-  Criar uma coluna;
-  Criar uma constraints/restrição - (isso serve para construir a PK/Primary Key)

![[Pasted image 20250620212556.png]]

Restrições são usadas por exemplo quando não queremos que dados sejam repetidos. No nosso caso, se aplica aos e-mails, pois não desejamos que e-mails sejam repetidos.

Após definir as colunas e restrições, nós salvamos e então vai ser criado o <mark style="background: #0000FF;">DATA DEFINITION LANGUAGE</mark>.

```SQL
CREATE TABLE base_de_dados.users (
id INT auto_increment NOT NULL,
first_name varchar(150) NOT NULL,
last_name varchar(150) NULL,
email varchar(255) NOT NULL,
password_hash varchar(255) NOT NULL,
CONSTRAINT users_pk PRIMARY KEY (id),
CONSTRAINT users_unique_email UNIQUE KEY (email),
CONSTRAINT users_unique_password_hash UNIQUE KEY (password_hash)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;
```

-  PKs que estão indo para outras entidades não são autoincrementadas!!!