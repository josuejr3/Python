import json
import os

# função que imprime "mais organizado"
from pprint import pprint

string_json = """
    {
    "title": "O Senhor dos Aneis: A Sociedade do Anel",
    "original_title": "The Lord Of The Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
    }

"""

filme = json.loads(string_json)

pprint(filme, width=40)
print(filme['title'])
print(filme['characters'][0])

from typing import TypedDict

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list
    budget: None

# sintaxe com typedict
filme: Movie = json.loads(string_json)
print(filme["characters"])


print(json.dumps(filme, ensure_ascii=False, indent=2))

############ AULA 18

filme_dict = {'title': 'O Senhor dos Aneis: A Sociedade do Anel',
              'original_title': 'The Lord Of The Rings: The Fellowship of the Ring',
              'is_movie': True, 'imdb_rating': 8.8, 'year': 2001,
              'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
              'budget': None}

NOME_ARQUVO = "aula18_m4.json"
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    # o file ja pega o caminho absoluto
    os.path.join(os.path.dirname(__file__), NOME_ARQUVO)
)

# "Exportando para arquivo json"
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding="utf-8") as file:
    json.dump(filme_dict, file, indent=4, ensure_ascii=False)

# 'Convertendo para arquivo json"
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as file:
    filme_do_json = json.load(file)
    print(filme_do_json)

















