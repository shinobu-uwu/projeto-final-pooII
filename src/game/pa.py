from src.game.ferramenta import Ferramenta
from src.game.interfaces.interface_pa import IPa


class Pa(Ferramenta, IPa):
    def __init__(self, forca, velocidade_ataque):
        super().__init__(forca, velocidade_ataque)
        self.__tipo = "2"
        self.__sprite = self.get_sprites(self.__tipo)

    def get_sprites(self, tipo):
        return super().get_sprites(tipo)

    def usar(self):
        print("Pázada!")

    @property
    def tipo(self):
        return self.__tipo

