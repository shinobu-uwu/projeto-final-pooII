from abc import ABC, abstractmethod
from src.game.ferramenta import ferramenta 

class Picareta(Ferramenta, ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def usar(self):
        pass
