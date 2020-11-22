from abc import ABC, abstractmethod
from item import Item

class Ferramenta(Item, ABC):
    @abstractmethod
    def __init__(self, forca: float, velocidade_ataque: float):
        self.__forca = forca
        self.__velocidade_ataque = velocidade_ataque

    @abstractmethod
    def usar(self):
        #Cada subclasse irá sobrescrever esse método
        pass

    @property
    def forca(self):
        return self.__forca

    @forca.setter
    def forca(self, forca):
        self.__forca = forca
