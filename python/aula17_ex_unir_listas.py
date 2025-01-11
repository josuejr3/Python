# def small_list(l1: list, l2: list):
#     return l1 if len(l1) < len(l2) else l2
#
# def zipper(l1: list, l2: list) -> list:
#     base_list = small_list(l1, l2)
#
#     list_result = []
#
#     for i in range(len(base_list)):
#         elemet = (base_list[i], l1[i]) if base_list != l1 else (l1[i], l2[i])
#         list_result.append(elemet)
#
#     return list_result
#
#
# l1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
# l2 = ["BA", "SP", "MG", "RJ"]
#
# print(zipper(l1, l2))
#
# print(l1)
# print(l2)

# CÓDIGO DO PROFESSOR

def zippr(lista1, lista2):
    # descobrindo menor indice entre listas
    intervalo = min(len(lista1), len(lista2))

    # usando list comprehension ele já adiciona automaticamente
    return [
        (lista1[i], lista2[i]) for i in range(intervalo)
    ]


l1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]
print(zippr(l1, l2))
print(list(zip(l1, l2)))

from itertools import zip_longest

print(list(zip_longest(l1, l2, fillvalue="Sem Cidade")))