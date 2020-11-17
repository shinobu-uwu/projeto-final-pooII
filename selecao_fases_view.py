from config_loader import ConfigLoader
import PySimpleGUIQt as sg


class SelecaoFasesView:
    def __init__(self):
        self.__layout = []
        self.__config_loader = ConfigLoader()

    def mostra_view(self):
        self.__layout = [
                            [sg.Text("Seleção de fases", size = self.__config_loader.tamanho_titulo, font = self.__config_loader.fonte_titulo, justification = "center")],
                            #Imagens de preview das fases
                            [sg.Image(), sg.Text(), sg.Image(), sg.Text(), sg.Image()],
                            [sg.Image(), sg.Text(), sg.Image(), sg.Text(), sg.Image()]
                        ]
        self.__window = sg.Window("Seleção de fases", self.__layout, element_justification = "center")
        return self.__layout

    def le_eventos(self):
        return self.__window.Read()
