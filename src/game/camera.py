from src.game.interfaces.interface_camera import ICamera


class Camera(ICamera):
    def __init__(self, velocidade:float, posicao:list):
        self.__velocidade = velocidade
        self.__posicao = posicao

    def mover(self):
        self.__posicao += self.__velocidade

    @property
    def posicao(self):
        return self.__posicao

    @property
    def velocidade(self):
        return self.__velocidade
