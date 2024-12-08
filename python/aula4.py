# INTERPOLAÇÃO DE STRINGS

nome = "Josue"
preco = 1000.986453
variavel = "%s, o preco total foi de: R$%f" % (nome, preco)
print(variavel)

# Verificando valores em hexadecimal

print("O valor 303 em hexadeimcal é %04X" % 303)

# Caso eu queria representar com mais casas basta adicionar o 0 antes do x e a quantidade de casas, 0 ou 8

# fstrings

var_abc = "ABC"
print(var_abc)

# Criando padding
print(f"{var_abc:0>10}")
print(f"{100.398493849334903:.2f}")

# EXISTEM BIBLIOTECAS ESPECIFICAS PARA FORMATAÇÃO DE DATA, NUMEROS, DINHEIRO, PREÇO...

# Podemos formatar usando f-strings para mostrar virgula ao inves de pontos
# sinais de numeros e definir a quantidade de casas decimais.

print(f"{10000.3849384934932432:+,.1f}")

# conversion flags: !r !s !a chamam os metodos especiais

# FATIAMENTO DE STRINGS

"""
012345678
Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
Função len retorna o tamanho ou a quantidade de caracteres ou do iterável.
"""

v_hw = "Olá mundo"
print(v_hw[4:7])
print(len(v_hw))



name = input("Digite seu nome: ")
age = input("Digite sua idade: ")

if age and name:
    print(f"Seu nome: {name}")
    print(f"Seu nome invertido: {name[::-1]}")
    print("Tem espaços" if " " in name else "Não contém espaços")
    print(f"Seu nome tem {len(name)} letras")
    print(f"A primeira letra do seu nome é: {name[0]}")
    print(f"A última letra do seu nome é: {name[-1]}")

else:
    print("Desculpe, você deixou campos em brancos")

# 49

# Introdução ao Try e Except
a = "a"
# erro - float(a)

numero = input("Vou dobrar o número que vc digitar: ")

# if numero.isdigit():
#     numero_float = float(numero)
#     print(f"O dobro de {numero} é {2*numero_float:.2f}")
# else:
#     print("Isso nao é um numero")



try:
    print("STR:", numero)
    numero_float = float(numero)
    print(f"O dobro de {numero} é {2 * numero_float:.2f}")
except:
    print("Isso nao é um numero")





























