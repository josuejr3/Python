class Armor:

    def __init__(self, constellation):
        self._constellation = constellation
        self._armor_type = None

    @property
    def constellation(self):
        return self._constellation

    @constellation.setter
    def constellation(self, value):
        self._constellation = value

    @property
    def armor_type(self):
        return self._armor_type

    @armor_type.setter
    def armor_type(self, value):
        self._armor_type = value

