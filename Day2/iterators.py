
from objects import Zawodnik


class IncrementIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        return self.i


for e in IncrementIterator(10):
    print(e)


# uzupełnic klase lista zwodnikow o metody __iter__ oraz __next__
class ListaZawodnikow:
    def __init__(self, path:str):
        self.zawodnicy = []
        with open(path, "r") as plik:
            for linia in plik:
                dane = linia.strip().split(";")
                if len(dane) == 3:
                    imie, waga, wzrost = dane
                    self.zawodnicy.append(Zawodnik(masa=float(waga), wzrost=float(wzrost), imie=imie))

    def __iter__(self):

    def __next__(self):


nasza_lista = ListaZawodnikow("dane.txt")
zawodnik = next(nasza_lista)

for z in nasza_lista:
    print(z)