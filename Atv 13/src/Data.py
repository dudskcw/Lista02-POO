from datetime import datetime, timedelta

hoje = datetime.now()
class Data:
    def __init__(self):
        self.__Dia = hoje.day
        self.__Mes = hoje.month
        self.__Ano = hoje.year
        self.__Meses = [4, 6, 9, 11]
        self.__Bissexto = 0

    #Acessando variaveis
    def getDia(self) -> int:
        return self.__Dia

    def getMes(self) -> int:
        return self.__Mes

    def getAno(self) -> int:
        return self.__Ano

    def getMeses(self) -> int:
        return self.__Meses

    def getBissexto(self) -> int:
        return self.__Bissexto
    #Acessando variaveis

    def setDia(self, dia:int):
        if dia <= 0:
            print("Dia invalido")

        elif self.getMes() == 2 and self.__Bissexto == True and dia > 29:
            print("Dia invalido")
        
        elif self.getMes() == 2 and self.__Bissexto == False and dia > 28:
            print("Dia invalido")

        elif self.getMes() in self.getMeses() and dia > 30:
            print("Dia invalido")
        
        elif dia > 31:
            print("Dia invalido")

        else:
            self.__Dia = dia

    def setMes(self, mes:int):
        if mes <= 0 or mes > 12:
            print("Mes invalido")
        else:
            self.__Mes = mes

    def setAno(self, ano:int):
        if ano <=0:
            print("Ano invalido")
        else:
            self.__Ano = ano

        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
            self.__Bissexto = True

        else:
            self.__Bissexto = False

    def DiaSeguinte(self):
        hoje = datetime(self.getAno(), self.getMes(), self.getDia())
        proximo = hoje + timedelta(days = 1)

        self.setDia(proximo.day)
        self.setMes(proximo.month)
        self.setAno(proximo.year)
    
    def __str__(self) -> str:
        return f"{self.getDia()}/{self.getMes()}/{self.getAno()}"
    