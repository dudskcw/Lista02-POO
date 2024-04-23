class Funcionario:
    def __init__(self):
        self.__Nome = ""
        self.__Sobrenome = ""
        self.__Salario = 0.0
        self.__Adicional = 0.0

    #Acessando variavel
    def getNome(self) -> str:
        return self.__Nome

    def setNome(self, nome:str):
        self.__Nome = nome

    def getSobenome(self) -> str:
        return self.__Sobrenome

    def setSobrenome(self, sobrenome:str):
        self.__Sobrenome = sobrenome

    def getSalario(self) -> float:
        return self.__Salario

    def setSalario(self, salario:float):
        if salario < 0:
            self.__Salario = 0.0

        else:
            self.__Salario = salario
            
    def getAdicional(self) -> float:
        return self.__Adicional

    def setAdicional(self, adicional:float):
        self.__Adicional = adicional
        
    #Acessando variavel
    def addAumento (self) -> float:
        novosalario = self.getSalario()
        novosalario =  self.getSalario() + (self.getSalario() * self.getAdicional())
        self.setSalario(novosalario)

    def __str__(self) -> str:
        return f"Nome: {self.getNome()} {self.getSobenome()}\nSalario: {self.getSalario():.2f}"

   
