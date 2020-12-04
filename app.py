import os
#Para os imports funcionarem corretamente é necessário exportar a env variable PYTHONPATH
os.environ["PYTHONPATH"] = os.path.abspath(os.path.dirname(__file__))

from src.controller.controller import Controller
from src.game.bloco_cenario import BlocoCenario
from src.game.cenario import Cenario
from src.game.jogo import Jogo
from src.game.jogador import Jogador


bloco = BlocoCenario(2, 2, [700, 400])
bloco2 = BlocoCenario(2, 2, [100, 400])
bloco3 = BlocoCenario(2, 2, [640, 300])

#tam = [22,16]
#loop para fazer "o chão"
x = 0
lista_blocos = []

while x < 1200:
    bloco = BlocoCenario(2, 2, [x, 500])
    lista_blocos.append(bloco)
    x += 22

lista_blocos.append(bloco)
lista_blocos.append(bloco2)
lista_blocos.append(bloco3)

cenario = Cenario(1, lista_blocos, 300)
#cenario = Cenario(1, [bloco3], 300)

#jogador = Jogador([300, 360])
#jogo = Jogo(2, 3, jogador, cenario, True)

a = Controller()
a.comeca()
