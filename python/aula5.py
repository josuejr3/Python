# Variáveis e condições

velocidade_atual = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passou_radar_1 = velocidade_atual > RADAR_1

multar_carro_radar_1 = (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade_carro_passou_radar_1


if velocidade_carro_passou_radar_1:
    print("Velocidade do carro passou do radar 1")

if multar_carro_radar_1:
    print("Carro multado em radar 1")


print(id(RADAR_RANGE))


# FLAGS - is, is not e None

# condicao = False
#
# if condicao:
#     # passou_if = True
#     print("Faça algo")
# else:
#     print("Nao faça algo")
#

# print(passou_if) -> erro pois a variavel so esta definida no if, se ela entra no else passou_if não existe

# condicao = False
# passou_no_if = None
#
# if condicao:
#     passou_no_if = True
#     print("Faça algo")
# else:
#     print("Não faça algo")
#
# print(passou_no_if, passou_no_if is not None)


# 54 - Exercicio


# Q1

# num = input("Digite um número: ")
#
# try:
#     num_int = int(num)
#     print("Numero par" if num_int % 2 == 0 else "Numero impar")
# except:
#     print("Ocorreu um erro")


# Q2

# hr = input("Digite uma hora: ")
#
# try:
#     hr_int = int(hr)
#     if 0 <= hr_int < 12 or hr_int == 24:
#         print("Bom dia")
#     elif 12 <= hr_int < 18:
#         print("Boa tarde")
#     elif 18 <= hr_int < 24:
#         print("Boa noite")
#     else:
#         print("Hora inválida")
# except:
#     print("Ocorreu um erro")


# Q3

# name = input("Qual o seu nome: ")
#
# if len(name) <= 4:
#     print("Nome curto")
# elif len(name) == 5 or len(name) == 6:
#     print("Nome médio")
# else:
#     print("Nome grande")

# Tipos built-in

string = "Luiz Otavio"
#string[3] = "ABC"
print(string[3])

# erro, strings imutáveis

# Para consertar, fazer fatiamento de strings
outra_string = f"{string[:3]}ABC{string[4:]}"

print(outra_string)

# preenche a string com 0 a esquerda até o total de 100
print(string.zfill(100))



















