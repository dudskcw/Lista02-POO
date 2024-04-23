class ContaBancaria: 
    def __init__(self):
        self.__Nome = ""
        self.__Numero = ""
        self.__Saldo = 0.0

    #Ascessar variavel privada
    def getNome(self)->str:
        return self.__Nome
    
    def setNome(self, nome):
      self.__Nome = nome

    def getNum(self)->str:
        return self.__Numero
    
    def setNum(self, numero):
      self.__Numero = numero

    def getSaldo(self)->float:
        return self.__Saldo
    
    def setSaldo(self, Saldo):
      self.__Saldo = Saldo

    #Ascessar variavel privada

    def depositar(self, valor:float):
        self.__Valor = valor
        self.__Saldo += self.__Valor
    
    def sacar(self, valor:float):
        self.__Valor = valor

        if self.__Valor > self.__Saldo:
            print("Você nâo pode sacar esse valor, por favor, tente outro")

        else:
            self.__Saldo -= self.__Valor

    def __str__(self) -> str:
      return f"Cliente: {self.__Nome}\nConta: {self.__Numero}\nSaldo: {self.__Saldo:.2f}"
