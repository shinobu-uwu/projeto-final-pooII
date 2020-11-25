import pygame
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
        #self.__win = ""
        #self.__bg = ""

        #temp (?)
        #self.__run = True

            #setar o framerate do jogo
        #self.__clock = pygame.time.Clock()

        #inicio do loop do jogo
        #self.inicia_loop()

    #temp(?)
    """ def inicia_loop(self):
        #temp
        pygame.init()
        pygame.display.set_caption("Blockfiesta!")
        win = pygame.display.set_mode((1280,720))
        self.__win = win
        bg = pygame.image.load("C:/Users/Arthur/Projects/projeto-final-pooII/assets/sprites/bgTESTE.jpg").convert_alpha()
        self.__bg = bg
        while self.__run:
            self.__clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__run = False

            tecla = pygame.key.get_pressed()
            self.__jogador.mover(tecla)
            self.atualizar()
     """
    #temp
    def atualizar(self):
        #esse num tem a ver com o indice da animação que ele vai fazer
        #com walk tem 8 sprites e uso 3 frames pra 1 sprite temos 24
        #se esse número for maior que 24 vai dar erro, por isso esse if

        #background TESTE
        self.__win.blit(self.__bg, (0,0))

        if self.__jogador.walk_count + 1 >= 24:
            self.__jogador.walk_count = 0

        if self.__jogador.left:
            self.__win.blit(self.__jogador.sprites["left"][self.__jogador.walk_count//3], (self.__jogador.posicao[0],self.__jogador.posicao[1]))
            self.__jogador.walk_count += 1

        elif self.__jogador.right:
            self.__win.blit(self.__jogador.sprites["right"][self.__jogador.walk_count//3], (self.__jogador.posicao[0],self.__jogador.posicao[1]))
            self.__jogador.walk_count += 1

        else:
            self.__win.blit(self.__jogador.sprites["idle"][0], (self.__jogador.posicao[0],self.__jogador.posicao[1]))
            self.__jogador.walk_count = 0

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
