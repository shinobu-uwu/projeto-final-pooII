import os
import json
import pygame
from pygame.transform import smoothscale, scale2x, scale

from src.config.config_loader import ConfigLoader


class JogadorConfigLoader(ConfigLoader):
    def __init__(self):
        self.__path = f"{os.path.abspath(os.path.dirname(__file__))}/jsons/jogador.json"
        self.load()
        self.__tam = [156,116]

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def diretorio_sprites(self):
        #codigo do path do bings - meu pythonpath tem 2 variáveis
        #return "C:/Users/Arthur/Projects/projeto-final-pooII/assets/sprites/"
        return f"{os.getenv('PYTHONPATH')}/assets/sprites/"



    def recortar_sprites(self):
        dir_sprites = self.diretorio_sprites

        #path para as imagens dos sprites
        PspritesLeft = f"{dir_sprites}runLeft.png"
        PspritesRight = f"{dir_sprites}runRight.png"
        Pspritesidle = f"{dir_sprites}idle.png"
        PspritesAttack = f"{dir_sprites}attack.png"
        PspritesFall = f"{dir_sprites}fall.png"
        PspritesJump = f"{dir_sprites}jump.png"

        #carregos as imagens com o pygame
        #spritesLeft = pygame.image.load(PspritesLeft)
        spritesRight = pygame.image.load(PspritesRight)
        spritesIdle = pygame.image.load(Pspritesidle)
        spritesAttack = pygame.image.load(PspritesAttack)
        spritesFall = pygame.image.load(PspritesFall)
        spritesJump = pygame.image.load(PspritesJump)

        spritesRight = scale(spritesRight, (1248,116))
        spritesIdle = scale(spritesIdle, (1716,116))
        spritesAttack = scale(spritesAttack, (468,116))
        spritesFall = scale(spritesFall, (156,116))
        spritesJump = scale(spritesJump, (156, 116))

        #listas onde armazeno os sprites de cada movimento
        
        rightS = ['']*8
        leftS = ['']*8
        idleS = ['']*11
        idleSM = ['']*11
        attackS = ['']*3
        attackSM = ['']*3


        #dois for's que recortam e populam as listas de sprites
        for i in range(8):
            #leftS[i] = spritesLeft.subsurface(pygame.Rect(self.__tam[0]*i, 0, self.__tam[0], self.__tam[1]))
            rightS[i] = spritesRight.subsurface(pygame.Rect(self.__tam[0]*i, 0, self.__tam[0], self.__tam[1]))
            leftS[i] = pygame.transform.flip(rightS[i],1,0)

        for a in range(11):
            idleS[a] = spritesIdle.subsurface(pygame.Rect(self.__tam[0]*a, 0, self.__tam[0], self.__tam[1]))
            idleSM[a] = pygame.transform.flip(idleS[a],1,0)

        for b in range(3):
            attackS[b] = spritesAttack.subsurface(pygame.Rect(self.__tam[0]*b, 0, self.__tam[0], self.__tam[1]))
            attackSM[b] = pygame.transform.flip(attackS[b],1,0)

        fallS = spritesFall.subsurface(pygame.Rect(0, 0, self.__tam[0], self.__tam[1]))
        fallSM = pygame.transform.flip(fallS,1,0)
        jumpS = spritesJump.subsurface(pygame.Rect(0, 0, self.__tam[0], self.__tam[1]))
        jumpSM = pygame.transform.flip(jumpS,1,0)

        #Retorno uma lista composta contendo todos os sprites utilizados
        dicSprites = {"left": leftS, "right": rightS, "idle": idleS, "idleM": idleSM, "attack": attackS, "attackM": attackSM, "fall": fallS, "fallM": fallSM, "jump": jumpS, "jumpM": jumpSM}
        return dicSprites
