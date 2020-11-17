from inventario import Inventario
from interface_jogador import IJogador


class Jogador(IJogador):
    def __init__(self):
        self.__morto = False
        self.__inventario = Inventario()
        self.__velocidade = 5#temporário
        self.__item_equipado = 0
        self.__posicao = [0, 10]#temporário
