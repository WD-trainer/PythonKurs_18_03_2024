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
    lista.extend(lista2)

    joined_list = lista + lista2
    print(joined_list)


    joined_list.remove(3)
    print(lista)

    random_list_comp = [random.randint(1, 10) for i in range(10)]
    print(random_list_comp)

    # Napisz kod który umieści w liście 10 kolejnych potęg liczby 2 uzywajac list składanych. 2 ** 2 = 4, 2 ** 3 = 8
    power_of_2 = [2 ** i for i in range(10)]
    print(power_of_2)

    power_of_2 = [(i, 2 ** i) for i in range(10)]
    print(power_of_2)

    lista = [0, 1, 2]
    lista2 = [3, 4, 5]

    lista_list = [lista, lista2]
    print(lista_list)
    pierwszy_element_pierwszej_listy = lista_list[0][0]
    print(pierwszy_element_pierwszej_listy)

    lista_zagniezdzone = [[[1], [2]]]

    poszukiwani = ["Michael Scofield", "Lincoln Burrows", "TheodoreBagwell", "Uczciwy polityk", "Andrzej Klusiewicz"]
    if ("Andrzej Klusiewicz" in poszukiwani):
        print("pszypau")
    else:
        print("nie pszypau")


    random_list_comp_2 = [random.randint(1, 10) for i in range(10)]
    print(f'Przed sortowaniem: {random_list_comp_2}')
    random_list_comp_2.sort()
    print(f'Po sortowaniu: {random_list_comp_2}')
    random_list_comp_2.reverse()
    print(f'Odwrotnie: {random_list_comp_2}')

    random_list_comp_3 = [random.randint(1, 10) for i in range(10)]
    posortowane = sorted(random_list_comp_3)
    odwrotnie = sorted(random_list_comp_3, reverse=True)
    print(posortowane)
    print(odwrotnie)

    filtorwane = [e for e in posortowane if e % 2 == 0]
    print(filtorwane)

    for root, dirs, files in os.walk(r'E:\PythonKurs_18_03_2024'):
        print(f"{root}, {dirs}, {files}")

    napis = "Litery RoZnej WIelKOSCI"
    print(napis.lower())

    # os.path.join()

    # Napisz wyszukiwarkę plików która
    # przyjmie od użytkownika szukaną frazę i katalog startowy. Wyszukiwarka ma wyswietlić
    # wszystkie pliki i katalogi zawierajace w nazwie szukaną frazę - wraz ze ścieżkami.
    # Wyszukiwarka ma być nieczuła na wielkość liter

    folder_startowy = "."
    szukna_fraze = ".txt"