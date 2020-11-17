from abc import ABC, abstractmethod
from inventario import Inventario

class IJogador(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def pular(self):
        pass

    @abstractmethod
    def usar(self):
        pass

    @abstractmethod
    def mudar_item(self):
        pass

    @abstractmethod
    @property
    def morto(self):
        pass

    @abstractmethod
    @property
    def inventario(self):
        pass

    @abstractmethod
    @property
    def velocidade(self):
        pass

    @abstractmethod
    @property
    def item_equipado(self):
        pass

    @abstractmethod
    @property
    def posicao(self):
        pass

    @abstractmethod
    @morto.setter
    def morto(self, morto):
        pass
