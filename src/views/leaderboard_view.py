from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from src.views.widgets.botao_padrao import BotaoPadrao
from src.views.widgets.scrollable_leaderboard import ScrollableLeaderboard
from src.views.widgets.titulo_janela import TituloJanela


class LeaderboardView(QWidget):
    sinal_voltar = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__layout = QVBoxLayout()
        self.mostra_view()

    def mostra_view(self):
        titulo = TituloJanela("Melhores jogador")
        titulo.adicionar_ao_layout(self.__layout)

        leaderboard = ScrollableLeaderboard(["Pog"])
        leaderboard.adicionar_item("Kappa")
        leaderboard.adicionar_ao_layout(self.__layout)

        botao_voltar = BotaoPadrao("Voltar")
        botao_voltar.clicked.connect(self.__voltar)
        botao_voltar.adicionar_ao_layout(self.__layout)

        self.setLayout(self.__layout)
        return self.__layout

    def __voltar(self):
        self.sinal_voltar.emit()
