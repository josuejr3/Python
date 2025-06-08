
#### <span style="color:rgb(4, 255, 0)">Threads</span>

Quando executamos um programa, significa que estamos executando um processo. Entretanto, esse processo pode fazer várias coisas e para que isso ocorra, temos as threads que são responsáveis por executar cada uma dessas tarefas.

> ~={green}Exemplo de uma main thread=~

```Python
from time import sleep
print("Hello")
for i in range(10):
	print(i)
	sleep(.5)
print("World")
```