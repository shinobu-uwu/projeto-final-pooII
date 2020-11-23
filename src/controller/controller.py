import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor, QImage

from src.views.main_window import MainWindow
from src.views.main_menu_view import MainMenuView
from src.views.selecao_fases_view import SelecaoFasesView
from src.views.ajuda_view import AjudaView
from src.config.menu_config_loader import MenuConfigLoader


class Controller:
    def __init__(self):
        self.__config = MenuConfigLoader()
        self.__app = QApplication(sys.argv)
        self.__window = MainWindow()
        self.__window.setFixedSize(self.__config.width_janela, self.__config.height_janela)
        self.__central_widget = MainMenuView()
        self.set_central_widget()

    def set_central_widget(self):
        self.__window.setCentralWidget(self.__central_widget)

    def comeca(self):
        self.__central_widget.sinal_jogar.connect(self.jogar)
        self.__central_widget.sinal_ajuda.connect(self.ajuda)
        self.__window.show()
        sys.exit(self.__app.exec_())

    def jogar(self):
        self.__central_widget = SelecaoFasesView()
        self.set_central_widget()
        self.__central_widget.sinal_voltar.connect(self.voltar)

    def ajuda(self):
        self.__central_widget = AjudaView()
        self.__central_widget.sinal_voltar.connect(self.voltar)
        self.set_central_widget()

    def voltar(self):
        self.__central_widget = MainMenuView()
        self.__central_widget.sinal_jogar.connect(self.jogar)
        self.__central_widget.sinal_ajuda.connect(self.ajuda)
        self.set_central_widget()
