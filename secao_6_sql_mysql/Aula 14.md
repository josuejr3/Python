
#### <span style="color:rgb(4, 255, 0)">Gerando números aleatórios com rand e arredondando com round</span> 

O MySQL possui uma função para criação de números aleatórios chamada de rand, veja o uso dela abaixo.

```SQL
SELECT RAND() * 10000;
```

-  Número aleatório multiplicado por 10000.

Além disso, como os valores estavam dando muitas casas decimais, podemos arredondar para duas casas decimais.

```SQL
SELECT ROUND(RAND() * 1000, 2);
```

```SQL
UPDATE users SET salary = ROUND(RAND () * 10000, 2);
SELECT salary FROM users WHERE salary BETWEEN 1000 AND 1500 ORDER BY salary ASC;
```

