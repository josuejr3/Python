
#### <span style="color:rgb(4, 255, 0)">Operações com JOINS</span>

###### <span style="color:rgb(4, 255, 0)">Selecionando com JOIN</span>

```SQL
SELECT u.id as uid, u.first_name, p.bio, r.name FROM users as u
LEFT JOIN profiles as p ON u.id = p.user_id
INNER JOIN users_roles as ur ON u.id = ur.user_id
INNER JOIN roles as r ON ur.role_id = r.id
ORDER BY uid ASC;
```
###### <span style="color:rgb(4, 255, 0)">Update com JOIN</span>

```SQL
-- Fazendo a SELECT
SELECT u.first_name, p.bio FROM users u
JOIN profiles AS p
ON p.user_id = u.id
WHERE u.first_name = "Katelyn";

-- Fazendo UPDATE
UPDATE users AS u
JOIN profiles AS p
ON p.user_id = u.id
SET p.bio = CONCAT(p.bio, " atualizado")
WHERE u.first_name = "Katelyn";
```

###### <span style="color:rgb(4, 255, 0)">Deletando dados com JOIN </span>

Quando eu faço um JOIN eu devo especificar de qual tabela eu desejo apagar.

```SQL
-- Fazendo o SELECT
SELECT u.first_name, p.bio FROM users u
JOIN profiles AS p
ON p.user_id = u.id
WHERE u.first_name = "Katelyn";

-- Fazendo o DELETE
DELETE FROM users u
JOIN profiles AS p
ON p.user_id = u.id
WHERE u.first_name = "Katelyn";
```

Do jeito que está o DELETE ele apaga da tabela users, caso seja necessário apagar da tabela profiles eu devo informar após o DELETE

```SQL
DELETE p FROM users u
JOIN profiles AS p
ON p.user_id = u.id
WHERE u.first_name = "Katelyn";
```








