import os
import json

from src.config.config_loader import ConfigLoader


class BlocoConfigLoader(ConfigLoader):
    def __init__(self):
        self.__path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "jsons/blocos.json")
        self.load()

    def load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def tamanho(self):
        return tuple(self.__config["tamanho"])
