from abc import ABC, abstractmethod


class IItem(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def usar(self):
        pass

    @abstractmethod
    @property
    def material(self):
        pass
