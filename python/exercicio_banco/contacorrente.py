from contas import Conta
from contapoupanca import ContaPoupanca

class ContaCorrente(Conta):

    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    def sacar(self, valor):
        valor_pos_saque = self._saldo - valor
        limite_maximo = -self._limite

        if valor_pos_saque >= limite_maximo:
            self._saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self._saldo

        print(f"Não foi possivel sacar o valor desejado")
        print(f'Seu limite é: {-self._limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self._saldo


    def __repr__(self):
        class_name = type(self).__name__
        attrs = (f'({self.agencia!r}, {self._numero!r}, {self._saldo!r}, '
                 f'{self._limite!r})')
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = ContaCorrente(111, 222, 0, 100)
    c1.sacar(1)
    c1.deposito(1)
    c1.sacar(1)
    c1.sacar(1)
    c1.sacar(98)
    c1.sacar(1)
