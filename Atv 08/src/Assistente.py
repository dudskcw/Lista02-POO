from src.Funcionario import Funcionario

class Assistente (Funcionario):
    def __init__(self):
        self.__Matricula = ""

    def getMatricula(self) -> str:
        return self.__Matricula

    def setMatricula(self, matricula:str):
        self.__Matricula = matricula
