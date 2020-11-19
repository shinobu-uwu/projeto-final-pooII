from src.game.interfaces.interface_bloco_cenario import Iblococenario


class Bloco_cenario(Iblococenario):
    def __init__(self, material:int,dano:float,posicao:list):
        self.__material= material
        self.__dano = dano
        self.__posicao=posicao
    
    def quebrar(self):
        pass

    @property
    def material(self):
        return self.__material

    @property
    def dano(self):
        return self.__dano

    @property
    def posicao(self):
        return self.__posicao
