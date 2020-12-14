import os
import pygame
from pygame.constants import KEYDOWN, K_LEFT, KEYUP, K_RIGHT, K_UP, K_SPACE, K_e, K_ESCAPE

from src.config.jogo_config_loader import JogoConfigLoader
from src.game.bloco_cenario import BlocoCenario
from src.game.bloco_item import BlocoItem
from src.game.camera import Camera
from src.game.cenario import Cenario
from src.game.hud import HUD
from src.game.interfaces.interface_jogo import IJogo
from src.game.jogador import Jogador
from src.game.menu_pause import MenuPause


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
        self.__hud=HUD()
        self.__blocktimer=pygame.time.get_ticks()
        self.__screen = pygame.display.set_mode((1280, 720))
        self.__menu_pause = MenuPause(self.__screen)

    def inicia_loop(self):
        x = 0
        pygame.display.set_caption("Blockfiesta!")
        try:
            self.__bg = pygame.image.load(self.cenario.fundo)
        except FileNotFoundError:
            self.__bg = pygame.image.load(os.path.join(self.__config.diretorio_sprites, f"fundo5.jpg"))
        rodando = True
        while rodando:
            rel_x = x % self.__bg.get_rect().width
            self.__clock.tick(33)
            self.__screen.blit(self.__bg, (rel_x - self.__bg.get_rect().width, 0))

            if self.__jogador.hitbox[1] >= 500 :
                print ("Morreu")
                losetext = pygame.font.Font(pygame.font.match_font(self.__config.fonte), self.__config.tamanho_fonte).render(f"Você perdeu!", True, self.__config.cor_fonte)
                self.__screen.blit(losetext, self.__config.posicao_texto)
                timertexto=pygame.time.get_ticks()
                while pygame.time.get_ticks()<timertexto+3000:
                    pygame.display.update()
                rodando=False

            elif self.__jogador.hitbox[1]-x>self.__cenario.final:
                print ("Ganhou")
                wintext = pygame.font.Font(pygame.font.match_font(self.__config.fonte), self.__config.tamanho_fonte).render(f"Terminou essa fase!", True, self.__config.cor_fonte)
                self.__screen.blit(wintext, self.__config.posicao_texto)
                timertexto=pygame.time.get_ticks()
                while pygame.time.get_ticks()<timertexto+3000:
                    pygame.display.update()
                rodando=False

            if rel_x < 1280:
                self.__screen.blit(self.__bg, (rel_x,0))
            x -= 1 

            self.jogador.teste_movimento = [0,0]
            self.__tipos_colisao = {"top": False, "bottom": False, "right": False, "left": False}

            if self.jogador.right == True:
                self.jogador.teste_movimento[0] += 7
            if self.jogador.left == True:
                self.jogador.teste_movimento[0] -= 5

            self.jogador.hitbox.x -= 2
            
            for item in self.cenario.itens:
                item.hitbox.x -= 2
            
            for bloco in self.cenario.mapa:
                bloco.hitbox.x -= 2
                if bloco.hitbox.x <= -44:
                    self.cenario.remover_bloco_mapa(bloco)
                    

            for item in self.__cenario.itens:
                item.hitbox.y += 8

            self.jogador.teste_movimento[1] += self.jogador.momentum[1]
            self.jogador.momentum[1] += 6

            if self.jogador.momentum[1] > 36:
                self.jogador.momentum[1] = 36

            if self.jogador.momentum[1] > 0:
                self.jogador.is_jump = False
                self.jogador.is_idle = True

            self.mover_teste()
            self.mover_itens()

            if self.__tipos_colisao["bottom"]:
                self.jogador.momentum[1] = 1

            if self.__tipos_colisao["top"]:
                self.jogador.momentum[1] = 1


            if self.jogador.hitbox.x >= 1248:
                self.jogador.right = False

            tecla = pygame.key.get_pressed()

            self.jogador.usar(None)
            self.jogador.mudar_item(tecla)
            self.adicionar_bloco_cenario(tecla)

            self.__jogador.atualizar_teste(self.__screen)
            self.__cenario.atualizar(self.__screen)
            self.__hud.atualizar(self.__jogador, self.__screen, int(pygame.time.get_ticks()/1000))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
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
                    if event.key == K_e:
                        self.jogador.usar(event.key)
                    if event.key == K_ESCAPE:
                        self.pausar()

                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        self.jogador.right = False
                    if event.key == K_LEFT:
                        self.jogador.left = False

                if not self.jogador.right and not self.jogador.left:
                    self.jogador.__is_idle = True

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


    def mover_itens(self):
        lista_colisao_itens = self.checar_colisoes_itens()

        for dupla in lista_colisao_itens:
            dupla[0].hitbox.y = dupla[1].hitbox.y - 10
            #dupla[0].hitbox.x = dupla[1].hitbox.x
            #item.hitbox.y = bloco.hitbox.y - 10
            #item.hitbox.x = bloco.hitbox.x

    def checar_colisoes_teste(self):
        lista_colisao = []
        for bloco in self.__cenario.mapa:

            if self.jogador.hitbox.colliderect(bloco.hitbox):
                if self.jogador.is_attack == True and self.jogador.hitbox.y != bloco.hitbox.y:
                    bloco_status = self.cenario.quebrar(bloco,self.__jogador.item_equipado)
                    
                    if bloco_status == False:
                        lista_colisao.append(bloco)
                else:
                    lista_colisao.append(bloco)
            
            else:
                media_bloco_x = bloco.hitbox.x + (bloco.hitbox.width/2)
                media_bloco_y = bloco.hitbox.y + (bloco.hitbox.height/2)

                media_jogador_x = self.jogador.hitbox.x + (self.jogador.hitbox.width/2)
                media_jogador_y = self.jogador.hitbox.y + (self.jogador.hitbox.height/2)

                #Sistema de vantagens/desvantagens das ferramentas
                #específco - material -- marreta = todos    /   pa = dano bom menos metal    /   picareta = boa em metal e pedra
                #geral - area de contato -- marreta = destroi tudo  /   pa = alcance menor  /   picareta = normal

                if self.jogador.item_equipado == 1:
                    alcance = 75
                elif self.jogador.item_equipado == 2:
                    alcance = 120
                else:
                    alcance = 95

                if abs(media_bloco_x - media_jogador_x) < alcance:
                    if abs(media_bloco_y - media_jogador_y) < alcance:

                        if self.jogador.hitbox.x < bloco.hitbox.x:
                            if self.jogador.last_side == 1 and self.jogador.is_attack:
                                bloco_status = self.cenario.quebrar(bloco,self.__jogador.item_equipado)
                        
                        elif self.jogador.hitbox.x > bloco.hitbox.x:
                            if self.jogador.last_side == 0 and self.jogador.is_attack:
                                bloco_status = self.cenario.quebrar(bloco,self.__jogador.item_equipado)

            
        return lista_colisao


    def checar_colisoes_itens(self):
        lista_colisoes_itens = []

        for item in self.cenario.itens:
            for bloco in self.__cenario.mapa:
                    if item.hitbox.colliderect(bloco.hitbox):
                        lista_colisoes_itens.append([item, bloco])

            if item.hitbox.colliderect(self.jogador.hitbox):
                self.adicionar_item(item)
                        

        return lista_colisoes_itens


    def adicionar_item(self, item):
        self.cenario.remover_item(item)
        self.jogador.adicionar_item(item)

    def adicionar_bloco_cenario(self, tecla):
        if tecla[K_e] and self.__blocktimer<pygame.time.get_ticks()-300:
            self.__blocktimer=pygame.time.get_ticks()
            pos_item = self.jogador.item_equipado
            item = self.jogador.inventario.itens[pos_item]

            if isinstance(item, BlocoItem):
                self.jogador.remover_item(item)
                self.cenario.adicionar_bloco_cenario(item, [self.jogador.hitbox.x,self.jogador.hitbox.y], self.jogador.last_side)

    def pausar(self):
        self.__menu_pause.show(self.__screen)

    def atualizar(self):
        pass

    @property
    def tempo(self):
        return self.__tempo

    @property
    def camera(self):
        return self.__camera

    @property
    def jogador(self):
        return self.__jogador

    @property
    def cenario(self):
        return self.__cenario

    @property
    def vitoria(self):
        return self.__vitoria
