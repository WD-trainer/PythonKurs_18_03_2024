import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools


def znajdz_pliki_i_katalogi(katalog_startowy, fraza):
    """
    Ta funckja zajmuje sie znajdowaniem katalowgo i plikow. Ignoruje wielkosci liter
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