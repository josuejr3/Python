# PEP-8

nome_completo = "Josue Junior"
idade = 20 + 3

print("Nome completo:", nome_completo, "Idade:", idade)
print("É maior?", idade >= 18)
int_um = int('1')
print(int_um)

print("valor: ", int_um)

# Exercicio

nome1 = "Jose"
sobrenome1 = "Julio"
idade1 = 23
ano_nascimento1 = 2024 - idade1
maior_de_idade1 = idade1 >= 18
altura1 = 1.72

print("Nome:", nome1)
print("Sobrenome:", sobrenome1)
print("Idade:", idade1)
print("Ano:", ano_nascimento1)
print("Maior:", maior_de_idade1)
print("Altura:", altura1)

# Operadores todo numero que vem apos sera zerado

a = 10 + 10
b = 10 + 10
c = 10 * 10
d = 10 / 10
e = 10 // 10
f = 10 % 10
g = 10 ** 10


# Concatenacao
conct = "Josue" + "Junior" + str(0b01)
print(conct)

# Sinal de multiplicaco, multiplica caracteres
string = 10 * 'A'
print(string)


# Precedência de operadores

# -  Parênteses;
# -  Potência;
# -  Multiplicação, divisão, divisão inteira e resto da divisão;
# -  Adição e subtração

conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)

nome = "JJ"
altura = 1.72
peso = 60.0
idade = 23
imc = ...

# ... é um place holder, usado para definir um código que ainda não foi definido o que ele faz
# serve como tapa buraco

imc = peso / (altura**altura)

print(imc)

ponto_flutuante = 40.75123985
pf = f"{ponto_flutuante:.2f}"
print(pf)


a = 'A'
b = 'B'
c = 2.35331325
formato = 'a={} b={} c={:.2f}'.format(a, b, c)
formato = 'a={0} b={1} c={2:.2f}'.format(a, b, c)
print(formato)


# Até a aula 32



