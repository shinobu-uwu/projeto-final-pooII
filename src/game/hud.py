import pygame
from pygame.locals import *
from pygame.transform import scale

from src.config.hud_config_loader import HUDConfigLoader
from src.game.interfaces.interface_hud import IHud
from src.game.jogador import Jogador
from src.game.bloco_item import BlocoItem


class HUD(IHud):
    def __init__(self):
        self.__config = HUDConfigLoader()
        #adcionar imagens de slot de inventario
        self.__slots = [pygame.Surface(self.__config.tamanho_slot) for i in range(self.__config.quantidade_slots)]
        self.__cursor = pygame.Surface(self.__config.tamanho_cursor)
        self.__cursor.fill(self.__config.cor_cursor)

    def atualizar(self, jogador, screen, tempo):
        tempo = pygame.font.Font(pygame.font.match_font(self.__config.fonte_tempo), self.__config.tamanho_fonte_tempo).render(f"Tempo: {tempo}s", True, self.__config.cor_fonte_tempo)
        screen.blit(tempo, self.__config.posicao_tempo)
        screen.blit(self.__cursor, (self.__config.posicao_slot[0] + jogador.item_equipado*(self.__config.tamanho_slot[0] + self.__config.espacamento_slots),
                                    self.__config.posicao_slot[1] + self.__config.tamanho_slot[1] + self.__config.espacamento_cursor))
        for slot in self.__slots:
            slot.fill(self.__config.cor_slot)
            screen.blit(slot, (self.__config.posicao_slot[0] + self.__slots.index(slot)*(self.__config.tamanho_slot[0] + self.__config.espacamento_slots), self.__config.posicao_slot[1]))

        for item in jogador.inventario.itens:
            try:
                screen.blit(scale(item.sprite, item.tamanho), (self.__config.posicao_slot[0] + jogador.inventario.itens.index(item)*
                                                              (self.__config.tamanho_slot[0] + self.__config.espacamento_slots + self.__config.espacamento_slots//4),
                                                               self.__config.posicao_slot[1] + self.__config.espacamento_slots//2))
                #Ele não consegue acessar quantidade do item
                quantidade = pygame.font.Font(pygame.font.match_font(self.__config.fonte_itens, self.__config.tamanho_fonte_itens).render(str(item.quantidade), True, (self.__config.cor_fonte_itens)))
            except AttributeError:
                pass
