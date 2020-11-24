from src.game.camera import Camera
from src.game.cenario import Cenario
from src.game.jogador import Jogador
from src.game.interfaces.interface_jogo import IJogo


class Jogo (IJogo):
    def __init__(self,tempo: float, camera: Camera, jogador: Jogador, cenario: Cenario, vitoria: bool):
        self.__camera = camera
        self.__jogador = jogador
        self.__cenario = cenario
        self.__tempo = tempo
        self.__vitoria = vitoria

    @property
    def tempo (self):
        return self.__tempo

    @property
    def camera (self):
        return self.__camera

    @property
    def jogador(self):
        return self.__jogador

    @property
    def cenario (self):
        return self.__cenario

    @property
    def vitoria (self):
        return self.__vitoria
