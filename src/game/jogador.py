import pygame
from pygame.locals import *

from src.config.jogador_config_loader import JogadorConfigLoader
from src.exceptions.tipo_nao_compativel_exception import TipoNaoCompativelException
from src.game.inventario import Inventario
from src.game.interfaces.interface_jogador import IJogador
from src.game.item import Item


class Jogador(IJogador):
    def __init__(self, velocidade: float, posicao_inicial: list):
        self.__config = JogadorConfigLoader
        self.__morto = False
        self.__inventario = Inventario()
        self.__velocidade = velocidade
        self.__item_equipado = 0
        self.__posicao = posicao_inicial

    def mover(self, tecla):
        if tecla == pygame.K_RIGHT:
            self.__posicao[0] += self.__velocidade
        elif tecla == pygame.K_LEFT:
            if self.__posicao[0] - self.__velocidade >= 0:
                self.__posicao[0] -= self.__velocidade
            else:
                self.__posicao[0] = 0
        elif tecla == pygame.K_SPACE:
            self.pular()
        elif tecla == pygame.K_e:
            try:
                self.usar()
            except AttributeError:
                print("Sem Item")
        elif tecla == ord('q'):
            self.adicionar_item(Picareta(2, 3))

    def pular(self):
        #TODO
        self.__posicao[1] = 3

    def usar(self):
        self.__inventario.itens[self.__item_equipado].usar()
        print("usou!")

    def mudar_item(self, tecla):
        self.__item_equipado = tecla

    def adicionar_item(self, item: Item):
        if isinstance(item, Item):
            try:
                i = self.__inventario.itens.index(None)
                self.__inventario.itens[i] = item
            except ValueError:
                print("Inventário cheio")
        else:
            raise TipoNaoCompativelException

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
