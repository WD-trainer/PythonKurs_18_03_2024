import random
import requests   # pip install requests

def sumuj(a:float,b:float) ->float:
    return a+b

def dajCyfry() -> list[int]:
    return list(range(1,11))

# https://docs.pytest.org/en/8.0.x/
# Napisz funkcje ktora sprawdzi czy podany tekst jest palindromem in napisz testy do niej
# "kajak"
# ""
# "kajak    "
# "to nie jest palindromem"
def is_palindrome(text:str) -> bool:
    """
    Sprawdza, czy dany ciąg znaków jest palindromem.

    Parameters:
        text (str): Ciąg znaków do sprawdzenia.

    Returns:
        bool: True, jeśli ciąg jest palindromem, False w przeciwnym razie.
    """
    text = text.lower().replace(" ", "")
    return text == text[::-1]       # range(start, stop, step)   [start:stop:step]   text[1:3]


def fetch_data():
    response = requests.get("https://example.com/api/data")
    return response.text



# napiszcie testy z parametryzacja (pytest) ktory sprawdzi czy potrafimy wyliczyc srednia
# osobny test dla pustej listy dla None porownanie is
def calculate_average(numbers : list[float]) -> float | None:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)







baza=[]
def loadDB():
    print("############## ŁADOWANIE BAZY ##############")
    global baza
    baza=[
    (1,"Marian"),
    (2,"Czesław"),
    (3,"Zenon"),
    (4,"Florian")
    ]

def getData():
    global baza
    return baza
def getOne(index:int):
    global baza
    return baza[index]