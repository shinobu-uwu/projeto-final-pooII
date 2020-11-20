from src.game.inventario import Inventario
from src.game.interfaces.interface_jogador import IJogador
from src.game.interface.interface_item import IItem


class Jogador(IJogador):
    def __init__(self):
        self.__morto = False
        self.__inventario = Inventario()
        self.__velocidade = 5#temporário
        self.__item_equipado = 0
        self.__posicao = [0, 10]#temporário

    def mover(self, tecla):
        pass

    def pular(self):
        pass

    def usar(self):
        pass

    def mudar_item(self, tecla):
        pass

    def adicionar_item(self, item):
        if isinstance(item, IItem):
            self.__inventario.itens.append(item)

    @property
    def morto(self):
        return self.__morto

    @property
    def inventario(self):
        return self.__inventario

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def item_equipado(self):
        return self.__item_equipado

    @property
    def posicao(self):
        return self.__posicao

    @morto.setter
    def morto(self, morto):
        self.__morto = morto
