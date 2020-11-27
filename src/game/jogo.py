import pygame

from src.config.jogo_config_loader import JogoConfigLoader
from src.game.camera import Camera
from src.game.cenario import Cenario
from src.game.jogador import Jogador
from src.game.interfaces.interface_jogo import IJogo


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
        self.__bg = pygame.image.load(f"{self.__config.diretorio_sprites}/bgTESTE.jpg")
        rodando = True
        while rodando:
            self.__clock.tick(33)
            self.__screen.blit(self.__bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False
            tecla = pygame.key.get_pressed()
            self.__jogador.mover(tecla)
            self.atualizar()
            pygame.display.update()

    def atualizar(self):
        if self.__jogador.walk_count + 1 >= 24:
            self.__jogador.walk_count = 0

        if self.__jogador.idle_count + 1 >= 33:
            self.__jogador.idle_count = 0

        if self.__jogador.is_attack:
            if self.__jogador.last_side == 1:
                self.__screen.blit(self.__jogador.sprites["attack"][self.__jogador.attack_count //4], tuple(self.__jogador.posicao))
                self.__jogador.attack_count += 1

            else:
                self.__screen.blit(self.__jogador.sprites["attackM"][self.__jogador.attack_count //4], tuple(self.__jogador.posicao))
                self.__jogador.attack_count += 1

        elif not self.__jogador.is_fall and self.__jogador.is_jump:
            if self.jogador.last_side == 1:
                self.__screen.blit(self.__jogador.sprites["jump"], tuple(self.__jogador.posicao))
            else:
                self.__screen.blit(self.__jogador.sprites["jumpM"], tuple(self.__jogador.posicao))

        elif self.__jogador.is_fall:
            if self.__jogador.last_side == 1:
                self.__screen.blit(self.__jogador.sprites["fall"], tuple(self.__jogador.posicao))
            else:
                self.__screen.blit(self.__jogador.sprites["fallM"], tuple(self.__jogador.posicao))

        elif self.__jogador.left:
            #if self.__jogador.last_side == 1:
                #self.__screen.blit(self.__jogador.sprites["idle"][0], tuple(self.__jogador.posicao))

            self.__screen.blit(self.__jogador.sprites["left"][self.__jogador.walk_count // 3], tuple(self.__jogador.posicao))
            self.__jogador.walk_count += 1
            self.__jogador.idle_count = 0
            self.__jogador.last_side = 0

        elif self.__jogador.right:
            #if self.__jogador.last_side == 0:
                #self.__screen.blit(self.__jogador.sprites["idleM"][0], tuple(self.__jogador.posicao))

            print(self.__jogador.walk_count)
            self.__screen.blit(self.__jogador.sprites["right"][self.__jogador.walk_count // 3], tuple(self.__jogador.posicao))
            self.__jogador.walk_count += 1
            self.__jogador.idle_count = 0
            self.__jogador.last_side = 1

        elif self.__jogador.is_idle == True and self.__jogador.is_attack == False:
            #idle pra esquerda e idle pra direita
            if self.__jogador.last_side == 1:
                #direita
                self.__screen.blit(self.__jogador.sprites["idle"][self.__jogador.idle_count // 3], tuple(self.__jogador.posicao))
                self.__jogador.idle_count += 1

            else:
                #esquerda
                self.__screen.blit(self.__jogador.sprites["idleM"][self.__jogador.idle_count // 3], tuple(self.__jogador.posicao))
                self.__jogador.idle_count += 1

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


jogador = Jogador(8, [3, 3])
a = Jogo(2, 2, jogador, 2, 2)
