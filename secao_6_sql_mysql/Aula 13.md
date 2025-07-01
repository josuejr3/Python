
#### <span style="color:rgb(4, 255, 0)">Relacionamentos</span> 

-  INNER JOIN

Imagine que cada um dos circulos abaixo se refere a uma tabela. Se eu quero que o relacionamento entre as duas tabelas existam, ou seja, um usuário seja atrelado a um perfil eu devo fazer um INNER JOIN. Basicamente o INNER JOIN retorna quando os valores das dua tabelas existem no relacionamento.

![[Relacionamentos.png]]

-  LEFT JOIN

No LEFT JOIN eu vou considerar apenas elementos que estão na tabela de usuários. Sendo assim, mesmo que um usuário não possua perfil eu ainda conseguirei identificá-lo. No MySQL vemos isso como LEFT ALTER JOIN.

-  RIGHT JOIN 

Faz algo semelhante ao LEFT JOIN, porém nesse caso é o inverso. Usando RIGHT JOIN eu vou obter todos os registros da tabela profiles mesmo que não exista um relacionamento com algum usuário.

> ~={green}Exemplos - Consulta INNER JOIN=~

```SQL
SELECT u.id AS uid, p.id AS pid, p.bio, u.first_name FROM users AS u, profiles AS p WHERE u.id = p.user_id;
```

Usando o INNER JOIN diretamente

```SQL
-- Escrevendo um JOIN
SELECT u.id AS uid, p.id AS pid, p.bio, u.first_name FROM users AS u INNER JOIN profiles p
ON u.id = p.user_id;
```

```SQL
SELECT u.id AS uid, p.id AS pid, p.bio, u.first_name FROM users AS u INNER JOIN profiles p ON uid = p.user_id WHERE u.first_name LIKE "%a" ORDER BY u.first_name DESC LIMIT 5;
```

> ~={green}Exemplo - Consultas com LEFT JOIN=~

Nesse caso, usando o LEFT JOIN teremos todos os valores presentes na tabela à esquerda que é de a de users, independente se eles possuem profiles atrelados ou não. Usuarios que não tem perfil atrelado tem seus valores representados por "NULL".

```SQL
SELECT u.id AS uid, p.id AS pid, p.bio, u.first_name FROM users AS u LEFT JOIN profiles p
ON u.id = p.user_id;
```

> ~={green}Exemplo - Consultas com RIGHT JOIN=~

Inicialmente para o exemplo que estamos usando não é possível realizar o procedimento de RIGHT JOIN, pois a foreign key da tabela profiles está na tabela users. Para resolver isso <mark style="background: #FF5582A6;">TEMPORARIAMENTE</mark> podemos excluir a foreign key.

```SQL
SELECT u.id AS uid, p.id AS pid, p.bio, u.first_name FROM users AS u LEFT JOIN profiles p
ON u.id = p.user_id;
```
