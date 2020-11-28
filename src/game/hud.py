from src.game.interfaces.interface_hud import IHud
from src.game.jogador import Jogador
import pygame
from pygame.locals import *

class HUD(IHud):
    def __init__(self,jogador: Jogador):
        self.__jogador=jogador

        self.space=pygame.Surface((30,30))
        #self.space=self.space.fill((0,0,0))

    def atualizar(self,screen,time):
        for i in range (0,6):
            screen.blit(self.space,(20+i*35,10))

        text_surface=pygame.font.Font(pygame.font.match_font('arial'),20).render("Tempo"+str(time)+"segs",True,(255,255,255))
        #text_surface=pygame.font.Font(font_name,size).render("Time:"+str(time),True,(255,255,255))
        #text_rect=text_surface.get_rect()
        #text_rect.midtop=(x,y)
        screen.blit(text_surface,(1150,20))