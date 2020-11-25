import os
#Para os imports funcionarem corretamente é necessário exportar a env variable PYTHONPATH
os.environ["PYTHONPATH"] = os.path.abspath(os.path.dirname(__file__))

from src.controller.controller import Controller
from src.game.machado import Machado
a = Machado(5,5)
a = Controller()
a.comeca()
