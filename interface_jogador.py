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
