import PySimpleGUIQt as sg
from main_menu import MainMenu


class Controller:
    def __init__(self):
        self.__window = MainMenu()

    def comeca(self):
        self.__window.mostra_view()
        while True:
            event, values = self.__window.le_eventos()
            if event == sg.WIN_CLOSED:
                break

            elif event == "jogar":
                print("funciona")
