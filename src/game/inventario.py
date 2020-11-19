from src.game.interfaces.interface_inventario import IInventario


class Inventario(IInventario):
    def __init__(self):
        self.__itens = []
        self.__capacidade = 10 #Temporário

    @property
    def itens(self):
        return self.__itens

    @property
    def capacidade(self):
        return self.__capacidade

    @itens.setter
    def itens(self, itens):
        self.__itens = itens
