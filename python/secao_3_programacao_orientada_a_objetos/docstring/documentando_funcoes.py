"""
Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções.
A função soma você já conhece bastante.
"""

variavel_1 = 1

def soma(x: int | float, y: int | float) -> int | float:
    """
    Soma x e y

    Este módulo contém funções e exemplos de documentação de funções.
    A função soma você já conhece bastante.

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float
    :return: A soma entre x e y
    :rtype: int or float
    """

    return x + y


# documentando classe
class Foo:
    """
    A CLASSE FOO NAO FAZ NADA
    """
    def soma(self, x, y):
        return x + y

    def bar(self) -> int:
        """O que ele faz

        :raises: NotImplementedError: Se o método não for definido
        """
        raise NotImplemented('Teste')




