# Métodos úteis de dicionários

people = {
    "name": "Josue",
    "surname": "Ferreira",
    "age": 24,
    "height": 1.72,
    "address": [
        {"rua": "tal tal", "número": 123},
        {"rua": "outra rua", "numero": 321}
    ]
}

# len
print(len(people))  # Retorna a quantidade de chaves que eu possuo no dicionário

# keys
print(list(people.keys()))

# Quando usamos o for para percorrer o dicionário e o iterável é .keys() ele percorre as chaves
# se usarmos somente o dicionário com iterável ele também percorre somente as chaves.

# 1
for key in people.keys():
    print(key, end=" ")
print("\n")
# 2
for key in people:
    print(key, end=" ")
# 1 e 2 são iguais

# values
# O mesmo ocorre para .values
print("\n")
for value in people.values():
    if type(value) is list:
        for element in value:
            print(element)
    print(value)

# items
print(type(people.items()))
print(type(list(people.items())[0]))

# semelhante ao que vimos no enumerate
for chave, valor in people.items():
    print(chave, valor)

# setdefault

# Verificando a chave "Pet". (Não existe)
print(list(people.keys())) # mostrando que não existe a chave
print(people.setdefault("Pet", "Dog"))# incrementando e adicionando a chave
print(list(people.keys()))


# Nessa situação, ele verifica se o dicionário possui a chave Pet
# Se existir, ele não faz nada, se não existir, ele irá criar a chave
# E vai atribuir o valor do segundo parâmetro.

# ===========================================================================================================

# copy - cópia rasa

d1 = {
    "c1": 1,
    "c2": 2,
    "l1": [1, 2, 3],
}
# Apontam para o mesmo local da memória.
d2 = d1.copy()

d2["c1"] = d1["c1"] * 2
d2["c2"] = d1["c2"] * 2

print(d1["c1"], d2["c1"])
print(d1["c2"], d2["c2"])

print(d1["l1"], d2["l1"])
d1["l1"][0] = 1000 # ambos os dicionários vao ser mudados
print(d1["l1"], d2["l1"])

# Para criar uma cópia profunda basta usar o módulo copy
import copy

d3 = copy.deepcopy(d2)

d3["l1"][0] = "AAAAA"
print(d3["l1"], d2["l1"])


# get
print(d1.get("pet", "chave nao existe"))


# pop
print(d1)
# d1.pop("c1")
remocao = d1.pop("c1") #ou então remocao
print(d1)
print(remocao)


# popitem
print(d2)
remocao_2 = d2.popitem()
print(remocao_2)
print(d2)


# Usando o método update para atualizar dicionarios
d1.update(
	{
		"nome": "Josue",  # altera o valor da chave nome para Josue
		"sobrenome": "Ferreira", # altera o valor da chave sobrenome
		"idade": 23, # cria uma chave de nome idade e com valor 23
		"serie": "Sons Of Anarchy", # cria uma chave de nome serie e valor
	}
)

print(d1)


# Usando argumentos nomeados sem passar dicionario dicionario
d1.update(pet="cachorro",cor="preto")
print(d1)

# Terceira forma usando tuplas

# esse caso só funciona se for uma estrutura bidimensional, tupla de tuplas, lista de listas, tupla de listas...
lista = [["chave", "valor"],]
print(type(lista))
d1.update(lista)
print(d1)


# ===============================================================================================

# CONJUNTOS

conjunto_1 = set()
# Set vazio

falso_conjunto = {}   # dicionario
# print(type(falso_conjunto))

# Dentro do set, podemos colocar iteráveis e ele itera sobre cada elemento
conjunto_2 = set("Luiz")
print(conjunto_2)

# Forma correta de adicionar iteraveis
conjunto_3 = {"Luiz"}
print(conjunto_3, type(conjunto_3))


# Eficientes para remover valores duplicados de iteraveis

s1 = {1 ,2, 3, 3, 3, 3, 3, 3, 4}
print(s1)


l1 = [1, 2, 3, 4, 4, 4, 5, 6, 6]
s2 = set(l1)
l2 = list(s2)
print(l2)
# [1, 2, 3, 4, 5, 6]

# s1 = s1 = {1, 2, 3, [123]}
# print(s1)
# Erro unhashable type

print(3 in s2)
print(10 in s2)

# """""""colocando indices com enumerate"""""""""
for i, v in enumerate(s2):
    print(i, v)

#==========================================================================================

# Métodos uteis de conjuntos

a3 = set()

# Adicionando elemntos noo set
a3.add(1)
a3.add(90)
print(a3)
a3.add(0)
print(a3)

# método update para modificar o conjunto
a3.update(("Ola mundo",))  # Como adicionar strings
print(a3)

# metodo clear pra limpar
print(a3)
a3.clear()
print(a3)

# método discard - usado para remover um elemento específico
a3.add(("Olá mundo"),)
a3.add(1)
print(a3)
a3.discard("Olá mundo")
print(a3)

#==========================================================================================

#                                   OPERAÇÕES ENTRE CONJUNTOS

c1 = {1, 2, 3}
c2 = {1, 3, 7}

# Unindo os dois conjuntos com |
c3 = c1 | c2
# c3 = c1.union(c2)
print(c3)

# Intersecção, elementos que estão nos dois conjuntos
c3 = c1 & c2
#c3 = c1.intersection(c2)
print(c3)

# Diferença (A ordem vai importar)
c3 = c1 - c2
#c3 = c1.difference(c2)
print(c3)

c4 = c2 - c1
#c4 = c2.difference(c1)
print(c4)

# Diferença simétrica
c3 = c2 ^ c1
c3 = c2.symmetric_difference(c1)
print(c3)





## Exemplo simples do uso de sets


letras = set()
while True:
    letra = input("Digite uma letra: ").lower()
    letras.add(letra)
    if "l" in letras:
        print("PARABENS")
        break

    print(letras)