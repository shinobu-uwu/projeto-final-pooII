import sys
from PyQt5.QtWidgets import QApplication

from src.config.menu_config_loader import MenuConfigLoader
from src.game.sistema import Sistema
from src.persistencia.dao import DAO
from src.views.ajuda_view import AjudaView
from src.views.leaderboard_view import LeaderboardView
from src.views.main_menu_view import MainMenuView
from src.views.main_window import MainWindow
from src.views.selecao_fases_view import SelecaoFasesView


class Controller:
    def __init__(self):
        self.__sistema = Sistema()
        self.__config = MenuConfigLoader()
        self.__dao = DAO()
        self.__app = QApplication(sys.argv)
        self.__window = MainWindow()
        self.__central_widget = MainMenuView()
        self.set_central_widget()

    def set_central_widget(self):
        self.__window.setCentralWidget(self.__central_widget)

    def comeca(self):
        self.__central_widget.sinal_jogar.connect(self.jogar)
        self.__central_widget.sinal_leaderboard.connect(self.leaderboard)
        self.__central_widget.sinal_ajuda.connect(self.ajuda)
        self.__window.show()
        sys.exit(self.__app.exec_())

    def jogar(self):
        self.__central_widget = SelecaoFasesView()
        self.set_central_widget()
        self.__central_widget.sinal_voltar.connect(self.voltar)
        self.__central_widget.sinal_fase.connect(self.selecionar_fase)

    def leaderboard(self):
        self.__dao.atualizar()
        scores = []
        for i in range(1, 7):
            try:
                scores.append(self.__dao.melhor_tempo_fase(i).to_string())
            #Ignora se for uma lista vazia
            except ValueError as e:
                print (e)
                pass
        self.__central_widget = LeaderboardView(scores)
        self.set_central_widget()
        self.__central_widget.sinal_voltar.connect(self.voltar)

    def ajuda(self):
        self.__central_widget = AjudaView()
        self.__central_widget.sinal_voltar.connect(self.voltar)
        self.set_central_widget()

    def voltar(self):
        self.__central_widget = MainMenuView()
        self.__central_widget.sinal_jogar.connect(self.jogar)
        self.__central_widget.sinal_leaderboard.connect(self.leaderboard)
        self.__central_widget.sinal_ajuda.connect(self.ajuda)
        self.set_central_widget()

    def selecionar_fase(self, nome, i):
        self.__window.hide()
        self.__sistema.selecionar_fase(nome, i)
        self.__window.show()
