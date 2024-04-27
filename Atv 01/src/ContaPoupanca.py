from src.ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self):
        self.__Rendimento = 0.0
    
    def getRend(self)->float:
        return self.__Rendimento
    
    def setRend(self, redimento:float):
        self.__Rendimento = redimento

    def calcularNovoSaldo(self):
      NovoSaldo = self.getSaldo()
      
      NovoSaldo += NovoSaldo * self.__Rendimento

      self.setSaldo(NovoSaldo)

    def depositar(self, valor:float):
        self.__Valor = valor
        self.setSaldo(self.getSaldo() + self.__Valor)
    
    def sacar(self, valor:float):
        self.__Valor = valor

        if self.__Valor > self.getSaldo():
            print("Você nâo pode sacar esse valor, por favor, tente outro")

        else:
            self.setSaldo(self.getSaldo() - self.__Valor)

    def __str__(self) -> str:
      return f"Cliente: {self.getNome()}\nConta: {self.getNum()}\nSaldo: {self.getSaldo():.2f}\nRendimento: {self.__Rendimento*100:.2f}%"

    
