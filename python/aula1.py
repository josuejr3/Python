# Comentários são feitos com hashtag

# Outra forma de realizar "comentários" é usando o """ """ <- Docstring

"""
Docstrigs
"""

# Uso da função print
print(123, 456, sep="\n")

print("aaaa", end="3\n")

# Tipos
# Strings
print("string")
print('string')

# Uso do r, é uma alternativa para exibir caracteres (o r é usado para expressões regulares)
print(r"Testando \"Teste")

# Tipo int - inteiros
print(11)
print(-11)
print(0)

# Tipo float - ponto flutuante/quebrado

print(3.5)
print(0.46)
print(-123.77)

# Função type() retorna o tipo do objeto
print(type("str"))

# Tipo de dado Boolean - booleano, retorna True ou False
print(10 == 10)
print("x" == "X")

# Conversão/Coerção de Tipos
print(1+1)  # correto, da certo
print("a" + "b") # correto, junta strings
# print(1 + "1") # erro, soma/concatenação de objetos diferentes

print(int("1"), type(int("1")))

# int(), str(), type() são classes
# strings vazias são consideradas falsas, strings com alguma coisa são verdadeiras

print(str(11)+"b")




