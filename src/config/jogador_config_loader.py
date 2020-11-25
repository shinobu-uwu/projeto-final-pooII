import os
import json

from src.config.interface_config_loader import IConfigLoader


class JogadorConfigLoader(IConfigLoader):
    def __init__(self):
        self.__path = f"{os.path.abspath(os.path.dirname(__file__))}/jsons/jogador.json"
        self.__load()

    def __load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def diretorio_sprites(self):
        return f"{os.getenv('PYTHONPATH')}/assets/sprites/"
