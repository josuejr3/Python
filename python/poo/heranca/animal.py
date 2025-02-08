class Animal:
    def __init__(self, nome, raca):
        self._nome = nome
        self._raca = raca

    @property
    def nome(self):
        return self._nome
    @property
    def raca(self):
        return self._raca
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @raca.setter
    def raca(self, raca):
        self._raca = raca
    def caminhar(self):
        print(f"The {self.__class__.__name__} is walking")


class Dog(Animal):

    def bark(self):
        print("Au au au!")

class Cat(Animal):

    def meow(self):
        print("Miau miau miau")

animal_abs = Animal("Anika", "desconhecida")
animal_abs.caminhar()

animal_abs.nome = "Who"
print(animal_abs.nome)
animal_abs.raca = "?"
print(animal_abs.raca)

lola = Cat("Lola", "SRD")
print(lola.nome)
print(lola.raca)
lola.caminhar()
lola.meow()

lola.nome = "Miley"
print(lola.nome)
lola.caminhar()

lola.raca = "alguma raca"
print(lola.raca)























