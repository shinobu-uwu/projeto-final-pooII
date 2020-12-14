from src.config.jogo_config_loader import JogoConfigLoader
from src.game.bloco_cenario import BlocoCenario
from src.game.cenario import Cenario
from src.game.interfaces.interface_sistema import ISistema
from src.game.jogo import Jogo
from src.game.jogador import Jogador
from src.game.machado import Machado
from src.game.pa import Pa
from src.game.picareta import Picareta


class Sistema (ISistema):
    def __init__(self, estado_jogo):
        self.__estado_jogo = estado_jogo
        self.__config = JogoConfigLoader()

    def selecionar_fase(self, numero_fase):
        cenario = Cenario(numero_fase + 1)

        jogador = Jogador(self.__config.obter_posicao_inicial(numero_fase + 1))
        machado = Machado(5,5)
        pa = Pa(5,5)
        picareta = Picareta(5,5)
        jogador.adicionar_item(machado)
        jogador.adicionar_item(pa)
        jogador.adicionar_item(picareta)
        jogo = Jogo(2, 3, jogador, cenario, True)
        jogo.inicia_loop()


    def abrir_opcoes(self):
        pass

    def fechar(self):
        pass

    @property
    def estado_jogo(self):
        return self.__estado_jogo
