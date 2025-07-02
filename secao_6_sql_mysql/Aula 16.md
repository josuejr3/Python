
#### <span style="color:rgb(4, 255, 0)">GROUP BY</span>

Em SQL o GROUP BY basicamente é uma forma de organizar  e agrupar os registros a partir de algum critério. No exemplo que estamos usando para estudos essa organização por se dar por exemplo através de usuários que possuem o mesmo primeiro nome em comum.

```SQL
SELECT id, first_name FROM users
GROUP BY first_name
ORDER BY first_name ASC;
```

Obs: quando usamos GROUP BY os registros devem ser agregáveis, isto é, não podemos agregar registros que possuem valores diferentes. Isso ocorre por exemplo quando temos usuários com nomes iguais, mas id diferentes.

	Uma solução para isso é remover da primeira linha que contém o SELECT O "id", pois ele está com valores diferentes para nomes iguais já que cada registro tem um id distinto.

```SQL
SELECT first_name, COUNT(id) AS total FROM users
GROUP BY first_name
ORDER BY first_name ASC;
```

-  O COUNT(id) vai contar quantas instâncias de nome cada um deles possui na tabela.

```SQL
SELECT first_name, COUNT(id) AS total FROM users
GROUP BY first_name
-- ORDER BY first_name ASC;
ORDER BY total DESC;
```

```SQL
SELECT u.first_name, COUNT(u.id) AS total FROM  users u
LEFT JOIN profiles AS p
ON p.user_id = u.id
WHERE u.id IN (617, 539, 537, 611)
GROUP BY first_name
ORDER BY total DESC
LIMIT 5;
```

