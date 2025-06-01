class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
fabricante = Fabricante('Volkswagen')
fusca.fabricante = fabricante

motor1_0 = Motor('1.0')
fusca.motor = motor1_0

print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)


fiat_uno = Carro("Uno")
fiat = Fabricante("Fiat")
motor2_0 = Motor("2.0")
fiat_uno.fabricante = fiat
fiat_uno.motor = motor2_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)










