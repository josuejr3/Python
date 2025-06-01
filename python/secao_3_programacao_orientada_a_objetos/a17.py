# Funções decoradoras e decoradores com classes

# DECORADOR
def adiciona_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f"{class_name}({class_dict})"
        return class_repr
    cls.__repr__ = my_repr
    return cls


class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f"{class_name}({class_dict})"
        return class_repr

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')
terra = Planeta('Terra')
marte = Planeta('Marte')

# Time = adiciona_repr(Time)
# Planeta = adiciona_repr(Planeta)


print(brasil)
print(portugal)
print(terra)
print(marte)


# Agora adicionando o repr personalizado na classe time

Time = adiciona_repr(Time)
Planeta = adiciona_repr(Planeta)
