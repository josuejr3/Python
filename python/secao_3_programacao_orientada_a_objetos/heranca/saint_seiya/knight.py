from character import Character

class Knight(Character):
    def __init__(self, name, age, height, weight, place_of_birth, constellation, armor_type, special_moves):
        super().__init__(name, age, height, weight, place_of_birth)
        self._constellation = constellation
        # classe armadura
        self._armor_type = armor_type
        self._special_moves = special_moves
        self._cosmos_level = 0

    @property
    def _constellation(self):
        return self._constellation

    @property
    def _armor_type(self):
        return self._armor_type

    @_armor_type.setter
    def _armor_type(self, armor):
        self._armor_type = armor

    @property
    def _cosmos_level(self):
        return self._cosmos_level

    @_cosmos_level.setter
    def _cosmos_level(self, value):
        self._cosmos_level = value

    def cosmos_awaken(self):
        if self._cosmos_level < 100:
            self._cosmos_level = self._cosmos_level + 1

    def attack(self):
        return self._special_moves



