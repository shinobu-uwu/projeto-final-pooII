from src.game.ferramenta import Ferramenta
from src.game.interfaces.interface_machado import IMachado


class Machado(Ferramenta, IMachado):
    def __init__(self, forca, velocidade_ataque):
        super().__init__(forca, velocidade_ataque)

    def usar(self):
        print("Machada!")
