
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

```Python
from threading import Thread  
from time import sleep  
  
# Criando threads  
  
class MyThread(Thread):  
    def __init__(self, texto, tempo):  
        self.texto = texto  
        self.tempo = tempo  
  
        super().__init__()  
  
    def run(self):  
        sleep(self.tempo)  
        print(f"{self.texto} foi finalizada!")  
  
# Criando minha thread  
t1 = MyThread('Thread 1', 5)  
# Iniciando a execução da thread  
t1.start()  
  
for i in range(10):  
    print(i)  
    sleep(1)
```

No código acima, primeiro nós criamos uma classe de threads que herda a classe de threads principal e sobreescrevemos o método run. 

Após isso, instanciamos uma thread 1 e a iniciamos. Após a finalização dessa thread ela exibe uma mensagem informando que foi finalizada. Com isso conseguimos perceber que mesmo que um for esteja rodando, a thread também estará rodando ao mesmo tempo.

```cmd
0
1
2
3
4
Thread 1 foi finalizada!
5
6
7
8
9
```

