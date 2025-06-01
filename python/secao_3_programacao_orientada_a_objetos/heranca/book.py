class Book:
    def __init__(self, title="", year="", pages="", content=""):
        self._title = title
        self._year = year
        self._pages = pages
        self._content = content

    def read(self):
        print(f"Titulo: {self._title}")
        print(f"Ano: {self._year}")
        print(f"Quantidade de páginas: {self._pages}")
        print(f"Conteudo: {self._content}")

class BookOfMonsters(Book):



    def read(self):
        print("Mastiga, mastiga, mastiga, mastiga...")

class InvisibleBook(Book):
    def read(self):
        print("")

livro_basico = Book("Harry Potter", "1990", 230, "Historia"
                                                 "de um bruxo")

livro_basico.read()
livro_monstro = BookOfMonsters()
livro_monstro.read()

livro_inv = InvisibleBook()
livro_inv.read()