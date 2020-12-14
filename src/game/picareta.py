from src.game.ferramenta import Ferramenta
from src.game.interfaces.interface_picareta import IPicareta


class Picareta(Ferramenta, IPicareta):
    def __init__(self, forca, velocidade_ataque):
        super().__init__(forca, velocidade_ataque)
        self.__tipo = "3"
        self.__sprite = self.get_sprites(self.__tipo)

    def get_sprites(self, tipo):
        return super().get_sprites(tipo)

    def usar(self):
        print("Picaretada!")

    @property
    def tipo(self):
        return self.__tipo
