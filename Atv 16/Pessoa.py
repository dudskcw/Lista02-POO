from datetime import datetime
hoje = datetime.now()
class Pessoa:    
    def __init__(self):
        self.__Nome = ""
        self.__Dia = 0
        self.__Mes = 0
        self.__Ano = 0
        self.__Idade = 0
        self.__Meses = [4, 6, 9, 11]
        self.__Bissexto = 0

    #Acessando variaveis
    def getNome(self) -> str:
        return self.__Nome

    def setNome(self, nome:str):
        self.__Nome = nome

    def getIdade(self) -> int:
        return self.__Idade

    def setIdade(self, idade:int):
        self.__Idade = idade

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

    def CaucularIdade(self):
        nascimento = datetime(self.getAno(), self.getMes(), self.getDia())
        id = hoje - nascimento
        self.setIdade(id.days//365)

    def informaIdade(self) -> str:
        print(f"Idade: {self.getIdade()}")

    def informaNome(self):
        print(f"Nome: {self.getNome()}")