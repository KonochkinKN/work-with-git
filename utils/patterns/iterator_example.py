from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalOrderIterator(Iterator):
   # текущее положение обхода
    _position: int = None
    # шаг обхода
    _step: int = 1

    def __init__(self, collection: WordsCollection, step: int = 1) -> None:
        self._collection = collection
        self._step = step
        self._position = -1 if step < 0 else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += self._step
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, -1)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection(['A', 'B', 'C', 'D'])

    print("Прямой проход:")
    print("\n".join(collection))
    print("")

    print("Обратный проход:")
    print("\n".join(collection.get_reverse_iterator()), end="")