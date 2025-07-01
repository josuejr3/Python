
#### <span style="color:rgb(4, 255, 0)">Utilizado o UPDATE</span> 

O UPDATE é semelhante ao DELETE, entretanto, agora será necessário repassar os valores que eu desejo substituir.

```SQL
SELECT * FROM users WHERE id = 119;
```

```SQL
UPDATE users SET first_name = "Joseph", last_name = "Morrison" WHERE id = 100;
select * from users where id = 100
```

-  No código acima nós trocamos o nome e o sobrenome para Joseph e Morrison o user 100;
-  Sempre é necessário usar o comando SET para fazer a alteração.

