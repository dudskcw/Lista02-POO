class Funcionario:
    def __init__(self):
        self.__Nome = ""
        self.__Salario = 0.0
        self.__Adicional = 0.0
        self.__SalarioAnual = 0.0

    #Acessando variavel
    def getNome(self) -> str:
        return self.__Nome

    def setNome(self, nome:str):
        self.__Nome = nome

    def getSalario(self) -> float:
        return self.__Salario

    def setSalario(self, salario:float):
        self.__Salario = salario

    def getAdicional(self) -> float:
        return self.__Adicional

    def setAdicional(self, adicional:float):
        self.__Adicional = adicional

    def getAnual(self) -> float:
        return self.__SalarioAnual

    def setAnual(self, anual:float):
        self.__SalarioAnual = anual
    #Acessando variavel

    def addAumento (self) -> float:
        novosalario = self.getSalario()
        novosalario =  self.getSalario() + (self.getSalario() * self.__Adicional)
        self.setSalario(novosalario)
    
    def ganhoAnual (self) -> float:
        self.__SalarioAnual = self.__Salario * 13

    def exibeDados (self):
        print(f"Nome: {self.getNome()}\nSalario: {self.getSalario():.2f}")
        print(f"Aumento: {self.getAdicional()*100}%\nGanho Anual: {self.getAnual():.2f}")
