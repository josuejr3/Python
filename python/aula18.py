# O count é um contador infinito

# from itertools import count
#
# c1 = count(8, 8)
# # o range é finito
# r1 = range(10, 100, 8)
#
# print(c1.__next__())
# print(c1.__next__())
#
#
# # verificando se eh um iterator
# print("c1", hasattr(c1, "__iter__"))  # garante que tem um iter
# print("c1", hasattr(c1, "__next__"))  # garante que tem um next
# print("r1", hasattr(r1, "__iter__"))  # garante que tem um iter - é um iterável
# print("r1", hasattr(r1, "__next__"))  # garante que tem um next - não é um iterator
#
#
#
# for i in c1:
#     if i > 100:
#         break
#     print(i)





# from itertools import combinations, permutations, product
#
#
# def print_iter(iterator):
#     print(*list(iterator), sep="\n")
#
#
# pessoas = ["Joao", "Joana", "Luiz", "Leticia"]
# camisetas = [
#     ["preta", "branca"],
#     ["p", "m", "g"],
# ]
#
# print_iter(combinations(pessoas, 2))
# print("\n")
# print_iter(permutations(pessoas, 2))
# print("\n")
# # desempacotando a lista de camisetas com *
# print_iter(product(*camisetas))




# groupby - agrupando valor (itertools)

from itertools import groupby

# alunos = [
#     {"nome": "Luiz", "nota": "A"},
#     {"nome": "Leticia", "nota": "B"},
#     {"nome": "Fabricio", "nota": "A"},
#     {"nome": "Rosemary", "nota": "C"},
#     {"nome": "Joana", "nota": "D"},
#     {"nome": "Joao", "nota": "A"},
#     {"nome": "Eduardo", "nota": "B"},
#     {"nome": "Andre", "nota": "A"},
#     {"nome": "Anderson", "nota": "C"},
# ]

# alunos = ["a", "a", "a", "a", "b", "c", "a"]

# passa o aluno e retorna pela chave "nota"


# def ordena(aluno):
#     return aluno["nota"]
#
# alunos_agrupados = sorted(alunos, key=ordena)
#
# grupos = groupby(alunos_agrupados, key=ordena)
#
# for chave, grupo in grupos:
#     print(chave)
#     for aluno in grupo:
#         print(aluno)




def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

produtos = [
    {"nome": "Produto 5", "preco": 10},
    {"nome": "Produto 1", "preco": 22},
    {"nome": "Produto 3", "preco": 2},
    {"nome": "Produto 2", "preco": 6},
    {"nome": "Produto 4", "preco": 4},
]


# relembrando mapeamento - MAP

# def aumentar_porcentagem(valor, porcentagem):
#     return round(valor * porcentagem, 2)
#
# from functools import partial
#
# aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)
#
# # novos_produtos = [{**p,"preco": aumentar_dez_porcento(p["preco"])} for p in produtos]
#
#
# def aumenta_preco(produto):
#     return {**produto, "preco": aumentar_dez_porcento(produto["preco"])}
#
#
# novos_produtos = map(
#     aumenta_preco,
#     produtos
# )
#
from types import GeneratorType
#
# print(novos_produtos)
#
# print(hasattr(novos_produtos, "__iter__"))
# print(hasattr(novos_produtos, "__next__"))
# print(isinstance(novos_produtos, GeneratorType))
#
# print_iter(produtos)
# print_iter(novos_produtos)
#
# print(
# 	  list(map(
# 		lambda x: x  + 7,
# 		[1, 2, 3, 4]
# 	  ))
# )




# relembrando filter em list comprehension - FILTER

# novos_produtos = [
#     p for p in produtos
#     if p["preco"] > 10
# ]
#
# print_iter(produtos)
# print_iter(novos_produtos)

# usando a função filter

# novos_produtos = filter(
#     lambda p: p["preco"] > 100,
#     produtos
# )
#
# print(novos_produtos)
#
# print(hasattr(novos_produtos, "__iter__"))
# print(hasattr(novos_produtos, "__next__"))
# print(isinstance(novos_produtos, GeneratorType))
#
# print_iter(novos_produtos)
#


# função de reduce - REDUCE

from functools import reduce

# total = 0
#
# for p in produtos:
#     total += p["preco"]
#
# print(total)

# outra alternativa usando list-comprehension e a função sum

# print(sum([p["preco"] for p in produtos]))

# Usando o reduce

# a variavel total é o acuulador, se ela nao for definida ele será o primeiro elemento
# do iterável
def funcao_do_reduce(acumulador, produto):
    print("acumulador: ", acumulador)
    print("produto: ", produto)
    print()
    return acumulador + produto["preco"]

total = reduce(
    funcao_do_reduce,
    produtos,
    0
)

print("Total: ", total)
















