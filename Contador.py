class Contador:
    def __init__(self, valorLimite = None, valorInicial = 0, valorIncremento = 1):

        self.__valorInicial = valorInicial
        self.__valorIncremento = valorIncremento
        self.__valorLimite = valorLimite
        pass    

    def getValorInicial(self):
        return self.__valorInicial

    def getValorIncremento(self):
        return self.__valorIncremento

    def getValorLimite(self):
        return self.__valorLimite
    