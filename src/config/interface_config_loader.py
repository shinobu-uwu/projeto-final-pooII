from abc import ABC, abstractmethod


class IConfigLoader(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __load(self):
        pass
