from timeit import default_timer as timer



class Osoba:
    # imie = 'Andrzej'
    # nazwisko = 'Klusiewicz'
    # wiek = 33
    pustePole = None

    def __init__(self, imie :str, nazwisko :str, wiek :int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def wypiszMnie(self):
        print("Cześć jestem:")
        print(self.imie, self.nazwisko, self.wiek)


    def __str__(self):
        return f'Cześć jestem: {self.imie}, {self.nazwisko}, {self.wiek}'

    def przywitaj_kolege(self, imie):
        print(f"Cześć {imie} jestem: {self.imie}")



o = Osoba("Jan", "Kowalski", wiek=32)
print(o.imie, o.nazwisko, o.wiek, o.pustePole)

# o.wypiszMnie()
o.dodatkowa_zmienna = 42 # tak nie robimy
o.przywitaj_kolege("Miłosza")

o.imie ='Krzysztof'
o.nazwisko ='Jarzyna'
print(o.imie ,o.nazwisko)

o2 = Osoba("Krzysztof", "P.", 50)
lista_osob = [o, o2]

for osoba in lista_osob:
    osoba.wypiszMnie()

print(o)

print("*" * 45)

#     Stwórz klasę "Samochod" posiadającą pola "marka", "model", "rejestracja".
#     Klasa ta powinna zawierać też metodę "wyswietl" wypisującą dane z obiektu na konsoli
#     Stwórz dwa obiekty tej klasy i korzystajac  z metody "wyświetl" wyswietl na konsoli ich zawartość.
class Samochod:
    def __init__(self, marka: str, model: str, rejstracja: str="DOMYSLNA WARTOSC"):
        self.__marka = marka
        self.model = model
        self.rejestracja = rejstracja


    def __str__(self):
        return f'Moj piekny samochodzik: {self.__marka}, {self.model}, {self.rejestracja}'

    def __repr__(self):
        return f'Samochod({self.__marka}, {self.model}, {self.rejestracja})'

    def wyswietl(self):
        print(f'{self.__marka}, {self.model}, {self.rejestracja}')

    def _funckja_dla_mechanika(self):
        print("Naprawiam")


s1 = Samochod("Opel", "Vectra", "SJZ 11111")
s2 = Samochod("Opel", "Astra")

#print(s1.__marka) ## tak się nie da __marka jest ukryta w innej przestrzen nazw
s1._funckja_dla_mechanika() # tu się da ale IDE nam nie pomoze

s1.wyswietl()
print(s1)
print(s2)


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        doc="The radius property."
    )


kolo = Circle(20)
#kolo.set_radius(30)
print(kolo.radius)

try:
    kolo.radius = 30
except Exception as err:
    print(err)



class Rectangle:
    def __init__(self, a:int, b:int):
        self._a = a
        self.b = b

    @property
    def a(self):
        print("Get a")
        return self._a

    @a.setter
    def a(self, value):
        print("Set a")
        self._a = value


r = Rectangle(4,2)
r.b = 8
r.a = 30
print(f'Rectangle {r.a}, {r.b}')


# Stwórz klasę Zawodnik posiadającą pola wzrost i masa, imie. Pola te mają być uzupełniane przy tworzeniu obiektu.
# stworz atrybut BMI który będzie tylko do odczytu
# Powołaj do życia obiekt tej klasy i wyświetl na konsoli obliczone BMI.
# Wzrost jest atrybutem chronionym (__wzrost)
# Waga może być zmieniana ale też jako atrybut z wykorzystaniem dekoratora @property
# wzor na bmi = masa / (wzrost ** 2)   wzrost podany w metrach 1.84
class Zawodnik:

    def __init__(self, wzrost: float, masa: float, imie: str, auto: Samochod = Samochod("Opel", "Vectra", "SJZ 11111")):
        self.__wzrost = wzrost
        self._masa = masa
        self._imie = imie
        self.auto = auto

    @property
    def BMI(self):
        return self._masa / (self.__wzrost ** 2)

    @property
    def waga(self):
        return self._masa

    @waga.setter
    def waga(self, value: float):
        self._masa = value


    # "180;180;Jan"
    @classmethod
    def create_from_string(cls, text: str):
        dane = text.strip().split(';')
        if len(dane) == 3:
            wzorst_cm, waga_lbs, imie = dane
            z = cls(wzrost=int(wzorst_cm) / 100, masa=int(waga_lbs) * 0.454, imie=imie)
            return z

    @staticmethod
    def nie_uzywam_atrybutow(info:str):
        print(info)

    # odczytali dane z pliku dane.txt
    # zbudowali sobie liste zawodnikow (jako obietky klasy) przy uzyciu  @classmethod
    @classmethod
    def create_from_file(cls, path_to_file: str):
        zawodnicy = []
        with open("dane.txt", "r") as plik:
            for linia in plik:
                dane = linia.strip().split(";")
                if len(dane) == 3:
                    imie, waga, wzrost = dane
                    zawodnicy.append(cls(masa=float(waga), wzrost=float(wzrost), imie=imie))
        return zawodnicy


    ## napisz funkcje __lt__ umożliwojącą sortowanie zawodników po BMI
    # uruchom tą funkcję z danymi wczytanymi z pliku i wypisz na konsoli imie zawodnika i jego BMI (użyj metody __str__)



zawodnicy_lista = Zawodnik.create_from_file("dane.txt")

nowy_zawodnik_z_napisu = Zawodnik.create_from_string("180;180;Jan")
nowy_zawodnik_z_napisu.nie_uzywam_atrybutow("Przykładowy tekst")

z1 = Zawodnik(1.80, 75, "Adam", Samochod("Opel", "Astra", "SJZ 22222"))
# print(z1)
z2 = Zawodnik(1.85, 80, "Adam")
# print(z2)

print(f"BMI: {z2.BMI:.2f}")

z2.waga = 75
print(f"Schudłem:")
print(f"BMI: {z2.BMI:.2f}")



###### Magic method page ---> https://realpython.com/python-magic-methods/