class Retangulo:
    def __init__(self, largura:float, altura:float):
        self.__Larg = largura
        self.__Alt = altura

    def getLarg (self) -> str:
        return self.__Larg

    def getAlt (self) -> str:
        return self.__Alt

    def Area(self):
        self.__Area = self.__Alt * self.__Larg

    def Perimetro(self):
        self.__Perimetro = (self.__Alt*2) + (self.__Larg * 2)

    def __str__(self) -> str:
        return f"Perimetro: {self.__Perimetro:.2f}\nArea: {self.__Area:.2f}"
