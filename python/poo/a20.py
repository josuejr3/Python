# class Foo:
#     ...
#
# f = Foo()
# print(isinstance(f, Foo))
#
# print(type(Foo))
#
# # Recriando a classe Foo usando a meta classe type
#
# Foo = type('Foo', (object,), {})
# g = Foo()
# print(type(Foo))
# print(type(g))


# Metaclasses

import sys
def meu_repr(self):
    return f'{type(self).__name__}({repr(self.__dict__)})'

class Meta(type):
    # New da meta classe vai ser responsável por criar a classe abaixo, Pessoa

    def __new__(mcs, name, *args, **kwargs):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, *args, **kwargs)
        cls.attr = 1234
        cls.__repr__ = meu_repr

        # definindo um metodo da metaclasse que deve ser criado nas outras classes
        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplemented('Implemente falar')

        return cls


    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplemented('Crie o attr nome')

        return instancia





class Pessoa(object, metaclass=Meta):

    #falar = 123

    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print('Falando...')

p1 = Pessoa('Luiz')
p1.falar()
# Criando uma metaclasse




















