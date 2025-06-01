# property = getter

class Pen:
    def __init__(self, color):
        self.color = color
        self._color_tip = None


    # getters em Python
    @property
    def color(self):
        print('PROPERTY')
        return self._cor


    @color.setter
    def color(self, color):
        print("ESTOU NO SETTER")
        self._cor = color

    @property
    def color_tip(self):
        return self._color_tip

    @color_tip.setter
    def color_tip(self, color):
        self._color_tip = color



def mostrar(caneta):
    return caneta.color


# caneta = Pen('Azul')
# print(caneta.color)
# print(caneta.tip)
caneta = Pen("red")

print(caneta.color)
caneta.color = "Rosa"
print(caneta.color)

print("===============================================================")

# modificadores de acesso em Python

class Foo:
    def __init__(self):
        self.public = "isso eh publico"
        self._protected = "isso eh protegido" # ok
        self._metodo_protected() # ok
        self.__private = 'isso eh private'

    def metodo_public(self):
        # self._metodo_protected() # ok
        print(self.__private)
        return "metodo publico" # ok

    def _metodo_protected(self):
        return "_metodo_protected" # ok

    def __metodo_private(self):
        return "metodo private"

f = Foo()
print(f._protected)
print(f._metodo_protected())

# ocorre erro de atributo
print(f._Foo__metodo_private())

# print(f.public)
# print(f.metodo_public())











