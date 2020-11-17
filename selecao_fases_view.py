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
                            [sg.Image("fase1.jpg"), sg.Text(), sg.Image("fase1.jpg"), sg.Text(), sg.Image("fase1.jpg")],
                            [sg.Text()],#Preenchimento
                            [sg.Image("fase1.jpg"), sg.Text(), sg.Image("fase1.jpg"), sg.Text(), sg.Image("fase1.jpg")],
                            [sg.Text()],
                            [sg.Button("Voltar", key = "voltar", size = self.__config_loader.tamanho_botoes, font = self.__config_loader.fonte_botoes)]
                        ]
        self.__window = sg.Window("Seleção de fases", self.__layout, element_justification = "center", size = [1280, 720])
        return self.__layout

    def le_eventos(self):
        return self.__window.Read()

    def fechar(self):
        self.__window.close()
