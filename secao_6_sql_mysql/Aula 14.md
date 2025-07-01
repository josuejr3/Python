
#### <span style="color:rgb(4, 255, 0)">Gerando números aleatórios com rand e arredondando com round</span> 

O MySQL possui uma função para criação de números aleatórios chamada de rand, veja o uso dela abaixo.

```SQL
SELECT RAND() * 10000;
```

-  Número aleatório multiplicado por 10000.

Além disso, como os valores estavam dando muitas casas decimais, podemos arredondar para duas casas decimais.

```SQL
SELECT ROUND(RAND() * 1000, 2);
```

```SQL
UPDATE users SET salary = ROUND(RAND () * 10000, 2);
SELECT salary FROM users WHERE salary BETWEEN 1000 AND 1500 ORDER BY salary ASC;
```

##### <span style="color:rgb(4, 255, 0)">Atribuindo valores a tabela users_roles</span> 

```SQL
INSERT INTO users_roles (user_id, role_id) VALUES (518, 4);
SELECT user_id, role_id FROM users_roles WHERE user_id = 518 AND ROLE_ID = 4;
```

Para fazer isso para todos os usuários precisamos de tanto o user do usuário como também um role_id que é a permissão, já que juntas essas variáveis formam a nossa primary key.

-  Outra forma de fazer um SELECT criando uma coluna dinamicamente

```SQL
select id, (select 1) as qualquer from users;
```

Sabendo disso, podemos fazer uma seleção randomica das roles que nós possuímos.

```SQL
SELECT id, (SELECT id, FROM roles ORDER BY RAND() LIMIT 1) AS qualquer FROM users;
```

Fazendo a inserção

```SQL
INSERT INTO users_roles (user_id, role_id) SELECT id, (SELECT id, FROM roles ORDER BY RAND() LIMIT 1) AS qualquer FROM users;
```

