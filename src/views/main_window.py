from PyQt5.Qt import QPixmap, QPainter
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from src.config.menu_config_loader import MenuConfigLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__config = MenuConfigLoader()
        #Configurações da janela
        self.setFixedSize(self.__config.width_janela, self.__config.height_janela)
        self.setWindowIcon(QIcon(f"{self.__config.diretorio_assets}/icon/icon.png"))

    #Reescrever o paintEvent da classe QMainWindow, para a
    #janela ser criada com o fundo que queremos
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap(f"{self.__config.diretorio_assets}/menu principal/fundo.png"))
        super().paintEvent(event)