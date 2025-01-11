
def list_join(lista_1: list, lista_2: list) -> list:
    return [sum(i) for i in zip(lista_1, lista_2)]

# o zip retorna um iterável, sendo assim, não há necessidade de converter para list

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

print(list_join(lista_a, lista_b))

# código professor - maneira mais génerica

# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
#
# print(lista_soma)

# código do professor usando enumerate ""pythonica""

# lista_soma = []
# # enumerate pegando apenas o índice
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
#
# print(lista_soma)

# solução mais facil

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]