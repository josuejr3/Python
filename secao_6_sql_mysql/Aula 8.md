
#### <span style="color:rgb(4, 255, 0)">Usando Where para filtrar valores </span>

O uso do where é importante para filtragem de dados, pois a partir da aplicação de um filtro é que conseguimos fazer o update de um dado ou até mesmo a exclusão.

> ~={green}Exemplo de Código=~

```SQL
SELECT * FROM users WHERE id=3;
```

O código diz basicamente o seguinte, selecione todos os elementos da tabela users onde o ID é 3.

```SQL
SELECT * FROM users WHERE first_name="Josue";
```

-  O SQL não faz destinção de "Josue" para "josue".

Além de usar o operador de "=" podemos usar outros operadores, como por exemplo >=, <=, < , !=, <> e >.

Podemos usar também com datas e também usar operadores lógicos AND e OR

```SQL
SELECT * FROM users WHERE created_at < "2025-06-29 14:46:14" AND first_name = "Luiz1" AND password_hash = "a_hash1";
```

Se uma das condições forem falsas, nenhum registro é mostrado.

