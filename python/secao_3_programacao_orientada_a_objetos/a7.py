class Pessoa:

    cpf = 1234

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        # nome da classe
        print("Classe PESSOA")
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        # nome da classe
        print("Eita, nem sai da classe cliente")
        print(self.nome, self.sobrenome, self.__class__.__name__)
class Aluno(Pessoa):
    cpf = 4444

c1 = Cliente('Josue', 'Junior')
c1.falar_nome_classe()
a1 = Aluno('Jose', 'Luiz')
a1.falar_nome_classe()

print(c1.cpf)
print(a1.cpf)

