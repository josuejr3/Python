
#### <span style="color:rgb(4, 255, 0)">Usando o DELETE</span> 

Inicialmente é preciso saber que o DELETE é controlado pelo WHERE.

-  A forma mais segura de excluir um registro é utilizando a Primary Key, no nosso caso é o campo ID.

```SQL
DELETE FROM users WHERE id = 114;
SELECT * FROM users WHERE id BETWEEN 110 AND 115;
```

Basicamente a primeira linha do código deleta na tabela usuários onde o ID é 114.

<mark style="background: #FF5582A6;">Obs: UMA VEZ QUE O VALOR FOI APAGADO OU ATUALIZADO NÃO É MAIS POSSÍVEL VOLTAR ATRÁS!!!!!!</mark>

<mark style="background: #FF5582A6;">Obs2: Só estamos conseguindo apagar, pois colocamos CASCADE no DDL (Data Definition Language)!!</mark> 

	Ou seja, quando um usuário fosse apagado, o profile relacionado ao usuário também seria apagado
	