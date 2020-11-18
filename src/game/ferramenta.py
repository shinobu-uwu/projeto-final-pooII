from abc import ABC, abstractmethod
from item import Item

class Ferramenta(ABC, Item):
    @abstractmethod
    def __init__(self, forca: float, velocidade_ataque: float):
        self.__forca = forca
        self.__velocidade_ataque = velocidade_ataque

    @abstractmethod
    def usar(self):
        #TODO - Lógica de Implementação do Método Usar
        pass

    @abstractmethod
    @property
    def forca(self):
        return self.__forca

    @abstractmethod
    @forca.setter
    def forca(self, forca):
        self.__forca = forca

        