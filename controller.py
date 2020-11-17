import PySimpleGUIQt as sg
from main_menu import MainMenu
from selecao_fases_view import SelecaoFasesView


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
                self.__window.fechar()
                self.selecionar_fase()
                self.__window.mostra_view()

    def selecionar_fase(self):
        window = SelecaoFasesView()
        window.mostra_view()
        while True:
            event, values = window.le_eventos()
            if event == sg.WIN_CLOSED:
                break

            elif event == "voltar":
                window.fechar()
                break
