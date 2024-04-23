from .ContaBancaria import ContaBancaria

class ContaEspecial(ContaBancaria):
    def __init__(self):
        self.__Limite = 0.0

    def getLimite(self)->float:
        return self.__Limite
    
    def setLimite(self, limite:float):
        self.__Limite = limite
  
    def SaqueEsp(self, valor:float):
        self.__Valor = valor
        limite = self.getSaldo()
        limite += limite * self.__Limite
        if self.__Valor > limite:            
          print("Você nâo pode sacar esse valor, por favor, tente outro!")

        else:
            NovoSaldo = self.getSaldo()
            NovoSaldo -= self.__Valor
            if NovoSaldo < 0:
              NovoSaldo = 0
              
            self.setSaldo(NovoSaldo)

    def __str__(self) -> str:
      return f"Cliente: {self.getNome()}\nConta: {self.getNum()}\nSaldo: {self.getSaldo():.2f}\nLimite: {self.__Limite*100:.2f}%"
        
