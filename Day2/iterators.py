
from objects import Zawodnik

from collections.abc import Iterator

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
class ListaZawodnikow(Iterator):
    def __init__(self, path:str):
        self.zawodnicy = []
        with open(path, "r") as plik:
            for linia in plik:
                dane = linia.strip().split(";")
                if len(dane) == 3:
                    imie, waga, wzrost = dane
                    self.zawodnicy.append(Zawodnik(masa=float(waga), wzrost=float(wzrost), imie=imie))
        self.index = 0


    def __next__(self):
        if self.index == len(self.zawodnicy):
            raise StopIteration
        self.index += 1
        return self.zawodnicy[self.index - 1]


nasza_lista = ListaZawodnikow("dane.txt")
zawodnik = next(nasza_lista)

for z in nasza_lista:
    print(z)



class MiesiaceIterator:
    def __init__(self):
        self.miesiace = [
            "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
            "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"
        ]
        self.indeks = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks < len(self.miesiace):
            miesiac = self.miesiace[self.indeks]
            self.indeks += 1
            return miesiac
        else:
            raise StopIteration

    def restart(self):
        self.indeks = 0


# Użycie iteratora
miesiace_iterator = MiesiaceIterator()

print("Miesiące:")
for i in range(12):
    print(next(miesiace_iterator))