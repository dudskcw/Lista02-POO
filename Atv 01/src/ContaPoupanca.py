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

    def __str__(self) -> str:
      return f"Cliente: {self.getNome()}\nConta: {self.getNum()}\nSaldo: {self.getSaldo():.2f}\nRendimento: {self.__Rendimento*100:.2f}%"

    
