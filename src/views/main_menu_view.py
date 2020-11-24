import sys
from PyQt5.Qt import QFont, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from src.config.menu_config_loader import MenuConfigLoader


class MainMenuView(QWidget):
    sinal_jogar = pyqtSignal()
    sinal_ajuda = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.__layout = QVBoxLayout()
        self.mostra_view()

    def mostra_view(self):
        #pretendo colocar isso no config loader, de algum jeito...
        alinhamento_titulo = Qt.AlignHCenter | Qt.AlignTop
        alinhamento_botao = Qt.AlignHCenter | Qt.AlignBottom

        titulo = QLabel("Algum dia saberemos")
        titulo.setFont(QFont(self.__config.fonte_titulo, self.__config.tamanho_fonte_titulo))
        self.__layout.addWidget(titulo, alignment = alinhamento_titulo)

        imagem_central = QLabel()
        pixmap = QPixmap(self.__config.diretorio_assets + "/menu principal/centro.png")
        imagem_central.setPixmap(pixmap)
        imagem_central.setFixedSize(960, 540)
        self.__layout.addWidget(imagem_central, alignment = Qt.AlignCenter)

        botao_jogar = QPushButton("Jogar")
        botao_jogar.setFont(QFont(self.__config.fonte_botoes, self.__config.tamanho_fonte_botoes))
        botao_jogar.setFixedSize(self.__config.width_botoes, self.__config.height_botoes)
        botao_jogar.clicked.connect(self.__jogar)
        self.__layout.addWidget(botao_jogar, alignment = alinhamento_botao)

        botao_ajuda = QPushButton("Ajuda")
        botao_ajuda.setFont(QFont(self.__config.fonte_botoes, self.__config.tamanho_fonte_botoes))
        botao_ajuda.setFixedSize(self.__config.width_botoes, self.__config.height_botoes)
        botao_ajuda.clicked.connect(self.__ajuda)
        self.__layout.addWidget(botao_ajuda, alignment = alinhamento_botao)

        botao_sair = QPushButton("Sair")
        botao_sair.setFont(QFont(self.__config.fonte_botoes, self.__config.tamanho_fonte_botoes))
        botao_sair.setFixedSize(self.__config.width_botoes, self.__config.height_botoes)
        botao_sair.clicked.connect(self.__sair)
        self.__layout.addWidget(botao_sair, alignment = alinhamento_botao)

        self.setLayout(self.__layout)
        return self.__layout

    def __jogar(self):
        self.sinal_jogar.emit()

    def __ajuda(self):
        self.sinal_ajuda.emit()

    def __sair(self):
        sys.exit()
