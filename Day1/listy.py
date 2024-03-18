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
    random_list_1 = []
    random_list_2 = []
    for i in range(10):
        random_list_1.append(random.randint(1, 10))
        random_list_2.append(random.randint(1, 10))

    print(random_list_1)
    print(random_list_2)
    ###########################

    lista = [0, 1, 2]
    lista2 = [3, 4, 5]

    # for el in lista2:
    #     lista.append(el)

    joined_list = lista + lista2
    print(joined_list)

    joined_list.remove(3)
    print(lista)

    random_list_comp = [random.randint(1, 10) for i in range(10)]
    print(random_list_comp)

    # Napisz kod który umieści w liście 10 kolejnych potęg liczby 2 uzywajac list składanych. 2 ** 2 = 4, 2 ** 3 = 8





