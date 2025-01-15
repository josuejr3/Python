import json
import os


#
# pessoas = [
#     {
#         "nome": "maria",
#         "sobrenome": "vieira",
#         "idade": 23,
#         "ativo": False,
#         "notas": ["A", "A+"],
#         "telefones":{
#             "residencial": "00 0000-0000",
#             "celular": "00 0000-0000",
#         }
#     },
#
#     {
#         "nome": "joana",
#         "sobrenome": "moreira",
#         "idade": 27,
#         "ativo": False,
#         "notas": ["A", "B+"],
#         "telefones": {
#             "residencial": "00 0000-0000",
#             "celular": "00 0000-0000",
#         }
#     }
# ]

BASE_DIR = os.path.dirname(__file__)
# SAVE_TO = os.path.join(BASE_DIR, "arquivo-python.json")

# with open(SAVE_TO, "w") as file:
#     json.dump(pessoas, file, indent=2)


# o dumps serve para ver em formato de string

# print(json.dumps(pessoas, indent=2))

#importando
JSON_FILE = os.path.join(BASE_DIR, "arquivo-python.json")


with open(JSON_FILE, "r") as file:
    pessoas = json.load(file)

    for pessoa in pessoas:
        print(pessoa["nome"])


















