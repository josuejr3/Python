# Exercicio - Sistema de Perguntas e Respostas Dicionarios

# import random
#
# perguntas = [
#
#     {
#         "Pergunta": "Quanto é 2 + 2?",
#         "Opções": [5, 1, 4, 7],
#         "Resposta": 4,
#     },
#     {
#         "Pergunta": "Quanto é 5 * 5?",
#         "Opções": [25, 55, 10, 51],
#         "Resposta": 25,
#     },
#     {
#         "Pergunta": "Quanto é 10 / 2?",
#         "Opções": [2, 5, 4, 1],
#         "Resposta": 5,
#     }
#
# ]
#
# # MEU CODIGO
#
# while True:
#     qtd_perguntas = len(perguntas)
#
#     # Sorteia uma pergunta
#
#     indice = random.randint(0, qtd_perguntas-1)
#
#     # Escolhendo pergunta definitiva
#     pergunta = perguntas[indice]        # dicionario
#
#
#     print("==========================")
#     print(f"Pergunta: {pergunta["Pergunta"]}")
#     resposta_pergunta = pergunta["Resposta"]
#
#     # Imprimindo as opções com enumerate
#     for i, opcoes_resposta in enumerate(pergunta["Opções"], start=1):
#         print(f"{i}) {opcoes_resposta}")
#
#     # Coletando entrada
#     opcao_usuario = input("Escolha uma opção: ")
#
#     # Testando entranda
#     try:
#         opcao_usuario_int = int(opcao_usuario)
#
#         if pergunta["Opções"][opcao_usuario_int-1] == resposta_pergunta:
#             print("Parabéns!! Você Acertou!!! 😁🤙")
#
#         elif opcao_usuario_int <= 0:
#             print("Opção inválida")
#
#         else:
#             print("Não foi dessa vez, tente novamente! 😱😭")
#     except IndexError:
#         print("Opção inválida")
#     except ValueError:
#         print("Opção inválida")
#




# CÓDIGO DO PROFESSOR


# qtd_acertos = 0
# for pergunta in perguntas:
#     print(f"Pergunta: {pergunta["Pergunta"]}")
#     print()
#
#     opcoes = pergunta["Opções"]
#     qtd_opcoes = len(opcoes)
#     for i, op in enumerate(pergunta["Opções"], start=1):
#         print(f"{i}) {op}")
#
#     print()
#
#     escolha = input("Escolha uma opção: ")
#     print()
#
#     acertou = False
#     escolha_int = None
#     if escolha.isdigit():
#         escolha_int = int(escolha)
#
#     if escolha_int is not None:
#         if 0 <= escolha_int < qtd_opcoes:
#             if opcoes[escolha_int-1] == pergunta["Resposta"]:
#                 qtd_acertos += 1
#                 acertou = True
#
#     if acertou:
#         print("Acertou!")
#     else:
#         print("Errou!")
#
# print("Você acertou", qtd_acertos)
# print("de", len(perguntas), "perguntas")


lista_de_lista_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontra_duplicado(lista: list) -> int:

    conjunto = set()
    primeiro_duplicado = -1

    for i in range(len(lista)):
        if lista[i] in conjunto:
            primeiro_duplicado = lista[i]
            break

        # Baseado no nome -                 >>>>>>     JOSUE    <<<<<<
        # tamanho_antes = len(conjunto)
        conjunto.add(lista[i])
        # tamanho_apos = len(conjunto)
        # if tamanho_antes == tamanho_apos:
        #     return lista[i]
    return primeiro_duplicado

for l in lista_de_lista_de_inteiros:
    valor_duplicado = encontra_duplicado(l)
    print(valor_duplicado)
















