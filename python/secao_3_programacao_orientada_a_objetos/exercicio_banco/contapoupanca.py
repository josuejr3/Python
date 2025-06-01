from contas import Conta

class ContaPoupanca(Conta):

    def sacar(self, valor):
        valor_pos_saque = self._saldo - valor

        if valor_pos_saque >= 0:
            self._saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self._saldo

        print(f"Não foi possivel sacar o valor desejado")
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self._saldo