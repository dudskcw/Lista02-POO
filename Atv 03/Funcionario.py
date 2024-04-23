class Funcionario:
    def __init__(self, nome:str, salario:float, cargo:str, diames:int):
        self.__Nome = nome
        self.__Salario = salario
        self.__Cargo = cargo
        self.__Diames = diames

    def getNome(self) -> str:
        return self.__Nome

    def getSalario(self) -> float:
        return self.__Salario

    def getCargo(self) -> str:
        return self.__Cargo

    def getDia(self) -> int:
        return self.__Diames

    def calculosalario(self):
        if self.__Salario <= 2129.70:
            self.__Salario -= (self.__Salario * 0.075) + (self.__Salario * 0.08) + (self.__Salario * 0.075)

        else:
            self.__Salario -= (self.__Salario * 0.075) + (self.__Salario * 0.08)

    def calculoTransporte(self):
        transporte = 8.00
        self.__Salario += (transporte * self.__Diames) - (self.__Salario * 0.06)
        print(f"Vale-Transporte: {self.__Diames * 8.00:.2f}")

    def calculoRefeicao(self):
        refeicao = 15.00
        self.__Salario += refeicao * self.__Diames
        print(f"Vale-alimentação: {self.__Diames * 15.00:.2f}")

    def __str__(self) -> str:
        return f"Funcionario: {self.__Nome}\nSalario: {self.__Salario:.2f}\nCargo: {self.__Cargo}"
    
        
        
