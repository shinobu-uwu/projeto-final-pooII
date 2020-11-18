from abc import ABC, abstractmethod
from game.ferramenta import Ferramenta

class Pa(ABC,Ferramenta):

    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def usar(self):
        pass
