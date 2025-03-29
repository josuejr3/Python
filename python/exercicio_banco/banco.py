from conta import Conta
from exercicio_banco.cliente import Cliente
from pessoa import Pessoa
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca

class Banco:

    def __init__(self,
                 agencias: list[int] | None = None,
                 clientes: list[Pessoa] | None = None,
                 contas = list[Conta] | None,
    ) -> None:

        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def autenticar(self, cliente: Pessoa, conta: Conta):
        return self._checa_agencia(conta) and self._checa_cliente(cliente) and self._checa_agencia(conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}{self.clientes!r}{self.contas!r})'
        return  f'{class_name}{attrs}'


if __name__ == '__main__':
    l = Cliente('luiz', 30)
    c1 = ContaCorrente(111, 222, 0, 0)
    l.conta = c1
    m = Cliente('maria', 20)
    c2 = ContaPoupanca(112, 223, 100)
    m.conta = c2

    banco = Banco()

    banco.clientes.extend([l, m])
    banco.contas.extend([c1, c2])
    banco.agencias.extend([111, 222])
    print(banco)


######### CONSERTAR ##########















