
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

