import os
import pygame

from src.config.jogo_config_loader import JogoConfigLoader
from src.game.camera import Camera
from src.game.cenario import Cenario
from src.game.interfaces.interface_jogo import IJogo
from src.game.jogador import Jogador
from src.game.hud import HUD


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
        self.__hud=HUD(self.__jogador)
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
            self.checar_colisoes()
            tecla = pygame.key.get_pressed()
            self.__jogador.atualizar(tecla, self.__screen)
            self.__hud.atualizar(self.__screen,self.__clock)
            self.atualizar()
            pygame.display.update()

    def checar_colisoes(self):
        
        """Vamo lá, o negócio das colisões é o seguinte, ele tá certa, o problema
            é que como ele tá em um for, ele tá checando todos, mas a colisão só funciona
            com o primeiro da lista. Acho realmente mais facil fazer com o pymunk e dar uma
            suavidade tbm no movimento dele, e a parte de quebrar os blocos é bem dboa"""


        for bloco in self.__cenario.mapa:
            #Checa se a direita do personagem colide com a esquerda de um bloco
            if self.__jogador.hitbox[0] + self.__jogador.tamanho_hitbox[0] >= bloco.hitbox[0] and\
            self.__jogador.hitbox[0] + self.__jogador.tamanho_hitbox[0] <= bloco.hitbox[0] + bloco.tamanho_hitbox[0]:
                #checa o hitbox no eixo y
                if self.__jogador.hitbox[1] >= bloco.hitbox[1] and self.__jogador.hitbox[1] <= bloco.hitbox[1] + bloco.tamanho_hitbox[1] or\
                self.__jogador.hitbox[1] + self.__jogador.tamanho_hitbox[1] >= bloco.hitbox[1] and\
                self.__jogador.hitbox[1] + self.__jogador.tamanho_hitbox[1] <= bloco.hitbox[1] + bloco.tamanho_hitbox[1]:
                    self.__jogador.pode_mover_direita = False
                    self.__jogador.pode_mover_esquerda = True
                    
                    #quebrar para a direita
                    if self.jogador.is_attack and self.jogador.last_side == 1:
                        self.__cenario.mapa.remove(bloco)
                        self.__jogador.pode_mover_direita = True
                        self.__jogador.pode_mover_esquerda = True
                        break

                #reset
                else:
                    self.__jogador.pode_mover_direita = True
                    self.__jogador.pode_mover_esquerda = True
            #mesma coisa para direita
            elif self.__jogador.hitbox[0] <= bloco.hitbox[0] + bloco.tamanho_hitbox[0] and self.__jogador.hitbox[0] >= bloco.hitbox[0]:
                if self.__jogador.hitbox[1] >= bloco.hitbox[1] and self.__jogador.hitbox[1] <= bloco.hitbox[1] + bloco.tamanho_hitbox[1] or\
                self.__jogador.hitbox[1] + self.__jogador.tamanho_hitbox[1] >= bloco.hitbox[1] and\
                self.__jogador.hitbox[1] + self.__jogador.tamanho_hitbox[1] <= bloco.hitbox[1] + bloco.tamanho_hitbox[1]:
                    self.__jogador.pode_mover_esquerda = True
                    self.__jogador.pode_mover_esquerda = False

                    #quebrar para a esquerda
                    if self.jogador.is_attack and self.jogador.last_side == 0:
                        self.__cenario.mapa.remove(bloco)
                        self.__jogador.pode_mover_direita = True
                        self.__jogador.pode_mover_esquerda = True
                        break

                #reset
                else:
                    self.__jogador.pode_mover_direita = True
                    self.__jogador.pode_mover_esquerda = True
            #reset
            else:
                self.__jogador.pode_mover_direita = True
                self.__jogador.pode_mover_esquerda = True

    def atualizar(self):
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

