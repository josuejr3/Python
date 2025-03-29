# Criando sua própria lista com iterable. iterator e sequence (collections abc)

# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Iterable, Iterator, Sequence

class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        print()
        return self._data[index]


if __name__ == '__main__':
    lista = MyList()
    lista.append('maria')
    lista.append('joao')
    print(lista[0])
