
#### <span style="color:rgb(4, 255, 0)">Usando o SELECT</span> <span style="color:rgb(4, 255, 0)">para selecionar todas as colunas de uma tabela</span>

Aqui nós vamos apender como selecionar as colunas da nossa tabela. Para introduzir, vamos aprender a selecionar coluna por coluna

```SQL
-- Selecionando todas as colunas da tabela users
SELECT * from users;
-- Poderiamos usar apelidos para tabelas também
-- SELECT * from users u;
```

O código acima basicamente seleciona todas as colunas presentes na tabela users. Entretanto, podemos dar um alias ou apelido para essa tabela, chamando de u, que pode ser utilizado ao longo do código.

```SQL
SELECT email, first_name from users;
```

O código acima mostra as colunas de e-mail em seguida as de primeiro nome da coluna de usuários.

<mark style="background: #FF5582A6;">Obs: pode ocorrer de colunas de uma tabela coincidirem com colunas de outra tabela e isso causa um choque, então devemos especificar de onde nós queremos determinada informação.</mark>

> ~={green}Exemplo=~

	users tem uma coluna id
	roles também tem uma coluna id

Para especificar usamos o ".", ficando assim. Abaixo nós referenciamos as colunas a cada tabela por meio do "." e além disso, "renomeamos" para nomes mais específicos.

```sql
SELECT u.email uemail, u.id uid, u.first_name ufirst_name from users as u;
```

