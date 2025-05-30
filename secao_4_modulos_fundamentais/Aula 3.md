
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


