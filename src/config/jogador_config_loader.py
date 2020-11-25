import os
import json

from src.config.config_loader import ConfigLoader


class JogadorConfigLoader(ConfigLoader):
    def __init__(self):
        self.__path = f"{os.path.abspath(os.path.dirname(__file__))}/jsons/jogador.json"
        self.load()

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def diretorio_sprites(self):
        return f"{self.diretorio_sprites}/sprites"
