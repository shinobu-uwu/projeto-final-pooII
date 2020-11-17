import PySimpleGUIQt as sg


class AjudaView:
    def __init__(self):
        self.__layout = []
        self.__config_loader = ConfigLoader

    def mostra_view(self):
        self.__layout = [
                            [sg.Text()]
                        ]
