import os
import json
import pygame
from pygame.transform import scale, flip

from src.config.config_loader import ConfigLoader


class JogadorConfigLoader(ConfigLoader):
    def __init__(self):
        self.__path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "jsons/jogador.json")
        self.load()
        self.__tamanho_original = [37, 28]

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def tamanho(self):
        return self.__tamanho_original[0] * 2, self.__tamanho_original[1] * 2

    @property
    def diretorio_sprites(self):
        #codigo do path do bings - meu pythonpath tem 2 variáveis
        #return "C:/Users/Arthur/Projects/projeto-final-pooII/assets/sprites/"
        return os.path.join(self.diretorio_assets, "sprites")



    def recortar_sprites(self):
        sprite_idle = pygame.image.load(os.path.join(self.diretorio_sprites, "idle.png"))
        sprite_run_left = pygame.image.load(os.path.join(self.diretorio_sprites, "runLeft.png"))
        sprite_run_right = pygame.image.load(os.path.join(self.diretorio_sprites, "runRight.png"))
        sprite_attack = pygame.image.load(os.path.join(self.diretorio_sprites, "attack.png"))
        sprite_pulo = scale(pygame.image.load(os.path.join(self.diretorio_sprites, "jump.png")), self.tamanho)
        sprite_pulo_invertido = flip(sprite_pulo, 1, 0)
        sprite_queda = scale(pygame.image.load(os.path.join(self.diretorio_sprites, "fall.png")), self.tamanho)
        sprite_queda_invertido = flip(sprite_queda, 1, 0)

        sprites_idle = []
        sprites_idle_invertido = []
        sprites_run_left = []
        sprites_run_right = []
        sprites_attack = []
        sprites_attack_invertido = []

        #sprites_idle.append(sprite_idle.subsurface(pygame.Rect(0, 0, self.__tamanho_original[0], self.__tamanho_original[1])))
        for i in range(11):
            sprites_idle.append(scale(sprite_idle.subsurface(pygame.Rect(78 * i, 0, self.__tamanho_original[0], self.__tamanho_original[1])), self.tamanho))
            sprites_idle_invertido.append(flip(sprites_idle[i], 1, 0))

        for j in range(8):
            sprites_run_left.append(scale(sprite_run_left.subsurface(pygame.Rect(78 * j, 0, self.__tamanho_original[0], self.__tamanho_original[1])), self.tamanho))
            sprites_run_right.append(scale(sprite_run_right.subsurface(pygame.Rect(78 * j, 0, self.__tamanho_original[0], self.__tamanho_original[1])), self.tamanho))


        sprites_attack.append(scale(sprite_attack.subsurface(pygame.Rect(0, 0, 58, 58)), (100, 100)))
        sprites_attack.append(scale(sprite_attack.subsurface(pygame.Rect(76, 0, 58, 58)), (100, 100)))
        sprites_attack.append(scale(sprite_attack.subsurface(pygame.Rect(129, 0, 53, 53)), (100, 100)))

        sprites_attack_invertido.append(flip(sprites_attack[0],1,0))
        sprites_attack_invertido.append(flip(sprites_attack[1],1,0))
        sprites_attack_invertido.append(flip(sprites_attack[2],1,0))

        return {"left": sprites_run_left, "right": sprites_run_right, "idle": sprites_idle, "idleM": sprites_idle_invertido,
                "attack": sprites_attack, "attackM": sprites_attack_invertido, "jump": sprite_pulo, "jumpM": sprite_pulo_invertido,
                "fall": sprite_queda, "fallM": sprite_queda_invertido}
