class Invoice:
    def __init__(self):
        self.__Numero = ''
        self.__Descricao = ''
        self.__Comprado = 0
        self.__Preco = 0.0

    def getNumero(self) -> str:
        return self.__Numero

    def setNumero(self, numero:str):
        self.__Numero = numero

    def getDescricao(self) -> str:
        return self.__Descricao

    def setDescricao(self, descricao:str):
        self.__Descricao = descricao

    def getComprado(self) -> int:
        return self.__Comprado

    def setComprado(self, comprado:int):
        self.__Comprado = comprado

    def getPreco(self) -> float:
        return self.__Preco

    def setPreco(self, preco:float):
        self.__Preco = preco

    def __str__(self):
        return f"{self.getNumero()} - {self.getDescricao()}: {self.getPreco():.2f}\nQuantidade vendidadas: {self.getComprado()}"
