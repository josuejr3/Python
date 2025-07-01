
#### <span style="color:rgb(4, 255, 0)">Um pouco mais sobre SELECT</span> 

##### <span style="color:rgb(4, 255, 0)">SELECT BETWEEN</span>

Além dos operadores comuns que conhecemos da programação (lógicos e booleanos) o MySQL oferece operadores para trabalhar com range de datas, por exemplo.

-  Primeira forma de obter um range de datas

```SQL
SELECT * FROM users WHERE created_at >= "2020-06-12 17:38:52" and created_at <= "2020-09-04 19:06:55";
```

-  Segunda forma usando BETWEEN 

```SQL
SELECT * FROM users WHERE created_at BETWEEN "2020-06-12 17:38:52" AND "2020-09-04 19:06:55";
```

##### <span style="color:rgb(4, 255, 0)">SELECT IN</span> 

Vimos anteriormente o SELECT BETWEEN que oferece uma especie de range. O SELECT IN faz uma seleção de elementos específicos, como se fosse um array de elementos. Por exemplo, queriamos os dados cujo ID fossem: 110, 115 e 120. Se precisassemos de bem mais IDs seria complicado digitá-los na mão. Para resolver isso, usamos o operador SELECT IN.

```SQL
SELECT * FROM users
WHERE id IN (110, 115, 120, 125, 130)
AND first_name IN ("Luiz", "Keelie");
```

##### <span style="color:rgb(4, 255, 0)">SELECT LIKE
</span>

O SELECT LIKE funciona como se fosse uma busca. Suponhamos que desejamos encontrar todos os nome que terminam com a letra "A".

```SQL
SELECT * FROM users WHERE first_name LIKE "%a";

-- Final da palavra
LIKE "%a"
-- Começo da palavra
LIKE "a%"
-- No meio da palavra
LIKE "%mo%"
LIKE "%a%b%"
```

Nesse caso, a seleção será feita em TODOS os ELEMENTOS da tabela USERS ONDE o PRIMEIRO NOME termina com QUALQUER COISA e um "A". O simbolo de "%" significa qualquer coisa. 

Se o objetivo é substituir apenas um único caractere então eu posso ao invés de usar um % (subsititui várias caracteres) posso usar um "\_" que substitui apenas um único.

##### <span style="color:rgb(4, 255, 0)">SELECT ORDER</span>

O SELECT ORDER basicamente faz a seleção de um conjunto de dados e ordena eles da forma escolhida pelo programador

```SQL
SELECT id, first_name, email as uemail from users where id BETWEEN 100 AND 150
ORDER BY id ASC;
```

No caso acima, estou selecionando as colunas id, first_name, email (como uemail) da tabela usuários onde o id está entre 100 e 150. A ordenação será pelo id e será asc, ou seja ascendente do menor para o maior.

<mark style="background: #FF5582A6;">Obs: se a variável que está sendo usada para ordenar não foi descrita no SELECT inicial não há problema.</mark>

<mark style="background: #FF5582A6;">Obs 2: eu posso ordenar através de duas variáveis.</mark>

```SQL
SELECT id, first_name, email as uemail from users where id BETWEEN 100 AND 150
ORDER BY id ASC, first_name DESC;
```

-  ASC - Ascendente
-  DESC - Descendente




























