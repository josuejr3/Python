
#### <span style="color:rgb(4, 255, 0)">Criação de data e hora com módulo datetime</span>

Para criação de datas, podemos usar o módulo datetime que já vem com o próprio Python

-  Usando o datetime, eu posso criar uma data sem especificar as horas (opcional)
-  A ordem é sempre ano-mes-dia-hora-minutos-segundos-microsegundos-zone

```Python
from datetime import datetime  

# Exemplo passando apenas a data
data = datetime(2022, 4, 20)  
print(data)

# Exemplo passando data e hora
data = datetime(2022, 4, 20, 7)  
print(data)

# Exemplo com data e hora completos
data = datetime(2022, 4, 20, 7, 6, 8)  
print(data)
```

Uma outra forma de representar data e horário é usar "datetime.strptime". Nesse caso, passamos uma string e informamos o formato.

Documentação que auxilia no uso de data e hora em Python

	https://docs.python.org/3/library/datetime.html

No final desse link, existem diretivas que nos ajudam a utilizar formatos de data e hora. Vamos focar em duas.

-  strftime() - formata datas
-  strptime() - cria datas

> *Ok Josué, mas como que eu vou transformar uma string em uma data e horário?*

Basta fazer o seguinte código

```Python
data_str = "2022/04/20 07:06:08"  
formato_data = "%Y/%m/%d %H:%M:%S"  
  
data_s = datetime.strptime(data_str, formato_data)  
  
print(data_s)
```

Nesse nosso caso, o formato_data sempre deve ser igual ao formato que temos em data_str