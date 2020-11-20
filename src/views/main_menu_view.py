import json
import PySimpleGUI as sg
from src.config.menu_config_loader import MenuConfigLoader


class MainMenuView:
    def __init__(self):
        self.__config = MenuConfigLoader()
        self.__tema = sg.theme("DarkAmber")
        self.__layout = []

    def mostra_view(self):
        self.__layout = [
                            [sg.Text("Algum dia saberemos!", size = self.__config.tamanho_titulo, font = self.__config.fonte_titulo, justification = "center")],
                            [sg.Text()],#Preenchimento entre os elementos, pretendo trocar esse primeiro com a imagem do personagem no futuro
                            [sg.Button("Jogar", size = self.__config.tamanho_botoes, font = self.__config.fonte_botoes, key = "jogar")],
                            [sg.Text()],
                            [sg.Button("Ajuda", size = self.__config.tamanho_botoes, font = self.__config.fonte_botoes, key = "ajuda")],
                            [sg.Text()],
                            [sg.Button("Sair", size = self.__config.tamanho_botoes, font = self.__config.fonte_botoes, key = "sair")]
                        ]

        self.__window = sg.Window("TBD", self.__layout, element_justification = self.__config.element_justification, size = self.__config.tamanho_janela)
        return self.__layout

    def le_eventos(self):
        return self.__window.Read()

    def fechar(self):
        self.__window.close()

    def maximiza(self):
        self.__window.Maximize()
