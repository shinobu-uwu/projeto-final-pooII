from src.controller.controller import Controller
import os

#Para os imports funcionarem corretamente é necessário exportar a env variable PYTHONPATH
os.environ["PYTHONPATH"] = os.path.abspath(os.path.dirname(__file__))
a = Controller()
a.comeca()
