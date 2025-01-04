# Valores Truthy e Falsy, tipos mutáveis e iutáveis

# Tipos mutáveis
# - list() ou []
# - dict() ou {}
# - set() ou {} - sem chave valor

# mutáveis

# # LISTAS
# list()
# []
#
# # DICIONARIOS
# dict()
# {} # chave valor
#
# # SET
# set()
# {} # sem chave valor
#
#
# # imutáveis
#
# # TUPLAS
# tuple()
# () # ou separado apenas por virgula
#
# # STRINGS
# str()
#
# # INT
# int()
#
# # FLOAT
# float()
#
# # BOOLEANO
# bool()
#
# # TIPO RANGE
# range(0, 10)
#
# # TIPO NAO VALOR
# None

# DIR, HASATTR E GETATTR em PYTHON


string = "Luiz"
print(string)

# o dir retorna todos os atributos e métodos definidos em string, os atributos da classe string
print(dir(string))

# o método hasattr chega se um objeto possui um método ou atributo passado como parâmetro (em string)
# segue o exemplo abaixo

string = "Luiz"
metodo = "upper"
if hasattr(string, "upper"):
    print("possui o método")
    print(getattr(string, metodo)())
    print(string.upper())
else:
    print("Nao existe o metodo", metodo)

# o método getattr verifica se um método ou atributo existe naquele objeto

# MAIS SOBRE ITERÁVEIS E ITERATORS

import sys

iterable = ["Eu", "Tenho", "__iter__"]
iterator = iterable.__iter__()

print(next(iterator))
print(next(iterator))

# GENERATOR EXPRESSION

# É específico do Python

# generator com list comprehension
lista = [n for n in range(1000000)]

# criando um generator (parecido com ""tuple comprehension"")
generator = (n for n in range(1000000))
print(generator)


# Os tamanhos da lista e do generator na memoria sao diferentes.
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# dificultaria se eu precisasse de mais valores, por ex 10000

# a diferença do generator para a lista é que os valores da lista sao todos ja colocados na memoria
# ja o do generator nao, os valores so sao acrescentados caso seja solicitado


# GENERATOR FUNCTIONS

# criando como funcao normal

def generator(n=0):
    yield 1 # ele pausa aqui
    print("Continuando....")
    yield 2 # pausa novamente
    print("Mais uma vez...")
    yield 3
    print("Vou terminar")
    return "ACABOU"

gen = generator(n=0)
print(gen.__iter__())
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def generator_2(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return


gen_2 = generator_2(n=5, maximum=8)
for x in gen_2:
    print(x)


# YIELD FROM NAS GENERATOR FUNCTIONS

def gen1():
    print("COMECOU GEN 1")
    yield 1
    yield 2
    yield 3
    print("ACABOU GEN 1")

def gen3():
    print("COMECOU GEN 3")
    yield 10
    yield 20
    yield 30
    print("ACABOU GEN 3")


def gen2(gen):
    print("COMECOU GEN 2")
    yield from gen()
    yield 4
    yield 5
    yield 6
    print("ACABOU GEN 2")

g = gen2(gen1)

for numero in g:
    print(numero)







