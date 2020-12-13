import pygame_menu

from src.config.menu_pause_config_loader import MenuPauseConfigLoader
from src.game.interfaces.interface_menu_pause import IMenuPause


class MenuPause(IMenuPause):
    def __init__(self, screen):
        self.__config = MenuPauseConfigLoader()
        self.__screen = screen
        self.__tema = self.__criar_tema()
        self.__menu = pygame_menu.Menu(self.__screen.get_height(), self.__screen.get_width(), 'Jogo pausado', theme = self.__tema)
        self.__menu.add_button("Continuar", self.continuar)
        self.__menu.add_button("Menu principal", self.voltar_menu_principal)
        self.__menu.add_button("Sair", self.sair_do_jogo)

    def show(self, screen):
        self.__menu.enable()
        self.__menu.mainloop(screen)

    def continuar(self):
        self.hide()

    def hide(self):
        self.__menu.disable()

    def sair_do_jogo(self):
        exit()

    def voltar_menu_principal(self):
        pass

    def __criar_tema(self):
        tema = pygame_menu.themes.Theme(background_color = self.__config.cor_fundo,
                                        title_font = self.__config.fonte_titulo,
                                        title_font_size = self.__config.tamanho_fonte_titulo,
                                        title_font_color = self.__config.cor_fonte_titulo,
                                        title_background_color = self.__config.cor_fundo_titulo,
                                        title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE,
                                        menubar_close_button = False,
                                        widget_alignment = pygame_menu.locals.ALIGN_CENTER,
                                        widget_font = self.__config.fonte_botoes,
                                        widget_font_size = self.__config.tamanho_fonte_botoes,
                                        widget_font_color = self.__config.cor_fonte_botoes,
                                        widget_margin = self.__config.espacamento
                                        )
        return tema
