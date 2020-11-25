import os
import json

from src.config.interface_config_loader import IConfigLoader


class JogoConfigLoader(IConfigLoader):
    def __init__(self):
        self.__path = f"{os.path.abspath(os.path.dirname(__file__))}/jsons/jogo.json"
        self.__load()

    def __load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def width_janela(self):
        return self.__config["tamanho_janela"]["width"]

    @property
    def height_janela(self):
        return self.__config["tamanho_janela"]["height"]

    @property
    def diretorio_assets(self):
        return f"{os.getenv('PYTHONPATH')}/assets"
