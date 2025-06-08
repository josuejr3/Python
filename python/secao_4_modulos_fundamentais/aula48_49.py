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

t2 = MyThread('Thread 2', 2)
t2.start()

t3 = MyThread('Thread 3', 10)
t3.start()

for i in range(10):
    print(i)
    sleep(1)

######## Outra forma - Aula 49

def vai_demorar(tempo: int, texto: str) -> None:
    sleep(tempo)
    print(texto)

thread_1 = Thread(target=vai_demorar, args=(10, "Terminou t1"))
thread_1.start()

# executando a main thread

# while thread_1.is_alive():
#     print('Esperando a thread.')
#     sleep(2)

t1.join()

# Posso fazer a thread principal esperar a thread "secundaria"
# finalizar para que ela continue, basta fazer o seguinte código

print('Acabou')
