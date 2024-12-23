"""
Criar uma lista de compras, o usuário, pode:
1 - Inserir itens na lista
2 - Apagar itens na lista
3 - Lista valores
Obs: não permite que índices inxesitentes na lista sejam quebrados
"""

# lista = list()
#
# while True:
#
#     print("Seleciona uma opção")
#     option = input("[i]nserir [a]pagar [l]istar: ").upper()
#
#     try:
#         if option.startswith("I"):
#             value = input("Digite um valor: ")
#             lista.append(value)
#         elif option.startswith("A"):
#             index = input("Digite o índice: ")
#             try:
#                 index = int(index)
#                 total_index = len(lista)
#                 lista.pop(index-1)
#                 # Ou então del lista[indice]
#             except (ValueError, IndexError):
#             # Usar parenteses para várias exceções
#                 print("Não foi possível apagar esse indíce")
#             # Ou usar vários except e tratar um de cada
#         elif option.startswith("L"):
#             if not lista:
#                 print("Lista vazia")
#             for number, product in enumerate(lista, start=1):
#                 print(f"{number}: {product}")
#         else:
#             print("Por favor, escolha I, A ou L")
#     except KeyboardInterrupt:
#         print("\nInterrupão do Teclado")


# ==============================================================

# Imprecisão de números flutuantes

import decimal

# numero1 = 0.1
# numero2 = 0.7
# numero3 = numero1 + numero2
# print(numero3)      # -> 0.7999999999 Valor impreciso

# ou então, outra opção

# print(round(numero3, 3))

# A terceira forma de usar um número é usando a classe Decimal que está dentro do módulo decimal

# numero1 = decimal.Decimal("0.1")
# numero2 = decimal.Decimal("0.7")
# numero3 = numero1 + numero2
# print(round(numero3, 2))

# =======================================================

# Metodo split divide a string baseada em um caractere e transforma em lista
# print(frase.split())
# print(frase)
#
# print(frase.split('o'))

# frase = "       olha so que       ,   coisa interessante       "
# lista_frases_cruas = frase.split(',')
#
# lista_frases = []
#
# for i, frase in enumerate(lista_frases_cruas):
#     lista_frases.append(lista_frases_cruas[i].strip())
#
# # Método strip remove espaços das laterais
# # lstrip remove da esquerda
# # rstrip remove da direita
#
# # print(lista_frases_cruas)
# # print(lista_frases)
#
# # frases_unidas = "-".join(lista_frases)
# # print(frases_unidas)
#
#
# # =======================================
#
# # Iteráveis dentro de iteráveis
#
salas = [

    # 0    1    2
    ["A", "B", "C"],
    # 0
    ["D"],
    # 0    1
    ["G", "H"]

]
#
# # Para acessar eu devo escolher o índice do iterável e depois o elemento dentro dele
# print(salas[2][0])
#
# for sala in salas:
#     print(sala)
#
# # melhor, item por item
# for i in range(len(salas)):
#     for j in range(len(salas[i])):
#         print(salas[i][j])


# Desempacotamento de funções

# string = "ABCD"
# lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
# tupla = "Python", "É", "LEGAL"
#
# a, b, *_, final  = lista
# print(a, final)
#
# for nome in lista:
#     print(nome, end=' ')
#
# print("\n===========")
#
# print(*lista)
# print(*tupla)
# print(*string)
#
# # Exibindo todos os elementos da matriz
# print(*salas, sep="\n")

# OPERACAO TERNARIA EM PYTHON

# forma direta
# print("Valor" if True else "Outro valor")

condicao = 10 == 10

variavel = "Valor" if condicao else "Outro valor"
print(variavel)

# digito = 10
#novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)
























