from src.config.bloco_config_loader import BlocoConfigLoader
from src.game.item import Item


class BlocoItem(Item):
    def __init__(self, material, posicao):
        super().__init__(material)
        self.__config = BlocoConfigLoader(material)
        self.__sprite = self.__config.obter_sprite_original()
        self.__posicao = posicao

    def usar(self):
        pass

    @property
    def sprite(self):
        return self.__sprite

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        return self.__posicao

    @property
    def tamanho(self):
        return self.__config.tamanho_original
