
#### <span style="color:rgb(4, 255, 0)">Data e hora atual (now), com Unix Timestamp e Timezone diferente (pytz)</span> 

-  Timezone é basicamente os diferentes fusos horários que existem ao longo do mundo

Em relação ao método now, basicamente ele vai retornar a hroa exata que está referenciada no computador. 

```Python
from datetime import datetime  
  
print(datetime.now())

# >>>> 2025-05-30 11:22:48.091455
```

Só que esse método tem um problema, que é o fato do timezone poder ser diferente. Dessa forma, a própria função fornece um atributo para que possamos alterar o timezone. 

Porém, esse procedimento não feito apenas com a datetime, para fazer a mudança de fuso horário devemos instalar uma biblioteca que não pertece ao python, chamada de "pytz"

-  Lista com timezones

	https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

> Exemplo de uso com timezone

```Python
from datetime import datetime  
from pytz import timezone  
  
print(datetime.now(timezone("America/Fortaleza")))  
print(datetime.now(timezone("Asia/Tokyo")))
```

Além disso, podemos usar o timezone nas datas e horários que criamos, veja abaixo.

```Python
data = datetime(2022, 4, 20, 7, 6, 8, tzinfo=timezone('Asia/Tokyo'))
```

Além dessas formas de criar e formatar datas e horas podemos utilizar o *Unix Timestamp* que é uma contagem feita de segundos 1/1/1970.

-  Link

	https://pt.wikipedia;org/wiki/Era_Unix


```Python
# Segundos de 1/1/1970 até hoje  
print(datetime.now().timestamp())  
  
# Criando data a partir do timestamp  
print(datetime.fromtimestamp(1748616998.970635))

# >> 1748617068.572584
# >> 2025-05-30 11:56:38.970635
```

