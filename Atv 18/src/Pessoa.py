from .Universidade import Universidade

class Pessoa:
    def __init__(self):
        self.__Nome = ""
    
    def getNome(self) -> str:
        return self.__Nome

    def setNome(self, nome:str):
        self.__Nome = nome

    def __str__(self) -> str:
        return self.__Nome


