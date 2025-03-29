# usando dataclasses

from dataclasses import dataclass, field

@dataclass()
class Pessoa:
    nome: str = 'Missing'
    sobrenome: str = 'Not Sent'

    idade: int = 0
    enderecos: list[str] = field(default_factory=list)


    # def __post_init__(self):
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'
    #
    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)

if __name__ == '__main__':

    p1 = Pessoa()
    print(p1)