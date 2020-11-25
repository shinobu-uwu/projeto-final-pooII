import os
from PyQt5.Qt import QFont, QPixmap, pyqtSignal
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QVBoxLayout

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
        alinhamento_botao_fases = Qt.AlignHCenter

        titulo = QLabel("Selecione a fase")
        titulo.setFont(QFont(self.__config.fonte_titulo, self.__config.tamanho_fonte_titulo))
        self.__layout.addWidget(titulo, alignment = alinhamento_titulo)

        fases_layout = QGridLayout()
        nome_imagens = sorted(os.listdir(f"{self.__config.diretorio_assets}/thumbnail fases/"))
        botoes = []
        for nome in nome_imagens:
            botao = QPushButton()
            botao.setStyleSheet(f"""
            background-image: url({self.__config.diretorio_assets}/thumbnail fases/{nome});
            {self.__config.fases_stylesheet}
            """)
            botao.setFixedSize(self.__config.width_fases, self.__config.height_fases)
            botoes.append(botao)
        fases_layout.addWidget(botoes[0], 0, 0)
        fases_layout.addWidget(botoes[1], 0, 1)
        fases_layout.addWidget(botoes[2], 0, 2)
        fases_layout.addWidget(botoes[3], 1, 0)
        fases_layout.addWidget(botoes[4], 1, 1)
        fases_layout.addWidget(botoes[5], 1, 2)
        self.__layout.addLayout(fases_layout)

        botao_voltar = QPushButton("Voltar")
        botao_voltar.setFont(QFont(self.__config.fonte_botoes, self.__config.tamanho_fonte_botoes))
        botao_voltar.setStyleSheet(self.__config.botoes_stylesheet)
        botao_voltar.setFixedSize(self.__config.width_botoes, self.__config.height_botoes)
        botao_voltar.clicked.connect(self.__voltar)
        self.__layout.addWidget(botao_voltar, alignment = alinhamento_botao)

        self.setLayout(self.__layout)
        return self.__layout

    def __voltar(self):
        self.sinal_voltar.emit()
