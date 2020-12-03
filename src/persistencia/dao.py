import json
import os

from src.game.score import Score


class DAO:
    def __init__(self):
        self.__datasource = os.path.join(os.getenv("PYTHONPATH"), "scores/scores.json")
        self.__cache = {}
        self.__load()

    def __dump(self):
        f = open(self.__datasource, 'w')
        json.dump(self.__cache, f, indent = 4)

   def __load(self):
        try:
            f = open(self.__datasource, 'r')
        except FileNotFoundError:
           self.__dump()
            self.__load()
        else:
            self.__cache = json.load(f)

    def add(self, score: Score):
        if isinstance(score, Score):
            if score.jogador not in self.__cache.keys():
               self.__cache[score.jogador] = {}
                for i in range(1, 7):
                    self.__cache[score.jogador][f"fase{i}"] = []
            self.__cache[score.jogador][f"fase{score.fase}"].append(score.to_dict())
           self.__dump()

    def melhor_tempo_fase(self, fase):
       #pode ser qualquer número inicial, desde que ele seja suficientemente grande
       minimo = 100000
        for key in self.__cache.keys():
            candidato_a_minimo = min(self.__cache[key][f"fase{fase}"])
            if candidato_a_minimo < minimo:
               jogador = key
                minimo = candidato_a_minimo
        return Score(minimo, fase, jogador)

    @property
    def cache(self):
        return self.__cache
