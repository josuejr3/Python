# Criando sua própria lista com iterable. iterator e sequence (collections abc)

# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Iterable, Iterator, Sequence

class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            raise StopIteration
        value = self._data[self._next_index]
        self._next_index += 1
        return value

if __name__ == '__main__':
    lista = MyList()
    lista.append('maria')
    lista.append('joao')
    # print(lista[0])


    for item in lista:
        print(item)
