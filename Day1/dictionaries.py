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

    nazwa_pliku = ''

    with open(nazwa_pliku, "r", encoding='utf-8') as plik:
        for linia in plik:
            linia_wyczyszczona = re.sub(r'\W+', ' ', linia) 