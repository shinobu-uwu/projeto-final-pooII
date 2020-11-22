from src.config.menu_config_loader import MenuConfigLoader
from PIL import Image
import PySimpleGUI as sg
import os
import io


class SelecaoFasesView:
    def __init__(self):
        self.__layout = []
        self.__config = MenuConfigLoader()

    def mostra_view(self):
        nome_imagens = sorted(f"{os.listdir(self.__config.diretorio_assets}/thumbnail fases"))
        imagens = [self.__get_image_data(f"{self.__config.diretorio_assets}/thumbnail fases/{nome}") for nome in nome_imagens]
        self.__layout = [
                            [sg.Text("Seleção de fases", size = self.__config.tamanho_titulo, font = self.__config.fonte_titulo, justification = "center")],
                            #Imagens de preview das fases
                            [sg.Image(data = imagens[i]) for i in range(3)],
                            [sg.Text()],#Preenchimento
                            [sg.Image(data = imagens[j]) for j in range(3, 6)],
                            [sg.Text()],
                            [sg.Button("Voltar", key = "voltar", size = self.__config.tamanho_botoes, font = self.__config.fonte_botoes)]
                        ]
        self.__window = sg.Window("Seleção de fases", self.__layout, element_justification = self.__config.element_justification, size = self.__config.tamanho_janela)
        return self.__layout

    def le_eventos(self):
        return self.__window.Read()

    def fechar(self):
        self.__window.close()

    def __get_image_data(self, f, maxsize = (320, 180)):
        #Converte imagem de outro diretório para um formato que o pysimplegui leia
        img = Image.open(f)
        img.thumbnail(maxsize)
        bio = io.BytesIO()
        img.save(bio, format = "PNG")
        del img
        return bio.getvalue()
