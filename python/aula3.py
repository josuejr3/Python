# Função para coletar entrada

nome = input('Qual o seu nome? ')

print(f'O seu nome é: {nome}')
# outra alternativa é
print(f'O seu nome é: {nome=}')

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um outro numero: "))

# Posso fazer o typecasting ja na coleta de entrada POREM NAO EH RECOMENDADO

soma = num1 + num2
print(f"A soma é: {soma=}")

# Operações condicionais

entrada = input('Você quer "entrar" ou "sair" ?')

if entrada == "entrar":
    print("Voce entrou no sistema")
elif entrada == "sair":
    print("Voce saiu do sistema")
else: print("erro")


condicao = True
if condicao:
    print("Voce acertou")
else:
    print("Voce errou")


if 10 == 10:
    print("Outro if")

print("Fim do programa")

# Operadores relacionais (comparação)

# >   maior
# <   menor
# >=  maior ou igual
# <=  menor ou igual
# ==  igual
# !=  diferente

maior = 3 > 2
menor = 2 < 3
maior_ou_igual = 4 >= 1
menor_ou_igual = 1 <= 2
igual = 'b' == 'b'
diferente = 'a' != 'b'

# Exercicio

first_value = input('Digite o primeiro valor: ')
second_value = input('Digite o segundo valor: ')

if first_value == second_value:
    print("Voce acertou")
elif first_value > second_value:
    print(f"Voce errou o valor {first_value} é maior que {second_value}")
elif first_value < second_value:
    print(f"Voce errou o valor {second_value} é maior que {first_value}")


# Operadores lógicos

# AND

entrada = input("[E]ntrar [S]air: ")
senha_d = input("Digite sua senha: ")
senha = '123'

if entrada == "S":
    print("Voce saiu")
elif (entrada == "E" or entrada == "e") and senha_d == senha:
    print("Voce entrou")

print(True and True and True) # True
print(True or False or 0 or 'abc') # True

# Exemplo

snh = input('Digite a senha: ') or "Sem senha"
print(snh)

# EXEMPLO USANDO NOT

if not snh:
    print("Voce nao digitou nada")


# OPERADORES QUE ENVOLVEM ITERAVEIS

nome = "OTAVIO"
print(nome[2])
print(nome[-4])

# exemplos de uso de verificao se esta EM
print('A' in nome)
print('Z' in nome)
print("VIO" in nome)




