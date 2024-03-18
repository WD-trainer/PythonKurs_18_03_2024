import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools


# https://refactoring.guru/pl/design-patterns/what-is-pattern

def do_opakowania():
    print("Opakuj mnie")

def dekorator(funkcja):
    def opakowujaca():
        print("Przed wywołaniem")
        funkcja()
        print("Po wywołaniu")


    return opakowujaca


@dekorator
def do_opakowania_2():
    print("Opakuj mnie")

if __name__ == '__main__':
    dek = dekorator(do_opakowania)
    dek()

    do_opakowania_2()

    # Stwórz funkcję której zadaniem będzie poczekanie 3 sekundy i wypisanie na konsoli komunikatu.
    # Dodaj dekorator który zliczy czas wykonywania tej funkcji. Pobranie aktualnego czasu to: "time.time()",
    # wstrzymanie na 3 sekundy: "time.sleep(3)"
    








    def opakuj_mnie():
        time.sleep(3)
        print("Robie ciekawe rzeczy w Pythonie")
