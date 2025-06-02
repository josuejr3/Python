import json

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