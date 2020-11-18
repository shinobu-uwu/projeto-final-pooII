from src.config.config_loader import ConfigLoader
from PIL import Image
import PySimpleGUIQt as sg
import os
import io


class SelecaoFasesView:
    def __init__(self):
        self.__layout = []
        self.__config_loader = ConfigLoader()

    def mostra_view(self):
        nome_imagens = sorted(os.listdir(f"{os.getcwd()}/assets/thumbnail fases"))
        imagens = [self.__get_image_data(f"{os.getcwd()}/assets/thumbnail fases/{nome}") for nome in nome_imagens]
        self.__layout = [
                            [sg.Text("Seleção de fases", size = self.__config_loader.tamanho_titulo, font = self.__config_loader.fonte_titulo, justification = "center")],
                            #Imagens de preview das fases
                            [sg.Image(data = imagens[i], key = f"fase{i}") for i in range(3)],
                            [sg.Text()],#Preenchimento
                            [sg.Image(data = imagens[j], key = f"fase{j}") for j in range(3, 6)],
                            [sg.Text()],
                            [sg.Button("Voltar", key = "voltar", size = self.__config_loader.tamanho_botoes, font = self.__config_loader.fonte_botoes)]
                        ]
        self.__window = sg.Window("Seleção de fases", self.__layout, element_justification = "center", size = self.__config_loader.tamanho_janela)
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
        img.save(bio, format = "JPEG")
        del img
        return bio.getvalue()
