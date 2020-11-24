from src.game.interfaces.interface_sistema import ISistema


class Sistema (ISistema):
    def __init__(self, estado_jogo: str):
        self.__estado_jogo = estado_jogo

    def selecionar_fase(self):
        pass

    def abrir_opcoes(self):
        pass
    
    def fechar(self):
        pass

    @property
    def estado_jogo(self):
        return self.__estado_jogo
