
#### <span style="color:rgb(4, 255, 0)">Cálculo de datas</span> 

O cálculo de datas serve para compararmos por exemplo se uma data é menor, maior ou igual outra.

> Exemplo

```Python
from datetime import datetime  
  
fmt = "%d/%m/%Y %H:%M:%S"  
data_inicio = datetime.strptime("20/04/1987 09:30:30", fmt)  
data_fim = datetime.strptime("12/12/2022 08:20:20", fmt)  
  
print(data_fim > data_inicio)
```

Além disso, podemos fazer outras operações entre datas, como por exemplo a diferença entre elas.

> Exemplo

```Python
from datetime import datetime  
  
fmt = "%d/%m/%Y %H:%M:%S"  
data_inicio = datetime.strptime("20/04/1987 09:30:30", fmt)  
data_fim = datetime.strptime("12/12/2022 08:20:20", fmt)  
  
print(data_fim - data_inicio)
```