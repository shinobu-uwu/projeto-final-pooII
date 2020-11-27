from PyQt5.Qt import QFont, pyqtSignal
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QVBoxLayout

from src.config.menu_config_loader import MenuConfigLoader
from src.views.widgets.botao_padrao import BotaoPadrao
from src.views.widgets.titulo_janela import TituloJanela


class AjudaView(QWidget):
    sinal_voltar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__layout = QVBoxLayout()
        self.mostra_view()

    def mostra_view(self):
        titulo = TituloJanela("Controles")
        titulo.adicionar_ao_layout(self.__layout)

        #TBD

        botao_voltar = BotaoPadrao("Voltar")
        botao_voltar.clicked.connect(self.__voltar)
        botao_voltar.adicionar_ao_layout(self.__layout)

        self.setLayout(self.__layout)
        return self.__layout

    def __voltar(self):
        self.sinal_voltar.emit()
