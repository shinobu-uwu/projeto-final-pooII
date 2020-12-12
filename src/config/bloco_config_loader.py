import os
import json
import pygame
from src.config.config_loader import ConfigLoader


class BlocoConfigLoader(ConfigLoader):
    def __init__(self):
        self.__path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "jsons/blocos.json")
        self.load()

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

    def obter_sprites(self, material):

        """ terra = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{material}/terra2.png")), tuple(self.tamanho))
        sprite_dmg1 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"2/blockdmg1.png")), tuple(self.tamanho))
        sprite_dmg2 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"2/blockdmg2.png")), tuple(self.tamanho))
        sprite_dmg3 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"2/blockdmg3.png")), tuple(self.tamanho))

        return {"base":terra,"dmg1":sprite_dmg1,"dmg2":sprite_dmg2,"dmg3":sprite_dmg3} """

        sprite_base = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{material}/block.png")), tuple(self.tamanho))
        sprite_dmg1 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{material}/blockdmg1.png")), tuple(self.tamanho))
        sprite_dmg2 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{material}/blockdmg2.png")), tuple(self.tamanho))
        sprite_dmg3 = pygame.transform.scale(pygame.image.load(os.path.join(self.diretorio_sprites, f"{material}/blockdmg3.png")), tuple(self.tamanho))
        #sprite_dmg1 = pygame.image.load(os.path.join(self.diretorio_sprites, "blockdmg1_",str(material),".png"))
        #sprite_dmg2 = pygame.image.load(os.path.join(self.diretorio_sprites, "blockdmg2_",str(material),".png"))
        #sprite_dmg3 = pygame.image.load(os.path.join(self.diretorio_sprites, "blockdmg3_",str(material),".png"))

        return {"base":sprite_base,"dmg1":sprite_dmg1,"dmg2":sprite_dmg2,"dmg3":sprite_dmg3}

    def obter_sprite_original(self, material):
        return pygame.image.load(os.path.join(self.diretorio_sprites, f"{material}/block.png"))

    def obter_dados(self, material, dado):
        #PASTA PARA JSONS COM OS BLOCOS
        #if material == 2:
          #  if dado == "dano":
           #     return 2
            #elif dado == "vida":
            #    return 18
       # elif material == 1:
        #    if dado == "dano":
         #       return 0
          #  elif dado == "vida":
           #     return 1
       # elif material == 3:
        #    if dado == "dano":
         #       return 0.5
          #  elif dado == "vida":
           #     return 18
    #    elif material == 4:
     #       if dado == "dano":
      #          return 0.2
       #     elif dado == "vida":
        #        return 15
        if dado =="dano":
            return self.__config["dano"][material]
        elif dado=="vida":
            return self.__config["vida"][material]
         
