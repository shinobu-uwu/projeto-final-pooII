import pygame
from pygame.locals import *

from src.config.jogador_config_loader import JogadorConfigLoader
from src.exceptions.tipo_nao_compativel_exception import TipoNaoCompativelException
from src.game.inventario import Inventario
from src.game.interfaces.interface_jogador import IJogador
from src.game.item import Item


class Jogador(IJogador):
    def __init__(self, velocidade: float, posicao_inicial: list):
        self.__config = JogadorConfigLoader()
        self.__morto = False
        self.__inventario = Inventario()
        self.__velocidade = velocidade
        self.__item_equipado = 0
        self.__posicao = posicao_inicial

        #lista composta para os sprites
        self.__sprites = self.__config.recortar_sprites()

        #bools para determinar qual animação o personagem está realizando
        self.__left = False
        self.__right = False
        #bool para saber a ultima direção que o personagem estava virado - 0 -> esquerda, 1 -> direita
        self.__last_side = 1
        self.__is_jump = False

        #contadores para o pulo e a animação de correr
        self.__walk_count = 0
        self.__jump_count = 0
        self.__idle_count = 0

    def mover(self, tecla):
        if tecla[pygame.K_RIGHT]:
            self.__posicao[0] += self.__velocidade
            self.__right = True
            self.__left = False

        elif tecla[pygame.K_LEFT]:
            if self.__posicao[0] - self.__velocidade >= 0:
                self.__posicao[0] -= self.__velocidade
                self.__left = True
                self.__right = False
            else:
                self.__posicao[0] = 0

        else:
            self.__right = False
            self.__left = False
            self.__walk_count = 0

        if not self.__is_jump:
            if tecla[pygame.K_SPACE]:
                self.__is_jump = True
                self.__walk_count = 0

        else:
            self.pular()
                
        if tecla[pygame.K_e]:
            try:
                self.usar()
            except AttributeError:
                print("Sem Item")

    def pular(self):
        if self.__jump_count >= -10:
            neg = 1
            if self.__jump_count < 0:
                neg = -1

            self.__posicao[1] -= (self.__jump_count**2) * neg
            self.__jump_count -= 1
        else:
            self.__is_jump = False
            self.__jump_count = 10
        #self.__posicao[1] = 3

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

    @morto.setter
    def morto(self, morto):
        self.__morto = morto

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

    @property
    def sprites(self):
        return self.__sprites

    @property
    def walk_count(self):
        return self.__walk_count

    @walk_count.setter
    def walk_count(self, walk_count):
        self.__walk_count = walk_count

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def idle_count(self):
        return self.__idle_count

    @idle_count.setter
    def idle_count(self, idle_count):
        self.__idle_count = idle_count

    @property
    def last_side(self):
        return self.__last_side

    @last_side.setter
    def last_side(self, last_side):
        self.__last_side = last_side