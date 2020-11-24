from abc import ABC, abstractmethod


class ICamera(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mover(self):
        pass
    
    @property
    @abstractmethod
    def posicao(self):
        pass
    
    @property
    @abstractmethod
    def velocidade(self):
        pass
