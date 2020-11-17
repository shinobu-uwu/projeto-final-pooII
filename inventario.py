class Inventario:
    def __init__(self):
        self.__itens = []
        self.__capacidade = 10#Não definido

    @property
    def itens(self):
        return self.__itens

    @property
    def capacidade(self):
        return self.__capacidade
