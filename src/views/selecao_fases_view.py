from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.Qt import QFont, QPixmap, pyqtSignal
from PyQt5.QtCore import Qt
import os

from src.config.menu_config_loader import MenuConfigLoader


class SelecaoFasesView(QWidget):
    sinal_fase = pyqtSignal(int)
    sinal_voltar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.__layout = QVBoxLayout()
        self.__layout.setAlignment(Qt.AlignHCenter)
        self.mostra_view()

    def mostra_view(self):
        alinhamento_titulo = Qt.AlignHCenter | Qt.AlignTop
        alinhamento_botao = Qt.AlignHCenter | Qt.AlignBottom

        titulo = QLabel("Selecione a fase")
        titulo.setFont(QFont(self.__config.fonte_titulo, self.__config.tamanho_fonte_titulo))
        self.__layout.addWidget(titulo, alignment = alinhamento_titulo)

        #TODO imagens


        botao_voltar = QPushButton("Voltar")
        botao_voltar.setFont(QFont(self.__config.fonte_botoes, self.__config.tamanho_fonte_botoes))
        botao_voltar.setFixedSize(self.__config.width_botoes, self.__config.height_botoes)
        botao_voltar.clicked.connect(self.__voltar)
        self.__layout.addWidget(botao_voltar, alignment = alinhamento_botao)

        self.setLayout(self.__layout)
        return self.__layout

    def __imagem_pixmap(self, img):
        return QPixmap(img)

    def __voltar(self):
        self.sinal_voltar.emit()
