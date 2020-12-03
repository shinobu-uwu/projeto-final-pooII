from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget

from src.config.menu_config_loader import MenuConfigLoader


class ScrollableLeaderboard(QListWidget):
    def __init__(self, itens):
        super().__init__()
        self.__config = MenuConfigLoader()
        for item in itens:
            self.addItem(item)
        self.setFixedSize(self.__config.width_leaderboard, self.__config.height_leaderboard)

    def adicionar_item(self, item):
        self.addItem(item)

    def adicionar_ao_layout(self, layout):
        layout.addWidget(self, alignment = Qt.AlignCenter)
