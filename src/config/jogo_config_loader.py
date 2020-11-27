import os
import json

from src.config.config_loader import ConfigLoader


class JogoConfigLoader(ConfigLoader):
    def __init__(self):
        self.__path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "jsons/jogo.json")
        self.load()

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def width_janela(self):
        return self.__config["tamanho_janela"]["width"]

    @property
    def height_janela(self):
        return self.__config["tamanho_janela"]["height"]

    @property
    def diretorio_sprites(self):
        return os.path.join(os.getenv('PYTHONPATH'), "assets/sprites")
