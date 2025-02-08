class Character:
    def __init__(self, name, age, height, weight, place_of_birth):
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight
        self.place_of_birth = place_of_birth
        self._sleeping = False

    @property
    def _name(self):
        return self._name

    @property
    def _age(self):
        return self._age

    @_age.setter
    def _age(self, new_age):
        if new_age > self._age:
            self._age = new_age

    @property
    def _height(self):
        return self._height

    @_height.setter
    def _height(self, new_height):
        if new_height > self._height:
            self._height = new_height

    @property
    def _weight(self):
        return self._weight

    @_weight.setter
    def _weight(self, new_weight):
        if new_weight:
            self._weight = new_weight

    @property
    def place_of_birth(self):
        return self.place_of_birth

    @place_of_birth.setter
    def place_of_birth(self, new_place):
        self.place_of_birth = new_place

    def introduce(self):
        return f"Hi, my name is {self._name} and I am {self._age} years old"

    def talk(self, msg):
        return f"{self._name} says: {msg}"

    def sleep(self):
        self._sleeping = True




