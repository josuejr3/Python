
#### <span style="color:rgb(4, 255, 0)">Funções de Agregação</span>

Vimos anteriormente que o MySQL tem algumas funções de agregação. Sendo assim, a função vai fazer uma agregação com os registros da tabela e vai retornar um output.

> ~={green}Exemplos=~

-  Agregando os registros e obtendo o maior salário

```SQL
SELECT MAX(salary) AS max_salary FROM users;
```

-  Agregando os registros e obtendo o menor salário

```SQL
SELECT MIN(salary) AS min_salary FROM users;
```

-  Agregando os registros e obtendo a média deles

```SQL
SELECT AVG(salary) AS avg_salary FROM users;
```

-  Agregando e obtendo a soma de todos os salários

```SQL
SELECT SUM(salary) AS sum_salary FROM users;
```

-  Agregando e obtendo a quantidade de registros na tabela

```SQL
SELECT COUNT(salary) AS count_salary FROM users;
```









