import random
import requests   # pip install requests

def sumuj(a:float,b:float) ->float:
    return a+b

def dajCyfry() -> list[int]:
    return list(range(1,11))




def fetch_data():
    response = requests.get("https://example.com/api/data")
    return response.text