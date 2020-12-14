from abc import ABC, abstractmethod
from src.game.item import Item
from src.config.ferramenta_config_loader import FerramentaConfigLoader
import pygame

class Ferramenta(Item, ABC):
    @abstractmethod
    def __init__(self, forca: float, velocidade_ataque: float):
        self.__config = FerramentaConfigLoader()
        self.__forca = forca
        self.__velocidade_ataque = velocidade_ataque
        self.__tipo = "0"

    def get_sprites(self, tipo):
        self.__sprite = self.__config.recortar_sprites(tipo)

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

    @property
    def sprite(self):
        return self.__sprite

    @property
    def tamanho(self):
        return self.__config.tamanho
