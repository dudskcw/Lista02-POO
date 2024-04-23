class Bomba:
    def __init__(self):
        self.__Valor = 0.0
        self.__Tipo = ""
        self.__Quant = 100.00

    #Acessando variaveis
    def getValor(self) -> float:
        return self.__Valor

    def setValor (self, valor:float):
        self.__Valor = valor

    def getTipo(self) -> str:
        return self.__Tipo

    def setTipo(self, tipo:str):
        self.__Tipo = tipo

    def getQuant(self) -> float:
        return self.__Quant

    def setQuant(self, quant:float):
        self.__Quant = quant
    #Acessando variaveis

    def AbastecerporValor(self, abastecimento:float):
        self.Abastecimento = abastecimento
        self.__Litros = self.Abastecimento/self.getValor()
        
        novaquant = self.getQuant() - self.__Litros
        self.setQuant(novaquant)
        print(f"{self.getQuant():.2f}")

        print(f"Litros: {self.__Litros:.2f}")

    def AbastecerporLitro(self, abastecimento:float):
        self.Abastecimento = abastecimento
        self.__APagar = self.Abastecimento * self.getValor()
        
        novaquant = self.getQuant() - self.Abastecimento
        self.setQuant(novaquant)
        print(f"{self.getQuant():.2f}")

        print(f"Valor: {self.__APagar:.2f}")

    def MudarValor(self, valor:float):
        self.setValor(valor)

    
        

 
