from src.game.interfaces.interface_hud import IHud
from src.game.jogador import Jogador
import pygame
from pygame.locals import *

class HUD(IHud):
    def __init__(self,jogador: Jogador):
        self.__jogador=jogador
        #adcionar imagens de slot de inventario
        self.space=pygame.Surface((30,30))
        

    def atualizar(self,screen,time):
        greenimage=pygame.Surface((30,10))
        greenimage.fill((255,0,255))
        screen.blit(greenimage,(20+(self.__jogador.item_equipado)*35,55))
        for i in range(0,6):
            screen.blit(self.space,(20+i*35,20))

        text_surface=pygame.font.Font(pygame.font.match_font('arial'),20).render("Tempo"+str(time)+"segs",True,(255,255,255))
        #text_surface=pygame.font.Font(font_name,size).render("Time:"+str(time),True,(255,255,255))
        screen.blit(text_surface,(1150,20))