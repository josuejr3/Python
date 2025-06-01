# Usando enum

import enum

class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2


#Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise TypeError('direcao invalida')


    print(f'Movendo para {direcao.name.title()} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
# mover('baixo')
# mover('cima')

# CHAMANDO PELO VALOR - O VALOR É A ENUMERAÃO EM SI
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)


# Pegando somente o nome e o valor da numeração (indice)
print(Direcoes(1).name, Direcoes(1).value)
print(Direcoes['DIREITA'].name, Direcoes.DIREITA.value)


class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2



