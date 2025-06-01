import json
import os


class Pessoa:
    def __init__(self, nome, idade, cpf, estado):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.estado = estado


    def apresentar(self):
        return f"Me chamo {self.nome} e tenho {self.idade}"
    

pessoa1 = Pessoa("Josue", 24, "123456789101", "PB")
pessoa2 = Pessoa("Maria", 22, "234439849343", "PB")

lista_de_pessoas = [vars(pessoa1), pessoa2.__dict__]


# retorna pasta atual
BASE_DIR = os.path.dirname(__file__)

NEW_DIR = os.path.join(BASE_DIR, "save_class.json")


with open(NEW_DIR, "w", encoding="utf-8") as f:
    json.dump(lista_de_pessoas, f, indent=2, ensure_ascii=False)


