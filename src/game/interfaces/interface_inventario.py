from abc import ABC, abstractmethod


class IInventario(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    @property
    def itens(self):
        pass

    @abstractmethod
    @property
    def capacidade(self):
        pass

    @abstractmethod
    @itens.setter
    def itens(self, itens):
        pass
