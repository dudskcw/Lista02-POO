from src.Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self):
        self.__Depatarmento = ""

    def getDepatarmento(self) -> str:
        return self.__Depatarmento

    def setDepartamento(self, depatarmento:str):
        self.__Depatarmento = depatarmento

    def toString (self):
        print(f"Nome: {self.getNome()}\nSalario: {self.getSalario():.2f}\nDepartamento: {self.getDepatarmento()}")
