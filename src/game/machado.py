from src.game.interfaces.interface_machado import IMachado
from src.game.ferramenta import Ferramenta

class Machado(Ferramenta, IMachado):
    def __init__(self):
        super().__init__(forca,velocidade_ataque)

    def usar(self):
        #TODO - Implementação da Lógica de Usar
        pass