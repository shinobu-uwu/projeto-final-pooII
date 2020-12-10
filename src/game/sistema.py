from src.game.interfaces.interface_sistema import ISistema
from src.game.bloco_cenario import BlocoCenario
from src.game.cenario import Cenario
from src.game.jogo import Jogo
from src.game.jogador import Jogador
from src.game.machado import Machado
from src.game.pa import Pa
from src.game.picareta import Picareta

class Sistema (ISistema):
    def __init__(self, estado_jogo: str):
        self.__estado_jogo = estado_jogo

    def selecionar_fase(self, numero_fase):

        #tam = [22,16]
        #loop para fazer "o chão"
        x = 0
        lista_blocos = []
        while x < 12000:

            bloco = BlocoCenario(1,[x, 500])
            lista_blocos.append(bloco)

            x += 44

        y = 400

        while y > 100:
            bloco = BlocoCenario(2,[800, y])
            lista_blocos.append(bloco)
            y -= 32
            
        ##bloco = BlocoCenario(2, [700, 400])
        #bloco2 = BlocoCenario(2, 2, [800, 460])
        ##bloco3 = BlocoCenario(2, [640, 350])
        ##bloco4 = BlocoCenario(2, [690, 370])
        ##bloco5 = BlocoCenario(2,  [620, 390])
        
        #lista_blocos.append(bloco)
        #lista_blocos.append(bloco2)
        ##lista_blocos.append(bloco3)
        ##lista_blocos.append(bloco4)
        ##lista_blocos.append(bloco5)

        cenario = Cenario(1, "mapa1", 300)
        #cenario = Cenario(1, [bloco3], 300)

        jogador = Jogador([300, 360])
        machado = Machado(5,5)
        pa = Pa(5,5)
        picareta = Picareta(5,5)
        jogador.adicionar_item(machado)
        jogador.adicionar_item(pa)
        jogador.adicionar_item(picareta)
        jogo = Jogo(2, 3, jogador, cenario, True)


    def abrir_opcoes(self):
        pass

    def fechar(self):
        pass

    @property
    def estado_jogo(self):
        return self.__estado_jogo