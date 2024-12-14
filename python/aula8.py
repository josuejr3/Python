# Tipos de Dados - Listas

nomes = list()
nomes.append("Jose")
nomes.append("Renato")
nomes.append("Paulo")
print(nomes)

# outra forma de criar uma lista
lista = []
print(lista)
print(type(lista))

other_list = [123, True, "Luiz Otavio", 1.2, []]

print(other_list[2][5])

# alterando a string para caixa alta
other_list[2]= other_list[2].upper()
print(other_list)

other_list[2] = "Jose"
print(other_list)




# Metodos del, append e pop

lista1 = [1, 2, 3, 4]
# alterando elemento
lista1[2] = 300

# Apaga elemento
del lista1[2]

print(lista1)
print(lista1[2])

lista1.pop()
lista1.pop()

print(lista1)

# Além de remover o pop retorna o valor que foi removido

# O método insert serve para inserir um elemento em um determinado indice

lista1.insert(2, 1000)
print(lista1)


lista2 = [1, 2, 3, 4]
lista2.insert(2, True)
print(lista2)


# Concatenação de listas

l3 = lista1 + lista2
print(l3)

# Porém o método extemd() faz a mesma coisa, porém ele nao retorna um elemento ele modifica o passado

l3.extend(lista2)        # não retorna nada
print(l3)

# formas de acesso copia e referencia

l4 = [1, 0, 0, 1]
l5 = l4

print(l4)
l4.append(7)
print(l4)
print(l5)

l6 = l4.copy()
l6.append(9)
print(l6)
print(l4)

# Usando for na lista

for e in l6:
    print(e)


# questao exibir indices de uma lista

lista_names = ["Maria", "Helena", "Luiza"]
print("=============================")
for i in range(len(lista_names)):
    print(i)

nome1, nome2, nome3 = lista_names
print(nome1)
print(nome2)
print(nome3)

n1, *resto = lista_names
print(n1)
print(resto)

# Outra forma mais legível

nome1, *_ = ["Maria", "Helena", "Luiz"]

# Tuplas são iguais as listas, porém são imutáveis


tupla = 1, True, "Ki"
print(type(tupla))

# Enumerate

lista = ["Maria", "Helena", "Luiz"]
lista.append("João")

lista_enumerada = enumerate(lista)
print(next(lista_enumerada))


# esse processo de chamar o next pode ser feito usando um for

# for item in lista_enumerada:
#     print(item)
#
# for item in enumerate(lista, start=1):
# 	print(item)

# A melhor forma para usar o enumerate

for i, valor in enumerate(lista_enumerada, start=1):
    print(i, valor, "oi")