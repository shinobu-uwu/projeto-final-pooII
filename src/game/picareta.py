from src.game.interfaces.interface_picareta import IPicareta
from src.game.ferramenta import Ferramenta

class Picareta(Ferramenta, IPicareta):
    def __init__(self, forca, velocidade_ataque):
        super().__init__(forca, velocidade_ataque)

    def usar(self):
        print("Picaretada!")
        pass
