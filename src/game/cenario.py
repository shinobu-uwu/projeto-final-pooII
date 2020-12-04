import pygame

from src.game.interfaces.interface_cenario import ICenario


class Cenario(ICenario):
    def __init__(self, fundo, mapa, final:float):
        self.__fundo = fundo
        self.__mapa = mapa
        self.__final = final

        self.__hitbox_blocos = [bloco.hitbox for bloco in self.__mapa]

    def quebrar(self, bloco):
        if bloco.vida == bloco.dano:
            self.__mapa.remove(bloco)
            return True
        else:
            bloco.vida -= bloco.dano
            bloco.atualizar()
            return False

    def atualizar(self, screen):
        for bloco in self.__mapa:
            screen.blit(bloco.sprite, tuple(bloco.posicao))
            pygame.draw.rect(screen, (255, 0, 0), bloco.hitbox, 2)

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
