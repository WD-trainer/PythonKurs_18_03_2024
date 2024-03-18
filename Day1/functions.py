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




    config("plik.csv", wersja=1, arg=2, argument321=3)
    config("plik.csv", arg_inny=2, argument321=10, wersja=2.0)

















    def zewnetrzna(x):
        def wewnetrzna(x):
            return x * 2
        print(wewnetrzna(x))
        return 1
