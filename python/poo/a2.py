class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa("João", 35)

#print(p1.__dict__)
#print(vars(p1))

# Criando novo atributo com __dict__

#p1.__dict__["outra"] = "coisa"
#print(p1.__dict__)
#del p1.__dict__["nome"]
#print(p1.__dict__)

import os
os.system('cls')

# p2 = {"nome": "Joao", "idade": 35}
# # p22 = Pessoa(**p2)
# # print(vars(p22))
# # print(p1.nome)

print(vars(p1))