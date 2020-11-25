from abc import ABC, abstractmethod


class IConfigLoader(ABC):
    @abstractmethod
    def __init__(self):
        pass

    #Esse load tá dando problema, acho que precisa tirar o __
    #@abstractmethod
    #def __load(self):
       # pass
