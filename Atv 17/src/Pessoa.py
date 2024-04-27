from .Universidade import Universidade

class Pessoa:
    def __init__(self):
        self.__Nome = ""
        self.__Nascimento = ""
        self.__Universidade = ""
    
    def getNome(self) -> str:
        return self.__Nome

    def setNome(self, nome:str):
        self.__Nome = nome

    def getNascimento(self) -> str:
        return self.__Nascimento

    def setNascimento(self, nascimento):
        self.__Nascimento = nascimento

    def getUnversidade(self) -> str:
        return self.__Universidade

    def setUniversidade(self, instituicao:str):
        self.__Universidade = instituicao

    def __str__ (self) -> str:
        return f"{self.getNome()} - {self.getUnversidade()}"

