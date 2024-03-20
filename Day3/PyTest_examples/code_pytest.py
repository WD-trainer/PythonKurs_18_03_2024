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



def fetch_data():
    response = requests.get("https://example.com/api/data")
    return response.text