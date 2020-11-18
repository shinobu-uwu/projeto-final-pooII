from abc import ABC, abstractmethod
from game.ferramenta import Ferramenta

class Machado(ABC,Ferramenta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def usar(self):
        pass
