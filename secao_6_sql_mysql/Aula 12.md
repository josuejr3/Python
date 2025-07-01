
#### <span style="color:rgb(4, 255, 0)">Selecionando valores de duas tabelas distintas</span>

Quando estamos trabalhando com múltiplas tabelas pode ocorrer de termos colunas repetidas. Isso ocorre quando observamos a tabela users e a profiles, ambas possuem a coluna "id". Essa repetição causa problemas na minha linguagem de programação, por esse motivo é necessário corrigir.

> ~={green}Exemplo=~

```SQL
SELECT u.id AS uid, p.id AS pid FROM users AS u, profiles AS p;
```

-  No código acima renomeamos o nome das colunas de id;
-  uid se refere a coluna id de usuários;
-  pid se refere a coluna id de profiles.

O resultado do código acima é um ~={red}produto cartesiano=~ dos perfis (profiles) pelos usuários (users).

Para resolver isso, notamos que o user_id (foreign key) de profiles está relacionado com o id de users (primary key.

```SQL
SELECT u.id AS uid, p.id AS pid FROM users AS u, profiles AS p WHERE u.id = p.user_id; 
```