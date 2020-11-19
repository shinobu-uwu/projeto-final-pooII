from abc import ABC, abstractmethod
class Icenario(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def fundo(self):
        pass
    
    @property
    @abstractmethod
    def mapa(self):
        pass
    
    @property
    @abstractmethod
    def final(self):
        pass

