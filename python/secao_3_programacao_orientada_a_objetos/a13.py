# Criando exceçoes em Python orientado a objetos

class MeuError(Exception):
    ...

class OutroError(Exception):
    ...



def levantar():
    exception_ = MeuError("a", 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Voce errou isso')
    raise exception_

try:
    #1/0
    levantar()
except (MeuError, ZeroDivisionError) as e:
    print(e.__class__.__name__)
    print(e)
    print()
    exception_2 = OutroError('Vou lançar de novo')
    exception_2.add_note('Mais uma nota')
    exception_2.__notes__ += e.__notes__.copy()
    raise exception_2 from e