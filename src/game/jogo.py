import pygame
from src.game.camera import Camera
from src.game.cenario import Cenario
from src.game.jogador import Jogador
from src.game.interfaces.interface_jogo import IJogo


class Jogo (IJogo):
    def __init__(self,tempo: float, camera: Camera, jogador: Jogador, cenario: Cenario, vitoria: bool):
        pygame.init()
        self.__camera = camera
        self.__jogador = jogador
        self.__cenario = cenario
        self.__tempo = tempo
        self.__vitoria = vitoria
        self.__clock = pygame.time.Clock()
        self.inicia_loop()

    def inicia_loop(self):
        pygame.display.set_caption("Blockfiesta!")
        self.__screen = pygame.display.set_mode((1280, 720))
        self.__bg = pygame.image.load("/home/shinobu/Documents/projeto-final-pooii/assets/sprites//bgTESTE.jpg")
        rodando = True
        while rodando:
            self.__clock.tick(33)
            self.__screen.blit(self.__bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False
            if self.__jogador.walk_count + 1 >= 33:
                self.__jogador.walk_count = 0
            self.__screen.blit(self.__jogador.sprites["idle"][self.__jogador.walk_count // 3], tuple(self.__jogador.posicao))
            self.__jogador.walk_count += 1
            pygame.display.update()

    def atualizar(self):
        if self.__jogador.walk_count + 1 >= 33:
            self.__jogador.walk_count = 0
        if self.__jogador.left:
            pass
        elif self.__jogador.right:
            pass

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
jogador = Jogador(2, [3, 3])
a = Jogo(2, 2, jogador, 2, 2)
