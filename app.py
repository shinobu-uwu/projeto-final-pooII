import os
#Para os imports funcionarem corretamente é necessário exportar a env variable PYTHONPATH
os.environ["PYTHONPATH"] = os.path.abspath(os.path.dirname(__file__))

from src.controller.controller import Controller
from src.game.jogo import Jogo
from src.game.jogador import Jogador

jogador = Jogador(2, [0, 0])
jogo = Jogo(2, 3, jogador, 3, True)

#a = Controller()
#a.comeca()
