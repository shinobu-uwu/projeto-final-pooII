from abc import ABC, abstractmethod
from interfaces.interface_item import IItem


class Item(IItem):
    def __init__(self, material):
        self.__material = material

    @abstractmethod
    def usar(self):
        pass

    @property
    def material(self):
        return self.__material
