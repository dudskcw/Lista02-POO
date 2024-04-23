from src.Funcionario import Funcionario

class Vendedor(Funcionario):
    def __init__(self):
        self.__Comissao = 0.0
        self.__NovoSalario = 0.0

    def getComissao(self) -> float:
        return self.__Comissao

    def setComicao(self, comissao:str):
        self.__Comissao = comissao 

    def getNovoSalario(self) -> float:
        return self.__NovoSalario

    def CalcularSalario(self):
        self.__NovoSalario = self.getSalario() + self.getSalario()*self.__Comissao


    def toString (self):
        print(f"Nome: {self.getNome()}\nSalario s/ comissão: {self.getSalario():.2f}")
        print(f"Porcentual da comissão: {self.getComissao() * 100 }\nSalario c/ comissão: {self.getNovoSalario():.2f}\n")
