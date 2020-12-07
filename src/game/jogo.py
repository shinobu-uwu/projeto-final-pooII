import os
import pygame
from pygame.constants import KEYDOWN, K_LEFT, KEYUP, K_RIGHT, K_UP, K_SPACE, K_e

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
        self.__tipos_colisao = {"top": False, "bottom": False, "right": False, "left": False}
        self.__clock = pygame.time.Clock()
        self.__hud=HUD(self.__jogador)
        self.inicia_loop_teste()

    def inicia_loop_teste(self):
        x = 0 
        pygame.display.set_caption("Blockfiesta!")
        self.__screen = pygame.display.set_mode((1280, 720))
        self.__bg = pygame.image.load(os.path.join(self.__config.diretorio_sprites, "fundo.jpg"))
        rodando = True
        while rodando:
            
            rel_x = x % self.__bg.get_rect().width
            self.__clock.tick(33)
            self.__screen.blit(self.__bg, (rel_x - self.__bg.get_rect().width, 0))
            if rel_x < 1280:
                self.__screen.blit(self.__bg, (rel_x,0))
            x -= 1 
            #print(self.__jogador.posicao[0])

            self.jogador.teste_movimento = [0,0]
            self.__tipos_colisao = {"top": False, "bottom": False, "right": False, "left": False}

            if self.jogador.right == True:
                self.jogador.teste_movimento[0] += 7
            if self.jogador.left == True:
                self.jogador.teste_movimento[0] -= 5

            self.jogador.hitbox.x -= 2
            
            for bloco in self.cenario.mapa:
                bloco.hitbox.x -= 2

            self.jogador.teste_movimento[1] += self.jogador.momentum[1]
            self.jogador.momentum[1] += 6

            if self.jogador.momentum[1] > 36:
                self.jogador.momentum[1] = 36

            if self.jogador.momentum[1] > 0:
                self.jogador.is_jump = False
                self.jogador.is_idle = True

            self.mover_teste()

            if self.__tipos_colisao["bottom"]:
                self.jogador.momentum[1] = 1

            if self.__tipos_colisao["top"]:
                self.jogador.momentum[1] = 1


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False

                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.jogador.right = True
                        self.jogador.left = False
                    if event.key == K_LEFT:
                        self.jogador.left = True
                        self.jogador.right = False
                    if event.key == K_SPACE:
                        if self.__tipos_colisao["bottom"]:
                            self.jogador.momentum[1] = -36
                            self.jogador.is_jump = True
                            self.jogador.is_idle = False

                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        self.jogador.right = False
                    if event.key == K_LEFT:
                        self.jogador.left = False


                if not self.jogador.right and not self.jogador.left:
                    self.jogador.__is_idle = True

            tecla = pygame.key.get_pressed()

            self.jogador.usar(tecla)
            self.jogador.mudar_item(tecla)

                    
            self.__jogador.atualizar_teste(self.__screen)
            self.__cenario.atualizar(self.__screen)
            
            """self.atualizar() """
            self.__hud.atualizar(self.__screen,self.__clock)
            pygame.display.update()

    def mover_teste(self):
        
        
        #print(f"POS PLAYER: {self.jogador.hitbox.x} - PRE SOMA")

        #Mover e Testar o x
        self.jogador.hitbox.x += self.jogador.teste_movimento[0]
        self.jogador.posicao[0] += self.jogador.teste_movimento[0]
        lista_colisao = self.checar_colisoes_teste()

        for bloco in lista_colisao:
            #print(f"POS BLOCOR:{bloco.hitbox.x} - POS SOMA")
            #print(f"POS PLAYER:{bloco.hitbox.x} - POS SOMA")
            if self.jogador.teste_movimento[0] > 0:
                self.jogador.hitbox.right = bloco.hitbox.left
                self.__tipos_colisao["right"] = True
            
            elif self.jogador.teste_movimento[0] < 0:
                self.jogador.hitbox.left = bloco.hitbox.right
                self.__tipos_colisao["left"] = True

        
                
        #Mover e Testar o y

        self.jogador.hitbox.y += self.jogador.teste_movimento[1]
        self.jogador.posicao[1] += self.jogador.teste_movimento[1]
        lista_colisao = self.checar_colisoes_teste()

        for bloco in lista_colisao:
            if self.jogador.teste_movimento[1] >  0:
                self.jogador.hitbox.bottom = bloco.hitbox.top
                self.__tipos_colisao["bottom"] = True

            elif self.jogador.teste_movimento[1] <  0:
                self.jogador.hitbox.top = bloco.hitbox.bottom
                self.__tipos_colisao["top"] = True

        #print(self.__tipos_colisao)


    def checar_colisoes_teste(self):
        lista_colisao = []
        for bloco in self.__cenario.mapa:
            if self.jogador.hitbox.colliderect(bloco.hitbox):
                if self.jogador.is_attack == True:
                    bloco_status = self.cenario.quebrar(bloco)
                    
                    if bloco_status == False:
                        lista_colisao.append(bloco)
                else:
                    lista_colisao.append(bloco)
                

        return lista_colisao

    def checar_colisoes(self):
        
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
                        is_quebrado = self.__cenario.quebrar(bloco)

                        if is_quebrado:
                            self.__jogador.pode_mover_direita = True
                            self.__jogador.pode_mover_esquerda = True

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
                        is_quebrado = self.__cenario.quebrar(bloco)

                        if is_quebrado:
                            self.__jogador.pode_mover_direita = True
                            self.__jogador.pode_mover_esquerda = True

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

