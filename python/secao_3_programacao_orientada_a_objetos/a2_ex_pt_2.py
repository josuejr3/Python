from a2_ex import NEW_DIR, Pessoa
import json


with open(NEW_DIR, "r", encoding="utf-8") as f:
    pessoas = json.load(f)
    
    p1 = Pessoa(**pessoas[0])
    print(p1.nome)

    p2 = Pessoa(**pessoas[1])
    print(p2.nome)