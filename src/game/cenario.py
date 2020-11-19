from src.game.interfaces.interface_cenario import Icenario


class Cenario(Icenario):
    def __init__(self, fundo, mapa,final:float):
        self.__fundo= fundo
        self.__mapa = mapa
        self.__final=final
    
    @property
    def fundo(self):
        return self.__fundo

    @property
    def mapa(self):
        return self.__mapa

    @property
    def final(self):
        return self.__final
