import operator
import random
import os
import re
from collections import defaultdict


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Pyton Kurs')

    lista = [0, 1, 2]
    lista2 = list()
    lista.append(1)

    print(lista)

    print(lista[0])
    print(lista[1:3])
    print(lista[-1])

    for element in lista:
        print(element)

    for index, element in enumerate(lista):
        print(f'Wypisuje {index} : {element}')

    example_rand = random.randint(1, 10)
    print(example_rand)

    #  Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10. Wypisz listy na konosole
