from abc import ABC, abstractmethod
class IJogo (ABC):

    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    @property
    def tempo (self):
        pass

    @abstractmethod
    @property
    def camera (self):
        pass

    @abstractmethod
    @property
    def jogador (self):
        pass

    @abstractmethod
    @property
    def cenario (self):
        pass

    @abstractmethod
    @property
    def vitoria (self):
        pass