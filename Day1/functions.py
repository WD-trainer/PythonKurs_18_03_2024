import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools


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

    def moja_suma(*liczby):
        suma = 0
        for i in liczby:
            suma += i
        return suma


    suma = moja_suma(1,2,3,4,5,15,18,50)
    print(suma)

    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7, 8, 9]


    def my_sum(a, b, c):
        print(a + b + c)

    print(my_sum(*list1))    # my_sum(1,2,3)
    print(moja_suma(*list1, *list2, *list3))


    def wiele_argumentów(*args):
        ile_ich = len(args)
        print(ile_ich)
        for element in args:
            print(element, type(element))


    wiele_argumentów([1], "abc", 1.0, 123, "Moj super kurs pythona")


    def pomnoz_razy_dwa(x):
        return x * 2

    def podziel_przez_trzy(x):
        return x / 3

    def dodaj_piec(x):
        return x + 5

    funkcje = [pomnoz_razy_dwa, podziel_przez_trzy, dodaj_piec]

    def aplikuj(wartosc: int, *funckje) -> float:
        for f in funckje:
            wartosc = f(wartosc)
        return wartosc

    print(aplikuj(1, *funkcje))


    def czytaj_pdf(plik):
        print("czytam pdf")


    def czytaj_xml(plik):
        print("czytam xml")


    dekodawnie_plikow = {
        ".pdf": czytaj_pdf,
        ".xml": czytaj_xml
    }
    wspierane = list(dekodawnie_plikow.keys())

    for plik in os.listdir("."):
        rozszerzenie = os.path.splitext(plik)[1]
        if rozszerzenie in wspierane:
            dekodawnie_plikow[rozszerzenie](plik)


    def parametr_kwargs(**kwargs):
        for k in kwargs:
            print(k, kwargs[k])


    parametr_kwargs(dodatkowy=48, nastepny=111)


    def zapisz_parametry_do_pliku(nazwa_pliku, **parametry):
        plik = open(nazwa_pliku, mode='w', encoding='utf-8')
        for p in parametry:
            plik.write(f'{p};{parametry[p]}\n')
        plik.close()


    zapisz_parametry_do_pliku('mojplik.csv', parametr1='wartość 1', parametr2=2,
                              moj_argument="Jestesmy zmeczeni bardzo")


    # Stworz funkcje "config" ktora bedzie otrzymywala argumenty kwargs bedace ustawieniami.
    # Funkcja ta ma zapisac podane argumenty do pliku config.csv w 2 kolumnach z czego pierwsza jest nazwa
    # argumentu a druga jego wartoscia. Jesli dane argument juz istnieje w pliku to trzeba bedzie tylko zaktualizowac
    # jego wartosc, jesli jeszcze go nie ma to trzeba go bedzie dodac do pliku.

    def config(nazwa_pliku, **parametry):
        wczytany_config = {}
        with open(nazwa_pliku, mode='r', encoding='utf-8') as plik:
            for linia in plik:
                if linia.isspace():
                    continue
                klucz, wartosc = linia.split(';')
                wczytany_config[klucz] = wartosc

        for p in parametry:
            wczytany_config[p] = parametry[p]

        plik = open(nazwa_pliku, mode='w', encoding='utf-8')
        for p in wczytany_config:
            plik.write(f'{p};{wczytany_config[p]}\n')
        plik.close()


    config("plik.csv", wersja=1, arg=2, argument321=3)
    config("plik.csv", arg_inny=2, argument321=10, wersja=2.0)




    # funckja w funkcji

    def zewnetrzna(x):
        def wewnetrzna(x):
            return x * 2

        print(wewnetrzna(x))
        return 1

    zewnetrzna(x=5)


    # funkcja zwracajaca funkcje
    def outer(x):
        def inner(y):
            return x + y

        return inner

    dodaj_dwa = outer(2)
    wynik = dodaj_dwa(4)
    print(wynik)




    # Napisz funkcje która będzie tworzyła listę liczb parzystych lub nieparzystych w danym zakresie
    # funkcje do sprawdzenia parzystosci napisz jako funckje wewnętrzne i w zależności
    # od przekazanego parametru wywołuj odpowiednią

    def generuj_liczby(start: int, koniec: int, parzyste: bool = True) -> list[int]:
        def parzysta(x: int) -> bool:
            return x % 2 == 0

        def nieparzysta(x: int) -> bool:
            return x % 2 == 1

        list_liczba = []
        for i in range(start, koniec):
            if parzyste and parzysta(i):
                list_liczba.append(i)
            elif not parzyste and nieparzysta(i):
                list_liczba.append(i)

        return list_liczba


    print(generuj_liczby(0, 20, parzyste=False))

    print(generuj_liczby(parzyste=True, koniec=100, start=10))

    print(generuj_liczby(10, parzyste=True, koniec=100))
    print(generuj_liczby(10, 100, True))

    # print(generuj_liczby( parzyste=True, 10, 100))












    # @functools.lru_cache(maxsize=None)
    # def czekacz():
    #     time.sleep(1)
    #     return 1
    #
    # poczatek = datetime.now()
    # for x in range(10):
    #     czekacz()
    # koniec = datetime.now()
    # print(koniec - poczatek)


    @functools.lru_cache()
    def fibonacci(num):
        print(f"Calculating fibonacci({num})")
        if num < 2:
            return num
        return fibonacci(num - 1) + fibonacci(num - 2)


    poczatek = datetime.now()
    fibonacci(10)
    koniec = datetime.now()
    print(f'Fibonnaci time: {koniec - poczatek}')









    # Using a Python dictionary to act as an adjacency list
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }

    visited = set()  # Set to keep track of visited nodes of graph.

    def dfs(visited, graph, node):  # function for dfs
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)
