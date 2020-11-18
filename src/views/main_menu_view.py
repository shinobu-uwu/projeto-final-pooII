import json
import PySimpleGUIQt as sg
from src.config.config_loader import ConfigLoader


class MainMenu:
    def __init__(self):
        self.__config_loader = ConfigLoader()
        self.__layout = []

    def mostra_view(self):
        self.__layout = [
                            [sg.Text("Algum dia saberemos!", size = self.__config_loader.tamanho_titulo, font = self.__config_loader.fonte_titulo, justification = "center")],
                            [sg.Text()],#Preenchimento entre os elementos, pretendo trocar esse primeiro com a imagem do personagem no futuro
                            [sg.Button("Jogar", size = self.__config_loader.tamanho_botoes, font = self.__config_loader.fonte_botoes, key = "jogar")],
                            [sg.Text()],
                            [sg.Button("Ajuda", size = self.__config_loader.tamanho_botoes, font = self.__config_loader.fonte_botoes, key = "ajuda")],
                            [sg.Text()],
                            [sg.Button("Sair", size = self.__config_loader.tamanho_botoes, font = self.__config_loader.fonte_botoes, key = "sair")]
                        ]

        self.__window = sg.Window("TBD", self.__layout, element_justification = self.__config_loader.element_justification, size = self.__config_loader.tamanho_janela)
        return self.__layout

    def le_eventos(self):
        return self.__window.Read()

    def fechar(self):
        self.__window.close()
