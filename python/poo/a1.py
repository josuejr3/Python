# Classes

# class Pessoa:
#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = sobrenome
#
#
# p1 = Pessoa("Luiz", "Otávio")
# # p1.nome = "Luiz"
# # p1.sobrenome = "Otávio"
#
# p2 = Pessoa("Maria", "Joana")
# # p2.nome = "Maria"
# # p2.sobrenome = "Joana"
# #
# print(p1.nome)
# print(p1.sobrenome)
# print(p2.nome)
# print(p2.sobrenome)

# Iniciaizador init e self


# Métodos em Instâncias de Classes Python

# class Car:
#     def __init__(self, name_car="Sem modelo"):
#         self.name = name_car
#
#     def acelerar(self):
#         print(f"{self.name} está acelerando...")
#
#
# fusca = Car("Fusca")
# print(fusca.name)
#
# celta = Car("Celta")
# print(celta.name)
#
# fusca.acelerar()
# celta.acelerar()
#
# Car.acelerar(fusca)
#
# class Animal:
#     # name = "Leão"
#     def __init__(self, name):
#         self.nome = name
#         variavel = "valor"
#         print(variavel)
#
#     def comendo(self, alimento="nada"):
#         # erro escopos diferentes
#         # print(variavel)
#         return f"{self.nome} está comendo {alimento}"
#
#     def executar(self, *args, **kwargs):
#         return self.comendo(*args, **kwargs)
#
# # Erro
# # print(name)
#
# # print(Animal.name)
# leao = Animal(name="Leao")
# print(leao.nome)
# print(leao.comendo("carne"))
#
# print(leao.executar("maçã"))

# MANTENDO ESTADOS DENTRO DA CLASSE


# class Camera:
#     def __init__(self, name, filming=False):
#         self.name = name
#         self.filming = filming
#
#     def film(self):
#
#         if self.filming:
#             print(f"{self.name} JÁ está filmando...")
#             return
#
#         print(f"{self.name} está filmando...")
#         self.filming = True
#
#     def stop_film(self):
#         if not self.filming:
#             print(f"{self.name} NÃO está filmando...")
#             return
#         print(f"{self.name} está parando de filmar...")
#         self.filming = False
#
#
#     def click(self):
#         if self.filming:
#             print(f"{self.name} não pode fotografar filmando")
#             return
#         print(f"{self.name} está fotografando...")
#
#
# c1 = Camera("Canon")
# c2 = Camera("Sony")
#
# c1.film()
# c1.film()
# c1.click()
# c1.stop_film()
# c1.click()

# print(c1.filming)
# print(c2.filming)


# Atributos de classe

# class Pessoa:
#
#     ANO_ATUAL = 2022
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
#     def get_ano_nascimento(self):
#         return Pessoa.ANO_ATUAL - self.idade
#
#
#
#
# p1 = Pessoa("João", 35)
# p2 = Pessoa("Maria", 12)
# print(Pessoa.ANO_ATUAL)
#
# # Isso modifica todas as instancias, já que elas dependem dos atributos da classe base
# # Pessoa.ANO_ATUAL = 1
# print(p1.get_ano_nascimento())
# print(p2.get_ano_nascimento())






























