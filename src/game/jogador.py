from src.game.inventario import Inventario
from src.game.interfaces.interface_jogador import IJogador
from src.game.item import Item


class Jogador(IJogador):
    def __init__(self, velocidade: float, posicao_inicial: list):
        self.__morto = False
        self.__inventario = Inventario()
        self.__velocidade = velocidade
        self.__item_equipado = 0
        self.__posicao = posicao_inicial

    def mover(self, tecla):
        pass

    def pular(self):
        pass

    def usar(self):
        pass

    def mudar_item(self, tecla):
        self.__item_equipado = tecla

    def adicionar_item(self, item: Item):
        if isinstance(item, Item):
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
