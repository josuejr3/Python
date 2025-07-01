
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

##### <span style="color:rgb(4, 255, 0)">SELECT com LIMIT</span>

O SELECT com LIMIT nada mais é do que uma filtragem da quantidade de dados que vai aparecer na seleção final. 

Supondo que uma busca retorne um total de 100 linhas de dados. Se utilizarmos a palavra dedicad LIMIT e um valor inferior a 100 significa que o retorno de linhas de dados vai ser apenas com a mesma quantidade que indicamos

> ~={green}Exemplo=~

-  Resultado - o padrão retorna 100 linhas de dados.

```SQL
SELECT id, first_name, email AS uemail FROM users WHERE id BETWEEN 100 and 150 ORDER BY first_name DESC LIMIT 5
```

O código acima vai selecionar as colunas id, first_name e e-mail da tabela usuários onde o id está entre 100 e 150 e vai ordenar pelo primeiro nome de forma decrescente. Supondo que o total de resultados seja de 100, ele só retornará os 5 primeiros, pois foi o que indicamos quando usamos o número 5 junto da palavra chave LIMIT.

##### <span style="color:rgb(4, 255, 0)"> SELECT OFFSET</span>

O SELECT OFFSET é uma outra forma que podemos limitar os dados. Basicamente ele limita o que estamos visualizando, por padrão o OFFSET é 0.

> ~={green}Exemplo=~

Se estivermos trabalhando com o limite de duas linhas de dados então teremos o seguinte.

	linha0 - ...
	linha1 - ...

O OFFSET mostrará essas duas linhas. Para enxergarmos novos valores o nosso OFFSET deverá ser de 2, pois ele vai deslocar do meu "linha0" em duas posições, ficando o seguinte:

	linha0 - ...
	linha1 - ...
	>>> deslocou <<<
	linha2 - ...
	linha3 - ...

O OFFSET é como se fosse um passo de 2 em 2, 3 em 3 e assim por diante...

```SQL
SELECT id, first_name, email AND uemail, FROM users WHERE id BETWEEN 100 AND 150 ORDER BY id ASC LIMIT 3 OFFSET 3;
```

Outra maneira de escrever é o seguinte

```SQL
SELECT id, first_name, email AND uemail, FROM users WHERE id BETWEEN 100 AND 150 ORDER BY id ASC LIMIT 3, 6;
```

A diferença é que nessa situação, primeiro temos o OFFSET (3) e depois o LIMIT (6).
##### <span style="color:rgb(4, 255, 0)">INSERT com SELECT</span>

O uso do INSERT junto com o SELECT é importante quando queremos inserir dados de uma tabela em outra.

> ~={green}Exemplo - Inserindo dados na tabela Profiles=~

```SQL
INSERT INTO profiles (bio, description, user_id) SELECT "bio", "description", id FROM users;
```

-  O que está entre parentêses são as informações que desejamos;
-  O código faz como se fosse um "for" na tabela e vai atribuir "bio" e "description" das linhas de users em novas linhas de profiles.

Agora vamos ver como fazer uma concatenação de valores com textos

```SQL
INSERT INTO profiles (bio, description, user_id) SELECT CONCAT("Bio de ", first_name), first_name, id FROM users;
```

-  Usamos a função CONCAT do MySQL.

















