import os
import json
import pygame

from src.config.config_loader import ConfigLoader


class JogadorConfigLoader(ConfigLoader):
    def __init__(self):
        self.__path = f"{os.path.abspath(os.path.dirname(__file__))}/jsons/jogador.json"
        self.load()
        self.__tam = [78,58]

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def diretorio_sprites(self):
        #codigo do path do bings - meu pythonpath tem 2 variáveis
        #return "C:/Users/Arthur/Projects/projeto-final-pooII/assets/sprites/"
        return f"{os.getenv('PYTHONPATH')}assets/sprites/"


    def recortar_sprites(self):
        dir_sprites = self.diretorio_sprites

        #path para as imagens dos sprites
        PspritesLeft = f"{dir_sprites}runLeft.png"
        PspritesRight = f"{dir_sprites}runRight.png"
        Pspritesidle = f"{dir_sprites}idle.png"

        print("\n")
        print(PspritesLeft)

        #carregos as imagens com o pygame
        spritesLeft = pygame.image.load(PspritesLeft)
        spritesRight = pygame.image.load(PspritesRight)
        spritesIdle = pygame.image.load(Pspritesidle)

        #listas onde armazeno os sprites de cada movimento
        leftS = ['']*8
        rightS = ['']*8
        idleS = ['']*11

        #dois for's que recortam e populam as listas de sprites
        for i in range(8):
            leftS[i] = spritesLeft.subsurface(pygame.Rect(self.__tam[0]*i, 0, self.__tam[0], self.__tam[1]))
            rightS[i] = spritesRight.subsurface(pygame.Rect(self.__tam[0]*i, 0, self.__tam[0], self.__tam[1]))

        for a in range(11):
            idleS[a] = spritesIdle.subsurface(pygame.Rect(self.__tam[0]*a, 0, self.__tam[0], self.__tam[1]))

        #Retorno uma lista composta contendo todos os sprites utilizados
        dicSprites = {"left": leftS, "right": rightS, "idle": idleS}
        return dicSprites
