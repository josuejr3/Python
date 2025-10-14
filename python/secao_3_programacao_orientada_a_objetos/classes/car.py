class Car:
    def __init__(self, name, year=1886):
        # chama o setter e altera o atributo
        self.year = year
        self.name = name

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @name.setter
    def name(self, name):
        # altera o atributo
        self.__name = "Sem marca" if name == "" else name

    def displayMessage(self):
        return f"Carro da marca: {self.name} do ano {self.year}"


carro1 = Car("")
print(carro1.displayMessage())

carro2 = Car("Renault")
print(carro2.displayMessage())
print(carro2.name)
carro2.name = "Hyundai"
carro2.year = 2017
print(carro2.displayMessage())
print(carro2.year)
carro2.year = 2020
carro2.name = "Honda"
print(carro2.year)
print(carro2.name)
print(carro2.displayMessage()) 


printf("Oi")

