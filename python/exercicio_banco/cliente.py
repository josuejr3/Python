from pessoas import Pessoa
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca
from contas import Conta

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)

        # Indicando o tipo da conta ou e Conta ou é None
        self.conta: Conta | None = None

    # Como cliente e conta sao coisas independentes, eu posso configurar ela depois
    # Por esse motivo foi colocado o None

if __name__ == '__main__':


    c1 = Cliente('LUIZ',30)
    c1.conta = ContaCorrente(111, 222, 0, 0)

    print(c1)
    print(c1.conta)