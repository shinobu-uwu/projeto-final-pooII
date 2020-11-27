import sys
from PyQt5.Qt import QFont, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from src.views.widgets.botao_padrao import BotaoPadrao
from src.views.widgets.imagem_central import ImagemCentral
from src.views.widgets.titulo_janela import TituloJanela


class MainMenuView(QWidget):
    sinal_jogar = pyqtSignal()
    sinal_ajuda = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__layout = QVBoxLayout()
        self.mostra_view()

    def mostra_view(self):
        titulo = TituloJanela("Blockfiesta!")
        titulo.adicionar_ao_layout(self.__layout)

        imagem_central = ImagemCentral()
        imagem_central.adicionar_ao_layout(self.__layout)

        botao_jogar = BotaoPadrao("Jogar")
        botao_jogar.clicked.connect(self.__jogar)
        botao_jogar.adicionar_ao_layout(self.__layout)

        botao_ajuda = BotaoPadrao("Ajuda")
        botao_ajuda.clicked.connect(self.__ajuda)
        botao_ajuda.adicionar_ao_layout(self.__layout)

        botao_sair = BotaoPadrao("Sair")
        botao_sair.clicked.connect(self.__sair)
        botao_sair.adicionar_ao_layout(self.__layout)

        self.setLayout(self.__layout)
        return self.__layout

    def __jogar(self):
        self.sinal_jogar.emit()

    def __ajuda(self):
        self.sinal_ajuda.emit()

    def __sair(self):
        sys.exit()
