from timeit import default_timer as timer
import time



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
except Exceptionas err:
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


    def __str__(self):
        return f"{self._imie}: BMI = {self.BMI:.2f}"

    ## napisz funkcje __lt__ umożliwojącą sortowanie zawodników po BMI
    # uruchom tą funkcję z danymi wczytanymi z pliku i wypisz na konsoli imie zawodnika i jego BMI (użyj metody __str__)
    def __lt__(self, other):
        return self.BMI < other.BMI


zawodnicy_lista = Zawodnik.create_from_file("dane.txt")
# zawodnicy_lista.append("napis")
zawodnicy_lista.sort()
for z in zawodnicy_lista:
    print(z)


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



##### Context menager ---> # https://realpython.com/python-with-statement/

# Napisz klase Timer która będzie mierzyła czas wykonania funkcji jako context menager.
# klasa ta w zaleznosci od zmiennej verbose bedzie wypisywała na ekran czas wykonania przy wyjsciu z contextu
# from timeit import default_timer as timer
class Timer(object):
    def __init__(self, verbose=False):
        self.timer = timer
        self.elapsed = 0
        self.verbose = verbose

    def __enter__(self):
        self.start = self.timer()
        return self

    def __exit__(self, *args):
        end = self.timer()
        self.elapsed_secs = end - self.start
        self.elapsed = self.elapsed_secs * 1000  # milliseconds
        if self.verbose:
            print('elapsed time: %f ms' % self.elapsed)



with Timer(verbose=True) as t:
    # time.sleep(3)
    print("Moja bardzo długa funkcja")


print(f'Ta funkcja trwała {t.elapsed}')



#################################################### CWICZENIE DODATKOWE

# Stwórz klasę Ustawienia która będzie w momencie tworzenia obiektu czytac plik ustawienia.csv o treści:
# encoding;utf-8
# language;pl
# timezone;-2
# Dane te mają zostać wczytane do wewnętrznego słownika tak, by pierwsza kolumna stanowila klucze a druga wartosci.
# Obiekt ma umożliwiać sprawdzanie ustawień w ten sposób:
# u=Ustawienia()
# print( u['encoding'] )
# Obiekt ma umożliwiać też ustawienie wartości na zasadzie u[‘nazwa’]=’wartosc’.
# W przypadku zmiany powinna ona dotyczyć również zawartości pliku.

#################################################### CWICZENIE DODATKOWE







#################################################### Dziedziczenie

class Animal(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

    def eat(self):
        print("eating")

    def __str__(self):
        return f'My name is {self.name}'

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")


animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

animal.speak()
dog.speak()
cat.speak()
cat.eat()

lista_zwierzat = [cat, dog]

for zwierze in lista_zwierzat:
    # zwierze.speak()
    # zwierze.eat()
    print(zwierze)


from abc import ABC, abstractmethod

class Rysuje(ABC):
    @abstractmethod
    def narysuje_mnie(self):
        pass


class Figura(ABC):
    def __init__(self, nazwa):
        self.nazwa = nazwa
    def pokaz_nazwe(self):
        print(self.nazwa)

    @abstractmethod
    def oblicz_pole(self):
        pass


class Kwadrat(Figura, Rysuje):
    def __init__(self, dlugosc_boku: int):
        super().__init__('Kwadrat')
        self.dlugosc_boku=dlugosc_boku

    def oblicz_pole(self):
        return pow(self.dlugosc_boku, 2)

    def narysuje_mnie(self):
        print("**")
        print("**")



# Stwórz klasę abstrakcyjną Restauracja która będzie posiadała abstrakcyjną metodę "serwuj_danie".
# Stwórz klasy "RestauracjaChinska", "RestauracjaWloska" i "RestaruracjaPolska".
# Wymuś posiadanie implementacji metody abstrakcyjnej "serwuj_danie" we wszystkich
# tych klasach ale o różnej implementacji. Powołaj do życia obiekty tych klas,
# a następnie na rzecz każdego z tych obiektów wywołaj funkcję serwuj_danie.

