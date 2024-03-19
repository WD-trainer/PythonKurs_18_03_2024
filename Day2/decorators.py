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

