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
            if score.jogador in self.__cache.keys():
                self.__cache[score.jogador].append(score.to_dict())
            else:
                self.__cache[score.jogador] = []
                self.__cache[score.jogador].append(score.to_dict())
            self.__dump()

    @property
    def cache(self):
        return self.__cache
