import json
import os
from src.config.config_loader import ConfigLoader


class MenuConfigLoader(ConfigLoader):
    def __init__(self):
        self.__path = f"{os.path.abspath(os.path.dirname(__file__))}/jsons/menus.json"
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
    def fonte_titulo(self):
        return self.__config["fonte_titulo"]["fonte"]

    @property
    def tamanho_fonte_titulo(self):
        return self.__config["fonte_titulo"]["tamanho"]

    @property
    def tamanho_titulo(self):
        return tuple(self.__config["tamanho_titulo"])

    @property
    def fonte_botoes(self):
        return self.__config["fonte_botoes"]["fonte"]

    @property
    def tamanho_fonte_botoes(self):
        return self.__config["fonte_botoes"]["tamanho"]

    @property
    def width_botoes(self):
        return self.__config["tamanho_botoes"]["width"]

    @property
    def height_botoes(self):
        return self.__config["tamanho_botoes"]["height"]

    @property
    def botoes_stylesheet(self):
        return self.__config["botoes_stylesheet"]

    @property
    def fases_stylesheet(self):
        return self.__config["fases_stylesheet"]

    @property
    def width_fases(self):
        return self.__config["tamanho_fases"]["width"]

    @property
    def height_fases(self):
        return self.__config["tamanho_fases"]["height"]
