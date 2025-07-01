
#### <span style="color:rgb(4, 255, 0)">Um pouco mais sobre SELECT</span> 

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




