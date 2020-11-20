import PySimpleGUI as sg
from src.config.menu_config_loader import MenuConfigLoader


class AjudaView:
    def __init__(self):
        self.__layout = []
        self.__config = MenuConfigLoader()

    def mostra_view(self):
        self.__layout = [
                            [sg.Text("Controles", size = self.__config.tamanho_titulo, font = self.__config.fonte_titulo, justification = "center")],
                            [sg.Text()],#A ser definido
                            [sg.Button("Voltar", size = self.__config.tamanho_botoes, font = self.__config.fonte_botoes, key = "voltar")]
                        ]
        self.__window = sg.Window("Ajuda", self.__layout, element_justification = self.__config.element_justification, size = self.__config.tamanho_janela)
        return self.__layout

    def le_eventos(self):
        return self.__window.read()

    def fechar(self):
        self.__window.close()
