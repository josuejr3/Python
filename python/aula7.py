# texto = "Python"
#
# for letra in texto:
#     print(letra)
#
# # o range
# print('========================')
# numeros = range(5)
#
# for numero in numeros:
#     print(numero)
#
#
#
# for i in range(10):
#     if i == 2:
#         print("i é 2, pulando...")
#         continue
#     if i == 8:
#         print("i é 8, seu else nao vai executar")
#         break
#     for j in range(1, 3):
#         print(i, j)
# else:
#     print("for completo com sucesso")


# Exercicio

import os

palavra_misteriosa = "PERFUME"
mascara = ""
cont = 0

while True:

    os.system("cls")

    entrada = input("Digite uma letra: ").upper()
    cont += 1

    if len(entrada) > 1:
        print("Digite apenas uma letra.")
        continue

    if entrada in palavra_misteriosa:
        mascara += entrada

    palavra_formada = ""
    for letra in palavra_misteriosa:
        if letra in mascara:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_misteriosa:
        print("Parabens voce ganhou!")
        print(f"Tentativas: {cont}")
        break












