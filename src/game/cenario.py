import pygame

from src.game.bloco_item import BlocoItem
from src.game.interfaces.interface_cenario import ICenario


class Cenario(ICenario):
    def __init__(self, fundo, mapa, final:float):
        self.__fundo = fundo
        self.__mapa = mapa
        self.__final = final
        #itens no chão
        self.__itens = []
        self.__hitbox_blocos = [bloco.hitbox for bloco in self.__mapa]

    def quebrar(self, bloco):
        if bloco.vida == bloco.dano:
            self.__mapa.remove(bloco)
            self.__itens.append(BlocoItem(bloco.material, [bloco.hitbox.x + bloco.tamanho_hitbox[0]//2, bloco.hitbox.y + bloco.tamanho_hitbox[1]]))
            return True
        else:
            bloco.vida -= bloco.dano
            bloco.atualizar()
            return False

    def atualizar(self, screen):
        for bloco in self.__mapa:
            screen.blit(bloco.sprite, (bloco.hitbox.x, bloco.hitbox.y))
            pygame.draw.rect(screen, (255, 0, 0), bloco.hitbox, 2)
        for item in self.__itens:
            screen.blit(item.sprite, tuple(item.posicao))

    @property
    def fundo(self):
        return self.__fundo

    @property
    def mapa(self):
        return self.__mapa

    @property
    def final(self):
        return self.__final

    @property
    def hitbox_blocos(self):
        return self.__hitbox_blocos

    @property
    def itens(self):
        return self.__itens
