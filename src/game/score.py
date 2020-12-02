class Score:
    def __init__(self, tempo, fase, jogador):
        self.__tempo = tempo
        self.__fase = fase
        self.__jogador = jogador


    def to_dict(self):
        score = {"tempo": str(self.__tempo), "fase": str(self.__fase)}
        return score

    @property
    def jogador(self):
        return self.__jogador
