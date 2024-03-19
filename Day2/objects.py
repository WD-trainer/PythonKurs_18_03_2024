
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

o.imi e ='Krzysztof'
o.nazwisk o ='Jarzyna'
print(o.imie ,o.nazwisko)

o2 = Osoba("Krzysztof", "P.", 50)
lista_osob = [o, o2]

for osoba in lista_osob:
    osoba.wypiszMnie()

print(o)



#     Stwórz klasę "Samochod" posiadającą pola "marka", "model", "rejestracja".
#     Klasa ta powinna zawierać też metodę "wyswietl" wypisującą dane z obiektu na konsoli
#     Stwórz dwa obiekty tej klasy i korzystajac  z metody "wyświetl" wyswietl na konsoli ich zawartość.
