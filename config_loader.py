import json


#Carrega as configurações necessárias para menus
class ConfigLoader:
    def __init__(self, config = "config.json"):
        with open(config, 'r') as f:
            self.__config = json.load(f)

    @property
    def tamanho_janela(self):
        return tuple(self.__config["tamanho_janela"])

    @property
    def posicao_janela(self):
        return tuple(self.__config["posicao_janela"])

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
