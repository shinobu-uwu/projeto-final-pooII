import os
import json
import pygame
from src.config.config_loader import ConfigLoader


class BlocoConfigLoader(ConfigLoader):
    def __init__(self,material:int):
        self.__path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "jsons/blocos.json")
        self.load()
        self.__material= str(material)

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def tamanho_original(self):
        return tuple(self.__config["tamanho"])

    @property
    def tamanho(self):
        return self.__config["tamanho"][0]*2, self.__config["tamanho"][1]*2

    @property
    def diretorio_sprites(self):
        return os.path.join(self.diretorio_assets, "sprites/blocos/")

    def obter_sprites(self):

        print(self.__material)

        if self.__material == '1':
            
            terra = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{self.__material}/terra2.png")), tuple(self.tamanho))
            sprite_dmg1 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"2/blockdmg1.png")), tuple(self.tamanho))
            sprite_dmg2 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"2/blockdmg2.png")), tuple(self.tamanho))
            sprite_dmg3 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"2/blockdmg3.png")), tuple(self.tamanho))

            return {"base":terra,"dmg1":sprite_dmg1,"dmg2":sprite_dmg2,"dmg3":sprite_dmg3}

        elif self.__material == '2':
            sprite_base = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{self.__material}/block.png")), tuple(self.tamanho))
            sprite_dmg1 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{self.__material}/blockdmg1.png")), tuple(self.tamanho))
            sprite_dmg2 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{self.__material}/blockdmg2.png")), tuple(self.tamanho))
            sprite_dmg3 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{self.__material}/blockdmg3.png")), tuple(self.tamanho))
            #sprite_dmg1 = pygame.image.load(os.path.join(self.diretorio_sprites, "blockdmg1_",str(self.__material),".png"))
            #sprite_dmg2 = pygame.image.load(os.path.join(self.diretorio_sprites, "blockdmg2_",str(self.__material),".png"))
            #sprite_dmg3 = pygame.image.load(os.path.join(self.diretorio_sprites, "blockdmg3_",str(self.__material),".png"))

            return {"base":sprite_base,"dmg1":sprite_dmg1,"dmg2":sprite_dmg2,"dmg3":sprite_dmg3}

    def obter_sprite_original(self):
        return pygame.image.load(os.path.join(self.diretorio_sprites, f"{self.__material}/block.png"))
