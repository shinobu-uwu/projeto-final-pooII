import os
import json
from src.config.interface_config_loader import IConfigLoader


class MenuConfigLoader():
    def __init__(self):
        self.__path = f"{os.path.abspath(os.path.dirname(__file__))}/jsons/menus.json"
        self.__load()

    def __load(self):
        with open(self.__path, 'r') as f:
            self.__config = json.load(f)

    @property
    def tamanho_janela(self):
        return tuple(self.__config["tamanho_janela"])

    @property
    def fonte_titulo(self):
        return tuple(self.__config["fonte_titulo"])

    @property
    def tamanho_titulo(self):
        return tuple(self.__config["tamanho_titulo"])

    @property
    def fonte_botoes(self):
        return tuple(self.__config["fonte_botoes"])

    @property
    def tamanho_botoes(self):
        return tuple(self.__config["tamanho_botoes"])

    @property
    def element_justification(self):
        return self.__config["element_justification"]

    @property
    def diretorio_assets(self):
        return f"{os.path.abspath(os.getenv('PYTHONPATH'))}/assets/thumbnail fases"
