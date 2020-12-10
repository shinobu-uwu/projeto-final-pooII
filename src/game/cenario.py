import pygame

from src.game.bloco_item import BlocoItem
from src.game.bloco_cenario import BlocoCenario
from src.game.interfaces.interface_cenario import ICenario
from src.config.cenario_config_loader import CenarioConfigLoader

class Cenario(ICenario):
    def __init__(self, fundo,mapa,final:float):
        self.__fundo = fundo
        
        self.__final = final
        self.__config = CenarioConfigLoader()
        configmapa=self.__config.obter_mapa(mapa)
        listablocos=[]
        for y in range (0,len(configmapa)):
            for x in range (0,(len(configmapa[y]))):
                try:
                    bloco = BlocoCenario(int(configmapa[y][x]), [x*33, y*(30)])
                #if configmapa[y][x]=="1":
                    #bloco = BlocoCenario(1, [x*33, y*(30)])
                    listablocos.append(bloco)
                except FileNotFoundError:
                    pass
                #else:
                #    pass
        self.__mapa= listablocos
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
            screen.blit(item.sprite, (item.hitbox.x, item.hitbox.y))

    def remover_item(self, item):
        self.__itens.remove(item)


    def adicionar_bloco_cenario(self, item: BlocoItem, pos: list):
        #Criar bloco
        bloco = BlocoCenario(item.material, [pos[0] + 60, pos[1] + 28])

        #Adicionar o bloco ao cenário
        self.__mapa.append(bloco)

    def remover_bloco_mapa(self, bloco):
        self.__mapa.remove(bloco)

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
