import os
import fire   # pip install fire  # https://github.com/google/python-fire/blob/master/docs/guide.md

def znajdz_pliki_i_katalogi(katalog_startowy, fraza):
    """
    Ta funckja zajmuje sie znajdowaniem katalowgo i plikow. Ignoruje wielkosci liter
    Parameters
    ----------
    katalog_startowy - katalog od ktorego zaczniemy przeszukiwanie
    fraza - fraza ktora jest wyszukiwana w nazwach plikow i katalogow

    Returns
    -------

    """
    znalezione_elementy = []

    fraza = fraza.lower()

    for root, dirs, files in os.walk(katalog_startowy):
        for element in dirs + files:
            if fraza in element.lower():
                znalezione_elementy.append(os.path.join(root, element))

    print(znalezione_elementy)


if __name__ == "__main__":
    fire.Fire(znajdz_pliki_i_katalogi)