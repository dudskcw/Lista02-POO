class Data:
    def __init__(self):
        self.__Dia = 0
        self.__Mes = 0
        self.__Ano = 0

    def getDia(self) -> int:
        return self.__Dia

    def getMes(self) -> int:
        return self.__Mes

    def getAno(self) -> int:
        return self.__Ano

    def setDia(self, dia):
        self.__Dia = dia

    def setMes(self, mes):
        self.__Mes = mes

    def setAno(self, ano):
        self.__Ano = ano

    def Display(self) -> str:
        print(f"{self.getDia()}/{self.getMes()}/{self.getAno()}")
