import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools


def star(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)

    return inner


@star
def znajdz_pliki_i_katalogi(katalog_startowy:str, fraza:str):
    """
    Ta funckja zajmuje sie czyms waznym i jest bardzo istotna
    Parameters
    ----------
    katalog_startowy
    fraza

    Returns
    -------

    """
    znalezione_elementy = []

    fraza = fraza.lower()

    for root, dirs, files in os.walk(katalog_startowy):
        for element in dirs + files:
            if fraza in element.lower():
                znalezione_elementy.append(os.path.join(root, element))
                time.sleep(0.010)

    print(znalezione_elementy)


help(znajdz_pliki_i_katalogi)
print(znajdz_pliki_i_katalogi.__doc__)

znajdz_pliki_i_katalogi(r"E:\PythonKurs_18_03_2024", ".txt")



def star_with_params(how_many:int):
    def star_inner(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print("*" * how_many)
            func(*args, **kwargs)
            print("*" * how_many)
        return inner
    return star_inner

@star_with_params(how_many=3)
def printer(msg):    #  printer = percent(star(printer))
    print(msg)


printer("Drugi dzien szkolenia, jest ekstra!")


# Napisz dekorator ktory z parametrem sleep_time ktory bedzie wywoływał funkcję sleep przed wykonaniem funkcji dekorowanej
def sleeper(sleep_time: float):
    def sleeper_decorator(func):
        def inner(*args, **kwargs):
            time.sleep(sleep_time)
            returned_value = func(*args, **kwargs)
            return returned_value
        return inner
    return sleeper_decorator



@sleeper(sleep_time=2.5)
def slow_add(a: float, b: float) -> float:
    return a + b

print(f'Wynik dodawania 2+2=')
print(f'{slow_add(2, 2)}')