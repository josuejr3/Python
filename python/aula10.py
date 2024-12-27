
# Deefinindo minhas próprias funções em Python - A1 Seção 4

# def Print(a, b, c):
#     print("Várias")


# Print()

# Não é recomendado nomear começando com letra maiúscula.

def imprimir(a, b, c):
    # print("Varias 1")
    # print("Varias 2")
    # print("Varias 3")
    print(a, b, c)


imprimir(1, 2, 3)
imprimir(4, 5, 6)


# Argumentos default/padrão

def imprimir_nome(nome="Sem nome"):
    print(f"{nome}")


imprimir_nome("Josue")
imprimir_nome("Luiz Otavio")
imprimir_nome("Maaria")
imprimir_nome()


# -------- ARGUMENTOS NOMEADOS E NÃO NOMEADOS ----------


# def soma(x, y, z = 0):
#     print(f"{x=} + y={y}", "|", "x + y = ", x + y)


# def soma(x, y, z=0):
#     print(x, y, z)

# Parâmetros e argumentos default
# def soma(x, y, z = None):
#     if z is not None:
#         print(f"{x=} + y={y}", "|", "x + y = ", x + y)
#     else:
#         print(f"{x=} + y={y}")

# print(soma) # printa o tipo function e o local na memoria
# print(soma(1, 2))   # vai retornar none, porque a própria soma já é um print
# # como a função não retorna nenhum valor, apenas printa, o retorno é tipo None
#
# soma(100, 200)
# soma(100, 200, 300)
#
# print("==========================================")
#
# x = 1
#
# def escopo():
#     global x
#     x = 10
#
#     def outra_funcao():
#         x = 11
#         y = 2
#
#         print(x, y)
#     outra_funcao()
#     print(x)
#
# print(x)
# escopo()
# print(x)


print("==============RETORNO DE FUNÇÕES===============")

variavel = print("Luiz")
print(variavel)

# Retorna None

def soma(x, y):
    if x > 10:
        return 10, 20 # retorno de uma tupla sem os colchetes
    return x + y

print(soma(2, 2))
print(soma(3, 3))
print(soma(11, 55))


## Empacotamento e desempacotamento de argumentos

# DESEMPACOTANDO A TUPLA
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma2(x, y):
    return x + y

print(1, 2, 3, 4, 5)

def somar(*args):
    args = list(args)
    print(args, type(args))
    # Como eu quero somar todos os valores que eu passei basta fazer um for
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum

print(somar(1, 2, 3, 4, 5, 6))


soma_1_2_3 = somar(1, 2, 3)
print(soma_1_2_3)

# ARGS SAO APENAS PARA PARAMETROS NAO NOMEADOS

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9 # Tupla de números

# Quando eu passo eles puramente para a função sum, ela considera 9 parametros
# Sendo assim, eu posso usar o desempacotamento

print(numeros)

# ==========================================================================

# Higher Order Functions - Funções de Primeira Classe


# def saudacao(msg, nome):
#     return f"{msg}, {nome}"
#
#
# def executa(funcao, *args): # Empacotei os argumentos em um tupla
#     return funcao(*args)    # Desempacotei os argumentos da tupla
#
#
# # v = saudacao("Bom dia")
# # print(v)
#
#
# v = executa(saudacao, "Bom dia")
# print(v)
#

# ========================== CLOSURE ========================
def criar_saudacao(saudacao, nome):
    def saudar():
        return f"{saudacao}, {nome}!"

    return saudar

s1 = criar_saudacao("Bom dia", "Luiz")
print(s1) # "Bom dia, Luiz!"

s2 = criar_saudacao("Boa noite", "Maria")
print(s2)

print()






