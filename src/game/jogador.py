import pygame
from pygame.locals import *

from src.config.jogador_config_loader import JogadorConfigLoader
from src.exceptions.tipo_nao_compativel_exception import TipoNaoCompativelException
from src.game.inventario import Inventario
from src.game.interfaces.interface_jogador import IJogador
from src.game.item import Item
from src.game.bloco_cenario import BlocoCenario


class Jogador(IJogador):
    def __init__(self, velocidade: float, posicao_inicial: list):
        self.__config = JogadorConfigLoader()
        self.__morto = False
        self.__inventario = Inventario()
        self.__velocidade = velocidade
        self.__item_equipado = 0
        self.__posicao = posicao_inicial


        #lista composta para os sprites
        self.__sprites = self.__config.recortar_sprites()

        #bools para determinar qual animação o personagem está realizando
        self.__left = False
        self.__right = False
        #bool para saber a ultima direção que o personagem estava virado - 0 -> esquerda, 1 -> direita
        self.__last_side = 1
        self.__is_jump = False
        self.__is_attack = False
        self.__is_idle = True
        self.__is_fall = False
        self.__pode_mover = True

        #contadores para o pulo e a animação de correr
        self.__walk_count = 0
        self.__jump_count = 0
        self.__idle_count = 0
        self.__attack_count = 0
        self.__tamanho_hitbox = (self.__config.tamanho[0], self.__config.tamanho[1])
        self.__hitbox = pygame.Rect(self.__posicao[0], self.__posicao[1], self.__tamanho_hitbox[0], self.__tamanho_hitbox[1])

    def atualizar(self, tecla, screen):
        self.mover(tecla)
        if self.__walk_count + 1 >= 24:
            self.__walk_count = 0

        if self.__idle_count + 1 >= 33:
            self.__idle_count = 0

        if self.__is_attack:
            if self.__last_side == 1:
                screen.blit(self.__sprites["attack"][self.__attack_count //4], tuple(self.__posicao))
                self.__attack_count += 1

            else:
                screen.blit(self.__sprites["attackM"][self.__attack_count //4], tuple(self.__posicao))
                self.__attack_count += 1

        elif not self.__is_fall and self.__is_jump:
            if self.__last_side == 1:
                if self.left:
                    self.__last_side = 0
                    screen.blit(self.__sprites["jumpM"], tuple(self.__posicao))
                else:
                    screen.blit(self.__sprites["jump"], tuple(self.__posicao))
            else:
                if self.right:
                    self.__last_side = 1
                    screen.blit(self.__sprites["jump"], tuple(self.__posicao))
                else:
                    screen.blit(self.__sprites["jumpM"], tuple(self.__posicao))

        elif self.__is_fall:
            if self.__last_side == 1:
                if self.left:
                    self.__last_side = 0
                    screen.blit(self.__sprites["jumpM"], tuple(self.__posicao))
                else:
                    screen.blit(self.__sprites["fall"], tuple(self.__posicao))
            else:
                if self.right:
                    self.__last_side = 0
                    screen.blit(self.__sprites["jump"], tuple(self.__posicao))
                else:
                    screen.blit(self.__sprites["fallM"], tuple(self.__posicao))

        elif self.__left:
            #if self.__last_side == 1:
                #screen.blit(self.__sprites["idle"][0], tuple(self.__posicao))

            screen.blit(self.__sprites["left"][self.__walk_count // 3], tuple(self.__posicao))
            self.__walk_count += 1
            self.__idle_count = 0
            self.__last_side = 0

        elif self.__right:
            #if self.__last_side == 0:
                #screen.blit(self.__sprites["idleM"][0], tuple(self.__posicao))

            print(self.__walk_count)
            screen.blit(self.__sprites["right"][self.__walk_count // 3], tuple(self.__posicao))
            self.__walk_count += 1
            self.__idle_count = 0
            self.__last_side = 1

        elif self.__is_idle == True and self.__is_attack == False:
            #idle pra esquerda e idle pra direita
            if self.__last_side == 1:
                #direita
                screen.blit(self.__sprites["idle"][self.__idle_count // 3], tuple(self.__posicao))
                self.__idle_count += 1

            else:
                #esquerda
                screen.blit(self.__sprites["idleM"][self.__idle_count // 3], tuple(self.__posicao))
                self.__idle_count += 1

        self.__hitbox.x = self.__posicao[0]
        self.__hitbox.y = self.__posicao[1]
        self.mudar_item(tecla)
        pygame.draw.rect(screen, (255, 0, 0), self.__hitbox, 2)

    def mover(self, tecla):
        if not self.__pode_mover:
            return
        if tecla[pygame.K_RIGHT]:
            self.__posicao[0] += self.__velocidade
            self.__right = True
            self.__left = False
            if self.__posicao[0]>1200:
                self.__posicao[0]=1200

        elif tecla[pygame.K_LEFT]:
            if self.__posicao[0] - self.__velocidade >= 0:
                self.__posicao[0] -= self.__velocidade
                self.__left = True
                self.__right = False
            else:
                self.__posicao[0] = 0

        else:
            self.__right = False
            self.__left = False
            self.__is_idle = True
            self.__walk_count = 0

        if not self.__is_jump:
            if tecla[pygame.K_SPACE]:
                self.__is_jump = True
                self.__is_idle = False
                self.__walk_count = 0

        else:
            self.pular()
                
        if not self.__is_attack:
            if tecla[pygame.K_e]:
                self.__is_attack = True
                self.__is_idle = False
    
        else:
            self.usar()

    def pular(self):
        if self.__jump_count >= -10:
            neg = 1
            if self.__jump_count < 0:
                neg = -1
                self.__is_fall = True

            self.__posicao[1] -= (self.__jump_count**2) * neg
            print(self.__jump_count)
            self.__jump_count -= 1
        else:
            self.__is_jump = False
            self.__is_fall = False
            self.__jump_count = 10
        #self.__posicao[1] = 3

    def usar(self):
        
        #if self.__item_equipado>=3:
            #criar bloco
            #pass
        
            if self.__attack_count >= 11:
                self.__attack_count = 0
                self.__is_attack = False
                self.__is_idle = True

            elif self.__attack_count == 0:
                try:
                    self.__inventario.itens[self.__item_equipado].usar()
                    print("usou!")
                except AttributeError:
                    print("Sem Item")
                    self.__is_attack = False
                    self.__attack_count = 0
            else:
                self.__attack_count += 1

    def mudar_item(self, tecla):
        if tecla[pygame.K_1]:
            self.__item_equipado = 0
        elif tecla[pygame.K_2]:
            self.__item_equipado = 1
        elif tecla[pygame.K_3]:
            self.__item_equipado = 2
        elif tecla[pygame.K_4]:
            self.__item_equipado = 3
        elif tecla[pygame.K_5]:
            self.__item_equipado = 4
        elif tecla[pygame.K_6]:
            self.__item_equipado = 5


    def adicionar_item(self, item: Item):
        if isinstance(item, Item):
            try:
                i = self.__inventario.itens.index(None)
                self.__inventario.itens[i] = item
            except ValueError:
                print("Inventário cheio")
        else:
            raise TipoNaoCompativelException

    @property
    def morto(self):
        return self.__morto

    @morto.setter
    def morto(self, morto):
        self.__morto = morto

    @property
    def inventario(self):
        return self.__inventario

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def item_equipado(self):
        return self.__item_equipado

    @property
    def posicao(self):
        return self.__posicao

    @property
    def sprites(self):
        return self.__sprites

    @property
    def walk_count(self):
        return self.__walk_count

    @walk_count.setter
    def walk_count(self, walk_count):
        self.__walk_count = walk_count

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def idle_count(self):
        return self.__idle_count

    @idle_count.setter
    def idle_count(self, idle_count):
        self.__idle_count = idle_count

    @property
    def last_side(self):
        return self.__last_side

    @last_side.setter
    def last_side(self, last_side):
        self.__last_side = last_side

    @property
    def is_attack(self):
        return self.__is_attack

    @is_attack.setter
    def is_attack(self, is_attack):
        self.__is_attack = is_attack

    @property
    def attack_count(self):
        return self.__attack_count

    @attack_count.setter
    def attack_count(self, attack_count):
        self.__attack_count = attack_count

    @property
    def is_idle(self):
        return self.__is_idle

    @is_idle.setter
    def is_idle(self, is_idle):
        self.__is_idle = is_idle

    @property
    def is_fall(self):
        return self.__is_fall

    @is_fall.setter
    def is_fall(self, is_fall):
        self.__is_fall = is_fall

    @property
    def is_jump(self):
        return self.__is_jump

    @is_jump.setter
    def is_jump(self, is_jump):
        self.__is_jump = is_jump

    @property
    def pode_mover(self):
        return self.__pode_mover

    @pode_mover.setter
    def pode_mover(self, pode_mover):
        self.__pode_mover = pode_mover

    @property
    def tamanho_hitbox(self):
        return self.__tamanho_hitbox

    @property
    def hitbox(self):
        return self.__hitbox
