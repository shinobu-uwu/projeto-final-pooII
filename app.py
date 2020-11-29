import os
#Para os imports funcionarem corretamente é necessário exportar a env variable PYTHONPATH
os.environ["PYTHONPATH"] = os.path.abspath(os.path.dirname(__file__))

from src.controller.controller import Controller
from src.game.bloco_cenario import BlocoCenario
from src.game.cenario import Cenario
from src.game.jogo import Jogo
from src.game.jogador import Jogador


bloco = BlocoCenario(2, 3, [640, 360])
cenario = Cenario(1, [bloco], 300)

jogador = Jogador([0, 600])
jogo = Jogo(2, 3, jogador, cenario, True)

#a = Controller()
#a.comeca()
