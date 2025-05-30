
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

Entretanto, o retorno obtido através de uma expressão "algébrica" não é uma data no formato padrão. O retorno é a quantidade de dias entre essas duas datas (inicial e final). O nome desse retorno é "timedelta". Sabemos que delta na matemática serve para representar variações, ou seja, quando temos uma quantidade inicial de algo e uma quantidade final. Isso é representado aqui como esse algo sendo o nosso tempo.

O objeto timedelta tem alguns atributos específicos a data e hora que podemos usar, como por exemplo "days", "seconds" e "microseconds". Além disso, também posso instanciar timedelta.

```Python
# obtendo mais dados a partir do timedelta  
delta = data_fim - data_inicio  
print(delta.days, delta.seconds, delta.total_seconds(), delta.microseconds)

timed = timedelta(days=10)
print(data_fim + timed)
```

-  Links importantes para bibliotecas de datetime e timedelta

	https://dateutil.readthedocs.io/en/stable/relativedelta.html
	https://docs.python.org/3/library/datetime.html#timedelta-objects

Uma alternativa para o timedelta é o "*dateutil.relativetimedelta*", necessário instalar o pacote

```cmd
pip install python-dateutil types-python-dateutil
```

A diferença da timedelta para a relativedelta é praticamente que a segunda oferece uma maior quantidade de atributos e parâmetros para ajuste.

```python
from dateutil.relativedelta import relativedelta  
print(data_fim - relativedelta(seconds=59))
```

#### <span style="color:rgb(4, 255, 0)">Formatando datas</span>

A formatação de datas é semelhante a criação, utiliza uma função parecida, segue o exemplo abaixo.

```Python
# primeiro - criar uma data  
nova_data = datetime.strptime('2022-12-13 07:59:23', "%Y-%m-%d %H:%M:%S")  
  
# passando para o formato padrão usando strftime()  
print(data.strftime(fmt))
```

Porém, após usar essa função temos um objeto do tipo string. Se quisermos continuar usando os atributos da classe e depois converte-los para string também é possível.

```Python
print(data.strftime("%Y"), nova_data.year)  
print(data.strftime("%m"), nova_data.month)
```










































