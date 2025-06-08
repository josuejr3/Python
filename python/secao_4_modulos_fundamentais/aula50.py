from threading import Thread, Lock
from time import sleep


class Igressos:
    def __init__(self, estoque):
        self.estoque = estoque
        # adicionar o lock que ajuda a eliminar a concorrencia
        # basicamente ele tranca o metodo comprar enquanto alguem estiver usado
        self.lock = Lock()

    def comprar(self, quantidade):
        # tranca o metodo
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Nao temos ingresso suficientes')
            self.lock.release()
            return

        # acontece alguma coisa que demore alguns segundos
        sleep(1)

        self.estoque -= quantidade
        print(f'Voce comprou {quantidade} ingressos, ainda temos {self.estoque}')
        # destranca o metodo
        self.lock.release()


if __name__ == '__main__':
    ingressos = Igressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)
