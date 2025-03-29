# usando dataclasses

from dataclasses import dataclass

@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str

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

    p1 = Pessoa('Josue', 'Ferreira')
    p2 = Pessoa('Joseph', 'Joestar')
    print(p1)
    print(p1 == p2)
    p1.nome_completo = 'Paulo Fernando da Silva'
    print(p1)


    print(p1.nome)
    p1.nome = 'JOSE'
    print(p1.nome)