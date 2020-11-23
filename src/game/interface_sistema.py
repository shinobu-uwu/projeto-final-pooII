from abc import ABC, abstractmethod
class ISistema (ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def selecionar_fase(self):
        pass

    @abstractmethod
    def abrir_opcoes(self):
        pass

    @abstractmethod
    def fechar(self):
        pass

    @abstractmethod
    @property
    def estado_jogo(self):
        pass