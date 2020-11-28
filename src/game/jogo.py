import os
import pygame

from src.config.jogo_config_loader import JogoConfigLoader
from src.game.camera import Camera
from src.game.cenario import Cenario
from src.game.interfaces.interface_jogo import IJogo
from src.game.jogador import Jogador


class Jogo (IJogo):
    def __init__(self,tempo: float, camera: Camera, jogador: Jogador, cenario: Cenario, vitoria: bool):
        pygame.init()
        self.__config = JogoConfigLoader()
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
        self.__bg = pygame.image.load(os.path.join(self.__config.diretorio_sprites, "fundo.jpg"))
        rodando = True
        while rodando:
            self.__clock.tick(33)
            self.__screen.blit(self.__bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False
            self.__cenario.atualizar(self.__screen)
            if self.__jogador.hitbox.collidelist(self.__cenario.hitbox_blocos) != -1:
                print("colidindo!!")

            tecla = pygame.key.get_pressed()
            self.__jogador.atualizar(tecla, self.__screen)
            self.atualizar()
            # self.__screen.blit(self.__jogador.sprites["attack"][0], (400, 500))
            # self.__screen.blit(self.__jogador.sprites["attack"][1], (600, 500))
            # self.__screen.blit(self.__jogador.sprites["attack"][2], (800, 500))
            # self.__screen.blit(self.__jogador.sprites["idle"][0], (1000, 500))
            pygame.display.update()

    def atualizar(self):
        #TODO colisão
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

jog = Jogador(5,[20,20])

camera = Camera(5,[20,20])
cen = Cenario("","",10)
jogo = Jogo(10,camera,jog,cen,0)