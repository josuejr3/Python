# Métodos de Classe e Métodos de Fábrica



class Pessoa:
    ano = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    # Método normal
    def metodo_de_classe(self):
        print("Hey")

    # Método de classe
    @classmethod
    def metodo_de_classe(cls):
        print("Hey")

    # Métodos de Fábrica
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def cria_sem_nome(cls, nome):
        return cls("Anonima", 50)

    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print("Oi")



Pessoa.metodo_de_classe()
p2 = Pessoa.criar_com_50_anos("Ze")
p3 = Pessoa("Anonima", 23)
print(p2.nome)
print(p3.nome, p3.idade)


p2.funcao_que_esta_na_classe(1, 2, 3)
Pessoa.funcao_que_esta_na_classe(1, 2, n=3)
p2.funcao_que_esta_na_classe(a=1)



