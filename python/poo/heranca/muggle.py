from human import Human

class Muggle(Human):

    def __init__(self, nome, idade, profession):
        super().__init__(nome, idade)
        self._profession = profession

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, profession):
        self._profession = profession


    def speak_profession(self):
        return f"Minha profissão é {self.profession} e eu sou um {self.__class__.__name__}"
