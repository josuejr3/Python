from abc import abstractmethod, ABC


class Conta(ABC):

    def __init__(self, agencia: int, conta: int, saldo: float =0) -> None:
        self.agencia = agencia
        self._numero = conta
        self._saldo = saldo

    def deposito(self, valor: float) -> float:
        self._saldo += valor
        self.detalhes(f'(DEPOSITO {valor})')
        return self._saldo

    def detalhes(self, msg: str = "") -> None:
        print(f'O seu saldo é: {self._saldo:.2f} {msg}')
        print("--")

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self._numero!r}, {self._saldo!r})'
        return f'{class_name}{attrs}'


    @abstractmethod
    def sacar(self, valor) -> float: ...


