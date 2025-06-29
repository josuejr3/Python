
#### <span style="color:rgb(4, 255, 0)">Usando Where para filtrar valores </span>

O uso do where é importante para filtragem de dados, pois a partir da aplicação de um filtro é que conseguimos fazer o update de um dado ou até mesmo a exclusão.

> ~={green}Exemplo de Código=~

```SQL
SELECT * from users where id=3;
```

O código diz basicamente o seguinte, selecione todos os elementos da tabela users onde o ID é 3.

```SQL
SELECT * from users where first_name="Josue";
```

-  O SQL não faz destinção de "Josue" para "josue".

Além de usar o operador de "=" podemos usar outros operadores, como por exemplo >=, <=, < e >.

