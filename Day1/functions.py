import operator
import random
import os
import re
from collections import defaultdict



def times2(a: int | list) -> str | int:  # Union[str, int]
    if a == 0:
        return "przez zero nie mnoze"
    return a * 2

if __name__ == '__main__':
    print(times2(2))

    print(times2("Napis")) # mypy tu jest bład
    print(type(times2([1,2,3,4])))

    def funkcja_jako_argument(f, x: int):
        print(f(x))


    funkcja_jako_argument(times2, 33)
    funkcja_jako_argument(lambda arg: arg + 2, 3)


    def powieksz(x: str) -> str:
        return x.upper()

    def tytul(napis: str) -> str:
        return napis.title()

    def zastosuj_dla_wszystkich(fun, *strings):
        print(strings)
        for a in strings:
            print(fun(a))

    zastosuj_dla_wszystkich(powieksz, 'siała', 'baba', 'mak')
    zastosuj_dla_wszystkich(tytul, 'siała', 'baba', 'mak', )

    # Stwórz funkcję która wydrukuje na konsoli sumę wartości przekazanych do niej jako *args
