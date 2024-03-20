
from . import logger

def hello_world():
    """
    Moja pierwsza funkcja w pakiecie
    Returns
    -------

    """
    logger.info("Tutaj loguje sobie cos na konsole")
    print("Hello world")

def funckja_prywatna():
    print("Jestem funkcja prywatna")