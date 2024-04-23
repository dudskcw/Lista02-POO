class Funcionario:
    def __init__(self):
        self.__Nome = ""
        self.__Salario = 0.0

    #Acessando variavel
    def getNome(self) -> str:
        return self.__Nome

    def setNome(self, nome:str):
        self.__Nome = nome

    def getSalario(self) -> float:
        return self.__Salario

    def setSalario(self, salario:float):
        self.__Salario = salario
    #Acessando variavel

    def toString (self):
        print(f"Nome: {self.getNome()}\nSalario: {self.getSalario():.2f}")
    
