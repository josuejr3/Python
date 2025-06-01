# Dunder methods, métodos especiais ou métodos mágicos

# __lt__(self, other) - self < other
# __le__(self, other) - self <= other
# __gt__(self, other) - self > other
# __ge__(self, other) - self >= other
# __eq__(self, other) - self == other
# __ne__(self, other) - self != other
# __add__(self, other) - self + other
# __sub__(self, other) - self - other
# __mul__(self, other) - self * other
# __truediv__(self, other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str - define uma forma de representação do objeto

class Ponto:
    def __init__(self, x: int, y: int, z="String"):
        self.x = x
        self.y = y
        self.z = z

    # def __str__(self):
    #     return f'({self.x}, {self.y})'

    def __repr__(self):
        class_name = self.__class__.__name__
        # class_name = type(self).__name__
        return f"{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})"

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other

p1 = Ponto(1, 2)
p2 = Ponto(3, 4)
print(p1, repr(p2))

print(f"{p2!r}")

print(p1 + p2)
print(p2 > p1)
# Utilizando outros métodos especiais

class A:
    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instancia')
        instancia = super().__new__(cls)
        print('Depois')
        instancia.x = 213
        return instancia
        # a instancia que esta sendo retornada é o nosso self

    def __init__(self):
        print("Sou o init")
    def __repr__(self):
        return 'A()'

# a = object.__new__(A)
# a.__init__()

a = A()
print(a)