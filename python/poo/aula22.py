# usando namedtuple

from collections import namedtuple

# nome da ""classe""   nome da ""classe""            ""membros""
Carta = namedtuple('Carta', ['valor', 'naipe'])

as_de_espadas = Carta('A', '♠️')
print(as_de_espadas)
print(as_de_espadas.valor)
print(as_de_espadas.naipe)

print("----------------------------")
for v in as_de_espadas:
    print(v)