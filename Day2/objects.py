
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

    #@property
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



