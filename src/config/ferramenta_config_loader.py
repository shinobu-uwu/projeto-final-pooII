import os
import json
import pygame
from pygame.transform import scale, flip
from src.config.config_loader import ConfigLoader

class FerramentaConfigLoader(ConfigLoader):
    def __init__(self):
        super().__init__()
        self.__tamanho_original = [30,30]

        @property
        def diretorio_sprites(self):
            return os.path.join(self.diretorio_assets, "sprites/ferramentas")

        def recortar_sprites(self, ferramenta):
            #TODO