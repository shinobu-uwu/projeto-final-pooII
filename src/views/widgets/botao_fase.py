from PyQt5.QtWidgets import QPushButton

from src.config.menu_config_loader import MenuConfigLoader


class BotaoFase(QPushButton):
    def __init__(self, imagem):
        super().__init__()
        self.__config = MenuConfigLoader()
        self.setFixedSize(self.__config.width_fases, self.__config.height_fases)
        self.setStyleSheet("BotaoFase{ " +
                           f"background-image: url({self.__config.diretorio_assets}/thumbnail fases/{imagem}); border-style: outset; border-color: green; border-radius: 20px; border-width: 6px;" +
                           "} BotaoFase:hover { border-color: #00A200; } BotaoFase:pressed { border-color: #007000 }")
