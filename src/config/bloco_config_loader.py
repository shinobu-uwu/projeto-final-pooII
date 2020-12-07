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
    def tamanho(self):
        return tuple(self.__config["tamanho"])

    @property
    def diretorio_sprites(self):
        return os.path.join(self.diretorio_assets, "sprites/blocos/")

    def obter_sprites(self):
        
        sprite_base = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{self.__material}/block.png")),(44,32))
        sprite_dmg1 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{self.__material}/blockdmg1.png")),(44,32))
        sprite_dmg2 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{self.__material}/blockdmg2.png")),(44,32))
        sprite_dmg3 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{self.__material}/blockdmg3.png")),(44,32))
        #sprite_dmg1 = pygame.image.load(os.path.join(self.diretorio_sprites, "blockdmg1_",str(self.__material),".png"))
        #sprite_dmg2 = pygame.image.load(os.path.join(self.diretorio_sprites, "blockdmg2_",str(self.__material),".png"))
        #sprite_dmg3 = pygame.image.load(os.path.join(self.diretorio_sprites, "blockdmg3_",str(self.__material),".png"))

        return {"base":sprite_base,"dmg1":sprite_dmg1,"dmg2":sprite_dmg2,"dmg3":sprite_dmg3}