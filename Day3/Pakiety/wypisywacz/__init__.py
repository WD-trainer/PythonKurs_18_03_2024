
print("Wywolano __init__.py z pakietu wypisywacz")


import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from .pisacz import hello_world

__author__ = "Wojciech"

__all__ = ["hello_world"]