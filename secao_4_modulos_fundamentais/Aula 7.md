A aula 6 foi "pulada", pois nela fazemos um exércicio sobre datas.

#### <span style="color:rgb(4, 255, 0)">Calendários</span>

Em Python podemos usar bibliotecas que nos aproximam mais quando estamos precisando trabalhar, manipular ou até utilizar variaveis de tempo. Uma biblioteca bastante utilizada é a calendar. Ela serve para:

-  Verificar o últim dia do mês;
-  Verificar o nome e o número de uma determinada data;
-  Criar um calendário em si;
-  Trabalhar com coisas específicas de calendários.

Nessa biblioteca, os dias da semana são enumerados de zero até seis, sendo o zero a segunda e o seis o domingo.

```Python
import calendar  
  
print(calendar.calendar(2022))  
print(calendar.month(2025, 2))  
  
print(calendar.monthrange(2022, 12))  
print(calendar.THURSDAY)

# o primeiro item da tupla informa se o primeiro dia foi em um seg, ter, qua, qui, sex, sab, dom
# enquanto que o segundo diz o ultimo dia 30, 31, 29...

print(calendar.day_name[calendar.weekday(1500, 4, 22)])

# codigo para ver as semanas  
for week in calendar.monthcalendar(2025, 6):  
    print(list(enumerate(week)))
```





