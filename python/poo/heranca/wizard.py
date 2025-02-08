from human import Human

class Wizard(Human):
    def __init__(self, name, idade, house, spell):
        super().__init__(name, idade)
        self.__houses = ('Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff', 'Grifinoria', 'Sonserina', 'Corvinal', 'Lufa-Lufa')
        self.spell = spell
        self.house = house


    @property
    def house(self):
        return self.__house

    @house.setter
    def house(self, house):
        if house not in self.__houses:
            house = 'Sem casa ainda'
        self.__house = house

    @property
    def spell(self):
        return self.__spell

    @spell.setter
    def spell(self, spell):
        self.__spell = spell

    def cast_spell(self):
        return f"Lançando feitiço: {self.spell}!"

    def display(self):
        return f"Nome: {self.nome}\nCasa: {self.house}\nSpell: {self.spell}"


# harry = Wizard("Harry", "Gryffindor", "Expecto Patronum")
# draco = Wizard("Draco", "Slytherin", "Sectumsempra")
# cedric = Wizard("Cedric", "Hufflepuff", "Accio")
# miguel = Wizard("Miguel", "Ravenclaw", "Reducto")
# murta = Wizard("Murta", "A", "?")
#
# print(harry.display())
# print("\n")
# print(draco.display())
# print("\n")
# print(cedric.display())
# print("\n")
# print(miguel.display())
#
# print(murta.display())
#
# harry.house = "Grifinoria"
# draco.house = "Sonserina"
# cedric.house = "Lufa-Lufa"
# miguel.house = "Corvinal"
# harry.name = "H"
# draco.name = "D"
# cedric.name = "C"
# miguel.name = "M"
# harry.spell = "1"
# draco.spell = "2"
# cedric.spell = "3"
# miguel.spell = "4"
#
# print(harry.display())
# print("\n")
# print(draco.display())
# print("\n")
# print(cedric.display())
# print("\n")
# print(miguel.display())
# print("\n")
# print(murta.display())
#
#
#
# print(harry.cast_spell())
# print("\n")
# print(draco.cast_spell())
# print("\n")
# print(cedric.cast_spell())
# print("\n")
# print(miguel.cast_spell())
# print("\n")

































































