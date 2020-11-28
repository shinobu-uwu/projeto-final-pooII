import os
import pygame

from src.game.interfaces.interface_bloco_cenario import IBlococenario
from src.config.bloco_config_loader import BlocoConfigLoader


class BlocoCenario(IBlococenario):
    def __init__(self, material:int,dano:float,posicao:list):
        self.__config = BlocoConfigLoader()
        self.__material = material
        self.__dano = dano
        self.__posicao = posicao

        self.__sprite = pygame.image.load(os.path.join(self.__config.diretorio_assets, "sprites/box.png"))
        self.__sprite = pygame.transform.scale(self.__sprite, (44, 32))
        self.__tamanho_hitbox = (44, 32)
        self.__hitbox = (self.__posicao[0], self.__posicao[1], self.__tamanho_hitbox[0], self.__tamanho_hitbox[1])

    def quebrar(self):
        pass

    @property
    def material(self):
        return self.__material

    @property
    def dano(self):
        return self.__dano

    @property
    def posicao(self):
        return self.__posicao

    @property
    def sprite(self):
        return self.__sprite

    @property
    def tamanho_hitbox(self):
        return self.__tamanho_hitbox

    @property
    def hitbox(self):
        return self.__hitbox
