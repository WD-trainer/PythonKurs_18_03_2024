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


