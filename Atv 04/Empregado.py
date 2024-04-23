class Empregado:
    def __init__(self) -> None:
        self.__Nome = ""
        self.__Sobrenome = ""
        self.__Salario:float = 0.0

    def getNome (self) -> str:
        return self.__Nome

    def setNome (self, nome:str) -> None:
        self.__Nome = nome

    def getSobrenome (self) -> str:
        return self.__Sobrenome
    
    def setSobrenomeome (self, sobrenome:str) -> None:
        self.__Sobrenome = sobrenome

    def getSalario (self) -> float:
        return self.__Salario
    
    def setSalario (self, salario:float) -> None:
        self.__Salario = salario

    def __str__(self) -> str:
        return f"Salario anual de {self.getNome()} {self.getSobrenome()}: {self.getSalario()*13:.2f}"

    
    
        