# Laços de repetição


# condicao = True
# cont = 0
#
# while condicao:
#     nome = input('Qual o seu nome? ')
#     print(f'Seu nome é: {nome}')
#     cont += 1
#     if cont == 3: break
#
# a = 1

# comando inline em python

# if a == 1: print("a é 1")
# else: print("a n eh 1")

# exemplo usando condicao explicita

# count = 0
# while count < 100:
#     count += 1
#
#     if count == 10:
#         print("nao mostro o 10")
#         continue
#
#     print(count)
#     if count == 40:
#         break
#
# print("Acabou")


# LAÇOS ANINHADOS


# qtd_linhas = 5
# qtd_colunas = 5
#
# linha = 1
#
# while linha <= qtd_linhas:
#     col = 1
#     while col <= qtd_colunas:
#         print(f"{linha=}, {col=}")
#         col+=1
#
#     linha+=1
#
# print("Acabou")

# nome = "maria helena"
# size_name= len(nome)
#
# nova_string = ""
#
# i = 0
#
# while i < size_name:
#
#     nova_string += ("*" + nome[i])
#
#     print(f"*{nome[i]}", end="")
#     i += 1
#
# # Ou se quiser outra solução criando uma nova variavel
#
# nova_string+='*'
# print("\n" + nova_string)


# Exercicio de calculadora

# while True:
#
#     numeros_validos = None
#
#     n1 = input("Digite o primeiro número: ")
#     n2 = input("Digite o segundo número: ")
#     op = input("Digite o operador (+-/*): ")
#
#     try:
#         n1_int = int(n1)
#         n2_int = int(n2)
#         numeros_validos = True
#
#     except:
#         print("Uma das entradas não é um número")
#         numeros_validos = None
#
#     if numeros_validos is None:
#         print("Um ou ambos os números são inválidos, tente de novo")
#         continue
#
#     operadores_permitidos = "+-/*"
#
#     if op not in operadores_permitidos:
#         print("Operador não permitido")
#         continue
#
#     if len(op) > 1:
#         print("Somente um operador")
#         continue
#
#     if op == '+':
#         r = n1_int + n2_int
#         print(f"Resultado={r}")
#     elif op == '-':
#         r = n1_int - n2_int
#         print(f"Resultado={r}")
#     elif op == '*':
#         r = n1_int * n2_int
#         print(f"Resultado={r}")
#     elif op == '/':
#         r = n1_int / n2_int
#         print(f"Resultado={r}")
#
#     sair = input("Deseja sair? S ou N").lower().startswith('s')
#     if sair is True:
#         break

# While else

#
# string = "Valor qualquer"
#
# i = 0
# while i < len(string):
#     letra = string[i]
#     print(letra)
#     i+= 1
#
# else:
#     print("O else é executado.")


frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum."

i = 0
letra_anterior_qtd = 0
letra = ''

while i < len(frase):

    letra_atual = frase[i]
    qts_vezes_apareceu = frase.count(letra_atual)

    if letra_anterior_qtd <= qts_vezes_apareceu and not letra_atual.isspace() and letra_atual != '.':
        letra_anterior_qtd = qts_vezes_apareceu
        letra = frase[i]

    i += 1
print(letra, letra_anterior_qtd)















