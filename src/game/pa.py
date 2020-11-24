from src.game.ferramenta import Ferramenta
from src.game.interfaces.interface_pa import IPa


class Pa(Ferramenta, IPa):
    def __init__(self, forca, velocidade_ataque):
        super().__init__(forca, velocidade_ataque)

    def usar(self):
        print("Pázada!")
