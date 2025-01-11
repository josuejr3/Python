
from copy import deepcopy
from dados import produtos

# produtos = [
#     {"nome": "Produto 5", "preco": 10.00},
#     {"nome": "Produto 1", "preco": 22.32},
#     {"nome": "Produto 3", "preco": 10.11},
#     {"nome": "Produto 2", "preco": 105.87},
#     {"nome": "Produto 4", "preco": 69.90},
# ]

# novos_produtos = [{**deepcopy(produto)} for produto in produtos]
# novos_produtos = [{**produto, "preco": round(produto["preco"] * 1., 2)} for produto in novos_produtos]
#
# produtos_ordenados_por_nome = [{**deepcopy(produto)} for produto in novos_produtos]
# produtos_ordenados_por_nome.sort(key=lambda x: x["nome"], reverse=False)
#
# produtos_ordenados_por_preco = [{**deepcopy(produto)} for produto in produtos_ordenados_por_nome]
# produtos_ordenados_por_preco.sort(key=lambda x: x["preco"], reverse=False)
#
# for i in range(len(produtos)):
#     for c, v in produtos_ordenados_por_nome[i].items():
#         print(f"{c} - {v}")
#
#
# # Parametro key
# # recebe um item da lista e organiza a lista a partir da chave "nome" dos items
#
#
# # ex - lista de strings
# # words = ["A", "b", "amapa", "Casa", "deseho", "brinquedo"]
# # # organizando através apenas de todas as palavras como minusculas.
# # print(sorted(words, key=lambda word: word.lower()))
#
# # ============================================================================================================
# #                                              CÓDIGO AULA
#
# # 1
#
# novos_produtos_1 = [
#     {**p, "preco": round(p["preco"] * 1.1, 2)} for p in deepcopy(produtos)
# ]
#
# # 2
#
# produtos_ordenados_por_nome_1 = sorted(deepcopy(produtos), key=lambda x: x["nome"], reverse=False)
#
# # 3
# produtos_ordenados_por_preco_1 = sorted(deepcopy(produtos), key=lambda x: x["preco"])
#
# print(produtos_ordenados_por_preco_1, sep="\n")

# ================================================================================================================


def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x):
    # adiando execucao e closure - criando uma funcao mais interna, porém, sem executar

    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = criar_funcao(soma, 5)
multiplica_com_dez = criar_funcao(multiplica, 10)

# CLOSURES

print(soma_com_cinco(10))
print(multiplica_com_dez(2))

# as funções internas lembra das constantes

# retorna a função sem executar
# criam funções internas para guardar valores e coisas importantes
# no retorno vira uma funcao para passarmos parametros posteriores




















