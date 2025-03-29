class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    # !r = repr
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}{self.idade!r})'

        return f'{class_name}{attrs}'