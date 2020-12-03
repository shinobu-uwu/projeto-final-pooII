import datetime

class Score:
    def __init__(self, tempo, fase, jogador):
        self.__tempo = tempo
        self.__fase = fase
        self.__jogador = jogador
        self.__data = datetime.datetime.now()


    def to_dict(self):
        score = {"tempo": str(self.__tempo), "fase": str(self.__fase), "data": str(self.__data)}
        return score

    @property
    def jogador(self):
        return self.__jogador
