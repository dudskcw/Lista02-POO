class Ingresso:
    def __init__(self):
        self.__Valor = 0.0

    def getValor(self) -> float:
        return self.__Valor

    def setValor(self, valor:float):
        self.__Valor = valor

    def ImprimirValor(self):
        print(f"Valor: {self.getValor()}")

class IngressoVip(Ingresso):
    def __init__(self):
        self.__Adicional = 0.0

    def getAdicional(self) -> float:
        return self.__Adicional

    def setAdicional(self, adicional:float):
        self.__Adicional = adicional

    def ImprimirValor2(self):
        novovalor = self.getValor()
        novovalor +=self.__Adicional
        self.setValor(novovalor)
        print(f"Valor: {self.getValor()}")
        
