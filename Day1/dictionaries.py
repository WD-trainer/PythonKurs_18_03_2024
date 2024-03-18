import operator
import random
import os
import re
from collections import defaultdict


if __name__ == '__main__':

    slownik = {}
    slownik2 = dict()

    info = {
        "LG123" : "Telewizor 60' z HD Ready, wejściem na internety ifiltrem reklam",
        "SONY666" : "Piekielnie dobry telewizor",
        "SZAJSUNG999" : "Telewizor świetnie nadający się do zakrycia dziury w ścianie(i niczego więcej)"
    }

    print(info)
    print(info["LG123"])
    print(info.keys())
    print(info.values())

    for i in info:
        print(f'i = {i}')
        print(f'info[i] = {info[i]}')

    for key in info.keys():
        print(info[key])

    if "LG123" in info:
        print("Mamy LG")
    else:
        print("niet :(")

    info["KLUCZ"] = "WARTOŚĆ"

    for i in info:
        print(f'i = {i}')
        print(f'info[i] = {info[i]}')


    osoby = {}

    with open("dane.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip().split(';')
            osoby[linia[0]] = (linia[1], linia[2])

            # print(linia)
    for key, value in osoby.items():
        print(f'Klucz: {key}, wartosc: {value}')


    # wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a
    # druga przypisane do nich wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości

    # plik = open("ustawienia.txt", "r")
    # #tutaj czytanie pliku
    # plik.close()

    ustawienia = {}

    with open("ustawienia.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip().split(';')
            if len(linia) == 2:
                klucz, wartosc = linia
                ustawienia[klucz] = wartosc


    for key, value in ustawienia.items():
        print(f'Klucz: {key}, wartosc: {value}')

    # lista = [1,2,3]
    # pierwszy_element, *reszta = lista
    # print(f"{pierwszy_element}, Reszta tutaj: {reszta}")







    # Napisz program który zwróci nam liczbe wystąpień każdego ze słow w pliku
    # Nazwa pliku ma zostać przekazana przez  zmienną.
    # Wynik powinien byc posortowany malejąco wg ilosci wystapien
    # a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj jako elemnt listy.
    # Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników
    # etc.

    # b) stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego
    # słowa
    # w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i
    # wartości 1
    # dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba
    # zwiększyc wartośc o 1

    # c) Przepakuj dane ze słownika do listy i posortuj.

    nazwa_pliku = 'text.txt'

    wystapienia = {}
    # Defining the dict
    wystapienia2 = defaultdict(int)  # from collections import defaultdict

    with open(nazwa_pliku, "r", encoding='utf-8') as plik:
        for linia in plik:
            linia_wyczyszczona = re.sub(r'\W+', ' ', linia)
            slowa = linia_wyczyszczona.lower().split()
            for slowo in slowa:
                if slowo in wystapienia:  # https://www.geeksforgeeks.org/defaultdict-in-python/
                    wystapienia[slowo] += 1
                else:
                    wystapienia[slowo] = 1

                wystapienia2[slowo] += 1

    print(wystapienia)

    posortowane_wystapienia = sorted(wystapienia.items(), key=lambda x: x[1], reverse=True)
    posortowane_wystapienia2 = sorted(wystapienia.items(), key=operator.itemgetter(1), reverse=True)

    print(posortowane_wystapienia)


    ##########################  Lambda

    # lambda argumenty : wyrażenie

    p = lambda argumenty: print(argumenty)
    p("moj napis")

    liczby = [1,2,3,4,5]
    powers = list(map(lambda x: x**2, liczby))
    p(powers)

    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    even_numbers2 = [e for e in numbers if e % 2 == 0]
    print(even_numbers2)

    employees = [{"name": "John", "salary": 50000}, {"name": "Jane", "salary": 55000}, {"name": "Jim", "salary": 60000}]
    highest_salary_employee = max(employees, key=lambda x: x["salary"])
    print(highest_salary_employee)


    # Tak nie robić !!! to juz za duzo na lambde
    calculate = lambda x, y: x + y if x > y else x - y
    print(calculate(5, 10))

    # lepiej tak
    def calculate(x, y):
        if x > y:
            return x + y
        else:
            return x - y

    ############### Sets - zbiory / zestawy

    list1 = [1, 2, 3, 4, 5, 5]
    list2 = [4, 5, 6, 7, 8]

    # Convert lists into sets
    set1 = set(list1)
    set2 = set(list2)

    print(list1)
    print(set1)

    # Perform set operations
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set1 = set1.difference(set2)
    difference_set2 = set2.difference(set1)
    symmetric_difference_set = set1.symmetric_difference(set2)

    # Display the results
    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Difference of Set 1 - Set 2:", difference_set1)
    print("Difference of Set 2 - Set 1:", difference_set2)
    print("Symmetric Difference:", symmetric_difference_set)





