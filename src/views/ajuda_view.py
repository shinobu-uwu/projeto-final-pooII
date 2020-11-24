from PyQt5.Qt import QFont, pyqtSignal
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QVBoxLayout

from src.config.menu_config_loader import MenuConfigLoader


class AjudaView(QWidget):
    sinal_voltar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.__layout = QVBoxLayout()
        self.mostra_view()

    def mostra_view(self):
        #pretendo colocar isso no config loader, de algum jeito...
        alinhamento_titulo = Qt.AlignHCenter | Qt.AlignTop
        alinhamento_controles = Qt.AlignCenter
        alinhamento_botao = Qt.AlignHCenter | Qt.AlignBottom

        titulo = QLabel("Controles")
        titulo.setFont(QFont(self.__config.fonte_titulo, self.__config.tamanho_fonte_titulo))
        self.__layout.addWidget(titulo, alignment = alinhamento_titulo)

        #TBD
        # controles = QLabel()
        # controles.setFont(QFont(self.__config.fonte_titulo, self.__config.tamanho_fonte_titulo))
        # self.__layout.addWidget(titulo, alignment = alinhamento_controles)

        botao_voltar = QPushButton("Voltar")
        botao_voltar.setFont(QFont(self.__config.fonte_botoes, self.__config.tamanho_fonte_botoes))
        botao_voltar.setFixedSize(self.__config.width_botoes, self.__config.height_botoes)
        botao_voltar.clicked.connect(self.__voltar)
        self.__layout.addWidget(botao_voltar, alignment = alinhamento_botao)

        self.setLayout(self.__layout)
        return self.__layout

    def __voltar(self):
        self.sinal_voltar.emit()
